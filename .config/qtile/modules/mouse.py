from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from .keys import mod
from bin.snapping_floating_window import move_snap_window


# Drag floating layouts
mouse = [
    Drag([mod], "Button1", move_snap_window(snap_dist=20),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

