pkgname = "ugrep"
pkgver = "7.0.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
make_check_target = "test"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "brotli-devel",
    "bzip2-devel",
    "linux-headers",
    "lz4-devel",
    "pcre2-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["bash"]
pkgdesc = "Grep-compatible file searcher"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://ugrep.com"
source = f"https://github.com/Genivia/ugrep/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9fb583a1569d070016ee8cf801b923f55b10556e64770fb369837f141d180449"


def post_install(self):
    self.install_license("LICENSE.txt")
