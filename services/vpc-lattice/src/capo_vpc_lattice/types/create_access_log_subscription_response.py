"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateAccessLogSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.access_log_destination_arn
    import capo_vpc_lattice.types.access_log_subscription_arn
    import capo_vpc_lattice.types.access_log_subscription_id
    import capo_vpc_lattice.types.resource_arn
    import capo_vpc_lattice.types.resource_id
    import capo_vpc_lattice.types.service_network_log_type


class CreateAccessLogSubscriptionResponse(TypedDict, closed=True):
    id: "capo_vpc_lattice.types.access_log_subscription_id.AccessLogSubscriptionId"
    """<p>The ID of the access log subscription.</p>"""
    arn: "capo_vpc_lattice.types.access_log_subscription_arn.AccessLogSubscriptionArn"
    """<p>The Amazon Resource Name (ARN) of the access log subscription.</p>"""
    resource_id: "capo_vpc_lattice.types.resource_id.ResourceId"
    """<p>The ID of the service network or service.</p>"""
    resource_arn: "capo_vpc_lattice.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the service network or service.</p>"""
    service_network_log_type: NotRequired[
        "capo_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
    ]
    """<p>The type of log that monitors your Amazon VPC Lattice service networks.</p>"""
    destination_arn: (
        "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the log destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessLogSubscriptionResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    if "service_network_log_type" in value:
        out["serviceNetworkLogType"] = value["service_network_log_type"]
    out["destinationArn"] = value["destination_arn"]
    return out


def deserialize_json(data: dict) -> CreateAccessLogSubscriptionResponse:
    out: CreateAccessLogSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("serviceNetworkLogType") is not None:
        out["service_network_log_type"] = data["serviceNetworkLogType"]
    if data.get("destinationArn") is not None:
        out["destination_arn"] = data["destinationArn"]
    else:
        out["destination_arn"] = ""
    return out
