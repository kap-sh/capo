"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RestorationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.restore_id_type
    import capo_cognito_identity_provider.types.restore_preview_list_type
    import capo_cognito_identity_provider.types.restore_status_type


class RestorationType(TypedDict, closed=True):
    restore_id: NotRequired[
        "capo_cognito_identity_provider.types.restore_id_type.RestoreIdType"
    ]
    """<p>The ID of the recovery. Use this ID in requests to describe, start, or cancel the recovery.</p>"""
    restore_status: NotRequired[
        "capo_cognito_identity_provider.types.restore_status_type.RestoreStatusType"
    ]
    """<p>The status of the recovery. Can be one of the following values.</p> <dl> <dt>PREVIEW_GENERATING</dt> <dd> <p>Amazon Cognito is waiting for available capacity in the Amazon Web Services Region or is generating the recovery preview. Write operations in the user pool are paused.</p> </dd> <dt>PREVIEW_GENERATED</dt> <dd> <p>The recovery preview is ready for review. Write operations in the user pool are paused. Within 24 hours after you initiate the recovery, apply it with a <code>StartPointInTimeRecovery</code> request or discard it with a <code>CancelPointInTimeRecovery</code> request.</p> </dd> <dt>PREVIEW_CANCELLED</dt> <dd> <p>You canceled the recovery. Amazon Cognito resumed write operations and didn't change your user pool data.</p> </dd> <dt>PREVIEW_GENERATION_FAILED</dt> <dd> <p>Amazon Cognito couldn't generate the recovery preview. Amazon Cognito resumed write operations and didn't change your user pool data. You can initiate a new recovery.</p> </dd> <dt>PREVIEW_EXPIRED</dt> <dd> <p>You didn't start or cancel the recovery within 24 hours after you initiated it. Amazon Cognito resumed write operations and didn't change your user pool data.</p> </dd> <dt>RESTORING</dt> <dd> <p>Amazon Cognito is restoring user data in the user pool to its state at the recovery point. Write operations in the user pool are paused.</p> </dd> <dt>RESTORE_COMPLETED</dt> <dd> <p>Amazon Cognito restored your user pool to its state at the recovery point and resumed write operations.</p> </dd> <dt>TEMPORARY_INTERNAL_ERROR_SEE_SUPPORT_CASE</dt> <dd> <p>The recovery encountered an internal error. Write operations in the user pool remain paused. Amazon Web Services Support contacts you through a support case to resolve the issue.</p> </dd> <dt>AWS_ABORTED</dt> <dd> <p>Amazon Cognito stopped the recovery because of an internal failure. Write operations in the user pool remain paused, and you can't cancel or retry the recovery. Amazon Web Services Support contacts you through a support case to resolve the issue.</p> </dd> </dl>"""
    restore_timestamp: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The point in time that the recovery restores the user pool to.</p>"""
    trigger_timestamp: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The end of the period of changes that the recovery reverts. This time is shortly after the time that you initiated the recovery. The recovery reverts changes to user data that occurred between <code>RestoreTimestamp</code> and <code>TriggerTimestamp</code>.</p>"""
    restore_preview: NotRequired[
        "capo_cognito_identity_provider.types.restore_preview_list_type.RestorePreviewListType"
    ]
    """<p>The recovery preview. For each type of entity, the preview shows the number of entities that the recovery creates, updates, and deletes. The preview doesn't include user data. Amazon Cognito returns the preview when it's available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestorationType) -> dict:
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
    if "trigger_timestamp" in value:
        import capo_cognito_identity_provider.types.date_type

        out["TriggerTimestamp"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["trigger_timestamp"]
            )
        )
    if "restore_preview" in value:
        import capo_cognito_identity_provider.types.restore_preview_list_type

        out["RestorePreview"] = (
            capo_cognito_identity_provider.types.restore_preview_list_type.serialize_aws_json_1_1(
                value["restore_preview"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestorationType:
    out: RestorationType = {}  # type: ignore[typeddict-item]
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
    if data.get("TriggerTimestamp") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["trigger_timestamp"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["TriggerTimestamp"]
            )
        )
    if data.get("RestorePreview") is not None:
        import capo_cognito_identity_provider.types.restore_preview_list_type

        out["restore_preview"] = (
            capo_cognito_identity_provider.types.restore_preview_list_type.deserialize_aws_json_1_1(
                data["RestorePreview"]
            )
        )
    return out
