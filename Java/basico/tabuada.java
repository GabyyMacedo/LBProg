package basico;
import java.util.Scanner;

public class tabuada {
    public static void main(String[] args){
        Scanner entrada=new Scanner(System.in);
        System.out.print("Digite um número e descubra sua tabuada: ");
        int num=entrada.nextInt();
        for(int i=1;i<=10;i++){
            System.out.println(num+"x"+i+" = "+(num*i));
        }    
        entrada.close();
    }
}
