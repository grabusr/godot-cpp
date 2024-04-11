from conans import ConanFile, tools, CMake


class GodotCppConan(ConanFile):
    name = "GodotCpp"
    version = "4.2.1"
    topics = "godot"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    scons_options = {}
    exports_sources = "CMakeLists.txt", "src/*", "misc/*", "include/*", "binding_generator.py", "gdextension/*", "cmake/*"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["DCMAKE_INSTALL_PREFIX"] = "install-dir"
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="gdextension")
        self.copy("*.hpp", dst="include", src="gdextension")
        self.copy("*.h", dst="include", src="include")
        self.copy("*.hpp", dst="include", src="include")
        self.copy("*.h", dst="include", src="gen/include")
        self.copy("*.hpp", dst="include", src="gen/include")

        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

        self.copy("*.cmake", dst="lib/cmake/GodotCpp", src="install-dir/lib/cmake")

    def package_info(self):
        self.cpp_info.includedirs = ["include", "include/core", "include/gen"]
        self.cpp_info.libs = tools.collect_libs(self)
