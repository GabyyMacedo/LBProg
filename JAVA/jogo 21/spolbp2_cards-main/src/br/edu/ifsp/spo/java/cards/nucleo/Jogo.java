package br.edu.ifsp.spo.java.cards.nucleo;

import br.edu.ifsp.spo.java.cards.itens.Baralho;
import br.edu.ifsp.spo.java.cards.itens.Carta;
import br.edu.ifsp.spo.java.cards.regras.Pontuador;
import br.edu.ifsp.spo.java.cards.ui.JogoUI;

import java.util.Optional;
import java.util.Scanner;

public class Jogo {

    private Baralho baralho;
    private Jogador jogador1;
    private Jogador jogador2;
    private Pontuador pontuador;
    private JogoUI ui;

    public Jogo() {
        this.ui = new JogoUI();
        this.pontuador = this.ui.escolherPontuador();
        this.baralho = new Baralho();

        this.jogador1 = new Jogador(ui.solicitarNomeJogador(1));
        this.jogador2 = new Jogador(ui.solicitarNomeJogador(2));

        for (int i = 0; i < 2; i++) {
            jogador1.receberCarta(baralho.tirarCarta());
            jogador2.receberCarta(baralho.tirarCarta());
        }

//        Scanner sc = new Scanner(System.in);
//        System.out.println("Você deseja iniciar o jogo?"); //controle e if
//        System.out.println("(1) SIM");
//        System.out.println("(2) NAO");
//        int resposta = sc.nextInt();
//
//        if (resposta == 1) {//sim
//            turno(jogador1);
//            turno(jogador2);
//            System.out.println(this); //resultado final
//        } else {//nao
//            System.out.println("Jogo cancelado.");
//        }
    }
    public void play(){
        Optional<Jogador> talvezVencedor = Optional.empty();
        do {
            rodadaDoJogador(this.jogador1);
            rodadaDoJogador(this.jogador2);
        }
    }

    private void turno(Jogador jogador) {
//        System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
        System.out.println("\n\n");

        System.out.println("===Vez de jogador " + jogador.getNome() + " ===");
        Scanner sc = new Scanner(System.in);
        int resposta;

        do {
//            System.out.println("Cartas: " + jogador);
            System.out.println(jogador);
//            System.out.println("Cartas de " + jogador.getNome() + ": " + jogador);
            System.out.println("Pontuação: " + pontuador.verificarPontuacao(jogador.getMao()));
            System.out.println("Você deseja comprar mais uma carta?");
            System.out.println("(1) SIM");
            System.out.println("(2) NAO");
            resposta = sc.nextInt();

            if (resposta == 1) {
                jogador.receberCarta(baralho.tirarCarta());
            }

        } while (resposta == 1);

        System.out.println("Fim do turno. Pontuação do jogador " + jogador.getNome() + ": " +
                pontuador.verificarPontuacao(jogador.getMao()));
        System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");


    }

//    @Override
//    public String toString() {
//        String resultado = "===Jogo de Baralho Genérico===\n";
//        resultado += "\nJogador 1: " + jogador1;
//        resultado += "\nPontuação Jogador 1: " + pontuador.verificarPontuacao(jogador1.getMao());
//        resultado += "\n\nJogador 2: " + jogador2;
//        resultado += "\nPontuação Jogador 2: " + pontuador.verificarPontuacao(jogador2.getMao());
//        return resultado;
//    }

    public void jogar() {
        turno(jogador1);
        turno(jogador2);

        int pontuacao1 = pontuador.verificarPontuacao(jogador1.getMao());
        int pontuacao2 = pontuador.verificarPontuacao(jogador2.getMao());

        System.out.println("\n=== RESULTADO FINAL ===");
//        System.out.println("Pontuação de " + jogador1.getNome() + ": " + pontuacao1);
//        System.out.println("Pontuação de " + jogador2.getNome() + ": " + pontuacao2);

        if (pontuacao1 == 21 && pontuacao2 == 21) { //reinicia
            System.out.println("EMPATE! AMBOS FIZERAM 21 PONTOS. O JOGO SERÁ REINICIADO");
            jogar(); //reinicia

        } else if (pontuacao1 == 21) {//alguem ganhou
            System.out.println("JOGADOR " + jogador1.getNome() + "VENCEU COM 21 PONTOS");

        } else if (pontuacao2 == 21) {
            System.out.println("JOGADOR " + jogador2.getNome() + " VENCEU COM 21 PONTOS");

        } else if (pontuacao1 > 21 && pontuacao2 <= 21) { //Se um jogador tiver mais que 21: o outro jogador ganhou
            System.out.println("JOGADOR " + jogador1.getNome() + " PERDEU COM " + pontuacao1 + " PONTOS");
            System.out.println("JOGADOR " + jogador2.getNome() + " VENCEU COM " + pontuacao2 + " PONTOS");

        } else if (pontuacao2 > 21 && pontuacao1 <= 21) { //Se um jogador tiver mais que 21: o outro jogador ganhou
            System.out.println("JOGADOR " + jogador1.getNome() + " VENCEU COM " + pontuacao1 + " PONTOS");
            System.out.println("JOGADOR " + jogador2.getNome() + " PERDEU COM " + pontuacao2 + " PONTOS");

        } else if (pontuacao1 > pontuacao2 && pontuacao1 < 21) { //mais proximo(1) ganha
            System.out.println("JOGADOR " + jogador1.getNome() + " VENCEU. COM " + pontuacao1 + " PONTOS, FOI QUEM CHEGOU MAIS PERTO DE 21");

        } else if (pontuacao2 > pontuacao1 && pontuacao2 < 21) { //mais proximo(2) ganha
            System.out.println("JOGADOR " + jogador2.getNome() + " VENCEU. COM " + pontuacao2 + " PONTOS, FOI QUEM CHEGOU MAIS PERTO DE 21");

        } else if (pontuacao2 == pontuacao1 && pontuacao2 < 21 ) { //mais proximo(2) ganha
            System.out.println("EMPATE! AMBOS FICARAM COM" + pontuacao1 + " PONTOS. O JOGO SERÁ REINICIADO.");

        } else {
            System.out.println("EMPATE! AMBOS ESTOURARAM OS 21 PONTOS. O JOGO SERÁ REINICIADO.");
            jogar(); //reinicia
        }
    }
}


