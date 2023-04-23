import pyglet

# Set the duration of the game in seconds
game_duration = 90 * 60 #(to make the game end in 20 minutes: 20*60)

# Create a window
window = pyglet.window.Window()

# Create a label to display the timer
timer_label = pyglet.text.Label("00:00",
                                font_size=36,
                                x=window.width // 2,
                                y=window.height - 50,
                                anchor_x='center',
                                anchor_y='center')

# Define a function to update the timer label
def update_timer(dt):
    global game_duration
    game_duration -= dt
    minutes = int(game_duration // 60)
    seconds = int(game_duration % 60)
    timer_label.text = f"{minutes:02}:{seconds:02}"

# Schedule the update_timer function to run every second
pyglet.clock.schedule_interval(update_timer, 1)

# Start the game
pyglet.app.run()
