"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InitiatePointInTimeRecoveryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class InitiatePointInTimeRecoveryRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that you want to recover.</p>"""
    restore_timestamp: "capo_cognito_identity_provider.types.date_type.DateType"
    """<p>The point in time that you want to recover your user pool to. Amazon Cognito reverts changes to user data that occurred after this time. The recovery point must be at least 15 minutes in the past and within the recovery period of your user pool feature plan: up to 1 day in the past with the Essentials feature plan, or up to 14 days in the past with the Plus feature plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InitiatePointInTimeRecoveryRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    import capo_cognito_identity_provider.types.date_type

    out["RestoreTimestamp"] = (
        capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
            value["restore_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InitiatePointInTimeRecoveryRequest:
    out: InitiatePointInTimeRecoveryRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("RestoreTimestamp") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["restore_timestamp"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["RestoreTimestamp"]
            )
        )
    else:
        import datetime

        out["restore_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
