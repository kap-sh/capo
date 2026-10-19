"""Generated from Smithy shape ``com.amazonaws.s3outposts#ListOutpostsWithS3Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3outposts.types.max_results
    import capo_s3outposts.types.next_token


class ListOutpostsWithS3Request(TypedDict, closed=True):
    next_token: NotRequired["capo_s3outposts.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListOutpostsWithS3</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional Outposts.</p>"""
    max_results: NotRequired["capo_s3outposts.types.max_results.MaxResults"]
    """<p>The maximum number of Outposts to return. The limit is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOutpostsWithS3Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOutpostsWithS3Request:
    out: ListOutpostsWithS3Request = {}  # type: ignore[typeddict-item]
    return out
