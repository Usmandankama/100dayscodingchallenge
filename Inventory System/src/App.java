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
        blocks,
        woodamt,
        rodsamt,
        cementamt,
        blocksamt,
        sellamt,
        rem,
        buildOption,
        option;
        String answer;

    // INSTANCES
        Scanner scan = new Scanner(System.in);
        // Random random = new Random();

    // EXECUTION
    // using a try method for proper handling of errors
        try {
            System.out.print("Input name: ");
            scan.next();
            System.out.println("-------------------------------------------------------------------");
            System.out.println("1.Self Contain---50x woods, 50x rod, 50x cement, 50x blocks---$2500");
            System.out.println("2.Bungalow---120x woods, 70x rod, 200x cement, 50x blocks---$5000");
            System.out.println("3.Palace---500x woods, 270x rod, 580x cement, 50x blocks---$15000");
            System.out.println("-------------------------------------------------------------------");
    
            System.out.print("Input Budget: ");
            money = scan.nextInt();
    
            System.out.print("Enter no of wood: ");
            wood = scan.nextInt();
            
            System.out.print("Enter no of rods: ");
            rods = scan.nextInt();
    
            System.out.print("Enter no of cement: ");
            cement = scan.nextInt();
    
            System.out.print("Enter no of blocks: ");
            blocks = scan.nextInt();   

            System.out.println("You have "+ wood + "xwood,"+  rods+ "xrods,"+ cement + "xcement," + blocks + "xBlocks");
            System.out.println("1.Build\n2.Sell\n3.Buy");
            option = scan.nextInt();
            if (option ==1) {
                System.out.println("1.Self Contain---50x woods, 50x rod, 50x cement, 50x blocks---$2500");
                System.out.println("2.Bungalow---120x woods, 70x rod, 200x cement, 50x blocks---$5000");
                System.out.println("3.Palace---500x woods, 270x rod, 580x cement, 50x blocks---$15000");
                System.out.print("Which do you want to build: ");
                buildOption = scan.nextInt();
                if (buildOption == 1) {
                    System.out.println("You chose the option self contain");
                    System.out.println("You have "+ wood + "xwood,"+  rods+ "xrods,"+ cement + "xcement," + blocks + "xBlocks");
                    // this is to check if the available resources are enough for the particular option selected
                    if (wood<50 || rods < 50 || cement < 50) {
                        System.out.println("Insufficient resources buy more to build a self contain");
                    }else if(money<2500){
                        System.out.println("Insufficient funds");
                        rem = 2500 - money;
                        System.out.println("You need $"+rem);
                    }else{
                        money -=2500;
                        System.out.println("Self Contain built sucessfuly");
                        System.out.println("You have $"+ money +" left");
                        System.out.println("Do you want to build another? ");
                        answer = scan.next().toLowerCase();
                        while (answer == "yes") {
                            System.out.println("You chose the option self contain");
                            System.out.println("You have "+ wood + "xwood,"+  rods+ "xrods,"+ cement + "xcement," + blocks + "xBlocks");
                            if (wood<50 || rods < 50 || cement < 50) {
                                System.out.println("Insufficient resources buy more to build a self contain");
                            }else if(money<2500){
                                System.out.println("Insufficient funds");
                                rem = 2500 - money;
                                System.out.println("You need $"+rem);
                            }else{
                                money -=2500;
                                System.out.println("Self Contain built sucessfuly");
                                System.out.println("You have $"+ money +" left");
                            }
                        }
                    }
                }
                else if (buildOption == 2) {
                    System.out.println("You chose the option Bungalow");
                    System.out.println("You have "+ wood + "xwood,"+  rods+ "xrods,"+ cement + "xcement," + blocks + "xBlocks");
                    if (wood<120 || rods < 70 || cement < 200) {
                        System.out.println("Insufficient resources buy more to build a self contain");
                    }else if(money<5000){
                        System.out.println("Insufficient funds");
                        rem = 5000 - money;
                        System.out.println("You need $"+rem);
                    }else{
                        System.out.println("Bungalow built sucessfuly");
                    }
                } 
                else if (buildOption == 3) {
                    System.out.println("You chose the option Palace");
                    System.out.println("You have "+ wood + "xwood,"+  rods+ "xrods,"+ cement + "xcement," + blocks + "xBlocks");
                    if (wood<500 || rods < 270 || cement < 580) {
                        System.out.println("Insufficient resources buy more to build a self contain");
                    }else if(money<15000){
                        System.out.println("Insufficient funds");
                        rem = 15000 - money;
                        System.out.println("You need $"+rem);
                    }
                    else{
                        System.out.println("Palace built sucessfuly");
                    }
                } 
            }
            else if (option == 2) {
                System.out.println("You have $"+money);
                System.out.print("Enter no of wood to sell: ");
                woodamt = scan.nextInt();
                
                System.out.print("Enter no of rods to sell: ");
                rodsamt = scan.nextInt();
        
                System.out.print("Enter no of cement to sell: ");
                cementamt = scan.nextInt();
        
                System.out.print("Enter no of blocks to sell: ");
                blocksamt = scan.nextInt();
    
                sellamt = woodamt+blocksamt+cementamt+rodsamt;
                money= +sellamt;
                System.out.println("$"+money);
            }
            else if (option == 3) {
                System.out.println("You have $"+money);
                System.out.print("Enter no of wood to buy: ");
                woodamt = scan.nextInt();
                
                System.out.print("Enter no of rods to buy: ");
                rodsamt = scan.nextInt();
        
                System.out.print("Enter no of cement to buy: ");
                cementamt = scan.nextInt();
        
                System.out.print("Enter no of blocks to buy: ");
                blocksamt = scan.nextInt();
    
                sellamt = woodamt+blocksamt+cementamt+rodsamt;
                money= -sellamt;
                System.out.println("$"+money);
            }
        } catch (InputMismatchException e) {
            System.out.println("You cannot enter letters in place of numbers and vice versa");
        }
        scan.close();   
    }      
}