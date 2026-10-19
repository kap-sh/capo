"""Generated from Smithy shape ``com.amazonaws.route53resolver#DisassociateResolverQueryLogConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class DisassociateResolverQueryLogConfigRequest(TypedDict, closed=True):
    resolver_query_log_config_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the query logging configuration that you want to disassociate a specified VPC from.</p>"""
    resource_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Amazon VPC that you want to disassociate from a specified query logging configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateResolverQueryLogConfigRequest) -> dict:
    out: dict = {}
    out["ResolverQueryLogConfigId"] = value["resolver_query_log_config_id"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateResolverQueryLogConfigRequest:
    out: DisassociateResolverQueryLogConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverQueryLogConfigId") is not None:
        out["resolver_query_log_config_id"] = data["ResolverQueryLogConfigId"]
    else:
        out["resolver_query_log_config_id"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    return out
