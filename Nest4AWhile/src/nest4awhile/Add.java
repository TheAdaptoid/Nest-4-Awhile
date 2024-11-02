package nest4awhile;

import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author Haivan Benjamin
 */
public class Add 
{
    public Add()
    {
        Scanner scnr = new Scanner(System.in);
        
        Random rand = new Random();
        
        int n = scnr.nextInt();
        
        int a;
        int b;
        
        for(int i = 1; i <= n; i++)
        {
            String[] line = scnr.next().split("\\+");
            
            a = Integer.parseInt(line[0]);
            b = Integer.parseInt(line[1]);
            
            System.out.println(a + b);
        }
    }
}
