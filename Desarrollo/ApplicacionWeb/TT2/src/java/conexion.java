
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;

/**
 *
 * @author danielmezam
 */
@ManagedBean
@SessionScoped
public class conexion {

    private String command = "/home/danielmezam/Escritorio/TT2/Corpus/Deportes/deportes/Makefile";

    public conexion() {
    }

    public void process() throws IOException {
        System.out.println("Creando proceso..");
        Process p = Runtime.getRuntime().exec(command);
        //ProcessBuilder pb = new ProcessBuilder(command);
        //BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
        try (BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()))) {                                
          String line;                                                                                                         
          while ((line = br.readLine()) != null)  {                                                                            
             System.out.println(line);                                                                                        
          }                                                                                                                    
      }  
    }

    public static void main(String[] args) throws IOException {
        conexion con = new conexion();
        con.process();
    }

}
