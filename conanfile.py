#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostIteratorConan(base.BoostBaseConan):
    name = "boost_iterator"
    url = "https://github.com/bincrafters/conan-boost_iterator"
    lib_short_names = ["iterator"]
    header_only_libs = ["iterator"]
    b2_requires = [
        "boost_assert",
        "boost_concept_check",
        "boost_config",
        "boost_conversion",
        "boost_core",
        "boost_detail",
        "boost_function_types",
        "boost_fusion",
        "boost_mpl",
        "boost_optional",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_type_traits",
        "boost_utility"
    ]
