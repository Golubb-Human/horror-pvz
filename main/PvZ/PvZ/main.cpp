#include <SFML/Graphics.hpp>
#include "Draw.h"
#include "Grid.h"

int main()
{
    Draw draw;
    Grid grid(insts::Pos(9, 5));
    sf::RenderWindow window(sf::VideoMode(640, 480), "Plants vs Zombies horror edition", sf::Style::Close);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear(sf::Color(100, 100, 100));
        // drawing

        draw.grid(&window, grid);

        window.display();
    }

    return 0;
}
