"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteResolverRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class DeleteResolverRuleRequest(TypedDict, closed=True):
    resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver rule that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResolverRuleRequest) -> dict:
    out: dict = {}
    out["ResolverRuleId"] = value["resolver_rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResolverRuleRequest:
    out: DeleteResolverRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverRuleId") is not None:
        out["resolver_rule_id"] = data["ResolverRuleId"]
    else:
        out["resolver_rule_id"] = ""
    return out
