let count = 0
function longestPalindrome(s: string): string {
    if(s==null || s.length==1) return s;
    let start=0;
    let end=0;
    for(let i=0; i< s.length; i++){
        let odd = expandToCenter(s,i,i);
        let even = expandToCenter(s,i,i+1);
        let len = Math.max(odd, even);
        if(len>end-start){
            start = i-Math.floor((len-1)/2)
            end =  i+Math.floor(len/2)
        }
    } 
    console.log(count)
    return s.substring(start,end+1);

};
function expandToCenter(s:string, i:number, j:number):number{
    count += 1 //roda 28 vezes
    while(i>=0 && j<s.length && s[i]==s[j]){
        count += 1 //roda 28 vezes
        i--;
        j++;
    }
    return j-i-1;
}

console.log(longestPalindrome("zABBAzzABAtu_ABcBA_"))