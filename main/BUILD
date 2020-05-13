load("@rules_cc//cc:defs.bzl", "cc_binary")

genrule(
    name = "foo",
    srcs = [],
    outs = ["foo.h"],
    cmd = "./$(location create_foo.sh) > \"$@\"",
    tools = ["create_foo.sh"],
)

cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
)
