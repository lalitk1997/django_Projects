 // PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT
var newName;
var rosterLength;
function addNew() {
  newName = prompt("Enter newName (will be added to array):");
  console.log(newName+" is added to array.");
  rosterLength = roster.length;
  roster[rosterLength] = newName;
  return roster.length;
}

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
var retName;
function removeNameL(){
  retName = roster.pop();
  console.log(retName + " is removed from the array.");
}

// REMOVE STUDENT
// review

// Create a function called remove that takes in a name
var nameComp;
function removeComp(nameComp) {
    for (var i = 0; i < roster.length; i++) {
      if (roster[i] === nameComp) {
        return roster.splice(i, 1);
      }
    }
}
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER
function displayRoster() {
  for (var i = 0; i < roster.length; i++) {
    console.log(roster[i]+" ");
  }
}

// Create a function called display that prints out the orster to the console.
function retRoster() {
  return roster;
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
