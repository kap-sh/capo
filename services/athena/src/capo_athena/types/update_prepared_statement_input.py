"""Generated from Smithy shape ``com.amazonaws.athena#UpdatePreparedStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.description_string
    import capo_athena.types.query_string
    import capo_athena.types.statement_name
    import capo_athena.types.work_group_name


class UpdatePreparedStatementInput(TypedDict, closed=True):
    statement_name: "capo_athena.types.statement_name.StatementName"
    """<p>The name of the prepared statement.</p>"""
    work_group: "capo_athena.types.work_group_name.WorkGroupName"
    """<p>The workgroup for the prepared statement.</p>"""
    query_statement: "capo_athena.types.query_string.QueryString"
    """<p>The query string for the prepared statement.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>The description of the prepared statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePreparedStatementInput) -> dict:
    out: dict = {}
    out["StatementName"] = value["statement_name"]
    out["WorkGroup"] = value["work_group"]
    out["QueryStatement"] = value["query_statement"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePreparedStatementInput:
    out: UpdatePreparedStatementInput = {}  # type: ignore[typeddict-item]
    if data.get("StatementName") is not None:
        out["statement_name"] = data["StatementName"]
    else:
        out["statement_name"] = ""
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    else:
        out["work_group"] = ""
    if data.get("QueryStatement") is not None:
        out["query_statement"] = data["QueryStatement"]
    else:
        out["query_statement"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
