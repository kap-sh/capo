"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MuteTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.mute_target_alarm_name_list


class MuteTargets(TypedDict, closed=True):
    alarm_names: NotRequired[
        "capo_cloudwatch.types.mute_target_alarm_name_list.MuteTargetAlarmNameList"
    ]
    """<p>The list of alarm names that this mute rule targets. You can specify up to 100 alarm names.</p> <p>Each alarm name must be between 1 and 255 characters in length. The alarm names must match existing alarms in your Amazon Web Services account and region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MuteTargets) -> dict:
    out: dict = {}
    if "alarm_names" in value:
        import capo_cloudwatch.types.mute_target_alarm_name_list

        out["AlarmNames"] = (
            capo_cloudwatch.types.mute_target_alarm_name_list.serialize_aws_json_1_0(
                value["alarm_names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MuteTargets:
    out: MuteTargets = {}  # type: ignore[typeddict-item]
    if data.get("AlarmNames") is not None:
        import capo_cloudwatch.types.mute_target_alarm_name_list

        out["alarm_names"] = (
            capo_cloudwatch.types.mute_target_alarm_name_list.deserialize_aws_json_1_0(
                data["AlarmNames"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MuteTargets, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_names" in value:
        import capo_cloudwatch.types.mute_target_alarm_name_list

        capo_cloudwatch.types.mute_target_alarm_name_list.serialize_query(
            value["alarm_names"], pairs, f"{key_prefix}AlarmNames"
        )


def deserialize_query(el: Element) -> MuteTargets:
    out: MuteTargets = {}  # type: ignore[typeddict-item]
    child_alarm_names = el.find("AlarmNames")
    if child_alarm_names is not None:
        import capo_cloudwatch.types.mute_target_alarm_name_list

        out["alarm_names"] = (
            capo_cloudwatch.types.mute_target_alarm_name_list.deserialize_query(
                child_alarm_names
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MuteTargets) -> dict:
    out: dict = {}
    if "alarm_names" in value:
        import capo_cloudwatch.types.mute_target_alarm_name_list

        out["AlarmNames"] = (
            capo_cloudwatch.types.mute_target_alarm_name_list.serialize_cbor(
                value["alarm_names"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> MuteTargets:
    out: MuteTargets = {}  # type: ignore[typeddict-item]
    if data.get("AlarmNames") is not None:
        import capo_cloudwatch.types.mute_target_alarm_name_list

        out["alarm_names"] = (
            capo_cloudwatch.types.mute_target_alarm_name_list.deserialize_cbor(
                data["AlarmNames"]
            )
        )
    return out
