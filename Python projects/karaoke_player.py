#!/usr/bin/env python3
"""
karaoke_player.py
Play a song and print synced lyrics in your terminal (like that Instagram reel).
Usage:
    python karaoke_player.py path/to/song.mp3 path/to/lyrics.lrc
Requirements:
    pip install pygame colorama
Notes:
    - Uses standard LRC timestamp format [mm:ss.xx] or [mm:ss].
    - Works on Windows, macOS, Linux.
"""
import sys
import time
import threading
import warnings
warnings.filterwarnings("ignore")

from pathlib import Path

try:
    import pygame
except ImportError:
    print("Missing dependency: pygame. Install with: pip install pygame")
    sys.exit(1)

try:
    from colorama import init as colorama_init, Fore, Style
except ImportError:
    print("Missing dependency: colorama. Install with: pip install colorama")
    sys.exit(1)


def parse_lrc(lrc_path):
    """
    Parse a .lrc file into a sorted list of (timestamp_seconds, text).
    Supports lines like:
      [00:12.34] Some lyric line
      [01:02] Next line (no hundredths)
    Lines may have multiple tags, e.g. [00:10.00][00:20.00] chorus
    """
    entries = []
    for raw in Path(lrc_path).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        parts = []
        text = line
        # collect all [mm:ss.xx] tags
        idx = 0
        while True:
            if "[" in text and "]" in text and text.index("[") < text.index("]"):
                start = text.index("[")
                end = text.index("]")
                tag = text[start + 1 : end]
                parts.append(tag)
                text = text[:start] + text[end + 1 :]
            else:
                break
        text = text.strip()
        for tag in parts:
            try:
                if ":" not in tag:
                    continue
                mm, ss = tag.split(":", 1)
                if "." in ss:
                    sec, hundredths = ss.split(".", 1)
                    seconds = int(mm) * 60 + int(sec) + int(hundredths[:2]) / 100.0
                else:
                    seconds = int(mm) * 60 + int(ss)
                entries.append((seconds, text))
            except Exception:
                # ignore weird tags like [ar:], [ti:], etc.
                continue
    entries.sort(key=lambda x: x[0])
    return entries


def print_synced_lyrics(lyrics, start_time, stop_event):
    """
    Print each lyric line at the scheduled time relative to start_time.
    """
    i = 0
    n = len(lyrics)
    colorama_init()
    last_printed = None
    while i < n and not stop_event.is_set():
        now = time.time() - start_time
        ts, text = lyrics[i]
        delay = ts - now
        if delay > 0:
            # sleep in tiny chunks so we can react to stop_event
            end_wait = time.time() + delay
            while time.time() < end_wait and not stop_event.is_set():
                time.sleep(0.01)
            if stop_event.is_set():
                break

        # Erase previous line hint (optional)
        if last_printed is not None:
            # Print previous line in dim color for context
            print(Style.DIM + last_printed + Style.RESET_ALL)

        # Print the current line emphasized
        print(Style.BRIGHT + Fore.CYAN + text + Style.RESET_ALL)
        last_printed = text
        i += 1


def main():
    if len(sys.argv) < 3:
        # Default files if no arguments are given
        song_path = Path("Twinkle Twinkle Little Star.mp3")
        lrc_path = Path("lyrics_example.lrc")
    else:
        song_path = Path(sys.argv[1]).expanduser()
        lrc_path = Path(sys.argv[2]).expanduser()


    if not song_path.exists():
        print(f"Song not found: {song_path}")
        sys.exit(1)
    if not lrc_path.exists():
        print(f"LRC not found: {lrc_path}")
        sys.exit(1)

    lyrics = parse_lrc(lrc_path)
    if not lyrics:
        print("No timestamped lyrics found in the LRC file.")
        sys.exit(1)

    # Init audio
    pygame.mixer.init()
    pygame.mixer.music.load(str(song_path))

    stop_event = threading.Event()

    # Start playback
    pygame.mixer.music.play()
    start_time = time.time()

    # Lyrics thread
    t = threading.Thread(target=print_synced_lyrics, args=(lyrics, start_time, stop_event))
    t.daemon = True
    t.start()

    try:
        # Keep the main thread alive while music is playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        stop_event.set()
        pygame.mixer.music.stop()
        pygame.mixer.quit()


if __name__ == "__main__":
    main()
