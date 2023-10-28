function Taiyaki(){
    this.filling = "red bean";
}


const taiyakiObj = new Taiyaki();
taiyakiObj.__proto__.eat = function(){
    return this.filling + " eating";
}
debugger

taiyakiObj.setFilling = function(newFilling){
    this.filling = newFilling;
		return newFilling;
}

debugger

console.log(taiyakiObj.setFilling("custard")) // Success (custard)

console.log(taiyakiObj.eat()) // Success (custard eating)
debugger
const taiyaki1 = new Taiyaki()
console.log(taiyaki1.setFilling("cream")) // Error

debugger