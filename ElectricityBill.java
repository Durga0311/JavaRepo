import java.util.Scanner;
class ElectricityBill{
Scanner s=new Scanner(System.in);
String customer_number;
String customer_name;
double previous_month_reading;
double current_month_reading;
double amount;
String type;
ElectricityBill(){
String customer_number="";
String customer_name="";
double previous_month_reading=0.0;
double current_month_reading=0.0;
}
void getBillDetail(){
System.out.println("enter customer number:");
customer_number=s.next();
System.out.println("enter customer name:");
customer_name=s.next();
System.out.println("enter previous month reading:");
previous_month_reading=s.nextDouble();
System.out.println("enter current  month reading:");
current_month_reading=s.nextDouble();
System.out.println("enter type:");
type=s.next();
}
void calculate_amount(){
double unit;
unit=current_month_reading-previous_month_reading;
if(type=="d")
{
if(unit<=100)
amount=unit*1;
else if(unit<=200)
amount=100+(unit-100)*2.50;
else if(unit<=500)
amount=100+250+(unit-200)*4;
else
amount=unit*6;
}
else
{
if(unit<=100)
amount=unit*2;
else if(unit<=200)
amount=100+(unit-100)*4.50;
else if(unit<=500)
amount=100+450+(unit-200)*6;
else
amount=unit*7;
}
}
void showbill(){
System.out.println("customer number:"+customer_number);
System.out.println("customer name:"+customer_name);
if (type.equals("d"))
System.out.println("type=domestic");
else
System.out.println("type=commercial");
System.out.println("prevoius month reading:"+previous_month_reading);
System.out.println("current month reading:"+current_month_reading);
System.out.println("amount:"+amount);
}
}
class Electricity{
public static void main(String args[]){
ElectricityBill e=new ElectricityBill();
e.getBillDetail();
e.calculate_amount();
e.showbill();
}
}