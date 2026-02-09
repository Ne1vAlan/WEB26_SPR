for (let i = 0; i < 3; i++) { // shows 0, then 1, then 2
  alert(i);
}
let i = 3;

while (i) {
  alert( i-- );
}
for (let i = 0; i < 10; i++) {

  if (i % 2) {
    alert( i );
  }

}
let sum = 0;

while (true) {

  let value = +prompt("Enter a number", '');

  if (!value) break; // (*)

  sum += value;

}
alert( 'Sum: ' + sum );