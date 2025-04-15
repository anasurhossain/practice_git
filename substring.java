import java.util.Scanner;

public class substring{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String email ;

        System.out.println("Enter your email !");
        email = scanner.nextLine();
        if(email.contains("@")){

            String username = email.substring(0, email.indexOf("@"));
            String domain = email.substring(email.indexOf("@"));
            System.out.println(username);
            System.out.println(domain);

        }
        else {
            System.out.println("Please provide a valid email .");
        }





        scanner.close();
    }
}