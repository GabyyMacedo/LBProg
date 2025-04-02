package br.edu.ifsp.spo.java.cards;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Jogador { //classe que representa o jogador
    //escopo da classe Jogador
    private final String nome; //local que armazena o nome do jogador --> definição da variável/atributo
    private List<Carta> mao; //lista que armazena as cartas que o jogador possui
    public Jogador(String nome){  //construtor (executado no momento de crianção da instancia da classe
        this.nome = nome; //this.nome --> se refere ao escopo da classe || =nome --> se refere ao nome do parenteses do public Jogador
        this.mao = new ArrayList<>(); //nao precisa escrever Carta dentro dos <>
    }
    //receber carta  e adicionar à mão do jogador
    //método
    public void receberCarta(Carta carta){
        //void: não retorna nada
        this.mao.add(carta);
    }
    @Override
    public String toString() {
        String resultado = "\nJogador: " + this.nome;
        resultado += "\nA mão do jogador é: ";
        for (Carta carta:this.mao){
            resultado += "\n"+carta.toString();
        }
        return resultado;

   }
}

//classe: tipo de dado ex: jogador
//instancia: dado da classe ex: daniel