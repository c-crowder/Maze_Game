# Complete your game here
import pygame
import time

class Maze():
    # Initialize the Maze class with basic information for the game
    def __init__(self):
        pygame.init()

        # Set the level to the first level, load the images, and load a new game with the current level
        self.levels = 1
        self.load_images()
        self.new_game()

        # Set won to False (win condition)
        # Set game font, and size/scale
        self.won = False
        self.game_font = pygame.font.SysFont("Arial", 36)
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[3].get_height()

        # Initialize the window based on the size and scale
        window_height = self.height * self.scale
        window_width = self.width * self.scale
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))

        # Name the window 'Maze Game'
        pygame.display.set_caption("Maze Game")

        
        # Start the main loop (uses a while loop)
        self.main_loop()

    # Iterates through the names and loads them into images list with .png appended on
    def load_images(self):
        self.images = []
        for image in ["coin", "door", "monster", "robot"]:
            self.images.append(pygame.image.load(f"{image}.png"))
    
    def new_game(self):
        # Level 1
        if self.levels == 1:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 1, 4, 4, 5, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5, 5, 5],
                        [5, 4, 4, 4, 5, 5, 5, 4, 4, 5, 4, 4, 4, 2, 4, 5, 5],
                        [5, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 5],
                        [5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 4, 4, 0, 5],
                        [5, 4, 4, 4, 5, 5, 5, 5, 4, 4, 5, 4, 4, 4, 4, 5, 5],
                        [5, 4, 3, 4, 4, 4, 4, 4, 1, 4, 4, 4, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        # Level 2
        elif self.levels == 2:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 4, 4, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 2, 4, 5, 5],
                        [5, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 5],
                        [5, 4, 4, 4, 4, 5, 5, 4, 4, 5, 5, 5, 5, 1, 4, 0, 5],
                        [5, 4, 4, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 4, 3, 4, 5, 5, 5, 5, 1, 4, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        # Level 3
        elif self.levels == 3:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 0, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        # Level 4
        elif self.levels == 4:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 1, 4, 5, 4, 3, 4, 4, 4, 4, 2, 4, 1, 4, 0, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        # Level 5
        elif self.levels == 5:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 1, 4, 5],
                        [5, 4, 5, 5, 4, 5, 4, 5, 4, 5, 4, 5, 5, 5, 5, 4, 5],
                        [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 0, 5],
                        [5, 4, 5, 5, 4, 5, 4, 5, 4, 5, 4, 5, 5, 5, 5, 4, 5],
                        [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 1, 4, 5],
                        [5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        # Level 6
        elif self.levels == 6:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5],
                        [5, 4, 5, 4, 5, 5, 5, 5, 5, 4, 4, 5, 4, 4, 5, 5, 5],
                        [5, 4, 3, 4, 5, 5, 5, 5, 4, 4, 5, 5, 5, 4, 4, 5, 5],
                        [5, 5, 4, 4, 5, 5, 5, 4, 4, 5, 5, 5, 5, 5, 4, 2, 5],
                        [5, 5, 5, 4, 4, 5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 0, 5],
                        [5, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        # Level 7
        elif self.levels == 7:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5],
                        [5, 5, 4, 5, 2, 1, 4, 5, 1, 4, 4, 5, 0, 5, 5, 5, 5],
                        [5, 5, 4, 5, 4, 5, 5, 5, 5, 5, 2, 5, 4, 5, 5, 5, 5],
                        [5, 5, 3, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        # Level 8
        elif self.levels == 8:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 5],
                        [5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 2, 5],
                        [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
                        [5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        # Level 9
        elif self.levels == 9:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 4, 5, 5],
                        [5, 4, 4, 5, 5, 4, 4, 4, 5, 5, 4, 4, 4, 5, 4, 5, 5],
                        [5, 4, 5, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 5, 4, 5, 5],
                        [5, 4, 5, 5, 5, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 5, 5],
                        [5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5],
                        [5, 1, 4, 5, 0, 4, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        # Level 10
        elif self.levels == 10:
            self.map = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 0, 5, 5],
                        [5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 4, 5],
                        [5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5],
                        [5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 4, 5],
                        [5, 5, 4, 1, 4, 5, 5, 5, 5, 5, 5, 1, 2, 4, 4, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        else:
            self.won = True

            


    # Check the events given since the last iteration
    # Draw the new window
    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()

    # Check for movement, exiting, or retrying
    # If the game is done, check for restart condition
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # Check for escape(exit), arrow keys(movement), 'r'(retry)
            if event.type == pygame.KEYDOWN:
                # Close Game
                if event.key == pygame.K_ESCAPE:
                    exit()
                # Move robot and move monster if robot move sucessful
                if event.key == pygame.K_LEFT:
                    if self.move(3, -1, 0) == 1:
                        self.move_monster()
                if event.key == pygame.K_RIGHT:
                    if self.move(3, 1, 0) == 1:
                        self.move_monster()
                if event.key == pygame.K_UP:
                    if self.move(3, 0, -1) == 1:
                        self.move_monster()
                if event.key == pygame.K_DOWN:
                    if self.move(3, 0, 1) == 1:
                        self.move_monster()
                # Start the level over
                if event.key == pygame.K_r:
                    self.new_game()
            # Restart condition = y, reinitialize everything to base value if y
            if self.won and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    self.won = False
                    self.levels = 1
                    self.new_game()
                if event.key == pygame.K_n:
                    exit()
    
    # Move monster towards robot
    def move_monster(self):
        robot_x, robot_y = self.find_robot()
        monster_x, monster_y = self.find_monster()
        if robot_x > monster_x:
            self.move(2, 1, 0)
        if robot_x < monster_x:
            self.move(2, -1, 0)
        if robot_y > monster_y:
            self.move(2, 0, 1)
        if robot_y < monster_y:
            self.move(2, 0, -1)

    # Defines how entities move
    def move(self, entity: int, move_x: int, move_y: int):
        
        # Freeze movement if game is won
        if self.won:
            return

        # If the entity is the robot, find where the robot is
        if entity == 3:
            old_robot_x, old_robot_y = self.find_robot()
        # If the entity is the monster, find where the monster is
        if entity == 2:
            old_robot_x, old_robot_y = self.find_monster()
        # Apply the potential move
        new_robot_x = old_robot_x + move_x
        new_robot_y = old_robot_y + move_y

        # If there is a wall, do nothing return 0
        if self.map[new_robot_y][new_robot_x] == 5:
            return 0
        
        # If the entity is a robot and it is moving into a monster, lose the level and try again
        if self.map[new_robot_y][new_robot_x] == 2 and entity == 3:
            self.lost()
            return 0

        # If the entity is a robot and it is moving into a door, 
        # Find the other door, then move to the right side of the other door on the map
        if self.map[new_robot_y][new_robot_x] == 1 and entity == 3:
            door_x, door_y = self.find_door(new_robot_x, new_robot_y)
            self.map[old_robot_y][old_robot_x] = 4
            # If the other side of the other door is clear, move there
            if self.map[door_y][door_x + 1] == 4:
                self.map[door_y][door_x + 1] = entity
            # If there is a monster on the other side of the other door, lose the level
            elif self.map[door_y][door_x + 1] == 2:
                self.lost()

        # If the entity is a robot and movement is onto the coin, win the level
        if self.map[new_robot_y][new_robot_x] == 0 and entity == 3:
            self.win()
            return 0
        
        # If movement is onto a normal square, move there
        if self.map[new_robot_y][new_robot_x] == 4:
            self.map[old_robot_y][old_robot_x] = 4
            self.map[new_robot_y][new_robot_x] = entity

        return 1
    
    # Find where the other door on the map is given the location of one door
    def find_door(self, door1_x: int, door1_y:int):
        for y in range(self.height):
            for x in range(self.width):
                if x == door1_x and y == door1_y:
                    continue
                if self.map[y][x] == 1:
                    return x, y
        raise ValueError("door not found")

    # Prints a win message for 1 second (sleep(1)), then starts a new game on the next levels
    def win(self):
        game_text = self.game_font.render("Level Passed!", True, (255, 255, 255))
        game_textx = (self.width*self.scale)/2 - game_text.get_width()/2
        game_texty = (self.height*self.scale)/2 - game_text.get_height()/2

        # Draw rectangle around text and vizualize text
        pygame.draw.rect(self.window, (0, 0, 255), (game_textx-10, game_texty, game_text.get_width()+20, game_text.get_height()))
        self.window.blit(game_text, (game_textx, game_texty))
        pygame.display.flip()
        time.sleep(1)
        self.levels += 1
        self.new_game()

    # Prints a lost message for 1 second, then restarts the level
    def lost(self):
        game_text = self.game_font.render("You Lost, Try Again", True, (255, 255, 255))
        game_textx = (self.width*self.scale)/2 - game_text.get_width()/2
        game_texty = (self.height*self.scale)/2 - game_text.get_height()/2

        pygame.draw.rect(self.window, (0, 0, 255), (game_textx-10, game_texty, game_text.get_width()+20, game_text.get_height()))
        self.window.blit(game_text, (game_textx, game_texty))
        pygame.display.flip()
        time.sleep(1)
        self.new_game()

    # Searches the map and returns the x, y coordinates of where the robot is
    def find_robot(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 3:
                    return x, y
        raise ValueError("robot not found")

    # Searchs the map, then returns the x, y coordinates of where the monster is
    def find_monster(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 2:
                    return x, y
    
    # Draws everything that has happened
    def draw_window(self):
        # Start with a white screen
        self.window.fill((255,255,255))

        # Draw either a black rectangle, or the correct image based on what is in the corresponding map index
        for y in range(self.height):
            for x in range(self.width):
                image = self.map[y][x]
                if image == 5:
                    pygame.draw.rect(self.window, (0, 0, 0), ((x * self.scale), (y * self.scale), (self.scale), (self.scale)))
                elif image == 4:
                    continue
                else:
                    self.window.blit(self.images[image], ((x*self.scale + self.scale/2) - (self.images[image].get_width()/2), ((y*self.scale + self.scale/2) - ((self.images[image].get_height())/2))))

        # Text for instructions at the bottom of the screen
        game_text = self.game_font.render(f"Level: {self.levels}", True, (0, 0, 0))
        self.window.blit(game_text, (100, self.height * self.scale + (self.scale/2 - game_text.get_height()/2)))

        game_text = self.game_font.render(f"(ESC) to exit (R) to retry", True, (0, 0, 0))
        self.window.blit(game_text, (400, self.height * self.scale + (self.scale/2 - game_text.get_height()/2)))
        
        # Render and display final won text
        if self.won:
            game_text = self.game_font.render("Congratulations! You beat all the levels!", True, (255, 255, 255))
            game_text2 = self.game_font.render("Restart? (y/n)", True, (255, 255, 255))
            game_textx = (self.width*self.scale)/2 - game_text.get_width()/2
            game_texty = (self.height*self.scale)/2 - game_text.get_height()/2
            game_text2x = (self.width*self.scale)/2 - game_text2.get_width()/2
            game_text2y = (self.height*self.scale)/2 - game_text2.get_height()/2 + 50

            pygame.draw.rect(self.window, (0, 0, 255), (game_textx-10, game_texty, game_text.get_width()+20, game_text.get_height()))
            self.window.blit(game_text, (game_textx, game_texty))
            pygame.draw.rect(self.window, (0, 0, 255), (game_text2x-10, game_text2y, game_text2.get_width()+20, game_text2.get_height()))
            self.window.blit(game_text2, (game_text2x, game_text2y))

        # Send all the displays to the screen
        pygame.display.flip()

# Call the Maze game object
if __name__ == "__main__":
    Maze()

