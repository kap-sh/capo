"""Generated from Smithy shape ``com.amazonaws.identitystore#UpdateIdentityStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.network_configuration


class UpdateIdentityStoreRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>"""
    network_configuration: NotRequired[
        "capo_identitystore.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration to apply to the identity store. This controls whether access through a virtual private cloud (VPC) endpoint is required and the source VPCs and IP addresses that are allowed to access the identity store.</p> <p>When you provide <code>NetworkConfiguration</code> in a request, the service performs a full replacement of the identity store's current network configuration with the values you specify. Any values that you omit are cleared. To preserve or change the allowed source VPCs or IP address ranges, include the complete set of values that you want in the request. To clear a list, omit it; an empty list is not accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIdentityStoreRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    if "network_configuration" in value:
        import capo_identitystore.types.network_configuration

        out["NetworkConfiguration"] = (
            capo_identitystore.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIdentityStoreRequest:
    out: UpdateIdentityStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "UpdateIdentityStoreRequest.identity_store_id required"
        )
    if data.get("NetworkConfiguration") is not None:
        import capo_identitystore.types.network_configuration

        out["network_configuration"] = (
            capo_identitystore.types.network_configuration.deserialize_aws_json_1_1(
                data["NetworkConfiguration"]
            )
        )
    return out
