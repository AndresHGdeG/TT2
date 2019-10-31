package web;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;

/**
 *
 * @author danielmezam
 */
@ManagedBean (name = "menuBean")
@RequestScoped
public class menuSecciones {
        
    private String msj ;

    public menuSecciones() {
        msj = "hol";
    }
    
    public void showPage(int idSection){
        
    }    
    
    
}
