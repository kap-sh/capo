"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DeleteSecretRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.boolean_type
    import capo_secrets_manager.types.recovery_window_in_days_type
    import capo_secrets_manager.types.secret_id_type


class DeleteSecretRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to delete.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    recovery_window_in_days: NotRequired[
        "capo_secrets_manager.types.recovery_window_in_days_type.RecoveryWindowInDaysType"
    ]
    """<p>The number of days from 7 to 30 that Secrets Manager waits before permanently deleting the secret. You can't use both this parameter and <code>ForceDeleteWithoutRecovery</code> in the same call. If you don't use either, then by default Secrets Manager uses a 30 day recovery window.</p>"""
    force_delete_without_recovery: NotRequired[
        "capo_secrets_manager.types.boolean_type.BooleanType"
    ]
    """<p>Specifies whether to delete the secret without any recovery window. You can't use both this parameter and <code>RecoveryWindowInDays</code> in the same call. If you don't use either, then by default Secrets Manager uses a 30 day recovery window.</p> <p>Secrets Manager performs the actual deletion with an asynchronous background process, so there might be a short delay before the secret is permanently deleted. If you delete a secret and then immediately create a secret with the same name, use appropriate back off and retry logic.</p> <p>If you forcibly delete an already deleted or nonexistent secret, the operation does not return <code>ResourceNotFoundException</code>.</p> <important> <p>Use this parameter with caution. This parameter causes the operation to skip the normal recovery window before the permanent deletion that Secrets Manager would normally impose with the <code>RecoveryWindowInDays</code> parameter. If you delete a secret with the <code>ForceDeleteWithoutRecovery</code> parameter, then you have no opportunity to recover the secret. You lose the secret permanently.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSecretRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    if "recovery_window_in_days" in value:
        out["RecoveryWindowInDays"] = value["recovery_window_in_days"]
    if "force_delete_without_recovery" in value:
        out["ForceDeleteWithoutRecovery"] = value["force_delete_without_recovery"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSecretRequest:
    out: DeleteSecretRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("DeleteSecretRequest.secret_id required")
    if data.get("RecoveryWindowInDays") is not None:
        out["recovery_window_in_days"] = data["RecoveryWindowInDays"]
    if data.get("ForceDeleteWithoutRecovery") is not None:
        out["force_delete_without_recovery"] = data["ForceDeleteWithoutRecovery"]
    return out
