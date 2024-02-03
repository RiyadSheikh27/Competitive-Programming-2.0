package Array_ArrayList;

import java.util.ArrayList;

public class arraylist {

    public static void main(String[] args) {
        ArrayList<Integer> number = new ArrayList<>();
        number.add(10);
        number.add(20);
        number.add(2, 30);

        for(int x: number){
            System.out.print(" "+x);
        }
        System.out.println();
        System.out.println(number);
        System.out.println(number.size());

        number.set(0, 15);
        for(int x : number){
            System.out.print(" "+x);
        }

    }
}