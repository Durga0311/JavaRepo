class SavingAccount{
    private static double annual_interest;
    private double saving_balance;
    SavingAccount(){
    saving_balance=0;
    annual_interest=0;    
    }
    SavingAccount(double balance){
        saving_balance=balance;
        annual_interest=0;
    }
    public void calculateMonthlyInterest(){
        System.out.println("current balance:"+saving_balance);
        double monthly_interest;
        monthly_interest=annual_interest*saving_balance/12;
        saving_balance=monthly_interest+saving_balance;
        System.out.println("new balance:"+saving_balance );
    }
    double getBalance(){
        return saving_balance;
    }
    
    public  void modifyInterestRate(double new_interest) {  
    annual_interest=new_interest;
   }
}
class NewSavings{
    public static void main(String args[]){
        SavingAccount saver1=new SavingAccount(2000);
        SavingAccount saver2=new SavingAccount(3000);
        saver1.modifyInterestRate(0.04);
        saver1.calculateMonthlyInterest();
        saver2.modifyInterestRate(0.04);
        saver2.calculateMonthlyInterest();
        System.out.println("after changing annual interset to 5%");
        saver1.modifyInterestRate(0.05);
        saver1.calculateMonthlyInterest();
        saver2.modifyInterestRate(0.05);
        saver2.calculateMonthlyInterest();
         
        
    }
}