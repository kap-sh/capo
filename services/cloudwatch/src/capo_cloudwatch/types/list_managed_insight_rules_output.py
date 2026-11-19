"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListManagedInsightRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.managed_rule_descriptions
    import capo_cloudwatch.types.next_token


class ListManagedInsightRulesOutput(TypedDict, closed=True):
    managed_rules: NotRequired[
        "capo_cloudwatch.types.managed_rule_descriptions.ManagedRuleDescriptions"
    ]
    """<p> The managed rules that are available for the specified Amazon Web Services resource. </p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p> Include this value to get the next set of rules if the value was returned by the previous operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListManagedInsightRulesOutput) -> dict:
    out: dict = {}
    if "managed_rules" in value:
        import capo_cloudwatch.types.managed_rule_descriptions

        out["ManagedRules"] = (
            capo_cloudwatch.types.managed_rule_descriptions.serialize_aws_json_1_0(
                value["managed_rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListManagedInsightRulesOutput:
    out: ListManagedInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("ManagedRules") is not None:
        import capo_cloudwatch.types.managed_rule_descriptions

        out["managed_rules"] = (
            capo_cloudwatch.types.managed_rule_descriptions.deserialize_aws_json_1_0(
                data["ManagedRules"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListManagedInsightRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "managed_rules" in value:
        import capo_cloudwatch.types.managed_rule_descriptions

        capo_cloudwatch.types.managed_rule_descriptions.serialize_query(
            value["managed_rules"], pairs, f"{key_prefix}ManagedRules"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListManagedInsightRulesOutput:
    out: ListManagedInsightRulesOutput = {}  # type: ignore[typeddict-item]
    child_managed_rules = el.find("ManagedRules")
    if child_managed_rules is not None:
        import capo_cloudwatch.types.managed_rule_descriptions

        out["managed_rules"] = (
            capo_cloudwatch.types.managed_rule_descriptions.deserialize_query(
                child_managed_rules
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListManagedInsightRulesOutput) -> dict:
    out: dict = {}
    if "managed_rules" in value:
        import capo_cloudwatch.types.managed_rule_descriptions

        out["ManagedRules"] = (
            capo_cloudwatch.types.managed_rule_descriptions.serialize_cbor(
                value["managed_rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListManagedInsightRulesOutput:
    out: ListManagedInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("ManagedRules") is not None:
        import capo_cloudwatch.types.managed_rule_descriptions

        out["managed_rules"] = (
            capo_cloudwatch.types.managed_rule_descriptions.deserialize_cbor(
                data["ManagedRules"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
