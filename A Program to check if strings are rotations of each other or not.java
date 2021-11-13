import java.util.*;
public class Main
{
	public static void main(String[] args) {
		String str1;
		String str2;
		Scanner sc=new Scanner(System.in);
		str1=sc.nextLine();
		str2=sc.nextLine();
		String temp=str1+str1;
		if(str1.length()==str2.length() && temp.indexOf(str2)!=-1)
		{
		    System.out.print("Yes");
		}
		else
		{
		    System.out.print("No");
		}
	}
}
