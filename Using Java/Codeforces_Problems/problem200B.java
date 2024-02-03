package Codeforces_Problems;

import java.util.Scanner;

public class problem200B {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num,sum=0;
        num = input.nextInt();
        int[] value = new int[num];
        for (int i = 0; i < num; i++) {
            value[i] = input.nextInt();
        }
        for (int i = 0; i < num; i++) {
           sum +=value[i];
        }
         double result = sum/num;
        System.out.println(result);

    }
}
