/** Luhn's Algorithm, vertify a credit card, valid or not, then classify it.
 * Really a hard work!
 */
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int calculate(string s);
int check(int sum, string s);

int length = 0;

int main(void)
{
    int correct = 0;
    string number;
    do
    {
        correct = 0;
        number = get_string("Number:");
        length = strlen(number);
        for (int i = 0; i < length; i++)
        {
            if (number[i] < 48 || number[i] > 57)
            {
                correct = 1;
                break;
            }
        }
    }
    while (correct);

    int sum = calculate(number);
    int result = check(sum, number);
    // printf the result
    switch (result)
    {
        case 1:
        case 2:
            printf("INVALID\n");
            break;
        case 3:
            printf("AMEX\n");
            break;
        case 4:
            printf("VISA\n");
            break;
        case 5:
            printf("MASTERCARD\n");
            break;
    }
}

// Calculate Checksum
int calculate(string s)
{
    int sum = 0;
    for (int i = 2; i < length + 1; i = i + 2)
    {
        if (s[length - i] > 52)
        {
            sum = sum + 1 + (s[length - i] - 48) * 2 - 10;
        }
        else
        {
            sum = sum + (s[length - i] - 48) * 2;
        }
    }

    for (int j = 1; j < length + 1; j = j + 2)
    {
        sum = sum + s[length - j] - 48;
    }
    return sum;
}

// Check for Card Length and Starting Digits
int check(int sum, string s)
{
    int start = s[0] - 48;
    int next = s[1] - 48;

    if (sum % 10)
    {
        return 1;
    }
    else if (start == 3 && (next == 4 || next == 7) && length == 15)
    {
        return 3;
    }
    else if (start == 4 && (length == 13 || length == 16))
    {
        return 4;
    }
    else if (start == 5 && next > 0 && next < 6 && length == 16)
    {
        return 5;
    }
    else
    {
        return 2;
    }
}
