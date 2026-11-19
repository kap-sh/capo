"""Generated from Smithy shape ``com.amazonaws.secretsmanager#StopReplicationToReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_id_type


class StopReplicationToReplicaRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the replica secret.</p> <p>For a cross-region replica, the replica ARN is the same as the original primary secret ARN except that the Region is changed to the replica Region. For a cross-account replica, this is the ARN or name of the replica secret in your account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopReplicationToReplicaRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopReplicationToReplicaRequest:
    out: StopReplicationToReplicaRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        out["secret_id"] = ""
    return out
