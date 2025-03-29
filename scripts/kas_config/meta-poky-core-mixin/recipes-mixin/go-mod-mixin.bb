LICENSE = "CLOSED"

SRC_URI = "https://foo.bar/baz.tar.gz"
SRC_URI[sha256sum] = "1234567890"

GO_IMPORT = "foo/bar"

inherit go-mod
