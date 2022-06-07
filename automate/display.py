import matplotlib.pyplot as plt

def show_CA(grid: list[list[int]], animation, transition_duration=0.1):
    last_grid = grid
    step = 0
    fig, ax = plt.subplots()
    ax.pcolormesh(last_grid)

    while True:
        step += 1
        last_grid = animation(last_grid, step)
        ax.pcolormesh(last_grid)
        plt.pause(transition_duration)
        print(step)

    plt.show()
