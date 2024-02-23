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
	static float downOffset;
	static float maxHealth;
	static float cost;
	const insts::Pos size = { 463.f, 325.f };
	void setIndexPosition(insts::Pos position);
	void setTexture(sf::Texture &texture);

	float getHealth() { return health; }
	void addHealth(float health) { this->health = health; }
	insts::Pos getDefaultPos() { return position * stgs::gridTileSize + stgs::gridOffset; };
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