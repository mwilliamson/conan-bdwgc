import os
import shutil

from conans import AutoToolsBuildEnvironment, ConanFile, tools
from conans.tools import download, unzip, check_md5, check_sha1, check_sha256


class BdwgcConan(ConanFile):
    name = "bdwgc"
    version = "8.0.4"
    license = "Similar to X11"
    url = "https://github.com/mwilliamson/conan-bdwgc"
    description = "The Boehm-Demers-Weiser conservative C/C++ Garbage Collector (libgc, bdwgc, boehm-gc) "
    topics = ("garbage collection", "gc")
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        archive_name = "gc-{}.tar.gz".format(self.version)
        download("https://github.com/ivmai/bdwgc/releases/download/v{version}/gc-{version}.tar.gz".format(version=self.version), archive_name)
        check_sha256(archive_name, "436a0ddc67b1ac0b0405b61a9675bca9e075c8156f4debd1d06f3a56c7cd289d")
        unzip(archive_name)
        shutil.move("gc-{}".format(self.version), "gc")
        os.unlink(archive_name)

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir="gc", args=["--enable-static"])
        autotools.make()

    def package(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.install()

    def package_info(self):
        self.cpp_info.libs = ["gc"]

