# -*- coding: utf-8 -*-

from django.test import TestCase
from django.db import models
from core.models import Menu, Category, Product


class MenuModelTest(TestCase):
    def test_should_be_a_field_name(self):
        """Should be a field name"""
        field = Menu._meta.get_field('name')
        self.assertIsInstance(field, models.CharField)


class CategoryModelTest(TestCase):
    def test_should_be_a_field_menu(self):
        """Should be a field menu"""
        field = Category._meta.get_field('menu')
        self.assertIsInstance(field, models.ForeignKey)

    def test_should_be_a_field_name(self):
        """Should be a field name"""
        field = Category._meta.get_field('name')
        self.assertIsInstance(field, models.CharField)


class ProductModelTest(TestCase):
    def test_should_be_a_field_category(self):
        """Should be a field category"""
        field = Product._meta.get_field('category')
        self.assertIsInstance(field, models.ForeignKey)

    def test_should_be_a_field_name(self):
        """Should be a field name"""
        field = Product._meta.get_field('name')
        self.assertIsInstance(field, models.CharField)

    def test_should_be_a_field_ingredients(self):
        """Should be a field ingredients"""
        field = Product._meta.get_field('ingredients')
        self.assertIsInstance(field, models.CharField)

    def test_should_be_a_field_price(self):
        """Should be a field price"""
        field = Product._meta.get_field('price')
        self.assertIsInstance(field, models.DecimalField)
