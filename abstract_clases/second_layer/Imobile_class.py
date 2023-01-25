from game_object import GameObject
from pygame.sprite import Sprite

class ImobileObjects(GameObject):
    """ Class for objects that are solid"""

    def __init__(self, x: int, y: int,  width:int, height:int, image: Sprite) -> None:
        super().__init__(x, y, width, height, image)

    def update(self)->None:
        """update"""