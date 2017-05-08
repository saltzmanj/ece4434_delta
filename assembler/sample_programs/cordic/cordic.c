#include <stdio.h>
#include <stdint.h>
#include <math.h>

int16_t angle[] = {11520,6801,3593,1824,916,458,229,115,57,29,14,7,4,2,1,0};

#define CORDIC_1K 155
#define MUL 256
#define MUL_SHIFTS 8
#define CORDIC_NTAB 16

#define CORDIC_GAIN 155

int main() {
    int16_t angle_test = 37;
    int16_t angle_test_orig = 37;
    int16_t x = CORDIC_GAIN;
    int16_t y = 0;

    angle_test = angle_test << MUL_SHIFTS;
    for(int i = 0; i < CORDIC_NTAB; i++) {
        if(angle_test > 0) {
            angle_test = angle_test - angle[i];
            int16_t xnew = x - (y >> i);
            int16_t ynew = y + (x >> i);
            x = xnew;
            y = ynew;
        } else {
            angle_test = angle_test + angle[i];
            int16_t xnew = x + (y >> i);
            int16_t ynew = y - (x >> i);
            x = xnew;
            y = ynew;
        }
    }

    double sin_ = (double) y/MUL;
    double cos_ = (double) x/MUL;
    printf("Angle = %u\nSin(angle) = %f\nCos(angle) = %f\n", angle_test_orig, sin_, cos_);
    printf("Angle = %u\nSin(angle) = %u\nCos(angle) = %u\n", angle_test_orig, y, x);

    for(int i = 0; i < 16; i++) {
        printf("0x%x\n", angle[i]);
    }  
}