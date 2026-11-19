"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmTypes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_type

AlarmTypes: TypeAlias = list["capo_cloudwatch.types.alarm_type.AlarmType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.alarm_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.alarm_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AlarmTypes:
    import capo_cloudwatch.types.alarm_type

    out: AlarmTypes = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.alarm_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AlarmTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.alarm_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.alarm_type.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> AlarmTypes:
    import capo_cloudwatch.types.alarm_type

    out: AlarmTypes = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.alarm_type.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmTypes) -> list:
    import capo_cloudwatch.types.alarm_type

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.alarm_type.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AlarmTypes:
    import capo_cloudwatch.types.alarm_type

    out: AlarmTypes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.alarm_type.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmTypes) -> list:
    import capo_cloudwatch.types.alarm_type

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.alarm_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AlarmTypes:
    import capo_cloudwatch.types.alarm_type

    out: AlarmTypes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.alarm_type.deserialize_cbor(item))
    return out
