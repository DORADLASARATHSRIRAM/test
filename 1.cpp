#include<iostream>
#include<math.h>
using namespace std;
void convertTernary(int n)
{
	if(n==0)
		return;
	int x=n%3;
	n/=3;
	if(x<0)
		n+=1;
	convertTernary(n);
	if(x<0)
		cout<<x+(3*-1);
	else
		cout<<x;
}
void convert(int decimal)
{
	if(decimal!=0)
		convertTernary(decimal);
	else
	cout<<"0"<<endl;
}
int main()
{
	int decimal;
	cin>>decimal;
	convert(decimal);
	return 0;
}