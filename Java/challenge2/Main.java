package challenge2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  static boolean consoleOpen = true;

  public static void main (String[] args) {
    BBInterpreter bbInterpreter = new BBInterpreter();
    while (consoleOpen){
      String command = readConsole();
      bbInterpreter.interpret(command);
    }
  }

  private static String readConsole() {
    //Open a reader object that receives input from the user input
    BufferedReader consoleBufferedReader = new BufferedReader(new InputStreamReader(System.in));
    //Stores user input
    String input = null;
    try {
      input = consoleBufferedReader.readLine();
      //Close reader
      //consoleBufferedReader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }


    return input;
  }
}
