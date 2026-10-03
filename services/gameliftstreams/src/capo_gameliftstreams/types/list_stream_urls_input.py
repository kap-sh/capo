"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListStreamUrlsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.max_results
    import capo_gameliftstreams.types.next_token
    import capo_gameliftstreams.types.stream_url_status


class ListStreamUrlsInput(TypedDict, closed=True):
    status: NotRequired["capo_gameliftstreams.types.stream_url_status.StreamUrlStatus"]
    """<p>Filters the list to stream URLs with the specified status.</p> <ul> <li> <p> <code>ACTIVE</code>: The stream URL is valid and can start stream sessions.</p> </li> <li> <p> <code>EXPIRED</code>: The stream URL has passed its expiration time and can no longer start stream sessions.</p> </li> <li> <p> <code>REVOKED</code>: The stream URL was revoked and can no longer start stream sessions.</p> </li> <li> <p> <code>LIMIT_REACHED</code>: The stream URL has been used the maximum number of times and can no longer start stream sessions.</p> </li> </ul>"""
    stream_group_identifier: NotRequired[
        "capo_gameliftstreams.types.identifier.Identifier"
    ]
    """<p>Filters the list to stream URLs that belong to the specified stream group.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    next_token: NotRequired["capo_gameliftstreams.types.next_token.NextToken"]
    """<p>The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>"""
    max_results: NotRequired["capo_gameliftstreams.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page. Valid values are 1-100. The default is 25.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamUrlsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStreamUrlsInput:
    out: ListStreamUrlsInput = {}  # type: ignore[typeddict-item]
    return out
