import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
public class App {
    public static void main(String[] args) throws Exception {
        int biddersCount,bids,rand;
        String names;

        String bidItemString[] = {
            "1960 Ford Mustang",
            "Antique Bed",
            "Antique Radio",
            "London snow art",
            "Plymouth Barracuda",
            "WWII bullet casing",
            "Ferrari F40",
            "Aventador SVJ",
            "Antique gum dispenser",
            "The Mona Lisa",
            "1782 Carriage",
            "The white House",
            "The kingdom of brunei",
            "The first Barcelona kit"
        };

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        ArrayList<String> biddersNames = new ArrayList<String>();
        ArrayList<Integer> biddersPrices = new ArrayList<Integer>();

        rand = random.nextInt(0,13);

        System.out.println("Welcome to Auction Houz");
        System.out.println("A maximum of ten bidders pls");
        System.out.println("Item of the day is: "+bidItemString[rand]);
        try {
        System.out.print("Input number of bidders: ");
        biddersCount = scanner.nextInt();
        while (biddersCount>10) {
            System.out.println("A maximum of ten bidders pls");
            System.out.print("Input number of bidders: ");
            biddersCount = scanner.nextInt();

        }
        for (int i= 0; i < biddersCount; i++) {
            System.out.print("Input name: ");
            names = scanner.next();
            biddersNames.add(names);
            System.out.print("Input amount to bid: ");
            bids = scanner.nextInt();
            biddersPrices.add(bids);
        }
        System.out.println("Bidders\t\tBids");
        for (int i = 0; i < biddersNames.size(); i++) {
            System.out.println(biddersNames.get(i)+"\t\t"+biddersPrices.get(i));
        }
        int highestBid = Collections.max(biddersPrices);            
        int highestBiddersName = biddersPrices.indexOf(highestBid); 
        System.out.println("Highest bidder: "+biddersNames.get(highestBiddersName));
        System.out.println("Highest bid: "+highestBid);

        } catch (InputMismatchException e) {
            System.out.println("Input mismatch");
            main(args);
        }
    }
}
