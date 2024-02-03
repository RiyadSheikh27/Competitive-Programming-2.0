package Array_ArrayList;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

import javax.swing.text.html.parser.Element;

public class arraylist2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Integer> number = new ArrayList<>();
        for (int i = 1; i <= 5; i++) {
            int elements = input.nextInt();
            System.out.print("Added Elements are " + elements);
            System.out.println();
            number.add(elements);
        }
        System.out.println();
        System.out.println(number);

        Collections.sort(number);
        System.out.println();
        System.out.print("Sorted Elemetns in Ascending are: "+number);
        Collections.sort(number, Collections.reverseOrder());
        System.out.println();
        System.out.println("Sorted Elements in Descending are: "+number);

    }
}
