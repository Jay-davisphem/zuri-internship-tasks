// A simple Calculator app

// Please the link to this javascript running in an html page is in the README.md of this directory ../README.md
const input = prompt

const nonZeroNumber = () => {
  // Returns when num is not zero
  let num = parseFloat(input("Enter second number: "));
  while (num == 0) {
    alert("\nDenominator cannot be zero!");
    num = parseFloat(input("Please reenter the second number: "));
  }
  return num;
};

const computeAnswer = (entry, num1, num2) => {
  let answer;
  if (entry == "+") answer = num1 + num2;
  else if (entry == "-") answer = num1 - num2;
  else if (entry == "*") answer = num1 * num2;
  else if (entry == "/") answer = num1 / num2;
  return answer;
};

function calculator() {
  const message = `
  Enter:
      + to do addition
      - to do subtraction
      * to do multiplication
      / to do division
  `;

  const operations = ["+", "-", "*", "/"];
  const errorOnZero = "/";
  console.info(message);
  let entry = input("Enter an operation + or - or * or /: ");
  let num1, num2, answer;
  if (operations.includes(entry)) {
    num1 = parseFloat(input("\nEnter first number: "));
    if (!isNaN(num1)) {
      if (entry == errorOnZero) num2 = nonZeroNumber();
      else num2 = parseFloat(input("Enter second number: "));
      answer = computeAnswer(entry, num1, num2);
      alert(`\n${num1} ${entry} ${num2} = ${answer}\n`);
    } else {
      alert("Input not a number type!\n");
    }
  } else {
    alert("Sorry, operation not not available\n");
  }
}

function retry(){
  // Retry calculator
  let yOrN = 'y';
  while(yOrN == 'y'){
    calculator()
    yOrN = input("Do you want to continue(y/n): ")
    while (!(['n', 'y'].includes(yOrN))){
      alert("Invalid response!\n")
      yOrN = input("Do you want to continue(y/n): ")
      if(['n', 'y'].includes(yOrN))
        break;
    }
  }
  alert('\nGoodbye techie!')
}

retry()
