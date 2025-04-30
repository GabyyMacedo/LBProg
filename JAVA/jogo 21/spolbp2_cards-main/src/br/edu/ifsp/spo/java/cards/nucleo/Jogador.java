package br.edu.ifsp.spo.java.cards.nucleo;

import br.edu.ifsp.spo.java.cards.itens.Carta;

import java.util.ArrayList;
import java.util.List;

public class Jogador {

    private final String nome;
    private final List<Carta> mao;

    public Jogador(String nome){
        this.nome = nome;
        this.mao = new ArrayList<>();
    }

    public void receberCarta(Carta carta){
        this.mao.add(carta);
    }

    @Override
    public String toString() {
//        String resultado = "\nJogador: " + this.nome;
        String resultado = "A mão de jogador é:";

//        resultado += "\n A mão de jogador é:";

        for(Carta carta : this.mao){
            resultado += "\n- " + carta.toString();
        }

        return resultado;
    }

    public List<Carta> getMao() {
        return this.mao;
    }

    public String getNome() {
        return this.nome;
    }
}
