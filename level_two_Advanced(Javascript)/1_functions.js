console.log("JavaScript is working !!")

//Problem 1 //NOT A WEEKDAY OR WE ARE ON A VACATION
function sleepIn(weekday, vacation){
  if(weekday !== true || vacation === true){
    return true;
  }else {
    return false;
  }
}

//Problem 2 BOTH SMILE OR NONE OF THEM SMILE
function monkeyTrouble(aSmile, bSmile) {
  if(aSmile === true && bSmile === true){
    return true;
  }else if(aSmile === false && bSmile === false){
    return true;
  }else{
    return false;
  }
}

//Problem 3 STRING TIMES
function stringTimes(str, n) {
  var temp = '';
  for (var i = 0; i < n; i++) {
    temp = temp + str;
  }
  return temp;
}

//Problem 4 luckySum
function luckySum(a, b, c) {
  if(a === 13){
    return 0;
  }else if (b === 13) {
    return a;
  }else if (c === 13) {
    return (a+b);
  }else {
    return (a+b+c);
  }
}

//Problem 5 caughtSpeeding
function caughtSpeeding(speed, is_birthday){
  if(is_birthday !== true){
    if(speed <= 60){
      return 0;
    }else if (speed > 60 && speed < 80) {
      return 1;
    }else if (speed >= 81) {
      return 2;
    }
  }
  if(is_birthday === true){
    if(speed <= 65){
      return 0;
    }else if (speed > 65 && speed < 85) {
      return 1;
    }else if (speed >= 86) {
      return 2;
    }
  }
} 

//Problem 6
function makeBricks(small, big, goal) {

}
