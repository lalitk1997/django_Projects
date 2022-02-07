var firstName = prompt("Enter your first name:");
var lastName = prompt("Enter your last name:");
var age = prompt("Enter your age :");
var height = prompt("Enter your height in cm :");
var petName = prompt("Enter your pet name :");

// first condition
var spy = false;

if(firstName[0]===lastName[0]){
  spy = true;
}
else {
  spy = false;
}

if(age > 20 && age < 30 && spy){
  spy = true;
}
else {
  spy = false;
}

if (height >= 170 && spy) {
  spy = true;
}
else {
  spy = false;
}

var len = petName.length
if(petName[len-1] == 'y' && spy){
  console.log("Welcome comerade!! we have a new mission.")
}
else{
  console.log("Nothing!")
}
