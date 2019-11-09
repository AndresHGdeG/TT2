/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ManagerBean;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.ManagedProperty;
import javax.faces.bean.SessionScoped;
import javax.faces.context.ExternalContext;
import javax.faces.context.FacesContext;
import javax.servlet.ServletContext;
import javax.servlet.http.HttpServletRequest;

/**
 *
 * @author Andrew
 */
@ManagedBean(name = "mBTabMenu")
@SessionScoped
public class MBTabMenu implements Serializable {

    @ManagedProperty("#{mBClasificador}")
    private MBClasificador clasificador;
    /**
     * Creates a new instance of MBTabMenu
     */
    private int index = 0;
    private String seleccion = "";
    private final ArrayList<String> make = new ArrayList<>();
    private final ArrayList<String> sitios = new ArrayList<>();

    public MBTabMenu() throws IOException {
        permission();
        sites();
        modifyFiles();
        addMake();
    }

    public void sites() {
        sitios.add("aristegui");
        sitios.add("azteca");
        sitios.add("economista");
        sitios.add("jornada");
        sitios.add("proceso");
        sitios.add("sopitas");
        sitios.add("universal");
    }

    public void inicio() throws IOException {
        clasificador.limpiarNoticias();

        ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
        ec.redirect(((HttpServletRequest) ec.getRequest()).getRequestURI());
    }

    public void SeleccionSeccion(int index) throws IOException, InterruptedException {
        String pathServer = site();
        this.index = index;
        this.seleccion = "Ya quedo" + index;
        System.out.println("Entre");
        File tempFile = new File(pathServer + "/Recolector/Clasificador/noticias.csv");
        System.out.println(tempFile);
        if (tempFile.exists()) {
            Thread.sleep(3000);
            System.out.println("Noticias recolectadas");
            Process pUnit = Runtime.getRuntime().exec(pathServer + "/Recolector/Makefile");
            pUnit.waitFor();
            System.out.println("Noticias unidas");
            createMakeToClassify(index - 1);
            Process pClassify = Runtime.getRuntime().exec(pathServer + "/Recolector/Clasificador/Makefile");
            pClassify.waitFor();
            System.out.println("Noticias Clasificadas");

        } else {
            process(index - 1);
        }
        clasificador.CargarNoticias(index - 1);

        ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
        ec.redirect(((HttpServletRequest) ec.getRequest()).getRequestURI());
    }

    public String site() {
        ServletContext servletContext = (ServletContext) FacesContext.getCurrentInstance().getExternalContext().getContext();
        String pathServer = servletContext.getRealPath("/resources");
        return pathServer;
    }

    public void permission() throws IOException {
        String pathServer = site();
        System.out.println(pathServer);
        Process p = Runtime.getRuntime().exec("chmod 777 -R " + pathServer);
    }

    public void modifyFiles() throws FileNotFoundException, IOException {
        String pathServer = site() + "/Recolector/";
        FileWriter fw = null;
        BufferedWriter bw = null;
        for (String sitio : sitios) {
            File file = new File(pathServer + "Make/" + sitio + "/Makefile");
            String newPath = site() + "/Recolector";
            fw = new FileWriter(file);
            bw = new BufferedWriter(fw);
            bw.write("all:\n");
            bw.write("\tcd " + newPath + "\n");
            bw.write("\tscrapy crawl " + sitio + " -t csv");
            bw.flush();
            fw.close();
        }
        File f = new File(pathServer + "/Makefile");
        fw = new FileWriter(f);
        bw = new BufferedWriter(fw);
        bw.write("all:\n");
        bw.write("\tcd " + pathServer + "\n");
        bw.write("\tpython concat.py");
        bw.flush();
        fw.close();
    }

    public void addMake() {
        String pathServer = site();
        make.add(pathServer + "/Recolector/Make/azteca/Makefile");
        make.add(pathServer + "/Recolector/Make/aristegui/Makefile");
        make.add(pathServer + "/Recolector/Make/economista/Makefile");
        make.add(pathServer + "/Recolector/Make/jornada/Makefile");
        make.add(pathServer + "/Recolector/Make/proceso/Makefile");
        make.add(pathServer + "/Recolector/Make/sopitas/Makefile");
        make.add(pathServer + "/Recolector/Make/universal/Makefile");
    }
    
//    public void runProcess(String command) throws IOException, InterruptedException{
//        ProcessBuilder p = new ProcessBuilder(command);
//        Process process = p.start();
//        
//        Scanner scan = new Scanner((Readable) process.getOutputStream());
//        
//        while(scan.hasNext()){
//            System.out.println(scan.next());
//        }
//    }

    public void process(int seccion) throws IOException, InterruptedException {
        String pathServer = site();
        System.out.println("Creando proceso..");
        for (String string : make) {
            //runProcess(string);
            System.out.println("...");
            Process aux = Runtime.getRuntime().exec(string);
            aux.waitFor(12, TimeUnit.SECONDS);
            aux.destroyForcibly();
        }
        //Thread.sleep(90000);
//
//        boolean no_exit = true;
//        while (no_exit) {
//            no_exit = false;
//            for (Process process : p) {
//                try {
//                    process.exitValue();
//                    System.out.println("Estoy dentro del try");
//                } catch (Exception e) {
//                    no_exit = true;
//                    System.out.println("Estoy dentro del catch");
//                }
//            }
//            Thread.sleep(1000);
//        }

        /*for (String sitio : sitios) {
            int i = 0;
            while (i < 7) {
                File tempdir = new File(pathServer + "/Recolector/" + sitio);
                if (tempdir.exists()) {
                    i++;
                }
            }
        }*/
        System.out.println("Noticias recolectadas");
        Process pUnit = Runtime.getRuntime().exec(pathServer + "/Recolector/Makefile");
//runProcess(pathServer + "/Recolector/Makefile");
        pUnit.waitFor();
        System.out.println("Noticias unidas");
        createMakeToClassify(seccion);
        Process pClassify = Runtime.getRuntime().exec(pathServer + "/Recolector/Clasificador/Makefile");
        //runProcess(pathServer + "/Recolector/Clasificador/Makefile");
        pClassify.waitFor();
        System.out.println("Noticias Clasificadas");
    }

    public void createMakeToClassify(int seccion) throws IOException {
        String pathServer = site() + "/Recolector/Clasificador";
        FileWriter fw = null;
        BufferedWriter bw = null;
        File f = new File(pathServer + "/Makefile");
        fw = new FileWriter(f);
        bw = new BufferedWriter(fw);
        bw.write("all:\n");
        bw.write("\tcd " + pathServer + "\n");
        bw.write("\tpython Clasifica.py 'noticias.csv' 'Modelo_MSV.save' " + seccion);
        bw.flush();
        fw.close();
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
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
