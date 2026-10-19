"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class GetResolverConfigRequest(TypedDict, closed=True):
    resource_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>Resource ID of the Amazon VPC that you want to get information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverConfigRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverConfigRequest:
    out: GetResolverConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    return out
