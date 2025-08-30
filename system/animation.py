
from ursina import *

class SpriteSheetAnimation(Entity):
    def __init__(self, texture_path, frame_count, fps=8,
                 orientation="horizontal", parent=None, scale=1, **kwargs):
        """
        Універсальний компонент анімації спрайтшитом.
        """
        super().__init__(parent=parent, **kwargs)

        self.frame_count = frame_count
        self.fps = fps
        self.orientation = orientation
        self.current_frame = 0
        self.time_accumulator = 0

        # створюємо власний Mesh замість quad
        self.model = Mesh(
            vertices=[(-.5,-.5,0), (.5,-.5,0), (.5,.5,0), (-.5,.5,0)],
            triangles=[(0,1,2), (2,3,0)],
            uvs=[Vec2(0,0), Vec2(1,0), Vec2(1,1), Vec2(0,1)]
        )
        self.texture = texture_path
        self.scale = scale

        # генеруємо UV для кожного кадру
        self.frames_uvs = []
        for i in range(frame_count):
            if orientation == "horizontal":
                u0 = i / frame_count
                u1 = (i+1) / frame_count
                self.frames_uvs.append([Vec2(u0,0), Vec2(u1,0), Vec2(u1,1), Vec2(u0,1)])
            else:  # vertical
                v0 = i / frame_count
                v1 = (i+1) / frame_count
                self.frames_uvs.append([Vec2(0,v0), Vec2(1,v0), Vec2(1,v1), Vec2(0,v1)])

        self.set_frame(0)

    def set_frame(self, frame_index):
        self.current_frame = frame_index % self.frame_count
        # оновлюємо UV у Mesh
        self.model.uvs = self.frames_uvs[self.current_frame]
        self.model.generate()

    def update(self):
        self.time_accumulator += time.dt
        if self.time_accumulator >= 1 / self.fps:
            self.time_accumulator = 0
            self.set_frame(self.current_frame + 1)

