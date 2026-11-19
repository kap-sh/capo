"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmMuteRuleStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

AlarmMuteRuleStatus: TypeAlias = Literal[
    "SCHEDULED",
    "ACTIVE",
    "EXPIRED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmMuteRuleStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AlarmMuteRuleStatus:
    return cast(AlarmMuteRuleStatus, data)


# --- awsQuery ser/de ---
def to_query_text(value: AlarmMuteRuleStatus) -> str:
    return value


def from_query_text(text: str) -> AlarmMuteRuleStatus:
    return cast(AlarmMuteRuleStatus, text)


def serialize_query(
    value: AlarmMuteRuleStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AlarmMuteRuleStatus:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmMuteRuleStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AlarmMuteRuleStatus:
    return cast(AlarmMuteRuleStatus, data)
