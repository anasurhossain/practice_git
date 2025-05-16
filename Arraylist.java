import java.util.ArrayList;
import java.util.Collections;
public class Arraylist {
    public static void main(String[] args){
        ArrayList<Integer>list = new ArrayList<>();

        list.add(4);
        list.add(2);
        list.add(1);
        list.add(9);

        //list.remove(0);
        //list.set(0, 1);
       // System.out.println(list.get(1));
       //System.out.println(list.size());

       Collections.sort(list);
       System.out.println(list);



    }

}
