"""Generated from Smithy shape ``com.amazonaws.interconnect#ConnectionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.amazon_resource_name
    import capo_interconnect.types.attach_point
    import capo_interconnect.types.billing_tier
    import capo_interconnect.types.connection_bandwidth
    import capo_interconnect.types.connection_description
    import capo_interconnect.types.connection_id
    import capo_interconnect.types.connection_shared_id
    import capo_interconnect.types.connection_state
    import capo_interconnect.types.environment_id
    import capo_interconnect.types.location
    import capo_interconnect.types.product_type
    import capo_interconnect.types.provider


class ConnectionSummary(TypedDict, closed=True):
    id: "capo_interconnect.types.connection_id.ConnectionId"
    """<p>The identifier of the requested <a>Connection</a> </p>"""
    arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the <a>Connection</a> </p>"""
    description: "capo_interconnect.types.connection_description.ConnectionDescription"
    """<p>A descriptive name of the <a>Connection</a> </p>"""
    bandwidth: "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth"
    """<p>The bandwidth of the <a>Connection</a> </p>"""
    attach_point: "capo_interconnect.types.attach_point.AttachPoint"
    """<p>The Attach Point to which the connection should be associated.</p>"""
    environment_id: "capo_interconnect.types.environment_id.EnvironmentId"
    """<p>The <a>Environment</a> that this <a>Connection</a> is created on.</p>"""
    provider: "capo_interconnect.types.provider.Provider"
    """<p>The provider on the remote end of this <a>Connection</a> </p>"""
    location: "capo_interconnect.types.location.Location"
    """<p>The provider specific location at the remote end of this <a>Connection</a> </p>"""
    type: "capo_interconnect.types.product_type.ProductType"
    """<p>The product variant supplied by this resource.</p>"""
    state: "capo_interconnect.types.connection_state.ConnectionState"
    """<ul> <li> <p> <code>requested</code>: The initial state of a connection. The state will remain here until the Connection is accepted on the Partner portal.</p> </li> <li> <p> <code>pending</code>: The connection has been accepted and is being provisioned between AWS and the Partner.</p> </li> <li> <p> <code>available</code>: The connection has been fully provisioned between AWS and the Partner.</p> </li> <li> <p> <code>deleting</code>: The connection is being deleted.</p> </li> <li> <p> <code>deleted</code>: The connection has been deleted.</p> </li> <li> <p> <code>failed</code>: The connection has failed to be created.</p> </li> <li> <p> <code>updating</code>: The connection is being updated.</p> </li> </ul>"""
    shared_id: "capo_interconnect.types.connection_shared_id.ConnectionSharedId"
    """<p>An identifier used by both AWS and the remote partner to identify the specific connection.</p>"""
    billing_tier: NotRequired["capo_interconnect.types.billing_tier.BillingTier"]
    """<p>The billing tier this connection is currently assigned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["description"] = value["description"]
    out["bandwidth"] = value["bandwidth"]
    import capo_interconnect.types.attach_point

    out["attachPoint"] = capo_interconnect.types.attach_point.serialize_aws_json_1_0(
        value["attach_point"]
    )
    out["environmentId"] = value["environment_id"]
    import capo_interconnect.types.provider

    out["provider"] = capo_interconnect.types.provider.serialize_aws_json_1_0(
        value["provider"]
    )
    out["location"] = value["location"]
    out["type"] = value["type"]
    import capo_interconnect.types.connection_state

    out["state"] = capo_interconnect.types.connection_state.serialize_aws_json_1_0(
        value["state"]
    )
    out["sharedId"] = value["shared_id"]
    if "billing_tier" in value:
        out["billingTier"] = value["billing_tier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionSummary:
    out: ConnectionSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    else:
        out["bandwidth"] = ""
    if data.get("attachPoint") is not None:
        import capo_interconnect.types.attach_point

        out["attach_point"] = (
            capo_interconnect.types.attach_point.deserialize_aws_json_1_0(
                data["attachPoint"]
            )
        )
    else:
        out["attach_point"] = {"$unknown": {"name": ""}}
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("provider") is not None:
        import capo_interconnect.types.provider

        out["provider"] = capo_interconnect.types.provider.deserialize_aws_json_1_0(
            data["provider"]
        )
    else:
        out["provider"] = {"$unknown": {"name": ""}}
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("state") is not None:
        import capo_interconnect.types.connection_state

        out["state"] = (
            capo_interconnect.types.connection_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_interconnect.types.connection_state.ConnectionState", ""
        )
    if data.get("sharedId") is not None:
        out["shared_id"] = data["sharedId"]
    else:
        out["shared_id"] = ""
    if data.get("billingTier") is not None:
        out["billing_tier"] = data["billingTier"]
    return out
