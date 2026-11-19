"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmHistoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_history_items
    import capo_cloudwatch.types.next_token


class DescribeAlarmHistoryOutput(TypedDict, closed=True):
    alarm_history_items: NotRequired[
        "capo_cloudwatch.types.alarm_history_items.AlarmHistoryItems"
    ]
    """<p>The alarm histories, in JSON format.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmHistoryOutput) -> dict:
    out: dict = {}
    if "alarm_history_items" in value:
        import capo_cloudwatch.types.alarm_history_items

        out["AlarmHistoryItems"] = (
            capo_cloudwatch.types.alarm_history_items.serialize_aws_json_1_0(
                value["alarm_history_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmHistoryOutput:
    out: DescribeAlarmHistoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmHistoryItems") is not None:
        import capo_cloudwatch.types.alarm_history_items

        out["alarm_history_items"] = (
            capo_cloudwatch.types.alarm_history_items.deserialize_aws_json_1_0(
                data["AlarmHistoryItems"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmHistoryOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_history_items" in value:
        import capo_cloudwatch.types.alarm_history_items

        capo_cloudwatch.types.alarm_history_items.serialize_query(
            value["alarm_history_items"], pairs, f"{key_prefix}AlarmHistoryItems"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAlarmHistoryOutput:
    out: DescribeAlarmHistoryOutput = {}  # type: ignore[typeddict-item]
    child_alarm_history_items = el.find("AlarmHistoryItems")
    if child_alarm_history_items is not None:
        import capo_cloudwatch.types.alarm_history_items

        out["alarm_history_items"] = (
            capo_cloudwatch.types.alarm_history_items.deserialize_query(
                child_alarm_history_items
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAlarmHistoryOutput) -> dict:
    out: dict = {}
    if "alarm_history_items" in value:
        import capo_cloudwatch.types.alarm_history_items

        out["AlarmHistoryItems"] = (
            capo_cloudwatch.types.alarm_history_items.serialize_cbor(
                value["alarm_history_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAlarmHistoryOutput:
    out: DescribeAlarmHistoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmHistoryItems") is not None:
        import capo_cloudwatch.types.alarm_history_items

        out["alarm_history_items"] = (
            capo_cloudwatch.types.alarm_history_items.deserialize_cbor(
                data["AlarmHistoryItems"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
