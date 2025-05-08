public class studentOob{
    public static void main(String[] args) {
        
        Student student1= new Student("Bob", 30, 2.5);
        Student student2 = new Student("marly", 25, 3.0);

        System.out.println(student1.name);
        System.out.println(student1.age);
        System.out.println(student1.gpa);
        System.out.println(student1.isStudent);
        student1.study();

        System.out.println(student2.name);
        System.out.println(student2.age);
        System.out.println(student2.gpa);
        System.out.println(student2.isStudent);
        student2.study();
    

    }
}