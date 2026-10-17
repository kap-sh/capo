"""Generated from Smithy shape ``com.amazonaws.lakeformation#RLSPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.column_list
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.predicate_string


class RLSPolicy(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog that contains the policy. By default, the account ID.</p>"""
    name: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>The name of the row-level security policy.</p>"""
    attachment_columns: NotRequired["capo_lakeformation.types.column_list.ColumnList"]
    """<p>The list of columns that the filter expression references.</p>"""
    filter_expression: NotRequired[
        "capo_lakeformation.types.predicate_string.PredicateString"
    ]
    """<p>The filter predicate, written in a SQL-like syntax, that determines which rows are returned to the principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RLSPolicy) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "attachment_columns" in value:
        import capo_lakeformation.types.column_list

        out["AttachmentColumns"] = capo_lakeformation.types.column_list.serialize_json(
            value["attachment_columns"]
        )
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
    return out


def deserialize_json(data: dict) -> RLSPolicy:
    out: RLSPolicy = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AttachmentColumns") is not None:
        import capo_lakeformation.types.column_list

        out["attachment_columns"] = (
            capo_lakeformation.types.column_list.deserialize_json(
                data["AttachmentColumns"]
            )
        )
    if data.get("FilterExpression") is not None:
        out["filter_expression"] = data["FilterExpression"]
    return out
