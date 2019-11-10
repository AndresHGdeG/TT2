/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ManagerBean;

import Clases.Noticia;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.Serializable;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.StringTokenizer;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;
import javax.faces.context.ExternalContext;
import javax.faces.context.FacesContext;
import javax.servlet.ServletContext;
import javax.servlet.http.HttpServletRequest;
import org.primefaces.PrimeFaces;

/**
 *
 * @author Andrew
 */
@ManagedBean(name = "mBClasificador")
@SessionScoped
public class MBClasificador implements Serializable {

    /**
     * Creates a new instance of ImportarNoticias
     */
    private ArrayList<Noticia> noticias;
    private ArrayList<Noticia> noticiasAyer;
    private ArrayList<Noticia> noticiasDosDias;
    private ArrayList<Noticia> noticiasMasDias;
    private String dateToday;
    private String dateYesterday;
    private String dateTwoDays;
    private int numNoticias = 0;
    private String seccion = "";
    
    private int seccionSeleccionada =0;
    private int cargarNoticias=0;

    public MBClasificador() {
        dateToday = new SimpleDateFormat("dd/MM/yyyy").format(new Date());
        dateYesterday = new SimpleDateFormat("dd/MM/yyyy").format(yesterday(1));
        dateTwoDays = new SimpleDateFormat("dd/MM/yyyy").format(yesterday(2));
        noticias = new ArrayList<>();
        noticiasAyer = new ArrayList<>();
        noticiasDosDias = new ArrayList<>();
        noticiasMasDias = new ArrayList<>();
    }

    private Date yesterday(int day) {
        final Calendar cal = Calendar.getInstance();
        cal.add(Calendar.DATE, -day);
        return cal.getTime();
    }
    
    public void ModalCargarNoticias(){
        
        if (this.cargarNoticias==1){
        PrimeFaces current = PrimeFaces.current();
        current.executeScript("PF('mostrar').show();");
        }
        
    }
        public void destroyWorld() {
            System.out.println("Funciono");
    }
    
    

    public void CargarNoticias() {

        this.NombreSeccion(this.seccionSeleccionada);
        System.out.println("Entre a cargar");
        System.out.println("Seccion="+this.seccionSeleccionada);
        noticias.clear();
        try {

            ServletContext servletContext = (ServletContext) FacesContext.getCurrentInstance().getExternalContext().getContext();
            String pathServer = servletContext.getRealPath("/resources");

            //FileReader f = new FileReader(pathServer + "/Recolector/Clasificador/noticiasClasificadas_" + this.seccionSeleccionada + ".txt");
            FileReader f = new FileReader(pathServer + "/Recolector/Clasificador/noticiasClasificadas_3.txt");

            BufferedReader brNoticias = new BufferedReader(f);
            String noticia_n = "";
            noticia_n = brNoticias.readLine();

            while ((noticia_n = brNoticias.readLine()) != null) {

                StringTokenizer tokens = new StringTokenizer(noticia_n, "&&&&&");
                String id = tokens.nextToken();
                String url = tokens.nextToken();
                String titulo = tokens.nextToken();
                String autor = tokens.nextToken();
                String fecha = tokens.nextToken();
                String descripcion = tokens.nextToken();
                Date temp =  new SimpleDateFormat("dd/MM/yyyy").parse(fecha);
                Date tempM = new SimpleDateFormat("dd/MM/yyyy").parse(dateTwoDays);
                Noticia noticiaAux = new Noticia(titulo, autor, url, fecha, descripcion);
                if (fecha.equalsIgnoreCase(dateToday)) {
                    noticias.add(noticiaAux);
                } else if (fecha.equalsIgnoreCase(dateYesterday)) {
                    noticiasAyer.add(noticiaAux);
                } else if(fecha.equalsIgnoreCase(dateTwoDays)){
                    noticiasDosDias.add(noticiaAux);
                } else if(temp.before(tempM)){
                    noticiasMasDias.add(noticiaAux);
                }
                this.numNoticias = Integer.parseInt(id);

            }
            
                    ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
        ec.redirect(((HttpServletRequest) ec.getRequest()).getRequestURI());

        } catch (Exception e) {
            System.out.println("Error: " + e);
        }

    }

    public void NombreSeccion(int seccionNum) {

        switch (seccionNum) {
            case 0:
                this.seccion = "Deportes";
                break;
            case 1:
                this.seccion = "Economía";
                break;
            case 2:
                this.seccion = "Politica";
                break;
            case 3:
                this.seccion = "Cultura";
                break;
            case 4:
                this.seccion = "Ciencia y tecnología";
                break;
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

    public void limpiarNoticias() {
        noticias.clear();
        noticiasAyer.clear();
        noticiasDosDias.clear();
        noticiasMasDias.clear();
    }

    public ArrayList<Noticia> getNoticiasAyer() {
        return noticiasAyer;
    }

    public void setNoticiasAyer(ArrayList<Noticia> noticiasAyer) {
        this.noticiasAyer = noticiasAyer;
    }

    public ArrayList<Noticia> getNoticiasDosDias() {
        return noticiasDosDias;
    }

    public void setNoticiasDosDias(ArrayList<Noticia> noticiasDosDias) {
        this.noticiasDosDias = noticiasDosDias;
    }

    public String getDateToday() {
        return dateToday;
    }

    public void setDateToday(String dateToday) {
        this.dateToday = dateToday;
    }

    public String getDateYesterday() {
        return dateYesterday;
    }

    public void setDateYesterday(String dateYesterday) {
        this.dateYesterday = dateYesterday;
    }

    public String getDateTwoDays() {
        return dateTwoDays;
    }

    public void setDateTwoDays(String dateTwoDays) {
        this.dateTwoDays = dateTwoDays;
    }

    public ArrayList<Noticia> getNoticiasMasDias() {
        return noticiasMasDias;
    }

    public void setNoticiasMasDias(ArrayList<Noticia> noticiasMasDias) {
        this.noticiasMasDias = noticiasMasDias;
    }
    
    
    public int getSeccionSeleccionada() {
        return seccionSeleccionada;
    }

    public void setSeccionSeleccionada(int seccionSeleccionada) {
        this.seccionSeleccionada = seccionSeleccionada;
    }

    public int getCargarNoticias() {
        return cargarNoticias;
    }

    public void setCargarNoticias(int cargarNoticias) {
        this.cargarNoticias = cargarNoticias;
    }
    
    

}
