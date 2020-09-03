@namespace
class SpriteKind:
    rock = SpriteKind.create()
    spacecraft = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    mySprite.destroy()
    game.reset()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

mySprite2: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.set_background_color(10)
mySprite.set_position(10, 60)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.start_countdown(60)

def on_update_interval():
    global mySprite2
    mySprite2 = sprites.create(img("""
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
        """),
        SpriteKind.enemy)
    mySprite2.set_position(160, randint(0, scene.screen_height()))
    mySprite2.set_velocity(-50, 0)
game.on_update_interval(500, on_update_interval)
