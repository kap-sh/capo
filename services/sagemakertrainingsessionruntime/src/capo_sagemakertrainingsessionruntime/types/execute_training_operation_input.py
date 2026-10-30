"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#ExecuteTrainingOperationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.client_token
    import capo_sagemakertrainingsessionruntime.types.operation_config
    import capo_sagemakertrainingsessionruntime.types.sequence_number
    import capo_sagemakertrainingsessionruntime.types.training_session_name


class ExecuteTrainingOperationInput(TypedDict, closed=True):
    training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName"
    """<p>The name of the training session to submit the operation to.</p>"""
    sequence_number: (
        "capo_sagemakertrainingsessionruntime.types.sequence_number.SequenceNumber"
    )
    """<p>The monotonically increasing sequence number that determines execution order. The training session processes operations strictly in sequence number order. If a gap exists, the session blocks until the missing operation arrives or times out. Must be at least 1.</p>"""
    client_token: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service ignores the request but does not return an error.</p>"""
    operation_config: (
        "capo_sagemakertrainingsessionruntime.types.operation_config.OperationConfig"
    )
    """<p>The configuration that specifies the type and parameters of the training operation. Exactly one member of the union must be set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteTrainingOperationInput) -> dict:
    out: dict = {}
    out["sequenceNumber"] = value["sequence_number"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_sagemakertrainingsessionruntime.types.operation_config

    out["operationConfig"] = (
        capo_sagemakertrainingsessionruntime.types.operation_config.serialize_json(
            value["operation_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExecuteTrainingOperationInput:
    out: ExecuteTrainingOperationInput = {}  # type: ignore[typeddict-item]
    if data.get("sequenceNumber") is not None:
        out["sequence_number"] = data["sequenceNumber"]
    else:
        out["sequence_number"] = 0
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("operationConfig") is not None:
        import capo_sagemakertrainingsessionruntime.types.operation_config

        out["operation_config"] = (
            capo_sagemakertrainingsessionruntime.types.operation_config.deserialize_json(
                data["operationConfig"]
            )
        )
    else:
        out["operation_config"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: ExecuteTrainingOperationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "operation_config" in value:
        import capo_sagemakertrainingsessionruntime.types.operation_config

        out["operation_config"] = (
            capo_sagemakertrainingsessionruntime.types.operation_config.redact_sensitive(
                value["operation_config"]
            )
        )
    return out
