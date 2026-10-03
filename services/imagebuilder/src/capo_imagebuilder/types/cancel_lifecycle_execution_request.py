"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CancelLifecycleExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.lifecycle_execution_id


class CancelLifecycleExecutionRequest(TypedDict, closed=True):
    lifecycle_execution_id: (
        "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    )
    """<p>Identifies the specific runtime instance of the image lifecycle to cancel.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelLifecycleExecutionRequest) -> dict:
    out: dict = {}
    out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CancelLifecycleExecutionRequest:
    out: CancelLifecycleExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("lifecycleExecutionId") is not None:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
    else:
        raise DeserializationError(
            "CancelLifecycleExecutionRequest.lifecycle_execution_id required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CancelLifecycleExecutionRequest.client_token required"
        )
    return out
