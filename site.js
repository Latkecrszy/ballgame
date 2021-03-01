function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

class Ball {
    constructor(mass, height, length, start) {
        this.posy = 0
        this.posx = start
        this.vely = 0
        this.velx = 0
        this.mass = mass
        this.height = height
        this.length = length
        this.elasticity = 1.1
        this.jumped_for = 0
    }
}

function gravity(obj) {obj.vely += obj.mass/200}
let ball = new Ball(100, 30, 30, 30)
console.log(ball)
let air_resistance = 1.02
let rect_points = {2: [], 1: [[200, 550], [400, 400], [600, 250], [800, 100], [1000, 250], [1200, 400], [300, 250]]}
let tri_points = {1: [(700, 690)], 2: [(400, 690), (500, 690), (600, 690), (700, 690), (800, 690), (900, 690), (1000, 690), (1100, 690), (1200, 690), (800, 400)]}
let win_points = {1: (1340, 680), 2: (1340, 680)}
let level = 1
let keys_down = []
document.addEventListener('keydown', function (event) {
    if (event.keyCode == 37) {
        keys_down.push("left")
    }
    if (event.keyCode == 39) {
        keys_down.push("right")
    }
    if (event.keyCode == 32) {
        keys_down.push("space")
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
    console.log("up")
})

async function start() {
    let canvas = document.getElementById("canvas");
    let context = canvas.getContext('2d');

    console.log(canvas)
    while (true) {
        context.clearRect(0, 0, canvas.width, canvas.height)
        context.beginPath();
        if (keys_down.includes("left")) {
            ball.velx -= 3
        }
        if (keys_down.includes("right")) {
            ball.velx += 3
        }
        if (ball.posy > 600-ball.height) {
            ball.posy = 600-ball.height
            ball.vely -= ball.vely*1.5-0.001
            ball.jumped_for = 0
        }
        else if (ball.posy < ball.height) {
            ball.posy = ball.height+50
            ball.vely *= -0.1
        }
        if (keys_down.includes("space")) {
            if (ball.jumped_for < 1) {
                ball.vely -= 6
                ball.jumped_for += 1
            }
        }
        if (ball.posx > 1500-ball.length) {
            ball.velx *= -1
            ball.velx -= 1
            ball.posx = 1500-ball.length
            ball.jumped_for = 0
        }
        else if (ball.posx < ball.length) {
            ball.velx *= -1
            ball.velx -= 1
            ball.posx = ball.length
            ball.jumped_for = 0
        }
        ball.posx += ball.velx
        ball.velx /= air_resistance+(ball.mass/2000)
        if (ball.posy < 600-ball.height) {
            gravity(ball)
        }
        console.log(rect_points[level])
        for (let rect of rect_points[level]) {
            console.log(rect)
            /*if (rect[1]-20-ball.height < ball.posy < rect[1]+20-ball.height && ball.vely >= 0 && rect[0] < ball.posx < rect[0]+140) {
                ball.posy = rect[1]-ball.height
                ball.vely = 0
                ball.jumped_for = 0
                console.log("true")
            }
            else {
                console.log("false")
            }
            if (rect[1]+10-ball.height < ball.posy < rect[1]+110-ball.height && ball.vely <= 0 && rect[0]-ball.length < ball.posx < rect[0]+151) {
                ball.vely *= -1
            }*/
            context.fillStyle = 'yellow';
            context.fillRect(rect[0], rect[1], 140, 50);
        }

        ball.posy += ball.vely
        context.arc(ball.posx, ball.posy, 30, 0, 2 * Math.PI, false);
        context.fillStyle = 'red';
        context.fill();
        await sleep(10)
        console.log(ball.posx)
        console.log(ball.posy)
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

