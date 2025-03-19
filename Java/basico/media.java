package basico;
import java.util.Scanner;

public class media{
    public static void main(String[] args){
        Scanner entrada=new Scanner(System.in);
        System.out.print("Digite a primeira nota: ");
        float num1 = entrada.nextFloat();
        System.out.print("Digite a segunda nota: ");
        float num2 = entrada.nextFloat();
        System.out.print("Digite a terceira nota: ");
        float num3 = entrada.nextFloat();

        float media = (num1+num2+num3)/3;
        System.out.println("A média das notas é: "+media);
        entrada.close();
        if (media>=6){
            System.out.print("Aprovado! Parabéns.");
        }else if (media<4){
            System.out.print("Reprovado.");
        }else{
            System.out.print("Você está de recuperação final. Boa sorte.");
        }
        }
    }