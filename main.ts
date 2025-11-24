scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairLarge, function (sprite, location) {
    game.over(true)
})
music.play(music.stringPlayable("B A E F F E A B ", 120), music.PlaybackMode.LoopingInBackground)
let mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . d d d d . . . . . . 
    . . . . . . f d d f . . . . . . 
    . . . . . . d d d d . . . . . . 
    . . . . . . d 2 3 d . . . . . . 
    . . . . . . . 2 d . . . . . . . 
    . . . . . d d d d d d . . . . . 
    . . . . d d 3 d d 3 2 d . . . . 
    . . . . d . d d d d . 2 . . . . 
    . . . . . . 7 e e 7 . . . . . . 
    . . . . . . e e e e . . . . . . 
    . . . . . . 7 e 7 e . . . . . . 
    . . . . . f f . . f f . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
tiles.setTilemap(tilemap`level_1`)
tiles.placeOnRandomTile(mySprite, sprites.builtin.forestTiles24)
scene.cameraFollowSprite(mySprite)
info.startCountdown(10)
