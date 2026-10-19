"""Generated from Smithy shape ``com.amazonaws.dataexchange#RedshiftDataShareDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string


class RedshiftDataShareDetails(TypedDict, closed=True):
    arn: "capo_dataexchange.types.__string.__string"
    """<p>The ARN of the underlying Redshift data share that is being affected by this notification.</p>"""
    database: "capo_dataexchange.types.__string.__string"
    """<p>The database name in the Redshift data share that is being affected by this notification.</p>"""
    function: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>A function name in the Redshift database that is being affected by this notification.</p>"""
    table: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>A table name in the Redshift database that is being affected by this notification.</p>"""
    schema: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>A schema name in the Redshift database that is being affected by this notification.</p>"""
    view: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>A view name in the Redshift database that is being affected by this notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftDataShareDetails) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Database"] = value["database"]
    if "function" in value:
        out["Function"] = value["function"]
    if "table" in value:
        out["Table"] = value["table"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    if "view" in value:
        out["View"] = value["view"]
    return out


def deserialize_json(data: dict) -> RedshiftDataShareDetails:
    out: RedshiftDataShareDetails = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    if data.get("Function") is not None:
        out["function"] = data["Function"]
    if data.get("Table") is not None:
        out["table"] = data["Table"]
    if data.get("Schema") is not None:
        out["schema"] = data["Schema"]
    if data.get("View") is not None:
        out["view"] = data["View"]
    return out
