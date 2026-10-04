"""Generated from Smithy shape ``com.amazonaws.identitystore#DescribeIdentityStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_arn
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.network_configuration_details


class DescribeIdentityStoreResponse(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    identity_store_arn: "capo_identitystore.types.identity_store_arn.IdentityStoreArn"
    """<p>The Amazon Resource Name (ARN) of the identity store. For example, <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>"""
    network_configuration: NotRequired[
        "capo_identitystore.types.network_configuration_details.NetworkConfigurationDetails"
    ]
    """<p>The network configuration of the identity store. This configuration controls whether access through a virtual private cloud (VPC) endpoint is required, and which source VPCs and IP addresses are allowed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIdentityStoreResponse) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["IdentityStoreArn"] = value["identity_store_arn"]
    if "network_configuration" in value:
        import capo_identitystore.types.network_configuration_details

        out["NetworkConfiguration"] = (
            capo_identitystore.types.network_configuration_details.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIdentityStoreResponse:
    out: DescribeIdentityStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "DescribeIdentityStoreResponse.identity_store_id required"
        )
    if data.get("IdentityStoreArn") is not None:
        out["identity_store_arn"] = data["IdentityStoreArn"]
    else:
        raise DeserializationError(
            "DescribeIdentityStoreResponse.identity_store_arn required"
        )
    if data.get("NetworkConfiguration") is not None:
        import capo_identitystore.types.network_configuration_details

        out["network_configuration"] = (
            capo_identitystore.types.network_configuration_details.deserialize_aws_json_1_1(
                data["NetworkConfiguration"]
            )
        )
    return out
