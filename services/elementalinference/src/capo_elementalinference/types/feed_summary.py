"""Generated from Smithy shape ``com.amazonaws.elementalinference#FeedSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_arn
    import capo_elementalinference.types.feed_association
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.feed_status
    import capo_elementalinference.types.resource_name


class FeedSummary(TypedDict, closed=True):
    arn: "capo_elementalinference.types.feed_arn.FeedArn"
    """<p>The ARN of the feed.</p>"""
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed.</p>"""
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the feed</p>"""
    association: NotRequired[
        "capo_elementalinference.types.feed_association.FeedAssociation"
    ]
    """<p>The resource, if any, associated with the feed.</p>"""
    status: "capo_elementalinference.types.feed_status.FeedStatus"
    """<p>The status of the feed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FeedSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "association" in value:
        import capo_elementalinference.types.feed_association

        out["association"] = (
            capo_elementalinference.types.feed_association.serialize_json(
                value["association"]
            )
        )
    import capo_elementalinference.types.feed_status

    out["status"] = capo_elementalinference.types.feed_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> FeedSummary:
    out: FeedSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("association") is not None:
        import capo_elementalinference.types.feed_association

        out["association"] = (
            capo_elementalinference.types.feed_association.deserialize_json(
                data["association"]
            )
        )
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
