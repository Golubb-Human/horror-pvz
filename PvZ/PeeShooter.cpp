#include "Plant.h"

PeeShooter::PeeShooter(insts::Pos position) { // !!!INDEX POSITION!!!
	this->position = position;
	health = 125.f;
}

void PeeShooter::update() {
	
}

void PeeShooter::shoot() {

}

void PeeShooter::moveBullets() { 

}

void PeeShooter::init() {
	float maxHealth = 125.f;
	float cost = 100.f;
	float downOffset = 10.f;
	float recharge = 1.5f;
	float damage = 20.f;
}
