import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        /*
         * A life simulator game
         * A maximum of three events a day
         * Hard choices
         * Real consequences
         * 1 life no mercy you die progress.reset();
         * An properly implemented gps 
         * A Store.......has everything
         * Basic survival needs for livig in a city(food,clothin and shelter)
         * A functional frnds system...............hang out, chat
         */
        String name,state,country;
        int age;
        Scanner scanner = new Scanner(System.in);
        System.out.println("-------------------------------------------");
        System.out.println("Welcome to lifeSim");
        System.out.println("-------------------------------------------");
        System.out.println("Create your charcter");
        System.out.print("Input Name: ");
        name = scanner.next().toUpperCase();
        System.out.print("Input Age: ");
        age = scanner.nextInt();
        System.out.print("Input State: ");
        state = scanner.next().toUpperCase();
        System.out.print("Input Country: ");
        country = scanner.next().toUpperCase();
        lifeSim(age, name, state, country);
        
    }
    // main game method/ mother
    public static void lifeSim(int age,String name,String state,String country) {
        Scanner scanner = new Scanner(System.in);
        try {
            mainMenu(name, age,state,country);
        } catch (InputMismatchException e) {
            System.out.println("Invalid Input");
            lifeSim(age, name, state, country);
        }
    }
    // ------------------------MAINMENU METHOD---------------------------
    public static void mainMenu(String name, int age,String country,String state) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        // the main menu method will guide the user through the game....
        System.out.println("Name: "+ name +"\t" + "Age: "+ age);
        System.out.println("1.GPS");
        System.out.println("2.PHONE");
        System.out.println("3.QUIT");
        System.out.print("Select from the available options: ");
        choice = scanner.nextInt();
        if (choice == 1) {
            gps(name, age, country, state);;
        }
        else if (choice ==2) {
            phone(name, age, state, country);
        } 
        else if (choice ==3) {
            System.out.println("Byee!!!");
        }else{
            System.out.println("Plese select from the available options");
        }
    }
    // ------------------------MAINMENU METHOD---------------------------

    // ------------------------GPS METHOD--------------------------------
    public static void gps(String name,int age,String country,String state){
        loadScreenDelay();
        int choice;
        Scanner scanner = new Scanner(System.in);
        System.out.println("1.MALL");
        System.out.println("2.RESTAURANT");
        System.out.println("3.PARK");
        // System.out.println("4.WORK");
        System.out.println("4.BANK");
        System.out.print("Input choice: ");
        choice = scanner.nextInt();

        switch (choice) {
            case 1:
                mall(name, age, state, country);
                break;
            case 2:
                restaurant(name, state, country, age);
                break;
            case 3:
                park(name, age, state, country);
                break;
            // case 4:
            //     work();
            //     break;
            case 4:
                bank(name, age, state, country);
                break;
        
            default:
                System.out.println("Please input from the above otpions");
                gps(name, age, country, state);
                break;
        }
    }
    // ------------------------GPS METHOD--------------------------------

    // ------------------------MALL METHOD-------------------------------

    public static void mall(String name,int age,String state, String country) {
        /*this mall has three categories of stuff you can buy 
        * Clothing
        * Groceries
        * Tech
        */

        Scanner scanner = new Scanner(System.in);
        int choice,qty;
        String color;
        loadScreenDelay();
        System.out.println("Welcome to Ziggo Mall");
        System.out.println("Floor 1: Clothing");
        System.out.println("Floor 2: Groceries");
        System.out.println("Floor 3: Tech");
        System.out.print("Input floor number: ");
        choice = scanner.nextInt();
        if(choice == 1){
            delay();
            System.out.println("You are at the floor 1");
            System.out.println("1.Shorts");
            System.out.println("2.T-shirt");
            System.out.println("3.Long Sleeve");
            System.out.println("4.Pants");
            System.out.println("What do you want to buy: ");
            choice = scanner.nextInt();
            if (choice == 1) {
                System.out.print("Color: ");
                color = scanner.next();
                System.out.print("How many: ");
                qty = scanner.nextInt();

                System.out.println(qty+" new "+color+"shorts bought");
            }
            if (choice == 2) {
                System.out.print("Color: ");
                color = scanner.next();
                System.out.print("How many: ");
                qty = scanner.nextInt();

                System.out.println(qty+" new "+color+"Tshirts bought");
            }
            if (choice == 3) {
                System.out.print("Color: ");
                color = scanner.next();
                System.out.print("How many: ");
                qty = scanner.nextInt();

                System.out.println(qty+" new "+color+"long sleeves bought");
            }
            if (choice == 4) {
                System.out.print("Color: ");
                color = scanner.next();
                System.out.print("How many: ");
                qty = scanner.nextInt();

                System.out.println(qty+" new "+color+"pants bought");
            }
            mall(name, age, state, country);;
        }
        if (choice == 2) {
            delay();
            System.out.println("Floor 2: Groceries");
            System.out.println("1.1-Man sized groceries");
            System.out.println("2.Newly wed sized groceries");
            System.out.println("3.Family sized groceries");
            System.out.println("4.Glutton sized groceries");
            System.out.print("Choice: ");
            choice = scanner.nextInt();
            if (choice == 1) {
                System.out.println("1-Man sized groceries purchased");
                gps(name, age, country, state);         
            }
            if (choice == 2) {
                System.out.println("Newly wed sized groceries purchased");
                gps(name, age, country, state);         
            }
            if (choice == 3) {
                System.out.println("Family sized groceries purchased");
                gps(name, age, country, state);         
            }
            if (choice == 4) {
                System.out.println("Glutton sized groceries purchased");
                gps(name, age, country, state);         
            }
        }
        if (choice == 3) {
            delay();
            System.out.println("Floor 3: Tech");
            System.out.println("Under construction");
            gps(name, age, country, state);
        }
    }
    // ------------------------MALL METHOD-------------------------------
    // ------------------------BANK METHOD-------------------------------

    public static void bank(String name,int age,String state, String country) {
        loadScreenDelay();
        Scanner scanner = new Scanner(System.in);
        int balance =0, pin, deposit;
        String reply;
        System.out.println("Welcome to Ziggo Bank");
        System.out.println("Welocme back "+name);
        System.out.println("Defaut pin == 1234");
        System.out.println("Input pin to proceed");
        pin = scanner.nextInt();
        if (pin == 1234) {
            System.out.println("Balance: "+balance);
            if (balance<=1000) {
                System.out.println("Low bank balance");
                System.out.print("Would you like to make a deposit?: ");
                reply = scanner.next().toLowerCase();
                if (reply.equals("yes")) {
                    System.out.print("Deposit: ");
                    deposit = scanner.nextInt();
                    balance +=deposit; 
                    System.out.println("New balance: "+balance);
                    gps(name, age, country, state);
                }
                else{
                  gps(name, age, country, state);
                }
            }
        }else{
            while (pin != 1234) {
                System.out.print("Input pin dummy: ");
                pin = scanner.nextInt();
                break;
            }
        }
    }
    // ------------------------BANK METHOD-------------------------------
    // ------------------------PHONE METHOD------------------------------
    public static void phone(String name,int age,String state,String country) {
        int choice;
        Scanner scanner = new Scanner(System.in);
        System.out.println("4g\t\t100%");
        System.out.println("1.Contacts");
        System.out.println("2.Messages");
        System.out.println("3.Episodes");
        System.out.println("4.Go back <--");
        System.out.print("Applicaton: ");
        choice = scanner.nextInt();

        if (choice == 1) {
            System.out.println("*****************************");
            System.out.println("Carita de Angel");
            System.out.println("Hanan");
            System.out.println("Fam");
            System.out.println("XOXO");
            System.out.println("DAD");
            System.out.println("Fati");
            System.out.println("MOM");
            System.out.println("SLS");
            System.out.println("Halima");
            System.out.println("Sis Fadila");
            System.out.println("Fauzy");
        }

        if (choice == 2) {
            System.out.println("*****************************");
            System.out.println("MOM:Where are you");
            System.out.println("DAD:I sent you the money");
            System.out.println("XOXO:Thanks papi");
            System.out.println("Fam: Guyy the match just hot");
            System.out.println("Service Provider: You are low on airtime please recharge");
            System.out.println("Carita de Angel: I am sorry");
            System.out.println("Hanan: Guy its just a kiss calm down");
            System.out.println("Fati: My pc don spoil ne");
            System.out.println("SLS: yh");
        }
        if (choice == 3) {
            episodes(name, age, state, country);
        }
        if (choice == 4){
            mainMenu(name, age, country, state);
        }
        phone(name, age, state, country);
    }

    // ------------------------PHONE METHOD------------------------------

    // ------------------------RESTAURANT METHOD-------------------------
    public static void restaurant(String name,String state,String country,int age) {
        String foodName;
        int quantity,price;
        Scanner scanner = new Scanner(System.in);
        loadScreenDelay();
        System.out.println("*****************************");
        System.out.println("Welcome to Mama Della`s "+name);
        System.out.println("Please place an order");
        System.out.println("*****************************");

        System.out.print("What do you want to eat?: ");
        foodName = scanner.next();
        delay();
        System.out.print("Input quantity(Servings): ");
        quantity = scanner.nextInt();
        delay();
        System.out.print("Input price: ");
        price = scanner.nextInt();
        price = price*quantity;   
        System.out.println("Proceed to checkout");
        System.out.println("********************************");
        System.out.println("Reciept for: "+name+"\t\tDate:2/1/2023");
        System.out.println("FOOD\t\tQUANTITY\tPRICE");
        System.out.println(foodName+"\t\t"+quantity+"\t\t"+price);
        System.out.println("********************************");
        gps(name, age, country, state);
    }
    // ------------------------RESTAURANT METHOD-------------------------

    // ------------------------WORK METHOD------------------------------
    public static void work() {
        
    }

    // ------------------------WORK METHOD------------------------------
    public static void park(String name,int age,String state,String country) {
        Scanner scanner = new Scanner(System.in);
        int option,theirChoice;
        String frndsName;
        loadScreenDelay();
        System.out.println("You are at the park");
        System.out.println("1.Call a friend");
        System.out.println("2.Find a date");
        System.out.println("3.Hang out alone");
        System.out.print("Choice: ");
        option = scanner.nextInt();
        if (option == 1) {
            System.out.println("Who do you want to call");
            System.out.print("Input their name: ");
            frndsName = scanner.next();
            theirChoice = frndsName.length()*2;
            if (theirChoice >= 10) {
                System.out.println(frndsName+" is on his way");
                System.out.println("You had fun with "+frndsName+"today it got dark so u went back home");
            gps(name, age, country, state);
            }
            else{
                System.out.println(frndsName+" coudnt make it");
                System.out.println("You ended up not having a good time");
            gps(name, age, country, state);
            }
        }
        if (option == 2) {
            String pos1 = "You got yourself a nice date",
            pos2 = "you got rejected";
            int rand;
            Random random = new Random();
            rand = random.nextInt(1,2);
            if (rand == 1) {
                System.out.println(pos1);
            }
            System.out.println(pos2);
            gps(name, age, country, state);
        }
        if (option == 3) {
            System.out.println("You ended up not having a good time");
            gps(name, age, country, state);
        }
    }
    // ------------------------TIPS METHOD-------------------------------
    public static void tips() {
        String tip1,tip2,tip3,tip4,tip5,tip6,tip7,tip8;
        int rand;
        Random random = new Random();
        tip1 = "TIPS: Make wise choices you only get to live once";
        tip2 = "TIPS: Use your day wisely else!!!!";
        tip3 = "TIPS: Organise your day before starting, Use the todo list which is your MyLife app on your phone";
        tip4 = "TIPS: Makinng new friends might be a challenge but you  can do absolutely nothing";
        tip5 = "TIPS: Watch out for your food u might die after two huge events";
        tip6 = "TIPS: If you ever decide to cook you can buy groceries at the mall";
        tip7 = "TIPS: You can get a phone at the tech floor in the Ziggomall";
        tip8 = "TIPS: If you ever get bored you can play episode on your mobile phone";
        rand = random.nextInt(1,7);
        if (rand == 1) {
            System.out.println(tip1);
        }
        else if (rand == 2) {
            System.out.println(tip2);
        }
        else if (rand == 3) {
            System.out.println(tip3);
        }
        else if (rand == 4) {
            System.out.println(tip4);
        }
        else if (rand == 5) {
            System.out.println(tip5);
        }
        else if (rand == 6) {
            System.out.println(tip6);
        }
        else if (rand == 7) {
            System.out.println(tip7);
        }
        else if (rand == 8) {
            System.out.println(tip8);
        }
    }
    // ------------------------TIPS METHOD-------------------------------   

    // ------------------------DELAY METHOD------------------------------
    // the function of this method is to add a delay to the console
    public static void delay() {
        try { 
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    public static void loadScreenDelay() {
        try {
            System.out.println("--------------LOADING-----------");
            tips();
            System.out.println("--------------------------------");
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    // ------------------------DELAY METHOD------------------------------
    // ------------------------M GAME METHOD-----------------------------

    public static void episodes(String name,int age,String state,String country){
        loadScreenDelay();
       String choice;
       Scanner scanner = new Scanner(System.in);
        //    event1 = "You woke up very late today as a result you got fired";
        //    event2 = "You just got a new baby";
        //    event3 = "Your friends are going sky diving but you are scared of height";
        //    event4 = "You saw your crush and confessed your feelings.That slap still hurts....Happiness -67%";

        System.out.print("You are bored are you going outside: ");
        choice = scanner.next().toLowerCase();
        if (choice.equals("yes")) {
            System.out.println("You went outside and it startes raining.Now u have runny nose....what will you doo");
            System.out.println("A.Hospital");
            System.out.println("B.Pray");
            System.out.println("C.Self Medicate");
            System.out.print("Choice: ");
            choice = scanner.next().toLowerCase();
            if (choice.equals("a")){
                System.out.println("you are feeling better now except you were left with your sister and she has cold too...you cant afford her bills");
                System.out.println("What will you doo");
                System.out.println("A.Hospital");
                System.out.println("B.Pray for her");
                System.out.println("C.Self Medicate");
                System.out.print("Choice: ");
                choice = scanner.next().toLowerCase();
                if (choice.equals("a")) {
                    System.out.println("You had no money to pay for the bills now you work for the hospital as a janitor");
                    System.out.println("Your sister insists on leaving to your uncles house");
                    System.out.println("A.Beg her to stay");
                    System.out.println("B.Insult her one last time");
                    System.out.println("C.Let her leave");
                    System.out.print("Choice: ");
                    choice = scanner.next().toLowerCase();
                    if (choice.equals("a")) {
                        System.out.println("You pleaded with her to stay and she did..You promised to get a better job");
                        System.out.println("You are out for a walk on your way you saw 10000$ lying around");
                        System.out.println("A.Pick it up");
                        System.out.println("B.Take it to the police");
                        System.out.println("C.Walk past it");
                        System.out.print("Choice: ");
                        choice = scanner.next().toLowerCase();
                        if(choice.equals("a")){
                            System.out.println("You picked it up and nothing happend you are now +10000$");
                            System.out.println("Now that you are stable....how will you spend the money");
                            System.out.println("A.Lavishly spend");
                            System.out.println("B.Invest the money");
                            System.out.println("C.Impress your sister");
                            System.out.print("Choice: ");
                            choice = scanner.next().toLowerCase();
                            if (choice.equals("a")) {
                                System.out.println("You spent all the money in a club and got broke again");
                                System.out.println("Your sister left you");
                                System.out.println("You are now homeless and sick");
                                System.out.println("You died while sleeping");
                                phone(name, age, state, country);
                            }
                            else if (choice.equals("b")) {
                                System.out.println("You invested 7000$");
                                System.out.println("13 years later,you are leading a very succesfull life with 4kids and a perfect wife");
                                System.out.println("Your first kid is now 18");
                                System.out.println("He came to you for advice on his education.He wants to major in History");
                                System.out.println("A. Wish him the best");
                                System.out.println("B. Pick his major");
                                System.out.println("C. Tell him you dont care");
                                System.out.print("Choice: ");
                                choice = scanner.next().toLowerCase();
                                if (choice.equals("a")) {
                                    System.out.println("You wished him the best.He majored in history");
                                    System.out.println("He became a teacher");
                                    System.out.println("He got married but lost");
                                    System.out.println("Unfortunately you have a business trip on the day of the funeral");
                                    System.out.println("A.Go on the business trip");
                                    System.out.println("B.Go to the funeral");
                                    System.out.println("C.Sleep");
                                }
                            }
                            else if (choice.equals("b")) {
                                System.out.println("You took the money to the nearest police station but they didnt care to look for the owner");
                                System.out.println("You got frustrated and sued them to court");
                                System.out.println("They lost their jobs and their family starved to death because of you");
                                System.out.println("The society hated you and you comitted suicide");
                                System.out.println("Acheivment unlocked: FOOL");
                                phone(name, age, state, country);
                            }
                            else if (choice.equals("c")) {
                                System.out.println("You left the money there.");
                                System.out.println("The next day you woke up to a loud bang...Turns out it was your neigbour who bought a new car");
                                System.out.println("You asked how he gt the money he told you he picked them up off the sidewalk");
                                System.out.println("You got jelous and wrecked his car...He called the police and you got a 3yrs sentence");
                                System.out.println("While at lunch one of the mafia boss looked for your trouble");
                                System.out.println("A.Punch him");
                                System.out.println("B.Ignore him");
                                System.out.println("C.Report him");
                                System.out.print("Choice: ");
                                choice = scanner.next().toLowerCase();
                                if (choice.equals("a")) {
                                    System.out.println("You gave him your hardest punch....he didnt even shake.");
                                    System.out.println("Long story short you died");
                                    phone(name, age, state, country);
                                }
                                else if(choice.equals("b")){
                                    System.out.println("You ignored him but he did not leave there scot free.He got another 2 years for assault");
                                    System.out.println("You started workout to prevent future events like dat as per the officers advice");
                                    System.out.println("You finished your sentence.....You led a very miserable life...you got ran over by an ambulance");
                                    phone(name, age, state, country);
                                }
                                else if(choice.equals("c")){
                                    System.out.println("You reported him to the nearest officer....He told you to grow up");

                                }
                            }
                        }
                    }
                }
            }else if (choice.equals("b")) {
                System.out.println("You prayed and got better anyways");
                System.out.println("Its a sunday and your freinds asked you to go sky diving....you have a fear of heights");
                System.out.println("A.Go with them");
                System.out.println("B.Confess to them");
                System.out.println("C.Abandon them");
                System.out.print("Choice: ");
                choice = scanner.next().toLowerCase();
                if (choice.equals("a")) {
                    System.out.println("You died because of parachute failure and your friends didnt even care");
                    phone(name, age, state, country);
                }
                else if (choice.equals("b")) {
                    System.out.println("You confessed your fear of height but they called you a chicken and unfriended u");
                    System.out.println("You are now lonely and have no friends you died of depression");
                    phone(name, age, state, country);
                }
                else if (choice.equals("c")) {
                    System.out.println("You are now lonely and have no friends you died of depression");
                    phone(name, age, state, country);
                }
            }
        }else if (choice.equals("no")) {
            System.out.println("you stayed at home and it ended up with a heavy rain");
            System.out.println("Your roof got water damage");
            System.out.println("A.Call the repair services");
            System.out.println("B.Do it yourself");
            System.out.println("C.Let it flow");
        }
        }

    // ------------------------M GAME METHOD-----------------------------
}