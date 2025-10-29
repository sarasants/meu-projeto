public class NormalizadorDeNomes
{
    String original;
    
    NormalizadorDeNomes(String original){
        this.original = original;
    }
    
    String trimPadrao(){
        return this.original.trim();
    }
    
    String somenteUmEspaco(){
        return this.original.replaceAll("//s+", " ");
    }
    
    String capitalizar(){
        String[] div = this.original.split(" ");
        String r = "";
        for(String s: div){
            char p = s.charAt(0);
            r = Character.toUpperCase(p) + s.substring(1).toLowerCase() + " ";
        }
        return r;
    }
    
}
