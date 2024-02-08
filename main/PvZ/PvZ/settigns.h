#pragma once

namespace insts {
	class Pos {
	public:
		double x, y;
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
		double vec() {
			return x, y;
		}
	};
}