function sqtrFloor1(n:number): number{
    for(let i=1; i<= n/2;i++){
        if(i**2 == n){
            return i;
        }
    }
    throw "without whole roots";
}

function isPrime(n:number):boolean{
    for(let i=2; i< Math.sqrt(n); i++){
        if(n%i == 0)
            return false
    }
    return true
}

function sqtrFloor2(n:number): number{
    for(let i=1; i<= n/2;i++){
        if(i**2 == n){
            return i;
        }
    }
    throw "without whole roots";
}

console.log(sqtrFloor1(100))