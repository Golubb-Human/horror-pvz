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
	maxHealth = 125.f;
	cost = 100.f;
	downOffset = 10.f;
	recharge = 1.5f;
	damage = 20.f;
}
