"""Generated from Smithy shape ``com.amazonaws.cloudwatch#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.tag_key

TagKeyList: TypeAlias = list["capo_cloudwatch.types.tag_key.TagKey"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TagKeyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> TagKeyList:
    out: TagKeyList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: TagKeyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> TagKeyList:
    out: TagKeyList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TagKeyList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagKeyList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TagKeyList:
    return [item for item in data if item is not None]
