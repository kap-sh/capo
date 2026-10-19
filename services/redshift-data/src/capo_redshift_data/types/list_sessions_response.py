"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ListSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_data.types.session_list
    import capo_redshift_data.types.string


class ListSessionsResponse(TypedDict, closed=True):
    sessions: "capo_redshift_data.types.session_list.SessionList"
    """<p>The sessions that match the request.</p>"""
    next_token: NotRequired["capo_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSessionsResponse) -> dict:
    out: dict = {}
    import capo_redshift_data.types.session_list

    out["Sessions"] = capo_redshift_data.types.session_list.serialize_aws_json_1_1(
        value["sessions"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSessionsResponse:
    out: ListSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Sessions") is not None:
        import capo_redshift_data.types.session_list

        out["sessions"] = (
            capo_redshift_data.types.session_list.deserialize_aws_json_1_1(
                data["Sessions"]
            )
        )
    else:
        out["sessions"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
