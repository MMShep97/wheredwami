import { database } from './database.js'

console.log('start of map.js')

//poster 1
var poster1 = database.ref('/poster-1');
poster1.on('value', snap => { 
  if (snap.val() == true) {
    console.log(snap.key + " is true!")
  }
 } );

//poster 2
var poster2 = database.ref('/poster-2');
poster2.on('value', snap => { 
  if (snap.val() == true) {
    console.log(snap.key + " is true!")
  }
 } );

//poster 3
var poster3 = database.ref('/poster-3');
poster3.on('value', snap => { 
  if (snap.val() == true) {
    console.log(snap.key + " is true!")
  }
 } );

//poster 4
var poster4 = database.ref('/poster-4');
poster4.on('value', snap => { 
  if (snap.val() == true) {
    console.log(snap.key + " is true!")
  }
 } );

//poster 5
var poster5 = database.ref('/poster-5');
poster5.on('value', snap => { 
  if (snap.val() == true) {
    console.log(snap.key + " is true!")
  }
 } );

//poster 6
var poster6 = database.ref('/poster-6');
poster6.on('value', snap => { 
  if (snap.val() == true) {
    console.log(snap.key + " is true!")
  }
 } );

//poster 7
var poster7 = database.ref('/poster-7');
poster7.on('value', snap => { 
  if (snap.val() == true) {
    console.log(snap.key + " is true!")
  }
 });

//poster 8
var poster8 = database.ref('/poster-8');
poster8.on('value', snap => { 
  if (snap.val() == true) {
    console.log(snap.key + " is true!")
  }
 } );

//poster 9
var poster9 = database.ref('/poster-9');
poster9.on('value', snap => { 
  if (snap.val() == true) {
    console.log(snap.key + " is true!")
  }
 });