"""Generated from Smithy shape ``com.amazonaws.datazone#RelationalFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.filter_expressions


class RelationalFilterConfiguration(TypedDict, closed=True):
    database_name: "str"
    """<p>The database name specified in the relational filter configuration for the data source.</p>"""
    schema_name: NotRequired["str"]
    """<p>The schema name specified in the relational filter configuration for the data source.</p>"""
    filter_expressions: NotRequired[
        "capo_datazone.types.filter_expressions.FilterExpressions"
    ]
    """<p>The filter expressions specified in the relational filter configuration for the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelationalFilterConfiguration) -> dict:
    out: dict = {}
    out["databaseName"] = value["database_name"]
    if "schema_name" in value:
        out["schemaName"] = value["schema_name"]
    if "filter_expressions" in value:
        import capo_datazone.types.filter_expressions

        out["filterExpressions"] = (
            capo_datazone.types.filter_expressions.serialize_json(
                value["filter_expressions"]
            )
        )
    return out


def deserialize_json(data: dict) -> RelationalFilterConfiguration:
    out: RelationalFilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        out["database_name"] = ""
    if data.get("schemaName") is not None:
        out["schema_name"] = data["schemaName"]
    if data.get("filterExpressions") is not None:
        import capo_datazone.types.filter_expressions

        out["filter_expressions"] = (
            capo_datazone.types.filter_expressions.deserialize_json(
                data["filterExpressions"]
            )
        )
    return out
