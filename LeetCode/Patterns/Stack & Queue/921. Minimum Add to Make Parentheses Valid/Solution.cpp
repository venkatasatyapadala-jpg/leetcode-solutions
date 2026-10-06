class Solution {
public:
    int minAddToMakeValid(string& s) {
        int p[2]={0};
        for (char c: s){
            bool isLeft=(c=='(');
            p[0]+=isLeft;
            p[p[0]<=0]+=(1-((p[0]>0)<<1))*(!isLeft);
        }
        return p[0]+p[1];
    }
};