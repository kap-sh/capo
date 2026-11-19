"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetAlarmMuteRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.name


class GetAlarmMuteRuleInput(TypedDict, closed=True):
    alarm_mute_rule_name: NotRequired["capo_cloudwatch.types.name.Name"]
    """<p>The name of the alarm mute rule to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAlarmMuteRuleInput) -> dict:
    out: dict = {}
    if "alarm_mute_rule_name" in value:
        out["AlarmMuteRuleName"] = value["alarm_mute_rule_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAlarmMuteRuleInput:
    out: GetAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmMuteRuleName") is not None:
        out["alarm_mute_rule_name"] = data["AlarmMuteRuleName"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAlarmMuteRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_mute_rule_name" in value:
        pairs.append(
            (f"{key_prefix}AlarmMuteRuleName", str(value["alarm_mute_rule_name"]))
        )


def deserialize_query(el: Element) -> GetAlarmMuteRuleInput:
    out: GetAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    child_alarm_mute_rule_name = el.find("AlarmMuteRuleName")
    if child_alarm_mute_rule_name is not None:
        out["alarm_mute_rule_name"] = str(child_alarm_mute_rule_name.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAlarmMuteRuleInput) -> dict:
    out: dict = {}
    if "alarm_mute_rule_name" in value:
        out["AlarmMuteRuleName"] = value["alarm_mute_rule_name"]
    return out


def deserialize_cbor(data: dict) -> GetAlarmMuteRuleInput:
    out: GetAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmMuteRuleName") is not None:
        out["alarm_mute_rule_name"] = data["AlarmMuteRuleName"]
    return out
