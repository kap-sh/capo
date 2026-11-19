"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DeleteConnectorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_identifier


class DeleteConnectorInput(TypedDict, closed=True):
    connector_identifier: (
        "capo_observabilityadmin.types.connector_identifier.ConnectorIdentifier"
    )
    """<p>The connector to delete. Specify one of the following:</p> <ul> <li> <p>The Amazon Resource Name (ARN) of the connector</p> </li> <li> <p>The ID of the connector</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorInput) -> dict:
    out: dict = {}
    out["ConnectorIdentifier"] = value["connector_identifier"]
    return out


def deserialize_json(data: dict) -> DeleteConnectorInput:
    out: DeleteConnectorInput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorIdentifier") is not None:
        out["connector_identifier"] = data["ConnectorIdentifier"]
    else:
        out["connector_identifier"] = ""
    return out
