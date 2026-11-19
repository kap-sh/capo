"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmMuteRuleStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_mute_rule_status

AlarmMuteRuleStatuses: TypeAlias = list[
    "capo_cloudwatch.types.alarm_mute_rule_status.AlarmMuteRuleStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmMuteRuleStatuses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.alarm_mute_rule_status

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.alarm_mute_rule_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AlarmMuteRuleStatuses:
    import capo_cloudwatch.types.alarm_mute_rule_status

    out: AlarmMuteRuleStatuses = []
    for child in el.findall("member"):
        out.append(
            capo_cloudwatch.types.alarm_mute_rule_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AlarmMuteRuleStatuses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.alarm_mute_rule_status

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.alarm_mute_rule_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AlarmMuteRuleStatuses:
    import capo_cloudwatch.types.alarm_mute_rule_status

    out: AlarmMuteRuleStatuses = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudwatch.types.alarm_mute_rule_status.deserialize_query(child)
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmMuteRuleStatuses) -> list:
    import capo_cloudwatch.types.alarm_mute_rule_status

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.alarm_mute_rule_status.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AlarmMuteRuleStatuses:
    import capo_cloudwatch.types.alarm_mute_rule_status

    out: AlarmMuteRuleStatuses = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.alarm_mute_rule_status.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmMuteRuleStatuses) -> list:
    import capo_cloudwatch.types.alarm_mute_rule_status

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.alarm_mute_rule_status.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AlarmMuteRuleStatuses:
    import capo_cloudwatch.types.alarm_mute_rule_status

    out: AlarmMuteRuleStatuses = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.alarm_mute_rule_status.deserialize_cbor(item))
    return out
