class NewThread implements Runnable{
    Thread t;
    NewThread(){
        t=new Thread(this,"Demo Thread");
        System.out.println("child thread"+t);
    }
    public void run(){
        try{
            for(int i=5;i>0;i--){
                System.out.println("chid thread"+i);
                Thread.sleep(500);
            }
        }
        catch (InterruptedException e)
        {
            System.out.println("chid thread interrupted");
        }
        System.out.println("exiting chid thread");
    }
}
class DemoThread{
    public static void main(String args[]){
    NewThread nt=new NewThread();
    nt.t.start();
    try{
            for(int i=5;i>0;i--){
                System.out.println("main thread"+i);
                Thread.sleep(1000);
            }
        }
        catch(InterruptedException e)
        {
            System.out.println("main thread interrupted");
        }
        System.out.println("exiting main thread");
    }
}