"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_verdict

RuleVerdictValueList: TypeAlias = list[
    "capo_mailmanager.types.rule_verdict.RuleVerdict"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVerdictValueList) -> list:
    import capo_mailmanager.types.rule_verdict

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.rule_verdict.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RuleVerdictValueList:
    import capo_mailmanager.types.rule_verdict

    out: RuleVerdictValueList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.rule_verdict.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleVerdictValueList) -> list:
    import capo_mailmanager.types.rule_verdict

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.rule_verdict.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RuleVerdictValueList:
    import capo_mailmanager.types.rule_verdict

    out: RuleVerdictValueList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.rule_verdict.deserialize_cbor(item))
    return out
