// IMPORTS
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

public class tic implements ActionListener{
    //INSTANCES AND VARIABLES 
    Random rand = new Random();
    JFrame frame =new JFrame();
    JPanel tittlePanel = new JPanel();
    JPanel namePanel = new JPanel();
    JPanel scorePanel = new JPanel();
    JPanel buttonPanel = new JPanel();
    JLabel textFields = new JLabel();
    JLabel displayName = new JLabel();
    JLabel scoreLabel = new JLabel();
    JButton[] buttons = new JButton[9];
    String playerName,player2Name;
    int cnt;
    boolean player1_turn;
    
    tic(){
        // Instantiating the swing properties
        playerName = JOptionPane.showInputDialog(null, "Input Player1 Name: ");
        player2Name = JOptionPane.showInputDialog(null, "Input Player2 Name: ");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800,800);
        frame.getContentPane().setBackground(new Color(50,50,50));
        frame.setLayout(new BorderLayout());
        frame.setVisible(true);
        // Textfield properties
        textFields.setBackground(Color.GRAY);
        textFields.setForeground(Color.WHITE);
        textFields.setFont(new Font("Ink Free",Font.BOLD,50));
        textFields.setHorizontalAlignment(JLabel.CENTER);
        textFields.setText("Tic-Tac-Toe");
        textFields.setOpaque(true);
        // This are the properties for the name to be displayed on the game
        displayName.setBackground(new Color(25,25,25));
        displayName.setForeground(new Color(25,255,0));
        displayName.setFont(new Font("Ink Free",Font.PLAIN,20));
        displayName.setHorizontalAlignment(JLabel.CENTER);
        displayName.setText(playerName+" vs "+player2Name);
        displayName.setOpaque(true);
        //The main container that houses the name display,playr turns and game title 
        tittlePanel.setLayout(new BorderLayout());
        tittlePanel.setBounds(0,0,400,100);
        // Name display
        namePanel.setLayout(new BorderLayout());
        namePanel.setBounds(0,0,400,100);
        scorePanel.setLayout(new BorderLayout());
        scorePanel.setBounds(0,0,400,100);
        //The button container   
        buttonPanel.setLayout(new GridLayout(3,3));
        buttonPanel.setBackground(Color.BLUE);

        // This will loop throught the button and attach the properties contained within the for loop 
        for (int i = 0; i < 9; i++) {
            buttons[i] =new JButton();
            buttonPanel.add(buttons[i]);
            buttons[i].setFont(new Font("MV Boli",Font.BOLD,120));
            buttons[i].setFocusable(false);
            buttons[i].addActionListener((ActionListener) this);
            buttons[i].setBackground(Color.CYAN);
        }
        // Adding the necessary contents to the main panel
        tittlePanel.add(textFields);
        namePanel.add(displayName);
        frame.add(tittlePanel,BorderLayout.NORTH);
        frame.add(namePanel,BorderLayout.WEST);
        frame.add(buttonPanel);
        FirstTurn();
    }


    @Override
    public void actionPerformed(ActionEvent e) {
        for (int i = 0; i < 9; i++) {
            // This is to check for an empty button container
            if (e.getSource()==buttons[i]) {
                if (player1_turn) {
                    if (buttons[i].getText()=="") {
                        buttons[i].setForeground(new Color(255,0,0));
                        buttons[i].setText("X");
                        player1_turn=false;
                        textFields.setText(player2Name+"`s turn");
                        check();
                    }
                }else{
                    if (buttons[i].getText()=="") {
                        buttons[i].setForeground(new Color(0,0,255));
                        buttons[i].setText("O");
                        player1_turn=true;
                        textFields.setText(playerName + "`s turn");
                        check();
                    }
                }
            }

        }
        
    }
