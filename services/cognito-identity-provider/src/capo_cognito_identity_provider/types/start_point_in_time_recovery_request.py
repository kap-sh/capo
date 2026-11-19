"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StartPointInTimeRecoveryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.restore_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class StartPointInTimeRecoveryRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the recovery that you want to start.</p>"""
    restore_id: "capo_cognito_identity_provider.types.restore_id_type.RestoreIdType"
    """<p>The ID of the recovery that you want to start. Amazon Cognito returns this ID in the response to an <code>InitiatePointInTimeRecovery</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartPointInTimeRecoveryRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["RestoreId"] = value["restore_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartPointInTimeRecoveryRequest:
    out: StartPointInTimeRecoveryRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("RestoreId") is not None:
        out["restore_id"] = data["RestoreId"]
    else:
        out["restore_id"] = ""
    return out
