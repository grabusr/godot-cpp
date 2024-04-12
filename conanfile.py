from conans import ConanFile, tools, CMake


class GodotCppConan(ConanFile):
    name = "godot_cpp"
    version = "4.2.1"
    topics = "godot"
    settings = "os", "compiler", "build_type", "arch"
    # generators = "cmake_find_package"

    exports_sources = "CMakeLists.txt", "src/*", "misc/*", "include/*", "binding_generator.py", "gdextension/*", "cmake/*"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = "install-dir"
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        cmake = CMake(self)
        self.copy("*", dst=".", src="install-dir")
        self.copy("FindGodotCpp.cmake", dst=".", src="cmake/")

#
    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
#         # self.cpp_info.set_property("cmake_target_name", "godot::godot-cpp")
#         self.output.info("Package information: {}".format(self.cpp_info))
#
#         # self.cpp_info.includedirs = ["include", "include/core", "include/gen"]
#         # self.cpp_info.libs = tools.collect_libs(self)
#         print(self.cpp_info)
#         print(self.cpp_info.names)
#         print(self.cpp_info.libs)
#
#         # self.name = "godot"
#         # self.cpp_info.set_property("cmake_file_name", "godot-cpp")
#         # self.cpp_info.set_property("cmake_target_name", "godot::godot-cpp")
#         #
#         # self.cpp_info.components["godot-cpp"].set_property("cmake_file_name", "godot::godot-cpp")
#         # self.cpp_info.components["godot-cpp"].set_property("cmake_target_name", "godot::godot-cpp")
#         # self.cpp_info.components["godot-cpp"].libs = tools.collect_libs(self)
#
#
