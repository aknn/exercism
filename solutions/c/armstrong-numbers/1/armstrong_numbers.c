#include "armstrong_numbers.h"
#include <math.h>
#include <stdio.h>

bool is_armstrong_number(int candidate) {
    if (candidate < 0) {
        return false;
    }

    if (candidate == 0) {
        return true;
    }

    int num_digits = floor(log10(candidate)) + 1;
    int sum = 0;
    int temp = candidate;

    while (temp > 0) {
        int digit = temp % 10;
        sum += pow(digit, num_digits);
        temp /= 10;
    }

    return sum == candidate;
}
