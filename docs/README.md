# About the project
The project is a calculator for the area and perimeter of various geometric shapes. It supports the following shapes:

- Circles
- Squares
- Rectangles
- Triangles

The user can select the shape and type of operation (area or perimeter) to perform calculations.
To do this, the functions presented below were implemented in accordance with their mathematical formulas

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Functions
## Rectangles
- area(a, b): takes the values ​​a and b, which are the lengths of the sides and are of type int. Returns an int calculated using the area formula
    ```
    area(10, 20)
    // 200

    area(1, 2)
    // 2
    ```

- perimeter(a, b): takes the values ​​a and b, which are the lengths of the sides and are of type int. Returns an int calculated using the perimeter formula
    ```
    perimeter(10, 20)
    // 60

    perimeter(1, 2)
    // 6
    ```

## Circle
- area(r): takes the value of radius, which are the type of int. Returns an int calculated using the area formula
    ```
    area(10)
    // 314.159...

    area(300)
    // 282743.338...
    ```

- perimeter(r): takes the value of radius, which are the type of int. Returns an int calculated using the perimeter formula
    ```
    perimeter(10)
    // 62.831...

    perimeter(300)
    // 1884.955...
    ```

## Triangle
- area(a,b,c): takes the values ​​a, b and c, which are the lengths of the sides and are of type int. Returns an int calculated using the area formula
    ```
    area(3, 4, 5)
    // 6

    area(7, 8, 9)
    // 12
    ```

- perimeter(a,b,c): takes the values ​​a, b and c, which are the lengths of the sides and are of type int. Returns an int calculated using the perimeter formula
    ```
    perimeter(3, 4, 5)
    // 12

    perimeter(7, 8, 9)
    // 24
    ```

## Square
- area(a): takes the value of side, which are the type of int. Returns an int calculated using the area formula
    ```
    area(10)
    // 100

    area(300)
    // 90000
    ```

- perimeter(a): takes the value of side, which are the type of int. Returns an int calculated using the perimeter formula
    ```
    perimeter(10)
    // 40

    perimeter(300)
    // 1200
    ```

## Calculate
- calc(fig, func, size): а function that calculates values ​​for certain predefined shapes
    ```
    calc("circle", "area", [5])
    // 78.539...

    calc("recrangle", "perimeter", [5, 10])
    // 30
    ```

# Commit history
```
1. 8ba9aeb - Circle and square added
2. d078c8d - Docs added
3. d080c78 - Triangle added
4. 51c40eb - Doc updated for triangle
5. d76db2a - Added calculate.py
6. b5b0fae - Update docs for calculate.py
```