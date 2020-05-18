import java.util.ArrayList;


public class ListArray {

	public static void main(String[] args) {
		
		ArrayList<String> list = new ArrayList<String>();
		list.add("Selenium");
		list.add("Webdriver");
		list.add("Java");
		
		System.out.println(list.get(2));
		
		for (int i=0;i < list.size(); i++){
			System.out.println(list.get(i));
			
		}
		
		

	}

}
