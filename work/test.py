def race(x, y):
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    
    minutes, tort, hare = 1, x, y
    while tort < hare:
        minutes += 1
        tort += x
        if minutes % 10 < 5:
            hare += y
        print(f'Tortoise: {tort}, Hare: {hare}, Minutes: {minutes}')

    return minutes

print(race(5, 7))
