#include "Grid.h"

Grid::Grid() {

}

void Grid::plant(Plant* plant, insts::Pos id) {
	grid[id.x][id.y] = plant;
}

void Grid::clearCell(insts::Pos id) {
	grid[id.x][id.y] = nullptr;
}

std::vector<std::vector<Plant*>> Grid::getGrid()
{
	return grid;
}

void Grid::update() {
	for (int i = 0; i < grid.size(); i++) {
		for (int j = 0; j < grid.at(0).size(); j++) {
			grid.at(i).at(j)->update(0);
		}
	}
}
