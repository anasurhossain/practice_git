public class string_methods{
    public static void main(String[] args){
        String name = "Anasur Hossain Lavin";
        int length = name.length();
        char letter = name.charAt(3);
        int index = name.indexOf("A");
//name = name.toUpperCase();

//name = name.replace("a","i");

        System.out.println(length);
        System.out.println(letter);
        System.out.println(index);
        System.out.println(name);
        
        if(name.isEmpty()){
            System.out.println("Your name is empty");
        }
        else{
            System.out.println("Hello "+name);
        }
    }
}