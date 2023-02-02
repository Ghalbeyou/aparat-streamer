
package ir.ghalbeyou.aparat_streamer_gui.Exe;

import java.io.IOException;

public class RunRenderer {
    public static boolean Render(String location, String key) throws IOException{
        ProcessBuilder pb = new ProcessBuilder("C:\\Renderer.exe", "-k=" + '"' + key + '"', "-l=" + '"' + location + '"');
        Process p = pb.start();
        return p.isAlive() != false;
    }
}
