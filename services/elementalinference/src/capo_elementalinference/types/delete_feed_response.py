"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteFeedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_arn
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.feed_status


class DeleteFeedResponse(TypedDict, closed=True):
    arn: "capo_elementalinference.types.feed_arn.FeedArn"
    """<p>The ARN of the deleted feed.</p>"""
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the deleted feed.</p>"""
    status: "capo_elementalinference.types.feed_status.FeedStatus"
    """<p>The current status of the feed. When deletion of the feed has succeeded, the status will be DELETED. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFeedResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_elementalinference.types.feed_status

    out["status"] = capo_elementalinference.types.feed_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteFeedResponse:
    out: DeleteFeedResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("status") is not None:
        import capo_elementalinference.types.feed_status

        out["status"] = capo_elementalinference.types.feed_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elementalinference.types.feed_status.FeedStatus", ""
        )
    return out
