import java.util.Scanner;
public class polymorphism {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);

        Animal1 animal;
        System.out.print("Would you like a cat(1) or dog(2): ");
        int choice=scanner.nextInt();

        if(choice==1){
            animal=new Dog1();
            animal.speak();
        }
        else if(choice==2){
        animal=new Cat1();
        animal.speak();
        }
    }
}
