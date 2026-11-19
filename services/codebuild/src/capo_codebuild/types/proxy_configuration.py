"""Generated from Smithy shape ``com.amazonaws.codebuild#ProxyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_proxy_rule_behavior
    import capo_codebuild.types.fleet_proxy_rules


class ProxyConfiguration(TypedDict, closed=True):
    default_behavior: NotRequired[
        "capo_codebuild.types.fleet_proxy_rule_behavior.FleetProxyRuleBehavior"
    ]
    """<p>The default behavior of outgoing traffic.</p>"""
    ordered_proxy_rules: NotRequired[
        "capo_codebuild.types.fleet_proxy_rules.FleetProxyRules"
    ]
    """<p>An array of <code>FleetProxyRule</code> objects that represent the specified destination domains or IPs to allow or deny network access control to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProxyConfiguration) -> dict:
    out: dict = {}
    if "default_behavior" in value:
        import capo_codebuild.types.fleet_proxy_rule_behavior

        out["defaultBehavior"] = (
            capo_codebuild.types.fleet_proxy_rule_behavior.serialize_aws_json_1_1(
                value["default_behavior"]
            )
        )
    if "ordered_proxy_rules" in value:
        import capo_codebuild.types.fleet_proxy_rules

        out["orderedProxyRules"] = (
            capo_codebuild.types.fleet_proxy_rules.serialize_aws_json_1_1(
                value["ordered_proxy_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProxyConfiguration:
    out: ProxyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("defaultBehavior") is not None:
        import capo_codebuild.types.fleet_proxy_rule_behavior

        out["default_behavior"] = (
            capo_codebuild.types.fleet_proxy_rule_behavior.deserialize_aws_json_1_1(
                data["defaultBehavior"]
            )
        )
    if data.get("orderedProxyRules") is not None:
        import capo_codebuild.types.fleet_proxy_rules

        out["ordered_proxy_rules"] = (
            capo_codebuild.types.fleet_proxy_rules.deserialize_aws_json_1_1(
                data["orderedProxyRules"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProxyConfiguration) -> dict:
    out: dict = {}
    if "default_behavior" in value:
        import capo_codebuild.types.fleet_proxy_rule_behavior

        out["defaultBehavior"] = (
            capo_codebuild.types.fleet_proxy_rule_behavior.serialize_cbor(
                value["default_behavior"]
            )
        )
    if "ordered_proxy_rules" in value:
        import capo_codebuild.types.fleet_proxy_rules

        out["orderedProxyRules"] = (
            capo_codebuild.types.fleet_proxy_rules.serialize_cbor(
                value["ordered_proxy_rules"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ProxyConfiguration:
    out: ProxyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("defaultBehavior") is not None:
        import capo_codebuild.types.fleet_proxy_rule_behavior

        out["default_behavior"] = (
            capo_codebuild.types.fleet_proxy_rule_behavior.deserialize_cbor(
                data["defaultBehavior"]
            )
        )
    if data.get("orderedProxyRules") is not None:
        import capo_codebuild.types.fleet_proxy_rules

        out["ordered_proxy_rules"] = (
            capo_codebuild.types.fleet_proxy_rules.deserialize_cbor(
                data["orderedProxyRules"]
            )
        )
    return out
