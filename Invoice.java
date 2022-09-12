class Invoice {
String number;
String description;
int quantity;
double price;
Invoice(String n,String d,int q,double p){
    this.number=n;
    this.description=d;
    this.quantity=q;
    this.price=p;
}
void setNumber(String n){
    this.number=n ;

}
String getNumber(){
    return number;
}
void setDescription(String d){
    this.description=d;
}
String getDescription(){
    return description;
}
void setQuantity(int q){
    this.quantity=q;
    if (q<0)
    quantity=0;
    
}
int getQuantity(){
    return quantity;
}
void setPrice(double p){
    this.price=p;
    if (p<0)
    price=0.0;
}
double getPrice(){
    return price;
}
double getInvoiceAmount(){
    return quantity*price;
}
}
class InvoiceTest{
    public static void main(String args[]){
        Invoice product=new Invoice("345","book",15,20.5);
        System.out.println("invoice for items sold at store"+"\n"+"product number:"+product.getNumber()+"\n"+"description:"+product.getDescription()+"\n"+"no.of items:"+product.getQuantity()+"\n"+"price per product:"+product.getPrice()+"\n"+"invoice amount:"+product.getInvoiceAmount());
    }
}

