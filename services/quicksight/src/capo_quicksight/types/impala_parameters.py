"""Generated from Smithy shape ``com.amazonaws.quicksight#ImpalaParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.database
    import capo_quicksight.types.host
    import capo_quicksight.types.port
    import capo_quicksight.types.sql_endpoint_path


class ImpalaParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>The host name of the Impala data source.</p>"""
    port: "capo_quicksight.types.port.Port"
    """<p>The port of the Impala data source.</p>"""
    database: NotRequired["capo_quicksight.types.database.Database"]
    """<p>The database of the Impala data source.</p>"""
    sql_endpoint_path: "capo_quicksight.types.sql_endpoint_path.SqlEndpointPath"
    """<p>The HTTP path of the Impala data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImpalaParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    if "database" in value:
        out["Database"] = value["database"]
    out["SqlEndpointPath"] = value["sql_endpoint_path"]
    return out


def deserialize_json(data: dict) -> ImpalaParameters:
    out: ImpalaParameters = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        out["host"] = ""
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    if data.get("SqlEndpointPath") is not None:
        out["sql_endpoint_path"] = data["SqlEndpointPath"]
    else:
        out["sql_endpoint_path"] = ""
    return out
