#pragma once
#include "settings.h"
#include <SFML/graphics.hpp>

class Plant {
protected:
	insts::Pos position;
	float health;
	sf::Sprite sprite;
public:
	// static parametres for everyone
	static float maxHealth;
	static float cost;
<<<<<<< HEAD
	const insts::Pos offset = { 4.f, 6.f };
=======
	const insts::Pos size = { 463.f, 325.f };
>>>>>>> c8041aba73a9a6484ece3a3c5eca70e52a532714
	void setIndexPosition(insts::Pos position);
	void setTexture(sf::Texture &texture);

	float getHealth() { return health; }
	void addHealth(float health) { this->health = health; }
	insts::Pos getDefaultPos() {
			return ((position + 1.f)
			* stgs::gridTileSize
			+ stgs::gridOffset
			- insts::Pos(sprite.getTextureRect().width, sprite.getTextureRect().height)
			- offset); 
	};
	insts::Pos getIndexPos() { return position; };

	virtual void update() = 0;
	virtual void draw(sf::RenderWindow* window);
};

class Shooter : public Plant {
protected:

public:
	// static parametres only for shooter
	static float recharge; // seconds
	static float damage;

	void shoot();
	void moveBullets();
	void draw(sf::RenderWindow* window) override;
};

class PeeShooter: public Shooter {
private:

public:
	PeeShooter(insts::Pos position = insts::Pos(0, 0));

	static void init();

	void shoot();
	void moveBullets();

	void update() override;
};