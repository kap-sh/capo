"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmHistoryItems``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_history_item

AlarmHistoryItems: TypeAlias = list[
    "capo_cloudwatch.types.alarm_history_item.AlarmHistoryItem"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmHistoryItems, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.alarm_history_item

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.alarm_history_item.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AlarmHistoryItems:
    import capo_cloudwatch.types.alarm_history_item

    out: AlarmHistoryItems = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.alarm_history_item.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AlarmHistoryItems, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.alarm_history_item

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.alarm_history_item.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AlarmHistoryItems:
    import capo_cloudwatch.types.alarm_history_item

    out: AlarmHistoryItems = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.alarm_history_item.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmHistoryItems) -> list:
    import capo_cloudwatch.types.alarm_history_item

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.alarm_history_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AlarmHistoryItems:
    import capo_cloudwatch.types.alarm_history_item

    out: AlarmHistoryItems = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.alarm_history_item.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmHistoryItems) -> list:
    import capo_cloudwatch.types.alarm_history_item

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.alarm_history_item.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AlarmHistoryItems:
    import capo_cloudwatch.types.alarm_history_item

    out: AlarmHistoryItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.alarm_history_item.deserialize_cbor(item))
    return out
