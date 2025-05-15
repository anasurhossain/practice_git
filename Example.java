import java.util.ArrayList;

public class Example {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();

        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Mango");

        System.out.println("First fruit: " + fruits.get(0)); // Apple
        System.out.println("Total fruits: " + fruits.size()); // 3

        fruits.set(1, "Orange"); // Replace Banana with Orange

        fruits.remove(0); // Remove Apple

        System.out.println("Now the list: " + fruits); // [Orange, Mango]
    }
}
