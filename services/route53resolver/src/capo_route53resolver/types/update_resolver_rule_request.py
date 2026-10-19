"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateResolverRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_rule_config
    import capo_route53resolver.types.resource_id


class UpdateResolverRuleRequest(TypedDict, closed=True):
    resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver rule that you want to update.</p>"""
    config: "capo_route53resolver.types.resolver_rule_config.ResolverRuleConfig"
    """<p>The new settings for the Resolver rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResolverRuleRequest) -> dict:
    out: dict = {}
    out["ResolverRuleId"] = value["resolver_rule_id"]
    import capo_route53resolver.types.resolver_rule_config

    out["Config"] = (
        capo_route53resolver.types.resolver_rule_config.serialize_aws_json_1_1(
            value["config"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResolverRuleRequest:
    out: UpdateResolverRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverRuleId") is not None:
        out["resolver_rule_id"] = data["ResolverRuleId"]
    else:
        out["resolver_rule_id"] = ""
    if data.get("Config") is not None:
        import capo_route53resolver.types.resolver_rule_config

        out["config"] = (
            capo_route53resolver.types.resolver_rule_config.deserialize_aws_json_1_1(
                data["Config"]
            )
        )
    else:
        raise DeserializationError("UpdateResolverRuleRequest.config required")
    return out
