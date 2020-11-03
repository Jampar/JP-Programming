package challenge2;

import com.sun.org.apache.xpath.internal.operations.Bool;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BBInterpreter {

  private static boolean terminated;

  public static enum type {
    op,
    symbol,
    value,
    equals,
    terminator,
  }

  public final static String[] ops = {
      "incr",
      "decr",
      "clear",
      "=",
      ";",
      "while",
      "not",
      "do",
  };

  public static char[] specialChars = {
      '=',
      ';',
      ' '
  };

  public boolean printMemory = false;

  static List<Variable> memory = new ArrayList<Variable>();

  static boolean whileFlag = false;
  static List<WhileBuffer> whileBuffers = new ArrayList<WhileBuffer>();

  public void interpret(String input) {

    Lexer lexer = new Lexer();
    Token[] tokens = lexer.lex(input);

    int tokenCounter = 0;
    for (Token token : tokens) {
      switch (token.getType()) {

        case symbol:
          if (tokens.length <= 2) {
            printVariable(token.getValue());
          } else {
            if (findInMemory(token.getValue()) == -1) {
              createNewVariable(token.getValue(), 0);
            }
          }
          break;

        case op:
          executeOperation(token.getValue(), tokens[tokenCounter + 1].getValue(), 0);
          break;

        case equals:
          int data = 0;

          Token tToken = tokens[tokenCounter + 1];
          if (tToken.getType() == type.value) {
            data = Integer.parseInt(tToken.getValue());
          } else {
            System.out.println("Value not given");
          }

          executeOperation(token.getValue(), tokens[tokenCounter - 1].getValue(), data);
          break;

        case terminator:
          if (printMemory) printMemory();
          return;

      }
      tokenCounter++;
    }
  }

  public static boolean isOp(String check) {
    for (String op : ops) {
      if (op.equals(check)) return true;
    }
    return false;
  }

  public static boolean isSpecialChar(char check) {
    for (char sc : specialChars) {
      if (sc == check) return true;
    }
    return false;
  }

  private static void writeToMemory(String label, int contents) {
    int memIndex = findInMemory(label);
    if (memIndex != -1) {
      memory.set(memIndex, new Variable(label, contents));
    } else {
      System.out.println("Could find " + label + " in memory");
    }
  }

  private static int getMemoryContents(String memoryLabel) {
    for (Variable var : memory) {
      if (var.label.equals(memoryLabel))
        return var.value;
    }
    return 0;
  }

  private void printVariable(String memoryLabel) {
    Object contents = getMemoryContents(memoryLabel);
    System.out.println(contents);
  }

  private static int findInMemory(String memoryLabel) {
    int i = 0;
    for (Variable var : memory) {
      if (var.label.equals(memoryLabel)) {
        return i;
      }
      i++;
    }
    return -1;
  }

  private void printMemory() {
    System.out.println("---MEMORY---");
    for (Variable v : memory) {
      System.out.println('[' + "Label: " + v.label + ',' + " Value: " + v.value + ']');
    }
  }

  private static void createNewVariable(String label, int contents) {
    memory.add(new Variable(label, contents));
  }

  private static void executeOperation(String opCode, String memoryLabel, int data) {
    int opIndex = Arrays.asList(ops).indexOf(opCode);

    switch (opIndex) {
      case 0:
        int value = getMemoryContents(memoryLabel);
        value += 1;
        writeToMemory(memoryLabel, value);
        break;

      case 1:
        value = getMemoryContents(memoryLabel);
        value -= 1;
        writeToMemory(memoryLabel, value);
        break;

      case 2:
        if (findInMemory(memoryLabel) == -1) {
          createNewVariable(memoryLabel, 0);
        }
        writeToMemory(memoryLabel, 0);
        break;

      case 3:
        writeToMemory(memoryLabel, data);
        break;

      case 4:
        terminated = true;
        break;

      case 5:
        whileFlag = true;
        break;

      case 6:
        break;
    }
  }



}

class WhileBuffer{

  List<String> commands = new ArrayList<String>();
  boolean condition;

  public WhileBuffer(boolean condition){
    this.condition = condition;
  }

  public void addCommand(String command){
    commands.add(command);
  }

  public boolean testCondition(){
    return condition;
  }
}

class Variable {
  String label;
  int value;

  public Variable(String label, int value) {
    this.label = label;
    this.value = value;
  }
}

class Lexer {

  private Token[] lastTokens;

  public Lexer() {
  }

  public Token[] lex(String instructionLine) {

    List<Token> tokens = new ArrayList<Token>();

    StringBuilder builder = new StringBuilder();
    for (int i = 0; i < instructionLine.length(); i++) {

      char currentChar = instructionLine.charAt(i);
      if (BBInterpreter.isSpecialChar(currentChar)) {
        if (BBInterpreter.isOp(builder.toString())) {
          tokens.add(new Token(builder.toString(), BBInterpreter.type.op));
        } else if (builder.length() > 0) {
          if (isNumeric(builder.toString())) {
            tokens.add(new Token(builder.toString(), BBInterpreter.type.value));
          } else {
            tokens.add(new Token(builder.toString(), BBInterpreter.type.symbol));
          }
        }

        if (currentChar == '=') {
          tokens.add(new Token(String.valueOf(currentChar), BBInterpreter.type.equals));
        } else if (currentChar == ';') {
          tokens.add(new Token(String.valueOf(currentChar), BBInterpreter.type.terminator));
        }

        builder = new StringBuilder();
      } else {
        builder.append(currentChar);
      }
    }
    this.lastTokens = tokens.toArray(new Token[0]);
    return tokens.toArray(new Token[0]);
  }

  public void printTokens() {
    for (Token token : lastTokens) System.out.print(token.output());
    System.out.print("\n");
  }

  public String strTokens() {
    StringBuilder tokens = new StringBuilder();
    for (Token token : lastTokens) tokens.append(token.output());
    tokens.append("\n");
    return tokens.toString();
  }

  public boolean isNumeric(String strNum) {
    if (strNum == null) {
      return false;
    }
    try {
      int d = Integer.parseInt(strNum);
    } catch (NumberFormatException nfe) {
      return false;
    }
    return true;
  }
}

/**
 * Token object to store information on each token in an instruction.
 */
class Token {

  //Value of the token
  private final String value;
  //Token Type
  private final BBInterpreter.type type;

  /**
   * Token Constructor
   *
   * @param value Value of Token e.g. "0", "X", "incr"
   * @param type  Type of Token e.g. op, symbol, number
   */
  public Token(String value, BBInterpreter.type type) {
    //Assign Token variables
    this.value = value;
    this.type = type;
  }

  /**
   * Type accessor method
   *
   * @return Token Type
   */
  public BBInterpreter.type getType() {
    return this.type;
  }


  /**
   * Value accessor method
   *
   * @return Token Value
   */
  //Value access method
  public String getValue() {
    return this.value;
  }

  public String output() {
    return new String('[' + getValue().toString() + ", " + getType().toString() + "] ");
  }
}
