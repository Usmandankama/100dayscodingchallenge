import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        // Variables
        Scanner  scanner = new Scanner(System.in);
        String name,subject,restartOption;
        // EXECUTION
        System.out.print("Enter name: ");
        name = scanner.next();

        System.out.print("Enter subject: ");
        subject = scanner.next();
        
        System.out.println("********************************");
        System.out.println("STUDENT NAME: "+name);
        System.out.println("SUSBJECT: "+subject);
        System.out.println("********************************");


        quizMath();
        System.out.println("Want to try again? YES/NO");
        restartOption = scanner.nextLine().toUpperCase();

        switch (restartOption) {
            case "YES":
                quizMath();
                break;

            case "NO":
                System.out.println("Bye.See you next time");
            break;
        
            default:
            System.out.println("Invalid Input");
                break;
        }
        scanner.close();
    }

    static void quizMath() {
        int cnt =0;
        String
        // grade,
        q1,q2,q3,
        q4,q5,q6,
        q7,q8,q9,
        q10,q11,q12;
        // INSTANCEs
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Q1.What is 2(2-4)");
        System.out.println("A.7 B.3 C.-11 D.-4");    //D
        System.out.print("Enter your choice: ");
        q1 = scan.next();
        
        System.out.println("Q2.What is sin(90)");
        System.out.println("A.1 B.20.423 C.-0.792 D.-0.444");           //A
        System.out.print("Enter your choice: ");
        q2 = scan.nextLine();
        
        System.out.println("Q3.What is 0/0");
        System.out.println("A.0 B.32 C.45 D.Indefinite"); //D
        System.out.print("Enter your choice: ");
        q3 = scan.nextLine();
        
        System.out.println("Q4.What is 123/56^2");
        System.out.println("A.33.0 B.18.76 C.12.22 D.0.40");//D
        System.out.print("Enter your choice: ");
        q4 = scan.nextLine();
        
        System.out.println("Q5.Find x in x+x=8");
        System.out.println("A.7 B.4 C.31 D.4");//D
        System.out.print("Enter your choice: ");
        q5 = scan.nextLine();
        
        System.out.println("Q6.Calculate the volume of a rectangle that measures 30cm X 15cm X 10cm");
        System.out.println("A.4230cm^3 B.500cm^3 C.4500cm^3 D.3178cm^3 ");//C
        System.out.print("Enter your choice: ");
        q6 = scan.nextLine();
        
        System.out.println("Q7.Solve the equation x/2=5");
        System.out.println("A.7 B.10 C.3 D.4");//B
        System.out.print("Enter your choice: ");
        q7 = scan.nextLine();
        
        System.out.println("Q8.Simplify 2x+3x+7");
        System.out.println("A.-2x+4 B.3x+2x+7 C.-12x D.5x+7");//D
        System.out.print("Enter your choice: ");
        q8 = scan.nextLine();
        
        System.out.println("Q9.Simplify 8m-2m-3m");
        System.out.println("A.-13m B.3m C.-11m D.4m");//A
        System.out.print("Enter your choice: ");
        q9 = scan.nextLine();
        
        System.out.println("Q10.How many 8`s are in 64");
        System.out.println("A.23 B.3 C.8 D.4");//C
        System.out.print("Enter your choice: ");
        q10 = scan.nextLine();
        
        System.out.println("Q11.What is the square root of 4");
        System.out.println("A.2 B.3 C.-11 D.-4");//A
        System.out.print("Enter your choice: ");
        q11 = scan.nextLine();
        
        System.out.println("Q12.What is -2(2+4-5)");
        System.out.println("A.-11 B.3 C.-2 D.-4");//C
        System.out.print("Enter your choice: ");
        q12 = scan.nextLine();

        if (q1 =="D"||q1=="d") {
            cnt+=1;
            System.out.println(cnt);
        }
        else  if(q2 =="A"||q2=="a") {
            cnt+=1;
        }
        else if(q3 =="D"||q3=="d") {
            cnt+=1;
        }
        else if (q4 =="D"||q4=="d") {
            cnt+=1;
        }
        else if (q5 =="D"||q5=="d") {
            cnt+=1;
        }
        else if (q6 =="C"||q6=="c") {
            cnt+=1;
        }
        else if (q7 =="B"||q7=="b") {
            cnt+=1;
        }
        else if (q8 =="D"||q8=="d") {
            cnt+=1;
        }
        else if (q9 =="A"||q9=="a") {
            cnt+=1;
        }
        else if (q10 =="C"||q10=="c") {
            cnt+=1;
        }
        else if (q11 =="A"||q11=="a") {
            cnt+=1;
        }
        else if (q12 =="C"||q12=="c") {
            cnt+=1;
        }
        System.out.println("********************************");
        System.out.println("Your score is: "+cnt);
        System.out.println("********************************");

        // if (cnt <=3){
        //     grade = "F";
        //     System.out.println("Your grade is "+grade+" Poor performance,try harder");
        // }else if (cnt>3&&cnt<=6) {
        //     grade = "D";
        //     System.out.println("Your grade is "+grade+" Try harder");
        // } 
        // else if (cnt>6&&cnt<=8) {
        //     grade = "C";
        //     System.out.println("Your grade is "+grade+" Average performance");
        // } else if (cnt>8&&cnt<=10) {
        //     grade = "B";
        //     System.out.println("Your grade is "+grade+"Good performance");
        // } else if (cnt>10&&cnt<=12) {
        //     grade = "A";
        //     System.out.println("Your grade is "+grade+"Excellent performance");
        // } 
        scan.close();
    }
}