"""Generated from Smithy shape ``com.amazonaws.appstream#UrlPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.url_pattern

UrlPatternList: TypeAlias = list["capo_appstream.types.url_pattern.UrlPattern"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UrlPatternList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UrlPatternList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UrlPatternList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> UrlPatternList:
    return [item for item in data if item is not None]
