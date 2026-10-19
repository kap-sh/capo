"""Generated from Smithy shape ``com.amazonaws.athena#NamedQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.database_string
    import capo_athena.types.description_string
    import capo_athena.types.name_string
    import capo_athena.types.named_query_id
    import capo_athena.types.query_string
    import capo_athena.types.work_group_name


class NamedQuery(TypedDict, closed=True):
    name: "capo_athena.types.name_string.NameString"
    """<p>The query name.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>The query description.</p>"""
    database: "capo_athena.types.database_string.DatabaseString"
    """<p>The database to which the query belongs.</p>"""
    query_string: "capo_athena.types.query_string.QueryString"
    """<p>The SQL statements that make up the query.</p>"""
    named_query_id: NotRequired["capo_athena.types.named_query_id.NamedQueryId"]
    """<p>The unique identifier of the query.</p>"""
    work_group: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup that contains the named query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamedQuery) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Database"] = value["database"]
    out["QueryString"] = value["query_string"]
    if "named_query_id" in value:
        out["NamedQueryId"] = value["named_query_id"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NamedQuery:
    out: NamedQuery = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        out["query_string"] = ""
    if data.get("NamedQueryId") is not None:
        out["named_query_id"] = data["NamedQueryId"]
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    return out
