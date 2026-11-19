"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteAlarmsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_names


class DeleteAlarmsInput(TypedDict, closed=True):
    alarm_names: NotRequired["capo_cloudwatch.types.alarm_names.AlarmNames"]
    """<p>The alarms to be deleted. Do not enclose the alarm names in quote marks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAlarmsInput) -> dict:
    out: dict = {}
    if "alarm_names" in value:
        import capo_cloudwatch.types.alarm_names

        out["AlarmNames"] = capo_cloudwatch.types.alarm_names.serialize_aws_json_1_0(
            value["alarm_names"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAlarmsInput:
    out: DeleteAlarmsInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmNames") is not None:
        import capo_cloudwatch.types.alarm_names

        out["alarm_names"] = capo_cloudwatch.types.alarm_names.deserialize_aws_json_1_0(
            data["AlarmNames"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAlarmsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_names" in value:
        import capo_cloudwatch.types.alarm_names

        capo_cloudwatch.types.alarm_names.serialize_query(
            value["alarm_names"], pairs, f"{key_prefix}AlarmNames"
        )


def deserialize_query(el: Element) -> DeleteAlarmsInput:
    out: DeleteAlarmsInput = {}  # type: ignore[typeddict-item]
    child_alarm_names = el.find("AlarmNames")
    if child_alarm_names is not None:
        import capo_cloudwatch.types.alarm_names

        out["alarm_names"] = capo_cloudwatch.types.alarm_names.deserialize_query(
            child_alarm_names
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAlarmsInput) -> dict:
    out: dict = {}
    if "alarm_names" in value:
        import capo_cloudwatch.types.alarm_names

        out["AlarmNames"] = capo_cloudwatch.types.alarm_names.serialize_cbor(
            value["alarm_names"]
        )
    return out


def deserialize_cbor(data: dict) -> DeleteAlarmsInput:
    out: DeleteAlarmsInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmNames") is not None:
        import capo_cloudwatch.types.alarm_names

        out["alarm_names"] = capo_cloudwatch.types.alarm_names.deserialize_cbor(
            data["AlarmNames"]
        )
    return out
