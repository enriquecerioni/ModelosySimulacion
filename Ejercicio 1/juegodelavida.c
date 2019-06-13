/*
--------------------------------------
Alumnos:Ivan Castro; Enrique Cerioni. |
Profesor:Ing. Diego Córdoba.		  |
Cátedra: Modelos y Simulación.        | 
--------------------------------------
JUEGO DE LA VIDA<<<
*/

#include <stdio.h>
#include <ncurses.h>

int main()
{

printf("\t\t\t<// JUEGO DE LA VIDA //> \n\n");
int fila,columna,ix, iy, ixd, ixe, iys, iyi, vius; //las variables ixd(ix derecha), iys(iy superior).etc..
//sirven para comprobar las casillas
//alrededor de la casilla que se examina

do{
    printf("Ingrese un numero de filas mayor o igual a 20: \n");
    scanf("%d", &fila);

    printf("\nIngrese un numero de columnas mayor o igual a 20: \n");
    scanf("%d", &columna);

    if(fila < 20 | columna < 20){
        printf("\nIngrese un numero valido de filas y columnas: \n");
    }
}while(fila < 20 | columna < 20);

char matriz[fila][columna], estado[fila][columna];
int opc;
//inicializar tabla matriz
for(ix=0; ix<fila; ix++)
    {
        for(iy=0; iy<columna; iy++)
        {
            matriz[ix][iy]=' ';
        }
    }

do{
    printf("\nSelecciona el estado inicial:\n1)figura\n2)parpadeador\n3)sapo\n4)panal\n5)nave ligera\n");
    scanf("%d", &opc);
        switch(opc){
           case 1:matriz[10][9]='@';matriz[10][10]='@';matriz[10][11]='@';matriz[9][10]='@';break;
           case 2:matriz[10][5]='@';matriz[10][6]='@';matriz[10][7]='@';break;
           case 3:matriz[13][12]='@';matriz[13][13]='@';matriz[13][14]='@';matriz[14][13]='@';matriz[14][14]='@';matriz[14][15]='@';break;
           case 4:matriz[10][9]='@';matriz[10][10]='@';matriz[10][11]='@';matriz[9][9]='@';break;
           case 5:matriz[18][12]='@';matriz[18][13]='@';matriz[18][14]='@';matriz[18][15]='@';matriz[16][12]='@';matriz[17][12]='@';matriz[17][16]='@';matriz[15][13]='@';matriz[15][16]='@';break;
           default: printf("La opcion es incorrecta: %d",opc);
        }
}while(opc > 5);

    while(1)
    {   
        for(ix=0; ix<fila; ix++)
        {   
            for(iy=0; iy<columna; iy++)
            {
                printf("%c",matriz[ix][iy]);
            }
            printf("\n");
        }
        sleep(0.01);
        system("clear");
        printf("\n");

        for(ix=0; ix<fila; ix++)
        {
            for(iy=0; iy<columna; iy++)
            {
                int vivos=0;

                if(ix>=fila-1)
                    ixd=0;
                else
                    ixd=ix+1;

                if(iy>=columna-1)
                    iyi=0;
                else
                    iyi=iy+1;

                if(ix<=0)
                    ixe=fila-1;
                else
                    ixe=ix-1;

                if(iy<=0)
                    iys=columna-1;
                else
                    iys=iy-1;

                //comprobación para saber si los vecinos están vivos o muertos
                if(matriz[ixd][iy]=='@')    vivos++;
                if(matriz[ixe][iy]=='@')    vivos++;
                if(matriz[ix][iys]=='@')    vivos++;
                if(matriz[ix][iyi]=='@')    vivos++;
                if(matriz[ixd][iys]=='@')   vivos++;
                if(matriz[ixe][iys]=='@')   vivos++;
                if(matriz[ixd][iyi]=='@')   vivos++;
                if(matriz[ixe][iyi]=='@')   vivos++;

                //condicional para determinar si la celda vive o muere
                if(matriz[ix][iy]=='@')
                {
                	// cuando esta vivo
                    if(vivos<=1 || vivos>3)
                    {
                        estado[ix][iy]=' ';
                    }else{
                            estado[ix][iy]='@';
                    }

                }else
                {
                    // cuando esta muerto
                    if(vivos==3)
                    {
                        estado[ix][iy]='@';
                    }else{

                        estado[ix][iy]=' ';
                    }
                }

            }

        }

        for(ix=0; ix<fila; ix++)
        {
            for(iy=0; iy<columna; iy++)
            {
                matriz[ix][iy]=estado[ix][iy];
            }
        }
    }

}