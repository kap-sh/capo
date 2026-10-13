"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetCodeReviewsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.code_review_id_list
    import capo_securityagent.types.code_review_list


class BatchGetCodeReviewsOutput(TypedDict, closed=True):
    code_reviews: NotRequired[
        "capo_securityagent.types.code_review_list.CodeReviewList"
    ]
    """<p>The list of code reviews that were found.</p>"""
    not_found: NotRequired[
        "capo_securityagent.types.code_review_id_list.CodeReviewIdList"
    ]
    """<p>The list of code review identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeReviewsOutput) -> dict:
    out: dict = {}
    if "code_reviews" in value:
        import capo_securityagent.types.code_review_list

        out["codeReviews"] = capo_securityagent.types.code_review_list.serialize_json(
            value["code_reviews"]
        )
    if "not_found" in value:
        import capo_securityagent.types.code_review_id_list

        out["notFound"] = capo_securityagent.types.code_review_id_list.serialize_json(
            value["not_found"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetCodeReviewsOutput:
    out: BatchGetCodeReviewsOutput = {}  # type: ignore[typeddict-item]
    if data.get("codeReviews") is not None:
        import capo_securityagent.types.code_review_list

        out["code_reviews"] = (
            capo_securityagent.types.code_review_list.deserialize_json(
                data["codeReviews"]
            )
        )
    if data.get("notFound") is not None:
        import capo_securityagent.types.code_review_id_list

        out["not_found"] = (
            capo_securityagent.types.code_review_id_list.deserialize_json(
                data["notFound"]
            )
        )
    return out


def redact_sensitive(value: BatchGetCodeReviewsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code_reviews" in value:
        import capo_securityagent.types.code_review_list

        out["code_reviews"] = (
            capo_securityagent.types.code_review_list.redact_sensitive(
                value["code_reviews"]
            )
        )
    return out
