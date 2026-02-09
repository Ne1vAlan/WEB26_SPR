let str = `Hello`;

// the first character
alert( str[0] ); // H
alert( str.at(0) ); // H
alert( "I'm the Walrus!" ); // I'm the Walrus!
// the last character
alert( str[str.length - 1] ); // o
alert( str.at(-1) );
alert( `My\n`.length ); // 3
alert( str.indexOf('Widget') ); // 0, because 'Widget' is found at the beginning
alert( str.indexOf('widget') ); // -1, not found, the search is case-sensitive
alert( str.indexOf("id") ); 
for (let i = 65; i <= 220; i++) {
  str += String.fromCodePoint(i);
}
alert( str );
function ucFirst(str) {
  if (!str) return str;

  return str[0].toUpperCase() + str.slice(1);
}

alert( ucFirst("john") ); // 