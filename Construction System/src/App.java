import java.util.InputMismatchException;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        int
        wood =0,
        cement=0,
        rods=0,
        money;
        String answer;
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Welcome to D Construction.io");
            System.out.print("Input name: ");
            scanner.next();
            System.out.println("----Input an amount greater than 80k-----");
            System.out.print("Input Budget: ");
            money = scanner.nextInt();
            for(int i=0; money<80000; i++){
                System.out.print("Input Budget: ");
                money = scanner.nextInt();
            }
            purchase(wood, cement, rods, money);
            build(money, wood, cement, rods);
            System.out.println("Want to build again?y/n: ");
            answer =scanner.next();
            switch (answer) {
                case "y":
                    build(money, wood, cement, rods);
                    break;
                case "n":
                    System.out.println("Byee!!!");
                    break;
                default:
                    break;
            }
        } catch (InputMismatchException e) {
            System.out.println("Invalid input.");
        }
        catch(Exception e){
            System.out.println("An error occured");
        }
            scanner.close();
    }

    public static void build(int money,int wood,int cement,int rods) {
        int option;
        Scanner scanner = new Scanner(System.in);
        System.out.println("We have enough resources lets build");
        System.out.println("1.Self-contain 80x wood,60x cement, 40xrods-----N40000");
        System.out.println("2.Duplex 180x wood,200x cement, 88x rods-----N78200");
        System.out.println("3.Palace 456x wood,361x cement, 437x rods-----N270800");
        System.out.print("Select what to build: ");
        option = scanner.nextInt();
        if (option == 1) {
                System.out.println("You have built a Self-contain");
                wood -=80;
                cement -=60;
                rods -=40; 
                money -=40000;
                System.out.println("You bought " +wood+"x wood"+cement+"x cement"+rods+"x rods");
                System.out.println("You have N"+money+" left");
        }
        else if(option == 2){
            if (wood>=180 && rods>=88 && cement>=200 || money>=78200) {
                System.out.println("You have built a Duplex");
                wood -=180;
                cement -=200;
                rods -=88; 
                money -=78200;
                System.out.println("You bought " +wood+"x wood"+cement+"x cement"+rods+"x rods");
                System.out.println("You have N"+money+" left");
            }else{
                System.out.println("Insufficient resources or funds");
            }
        }
        else if(option ==3){
            if (wood>=456 && rods>=361 && cement>=437 || money>=270800) {
                System.out.println("You have built a Palace");
                wood -=456;
                cement -=361;
                rods -=437; 
                money -=270800;
                System.out.println("You bought " +wood+"x wood"+cement+"x cement"+rods+"x rods");
                System.out.println("You have N"+money+" left");
            }else {
                System.out.println("Insufficient resources or funds");
            }
        }
        else{
            System.out.println("Invalid Input");
        }
    }

    public static void purchase(int wood,int cement,int rods,int money){
        int option,cost;
        Scanner scanner = new Scanner(System.in);
        System.out.println("**************************************");
        System.out.println("All resources must be bought here");
        System.out.println("Lets buy some before we start building");
        System.out.println("Welcome to the resource marketplace");
        System.out.println("**************************************");
        System.out.println("We have two purchasing methods");
        System.out.println("1.Bundle purchase");
        System.out.println("2.Individual purchase");
        System.out.print("Select a purchase method: ");
        option = scanner.nextInt();
        if (option == 1) {
            System.out.println("Bundle purchase selected");
            System.out.println("There are 3 bundles available");
            System.out.println("1.----Basic Bundle----");
            System.out.println("100x woods 120x cement 70x rods");
            System.out.println("2.-----Standard Bundle-----");
            System.out.println("300x woods 230x cement 150x rods");
            System.out.println("3.-----Premium Bundle-----");
            System.out.println("700x woods 620x cement 540x rods");
            System.out.print("Select a bundle: ");
            option = scanner.nextInt();
            switch (option) {
                case 1:
                    wood =100;
                    cement =120;
                    rods =70;
                    cost =28560;
                    money -=cost;
                    System.out.println("----------------------------------------------------------");
                    System.out.println("You bought " +wood+"x wood"+cement+"x cement"+rods+"x rods");
                    System.out.println("You have N"+money+" left");
                    System.out.println("----------------------------------------------------------");
                    break;

                case 2:
                    wood =200;
                    cement =230;
                    rods =150;
                    cost = 72350;
                    money -=cost;
                    System.out.println("----------------------------------------------------------");
                    System.out.println("You bought " +wood+" x wood"+cement+" x cement"+rods+" x rods");
                    System.out.println("You have N"+money+" left");
                    System.out.println("----------------------------------------------------------");
                break;
                case 3:
                    wood = 700;
                    cement = 620;
                    rods = 540;
                    cost =128065;
                    money -=cost;
                    System.out.println("----------------------------------------------------------");
                    System.out.println("You bought "+wood+"x wood,"+cement+"x cement,"+rods+"x rods");
                    System.out.println("You have N"+money+" left");
                    System.out.println("----------------------------------------------------------");
                    break;
                default:
                    System.out.println("Invalid Input");
                break;
            }
        }else if (option ==2) {
            System.out.println("Welcome to the Market place");
            System.out.println("Fill in the info below to buy");
            int woodamt,cementamt,rodsamt;
            System.out.print("Input no of wood to buy: ");
            woodamt = scanner.nextInt();
            System.out.print("Input no of cement to buy: ");
            cementamt = scanner.nextInt();
            System.out.print("Input no of rods to buy: ");
            rodsamt = scanner.nextInt();
            cost = (woodamt+cementamt+rodsamt)*2;
            wood+=woodamt;
            cement+=cementamt;
            rods+=rodsamt;
            money -=cost; 
            System.out.println("You have" +wood+"x wood"+cement+"x cement"+rods+"x rods");
            System.out.println("You have N"+money+" left");

            build(money, wood, cement, rods);
        } else {
            
        }
    }
}