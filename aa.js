function Vector(x, y) {
    this.x = x || 0;
    this.y = y || 0;
}
Vector.prototype = {
// 입력값이 하나이면 {x.x x.y} 두 개이면 {x, y}
    add: function (x, y) {
        if (arguments.length === 1) {
// 값이 하나이면 아래 로직 실행
            this.x += x.x;
            this.y += x.y;
        } else if (arguments.length === 2) {
// 값이 두 개이면 아래 로직 실행
            this.x += x;
            this.y += y;
        }
// 메서드 체이닝을 위한 반환값 this
       return this;
},
    sub: function (x, y) {
        if (arguments.length === 1) {
            this.x -= x.x;
            this.y -= x.y;
        } else if (arguments.length === 2) {
            this.x -= x;
            this.y -= y;
        }
        return this;
    }}

    Vector.sub = function (v1, v2) {
            // 아규먼트를 받고 v1에서 v2를 빼 다시 벡터를 만든다.
            // 하지만 위에 프로토타입에 sub를 정의해서 아규먼트 개수가 한 개인지 두 개인지 확인하고 적용한다.
        return new Vector(v1.x - v2.x, v1.y - v2.y);
    };
    Vector.add = function (v1, v2) {
            // 위에 프로토타입에 add를 정의해서 아규먼트 개수가 한 개인지 두 개인지 확인하고 적용한다.
        return new Vector(v1.x + v2.x, v1.y + v2.y);
    };

const v1 = new Vector(3, 4);
const v2 = new Vector(2, 3);

const resultAdd = Vector.add(v1, v2);
const resultSub = Vector.sub(v1, v2);

console.log('덧셈 결과: (' + resultAdd.x + ', ' + resultAdd.y + ')');// 5,7
console.log('뺄셈 결과: (' + resultSub.x + ', ' + resultSub.y + ')');// 1,1

const v3 = {x:2,y:2};
const resultOneArgAdd =v1.add(v3);
console.log('스칼라 덧셈 결과: (' + resultOneArgAdd.x + ', ' + resultOneArgAdd.y + ')');// 5,6
const resultOneArgSub = v1.sub(v3);
console.log('스칼라 뺄셈 결과: (' + resultOneArgSub.x + ', ' + resultOneArgSub.y + ')');// 1,2

const v4 = new Vector(2, 3);
// 메서드 체이닝
v4.add(1, 2).sub(2, 1);
console.log(v4)// 1,4
