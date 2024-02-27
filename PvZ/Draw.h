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
	void plantsList();
};