// METHODS
    public void FirstTurn() {
        // This adds a delay to the player turn input
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {

            e.printStackTrace();
        }
        //Makes the game a bit more fun by randomising the players that get to start
        if(rand.nextInt(2)==0){
            player1_turn=true;
            textFields.setText(playerName + "`s turn");
        }    
        else{
            player1_turn=false;
            textFields.setText(player2Name + "`s turn");
        }
    }

    public void check() {
        // Checks for winning conditions
        // x wining conditions
        if (
            (buttons[0].getText()=="X"&&
            buttons[1].getText()=="X"&&
            buttons[2].getText()=="X")
            ) {
            xwins(0, 1, 2); 
        }

        if (
            (buttons[3].getText()=="X"&&
            buttons[4].getText()=="X"&&
            buttons[5].getText()=="X")
            ) {
            xwins(3, 4, 5); 
        }

        if (
            (buttons[6].getText()=="X"&&
            buttons[7].getText()=="X"&&
            buttons[8].getText()=="X")
            ) {
            xwins(6, 7, 8); 
        }

        if (
            (buttons[0].getText()=="X"&&
            buttons[3].getText()=="X"&&
            buttons[6].getText()=="X")
            ) {
            xwins(0, 3, 6); 
        }

        if (
            (buttons[1].getText()=="X"&&
            buttons[4].getText()=="X"&&
            buttons[7].getText()=="X")
            ) {
            xwins(1, 4, 7); 
        }
        if (
            (buttons[2].getText()=="X"&&
            buttons[5].getText()=="X"&&
            buttons[8].getText()=="X")
            ) {
            xwins(2, 5, 8); 
        }

        if (
            (buttons[0].getText()=="X"&&
            buttons[4].getText()=="X"&&
            buttons[8].getText()=="X")
            ) {
            xwins(0, 4, 8); 
        }    
        if (
            (buttons[2].getText()=="X"&&
            buttons[4].getText()=="X"&&
            buttons[6].getText()=="X")
            ) {
            xwins(2, 4, 6); 
        }
        // 0 wining conditions
        
        if (
            (buttons[0].getText()=="O"&&
            buttons[1].getText()=="O"&&
            buttons[2].getText()=="O")
            ) {
            owins(0, 1, 2); 
        }

        if (
            (buttons[3].getText()=="O"&&
            buttons[4].getText()=="O"&&
            buttons[5].getText()=="O")
            ) {
            owins(3, 4, 5); 
        }

        if (
            (buttons[6].getText()=="O"&&
            buttons[7].getText()=="O"&&
            buttons[8].getText()=="O")
            ) {
            owins(6, 7, 8); 
        }

        if (
            (buttons[0].getText()=="O"&&
            buttons[3].getText()=="O"&&
            buttons[6].getText()=="O")
            ) {
            owins(0, 3, 6); 
        }

        if (
            (buttons[1].getText()=="O"&&
            buttons[4].getText()=="O"&&
            buttons[7].getText()=="O")
            ) {
            owins(1, 4, 7); 
        }
        if (
            (buttons[2].getText()=="O"&&
            buttons[5].getText()=="O"&&
            buttons[8].getText()=="O")
            ) {
            owins(2, 5, 8); 
        }

        if (
            (buttons[0].getText()=="O"&&
            buttons[4].getText()=="O"&&
            buttons[8].getText()=="O")
            ) {
                owins(0, 4, 8); 
        }    
        if (
            (buttons[2].getText()=="O"&&
            buttons[4].getText()=="O"&&
            buttons[6].getText()=="O")
            ) {
            owins(2, 4, 6); 
        }
    }

    public void xwins(int a,int b,int c) {
        buttons[a].setBackground(Color.green);
        buttons[b].setBackground(Color.green);
        buttons[c].setBackground(Color.green);
        for (int i = 0; i < 9; i++) {
            buttons[i].setEnabled(false);
            textFields.setText(playerName+" wins");
        }
    }

    public void owins(int a,int b,int c) {
        buttons[a].setBackground(Color.green);
        buttons[b].setBackground(Color.green);
        buttons[c].setBackground(Color.green);
        for (int i = 0; i < 9; i++) {
            buttons[i].setEnabled(false);
            textFields.setText(player2Name+" wins");
        }
    }
}