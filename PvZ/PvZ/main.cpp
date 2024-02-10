#include <SFML/Graphics.hpp>
#include "Draw.h"
#include "Grid.h"

int main()
{
    sf::Texture background;
    sf::Sprite s_background;
    Grid grid(insts::Pos(9, 5));
    sf::RenderWindow window(sf::VideoMode(640, 480), "Plants vs Zombies horror edition", sf::Style::Close);
    Draw draw(&window);
    if (!background.loadFromFile("res\\textures\\background.png")) {
        window.close();
    }
    s_background.setTexture(background);
    draw.setBackground(&background);

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

        window.draw(s_background);
        draw.grid(grid);

        window.display();
    }

    return 0;
}
