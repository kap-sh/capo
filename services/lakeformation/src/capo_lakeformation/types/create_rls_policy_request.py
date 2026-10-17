"""Generated from Smithy shape ``com.amazonaws.lakeformation#CreateRLSPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.column_list
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.predicate_string


class CreateRLSPolicyRequest(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>A unique name for the row-level security policy within the Data Catalog.</p>"""
    attachment_columns: "capo_lakeformation.types.column_list.ColumnList"
    """<p>The list of columns that the filter expression references. These columns define the shape of the data that the policy can be attached to.</p>"""
    filter_expression: "capo_lakeformation.types.predicate_string.PredicateString"
    """<p>A filter predicate, written in a SQL-like syntax, that Lake Formation evaluates against each row. Only the rows for which the expression evaluates to true are returned to the principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRLSPolicyRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_lakeformation.types.column_list

    out["AttachmentColumns"] = capo_lakeformation.types.column_list.serialize_json(
        value["attachment_columns"]
    )
    out["FilterExpression"] = value["filter_expression"]
    return out


def deserialize_json(data: dict) -> CreateRLSPolicyRequest:
    out: CreateRLSPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRLSPolicyRequest.name required")
    if data.get("AttachmentColumns") is not None:
        import capo_lakeformation.types.column_list

        out["attachment_columns"] = (
            capo_lakeformation.types.column_list.deserialize_json(
                data["AttachmentColumns"]
            )
        )
    else:
        raise DeserializationError("CreateRLSPolicyRequest.attachment_columns required")
    if data.get("FilterExpression") is not None:
        out["filter_expression"] = data["FilterExpression"]
    else:
        raise DeserializationError("CreateRLSPolicyRequest.filter_expression required")
    return out
