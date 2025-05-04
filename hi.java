import java.util.Scanner;

public class hi {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  // Create Scanner object for input

        System.out.print("Enter your name: ");     // Prompt user
        String name = scanner.nextLine();          // Read user input

        System.out.println("Hello, " + name + "! Welcome to Java.");  // Greet user

        scanner.close();  // Close the scanner
    }
}
