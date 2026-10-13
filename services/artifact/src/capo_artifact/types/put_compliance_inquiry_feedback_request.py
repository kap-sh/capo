"""Generated from Smithy shape ``com.amazonaws.artifact#PutComplianceInquiryFeedbackRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_artifact.errors import DeserializationError

if TYPE_CHECKING:
    import capo_artifact.types.feedback_comment_attribute
    import capo_artifact.types.feedback_rating
    import capo_artifact.types.feedback_reason_code_list
    import capo_artifact.types.idempotent_client_token
    import capo_artifact.types.inquiry_id


class PutComplianceInquiryFeedbackRequest(TypedDict, closed=True):
    compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId"
    """<p>The unique identifier for the compliance inquiry.</p>"""
    query_identifier: NotRequired["int"]
    """<p>The sequential identifier of the query to provide feedback on.</p>"""
    rating: "capo_artifact.types.feedback_rating.FeedbackRating"
    """<p>The rating for the feedback. Valid values are THUMBS_UP and THUMBS_DOWN.</p>"""
    response_revision_id: NotRequired["int"]
    """<p>The response revision ID. Use this value to prevent submitting feedback on a stale response.</p>"""
    reason_codes: NotRequired[
        "capo_artifact.types.feedback_reason_code_list.FeedbackReasonCodeList"
    ]
    """<p>The reason codes that describe why you rated the response. Valid values are OTHER, PARTIAL_RESPONSE, and IRRELEVANT_RESPONSE.</p>"""
    comment: NotRequired[
        "capo_artifact.types.feedback_comment_attribute.FeedbackCommentAttribute"
    ]
    """<p>An optional comment for the feedback.</p>"""
    client_token: NotRequired[
        "capo_artifact.types.idempotent_client_token.IdempotentClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutComplianceInquiryFeedbackRequest) -> dict:
    out: dict = {}
    out["complianceInquiryId"] = value["compliance_inquiry_id"]
    if "query_identifier" in value:
        out["queryIdentifier"] = value["query_identifier"]
    import capo_artifact.types.feedback_rating

    out["rating"] = capo_artifact.types.feedback_rating.serialize_json(value["rating"])
    if "response_revision_id" in value:
        out["responseRevisionId"] = value["response_revision_id"]
    if "reason_codes" in value:
        import capo_artifact.types.feedback_reason_code_list

        out["reasonCodes"] = (
            capo_artifact.types.feedback_reason_code_list.serialize_json(
                value["reason_codes"]
            )
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutComplianceInquiryFeedbackRequest:
    out: PutComplianceInquiryFeedbackRequest = {}  # type: ignore[typeddict-item]
    if data.get("complianceInquiryId") is not None:
        out["compliance_inquiry_id"] = data["complianceInquiryId"]
    else:
        raise DeserializationError(
            "PutComplianceInquiryFeedbackRequest.compliance_inquiry_id required"
        )
    if data.get("queryIdentifier") is not None:
        out["query_identifier"] = data["queryIdentifier"]
    if data.get("rating") is not None:
        import capo_artifact.types.feedback_rating

        out["rating"] = capo_artifact.types.feedback_rating.deserialize_json(
            data["rating"]
        )
    else:
        raise DeserializationError(
            "PutComplianceInquiryFeedbackRequest.rating required"
        )
    if data.get("responseRevisionId") is not None:
        out["response_revision_id"] = data["responseRevisionId"]
    if data.get("reasonCodes") is not None:
        import capo_artifact.types.feedback_reason_code_list

        out["reason_codes"] = (
            capo_artifact.types.feedback_reason_code_list.deserialize_json(
                data["reasonCodes"]
            )
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: PutComplianceInquiryFeedbackRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comment" in value:
        out["comment"] = "*** Sensitive Data Redacted ***"
    return out
