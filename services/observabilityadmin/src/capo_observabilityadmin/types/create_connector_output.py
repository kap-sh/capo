"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateConnectorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector


class CreateConnectorOutput(TypedDict, closed=True):
    connector: "capo_observabilityadmin.types.connector.Connector"
    """<p>The connector that this request created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorOutput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.connector

    out["Connector"] = capo_observabilityadmin.types.connector.serialize_json(
        value["connector"]
    )
    return out


def deserialize_json(data: dict) -> CreateConnectorOutput:
    out: CreateConnectorOutput = {}  # type: ignore[typeddict-item]
    if data.get("Connector") is not None:
        import capo_observabilityadmin.types.connector

        out["connector"] = capo_observabilityadmin.types.connector.deserialize_json(
            data["Connector"]
        )
    else:
        raise DeserializationError("CreateConnectorOutput.connector required")
    return out
