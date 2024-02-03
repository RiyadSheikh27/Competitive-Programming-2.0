package String;
 public class string1 {
 
    public static void main(String[] args) {
        String riyad = "My name is Riyad";
        String[] array = {"Riyad","Roshni","Akash"};
        for(String x : array){
            System.out.print(x);
        }
        System.out.println();
        System.out.println(riyad.toUpperCase());
        System.out.println(riyad.toLowerCase());
        boolean ans = riyad.startsWith("My");
        System.out.println(ans);


    }
 }
