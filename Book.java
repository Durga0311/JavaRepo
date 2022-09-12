public class Book { 
 String BookName = ""; 
int ISBN = 0; 
 String AuthorName = ""; 
 String Publisher = ""; 
 Book(String name, int isbn,String author,String publisher){ 
 BookName = name; 
 ISBN = isbn; 
 AuthorName = author; 
 Publisher = publisher; 
 } 
 
public String getBookName() { 
 return BookName; 
 } 
public void setBookName(String bookName) { 
 BookName = bookName; 
 } 
public int getISBN() { 
 return ISBN; 
 } 
public void setISBN(int iSBN) { 
 ISBN = iSBN; 
 } 
public String getAuthorName() { 
 return AuthorName; 
 } 
public void setAuthorName(String authorName) { 
 AuthorName = authorName; 
 } 
public String getPublisher() { 
 return Publisher; 
 } 
public void setPublisher(String publisher) { 
 Publisher = publisher; 
 } 
 String getBookInfo() { 
 return "First Name : "+BookName+"\nISBN :"+ISBN+"\nAuthor Name : 
"+AuthorName+"\nPublisher : "+Publisher+"\n"; 
 } 
 
} 
import java.util.Scanner; 
public class BookTest { 
public static void main(String[] args) { 
 Scanner var = new Scanner(System.in); 
 Book B[] = new Book[30]; 
 System.out.println("Enter Book Name : "); 
 String name = var.nextLine(); 
 
 System.out.println("Enter ISBN : "); 
 int isbn = var.nextInt(); 
 var.nextLine(); 
 
 System.out.println("Enter Author Name : "); 
 String authorName = var.nextLine(); 
 
 System.out.println("Enter Publisher : "); 
 String publisher = var.nextLine(); 
 
 B[0] = new Book(name, isbn, authorName, publisher); 
 System.out.println("Description \n" + B[0].getBookInfo()); 
 var.close(); 
 }
}