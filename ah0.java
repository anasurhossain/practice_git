import java.util.Scanner;

public class ah0{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name;
        int age;
        double gpa;
        System.out.print("Enter your name: ");
        name=scanner.nextLine();
        System.out.print("Enter your age: ");
        age=scanner.nextInt();
        System.out.print("What is your gpa🤐 : ");
        gpa=scanner.nextDouble();

        System.out.print("Hi, "+name +"your age is "+age+". But you have to improve your "+gpa+" this gpa.");

        scanner.close();
    }
}