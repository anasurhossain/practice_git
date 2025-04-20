import java.util.Scanner;

public class temp_converter{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int temp;
        double newTemp;
        String unit;

        System.out.print("Enter the temperature : ");
        temp= scanner.nextInt();

        System.out.print("Convert into C or F: ");
        unit= scanner.next().toUpperCase();

        newTemp=(unit.equals("C")) ? (temp-32) * 5/9 : (temp * 5/9)+32;

        System.out.printf("%.2f %s",newTemp,unit);

        scanner.close();
    }
}