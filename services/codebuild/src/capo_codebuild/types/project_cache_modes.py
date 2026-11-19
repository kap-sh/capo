"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectCacheModes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.cache_mode

ProjectCacheModes: TypeAlias = list["capo_codebuild.types.cache_mode.CacheMode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectCacheModes) -> list:
    import capo_codebuild.types.cache_mode

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.cache_mode.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectCacheModes:
    import capo_codebuild.types.cache_mode

    out: ProjectCacheModes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.cache_mode.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectCacheModes) -> list:
    import capo_codebuild.types.cache_mode

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.cache_mode.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProjectCacheModes:
    import capo_codebuild.types.cache_mode

    out: ProjectCacheModes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.cache_mode.deserialize_cbor(item))
    return out
