import java.util.Random;
import java.util.Scanner;

public class guessNumber{
    public static void main(String[] args) {
        //guess the number game
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        int guess;
        int attempt=0;
        int min=1;
        int max=100;
        int randomNumber = random.nextInt(min, max+1);


        System.out.println("Number guessing game");
        System.out.printf("Guess a number between %d - %d ",min,max);

        do{
            System.out.print("Guess a number : ");
            guess= scanner.nextInt();
            attempt++;

            if(guess < randomNumber){
                System.out.println("TOO Low ! Try again");
            }
            else if(guess>randomNumber){
                System.out.println("Too High! Try again.");
            }
            else{
                System.out.println("Correct. You entered the right number and it is "+randomNumber);
                System.out.println("#Number of attempt is "+ attempt);
            }
        }while(guess != randomNumber);



        scanner.close();
    }
}