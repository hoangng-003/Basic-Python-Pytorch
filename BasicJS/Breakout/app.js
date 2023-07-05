const grid = document.querySelector('.grid')


// Block Class
class Block {
  constructor(x, y) {
    this.topLeft = [x, y]
  }
}

// Creat Block Objects

const blocks = [
  new Block(0, 10),
  new Block(0, 120),
  new Block(0, 230),
  new Block(0, 340),
  new Block(0, 450),
  new Block(0, 560),
  new Block(0, 670),
  new Block(30, 60),
  new Block(30, 170),
  new Block(30, 280),
  new Block(30, 390),
  new Block(30, 500),
  new Block(30, 610),
  new Block(60, 10),
  new Block(60, 120),
  new Block(60, 230),
  new Block(60, 340),
  new Block(60, 450),
  new Block(60, 560),
  new Block(60, 670),
  new Block(90, 60),
  new Block(90, 170),
  new Block(90, 280),
  new Block(90, 390),
  new Block(90, 500),
  new Block(90, 610),
  new Block(120, 10),
  new Block(120, 120),
  new Block(120, 230),
  new Block(120, 340),
  new Block(120, 450),
  new Block(120, 560),
  new Block(120, 670),

]

// create Block is Child of Grid 
function addBlock() {

  for (let i = 0; i < blocks.length; i++) {

    // create Block is div element and have class 'block'
    const block = document.createElement('div')
    block.classList.add('block')

    // Css style for block

    block.style.left = blocks[i].topLeft[1] + 'px'
    block.style.top = blocks[i].topLeft[0] + 'px'

    // add block in grid child list

    grid.appendChild(block)

  }
}

addBlock()

// create User same Block

const user = document.createElement('div')
user.classList.add('user')

let currentPos = [350, 300]

drawUser()

grid.appendChild(user)

function drawUser() {
  if (currentPos[0] < 0) {
    currentPos[0] = 0;
  }

  if (currentPos[0] > 700) {
    currentPos[0] = 700;
  }

  user.style.left = currentPos[0] + 'px'
  user.style.top = currentPos[1] + 'px'
}

// user move

function moveUser(e) {
  switch (e.key) {
    case 'ArrowLeft':
      currentPos[0] -= 30
      drawUser()
      break;
    case 'ArrowRight':
      currentPos[0] += 30
      drawUser()
      break;
  }
}

document.addEventListener('keydown', moveUser)

// create Pong same Block

const pong = document.createElement('div')
pong.classList.add('pong')

let pongCurrentPos = [390, 200]

drawPong()

grid.appendChild(pong)

function drawPong() {
  pong.style.left = pongCurrentPos[0] + 'px'
  pong.style.top = pongCurrentPos[1] + 'px'
}

// Pong move

function movePong() {
  // pongCurrentPos[0] += 5
  // pongCurrentPos[1] -= 5
  drawPong()
}

// setInterval(movePong, 30)