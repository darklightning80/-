namespace SpriteKind {
    export const rock = SpriteKind.create()
    export const spacecraft = SpriteKind.create()
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    mySprite.destroy()
    game.reset()
})
let mySprite2 : Sprite = null
let mySprite : Sprite = null
mySprite = sprites.create(img`
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 2 2 . . . . . . . . . . . . . 
            . 5 2 2 f f f 5 5 5 . . . . . f 
            . 5 5 2 f 5 f 5 5 f 5 5 . . f f 
            2 5 2 2 2 f f 5 f 5 5 f 5 f 5 f 
            5 2 5 2 2 f f 5 f 5 5 f 5 f 5 f 
            . 5 2 2 f 5 f 5 5 f 5 5 . . f f 
            . 5 2 2 f f f 5 5 5 . . . . . f 
            . 2 2 . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
scene.setBackgroundColor(10)
mySprite.setPosition(10, 60)
mySprite.setFlag(SpriteFlag.StayInScreen, true)
info.startCountdown(60)
game.onUpdateInterval(500, function on_update_interval() {
    
    mySprite2 = sprites.create(img`
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . f . f f f . . . . . 
                    . . . . . f . f . f e f . . . . 
                    . . . . f e . f f e f . e . . . 
                    . . . . f e f f f f f f f . . . 
                    . . . . f f f f f e f f . . . . 
                    . . . . . f f e . f e . . . . . 
                    . . . . . . f f f f f . . . . . 
                    . . . . . . . . . f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        `, SpriteKind.Enemy)
    mySprite2.setPosition(160, randint(0, scene.screenHeight()))
    mySprite2.setVelocity(-50, 0)
})
