"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetAccessLogSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.access_log_destination_arn
    import capo_vpc_lattice.types.access_log_subscription_arn
    import capo_vpc_lattice.types.access_log_subscription_id
    import capo_vpc_lattice.types.resource_arn
    import capo_vpc_lattice.types.resource_id
    import capo_vpc_lattice.types.service_network_log_type
    import capo_vpc_lattice.types.timestamp


class GetAccessLogSubscriptionResponse(TypedDict, closed=True):
    id: "capo_vpc_lattice.types.access_log_subscription_id.AccessLogSubscriptionId"
    """<p>The ID of the access log subscription.</p>"""
    arn: "capo_vpc_lattice.types.access_log_subscription_arn.AccessLogSubscriptionArn"
    """<p>The Amazon Resource Name (ARN) of the access log subscription.</p>"""
    resource_id: "capo_vpc_lattice.types.resource_id.ResourceId"
    """<p>The ID of the service network or service.</p>"""
    resource_arn: "capo_vpc_lattice.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the service network or service.</p>"""
    destination_arn: (
        "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the access log destination.</p>"""
    service_network_log_type: NotRequired[
        "capo_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
    ]
    """<p>The log type for the service network.</p>"""
    created_at: "capo_vpc_lattice.types.timestamp.Timestamp"
    """<p>The date and time that the access log subscription was created, in ISO-8601 format.</p>"""
    last_updated_at: "capo_vpc_lattice.types.timestamp.Timestamp"
    """<p>The date and time that the access log subscription was last updated, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessLogSubscriptionResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    out["destinationArn"] = value["destination_arn"]
    if "service_network_log_type" in value:
        out["serviceNetworkLogType"] = value["service_network_log_type"]
    import capo_vpc_lattice.types.timestamp

    out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_vpc_lattice.types.timestamp

    out["lastUpdatedAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetAccessLogSubscriptionResponse:
    out: GetAccessLogSubscriptionResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("destinationArn") is not None:
        out["destination_arn"] = data["destinationArn"]
    else:
        out["destination_arn"] = ""
    if data.get("serviceNetworkLogType") is not None:
        out["service_network_log_type"] = data["serviceNetworkLogType"]
    if data.get("createdAt") is not None:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdatedAt") is not None:
        import capo_vpc_lattice.types.timestamp

        out["last_updated_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
