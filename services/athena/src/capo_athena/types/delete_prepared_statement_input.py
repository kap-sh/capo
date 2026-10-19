"""Generated from Smithy shape ``com.amazonaws.athena#DeletePreparedStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.statement_name
    import capo_athena.types.work_group_name


class DeletePreparedStatementInput(TypedDict, closed=True):
    statement_name: "capo_athena.types.statement_name.StatementName"
    """<p>The name of the prepared statement to delete.</p>"""
    work_group: "capo_athena.types.work_group_name.WorkGroupName"
    """<p>The workgroup to which the statement to be deleted belongs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePreparedStatementInput) -> dict:
    out: dict = {}
    out["StatementName"] = value["statement_name"]
    out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePreparedStatementInput:
    out: DeletePreparedStatementInput = {}  # type: ignore[typeddict-item]
    if data.get("StatementName") is not None:
        out["statement_name"] = data["StatementName"]
    else:
        out["statement_name"] = ""
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    else:
        out["work_group"] = ""
    return out
