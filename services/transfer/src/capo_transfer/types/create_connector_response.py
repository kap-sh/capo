"""Generated from Smithy shape ``com.amazonaws.transfer#CreateConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.connector_id


class CreateConnectorResponse(TypedDict, closed=True):
    connector_id: "capo_transfer.types.connector_id.ConnectorId"
    """<p>The unique identifier for the connector, returned after the API call succeeds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectorResponse) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectorResponse:
    out: CreateConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    else:
        out["connector_id"] = ""
    return out
