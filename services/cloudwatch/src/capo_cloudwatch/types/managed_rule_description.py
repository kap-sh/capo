"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ManagedRuleDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.amazon_resource_name
    import capo_cloudwatch.types.managed_rule_state
    import capo_cloudwatch.types.template_name


class ManagedRuleDescription(TypedDict, closed=True):
    template_name: NotRequired["capo_cloudwatch.types.template_name.TemplateName"]
    """<p> The template name for the managed rule. Used to enable managed rules using <code>PutManagedInsightRules</code>. </p>"""
    resource_arn: NotRequired[
        "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p> If a managed rule is enabled, this is the ARN for the related Amazon Web Services resource. </p>"""
    rule_state: NotRequired["capo_cloudwatch.types.managed_rule_state.ManagedRuleState"]
    """<p> Describes the state of a managed rule. If present, it contains information about the Contributor Insights rule that contains information about the related Amazon Web Services resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedRuleDescription) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "rule_state" in value:
        import capo_cloudwatch.types.managed_rule_state

        out["RuleState"] = (
            capo_cloudwatch.types.managed_rule_state.serialize_aws_json_1_0(
                value["rule_state"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ManagedRuleDescription:
    out: ManagedRuleDescription = {}  # type: ignore[typeddict-item]
    if data.get("TemplateName") is not None:
        out["template_name"] = data["TemplateName"]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("RuleState") is not None:
        import capo_cloudwatch.types.managed_rule_state

        out["rule_state"] = (
            capo_cloudwatch.types.managed_rule_state.deserialize_aws_json_1_0(
                data["RuleState"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedRuleDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "template_name" in value:
        pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceARN", str(value["resource_arn"])))
    if "rule_state" in value:
        import capo_cloudwatch.types.managed_rule_state

        capo_cloudwatch.types.managed_rule_state.serialize_query(
            value["rule_state"], pairs, f"{key_prefix}RuleState"
        )


def deserialize_query(el: Element) -> ManagedRuleDescription:
    out: ManagedRuleDescription = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_resource_arn = el.find("ResourceARN")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_rule_state = el.find("RuleState")
    if child_rule_state is not None:
        import capo_cloudwatch.types.managed_rule_state

        out["rule_state"] = capo_cloudwatch.types.managed_rule_state.deserialize_query(
            child_rule_state
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ManagedRuleDescription) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "rule_state" in value:
        import capo_cloudwatch.types.managed_rule_state

        out["RuleState"] = capo_cloudwatch.types.managed_rule_state.serialize_cbor(
            value["rule_state"]
        )
    return out


def deserialize_cbor(data: dict) -> ManagedRuleDescription:
    out: ManagedRuleDescription = {}  # type: ignore[typeddict-item]
    if data.get("TemplateName") is not None:
        out["template_name"] = data["TemplateName"]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("RuleState") is not None:
        import capo_cloudwatch.types.managed_rule_state

        out["rule_state"] = capo_cloudwatch.types.managed_rule_state.deserialize_cbor(
            data["RuleState"]
        )
    return out
