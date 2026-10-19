"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviews``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_review_action
    import capo_ssm.types.document_review_comment_list


class DocumentReviews(TypedDict, closed=True):
    action: "capo_ssm.types.document_review_action.DocumentReviewAction"
    """<p>The action to take on a document approval review request.</p>"""
    comment: NotRequired[
        "capo_ssm.types.document_review_comment_list.DocumentReviewCommentList"
    ]
    """<p>A comment entered by a user in your organization about the document review request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReviews) -> dict:
    out: dict = {}
    import capo_ssm.types.document_review_action

    out["Action"] = capo_ssm.types.document_review_action.serialize_aws_json_1_1(
        value["action"]
    )
    if "comment" in value:
        import capo_ssm.types.document_review_comment_list

        out["Comment"] = (
            capo_ssm.types.document_review_comment_list.serialize_aws_json_1_1(
                value["comment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentReviews:
    out: DocumentReviews = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_ssm.types.document_review_action

        out["action"] = capo_ssm.types.document_review_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_ssm.types.document_review_action.DocumentReviewAction", ""
        )
    if data.get("Comment") is not None:
        import capo_ssm.types.document_review_comment_list

        out["comment"] = (
            capo_ssm.types.document_review_comment_list.deserialize_aws_json_1_1(
                data["Comment"]
            )
        )
    return out
