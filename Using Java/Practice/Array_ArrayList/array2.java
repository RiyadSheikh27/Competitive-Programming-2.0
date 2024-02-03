package Array_ArrayList;

import java.util.Arrays;

public class array2 {
    public static void main(String[] args) {
        int[] number = { 10, -4, 4, 9, 12, 16 };
        Arrays.sort(number);
        System.out.print("Ascending: ");
        for (int i = 0; i < 6; i++) {
            System.out.print(" " + number[i]);
        }
        System.out.println();
        System.out.print("Descending: ");
        for (int i = 5; i >= 0; i--) {
            System.out.print(" " + number[i]);
        }

    }
}