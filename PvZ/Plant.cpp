#include "Plant.h"

void Plant::draw(sf::RenderWindow *window) {
	window->draw(sprite);
}

void Plant::setTexture(sf::Texture &texture) {
	sprite.setTexture(texture);
}

void Plant::setIndexPosition(insts::Pos position) { 
	this->position = position;
	sprite.setPosition(((position+1.f) 
		* stgs::gridTileSize 
		+ stgs::gridOffset
		- insts::Pos(sprite.getTextureRect().width, sprite.getTextureRect().height)
		- offset));
}

