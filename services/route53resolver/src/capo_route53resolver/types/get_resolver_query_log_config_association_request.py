"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverQueryLogConfigAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class GetResolverQueryLogConfigAssociationRequest(TypedDict, closed=True):
    resolver_query_log_config_association_id: (
        "capo_route53resolver.types.resource_id.ResourceId"
    )
    """<p>The ID of the Resolver query logging configuration association that you want to get information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverQueryLogConfigAssociationRequest) -> dict:
    out: dict = {}
    out["ResolverQueryLogConfigAssociationId"] = value[
        "resolver_query_log_config_association_id"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverQueryLogConfigAssociationRequest:
    out: GetResolverQueryLogConfigAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverQueryLogConfigAssociationId") is not None:
        out["resolver_query_log_config_association_id"] = data[
            "ResolverQueryLogConfigAssociationId"
        ]
    else:
        out["resolver_query_log_config_association_id"] = ""
    return out
