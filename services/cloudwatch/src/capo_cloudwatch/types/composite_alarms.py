"""Generated from Smithy shape ``com.amazonaws.cloudwatch#CompositeAlarms``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.composite_alarm

CompositeAlarms: TypeAlias = list[
    "capo_cloudwatch.types.composite_alarm.CompositeAlarm"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CompositeAlarms, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.composite_alarm

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.composite_alarm.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> CompositeAlarms:
    import capo_cloudwatch.types.composite_alarm

    out: CompositeAlarms = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.composite_alarm.deserialize_query(child))
    return out


def serialize_query_flat(
    value: CompositeAlarms, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.composite_alarm

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.composite_alarm.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CompositeAlarms:
    import capo_cloudwatch.types.composite_alarm

    out: CompositeAlarms = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.composite_alarm.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CompositeAlarms) -> list:
    import capo_cloudwatch.types.composite_alarm

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.composite_alarm.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> CompositeAlarms:
    import capo_cloudwatch.types.composite_alarm

    out: CompositeAlarms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.composite_alarm.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CompositeAlarms) -> list:
    import capo_cloudwatch.types.composite_alarm

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.composite_alarm.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> CompositeAlarms:
    import capo_cloudwatch.types.composite_alarm

    out: CompositeAlarms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.composite_alarm.deserialize_cbor(item))
    return out
