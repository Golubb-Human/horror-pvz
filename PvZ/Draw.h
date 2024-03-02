#pragma once
#include <SFML/Graphics.hpp>
#include "Grid.h"
#include <vector>

class Draw {
private:
	sf::RenderWindow* window;
	sf::Sprite backgroundSprite;
public:
	Draw(sf::RenderWindow* window);
	void setBackground(sf::Texture* texture);
	void grid(Grid grid);
	void background();
	void background(sf::Texture* texture);
	void plant(insts::Pos index, std::vector<std::vector<Plant*>> grid);
<<<<<<< HEAD
	void plantsList();
=======
>>>>>>> c8041aba73a9a6484ece3a3c5eca70e52a532714
};

