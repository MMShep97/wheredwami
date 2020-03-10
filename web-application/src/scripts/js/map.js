import { database } from './database.js'

console.log('start of map.js')
var posterChanged = database.ref('/');
posterChanged.on('value', function(snapshot) {
  // updateStarCount(postElement, snapshot.val());
  console.log(snapshot.val())
});