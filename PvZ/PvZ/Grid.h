#pragma once
#include <vector>
#include "Plant.h"
#include "settings.h"
class Grid
{
private:
	std::vector<std::vector<Plant*>> grid;
public:
	Grid(insts::Pos indexSize);
	void plant(Plant* plant, insts::Pos id);
	void clearCell(insts::Pos id);
	std::vector<std::vector<Plant*>> getGrid();
	void update();
};

