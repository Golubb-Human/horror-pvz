#include "Plant.h"

void Plant::draw(sf::RenderWindow *window) {
	window->draw(sprite);
}

void Plant::setTexture(sf::Texture &texture) {
	sprite.setTexture(texture);
	sprite.setTextureRect(sf::IntRect({
		(int)position.x + (stgs::gridTileSize.x - size.x) / 2,
		(int)position.y + (stgs::gridTileSize.y - size.y) / 2,
		(int)size.x,
		(int)size.y }));
}

void Plant::setIndexPosition(insts::Pos position) { 
	this->position = position;	

	sprite.setTextureRect(sf::IntRect({
		(float)position.x + (stgs::gridTileSize.x - size.x) / 2,
		(float)position.y + (stgs::gridTileSize.y - size.y) / 2,
		(float)size.x,
		(float)size.y }));
}
