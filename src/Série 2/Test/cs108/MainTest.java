package cs108;

import org.junit.jupiter.api.Test;
import org.junit.platform.commons.JUnitException;

import java.io.IOException;
import java.util.Arrays;

class MainTest {

    @Test
    void byteFrequencies() throws IOException {
        for (int i = 0; i <= 5; i ++) {
            System.out.println(Arrays.toString(Main.byteFrequencies("file" + i + ".bin")));
        }
    }

    @Test
    void average() throws IOException {
        for (int i = 0; i <= 5; i ++) {
            System.out.println(Main.average(Main.byteFrequencies("file" + i + ".bin")));
        }
    }

    @Test
    void entropy() throws IOException {
        for (int i = 0; i <= 5; i ++) {
            System.out.println(Main.entropy(Main.byteFrequencies("file" + i + ".bin")));
        }
    }


    @Test
    void stemplot() throws IOException {
        for (int i = 0; i <= 5; i ++){
            Main.stemplot(Main.byteFrequencies("file" + i + ".bin"));
        }
    }
}