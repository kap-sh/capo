"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_proxy_rule_effect_type
    import capo_codebuild.types.fleet_proxy_rule_entities
    import capo_codebuild.types.fleet_proxy_rule_type


class FleetProxyRule(TypedDict, closed=True):
    type: "capo_codebuild.types.fleet_proxy_rule_type.FleetProxyRuleType"
    """<p>The type of proxy rule.</p>"""
    effect: "capo_codebuild.types.fleet_proxy_rule_effect_type.FleetProxyRuleEffectType"
    """<p>The behavior of the proxy rule.</p>"""
    entities: "capo_codebuild.types.fleet_proxy_rule_entities.FleetProxyRuleEntities"
    """<p>The destination of the proxy rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetProxyRule) -> dict:
    out: dict = {}
    import capo_codebuild.types.fleet_proxy_rule_type

    out["type"] = capo_codebuild.types.fleet_proxy_rule_type.serialize_aws_json_1_1(
        value["type"]
    )
    import capo_codebuild.types.fleet_proxy_rule_effect_type

    out["effect"] = (
        capo_codebuild.types.fleet_proxy_rule_effect_type.serialize_aws_json_1_1(
            value["effect"]
        )
    )
    import capo_codebuild.types.fleet_proxy_rule_entities

    out["entities"] = (
        capo_codebuild.types.fleet_proxy_rule_entities.serialize_aws_json_1_1(
            value["entities"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetProxyRule:
    out: FleetProxyRule = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.fleet_proxy_rule_type

        out["type"] = (
            capo_codebuild.types.fleet_proxy_rule_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_codebuild.types.fleet_proxy_rule_type.FleetProxyRuleType", ""
        )
    if data.get("effect") is not None:
        import capo_codebuild.types.fleet_proxy_rule_effect_type

        out["effect"] = (
            capo_codebuild.types.fleet_proxy_rule_effect_type.deserialize_aws_json_1_1(
                data["effect"]
            )
        )
    else:
        import typing

        out["effect"] = typing.cast(
            "capo_codebuild.types.fleet_proxy_rule_effect_type.FleetProxyRuleEffectType",
            "",
        )
    if data.get("entities") is not None:
        import capo_codebuild.types.fleet_proxy_rule_entities

        out["entities"] = (
            capo_codebuild.types.fleet_proxy_rule_entities.deserialize_aws_json_1_1(
                data["entities"]
            )
        )
    else:
        out["entities"] = []
    return out
