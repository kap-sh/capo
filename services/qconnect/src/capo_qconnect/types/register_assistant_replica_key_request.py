"""Generated from Smithy shape ``com.amazonaws.qconnect#RegisterAssistantReplicaKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.client_token
    import capo_qconnect.types.replica_kms_key
    import capo_qconnect.types.uuid_or_arn


class RegisterAssistantReplicaKeyRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    replica_kms_key: "capo_qconnect.types.replica_kms_key.ReplicaKmsKey"
    """<p>The replica Region KMS key to register for the assistant.</p>"""
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAssistantReplicaKeyRequest) -> dict:
    out: dict = {}
    import capo_qconnect.types.replica_kms_key

    out["replicaKmsKey"] = capo_qconnect.types.replica_kms_key.serialize_json(
        value["replica_kms_key"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RegisterAssistantReplicaKeyRequest:
    out: RegisterAssistantReplicaKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("replicaKmsKey") is not None:
        import capo_qconnect.types.replica_kms_key

        out["replica_kms_key"] = capo_qconnect.types.replica_kms_key.deserialize_json(
            data["replicaKmsKey"]
        )
    else:
        raise DeserializationError(
            "RegisterAssistantReplicaKeyRequest.replica_kms_key required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
