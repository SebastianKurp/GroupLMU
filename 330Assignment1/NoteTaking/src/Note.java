import com.sun.xml.internal.ws.policy.privateutil.PolicyUtils;
import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Note {
    Vector<File> filesForRead = new Vector<>();
    Vector<String> filesToPrint = new Vector<>();
    Vector<String> keywords = new Vector<>();
    Map<String,String> map = new HashMap<>();
    Vector<String> mentionList = new Vector<>();
    Map<String,Integer> outDegree = new HashMap<>();
    Map<String,Integer> inDegree = new HashMap<>();
    Vector<String> keysNoReferences = new Vector<>();
    Vector<String> keysOutReferences = new Vector<>();
    Vector<String> keysReferenced = new Vector<>();



    public void readFiles(String path){
        /*stores file names in vector. Only allows for .txt files*/
        File folder = new File(path);

        for(File file :folder.listFiles()){
            String fileName = file.toString();
            if(fileName.contains(".txt")&& file.isFile()){
                filesForRead.add(file);
            }
        }
    }

    public void getNotesFromFiles() throws IOException {//open files and read them


        for (int i = 0; i<filesForRead.size();i++) {
            String fileName = filesForRead.get(i).getName();
            String filePath = filesForRead.get(i).getPath();

            StringBuffer contents = new StringBuffer();
            BufferedReader reader = new BufferedReader(
                    new FileReader(filePath));
            char[] ch = new char[9000000];
            int n = 0;
            while ((n = reader.read(ch)) != -1) {
                contents.append(ch, 0, n);
            }
            reader.close();
            String fileContent = contents.toString();

            map.put(fileName,fileContent);
        }
    }

    public void iterateMapSearch(String searchValue){//goes through map with search value

        for(Map.Entry<String,String> entry : map.entrySet()){
            String value = entry.getValue();
            String key = entry.getKey();
            String mentionedWord = "";
            if(value.contains(searchValue)){
                int prevIndex = value.indexOf(searchValue)-1;
                char prevChar = value.charAt(prevIndex);
                int currentIndex = value.indexOf(searchValue);
                char currentChar = value.charAt(currentIndex);
                while(currentChar != ' ' && currentChar !='\n'){//looks for end of word or end of line
                    mentionedWord += value.charAt(currentIndex);
                    currentIndex++;
                    currentChar = value.charAt(currentIndex);
                }
                if(prevChar == ' ' || prevIndex == -1){//prevents emails from being included
                    if(filesToPrint.contains(key)){
                        continue;
                    }else{
                        filesToPrint.add(key + ": " + mentionedWord);
                    }
                }
            }
        }
    }
    public void printFilesToPrint(){ //prints files containing mentions
        for(String key : filesToPrint){
               System.out.println(key);}
    }

    public void printFilesToPrintSorted(){ //prints files containing mentions in alphabetical order
        for(String key : filesToPrint){
            mentionList.add(key);
        }
        java.util.Collections.sort(mentionList, String.CASE_INSENSITIVE_ORDER);
        for(String key : mentionList){
            System.out.println(key);
        }
    }

    public void generateKeywords() throws IOException{ //generates a unique list of keywords for a file
        //these are just a test

        for(String key : filesToPrint) {
            int totalWordCount = 0;
            int threshold;
            int wordAppearance = 0;
            String word = "hello";
            //words into a map:  key is word, value is wordAppearance
            //get word count of file
            //get appearance of each word

            threshold = (totalWordCount/4);
            if (wordAppearance>=threshold){
                keywords.add(word);
            }
            System.out.println("FILE:   " + key + "     KEYWORDS:   " + keywords);
            System.out.println();
            keywords.clear();
        }

    }
    //notes with no references to them have inDegree&&outdegree=0
    //STEP 1: identify file with no references to them                  DONE
    //Step 2: If a file has no in or out degrees, display them first    DONE
    //Step 3: then display a file with no in degrees but out degrees    DONE
    //Step 4: delete this file
    //Step 5: repeat 3 and 4 until all keys are listed

    //if file A has ^B in it, then B has 1 indegree and A has 1 outdegree
    //topological sort would be A, B
    //FIFO?
    

    public void topologicalSort() throws IOException{
        int degree[]=new int[2];
        for(Map.Entry<String,String> entry : map.entrySet()) {
            String value = entry.getValue();
            String key = entry.getKey();
            int in = 0;
            int out = 0;
            if (value.contains("^")) {
                out++;
            } else if (value.contains("!") && (value.indexOf("!") == 0)) {
                in++;
            }
            outDegree.put(key, out);
            inDegree.put(key, in);
            degree[0]=out;
            degree[1]=in;
            int numDegrees=degree[0]+degree[1];
            if (numDegrees==0){ keysNoReferences.add(key); }
            else if (degree[0]==1){ if (degree[1]==0){keysOutReferences.add(key); }}
            else {keysReferenced.add(key);}
        }
        topologicalPrint();
    }

    public void topologicalPrint(){
        for (String key : keysNoReferences){
            System.out.println(key);
        }
        for (String key : keysOutReferences){
            System.out.println(key);
        }
        for (String key : keysReferenced){
            System.out.println(key);
        }
    }
}
