A package to produce a carrot-inspired color palette for python/matplotlib.

![carrot_palette](https://user-images.githubusercontent.com/30849698/134641770-4384a5bb-46f3-41e0-b38b-02f166552fd6.jpg)

Install:
pip install carrotColors

Update:
pip install --upgrade  carrotColors

Usage:

import carrotColors as c
my_cmap = c.CarrotColors.get_carrots()

An example: 

![Carrot_Example1](https://user-images.githubusercontent.com/30849698/134832133-52889e9d-3f01-480a-b092-91a49a6bce64.png)

Also now with Mulberries:

![mulberrys](https://user-images.githubusercontent.com/30849698/134832110-74732282-9f6f-44ff-b0b4-7625f8539218.png)

my_cmap = c.CarrotColors.get_mulberries()


And for those of you who like your color palettes perceptually uniform, here is the perceptually uniform version courtest of empet:

my_cmap = c.CarrotColors.get_uniform_carrots()

