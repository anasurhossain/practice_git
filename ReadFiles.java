
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class ReadFiles {
    public static void main(String[] args) {
        
        String filePath = "C:\\Users\\lavin\\OneDrive\\Desktop\\test.txt";

        try(BufferedReader reader = new BufferedReader(new FileReader(filePath))){
            String line;
            while((line = reader.readLine()) != null){
                System.out.println(line);
            }
        }
        catch(FileNotFoundException b){
            System.out.println("Could not found the file location !");
        }
        catch(IOException b){
            System.out.println("Something went wrong !!");
        }
    }
}
