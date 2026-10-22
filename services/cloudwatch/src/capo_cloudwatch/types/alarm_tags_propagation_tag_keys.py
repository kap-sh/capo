"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmTagsPropagationTagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_tags_propagation_tag_key

AlarmTagsPropagationTagKeys: TypeAlias = list[
    "capo_cloudwatch.types.alarm_tags_propagation_tag_key.AlarmTagsPropagationTagKey"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmTagsPropagationTagKeys, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> AlarmTagsPropagationTagKeys:
    out: AlarmTagsPropagationTagKeys = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: AlarmTagsPropagationTagKeys, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> AlarmTagsPropagationTagKeys:
    out: AlarmTagsPropagationTagKeys = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmTagsPropagationTagKeys) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AlarmTagsPropagationTagKeys:
    return [item for item in data if item is not None]
