pkgname = "strongswan"
pkgver = "5.9.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",
    "--with-ipsecdir=/usr/lib/strongswan",
    "--with-capabilities=libcap",
    "--with-user=_strongswan",
    "--with-group=_strongswan",
    "--disable-aes",
    "--disable-des",
    "--disable-eap-gtc",
    "--disable-hmac",
    "--disable-ldap",
    "--disable-md5",
    "--disable-mysql",
    "--disable-rc2",
    "--disable-sha1",
    "--disable-sha2",
    "--disable-static",
    "--enable-addrblock",
    "--enable-attr-sql",
    "--enable-blowfish",
    "--enable-bypass-lan",
    "--enable-cmd",
    "--enable-curl",
    "--enable-eap-aka",
    "--enable-eap-aka-3gpp2",
    "--enable-eap-dynamic",
    "--enable-eap-identity",
    "--enable-eap-md5",
    "--enable-eap-mschapv2",
    "--enable-eap-peap",
    "--enable-eap-radius",
    "--enable-eap-sim",
    "--enable-eap-sim-file",
    "--enable-eap-simaka-pseudonym",
    "--enable-eap-simaka-reauth",
    "--enable-eap-tls",
    "--enable-eap-ttls",
    "--enable-gcm",
    "--enable-gmp",
    "--enable-ha",
    "--enable-ikev1",
    "--enable-ipseckey",
    "--enable-md4",
    "--enable-openssl",
    "--enable-pkcs11",
    "--enable-pki",
    "--enable-python-eggs",
    "--enable-shared",
    "--enable-sqlite",
    "--enable-swanctl",
    "--enable-unbound",
    "--enable-unity",
    "--enable-vici",
    "--enable-whitelist",
    "--enable-xauth-eap",
    "--enable-xauth-generic",
    "--enable-xauth-pam",
]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = [
    "gettext-devel",
    "gmp-devel",
    "libcap-devel",
    "libcurl-devel",
    "libldns-devel",
    "linux-headers",
    "linux-pam-devel",
    "openssl-devel",
    "sqlite-devel",
    "unbound-devel",
]
pkgdesc = "Open Source IKEv2 IPsec-based VPN solution"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "GPL-2.0-or-later"
url = "https://www.strongswan.org"
source = f"https://download.strongswan.org/strongswan-{pkgver}.tar.bz2"
sha256 = "728027ddda4cb34c67c4cec97d3ddb8c274edfbabdaeecf7e74693b54fc33678"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "strongswan")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
