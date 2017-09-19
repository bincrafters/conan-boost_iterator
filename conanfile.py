from conans import ConanFile, tools, os

class BoostIteratorConan(ConanFile):
    name = "Boost.Iterator"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-iterator"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["iterator"]
    requires =  "Boost.Assert/1.65.1@bincrafters/stable", \
                      "Boost.Concept_Check/1.65.1@bincrafters/stable", \
                      "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Conversion/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Detail/1.65.1@bincrafters/stable", \
                      "Boost.Function_Types/1.65.1@bincrafters/stable", \
                      "Boost.Fusion/1.65.1@bincrafters/stable", \
                      "Boost.Mpl/1.65.1@bincrafters/stable", \
                      "Boost.Optional/1.65.1@bincrafters/stable", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/stable", \
                      "Boost.Static_Assert/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable",\
                      "Boost.Utility/1.65.1@bincrafters/stable"
    
                      #assert1 concept_check5 config0 conversion5 core2 detail5 function_types5 fusion5 mpl5 optional5 smart_ptr4 static_assert1 type_traits3 utility5
    
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()