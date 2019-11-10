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
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributeView;
import java.nio.file.attribute.BasicFileAttributes;
import java.nio.file.attribute.FileTime;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import static java.time.OffsetTime.now;
import java.util.ArrayList;
import java.util.Date;
import java.util.Locale;
import java.util.concurrent.TimeUnit;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.ManagedProperty;
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
@ManagedBean(name = "mBTabMenu")
@SessionScoped
public class MBTabMenu implements Serializable {

    @ManagedProperty("#{mBClasificador}")
    private MBClasificador clasificador;
    /**
     * Creates a new instance of MBTabMenu
     */
    private int index = 0;
    private final ArrayList<String> make = new ArrayList<>();
    private final ArrayList<String> sitios = new ArrayList<>();
    private Date actualHour;
    private Date fileCreartionHour;

    public MBTabMenu() throws IOException {
        permission();
        sites();
        modifyFiles();
        addMake();
    }

    public void permission() throws IOException {
        String pathServer = site();
        System.out.println(pathServer);
        Process p = Runtime.getRuntime().exec("chmod 777 -R " + pathServer);
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

    public void inicio() throws IOException {
        clasificador.limpiarNoticias();
        this.index = 0;

        ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
        ec.redirect(((HttpServletRequest) ec.getRequest()).getRequestURI());
    }

    public void SeleccionSeccion(int index) throws IOException, InterruptedException, ParseException {
        String pathServer = site();
        this.index = index;
        File tempFile = new File(pathServer + "/Recolector/Clasificador/noticiasClasificadas_" + (this.index - 1) + ".txt");

        if (!tempFile.exists()) {
            clasificarNoticias(index - 1);
            //clasificador.ClasificarNoticias(index - 1);
            System.out.println("Noticias Clasificadas");
        } else {
            actualHour = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss").parse(new SimpleDateFormat("dd/MM/yyyy HH:mm:ss").format(new Date(System.currentTimeMillis() - 3600 * 4000)));
            System.out.println("Actual time:" + actualHour);
            fileCreartionHour = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss").parse(new SimpleDateFormat("dd/MM/yyyy HH:mm:ss").format(getCreationTime(tempFile).toMillis()));
            System.out.println("Creation time:" + fileCreartionHour);
            if (fileCreartionHour.before(actualHour)) {
                //Aquí se debe llamar al método que recolecta noticias
                System.out.println("Ya caduco la hora del archivo");
            } else if (actualHour.before(fileCreartionHour)) {
                //Quiere decir que aún no han transcurrido 4 horas
                System.out.println("Aun no");

            }
        }

        //clasificador.CargarNoticias(index - 1);
        Thread.sleep(2000); //ESte sleep es para ver el modal que descarga noticias, solo es de prueba
        this.CerrarModalDescarga();
        clasificador.setSeccionSeleccionada(index - 1);
        clasificador.setCargarNoticias(1);
        clasificador.ModalCargarNoticias();

    }

    public void CerrarModalDescarga() {

        PrimeFaces current = PrimeFaces.current();
        current.executeScript("PF('descarga').hide();");

    }

    public static FileTime getCreationTime(File file) throws IOException {
        Path p = Paths.get(file.getAbsolutePath());
        BasicFileAttributes view
                = Files.getFileAttributeView(p, BasicFileAttributeView.class)
                        .readAttributes();
        FileTime fileTime = view.creationTime();
        return fileTime;
    }

    public String site() {
        ServletContext servletContext = (ServletContext) FacesContext.getCurrentInstance().getExternalContext().getContext();
        String pathServer = servletContext.getRealPath("/resources");
        return pathServer;
    }

    public void clasificarNoticias(int seccion) throws IOException, InterruptedException {
        String pathServer = site();
        System.out.println("Creando proceso..");
        for (String string : make) {
            System.out.println("...");
            Process aux = Runtime.getRuntime().exec(string);
            aux.waitFor(12, TimeUnit.SECONDS);
            aux.destroyForcibly();
        }
        //Thread.sleep(90000);

        System.out.println("Noticias recolectadas");
        Process pUnit = Runtime.getRuntime().exec(pathServer + "/Recolector/Makefile");
//      runProcess(pathServer + "/Recolector/Makefile");
        pUnit.waitFor();
        System.out.println("Noticias unidas");
        createMakeToClassify();
        Process pClassify = Runtime.getRuntime().exec(pathServer + "/Recolector/Clasificador/Makefile");
        //runProcess(pathServer + "/Recolector/Clasificador/Makefile");
        pClassify.waitFor();
        System.out.println("Noticias Clasificadas");
    }

    public void createMakeToClassify() throws IOException {
        String pathServer = site() + "/Recolector/Clasificador";
        FileWriter fw = null;
        BufferedWriter bw = null;
        File f = new File(pathServer + "/Makefile");
        fw = new FileWriter(f);
        bw = new BufferedWriter(fw);
        bw.write("all:\n");
        bw.write("\tcd " + pathServer + "\n");
        bw.write("\tpython Clasifica.py 'noticias.csv' 'Modelo_MSV.save'");
        bw.flush();
        fw.close();
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public MBClasificador getClasificador() {
        return clasificador;
    }

    public void setClasificador(MBClasificador clasificador) {
        this.clasificador = clasificador;
    }

}
