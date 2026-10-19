"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ListStatementsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_data.types.statement_list
    import capo_redshift_data.types.string


class ListStatementsResponse(TypedDict, closed=True):
    statements: "capo_redshift_data.types.statement_list.StatementList"
    """<p>The SQL statements. </p>"""
    next_token: NotRequired["capo_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStatementsResponse) -> dict:
    out: dict = {}
    import capo_redshift_data.types.statement_list

    out["Statements"] = capo_redshift_data.types.statement_list.serialize_aws_json_1_1(
        value["statements"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStatementsResponse:
    out: ListStatementsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Statements") is not None:
        import capo_redshift_data.types.statement_list

        out["statements"] = (
            capo_redshift_data.types.statement_list.deserialize_aws_json_1_1(
                data["Statements"]
            )
        )
    else:
        out["statements"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
