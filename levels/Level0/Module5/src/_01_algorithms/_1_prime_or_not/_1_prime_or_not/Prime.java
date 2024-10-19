package _01_algorithms._1_prime_or_not._1_prime_or_not;
import javax.swing.JOptionPane;

public class Prime {

    public static Boolean go(){
        long num = Long.parseLong(JOptionPane.showInputDialog("Pick a number"));
        for(long i = 2; i < num/2; i+=2){
            if(num % i == 0){
                System.out.println(Long.toString(num) + " is not prime");
                return false;
            }
        }
        System.out.println(Long.toString(num) + " is prime");
        return true;
    }

    public static void main(String[] args) {
		new Prime();
        Prime.go();
	}

    
}

//1367161723
//2724711961