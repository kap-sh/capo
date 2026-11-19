"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RestorationDescriptionType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.restore_id_type
    import capo_cognito_identity_provider.types.restore_status_type


class RestorationDescriptionType(TypedDict, closed=True):
    restore_id: NotRequired[
        "capo_cognito_identity_provider.types.restore_id_type.RestoreIdType"
    ]
    """<p>The ID of the recovery.</p>"""
    restore_status: NotRequired[
        "capo_cognito_identity_provider.types.restore_status_type.RestoreStatusType"
    ]
    """<p>The status of the recovery. For a description of each status, see the <code>RestoreStatus</code> parameter of <code>RestorationType</code>.</p>"""
    restore_timestamp: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The point in time that the recovery restores the user pool to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestorationDescriptionType) -> dict:
    out: dict = {}
    if "restore_id" in value:
        out["RestoreId"] = value["restore_id"]
    if "restore_status" in value:
        import capo_cognito_identity_provider.types.restore_status_type

        out["RestoreStatus"] = (
            capo_cognito_identity_provider.types.restore_status_type.serialize_aws_json_1_1(
                value["restore_status"]
            )
        )
    if "restore_timestamp" in value:
        import capo_cognito_identity_provider.types.date_type

        out["RestoreTimestamp"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["restore_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestorationDescriptionType:
    out: RestorationDescriptionType = {}  # type: ignore[typeddict-item]
    if data.get("RestoreId") is not None:
        out["restore_id"] = data["RestoreId"]
    if data.get("RestoreStatus") is not None:
        import capo_cognito_identity_provider.types.restore_status_type

        out["restore_status"] = (
            capo_cognito_identity_provider.types.restore_status_type.deserialize_aws_json_1_1(
                data["RestoreStatus"]
            )
        )
    if data.get("RestoreTimestamp") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["restore_timestamp"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["RestoreTimestamp"]
            )
        )
    return out
