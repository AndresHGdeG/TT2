/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ManagerBean;


import Clases.Noticia;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.StringTokenizer;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;
import javax.faces.bean.SessionScoped;
import javax.faces.context.FacesContext;
import javax.servlet.ServletContext;

/**
 *
 * @author Andrew
 */
@ManagedBean (name="mBClasificador")
@SessionScoped
public class MBClasificador implements Serializable{

    /**
     * Creates a new instance of ImportarNoticias
     */
    private ArrayList<Noticia> noticias;
    private int numNoticias=0;
    private String seccion="";
    
    public MBClasificador() {
        noticias=new ArrayList<Noticia>();
                
    }
    
    public void CargarNoticias(int seccion){
        
        this.NombreSeccion(seccion);
        noticias.clear();
        try {
            
        ServletContext servletContext = (ServletContext) FacesContext.getCurrentInstance().getExternalContext().getContext();
        String pathServer = servletContext.getRealPath("/resources");
        
      
        FileReader f = new FileReader( pathServer+"/Noticias/noticiasClasificadas.txt");

 
             BufferedReader brNoticias=new BufferedReader(f);
             String noticia_n="";
             noticia_n=brNoticias.readLine();
             
             while ((noticia_n=brNoticias.readLine())!=null){
               // System.out.println(noticia_n);
                 
                 StringTokenizer tokens=new StringTokenizer(noticia_n,"&&&&&");
                 String id=tokens.nextToken();
                 String url=tokens.nextToken();
                 String titulo=tokens.nextToken();
                 String autor=tokens.nextToken();
                 String fecha=tokens.nextToken();
                 //String descripcion=tokens.nextToken();
                 
                 Noticia noticiaAux=new Noticia(titulo,url,fecha);
                 noticias.add(noticiaAux);
                 this.numNoticias=Integer.parseInt(id);
                 
                 
             }
             
        } catch (Exception e) {
            System.out.println("Error: "+e);
        }
       
     /*   
        Noticia noticia1 = new Noticia("titulo 1 "+this.seccion,"http://quotes.toscrape.com/page/1","01/01/2019");
        Noticia noticia2 = new Noticia("titulo 2 "+this.seccion,"http://quotes.toscrape.com/page/2","01/01/2019");
        Noticia noticia3 = new Noticia("titulo 3 "+this.seccion,"http://quotes.toscrape.com/page/3","01/01/2019");
        Noticia noticia4 = new Noticia("titulo 4 "+this.seccion,"http://quotes.toscrape.com/page/4","01/01/2019");
        Noticia noticia5 = new Noticia("titulo 5 "+this.seccion,"http://quotes.toscrape.com/page/5","01/01/2019");
        Noticia noticia6 = new Noticia("titulo 6 "+this.seccion,"http://quotes.toscrape.com/page/6","01/01/2019");
        Noticia noticia7 = new Noticia("titulo 6 "+this.seccion,"http://quotes.toscrape.com/page/7","01/01/2019");
        
        Noticia noticia8 = new Noticia("titulo 8 "+this.seccion,"http://quotes.toscrape.com/page/8","01/01/2019");
        Noticia noticia9 = new Noticia("titulo 9 "+this.seccion,"http://quotes.toscrape.com/page/9","01/01/2019");
        Noticia noticia10 = new Noticia("titulo 10 "+this.seccion,"http://quotes.toscrape.com/page/10","01/01/2019");
        Noticia noticia11 = new Noticia("titulo 11 "+this.seccion,"http://quotes.toscrape.com/page/11","01/01/2019");
        Noticia noticia12 = new Noticia("titulo 12 "+this.seccion,"http://quotes.toscrape.com/page/12","01/01/2019");
        Noticia noticia13 = new Noticia("titulo 13 "+this.seccion,"http://quotes.toscrape.com/page/13","01/01/2019");
        Noticia noticia14 = new Noticia("titulo 14 "+this.seccion,"http://quotes.toscrape.com/page/14","01/01/2019");
        
        
        noticias.add(noticia1);
        noticias.add(noticia2);
        noticias.add(noticia3);
        noticias.add(noticia4);
        noticias.add(noticia5);
        noticias.add(noticia6);
        noticias.add(noticia7);
        
        noticias.add(noticia8);
        noticias.add(noticia9);
        noticias.add(noticia10);
        noticias.add(noticia11);
        noticias.add(noticia12);
        noticias.add(noticia13);
        noticias.add(noticia14);*/
       
               
        
    }
    
    public void NombreSeccion(int seccionNum){
        
        switch(seccionNum){
            case 0: this.seccion="Deportes"; break; 
            case 1: this.seccion="Economía"; break;
            case 2: this.seccion="Politica"; break;
            case 3: this.seccion="Cultura"; break;
            case 4: this.seccion="Ciencia y tecnología"; break;
        }
    }

    public ArrayList<Noticia> getNoticias() {
        return noticias;
    }

    public int getNumNoticias() {
        return numNoticias;
    }

    public void setNoticias(ArrayList<Noticia> noticias) {
        this.noticias = noticias;
    }

    public void setNumNoticias(int numNoticias) {
        this.numNoticias = numNoticias;
    }

    public String getSeccion() {
        return seccion;
    }

    public void setSeccion(String seccion) {
        this.seccion = seccion;
    }


    
    
    

}
