import java.util.Scanner;

public class Hello{
    public static void main(String[] args){
        //Compound interest calculator.
        Scanner scanner = new Scanner(System.in);

        double principal;
        double rate;
        int time;
        int years;
        double total;

        System.out.print("Enter principal amount: ");
        principal= scanner.nextDouble();

        System.out.print("Enter the interest rate: ");
        rate= scanner.nextDouble()/100;

        System.out.print("Enter the times compounded per year: ");
        time=scanner.nextInt();

        System.out.print("Enter total year: ");
        years= scanner.nextInt();

        total=principal*Math.pow(1+rate/time, years*time);
        System.out.printf("The amount after %d year is $%,.1f",years,total);

        scanner.close();
    }
}