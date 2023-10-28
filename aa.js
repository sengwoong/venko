
function Taiyaki(){
    this.filling = "red bean";
}


const taiyaki1 = new Taiyaki();
taiyaki1.prototype.heat = function(){
    return this.filling + "heating";
}

console.log(taiyaki1.heat()) // Success (custard eating)
const taiyaki2 = new Taiyaki()
console.log(taiyaki2.heat()) // false