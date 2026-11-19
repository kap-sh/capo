"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleDmarcValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_dmarc_policy

RuleDmarcValueList: TypeAlias = list[
    "capo_mailmanager.types.rule_dmarc_policy.RuleDmarcPolicy"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleDmarcValueList) -> list:
    import capo_mailmanager.types.rule_dmarc_policy

    out: list = []
    for item in value:
        out.append(
            capo_mailmanager.types.rule_dmarc_policy.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RuleDmarcValueList:
    import capo_mailmanager.types.rule_dmarc_policy

    out: RuleDmarcValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mailmanager.types.rule_dmarc_policy.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleDmarcValueList) -> list:
    import capo_mailmanager.types.rule_dmarc_policy

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.rule_dmarc_policy.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RuleDmarcValueList:
    import capo_mailmanager.types.rule_dmarc_policy

    out: RuleDmarcValueList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.rule_dmarc_policy.deserialize_cbor(item))
    return out
