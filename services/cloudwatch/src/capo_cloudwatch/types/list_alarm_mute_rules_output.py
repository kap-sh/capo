"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListAlarmMuteRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_mute_rule_summaries
    import capo_cloudwatch.types.next_token


class ListAlarmMuteRulesOutput(TypedDict, closed=True):
    alarm_mute_rule_summaries: NotRequired[
        "capo_cloudwatch.types.alarm_mute_rule_summaries.AlarmMuteRuleSummaries"
    ]
    """<p>A list of alarm mute rule summaries.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of results. If this field is absent, there are no more results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAlarmMuteRulesOutput) -> dict:
    out: dict = {}
    if "alarm_mute_rule_summaries" in value:
        import capo_cloudwatch.types.alarm_mute_rule_summaries

        out["AlarmMuteRuleSummaries"] = (
            capo_cloudwatch.types.alarm_mute_rule_summaries.serialize_aws_json_1_0(
                value["alarm_mute_rule_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAlarmMuteRulesOutput:
    out: ListAlarmMuteRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmMuteRuleSummaries") is not None:
        import capo_cloudwatch.types.alarm_mute_rule_summaries

        out["alarm_mute_rule_summaries"] = (
            capo_cloudwatch.types.alarm_mute_rule_summaries.deserialize_aws_json_1_0(
                data["AlarmMuteRuleSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListAlarmMuteRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_mute_rule_summaries" in value:
        import capo_cloudwatch.types.alarm_mute_rule_summaries

        capo_cloudwatch.types.alarm_mute_rule_summaries.serialize_query(
            value["alarm_mute_rule_summaries"],
            pairs,
            f"{key_prefix}AlarmMuteRuleSummaries",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListAlarmMuteRulesOutput:
    out: ListAlarmMuteRulesOutput = {}  # type: ignore[typeddict-item]
    child_alarm_mute_rule_summaries = el.find("AlarmMuteRuleSummaries")
    if child_alarm_mute_rule_summaries is not None:
        import capo_cloudwatch.types.alarm_mute_rule_summaries

        out["alarm_mute_rule_summaries"] = (
            capo_cloudwatch.types.alarm_mute_rule_summaries.deserialize_query(
                child_alarm_mute_rule_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAlarmMuteRulesOutput) -> dict:
    out: dict = {}
    if "alarm_mute_rule_summaries" in value:
        import capo_cloudwatch.types.alarm_mute_rule_summaries

        out["AlarmMuteRuleSummaries"] = (
            capo_cloudwatch.types.alarm_mute_rule_summaries.serialize_cbor(
                value["alarm_mute_rule_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAlarmMuteRulesOutput:
    out: ListAlarmMuteRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmMuteRuleSummaries") is not None:
        import capo_cloudwatch.types.alarm_mute_rule_summaries

        out["alarm_mute_rule_summaries"] = (
            capo_cloudwatch.types.alarm_mute_rule_summaries.deserialize_cbor(
                data["AlarmMuteRuleSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
