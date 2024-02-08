#pragma once
class Plant {
private:

public:
	static double health;
	static double cost;
	virtual void update() = 0;
};

class PeeShooter: Plant {
private:

public:
	static double rechargeSeconds;
	static double damage;

	PeeShooter();
	void update() override;
	void shoot();
	void moveBullets();
};