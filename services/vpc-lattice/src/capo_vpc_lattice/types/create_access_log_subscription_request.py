"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateAccessLogSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.access_log_destination_arn
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.resource_identifier
    import capo_vpc_lattice.types.service_network_log_type
    import capo_vpc_lattice.types.tag_map


class CreateAccessLogSubscriptionRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier"
    """<p>The ID or ARN of the service network or service.</p>"""
    destination_arn: (
        "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.</p>"""
    service_network_log_type: NotRequired[
        "capo_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
    ]
    """<p>The type of log that monitors your Amazon VPC Lattice service networks.</p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the access log subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessLogSubscriptionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["resourceIdentifier"] = value["resource_identifier"]
    out["destinationArn"] = value["destination_arn"]
    if "service_network_log_type" in value:
        out["serviceNetworkLogType"] = value["service_network_log_type"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAccessLogSubscriptionRequest:
    out: CreateAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        out["resource_identifier"] = ""
    if data.get("destinationArn") is not None:
        out["destination_arn"] = data["destinationArn"]
    else:
        out["destination_arn"] = ""
    if data.get("serviceNetworkLogType") is not None:
        out["service_network_log_type"] = data["serviceNetworkLogType"]
    if data.get("tags") is not None:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
