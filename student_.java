import java.util.ArrayList;
import java.util.Scanner;

//Copied from chatgpt

class Student {
    private String name;
    private int age;
    private String course;

    public Student(String name, int age, String course) {
        this.name = name;
        this.age = age;
        this.course = course;
    }

    public String getName() {
        return name;
    }

    public String toString() {
        return name + " (Age: " + age + ", Course: " + course + ")";
    }
}

public class student_ {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Student> students = new ArrayList<>();

        while (true) {
            System.out.println("\n--- Student Manager ---");
            System.out.println("1. Add Student");
            System.out.println("2. List Students");
            System.out.println("3. Search by Name");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");

            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("Enter name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter age: ");
                    int age = Integer.parseInt(scanner.nextLine());
                    System.out.print("Enter course: ");
                    String course = scanner.nextLine();
                    students.add(new Student(name, age, course));
                    System.out.println("Student added!");
                    break;
                case "2":
                    if (students.isEmpty()) {
                        System.out.println("No students found.");
                    } else {
                        System.out.println("List of students:");
                        for (Student s : students) {
                            System.out.println("- " + s);
                        }
                    }
                    break;
                case "3":
                    System.out.print("Enter name to search: ");
                    String searchName = scanner.nextLine();
                    boolean found = false;
                    for (Student s : students) {
                        if (s.getName().equalsIgnoreCase(searchName)) {
                            System.out.println("Found: " + s);
                            found = true;
                        }
                    }
                    if (!found) {
                        System.out.println("No student found with that name.");
                    }
                    break;
                case "4":
                    System.out.println("Exiting program.");
                    return;
                default:
                    System.out.println("Invalid option. Try again.");
            }
        }
    }
}
