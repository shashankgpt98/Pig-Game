#include<bits/stdc++.h>
#include <algorithm>
#include <iostream>

using namespace std;
int main()
{	
	set<int>f,t;
	int n,m,x,y;
	cin>>n>>m;
	int from[n],to[n];
	int max=0;
	if(n>m)
		max=n;
	else max=m;
	for(int i=0;i<max;i++)
		{
			cin>>x>>y;
			from[i]=x;
			to[i]=y;
		}

	// for (int i = 0; i < (max); ++i)
	// 	{
	// 		cout<<from[i]<<" "<<to[i];
	// 	}	
		  for (int i = 0; i < max; i++) { 
  
        // insert into set 
        f.insert(from[i]); 
    } 
      for (int i = 0; i < max; i++) { 
  
        // insert into set 
        t.insert(to[i]); 
    } 
    cout<<t.size();
	return 0;
}