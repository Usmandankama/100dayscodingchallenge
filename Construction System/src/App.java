import java.util.InputMismatchException;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        construct();
    }

    public static void construct() {
        Scanner scanner = new Scanner(System.in);
        int wood =0,cement=0,rods=0,money,cost,option;
        // Using the try and catch method to prevent unseen errors from occuring and crashing the program
        try {
            System.out.println("Welcome to D CONSTRUCTION.io");
            System.out.println("----Input an amount greater than 90k-----");
            System.out.print("Input Budget: ");
            money = scanner.nextInt();
            // below is a for loop to stop a user from inputting a budget less than 90k......cmon the business is not for poor ppl
            for(int i=0; money<90000; i++){
                System.out.println("Input an amount greater than 90k");
                System.out.print("Input Budget: ");
                money = scanner.nextInt();
            }
            //--------------------NAVIGATING THE USER TO THE MARKETPLACE-----------------------------------------
            /* 
             * this is where the user will buy the products from us
             * Each nomber of resources cost a certain amount of money which will be deducted when the user is done purchasing
             * Once his money gets low he has to add to his budget or leave the facility to comeback someday
             */
            System.out.println("-------------------MINIMUM REQUIREMENTS-----------------------");
            System.out.println("1.Self-contain 80x wood,60x cement, 40xrods-----N40000");
            System.out.println("2.Duplex 180x wood,200x cement, 88x rods-----N78200");
            System.out.println("3.Palace 456x wood,361x cement, 437x rods-----N270800");
            // -----------------------MARKETPLACE---------------------------------
            //this is to add a little delay before displaying the message below... 
            delay();
            System.out.println("------------------------------");
            System.out.println("Now that you know the requrements, lets head to the maketplace");
            //this is to add a little delay before displaying the message below... 
            delay();
            System.out.println("Welcome to the Market place");
            System.out.println("------------------------------");
            int woodamt,cementamt,rodsamt;
            System.out.print("Input no of wood to buy: ");
            wood = scanner.nextInt();
            woodamt = wood*15;
            System.out.print("Input no of cement to buy: ");
            cement = scanner.nextInt();
            cementamt = cement*50;
            System.out.print("Input no of rods to buy: ");
            rods = scanner.nextInt();
            rodsamt = rods*7;
            cost = woodamt+cementamt+rodsamt;
            money -=cost; 
            System.out.println("You have " +wood+"x wood "+cement+"x cement "+rods+"x rods");
            System.out.println("You have N"+money+" left");
            build(wood, cement, money, rods);
            restart();
            // ------------------------------------------------------------------
        } catch (InputMismatchException e) {
            System.out.println("Invalid input");
        }
    }
    // -------------------------------DELAY METHOD--------------------------------
    // the function of this method is to add a delay to the console
    public static void delay() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    // -------------------------------DELAY METHOD--------------------------------
    // -------------------------------RESOURCES CHECKER---------------------------
    // the function of this method is to check if resources meet the minimum requirments and build if so.
    public static void checker(int wood,int rods, int cement,int option,int money) {
        if (option == 1) {
            if (wood>=80 && rods>=40 && cement>=60) {
                if (money>=40000) {
                    System.out.println("You have built a Self-contain");
                    wood -=80;
                    cement -=60;
                    rods -=40; 
                    money -=40000;
                    delay();
                    System.out.println("--------------------------------------------------------");
                    System.out.println("You have " +wood+"x wood "+cement+"x cement "+rods+"x rods");
                    System.out.println("You have N"+money+" left");
                    System.out.println("--------------------------------------------------------");
                    buildAgain(wood, cement, money, rods);

                }else{
                    addMore(money);
                }
            }else{
                addMoreResources(money, wood, cement, rods);
            }
        } 
        if(option == 2){
            if (wood>=180 && rods>=88 && cement>=200 ) {
                if (money>=78200) {
                    System.out.println("You have built a Duplex");
                    wood -=180;
                    cement -=200;
                    rods -=88; 
                    money -=78200;
                    delay();
                    System.out.println("--------------------------------------------------------");
                    System.out.println("You have " +wood+"x wood "+cement+"x cement "+rods+"x rods");
                    System.out.println("You have N"+money+" left");
                    System.out.println("--------------------------------------------------------");
                    buildAgain(wood, cement, money, rods);
                }else {
                    addMore(money);
                }
            }else{
                addMoreResources(money, wood, cement, rods);
            }
        }
        if(option == 3){
            if (wood>=456 && rods>=361 && cement>=437 ) {
                if (money>=270800) {
                    System.out.println("You have built a Palace");
                    wood -=456;
                    cement -=361;
                    rods -=437; 
                    money -=270800;
                    delay();
                    System.out.println("--------------------------------------------------------");
                    System.out.println("You have " +wood+"x wood "+cement+"x cement "+rods+"x rods");
                    System.out.println("You have N"+money+" left");
                    System.out.println("--------------------------------------------------------");
                    buildAgain(wood, cement, money, rods);
                } else {
                    addMore(money);
                }
            }else {
               addMoreResources(money, wood, cement, rods);
            }
        }
    }
    // -------------------------------RESOURCES CHECKER---------------------------
    // -----------------------------ADD MORE RESOURCES METHOD---------------------
        public static void addMoreResources(int money,int wood,int cement,int rods) {
            Scanner scanner =new Scanner(System.in);
            int woodAdded,cementAdded,rodsAdded,woodamt,cementamt,rodsamt,cost;
            System.out.println("Insufficient resources");
            System.out.print("Input no of wood to buy: ");
            woodAdded = scanner.nextInt();
            woodamt = woodAdded*15;
            System.out.print("Input no of cement to buy: ");
            cementAdded = scanner.nextInt();
            cementamt = cementAdded*50;
            System.out.print("Input no of rods to buy: ");
            rodsAdded = scanner.nextInt();
            rodsamt = rodsAdded*7;
            cost = woodamt+cementamt+rodsamt;
            money -=cost; 

            delay();
            System.out.println("--------------------------------------------------------");
            System.out.println("You have " +wood+"x wood "+cement+"x cement "+rods+"x rods");
            System.out.println("You have N"+money+" left");
            System.out.println("--------------------------------------------------------");
            }
    // ----------------------------ADD MORE RESOURCES METHOD----------------------
    // -------------------------------ADD MORE METHOD-----------------------------
    public static void addMore(int money) {
        String answer;
        int moneyAdded;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Insufficient funds");
        System.out.print("Do you wish to add more yes/no: ");
        answer = scanner.next().toLowerCase();
        if (answer.equals("yes")) {
            System.out.print("Input Money: ");
            moneyAdded = scanner.nextInt();
            money +=moneyAdded;
        }
        else{
            System.out.println("Byeee!!!");
        }
    }
    // -------------------------------ADD MORE METHOD-----------------------------
    // -------------------------------RESTART METHOD------------------------------
    public static void restart() {
        String option;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Want to try again yes/no: ");
        option = scanner.next().toLowerCase();
        while (option.equals("yes")) {
            construct();
            break;
        }
    }
    // -------------------------------RESTART METHOD------------------------------
    // -------------------------------BUILD AGAIN METHOD--------------------------
    public static void buildAgain(int wood,int cement,int money,int rods) {
        String option;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Want to try again yes/no: ");
        option = scanner.next().toLowerCase();
        while (option.equals("yes")) {
            build(wood, cement, money, rods);
            break;
        }
    }
    // -------------------------------BUID AGAIN METHOD---------------------------
    // -------------------------------BUILD  METHOD-------------------------------
    public static void build(int wood,int cement,int money,int rods) {
        int option;
        Scanner scanner = new Scanner(System.in);
        System.out.println("We have enough resources lets build");
        System.out.println("1.Self-contain 80x wood,60x cement, 40xrods-----N40000");
        System.out.println("2.Duplex 180x wood,200x cement, 88x rods-----N78200");
        System.out.println("3.Palace 456x wood,361x cement, 437x rods-----N270800");
        System.out.print("Select what to build: ");
        option = scanner.nextInt();
        checker(wood, rods, cement, option, money);
    }
}
    // -------------------------------BUILD  METHOD-------------------------------