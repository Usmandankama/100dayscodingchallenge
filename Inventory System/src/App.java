/** This is a constrution system
    user should store resources
    gather them
    sell them 
    buy them
    craft or build something good
*/

// IMPORTS
// import java.util.Random;
import java.util.InputMismatchException;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
    // VARIABLES
        int money,
        wood,
        rods,
        cement,
        option;
        String answer;

    // INSTANCES
        Scanner scan = new Scanner(System.in);
        // Random random = new Random();

    // EXECUTION
    // using a try method for proper handling of errors
        try {
            System.out.println("Welcome to DKM CONSTRUCTIONS INC");
            System.out.println("-------------------------------------------------------------------");
            System.out.println("1.Self Contain---50x woods, 50x rod, 50x cement---$2500");
            System.out.println("2.Bungalow---120x woods, 70x rod, 200x cement---$5000");
            System.out.println("3.Palace---500x woods, 270x rod, 580x cement---$15000");
            System.out.println("-------------------------------------------------------------------");
            System.out.print("Input name: ");
            scan.next();
            System.out.print("Input budget: ");
            money=scan.nextInt();            
            // the series of outputs below is to get to know how many resources the user has available
            System.out.print("Enter no of wood: ");
            wood = scan.nextInt();
            System.out.print("Enter no of rods: ");
            rods = scan.nextInt();
            System.out.print("Enter no of cement: ");
            cement = scan.nextInt();
            System.out.println("You have "+ wood + "xwood,"+  rods+ "xrods,"+ cement + "xcement");

            System.out.println("1.Build\n2.Sell\n3.Buy");
            option = scan.nextInt();
            if (option == 1) {
                build(wood,rods,cement,money);
            }
            else if (option == 2) {
                sell(money);
            }
            else if (option == 3) {
                buy(money);
            }   
        }
        catch (InputMismatchException e) {
            System.out.println("You cannot enter letters in place of numbers and vice versa");
        }
        catch (Exception e){
            System.out.println("Something went wrong");
        }
        scan.close();   
    }  
    // METHODS
    public static void build(int wood, int rods, int cement, int money) {
        String answer;
        int  buildOption,rem;
        Scanner scanner= new Scanner(System.in);
        System.out.println("1.Self Contain---50x woods, 50x rod, 50x cement---$2500");
        System.out.println("2.Bungalow---120x woods, 70x rod, 200x cement---$5000");
        System.out.println("3.Palace---500x woods, 270x rod, 580x cement---$15000");
        System.out.print("Which do you want to build: ");
        buildOption = scanner.nextInt();
        if (buildOption == 1) {
            if (wood<50 || rods < 50 || cement < 50) {
                System.out.println("Insufficient resources buy more to build a self contain");
            }else if(money<2500){
                System.out.println("Insufficient funds");
                rem = 2500 - money;
                System.out.println("You need $"+rem);
            }else{
                money -=2500;
                System.out.println("********************************\t"+"********************************");
                System.out.println("********************************\t"+"********************************");
                System.out.println("||||||||\t\t\t\t"+"**********");
                System.out.println("||||||||\t\t\t\t"+"**********");
                System.out.println("||||||||\t\t\t\t"+"**********");
                System.out.println("********************************\t"+"**********");
                System.out.println("********************************\t"+"**********");
                System.out.println("********************************\t"+"**********");
                System.out.println("\t\t\t||||||||\t"+"**********");
                System.out.println("\t\t\t||||||||\t"+"**********");
                System.out.println("********************************\t"+"********************************");
                System.out.println("********************************\t"+"********************************");
                System.out.println("********************************\t"+"********************************");
                System.out.println("Self Contain built sucessfuly");
                System.out.println("You have $"+ money +" left");
            }
         }else if (buildOption == 3) {
            
            System.out.println("You chose the option Palace");
            System.out.println("You have "+ wood + "xwood,"+  rods+ "xrods,"+ cement + "xcement");
            if (wood<500 || rods < 270 || cement < 580) {
                System.out.println("Insufficient resources buy more to build a self contain");
            }else if(money<15000){
                System.out.println("Insufficient funds");
                rem = 15000 - money;
                System.out.println("You need $"+rem);
            }
            else{
                System.out.println("********************************");
                System.out.println("********************************");
                System.out.println("||||||||\t\t||||||||");
                System.out.println("||||||||\t\t||||||||");
                System.out.println("||||||||\t\t||||||||");
                System.out.println("||||||||\t\t||||||||");
                System.out.println("********************************\t");
                System.out.println("********************************\t");
                System.out.println("********************************\t");
                System.out.println("||||||||");
                System.out.println("||||||||");
                System.out.println("||||||||");
                System.out.println("||||||||");
                System.out.println("Palace built sucessfuly");
                System.out.println("You have $"+ money +" left");
            }
         }
         else if (buildOption == 2) {
            System.out.println("You chose the option Bungalow");
            System.out.println("You have "+ wood + "xwood,"+  rods+ "xrods,"+ cement + "xcement");
            if (wood<120 || rods < 70 || cement < 200) {
                System.out.println("Insufficient resources buy more to build a self contain");
            }else if(money<5000){
                System.out.println("Insufficient funds");
                rem = 5000 - money;
                System.out.println("You need $"+rem);
            }else{
                System.out.println("********************************");
                System.out.println("********************************");
                System.out.println("||||||||\t\t||||||||");
                System.out.println("||||||||\t\t||||||||");
                System.out.println("||||||||\t\t||||||||");
                System.out.println("********************************\t");
                System.out.println("********************************\t");
                System.out.println("********************************\t");
                System.out.println("||||||||\t\t||||||||");
                System.out.println("||||||||\t\t||||||||");
                System.out.println("********************************");
                System.out.println("********************************");
                System.out.println("********************************");
                System.out.println("Bungalow built sucessfuly");
                System.out.println("You have $"+ money +" left");
            }
        }
        // scanner.close();
         // this is to check if the available resources are enough for the particular option selected
    }

    public static void sell(int money) {
        int rodsamt,woodamt,sellamt,cementamt;
        String answer;
        Scanner scanner= new Scanner(System.in);
        System.out.println("You have $"+money);
        System.out.print("Enter no of wood to sell: ");
        woodamt = scanner.nextInt();
        
        System.out.print("Enter no of rods to sell: ");
        rodsamt = scanner.nextInt();

        System.out.print("Enter no of cement to sell: ");
        cementamt = scanner.nextInt();

        System.out.print("Enter no of  to sell: ");

        sellamt = (woodamt+cementamt+rodsamt)*2;
        money= +sellamt;
        System.out.println("$"+money);
        }
        // scanner.close();

    public static void buy(int money) {
        String answer;
        int rodsamt,woodamt,sellamt,cementamt;
        Scanner scanner= new Scanner(System.in);
        System.out.println("You have $"+money);
        System.out.print("Enter no of wood to sell: ");
        woodamt = scanner.nextInt();
        
        System.out.print("Enter no of rods to sell: ");
        rodsamt = scanner.nextInt();

        System.out.print("Enter no of cement to sell: ");
        cementamt = scanner.nextInt();

        System.out.print("Enter no of  to sell: ");

        sellamt = (woodamt+cementamt+rodsamt)*2;
        money= -sellamt;
        System.out.println("$"+money);
        }
        // scanner.close();
    }