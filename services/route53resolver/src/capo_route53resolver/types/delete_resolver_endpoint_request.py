"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteResolverEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class DeleteResolverEndpointRequest(TypedDict, closed=True):
    resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver endpoint that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResolverEndpointRequest) -> dict:
    out: dict = {}
    out["ResolverEndpointId"] = value["resolver_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResolverEndpointRequest:
    out: DeleteResolverEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverEndpointId") is not None:
        out["resolver_endpoint_id"] = data["ResolverEndpointId"]
    else:
        out["resolver_endpoint_id"] = ""
    return out
