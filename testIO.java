 import java.util.Scanner;
 public class testIO {
 public static void main(String[] args) {
  //Open the standard input
  Scanner input = new Scanner(System.in);
  
  System.out.print("Input a word: ");
  String aword = input.next();
  System.out.println("The word is [" + aword + "]");
  
  System.out.print("Input an integer: ");
  int anint = input.nextInt();
  System.out.println("An integer is [" + anint + "]");
  
  System.out.print("Input a double: ");
  double adouble = input.nextDouble();
  System.out.println("A double is [" + adouble + "]");
  
  //Skip the new line from the last input double
  input.nextLine();
  
  System.out.print("Input a line: ");
  String aline = input.nextLine();
  System.out.println("The line is [" + aline + "]");
  
  //Close the input
  input.close();
 }
 }