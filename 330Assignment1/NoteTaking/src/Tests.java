import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import java.io.*;

public class Tests {
    Search search = new Search();
    Note note = new Note();
    Main main = new Main();
    static String path = "C:\\Users\\Eva\\IdeaProjects\\330Assignment1\\Too-Many-Cats";

    @Test
    public void testOptionAOutput() throws IOException{
        //option A should have a .txt and @ output
        search.searchBy("a");
        boolean bool;
        for(String str :note.filesToPrint){
            if(str.contains("@")&&str.contains(".txt")){
                bool = true;
            }else{
                bool = false;
            }
            assertEquals(bool,true);
        }
    }

    @Test
    public void testOptionBOutput()throws IOException{
        //option B should have a .txt and @ output alphabetized
        search.searchBy("b");
        boolean bool;
        for(String str :note.filesToPrint){
            if(str.contains("@")&&str.contains(".txt")){
                bool = true;
            }else{
                bool = false;
            }
            assertEquals(bool,true);
        }
    }

    @Test
    public void testOptionCOutput()throws IOException{
        //option C should have a .txt file and a list of keywords
        search.searchBy("c");
        boolean bool;
        for(String str :note.filesToPrint){
            if(str.contains(".txt")||str.contains("\n")){
                bool = true;
            }else{
                bool = false;
            }
            assertEquals(bool,true);
        }
    }


    @Test
    public void testOptionDOutput()throws IOException{
        //option D should have a .txt and list of keywords alphabetized
        search.searchBy("d");
        boolean bool;
        for(String str :note.filesToPrint){
            if(str.contains(".txt")||str.contains("=")){
                bool = true;
            }else{
                bool = false;
            }
            assertEquals(bool,true);
        }
    }


    @Test
    public void testOptionEOutput()throws IOException{
        //option E should have a .txt output from a search
        note.readFiles(main.path);
        note.getNotesFromFiles();
        search.searchBy("e");
        boolean bool;
        for(String str :note.filesToPrint){
            if(str.contains(".txt")){
                bool = true;
            }else{
                bool = false;
            }
            assertEquals(bool,true);
        }
    }


    @Test
    public void testOptionFOutput()throws IOException{
        //Option F should list all .txt files
        search.searchBy("e");
        boolean bool;
        for(String str :note.filesToPrint){
            if(str.contains(".txt")){
                bool = true;
            }else{
                bool = false;
            }
            assertEquals(bool,true);
        }
    }


}