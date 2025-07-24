/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if(n<=1){
        return n;
    }
    let n1=0;
    let n2=1;
    let n3;
    for(i=2;i<=n;i++){
        n3=n1+n2;
        n1=n2;
        n2=n3;
    }
    return n3;
};