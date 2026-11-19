"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ScheduleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.end_time_offset
    import capo_cloudwatch.types.schedule_expression
    import capo_cloudwatch.types.start_time_offset


class ScheduleConfiguration(TypedDict, closed=True):
    schedule_expression: NotRequired[
        "capo_cloudwatch.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The schedule expression that defines how often the underlying CloudWatch Logs scheduled query runs. Specify a <code>rate()</code> expression, for example <code>rate(5 minutes)</code>.</p>"""
    start_time_offset: NotRequired[
        "capo_cloudwatch.types.start_time_offset.StartTimeOffset"
    ]
    """<p>The offset, in seconds, before the scheduled execution time at which the query time range begins. For example, an offset of 360 (6 minutes) on a query running at 12:05:00 starts the query time range at 11:59:00.</p>"""
    end_time_offset: NotRequired["capo_cloudwatch.types.end_time_offset.EndTimeOffset"]
    """<p>The offset, in seconds, before the scheduled execution time at which the query time range ends. Must be non-negative and less than <code>StartTimeOffset</code>. The default is 0.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "start_time_offset" in value:
        out["StartTimeOffset"] = value["start_time_offset"]
    if "end_time_offset" in value:
        out["EndTimeOffset"] = value["end_time_offset"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("StartTimeOffset") is not None:
        out["start_time_offset"] = data["StartTimeOffset"]
    if data.get("EndTimeOffset") is not None:
        out["end_time_offset"] = data["EndTimeOffset"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduleConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "schedule_expression" in value:
        pairs.append(
            (f"{key_prefix}ScheduleExpression", str(value["schedule_expression"]))
        )
    if "start_time_offset" in value:
        pairs.append((f"{key_prefix}StartTimeOffset", str(value["start_time_offset"])))
    if "end_time_offset" in value:
        pairs.append((f"{key_prefix}EndTimeOffset", str(value["end_time_offset"])))


def deserialize_query(el: Element) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    child_schedule_expression = el.find("ScheduleExpression")
    if child_schedule_expression is not None:
        out["schedule_expression"] = str(child_schedule_expression.text or "")
    child_start_time_offset = el.find("StartTimeOffset")
    if child_start_time_offset is not None:
        out["start_time_offset"] = int(child_start_time_offset.text or "")
    child_end_time_offset = el.find("EndTimeOffset")
    if child_end_time_offset is not None:
        out["end_time_offset"] = int(child_end_time_offset.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "start_time_offset" in value:
        out["StartTimeOffset"] = value["start_time_offset"]
    if "end_time_offset" in value:
        out["EndTimeOffset"] = value["end_time_offset"]
    return out


def deserialize_cbor(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("StartTimeOffset") is not None:
        out["start_time_offset"] = data["StartTimeOffset"]
    if data.get("EndTimeOffset") is not None:
        out["end_time_offset"] = data["EndTimeOffset"]
    return out
