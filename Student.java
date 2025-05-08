public class Student{
    String name;
    int age;
    double gpa;
    boolean isStudent;

    Student(String name,int age,double gpa){
        this.name = name;
        this.age = age;
        this.gpa = gpa;
        this.isStudent = true;
    }

    void study(){
        System.out.println(this.name+ " is studing.");
    }
        

}