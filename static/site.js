function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

class Object {
    constructor(mass, height, length, start) {
        this.posy = 0
        this.posx = start
        this.vely = 0
        this.velx = 0
        this.mass = mass
        this.height = height
        this.length = length
        this.jumped_for = 0
        this.coins = 0
    }
}

function gravity(obj) {obj.vely += obj.mass / 90}


function draw_tri(coors) {return (coors[0], coors[1]), (coors[0] + 70, coors[1]), (coors[0] + 35, coors[1] - 60)}


function reset(obj) {
    obj.posx = 100
    obj.posy = 650
    obj.vely, obj.velx = 0, 0
    obj.jumped_for = 0
    obj.coins -= len(collected_coins[level])
    collected_coins[level] = []
}

let ball = new Object(100, 20, 20, 30)
let air_resistance = 1.05
let RECT_HEIGHT = 50
let RECT_WIDTH = 140
let vert_rect_points = {1: [], 2: [[600, 540], [600, 380], [600, 120]], 3: []}
let horiz_rect_points = {3: [], 2: [],
                     1: [[200, 550], [400, 400], [600, 250], [800, 100], [1000, 250], [1200, 400], [300, 250]]}
let tri_points = {1: [[700, 690]], 2: [],
              3: [[400, 690], [500, 690], [600, 690], [700, 690], [800, 690], [900, 690], [1000, 690], [1100, 690],
                  [1200, 690], [800, 400]]}
let win_points = {1: [1340, 680], 2: [1340, 680], 3: [1340, 680]}
let jump_points = {1: [], 2: [[450, 690]], 3: []}
let coin_points = {1: [[735, 500]], 2: [[625, 320]], 3: [[870, 75], [865, 220]]}
let collected_coins = {1: [], 2: [], 3: []}
let level = 1
let keys_down = []
document.addEventListener('keydown', function (event) {
    if (event.keyCode == 37) {
        if (!keys_down.includes("left")) {keys_down.push("left")}
    }
    if (event.keyCode == 39) {
       if (!keys_down.includes("right")) {keys_down.push("right")}
    }
    if (event.keyCode == 32) {
        if (!keys_down.includes("space")) {keys_down.push("space")}
    }
    event.preventDefault()}, true)
document.addEventListener('keyup', function (event) {
    if (event.keyCode == 37) {
        keys_down.splice(keys_down.indexOf('left'), 1)
    }
    if (event.keyCode == 39) {
        keys_down.splice(keys_down.indexOf('right'), 1)
    }
    if (event.keyCode == 32) {
        keys_down.splice(keys_down.indexOf('space'), 1)
    }
})

async function start() {
    let canvas = document.getElementById("canvas");
    let context = canvas.getContext('2d');
    while (true) {
        context.clearRect(0, 0, canvas.width, canvas.height)
        context.beginPath();
        if (keys_down.includes("left")) {
            ball.velx -= 3
        }
        if (keys_down.includes("right")) {
            ball.velx += 3
        }
        if (ball.posy > 690 - ball.height) {
            ball.posy = 690 - ball.height
            ball.vely -= ball.vely * 1.5 - 0.001
            ball.jumped_for = 0
        }
        else if (ball.posy < ball.height) {
            ball.posy = ball.height + 50
            ball.vely *= -0.35
        }
        if (keys_down.includes("space")) {
            if (ball.jumped_for < 4) {
                ball.vely -= 5.7
                ball.jumped_for += 1
            }
        }
        if (ball.posx > 1500 - ball.length) {
            ball.velx *= -1
            ball.velx -= 1
            ball.posx = 1500 - ball.length
            ball.jumped_for = 0
        }
        else if (ball.posx < ball.length) {
            ball.velx *= -1
            ball.velx -= 1
            ball.posx = ball.length
            ball.jumped_for = 0
        }
        ball.posx += ball.velx
        ball.velx /= air_resistance + (ball.mass / 2000)
        for (let rect of horiz_rect_points[level]) {
            if (rect[1] <= ball.posy <= rect[1] + 20 - ball.height && ball.vely >= 0 && parseInt(rect[0]) <= parseInt(ball.posx) <= parseInt(rect[0]) + RECT_WIDTH) {
                console.log("rect")
                console.log(rect[0])
                console.log(ball.posx)
                ball.posy = rect[1] - ball.height
                ball.vely = 0
                ball.jumped_for = 0
            }
            /*else if (rect[1] + 10 - ball.height <= ball.posy <= rect[1] + 110 - ball.height && ball.vely <= 0 && rect[0] - ball.length <= ball.posx <= rect[0] + 151) {
                ball.vely *= -1
            }
            else if (rect[1] <= ball.posy <= rect[1] + RECT_HEIGHT + ball.height) {
                if (rect[0] - ball.length <= ball.posx <= rect[0] + 10) {
                    ball.posx = rect[0] - ball.length - 10
                    ball.velx *= -0.2
                }
                else if (rect[0] + RECT_WIDTH + 1 <= ball.posx <= rect[0] + RECT_WIDTH + 10) {
                    ball.posx = rect[0] + RECT_WIDTH
                    ball.velx *= -0.2
                }
            }*/
            context.fillStyle = 'yellow';
            context.fillRect(rect[0], rect[1], 140, 50);
            context.fill()
        }

        gravity(ball)
        ball.posy += ball.vely
        context.arc(ball.posx, ball.posy, ball.height, 0, 2 * Math.PI, false);
        context.fillStyle = 'red';
        context.fill();
        await sleep(12)
    }
}

function move(keyCode) {
    keyCode = keyCode.keyCode
    if (keyCode == 37) {
        ball.velx -= 3
    }
    else if (keyCode == 39) {
        ball.velx += 3
    }
    else if (keyCode == 32) {
        if (ball.jumped_for < 4) {
            ball.vely -= 6
            ball.jumped_for += 1
        }
    }
}

