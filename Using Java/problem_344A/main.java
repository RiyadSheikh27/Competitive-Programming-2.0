package problem_344A;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine()); //number of magnets 
        int cnt = 1;
        
        char curr = scanner.nextLine().charAt(1);

        for(int i = 1; i<n ; i++)
        {
            char compare = scanner.nextLine().charAt(1); 
            if(curr != compare){
                cnt+=1;
                curr = compare;
            }
        }
        System.out.println(cnt);
    }
}