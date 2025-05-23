import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);
        
        int numberToGuess = random.nextInt(100) + 1; // Random number between 1 and 100
        int guess = 0;
        
        System.out.println("Welcome to the Guess the Number Game!");
        System.out.println("I'm thinking of a number between 1 and 100... Can you guess it?");
        
        while (guess != numberToGuess) {
            System.out.print("Enter your guess: ");
            guess = scanner.nextInt();
            
            if (guess < numberToGuess) {
                System.out.println("Too low! Try again.");
            } else if (guess > numberToGuess) {
                System.out.println("Too high! Try again.");
            } else {
                System.out.println("Congratulations! You guessed the number!");
            }
        }
        
        scanner.close();
    }
}
