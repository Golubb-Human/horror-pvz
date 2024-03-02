#include "Plant.h"

void Plant::draw(sf::RenderWindow *window) {
	window->draw(sprite);
}

void Plant::setTexture(sf::Texture &texture) {
	sprite.setTexture(texture);
<<<<<<< HEAD
}

void Plant::setIndexPosition(insts::Pos position) { 
	this->position = position;
	sprite.setPosition(((position+1.f) 
		* stgs::gridTileSize 
		+ stgs::gridOffset
		- insts::Pos(sprite.getTextureRect().width, sprite.getTextureRect().height)
		- offset));
}

=======
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
>>>>>>> c8041aba73a9a6484ece3a3c5eca70e52a532714
