import java.util.Scanner;

public class weight_convertion{
    public static void main(String[] args){
        //WEIGHT CONVERTER

        Scanner scanner = new Scanner(System.in);

        //Declare variables
        double weight;
        double newWeight;
        int choice;

        //welcome message

        System.out.println("Weight conversion program");
        System.out.println(" 1: convert lbs to kgs");
        System.out.println(" 2: convert kgs to lbs");

        //Prompt for user choice

        System.out.print("Choose an option: ");
        choice = scanner.nextInt();

        //option 1 convert lbs to kgs

        if(choice == 1){
            System.out.print("Enter the weights in lbs : ");
            weight=scanner.nextDouble();
            newWeight = weight * 0.453592;
            System.out.printf("The new weight in kgs is : %.2f",newWeight);
        }
        //option 2 convert kgs to lbs
        else if(choice == 2){
            System.out.print("Enter the weights in kgs : ");
            weight=scanner.nextDouble();
            newWeight = weight * 2.20462;
            System.out.printf("The new weight in lbs is : %.2f",newWeight);
        }

        //else print not a valid choice

        else{
            System.out.println("Your option is invalid !");
        }

        scanner.close();
    }
}