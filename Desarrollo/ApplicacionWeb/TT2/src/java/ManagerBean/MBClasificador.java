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
import javax.faces.context.FacesContext;
import javax.servlet.ServletContext;

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
    private int numNoticias = 0;
    private String seccion = "";
    private String dateToday;
    private String dateYesterday;

    public MBClasificador() {
        noticias = new ArrayList<Noticia>();
        dateToday = new SimpleDateFormat("dd/MM/yyyy").format(new Date());
        dateYesterday = new SimpleDateFormat("dd/MM/yyyy").format(yesterday());
    }

    private Date yesterday() {
        final Calendar cal = Calendar.getInstance();
        cal.add(Calendar.DATE, -1);
        return cal.getTime();
    }

    public void CargarNoticias(int seccion) {

        this.NombreSeccion(seccion);
        noticias.clear();
        try {

            ServletContext servletContext = (ServletContext) FacesContext.getCurrentInstance().getExternalContext().getContext();
            String pathServer = servletContext.getRealPath("/resources");

            FileReader f = new FileReader(pathServer + "/Recolector/Clasificador/noticiasClasificadas_" + seccion +".txt");

            BufferedReader brNoticias = new BufferedReader(f);
            String noticia_n = "";
            noticia_n = brNoticias.readLine();

            while ((noticia_n = brNoticias.readLine()) != null) {
                // System.out.println(noticia_n);

                StringTokenizer tokens = new StringTokenizer(noticia_n, "&&&&&");
                String id = tokens.nextToken();
                String url = tokens.nextToken();
                String titulo = tokens.nextToken();
                String autor = tokens.nextToken();
                String fecha = tokens.nextToken();
                String descripcion = tokens.nextToken();

                Noticia noticiaAux = new Noticia(titulo, autor, url, fecha, descripcion);
                noticias.add(noticiaAux);
                this.numNoticias = Integer.parseInt(id);

            }

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

}
