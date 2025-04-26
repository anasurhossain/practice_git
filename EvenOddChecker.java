// This is a simple Java program where I check if a number is even or odd

import java.util.Scanner; // I import Scanner to take user input

public class EvenOddChecker {

    // This is my main method. The program starts running from here
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in); // Create a Scanner object

        System.out.print("Enter a number: ");
        int number = sc.nextInt(); // Take an integer input from the user

        // Call a method to check even or odd
        checkEvenOdd(number);
        
        sc.close(); // Always close the scanner
    }

    // This is a method to check and print if a number is even or odd
    public static void checkEvenOdd(int num) {
        if (num % 2 == 0) {
            System.out.println(num + " is Even.");
        } else {
            System.out.println(num + " is Odd.");
        }
    }
}
