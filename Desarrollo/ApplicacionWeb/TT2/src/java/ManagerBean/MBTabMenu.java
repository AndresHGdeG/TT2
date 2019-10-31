/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ManagerBean;

import java.io.IOException;
import java.io.Serializable;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.ManagedProperty;
import javax.faces.bean.SessionScoped;
import javax.faces.context.ExternalContext;
import javax.faces.context.FacesContext;
import javax.servlet.http.HttpServletRequest;

/**
 *
 * @author Andrew
 */
@ManagedBean (name="mBTabMenu")
@SessionScoped
public class MBTabMenu implements Serializable{

    @ManagedProperty("#{mBClasificador}")
private MBClasificador clasificador;   
    /**
     * Creates a new instance of MBTabMenu
     */
    private int index=0;
    private String seleccion="";
    
    public MBTabMenu(){
       // MBClasificador clasificador=new  MBClasificador();
    }

    public void SeleccionSeccion(int index) throws IOException{
        this.index=index;
        this.seleccion="Ya quedo" +index;
        System.out.println("Entre");
        
        
        clasificador.CargarNoticias(index-1);
        
        ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
        ec.redirect(((HttpServletRequest) ec.getRequest()).getRequestURI());
       
    }
    
    
    
    public int getIndex(){
        return index;
    }
    public void setIndex(int index){
        this.index=index;
    }

    public String getSeleccion() {
        return seleccion;
    }

    public void setSeleccion(String seleccion) {
        this.seleccion = seleccion;
    }

    public MBClasificador getClasificador() {
        return clasificador;
    }

    public void setClasificador(MBClasificador clasificador) {
        this.clasificador = clasificador;
    }
    
 
    
}
