package nest4awhile;

import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author Haivan Benjamin
 */
public class Nest4AWhile 
{
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        Scanner scnr = new Scanner(System.in);
        
        Random rand = new Random();
        
        int n = scnr.nextInt();
        
        for(int i = 1; i <= n; i++)
        {
            int a = rand.nextInt(0, 1001);
            int b = rand.nextInt(0, 1001);
            
            System.out.println(a + b);
        }
    }

}
