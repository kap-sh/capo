"""Generated from Smithy shape ``com.amazonaws.athena#UpdateNamedQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.name_string
    import capo_athena.types.named_query_description_string
    import capo_athena.types.named_query_id
    import capo_athena.types.query_string


class UpdateNamedQueryInput(TypedDict, closed=True):
    named_query_id: "capo_athena.types.named_query_id.NamedQueryId"
    """<p>The unique identifier (UUID) of the query.</p>"""
    name: "capo_athena.types.name_string.NameString"
    """<p>The name of the query.</p>"""
    description: NotRequired[
        "capo_athena.types.named_query_description_string.NamedQueryDescriptionString"
    ]
    """<p>The query description.</p>"""
    query_string: "capo_athena.types.query_string.QueryString"
    """<p>The contents of the query with all query statements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNamedQueryInput) -> dict:
    out: dict = {}
    out["NamedQueryId"] = value["named_query_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["QueryString"] = value["query_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNamedQueryInput:
    out: UpdateNamedQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("NamedQueryId") is not None:
        out["named_query_id"] = data["NamedQueryId"]
    else:
        out["named_query_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        out["query_string"] = ""
    return out
