"""Generated from Smithy shape ``com.amazonaws.secretsmanager#StopReplicationToReplicaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_arn_type


class StopReplicationToReplicaResponse(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the promoted secret. For a cross-region replica, this ARN is the same as the original primary secret's ARN except that the Region is changed. For a cross-account replica, this is the ARN of the promoted secret in your account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopReplicationToReplicaResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopReplicationToReplicaResponse:
    out: StopReplicationToReplicaResponse = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    return out
