"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetPreparedStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.prepared_statement_name_list
    import capo_athena.types.work_group_name


class BatchGetPreparedStatementInput(TypedDict, closed=True):
    prepared_statement_names: (
        "capo_athena.types.prepared_statement_name_list.PreparedStatementNameList"
    )
    """<p>A list of prepared statement names to return.</p>"""
    work_group: "capo_athena.types.work_group_name.WorkGroupName"
    """<p>The name of the workgroup to which the prepared statements belong.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetPreparedStatementInput) -> dict:
    out: dict = {}
    import capo_athena.types.prepared_statement_name_list

    out["PreparedStatementNames"] = (
        capo_athena.types.prepared_statement_name_list.serialize_aws_json_1_1(
            value["prepared_statement_names"]
        )
    )
    out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetPreparedStatementInput:
    out: BatchGetPreparedStatementInput = {}  # type: ignore[typeddict-item]
    if data.get("PreparedStatementNames") is not None:
        import capo_athena.types.prepared_statement_name_list

        out["prepared_statement_names"] = (
            capo_athena.types.prepared_statement_name_list.deserialize_aws_json_1_1(
                data["PreparedStatementNames"]
            )
        )
    else:
        out["prepared_statement_names"] = []
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    else:
        out["work_group"] = ""
    return out
