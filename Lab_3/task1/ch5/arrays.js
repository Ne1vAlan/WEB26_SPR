let fruits = ["Apple", "Orange", "Plum"];

alert( fruits[0] ); // Apple
alert( fruits[1] ); // Orange
alert( fruits[2] ); // Plum
// mix of values
let arr = [ 'Apple', { name: 'John' }, true, function() { alert('hello'); } ];

// get the object at index 1 and then show its name
alert( arr[1].name ); // John

// get the function at index 3 and run it
arr[3](); // hello

alert( fruits.shift() ); // remove Apple and alert it

alert( fruits ); // Orange, Pear
for (let fruit of fruits) {
  alert( fruit );
}
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

alert( matrix[0][1] );

let shoppingCart = fruits;

shoppingCart.push("Banana");

alert( fruits.length ); // 4