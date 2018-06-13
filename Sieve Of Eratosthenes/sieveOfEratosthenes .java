import java.util.Scanner;
//Finding primes with Sieve Of Eratosthenes 
//Mutluhan Boz 16.01.18
public class Primes {
	static void sieveOfEratosthenes(int n) {
		boolean prime[] = new boolean [n+1];		
		for(int i=0; i<n; i++) {
			prime[i] = true ;
		}
		for(int i=2; i*i<=n; i++) {
			if(prime[i] == true) {
				for(int j=i*2; j<=n; j+=i) {
					prime[j] = false;
				}
			}
		}
		for(int i=2; i<n; i++) {
			if(prime[i] == true) {
			System.out.printf("\n%d",i);
			}
		}	
	}
	
	public static void main(String[] args) {
		Scanner read = new Scanner(System.in);
		System.out.print("Sayi Giriniz : ");
		int n = read.nextInt();
		sieveOfEratosthenes(n);
	
	}

}
