LICENSE = "CLOSED"

SRC_URI = "https://foo.bar/baz.tar.gz"
SRC_URI[sha256sum] = "1234567890"


python() {
    from bb.parse.parse_py import BBHandler
    
    # someone was clever and renamed the implementation
    # so release specifically a different files needs to be
    # inherited :-(
    try:
        BBHandler.inherit("kernel-fit-image", "sca-on-recipe", 1, d)
    except bb.parse.ParseError:
        BBHandler.inherit("kernel-fitimage", "sca-on-recipe", 1, d)
}
