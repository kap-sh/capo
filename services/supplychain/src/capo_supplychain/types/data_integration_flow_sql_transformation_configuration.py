"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowSQLTransformationConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_sql_query


class DataIntegrationFlowSQLTransformationConfiguration(TypedDict, closed=True):
    query: "capo_supplychain.types.data_integration_flow_sql_query.DataIntegrationFlowSQLQuery"
    """<p>The transformation SQL query body based on SparkSQL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowSQLTransformationConfiguration) -> dict:
    out: dict = {}
    out["query"] = value["query"]
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowSQLTransformationConfiguration:
    out: DataIntegrationFlowSQLTransformationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("query") is not None:
        out["query"] = data["query"]
    else:
        out["query"] = ""
    return out


def redact_sensitive(
    value: DataIntegrationFlowSQLTransformationConfiguration,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query" in value:
        out["query"] = "*** Sensitive Data Redacted ***"
    return out
