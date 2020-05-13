load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_toolchains",
    sha256 = "04b10647f76983c9fb4cc8d6eb763ec90107882818a9c6bef70bdadb0fdf8df9",
    strip_prefix = "bazel-toolchains-1.2.4",
    urls = [
        "https://github.com/bazelbuild/bazel-toolchains/releases/download/1.2.4/bazel-toolchains-1.2.4.tar.gz",
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-toolchains/archive/1.2.4.tar.gz",
    ],
)

load("@bazel_toolchains//rules:rbe_repo.bzl", "rbe_autoconfig")

rbe_autoconfig(name = "rbe_default")
