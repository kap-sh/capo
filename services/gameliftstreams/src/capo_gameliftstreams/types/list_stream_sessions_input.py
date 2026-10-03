"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListStreamSessionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.export_files_status
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.max_results
    import capo_gameliftstreams.types.next_token
    import capo_gameliftstreams.types.stream_session_status


class ListStreamSessionsInput(TypedDict, closed=True):
    status: NotRequired[
        "capo_gameliftstreams.types.stream_session_status.StreamSessionStatus"
    ]
    """<p>Filter by the stream session status. You can specify one status in each request to retrieve only sessions that are currently in that status.</p>"""
    export_files_status: NotRequired[
        "capo_gameliftstreams.types.export_files_status.ExportFilesStatus"
    ]
    """<p>Filter by the exported files status. You can specify one status in each request to retrieve only sessions that currently have that exported files status.</p> <p> Exported files can be in one of the following states: </p> <ul> <li> <p> <code>SUCCEEDED</code>: The exported files are successfully stored in an S3 bucket.</p> </li> <li> <p> <code>FAILED</code>: The session ended but Amazon GameLift Streams couldn't collect and upload the files to S3.</p> </li> <li> <p> <code>PENDING</code>: Either the stream session is still in progress, or uploading the exported files to the S3 bucket is in progress.</p> </li> </ul>"""
    next_token: NotRequired["capo_gameliftstreams.types.next_token.NextToken"]
    """<p>The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>"""
    max_results: NotRequired["capo_gameliftstreams.types.max_results.MaxResults"]
    """<p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>. </p>"""
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>The unique identifier of a Amazon GameLift Streams stream group to retrieve the stream session for. You can use either the stream group ID or the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamSessionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStreamSessionsInput:
    out: ListStreamSessionsInput = {}  # type: ignore[typeddict-item]
    return out
