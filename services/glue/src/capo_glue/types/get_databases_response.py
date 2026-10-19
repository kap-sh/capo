"""Generated from Smithy shape ``com.amazonaws.glue#GetDatabasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.database_list
    import capo_glue.types.token


class GetDatabasesResponse(TypedDict, closed=True):
    database_list: "capo_glue.types.database_list.DatabaseList"
    """<p>A list of <code>Database</code> objects from the specified catalog.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDatabasesResponse) -> dict:
    out: dict = {}
    import capo_glue.types.database_list

    out["DatabaseList"] = capo_glue.types.database_list.serialize_aws_json_1_1(
        value["database_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDatabasesResponse:
    out: GetDatabasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseList") is not None:
        import capo_glue.types.database_list

        out["database_list"] = capo_glue.types.database_list.deserialize_aws_json_1_1(
            data["DatabaseList"]
        )
    else:
        out["database_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
