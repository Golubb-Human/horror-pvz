#include "Draw.h"

void Draw::grid(sf::RenderWindow* window, Grid grid) {
	std::vector<std::vector<Plant*>> gridVec = grid.getGrid();
	
	sf::RectangleShape squard;

	squard.setFillColor(sf::Color(0));

	squard.setOutlineThickness(2);
	squard.setOutlineColor(sf::Color(10, 10, 10));
	squard.setSize(stgs::gridTileSize.vec2f());

	for (int i = 0; i < gridVec.size(); i++) {
		for (int j = 0; j < gridVec.at(0).size(); j++) {
			if (gridVec.at(i).at(j) != nullptr) {
				insts::Pos position = gridVec.at(i).at(j)->getDefaultPos();
				squard.setPosition(position.vec2f());
			} else {
				insts::Pos position = insts::Pos(i, j) * stgs::gridTileSize + stgs::gridOffset;
				squard.setPosition(position.vec2f());
			}
			window->draw(squard);
		}
	}
}

