bonequinhos = [
    'saindo.gif',
    'dormindo.gif',
    'sentado.gif',
    'aplaudindoSentado.gif',
    'aplaudindoEmPe.gif',
    'festejando.gif',
    'idolatrando.gif'
]
bonequinhoAtual = 0
delta = 1

onload = function(){
    this.setInterval(trocaBonequinho,1*1000)
}

function trocaBonequinho(){
    console.log('Aumenta Cotação')
    bonequinhoAtual+=delta;
    if(bonequinhoAtual>=bonequinhos.length){
       bonequinhoAtual = bonequinhoAtual.length-1
       delta = -1 
    }
    else if(bonequinhoAtual<0){
        bonequinhoAtual = 1
        delta = 1
    }

    document.getElementById('idBonequinho').src = 'images/' + bonequinho[bonequinhoAtual];
}