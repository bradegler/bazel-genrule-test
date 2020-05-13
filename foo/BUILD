load("@rules_cc//cc:defs.bzl", "cc_binary")

genrule(
    name = "gen-foo",
    srcs = [],
    outs = ["foo.h"],
    cmd = "./$(location create_foo.sh) > \"$@\"",
    tools = ["create_foo.sh"],
)

cc_library(
    name = "lib",
    hdrs = ["foo.h"],
    visibility = ["//visibility:public"]
)
