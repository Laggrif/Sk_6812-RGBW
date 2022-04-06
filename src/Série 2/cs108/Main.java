package cs108;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {

    static int[] byteFrequencies(String fileName) throws IOException {
        int[] byteFrequencies  = new int[256];
        try (InputStream stream = new FileInputStream(fileName)){
            int b;
            while ((b = stream.read()) != -1){
                byteFrequencies[b] ++;
            }
        }
        return byteFrequencies;
    }

    static double average(int[] freq) {
        double total = 0;
        for (int i = 0; i <= 255; i ++){
            total += (i * freq[i]);
        }
        return total / 256.0;
    }

    static double log_b(double x, int b){
        return Math.log(x) / Math.log(b);
    }

    static double entropy(int[] freq) {
        double sum = 0;
        for (int i = 0; i <= 255; i ++){
            if (freq[0] != 0) {
                double prob = freq[i] / 256.0;
                sum -= prob * log_b(prob, 2);
            }
        }
        return sum;
    }

    static double maxFreq(int[] freq) {
        double maxFreq = 0;
        for (int i = 0; i <= freq.length - 1; i ++){
            if (freq[i] > maxFreq) maxFreq = freq[i];
        }
        return maxFreq;
    }

    static void stemplot(int[] freq){
        int reductor = (int) Math.ceil(maxFreq(freq) / 80.0);
        StringBuilder vals = new StringBuilder();
        for (int i = 0; i <= 255; i ++){
            int mod = i % 10;
            for (int j = 0; j <= freq[i] / reductor; j ++) {
                vals.append(i - (i / 10) * 10);
            }
            if (mod == 9) {
                System.out.println(i / 10 + " | " + vals);
                vals = new StringBuilder();
            }
        }
        System.out.println(25 + " | " + vals);
    }
}
