"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetConnectorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector


class GetConnectorOutput(TypedDict, closed=True):
    connector: "capo_observabilityadmin.types.connector.Connector"
    """<p>The connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorOutput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.connector

    out["Connector"] = capo_observabilityadmin.types.connector.serialize_json(
        value["connector"]
    )
    return out


def deserialize_json(data: dict) -> GetConnectorOutput:
    out: GetConnectorOutput = {}  # type: ignore[typeddict-item]
    if data.get("Connector") is not None:
        import capo_observabilityadmin.types.connector

        out["connector"] = capo_observabilityadmin.types.connector.deserialize_json(
            data["Connector"]
        )
    else:
        raise DeserializationError("GetConnectorOutput.connector required")
    return out
