#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;
int main(int argc, char const *argv[])
{
    double a = 1.0, b = sqrt(2.0) / 2.0, t = 0.25, p = 1.0;
    double a1 = 1.0, b1 = 1.0 / sqrt(2.0) / 2.0, t1 = 0.25, p1 = 1.0;

    for (int i = 0; i < 10; i++)
    {
        //ガウス・ルジャンドル法を利用
        a1 = (a + b) / 2.0;
        b1 = sqrt(a * b);                 //ここの精度後々不安すぎる
        t1 = t - p * (a - a1) * (a - a1); //ここで整合性が取れなくなるので計算の順番は変えないこと
        p1 = 2.0 * p;

        a = a1;
        b = b1;
        t = t1;
        p = p1;
        //cout<<fixed;
        //これを入れると未計算の桁が0埋めされる
        cout << setprecision(200) //桁数はiomanipで指定してるよ
             << a << " " << b << " " << t << " " << p << " " << (a + b) * (a + b) / 4.0 / t << endl;
        //答えを求める公式(a + b) * (a + b) / 4.0 / t
    }
    return 0;
}
