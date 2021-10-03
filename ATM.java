import java.util.*;

import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int val=sc.nextInt();
		float balance=sc.nextFloat();
		if(val>balance)
		System.out.println(balance);
		else if(val%5!=0)
		{
		    System.out.println(balance);
		}
		else if((val+0.50)>balance)
		{
		    System.out.println(balance);
		}
		else
		{
		    balance=balance-val-0.50f;
		    System.out.println(balance);
		}
	}	
}
