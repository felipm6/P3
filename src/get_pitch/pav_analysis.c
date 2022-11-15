#include <math.h>
#include "pav_analysis.h"


float compute_power(const float *x, unsigned int N) {
    float power;
    float tmp = 0;

    for(unsigned int i=0; i<(N-1); i++){
        tmp += x[i]*x[i];
    }

    tmp = tmp / N;
    power = 10*log10(tmp);

    return power;
}

float compute_am(const float *x, unsigned int N) {
    float media;
    float tmp;
    
    for(unsigned int i=0; i<(N-1); i++){
        tmp += fabs(x[i]);
    }
    
    media = tmp/N;

    return media;
}

float compute_zcr(const float *x, unsigned int N, float fm) {
    float zrc;
    float tmp;

    for(unsigned int i=1; i<N; i++){
        
        if((x[i]<0 && x[i-1]>0) || (x[i]>0 && x[i-1]<0)){ //si el valor anterior es negativo y 
            tmp++;                                        //el siguiente es positivo o viceversa augmentamos el zcr
        }
    }

    zrc = tmp*(fm/(2*(N-1)));
        
    return zrc;
}
