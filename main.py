def on_overlap_tile(sprite, location):
    tiles.set_tilemap(tilemap("""
        level_3
        """))
    tiles.place_on_random_tile(mySprite, sprites.swamp.swamp_tile2)
    info.start_countdown(10)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_hole,
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_tilemap(tilemap("""
        level_2
        """))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        transparency16
        """))
    info.start_countdown(10)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_large,
    on_overlap_tile2)

mySprite: Sprite = None
music.play(music.string_playable("B A E F F E A B ", 120),
    music.PlaybackMode.UNTIL_DONE)
mySprite = sprites.create(img("""
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
"""),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
tiles.set_tilemap(tilemap("""level_1"""))
tiles.place_on_random_tile(mySprite, sprites.builtin.forest_tiles24)
scene.camera_follow_sprite(mySprite)
info.start_countdown(10)