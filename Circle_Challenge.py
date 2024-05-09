{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7d33ade0-b208-4a60-b74e-444434395a9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Circle Tester!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the radius (upto two decimals): \n",
      " 4.5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Radius: 4.5\n",
      "Diameter: 9.0\n",
      "Circumference: 28.27\n",
      "Area: 63.62\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Would you like to grow your circle? (y/n) \n",
      " y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Standby while you circle magically grows....\n",
      "New Radius: 5.5\n",
      "Diameter: 11.0\n",
      "Circumference: 34.56\n",
      "Area: 95.03\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Would you like to grow your circle? (y/n) \n",
      " y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Standby while you circle magically grows....\n",
      "New Radius: 6.5\n",
      "Diameter: 13.0\n",
      "Circumference: 40.84\n",
      "Area: 132.73\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Would you like to grow your circle? (y/n) \n",
      " y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Standby while you circle magically grows....\n",
      "New Radius: 7.5\n",
      "Diameter: 15.0\n",
      "Circumference: 47.12\n",
      "Area: 176.71\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Would you like to grow your circle? (y/n) \n",
      " n\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Goodbye!\n"
     ]
    }
   ],
   "source": [
    "#Circle_Challenge\n",
    "from math import pi\n",
    "\n",
    "#Creating class\n",
    "class Circle:\n",
    "    def __init__(self,radius):\n",
    "        self.radius = radius\n",
    "        \n",
    "    def calculate_diameter(self): \n",
    "        #Returns the calculated diameter\n",
    "        return 2*self.radius\n",
    "\n",
    "    def calculate_circumference(self):\n",
    "        #Returns the calculated circumference\n",
    "        return round(2*pi*self.radius, 2)\n",
    "\n",
    "    def calculate_area(self):\n",
    "        #Returns the calculated area \n",
    "       return round(pi*self.radius**2, 2)\n",
    "       \n",
    "    def grow(self):\n",
    "        #Doubles the radius property\n",
    "        return self.radius+1\n",
    "        \n",
    "    def get_radius(self):\n",
    "        # Returns the radius value\n",
    "        return self.radius\n",
    "\n",
    "#Welcome message and user input\n",
    "print(\"Welcome to the Circle Tester!\")\n",
    "rad = float(input(\"Enter the radius (upto two decimals): \\n\"))\n",
    "\n",
    "\n",
    "#validating user entry and calling class instance methods\n",
    "if rad <= 0 :\n",
    "    print(\"Please enter a positive number for radius\")\n",
    "    rad =  float(input(\"Enter the radius (upto two decimals): \\n\"))\n",
    "        \n",
    "\n",
    "circle = Circle(rad)\n",
    "print(f\"Radius: {circle.get_radius()}\")\n",
    "print(f\"Diameter: {circle.calculate_diameter()}\")\n",
    "print(f\"Circumference: {circle.calculate_circumference()}\")\n",
    "print(f\"Area: {circle.calculate_area()}\")\n",
    "\n",
    "#Asking for user willingness to grow the circle\n",
    "user_cnt = input(\"\\nWould you like to grow your circle? (y/n) \\n\")\n",
    "\n",
    "while user_cnt != 'n':\n",
    "    print(\"\\nStandby while you circle magically grows....\")\n",
    "    new_rad = circle.grow()\n",
    "    circle = Circle(new_rad)\n",
    "    print(f\"New Radius: {circle.get_radius()}\")\n",
    "    print(f\"Diameter: {circle.calculate_diameter()}\")\n",
    "    print(f\"Circumference: {circle.calculate_circumference()}\")\n",
    "    print(f\"Area: {circle.calculate_area()}\")\n",
    "    \n",
    "    user_cnt = input(\"\\nWould you like to grow your circle? (y/n) \\n\")\n",
    "\n",
    "#exit message\n",
    "print(\"Goodbye!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af0fb51c-65b1-40a9-985a-4610e52a1f40",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "846727b2-53df-4092-ae38-63333c827a78",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
