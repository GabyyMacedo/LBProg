package br.edu.ifsp.spo.java.cards;

public class Jogo { //classe que represnta o jogo
    private final Baralho baralho;
    private final Jogador player1;
    private final Jogador player2;
    public Jogo() {
        //cria baralho
        this.baralho = new Baralho();
        //cria jogador 1
        this.player1 = new Jogador("Marina"); //cria novo jogador
        //cria jogador 2
        this.player2 = new Jogador("Amorim");
        //Carta carta = this.baralho.tirarCarta(); //tira uma carta e da para o jogador 1

        int tamanhoInicialMao = 2;
        for (int i = 0; i < tamanhoInicialMao; i++) {
            this.player1.receberCarta(this.baralho.tirarCarta());
            this.player2.receberCarta(this.baralho.tirarCarta());
        }
    }

    @Override
    public String toString() {
        String resultado = "\nJogo de Baralho Genérico\n";
        resultado += "\nJogadores: "; //resultado = resultado + "\nJogadores: ";
        resultado += "\n----------" + this.player1.toString();
        resultado += "\n-" + this.player2.toString();

        return resultado;
    }
}
