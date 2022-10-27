import java.util.InputMismatchException;
import java.util.Scanner;
public class InputMismatchExample{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        try{
        System.out.println("enter any number:");
        int a = sc.nextInt();
        System.out.println((a*a));
    }
    catch(InputMismatchException ex){
        System.out.println(ex);
    }
}
}
