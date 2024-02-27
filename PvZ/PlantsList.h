#include <vector>
#include "Plant.h"

#pragma once
class PlantsList {
public:
	std::vector<Plant*> plants;
	void addPlant(Plant *plant);
	void update();
};

