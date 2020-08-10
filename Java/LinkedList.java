import java.util.*;

public class LinkedList {
  Node head;
  
  public static void main(String[] args) {
    Random rand = new Random();
    
    int n = rand.nextInt(51);    //maximum is 50
    Node node = new Node(n);
    System.out.println("Node value = " + node.data);
    
    
  }
}
 
class Node {
  int data;
  Node next;
  Node(int d) {
    data = d;
    next = null;
  }
}
