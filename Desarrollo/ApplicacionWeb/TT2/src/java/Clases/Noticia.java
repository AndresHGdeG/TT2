/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Clases;

/**
 *
 * @author Andrew
 */
public class Noticia {
    
    private String titulo;
    private String url;
    private String fecha;
    private String resumen;
    
    public Noticia(){
    }
    
    public Noticia(String titulo, String url, String fecha){
        this.titulo=titulo;
        this.url=url;
        this.fecha=fecha;
    }
    
    public Noticia(String titulo, String url, String fecha,String resumen){
        this.titulo=titulo;
        this.url=url;
        this.fecha=fecha;
        this.resumen=resumen;
        
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    
    public String getTitulo() {
        return titulo;
    }

    public String getUrl() {
        return url;
    }

    public String getFecha() {
        return fecha;
    }

    public String getResumen() {
        return resumen;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public void setResumen(String resumen) {
        this.resumen = resumen;
    }
    
    
    
}
