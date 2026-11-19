"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ManagedRuleState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_name
    import capo_cloudwatch.types.insight_rule_state


class ManagedRuleState(TypedDict, closed=True):
    rule_name: NotRequired["capo_cloudwatch.types.insight_rule_name.InsightRuleName"]
    """<p> The name of the Contributor Insights rule that contains data for the specified Amazon Web Services resource. </p>"""
    state: NotRequired["capo_cloudwatch.types.insight_rule_state.InsightRuleState"]
    """<p> Indicates whether the rule is enabled or disabled. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedRuleState) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ManagedRuleState:
    out: ManagedRuleState = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedRuleState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_name" in value:
        pairs.append((f"{key_prefix}RuleName", str(value["rule_name"])))
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))


def deserialize_query(el: Element) -> ManagedRuleState:
    out: ManagedRuleState = {}  # type: ignore[typeddict-item]
    child_rule_name = el.find("RuleName")
    if child_rule_name is not None:
        out["rule_name"] = str(child_rule_name.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ManagedRuleState) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_cbor(data: dict) -> ManagedRuleState:
    out: ManagedRuleState = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    return out
