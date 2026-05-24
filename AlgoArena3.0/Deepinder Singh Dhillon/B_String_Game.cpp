#include<bits/stdc++.h>
using namespace std;
# define vecin(n,a) vector<int> a(n); for(int i=0;i<n;i++){cin>>a[i];}
# define vecout(a)  for(auto i: a){cout<<i<<" ";} cout<<endl;
# define int long long int
int32_t main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string t,p;
    cin>>t;
    cin>>p;
    int n=t.size();
    vector<int> a(n);
    for (int i = 0; i < n; i++)
    {
        cin>>a[i];
    }
    int up=t.size()-p.size();
    int lo=0;
    int ans;
    while(up>=lo){
        int mid=lo+(up-lo)/2;
        vector<bool> pick(n,0);
        for (int i = 0; i < mid; i++)
        {
            pick[a[i]-1]=1;
        }
        
        int idx=0;int flag=0;
        for (int i = 0; i < p.size(); i++)
        {
            while(idx<n&&(pick[idx]==1||t[idx]!=p[i])){
                idx++;
            }
            if(idx==n){flag=1;break;}
            idx++;
        }
        if(flag==0){
            lo=mid+1;
            ans=mid;
        }
        else{
            up=mid-1;
        }
        
    }
    cout<<ans<<endl;
    return 0;
}