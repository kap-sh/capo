"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ReplicationStatusType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_replication_state


class ReplicationStatusType(TypedDict, closed=True):
    status: "capo_payment_cryptography.types.key_replication_state.KeyReplicationState"
    """<p>The current status of key replication in this Amazon Web Services Region.</p> <p>This field indicates whether the key replication is in progress, completed successfully, or has encountered an error. Possible values include states such as <code>SYNCRHONIZED</code>, <code>IN_PROGRESS</code>, <code>DELETE_IN_PROGRESS</code>, or <code>FAILED</code>. This provides visibility into the replication process for monitoring and troubleshooting purposes.</p>"""
    status_message: NotRequired["str"]
    """<p>A message that provides additional information about the current replication status of the key.</p> <p>This field contains details about any issues or progress updates related to key replication operations. It may include information about replication failures, synchronization status, or other operational details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicationStatusType) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicationStatusType:
    out: ReplicationStatusType = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
