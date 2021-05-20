# imports the Pygame library
import pygame


def main():
    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption(u'Mouse events')

    # sets the window size
    pygame.display.set_mode((400, 400))

    # infinite loop
    while True:
        # gets a single event from the event queue
        event = pygame.event.wait()
        #print(event)

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break

        # if any mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            # prints on the console the pressed button and its position at that moment
            print (u'button {} pressed in the position {}'.format(event.button, event.pos))

        # if any mouse button is released
        if event.type == pygame.MOUSEBUTTONUP:
            # prints on the console the button released and its position at that moment
            print (u'button {} released in the position {}'.format(event.button, event.pos))

        

    # finalizes Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
