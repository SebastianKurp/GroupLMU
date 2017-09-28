import java.io.IOException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Search {
    Main main = new Main();
    Note note = new Note();

    Scanner scanner = new Scanner(System.in);
    Vector<String> count = new Vector<>();


    //reads files into map
    public void setMap() throws IOException {
        note.readFiles(main.path);
        note.getNotesFromFiles();
    }

    public void searchBy(String key) throws IOException {
        if (key.equalsIgnoreCase("a")) {
            //display all notes with mentions
            System.out.println("These files contain mentions: \n");
            note.iterateMapSearch("@");
            note.printFilesToPrint();
        }

        if (key.equalsIgnoreCase("b")) {
            //display all notes organized by mention
            System.out.println("\nThese files contain mentions: \n");
            note.iterateMapSearch("@");
            note.printFilesToPrintSorted();
        }


        if (key.equalsIgnoreCase("c")) {
            //displays all important words in each note
            Vector<Integer> numbers = new Vector<>();
            Vector<String> sortedCount = new Vector<>();
            Vector<String> usedWords = new Vector<>();
            for(Map.Entry<String,String> entry : note.map.entrySet()){
                String value = entry.getValue();
                String[] splitString = value.trim().split(",|\\.|\\?|:|\\s|!|;|—");//split with regex
                Set<String> commonWords = new HashSet<>(Arrays.asList("the", "and","that","have","for","not","with","this","but","from","will","would","there","their","what","out","about",
                        "get","like","just","into","your","some","could","them","other","than","then","now","its","over","also","well","because","these", "The", "And", "That", "Have", "For",
                        "you","her","his","were", "Not","was","most","upon"));

                List list = Arrays.asList(splitString);
                Set<String> set = new LinkedHashSet<>(list);
                for(String str : set) {
                    if (str.length() < 3) {
                        continue;
                    }else if(commonWords.contains(str)){
                        continue;
                    }else {
                        count.add(Collections.frequency(list, str) + " = " + str);//counts number of occurrences
                    }
                    if(entry.getKey().toLowerCase().contains(str.toLowerCase())||str.contains("#")){//if word is also present in note title increase value
                        int i =0;
                        String number = "";
                        while(Character.isDigit(count.lastElement().charAt(i))){//checks for double digits
                            number += count.lastElement().charAt(i);
                            i++;
                        }
                        int num = Integer.parseInt(number);
                        num +=10;
                        String oldString = count.lastElement();//replace string with new value
                        String newString = Integer.toString(num) + oldString.substring(number.length());
                        count.remove(count.size()-1);
                        count.add(newString);
                    }
                }

                for(String str : count){//adds word frequency to new vector to sort
                    int i =0;
                    String number = "";
                    while(Character.isDigit(str.charAt(i))){//checks for double digit
                        number += str.charAt(i);
                        i++;
                    }
                    int num = Integer.parseInt(number);
                    numbers.add(num);
                }
                Collections.sort(numbers);
                Collections.reverse(numbers);

                for(int num : numbers){//takes unsorted vector and sorts by first index which is number of occurrences
                    for(String str: count){
                        if(num >= 0) {
                            if (str.contains(Integer.toString(num))) {
                                if(str.indexOf(Integer.toString(num))==0) {
                                    sortedCount.add(str);
                                }
                            }
                        }
                    }
                }
                Vector<String> noDuplicates = new Vector<>();
                Vector<String> noCount = new Vector<>();
                for(String str : sortedCount){//removes duplicates from sortedCount
                    if(noDuplicates.contains(str)){
                        continue;
                    }else{
                        noDuplicates.add(str);
                    }
                }
                for(String str: noDuplicates){//removes count for top words
                    int i =0;
                    String word = "";
                    while(i<str.length()){//checks for digits/spaces/=
                        if(Character.isDigit(str.charAt(i))||str.charAt(i)==' '||str.charAt(i)=='='){
                            i++;
                        }else {
                            word += str.charAt(i);
                            i++;
                        }
                    }
                    if(noCount.size()<=10) {
                        noCount.add(word);
                    }
                }
                Collections.shuffle(noCount);
                System.out.println("\n"+entry.getKey()+ ":");

                int i = 0;
                while( i <=10){//displays the top 10 words
                    if(i >= noCount.size()){
                        break;
                    }else {
                        System.out.println(noCount.get(i));
                        i++;
                    }
                }
                count.clear();
                numbers.clear();
                sortedCount.clear();
                usedWords.clear();
                noDuplicates.clear();
            }
        }

        if (key.equalsIgnoreCase("d")) {
            //report all notes organized by frequently used words
            Vector<Integer> numbers = new Vector<>();
            Vector<String> sortedCount = new Vector<>();
            Vector<String> usedWords = new Vector<>();
            for(Map.Entry<String,String> entry : note.map.entrySet()){
                String value = entry.getValue();
                String[] splitString = value.trim().split(",|\\.|\\?|:|\\s|!|;|—");//split with regex
                Set<String> commonWords = new HashSet<>(Arrays.asList("the", "and","that","have","for","not","with","this","but","from","will","would","there","their","what","out","about",
                        "get","like","just","into","your","some","could","them","other","than","then","now","its","over","also","well","because","these", "The", "And", "That", "Have", "For",
                        "you","her","his","were", "Not","was","most","upon"));
                List list = Arrays.asList(splitString);
                Set<String> set = new LinkedHashSet<>(list);
                for(String str : set) {
                    if (str.length() < 3) {
                        continue;
                    }else if(commonWords.contains(str)){
                        continue;
                    }else {
                        count.add(Collections.frequency(list, str) + " = " + str);//counts number of occurrences
                    }
                    if(entry.getKey().toLowerCase().contains(str.toLowerCase())||str.contains("#")){//if word is also present in note title increase value
                        int i =0;
                        String number = "";
                        while(Character.isDigit(count.lastElement().charAt(i))){//checks for double digits
                            number += count.lastElement().charAt(i);
                            i++;
                        }
                        int num = Integer.parseInt(number);
                        num +=10;
                        String oldString = count.lastElement();//replace string with new value
                        String newString = Integer.toString(num) + oldString.substring(number.length());
                        count.remove(count.size()-1);
                        count.add(newString);
                    }
                }

                for(String str : count){//adds word frequency to new vector to sort
                    int i =0;
                    String number = "";
                    while(Character.isDigit(str.charAt(i))){//checks for double digit
                        number += str.charAt(i);
                        i++;
                    }
                    int num = Integer.parseInt(number);
                    numbers.add(num);
                }
                Collections.sort(numbers);
                Collections.reverse(numbers);

                for(int num : numbers){//takes unsorted vector and sorts by first index which is number of occurrences
                    for(String str: count){
                        if(num >= 0) {
                            if (str.contains(Integer.toString(num))) {
                                if(str.indexOf(Integer.toString(num))==0) {
                                    sortedCount.add(str);
                                }
                            }
                        }
                    }
                }
                Vector<String> noDuplicates = new Vector<>();
                for(String str : sortedCount){//removes duplicates from sortedCount
                    if(noDuplicates.contains(str)){
                        continue;
                    }else{
                        noDuplicates.add(str);
                    }
                }
                System.out.println("\n"+entry.getKey()+ ":");

                int i = 0;
                while( i <=10){//displays the top 10 words
                    if(i >= noDuplicates.size()){
                        break;
                    }else {
                        System.out.println(noDuplicates.get(i));
                        i++;
                    }
                }
                count.clear();
                numbers.clear();
                sortedCount.clear();
                usedWords.clear();
                noDuplicates.clear();
            }

            note.generateKeywords();
        }

        if (key.equalsIgnoreCase("e")) {
            //report all notes that contain a searched frequently used word or @
            System.out.println("Please enter a person or keyword you would like to search for: ");
            String searchValue = scanner.nextLine();
            Pattern p = Pattern.compile(searchValue, Pattern.CASE_INSENSITIVE);//search for value including mentions with regex
            for (Map.Entry<String, String> entry : note.map.entrySet()) {
                String input = entry.getValue();
                Matcher m = p.matcher(input);
                if (m.find()) {
                    note.filesToPrint.add(entry.getKey());
                }
            }
            note.printFilesToPrint();
            note.filesToPrint.clear();
            System.out.println();
            System.out.println("Would you like to search for another term? Y/N ");
            String searchAgain = scanner.nextLine();
            searchAgain = searchAgain.toLowerCase();
            if (searchAgain.equals("y")) { searchBy("e"); }
            else { main.options(); }
        }

        if (key.equalsIgnoreCase("f")) {
            note.topologicalSort();
        }
        System.out.println();
        main.options();
    }
}
