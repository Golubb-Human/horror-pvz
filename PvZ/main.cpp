#include <SFML/Graphics.hpp>
#include "Draw.h"
#include "Grid.h"
#include "Plant.h"

int main()
{
    PeeShooter::init();

    PeeShooter plant;

    insts::Pos plantPos(2, 2);

    plant.setIndexPosition(plantPos);

    sf::Texture plantTexture;

    plantTexture.loadFromFile(".\\res\\textures\\peashooter.png");

    plant.setTexture(plantTexture);

    sf::Texture background;
    Grid grid(stgs::numCels);
    grid.plant(&plant, plantPos);
    sf::RenderWindow window(sf::VideoMode(640, 480), "Plants vs Zombies horror edition", sf::Style::Close);
    Draw draw(&window);

    if (!background.loadFromFile(".\\res\\textures\\background.png")) {
        window.close();
    }
    draw.setBackground(&background);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }
        // drawing

        draw.background();
        draw.grid(grid);

        window.display();
    }

    return 0;
}
