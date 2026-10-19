"""Generated from Smithy shape ``com.amazonaws.quicksight#ExasolParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.host
    import capo_quicksight.types.port


class ExasolParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>The hostname or IP address of the Exasol data source.</p>"""
    port: "capo_quicksight.types.port.Port"
    """<p>The port for the Exasol data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExasolParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    return out


def deserialize_json(data: dict) -> ExasolParameters:
    out: ExasolParameters = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        out["host"] = ""
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    return out
