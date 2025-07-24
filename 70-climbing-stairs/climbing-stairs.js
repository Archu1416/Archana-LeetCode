/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if(n<=2){
        return n;
    }
    let n1=1;
    let n2=1;
    let n3;
    for(let i=2;i<=n;i++){
        n3=n1+n2;
        n1=n2;
        n2=n3;
    }
    return n3;
};