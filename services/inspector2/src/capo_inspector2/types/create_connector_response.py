"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_arn


class CreateConnectorResponse(TypedDict, closed=True):
    connector_arn: "capo_inspector2.types.connector_arn.ConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the created connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorResponse) -> dict:
    out: dict = {}
    out["connectorArn"] = value["connector_arn"]
    return out


def deserialize_json(data: dict) -> CreateConnectorResponse:
    out: CreateConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
    else:
        out["connector_arn"] = ""
    return out
