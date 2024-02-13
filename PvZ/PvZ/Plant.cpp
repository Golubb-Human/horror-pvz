#include "Plant.h"

void Plant::draw(sf::RenderWindow *window) {
	window->draw(sprite);
}

void Plant::setTexture(sf::Texture texture) {
	sprite.setTexture(texture);
}

void Plant::setIndexPosition(insts::Pos position) { 
	this->position = position;
}
