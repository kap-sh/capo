"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverQueryLogConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class GetResolverQueryLogConfigRequest(TypedDict, closed=True):
    resolver_query_log_config_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver query logging configuration that you want to get information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverQueryLogConfigRequest) -> dict:
    out: dict = {}
    out["ResolverQueryLogConfigId"] = value["resolver_query_log_config_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverQueryLogConfigRequest:
    out: GetResolverQueryLogConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverQueryLogConfigId") is not None:
        out["resolver_query_log_config_id"] = data["ResolverQueryLogConfigId"]
    else:
        out["resolver_query_log_config_id"] = ""
    return out
