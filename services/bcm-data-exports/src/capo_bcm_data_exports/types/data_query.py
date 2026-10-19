"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#DataQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.query_statement
    import capo_bcm_data_exports.types.table_configurations


class DataQuery(TypedDict, closed=True):
    query_statement: "capo_bcm_data_exports.types.query_statement.QueryStatement"
    """<p>The query statement.</p>"""
    table_configurations: NotRequired[
        "capo_bcm_data_exports.types.table_configurations.TableConfigurations"
    ]
    """<p>The table configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQuery) -> dict:
    out: dict = {}
    out["QueryStatement"] = value["query_statement"]
    if "table_configurations" in value:
        import capo_bcm_data_exports.types.table_configurations

        out["TableConfigurations"] = (
            capo_bcm_data_exports.types.table_configurations.serialize_aws_json_1_1(
                value["table_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQuery:
    out: DataQuery = {}  # type: ignore[typeddict-item]
    if data.get("QueryStatement") is not None:
        out["query_statement"] = data["QueryStatement"]
    else:
        out["query_statement"] = ""
    if data.get("TableConfigurations") is not None:
        import capo_bcm_data_exports.types.table_configurations

        out["table_configurations"] = (
            capo_bcm_data_exports.types.table_configurations.deserialize_aws_json_1_1(
                data["TableConfigurations"]
            )
        )
    return out
