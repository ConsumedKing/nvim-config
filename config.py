# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
#myTerm = "cool-retro-term"      # My terminal of choice
myBrowser = "firefox" # My browser of choice

keys = [
        Key([], "XF86AudioMute",
             lazy.spawn("pamixer -t"),
             desc='Launches My Terminal'
             ),
        Key([], "XF86AudioRaiseVolume",
             lazy.spawn("pamixer -i 5"),
             desc='Launches My Terminal'
             ),
        Key([], "XF86AudioLowerVolume",
             lazy.spawn("pamixer -d 5"),
             desc='Launches My Terminal'
             ),
        Key([], "XF86MonBrightnessUp",
             lazy.spawn("light -A 1"),
             desc='Launches My Terminal'
             ),
        Key([], "XF86MonBrightnessDown",
             lazy.spawn("light -U 1"),
             desc='Launches My Terminal'
             ),
        Key([mod], "p", lazy.spawn("i3lock-fancy")),
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn("dmenu_run -fn \"Ubuntu Mono\""),
             desc='Run Launcher'
             ),
         Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='Qutebrowser'
             ),
         # Key([mod], "/",
         #     lazy.spawn("dtos-help"),
         #     desc='DTOS Help'
         #     ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "c",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         # Key(["control", "shift"], "e",
         #     lazy.spawn("emacsclient -c -a emacs"),
         #     desc='Doom Emacs'
         #     ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([mod], "r",
             lazy.to_screen(2),
             desc='Keyboard focus to monitor 3'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.screen.next_group(),
             desc='Move focus to next group'
             ),
         Key([mod], "comma",
             lazy.screen.prev_group(),
             desc='Move focus to prev group'
             ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod], "h",
             lazy.layout.left(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "l",
             lazy.layout.right(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "Down",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "Up",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "Down",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "Up",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
       Key(["mod1"], "Shift_L", lazy.widget["keyboardlayout"].next_keyboard())
]

groups = [Group("1", layout='monadtall'),
          Group("2", layout='monadtall'),
          Group("3", layout='monadtall'),
          Group("4", layout='monadtall'),
          Group("5", layout='monadtall'),
          Group("6", layout='monadtall'),
          Group("7", layout='monadtall'),
          Group("8", layout='monadtall'),
          Group("9", layout='monadtall'),
          ]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 3,
                "margin": 2,
                "border_focus": "018ab7",
                "border_normal": "1D2330"
                }




layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
#    layout.Max(**layout_theme),
#    layout.Stack(num_stacks=2),
#    layout.RatioTile(**layout_theme),
#    layout.TreeTab(
#         font = "Ubuntu",
#         fontsize = 16,
#         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
#         section_fontsize = 12,
#         border_width = 2,
#         bg_color = "1c1f24",
#         active_bg = "c678dd",
#         active_fg = "000000",
#         inactive_bg = "a9a1e1",
#         inactive_fg = "1c1f24",
#         padding_left = 0,
#         padding_x = 0,
#         padding_y = 5,
#         section_top = 10,
#         section_bottom = 20,
#         level_shift = 8,
#         vspace = 3,
#         panel_width = 200
#         ),
    layout.Floating(**layout_theme)
]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize = 16,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 16,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = "eff0f7",#colors[2],
                       inactive = "909199",#colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       hide_unused = True,
                       spacing = 2,
                       highlight_method = "block",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Sep(
                       foreground = colors[0],#colors[4],
                       background = colors[0],
                       linewidth = 5,
                  ),
              widget.WindowName(
                       foreground = "eff0f7",#colors[4],
                       background = colors[0],
                  ),
             #`` widget.Spacer(
             #``          length = bar.STRETCH,
             #``          padding = 6,
             #``          foreground = colors[0],
             #``          background = colors[0]
             #``          ),
              widget.Clock(
                       foreground = "fc160a",#colors[6],
                       background = colors[0],
                       format = "%A , %b %d - %I:%M %p ",
                       padding = 65,
                       ),
              widget.Spacer(
                       length = bar.STRETCH,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.CPU(
                       foreground = "eff0f7",#colors[4],
                       background = colors[0],
                       threshold = 90,
                       fmt = 'CPU: {}',
                       padding = 5,
                       format = "{load_percent:.1f}%"
                       ),
                widget.Backlight(
                       foreground = "eff0f7",#colors[9],
                       background = colors[0],
                       backlight_name = 'intel_backlight',
                       fmt = 'BRIGHT:{}',
                       padding = 5,
                       ),
                       widget.Battery(
                       foreground = "eff0f7",#colors[6],
                       background = colors[0],
                       format = 'BAT:{percent:2.0%}',
                       padding = 5,
                       ),

              widget.KeyboardLayout(
                       foreground = "eff0f7",#colors[8],
                       background = colors[0],
                       display_map = {'ara digits' : 'AR', 'us' : 'EN'},
                       configured_keyboards = ["us", "ara digits"],
                       fmt = '{}',
                       padding = 5
                       ),
              widget.Memory(
                       foreground = "eff0f7",#colors[9],
                       background = colors[0],
                       measure_mem='G',
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       format = 'MEM:{MemUsed:.1f} GB',
                       padding = 5,
                       ),
              widget.Volume(
                       foreground = "eff0f7",#colors[7],
                       background = colors[0],
                       fmt = 'Vol:{}',
                       padding = 5,
                       ),
              widget.Systray(
                       foreground = "eff0f7",#colors[7],
                       background = colors[0],
                      ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='goldendict'),
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

#@hook.subscribe.client_new
#def fix_group(window):
#    group = qtile.current_group
#    if window.group != group:
#        window.togroup(group.name)
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
