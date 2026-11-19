"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListRuleTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.aws_region_name
    import capo_codepipeline.types.rule_owner


class ListRuleTypesInput(TypedDict, closed=True):
    rule_owner_filter: NotRequired["capo_codepipeline.types.rule_owner.RuleOwner"]
    """<p>The rule owner to filter on.</p>"""
    region_filter: NotRequired["capo_codepipeline.types.aws_region_name.AWSRegionName"]
    """<p>The rule Region to filter on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleTypesInput) -> dict:
    out: dict = {}
    if "rule_owner_filter" in value:
        import capo_codepipeline.types.rule_owner

        out["ruleOwnerFilter"] = (
            capo_codepipeline.types.rule_owner.serialize_aws_json_1_1(
                value["rule_owner_filter"]
            )
        )
    if "region_filter" in value:
        out["regionFilter"] = value["region_filter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleTypesInput:
    out: ListRuleTypesInput = {}  # type: ignore[typeddict-item]
    if data.get("ruleOwnerFilter") is not None:
        import capo_codepipeline.types.rule_owner

        out["rule_owner_filter"] = (
            capo_codepipeline.types.rule_owner.deserialize_aws_json_1_1(
                data["ruleOwnerFilter"]
            )
        )
    if data.get("regionFilter") is not None:
        out["region_filter"] = data["regionFilter"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRuleTypesInput) -> dict:
    out: dict = {}
    if "rule_owner_filter" in value:
        import capo_codepipeline.types.rule_owner

        out["ruleOwnerFilter"] = capo_codepipeline.types.rule_owner.serialize_cbor(
            value["rule_owner_filter"]
        )
    if "region_filter" in value:
        out["regionFilter"] = value["region_filter"]
    return out


def deserialize_cbor(data: dict) -> ListRuleTypesInput:
    out: ListRuleTypesInput = {}  # type: ignore[typeddict-item]
    if data.get("ruleOwnerFilter") is not None:
        import capo_codepipeline.types.rule_owner

        out["rule_owner_filter"] = capo_codepipeline.types.rule_owner.deserialize_cbor(
            data["ruleOwnerFilter"]
        )
    if data.get("regionFilter") is not None:
        out["region_filter"] = data["regionFilter"]
    return out
