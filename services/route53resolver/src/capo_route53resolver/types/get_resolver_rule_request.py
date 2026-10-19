"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class GetResolverRuleRequest(TypedDict, closed=True):
    resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver rule that you want to get information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverRuleRequest) -> dict:
    out: dict = {}
    out["ResolverRuleId"] = value["resolver_rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverRuleRequest:
    out: GetResolverRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverRuleId") is not None:
        out["resolver_rule_id"] = data["ResolverRuleId"]
    else:
        out["resolver_rule_id"] = ""
    return out
