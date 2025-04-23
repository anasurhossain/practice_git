import java.util.Scanner;

public class operators{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String username ;

        System.out.print("Enter your user name :");
        username=scanner.nextLine();

        if (username.length() < 4 || username.length() >12) {
            System.out.println("User name must be between 4-12 characters!");
        }
        else if(username.contains(" ") || username.contains("_")){
            System.out.println("User name must not contain spaces and underscore .");

        }
        else{
            System.out.println("welcome "+ username);
        }

        scanner.close();
    } 
}