#pragma once
#include "SFML/Graphics.hpp"

namespace insts { // instruments
	class Pos {
	public:
		float x, y;
		template<typename Tx, typename Ty>
		Pos(Tx x, Ty y) {
			this->x = x;
			this->y = y;
		}
		Pos() {
			x = 0, 
			y = 0;
		}
		Pos operator +(Pos& other) {
			return Pos(this->x + other.x, this->y + other.y);
		}

		Pos operator -(Pos& other) {
			return Pos(this->x - other.x, this->y - other.y);
		}

		Pos operator *(Pos& other) {
			return Pos(this->x * other.x, this->y * other.y);
		}

		Pos operator /(Pos& other) {
			return Pos(this->x / other.x, this->y / other.y);
		}

		bool operator ==(Pos& other) {
			return this->x == other.x && this->y == other.y;
		}

		bool operator !=(Pos& other) {
			return this->x != other.x || this->y != other.y;
		}

		Pos* operator =(Pos& other) {
			this->x = other.x;
			this->y = other.y;
			return this;
		}
		sf::Vector2f vec2f() {
			return sf::Vector2f({ x, y });
		}
	};
}

namespace stgs { // settings
	static insts::Pos gridOffset(150, 80);
	static insts::Pos gridTileSize(50, 50);
}
