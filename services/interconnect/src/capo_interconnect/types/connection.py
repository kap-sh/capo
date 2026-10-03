"""Generated from Smithy shape ``com.amazonaws.interconnect#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_interconnect.types.activation_key
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
    import capo_interconnect.types.owner_account_id
    import capo_interconnect.types.product_type
    import capo_interconnect.types.provider
    import capo_interconnect.types.tag_map


class Connection(TypedDict, closed=True):
    id: "capo_interconnect.types.connection_id.ConnectionId"
    """<p>The short identifier of the connection object.</p>"""
    arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName"
    """<p>An ARN of a <a>Connection</a> object.</p>"""
    description: "capo_interconnect.types.connection_description.ConnectionDescription"
    """<p>A descriptive name for the connection.</p>"""
    bandwidth: "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth"
    """<p>The specific selected bandwidth of this connection.</p>"""
    attach_point: "capo_interconnect.types.attach_point.AttachPoint"
    """<p>The Attach Point to which the connection should be associated."</p>"""
    environment_id: "capo_interconnect.types.environment_id.EnvironmentId"
    """<p>The specific <a>Environment</a> this connection is placed upon.</p>"""
    provider: "capo_interconnect.types.provider.Provider"
    """<p>The provider on the remote side of this <a>Connection</a>.</p>"""
    location: "capo_interconnect.types.location.Location"
    """<p>The provider specific location on the remote side of this <a>Connection</a> </p>"""
    type: "capo_interconnect.types.product_type.ProductType"
    """<p>The specific product type of this <a>Connection</a>.</p>"""
    state: "capo_interconnect.types.connection_state.ConnectionState"
    """<ul> <li> <p> <code>requested</code>: The initial state of a connection. The state will remain here until the Connection is accepted on the Partner portal.</p> </li> <li> <p> <code>pending</code>: The connection has been accepted and is being provisioned between AWS and the Partner.</p> </li> <li> <p> <code>available</code>: The connection has been fully provisioned between AWS and the Partner.</p> </li> <li> <p> <code>deleting</code>: The connection is being deleted.</p> </li> <li> <p> <code>deleted</code>: The connection has been deleted.</p> </li> <li> <p> <code>failed</code>: The connection has failed to be created.</p> </li> <li> <p> <code>updating</code>: The connection is being updated.</p> </li> </ul>"""
    shared_id: "capo_interconnect.types.connection_shared_id.ConnectionSharedId"
    """<p>An identifier used by both AWS and the remote partner to identify the specific connection.</p>"""
    billing_tier: NotRequired["capo_interconnect.types.billing_tier.BillingTier"]
    """<p>The billing tier this connection is currently assigned.</p>"""
    owner_account: "capo_interconnect.types.owner_account_id.OwnerAccountId"
    """<p>The account that owns this <a>Connection</a> </p>"""
    activation_key: "capo_interconnect.types.activation_key.ActivationKey"
    """<p>The Activation Key associated to this connection.</p>"""
    tags: NotRequired["capo_interconnect.types.tag_map.TagMap"]
    """<p>The tags on the <a>Connection</a> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Connection) -> dict:
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
    out["ownerAccount"] = value["owner_account"]
    out["activationKey"] = value["activation_key"]
    if "tags" in value:
        import capo_interconnect.types.tag_map

        out["tags"] = capo_interconnect.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Connection.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Connection.arn required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("Connection.description required")
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError("Connection.bandwidth required")
    if data.get("attachPoint") is not None:
        import capo_interconnect.types.attach_point

        out["attach_point"] = (
            capo_interconnect.types.attach_point.deserialize_aws_json_1_0(
                data["attachPoint"]
            )
        )
    else:
        raise DeserializationError("Connection.attach_point required")
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("Connection.environment_id required")
    if data.get("provider") is not None:
        import capo_interconnect.types.provider

        out["provider"] = capo_interconnect.types.provider.deserialize_aws_json_1_0(
            data["provider"]
        )
    else:
        raise DeserializationError("Connection.provider required")
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        raise DeserializationError("Connection.location required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Connection.type required")
    if data.get("state") is not None:
        import capo_interconnect.types.connection_state

        out["state"] = (
            capo_interconnect.types.connection_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    else:
        raise DeserializationError("Connection.state required")
    if data.get("sharedId") is not None:
        out["shared_id"] = data["sharedId"]
    else:
        raise DeserializationError("Connection.shared_id required")
    if data.get("billingTier") is not None:
        out["billing_tier"] = data["billingTier"]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    else:
        raise DeserializationError("Connection.owner_account required")
    if data.get("activationKey") is not None:
        out["activation_key"] = data["activationKey"]
    else:
        raise DeserializationError("Connection.activation_key required")
    if data.get("tags") is not None:
        import capo_interconnect.types.tag_map

        out["tags"] = capo_interconnect.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
