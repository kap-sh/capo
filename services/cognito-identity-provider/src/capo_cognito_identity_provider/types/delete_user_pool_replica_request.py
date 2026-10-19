"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteUserPoolReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.region_name_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DeleteUserPoolReplicaRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the replica to delete.</p>"""
    region_name: "capo_cognito_identity_provider.types.region_name_type.RegionNameType"
    """<p>The Amazon Web Services Region of the replica to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserPoolReplicaRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserPoolReplicaRequest:
    out: DeleteUserPoolReplicaRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    else:
        out["region_name"] = ""
    return out
