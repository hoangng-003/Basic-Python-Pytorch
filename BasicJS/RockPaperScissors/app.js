let choices = {
  1: 'Gun',
  2: 'Lightning',
  3: 'Devil',
  4: 'Dragon',
  5: 'Water',
  6: 'Air',
  7: 'Paper',
  8: 'Sponge',
  9: 'Wolf',
  10: 'Tree',
  11: 'Human',
  12: 'Snake',
  13: 'Scissors',
  14: 'Fire',
  15: 'Rock',
}

const buttonDisplay = document.getElementById('btn')

let printBtn = '<button class="btn' + 1 + '" id="' + 1 + '">' + choices[1] + '</button>' + '<br>'

for (let i = 2; i <= Object.keys(choices).length; i++) {
  printBtn += '<button class="btn' + i + '" id="' + i + '">' + choices[i] + '</button>' + '<br>';
}

buttonDisplay.innerHTML = printBtn

const computerChoiceDisplay = document.getElementById('computer-choice')
const userChoiceDisplay = document.getElementById('user-choice')
const resultDisplay = document.getElementById('result')
const possibleChoices = document.querySelectorAll('button')

let userChoiceKey
let result
let computerChoiceKey

possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e) => {
  userChoiceKey = e.target.id
  userChoiceDisplay.innerHTML = choices[userChoiceKey]
  generateComputerChoice();
  generateResult()
}))

function generateComputerChoice() {
  computerChoiceKey = Math.floor(Math.random() * Object.keys(choices).length) + 1
  computerChoiceDisplay.innerHTML = choices[computerChoiceKey]
}

function generateResult() {

  const numberOfChoicesEachChoiceCanWin = Math.floor(Object.keys(choices).length / 2)

  function checkMinus(a) {
    if (a <= 0) {
      a += Object.keys(choices).length
    }
    return a;
  }

  if (userChoiceKey == computerChoiceKey) {
    result = "Draw"
  } else if (computerChoiceKey >= checkMinus(userChoiceKey - numberOfChoicesEachChoiceCanWin) && computerChoiceKey <= checkMinus(userChoiceKey - 1)) {
    result = "Win"
  } else {
    result = "Lose"
  }

  resultDisplay.innerHTML = result;

}
