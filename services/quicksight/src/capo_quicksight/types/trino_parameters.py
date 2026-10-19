"""Generated from Smithy shape ``com.amazonaws.quicksight#TrinoParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.catalog
    import capo_quicksight.types.host
    import capo_quicksight.types.port


class TrinoParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>The host name of the Trino data source.</p>"""
    port: "capo_quicksight.types.port.Port"
    """<p>The port for the Trino data source.</p>"""
    catalog: "capo_quicksight.types.catalog.Catalog"
    """<p>The catalog name for the Trino data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrinoParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["Catalog"] = value["catalog"]
    return out


def deserialize_json(data: dict) -> TrinoParameters:
    out: TrinoParameters = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        out["host"] = ""
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    return out
