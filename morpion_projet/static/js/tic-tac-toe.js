/*********************
* Auteur : Romain SEMLER
* Fichier : tic-tac-toe.js
* Date : 07/09/2014
**********************/
function estValide(button)
{
     return button.innerHTML.length == 0;
}

function setSymbol(btn, symbole)
{
     btn.innerHTML = symbole;
}

function rechercherVainqueur(pions, joueurs, tour)
{

  // parcourir de la  ligne
  codepoint = 0
  tableaugagnant= [0,0,0,0]
  for (i=0;i<Math.sqrt(pions.length);i++){
    pointAligner = 0
    for (j=0;j<Math.sqrt(pions.length);j++){
      if (pions[codepoint] !== undefined) {
      if(pions[codepoint].innerHTML == joueurs[tour]){
        tableaugagnant[pointAligner] = codepoint
        pointAligner+=1
      }else{
            pointAligner=0;
            tableaugagnant= [0,0,0,0]
        }
        if(pointAligner==4){
          break;
        }
      }
      
    codepoint+=1
  } 
  if (pointAligner==4){
    for(g=0;g<4;g++){
      if (pions[tableaugagnant[0]].innerHTML == "O"){
        pions[tableaugagnant[g]].style.backgroundColor = "#5CB85C";
      }else{
        pions[tableaugagnant[g]].style.backgroundColor = "#F76763";
      }
    }
    return true
  }
  }


    // parcourir de les colonne
    codepoint = 0
    tableaugagnant= [0,0,0,0]
    for (i=0;i<Math.sqrt(pions.length);i++){
      for (j=0;j<Math.sqrt(pions.length);j++){
        pointAligner = 0
        codepointItem = codepoint
        for (nb=0;nb<4;nb++){
          if (pions[codepointItem] !== undefined) {
            if (pions[codepointItem].innerHTML == joueurs[tour]){
              tableaugagnant[pointAligner] = codepointItem
              codepointItem=codepointItem+Math.sqrt(pions.length)
              pointAligner+=1
            }else{
                pointAligner=0;
                tableaugagnant= [0,0,0,0]
            }
            if(pointAligner==4){
              break;
            }
          }
        }

        if (pointAligner==4){
          for(g=0;g<4;g++){
            if (pions[tableaugagnant[0]].innerHTML == "O"){
              pions[tableaugagnant[g]].style.backgroundColor = "#5CB85C";
            }else{
              pions[tableaugagnant[g]].style.backgroundColor = "#F76763";
            }
          }
          return true
        }
        codepoint+=1
      }
    }





      // parcourir matrice diaogonal principale
    codepoint = 0
    tableaugagnant= [0,0,0,0]
    for (i=0;i<Math.sqrt(pions.length);i++){
      for (j=0;j<Math.sqrt(pions.length);j++){
        pointAligner = 0
        codepointItem = codepoint
        for (nb=0;nb<4;nb++){
          if (pions[codepointItem] !== undefined) {
          if (pions[codepointItem].innerHTML == joueurs[tour]){
            tableaugagnant[pointAligner] = codepointItem
            codepointItem=codepointItem+Math.sqrt(pions.length)+1
            pointAligner+=1
          }else{
              pointAligner=0;
              tableaugagnant= [0,0,0,0]
          }
          if(pointAligner==4){
            break;
          }
        }
        }

        if (pointAligner==4){
          for(g=0;g<4;g++){
            if (pions[tableaugagnant[0]].innerHTML == "O"){
              pions[tableaugagnant[g]].style.backgroundColor = "#5CB85C";
            }else{
              pions[tableaugagnant[g]].style.backgroundColor = "#F76763";
            }
          }
          return true
        }
        codepoint+=1
      }
    }



      // parcourir matrice diaogonal secondaire
      codepoint =  0
      tableaugagnant= [0,0,0,0]
      for (i=0;i<Math.sqrt(pions.length);i++){
        for (j=0;j<Math.sqrt(pions.length);j++){
          pointAligner = 0
          codepointItem = codepoint
          for (nb=0;nb<4;nb++){
            if (pions[codepointItem] !== undefined) {
            if (pions[codepointItem].innerHTML == joueurs[tour]){
              tableaugagnant[pointAligner] = codepointItem
              codepointItem=codepointItem+Math.sqrt(pions.length)-1
              pointAligner+=1
            }else{
                pointAligner=0;
                tableaugagnant= [0,0,0,0]
            }
          }
          if(pointAligner==4){
            break;
          }
          }
  
          if (pointAligner==4){
            for(g=0;g<4;g++){
              if (pions[tableaugagnant[0]].innerHTML == "O"){
                pions[tableaugagnant[g]].style.backgroundColor = "#5CB85C";
              }else{
                pions[tableaugagnant[g]].style.backgroundColor = "#F76763";
              }
            }
            return true
          }
          codepoint+=1
        }
      }

    return false
}

function matchNul(pions)
{
     for (var i = 0, len = pions.length; i < len; i++)
     {
         if (pions[i].innerHTML.length == 0)
              return false;
     }

     return true;
}

var Afficheur = function(element)
{
     var affichage = element;

     function setText(message)
     {
         affichage.innerHTML = message;
     }

     return {sendMessage : setText};
}
