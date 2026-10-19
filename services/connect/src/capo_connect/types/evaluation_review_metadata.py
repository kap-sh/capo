"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_review_request_comment_list
    import capo_connect.types.resource_id
    import capo_connect.types.timestamp


class EvaluationReviewMetadata(TypedDict, closed=True):
    review_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The unique identifier for the evaluation review.</p>"""
    requested_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the evaluation review was requested.</p>"""
    requested_by: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The user who requested the evaluation review.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the evaluation review was created.</p>"""
    created_by: "capo_connect.types.arn.ARN"
    """<p>The user who created the evaluation review.</p>"""
    review_request_comments: "capo_connect.types.evaluation_review_request_comment_list.EvaluationReviewRequestCommentList"
    """<p>Comments provided when requesting the evaluation review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewMetadata) -> dict:
    out: dict = {}
    if "review_id" in value:
        out["ReviewId"] = value["review_id"]
    if "requested_time" in value:
        import capo_connect.types.timestamp

        out["RequestedTime"] = capo_connect.types.timestamp.serialize_json(
            value["requested_time"]
        )
    if "requested_by" in value:
        out["RequestedBy"] = value["requested_by"]
    import datetime

    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value.get(
            "created_time", datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
        )
    )
    out["CreatedBy"] = value.get("created_by", "n/a")
    import capo_connect.types.evaluation_review_request_comment_list

    out["ReviewRequestComments"] = (
        capo_connect.types.evaluation_review_request_comment_list.serialize_json(
            value["review_request_comments"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationReviewMetadata:
    out: EvaluationReviewMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ReviewId") is not None:
        out["review_id"] = data["ReviewId"]
    if data.get("RequestedTime") is not None:
        import capo_connect.types.timestamp

        out["requested_time"] = capo_connect.types.timestamp.deserialize_json(
            data["RequestedTime"]
        )
    if data.get("RequestedBy") is not None:
        out["requested_by"] = data["RequestedBy"]
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    else:
        out["created_by"] = "n/a"
    if data.get("ReviewRequestComments") is not None:
        import capo_connect.types.evaluation_review_request_comment_list

        out["review_request_comments"] = (
            capo_connect.types.evaluation_review_request_comment_list.deserialize_json(
                data["ReviewRequestComments"]
            )
        )
    else:
        out["review_request_comments"] = []
    return out
