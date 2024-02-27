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

		Pos operator +(const Pos& other) {
			return Pos(this->x + other.x, this->y + other.y);
		}

		Pos operator +(float num) {
			return Pos(this->x + num, this->y + num);
		}

		Pos operator -(Pos& other) {
			return Pos(this->x - other.x, this->y - other.y);
		}

		Pos operator -(const Pos& other) {
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

		bool operator ==(float other[2]) {
			return this->x == other[0] && this->y == other[1];
		}

		bool operator !=(Pos& other) {
			return this->x != other.x || this->y != other.y;
		}

		Pos* operator = (Pos& other) {
			this->x = other.x;
			this->y = other.y;
			return this;
		}

		Pos* operator = (float other[2]) {
			this->x = other[0];
			this->y = other[1];
			return this;
		}

		operator sf::Vector2f() {
			return sf::Vector2f({ x, y });
		}

		sf::Vector2f vec2f() {
			return sf::Vector2f({ x, y });
		}
	};
}

namespace stgs { // settings
	static insts::Pos gridOffset(176, 79);
	static insts::Pos gridTileSize(52, 68);
	static insts::Pos gridNumCels(9, 5);
	static insts::Pos platsListOffset(176, 79);
	static insts::Pos platsListTileSize(52, 68);
	static int plantListlength(10);
}
