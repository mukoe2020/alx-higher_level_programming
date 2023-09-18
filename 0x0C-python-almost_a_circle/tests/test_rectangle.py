#!/usr/bin/python3
#test_rectangle.py
"""Defining unittests for rectangle.py

Unittest classes:
                 Testrectangle_instantiation - Line 25
                 Testrectangle_width - Line 114
                 Testrectangle_height - Line 187
                 Testrectangle_x - Line 259
                 Testrectangle_y - Line 330
                 Testrectangle_order_of_init - Line 397
                 Testrectangle_area - Line 421
                 Testrectangle_str_display - Line 444
                 Testrectangle_updating_args - Line 528
                 Test_rectangle_updating_kwargs - Line 665
                 Testrectangle_to_dict - Line 777

"""

import csv
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Testrectangle_instantiation(unittest.TestCase):
    """test instantiation of the rectangle class"""

    def test_rect_is_base(self):
        self.assertIsInstance(Rectangle(10, 4), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        rec1 = Rectangle(10, 4)
        rec2 = Rectangle(4, 10)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_three_args(self):
        rec1 = Rectangle(2, 4, 8)
        rec2 = Rectangle(4, 2, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_four_args(self):
        rec1 = Rectangle(2, 4, 8, 4)
        rec2 = Rectangle(4, 2, 2, 1)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(15, 3, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 6, 6, 1, 3)

    def test_width_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 0, 0, 1).__width)

    def test_height_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 0, 0, 1).__height)

    def test_x_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 0, 0, 1).__x)

    def test_y_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 0, 0, 1).__y)

    def width_getter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        self.assertEqual(4, rect.width)

    def width_setter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        rect.width = 12
        self.assertEqual(12, rect.width)

    def height_getter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        self.assertEqual(4, rect.height)

    def height_setter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        rect.height = 12
        self.assertEqual(12, rect.height)

    def x_getter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        self.assertEqual(4, rect.x)

    def x_setter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        rect.x = 12
        self.assertEqual(12, rect.x)

    def y_getter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        self.assertEqual(4, rect.y)

    def y_setter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        rect.y = 12
        self.assertEqual(12, rect.y)


class Testrectangle_width(unittest.TestCase):
    """test instantiation of the rectangle's width attribute"""

    def test_None_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 3)

    def test_str_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("habibi", 3)

    def test_float_as_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(7.7, 2)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(4), 3)

    def test_dict_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"h":7, "b":6}, 3)

    def test_set_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({4,5, 6}, 3)

    def test_list_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 3, 4], 3)

    def test_range_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(6), 3)

    def test_tuple_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((2, 6, 3), 2)

    def test_frozen_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 3, 4, 1}), 3)

    def test_bytes_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 3)

    def test_bytearrays_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'habibi'), 3)

    def test_memoryview_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'habibi'), 3)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 3)

    def test_nan_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)

    def test_zero_as_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)


class Testrectangle_height(unittest.TestCase):
    """test the height attribute of the class Rectangle"""

    def test_None_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, None)

    def test_str_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "habibi")

    def test_float_as_width(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(2, 7.7)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, complex(4))

    def test_dict_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {"h":7, "b":6})

    def test_set_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {4,5, 6})

    def test_list_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, [2, 3, 4])

    def test_range_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, range(6))

    def test_tuple_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (2, 6, 3))

    def test_frozen_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, frozenset({1, 3, 4, 1}))

    def test_bytes_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, b'Python',)

    def test_bytearrays_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, bytearray(b'habibi'))

    def test_memoryview_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, memoryview(b'habibi'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('inf'))

    def test_nan_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('nan'))

    def test_neg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -3)

    def test_zero_as_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)


class Testrectangle_x(unittest.TestCase):
    """test the x attribute for the class rectangle"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

class Testrectangle_y(unittest.TestCase):
    """test y attribute of the class rectangle"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)

class Testrectangle_order_of_init(unittest.TestCase):
    """test order of attribute initalization"""

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 4, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 4, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class Testrectangle_area(unittest.TestCase):
    """test area attribute of the class rectangle"""

    def test_small_area(self):
        rect = Rectangle(10, 2, 1, 1, 1)
        self.assertEqual(20, rect.area())

    def test_large_area(self):
        rect = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, rect.area())

    def test_area_changed_attr(self):
        rect = Rectangle(2, 10, 1, 1, 2)
        rect.width = 7
        rect.height = 3
        self.assertEqual(21, rect.area())

    def test_area_one_arg(self):
        rect = Rectangle(2, 5, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect.area(1)

class Testrectangle_str_display(unittest.TestCase):
    """Unittests for str method and display method"""

    @staticmethod
    def output(rect, method):
        """outputs and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        output = io.StringIO()
        sys.stdout = output
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return output

    #Tests for str method as follows
    def test_str_print_w_and_h(self):
        rect = Rectangle(4, 8)
        output = Testrectangle_str_display.output(rect, "print")
        expected = "[Rectangle] ({}) 0/0 - 4/8\n".format(rect.id)
        self.assertEqual(expected, output.getvalue())

    def test_str_method_width_height_x(self):
        rect = Rectangle(5, 5, 1)
        expected = "[Rectangle] ({}) 1/0 - 5/5".format(rect.id)
        self.assertEqual(expected, rect.__str__())

    def test_str_method_width_height_x_y(self):
        rect = Rectangle(1, 8, 2, 4)
        expected = "[Rectangle] ({}) 2/4 - 1/8".format(rect.id)
        self.assertEqual(expected, str(rect))

    def test_str_method_width_height_x_y_id(self):
        rect = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rect))

    def test_str_method_changed_attributes(self):
        rect = Rectangle(7, 7, 0, 0, [4])
        rect.width = 15
        rect.height = 1
        rect.x = 8
        rect.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rect))

    def test_str_method_one_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.__str__(1)

    # Test display method
    def test_display_width_height(self):
        rect = Rectangle(2, 3, 0, 0, 0)
        output= Testrectangle_str_display.output(rect, "display")
        self.assertEqual("##\n##\n##\n", output.getvalue())

    def test_display_width_height_x(self):
        rect = Rectangle(3, 2, 1, 0, 1)
        output= Testrectangle_str_display.output(rect, "display")
        self.assertEqual("###\n###\n", output.getvalue())

    def test_display_width_height_y(self):
        rect= Rectangle(4, 5, 0, 1, 0)
        output= Testrectangle_str_display.output(rect, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, output.getvalue())

    def test_display_width_height_x_y(self):
        rect = Rectangle(2, 4, 3, 2, 0)
        output= Testrectangle_str_display.output(rect, "display")
        display = "\n\n##\n##\n##\n##\n"
        self.assertEqual(display, output.getvalue())

    def test_display_one_arg(self):
        rect = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rect.display(1)

class Testrectangle_updating_args(unittest.TestCase):
    """Unittests for args attribute of class rectangle"""

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class Testrectangle_updating_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class Testrectangle_to_dict(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
