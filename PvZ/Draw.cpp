#include "Draw.h"

Draw::Draw(sf::RenderWindow* window) {
	this->window = window;
}


void Draw::setBackground(sf::Texture* texture) {
	backgroundSprite.setTexture(*texture);
}


void Draw::grid(Grid grid) {
	std::vector<std::vector<Plant*>> gridVec = grid.getGrid();
	
	sf::RectangleShape squard;

	squard.setFillColor(sf::Color(0));

	squard.setOutlineThickness(2);
	squard.setOutlineColor(sf::Color(10, 10, 10));
	squard.setSize(stgs::gridTileSize.vec2f());

	for (int i = 0; i < gridVec.size(); i++) {
		for (int j = 0; j < gridVec.at(0).size(); j++) {
			insts::Pos position = insts::Pos(i, j) * stgs::gridTileSize + stgs::gridOffset;
			if (gridVec.at(i).at(j) != nullptr) {
				insts::Pos position = gridVec.at(i).at(j)->getDefaultPos();
				this->plant(insts::Pos(i, j), gridVec);
			}
			squard.setPosition(position.vec2f());
			window->draw(squard);
		}
	}
}



void Draw::background() {
	window->draw(backgroundSprite);
}


void Draw::background(sf::Texture* texture) {
	backgroundSprite.setTexture(*texture);
	window->draw(backgroundSprite);
}


void Draw::plant(insts::Pos index, std::vector<std::vector<Plant*>> grid) {
	grid.at((int)index.x).at((int)index.y)->draw(window);
}