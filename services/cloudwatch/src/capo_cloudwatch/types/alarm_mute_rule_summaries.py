"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmMuteRuleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_mute_rule_summary

AlarmMuteRuleSummaries: TypeAlias = list[
    "capo_cloudwatch.types.alarm_mute_rule_summary.AlarmMuteRuleSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmMuteRuleSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.alarm_mute_rule_summary

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.alarm_mute_rule_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AlarmMuteRuleSummaries:
    import capo_cloudwatch.types.alarm_mute_rule_summary

    out: AlarmMuteRuleSummaries = []
    for child in el.findall("member"):
        out.append(
            capo_cloudwatch.types.alarm_mute_rule_summary.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AlarmMuteRuleSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.alarm_mute_rule_summary

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.alarm_mute_rule_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AlarmMuteRuleSummaries:
    import capo_cloudwatch.types.alarm_mute_rule_summary

    out: AlarmMuteRuleSummaries = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudwatch.types.alarm_mute_rule_summary.deserialize_query(child)
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmMuteRuleSummaries) -> list:
    import capo_cloudwatch.types.alarm_mute_rule_summary

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.alarm_mute_rule_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AlarmMuteRuleSummaries:
    import capo_cloudwatch.types.alarm_mute_rule_summary

    out: AlarmMuteRuleSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.alarm_mute_rule_summary.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmMuteRuleSummaries) -> list:
    import capo_cloudwatch.types.alarm_mute_rule_summary

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.alarm_mute_rule_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AlarmMuteRuleSummaries:
    import capo_cloudwatch.types.alarm_mute_rule_summary

    out: AlarmMuteRuleSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.alarm_mute_rule_summary.deserialize_cbor(item))
    return out
