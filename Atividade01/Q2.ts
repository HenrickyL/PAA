function remove(v:number[], pos:number){
    for(let i=pos; i< v.length-1; i++){
        v[i] =v[i+1];
    }
    v.pop();
}
function findRecurrence( v: number[], w: number[]):number[]{
    console.log(v,w)
    let res:number[] = []
    for(let i=0; i<v.length;i++){
        for(let j=0; j<w.length;j++){
            if(v[i]==w[j]){
                res.push(v[j])
                remove(w,j);
                break
            }
        }
    }
    return res;
}

console.log(findRecurrence([2,5,5,5],[2,2,3,5,5,7]))