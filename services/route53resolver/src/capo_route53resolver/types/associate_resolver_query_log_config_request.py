"""Generated from Smithy shape ``com.amazonaws.route53resolver#AssociateResolverQueryLogConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class AssociateResolverQueryLogConfigRequest(TypedDict, closed=True):
    resolver_query_log_config_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the query logging configuration that you want to associate a VPC with.</p>"""
    resource_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of an Amazon VPC that you want this query logging configuration to log queries for.</p> <note> <p>The VPCs and the query logging configuration must be in the same Region.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateResolverQueryLogConfigRequest) -> dict:
    out: dict = {}
    out["ResolverQueryLogConfigId"] = value["resolver_query_log_config_id"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateResolverQueryLogConfigRequest:
    out: AssociateResolverQueryLogConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverQueryLogConfigId") is not None:
        out["resolver_query_log_config_id"] = data["ResolverQueryLogConfigId"]
    else:
        out["resolver_query_log_config_id"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    return out
