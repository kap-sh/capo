"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_arn


class DeleteConnectorRequest(TypedDict, closed=True):
    connector_arn: "capo_inspector2.types.connector_arn.ConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the connector to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorRequest) -> dict:
    out: dict = {}
    out["connectorArn"] = value["connector_arn"]
    return out


def deserialize_json(data: dict) -> DeleteConnectorRequest:
    out: DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
    else:
        out["connector_arn"] = ""
    return out
