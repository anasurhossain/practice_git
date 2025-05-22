
import java.util.Scanner;

public class New {
    public static void Main (String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("What is your name: ");
        String name = scanner.next();
        System.out.println(name);

        scanner.close();

    }
}
