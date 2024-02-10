#pragma once
#include "settings.h"

class Plant {
protected:
	insts::Pos position;
	float health;
	static float downOffset;
public:
	// static parametres for everyone
	const float maxHealth = 125.;
	const float cost = 100.;
	virtual void update() = 0;
	void setDefaultPosition(insts::Pos position) {};
	insts::Pos getDefaultPos() { return position * stgs::gridTileSize + stgs::gridOffset; };
	insts::Pos getIndexPos() { return position; };
};

class PeeShooter: Plant {
private:

public:
	// static parametres only for peeshooter
	const float recharge = 1.5; // seconds
	const float damage = 20.;

	PeeShooter(insts::Pos position);
	void update() override;
	void shoot();
	void moveBullets();
};