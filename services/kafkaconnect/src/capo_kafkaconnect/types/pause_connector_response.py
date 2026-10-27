"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#PauseConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string


class PauseConnectorResponse(TypedDict, closed=True):
    connector_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    connector_operation_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector operation created to perform the pause.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PauseConnectorResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    if "connector_operation_arn" in value:
        out["connectorOperationArn"] = value["connector_operation_arn"]
    return out


def deserialize_json(data: dict) -> PauseConnectorResponse:
    out: PauseConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
    if data.get("connectorOperationArn") is not None:
        out["connector_operation_arn"] = data["connectorOperationArn"]
    return out
