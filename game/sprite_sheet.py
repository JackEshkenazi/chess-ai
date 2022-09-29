from enum import Enum
import PIL
import pygame

CHESS_PIECES_SPRITES_ENUM = {
   'white_king': 'content/128h/w_king_png_128px.png',
   'white_queen': 'content/128h/w_queen_png_128px.png',
   'white_bishop': 'content/128h/w_bishop_png_128px.png',
   'white_knight': 'content/128h/w_knight_png_128px.png',
   'white_rook': 'content/128h/w_rook_png_128px.png',
   'white_pawn': 'content/128h/w_pawn_png_128px.png',
   'black_king': 'content/128h/b_king_png_128px.png',
   'black_queen': 'content/128h/b_queen_png_128px.png',
   'black_bishop': 'content/128h/b_bishop_png_128px.png',
   'black_knight': 'content/128h/b_knight_png_128px.png',
   'black_rook': 'content/128h/b_rook_png_128px.png',
   'black_pawn': 'content/128h/b_pawn_png_128px.png',
}
    
class SpriteSheet:
    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

    def load_grid_images(self, num_rows, num_cols, x_margin=0, x_padding=0,
            y_margin=0, y_padding=0):
        """Load a grid of images.
        x_margin is space between top of sheet and top of first row.
        x_padding is space between rows.
        Assumes symmetrical padding on left and right.
        Same reasoning for y.
        Calls self.images_at() to get list of images.
        """
        sheet_rect = self.sheet.get_rect()
        sheet_width, sheet_height = sheet_rect.size

        # To calculate the size of each sprite, subtract the two margins, 
        #   and the padding between each row, then divide by num_cols.
        # Same reasoning for y.
        x_sprite_size = ( sheet_width - 2 * x_margin
                - (num_cols - 1) * x_padding ) / num_cols
        y_sprite_size = ( sheet_height - 2 * y_margin
                - (num_rows - 1) * y_padding ) / num_rows

        sprite_rects = []
        for row_num in range(num_rows):
            for col_num in range(num_cols):
                # Position of sprite rect is margin + one sprite size
                #   and one padding size for each row. Same for y.
                x = x_margin + col_num * (x_sprite_size + x_padding)
                y = y_margin + row_num * (y_sprite_size + y_padding)
                sprite_rect = (x, y, x_sprite_size, y_sprite_size)
                sprite_rects.append(sprite_rect)

        grid_images = self.images_at(sprite_rects)
        print(f"Loaded {len(grid_images)} grid images.")

        return grid_images