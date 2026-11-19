"""Generated from Smithy shape ``com.amazonaws.comprehend#InvalidRequestDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.invalid_request_detail_reason


class InvalidRequestDetail(TypedDict, closed=True):
    reason: NotRequired[
        "capo_comprehend.types.invalid_request_detail_reason.InvalidRequestDetailReason"
    ]
    """<p>Reason codes include the following values:</p> <ul> <li> <p>DOCUMENT_SIZE_EXCEEDED - Document size is too large. Check the size of your file and resubmit the request.</p> </li> <li> <p>UNSUPPORTED_DOC_TYPE - Document type is not supported. Check the file type and resubmit the request.</p> </li> <li> <p>PAGE_LIMIT_EXCEEDED - Too many pages in the document. Check the number of pages in your file and resubmit the request.</p> </li> <li> <p>TEXTRACT_ACCESS_DENIED - Access denied to Amazon Textract. Verify that your account has permission to use Amazon Textract API operations and resubmit the request.</p> </li> <li> <p>NOT_TEXTRACT_JSON - Document is not Amazon Textract JSON format. Verify the format and resubmit the request.</p> </li> <li> <p>MISMATCHED_TOTAL_PAGE_COUNT - Check the number of pages in your file and resubmit the request.</p> </li> <li> <p>INVALID_DOCUMENT - Invalid document. Check the file and resubmit the request.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequestDetail) -> dict:
    out: dict = {}
    if "reason" in value:
        import capo_comprehend.types.invalid_request_detail_reason

        out["Reason"] = (
            capo_comprehend.types.invalid_request_detail_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRequestDetail:
    out: InvalidRequestDetail = {}  # type: ignore[typeddict-item]
    if data.get("Reason") is not None:
        import capo_comprehend.types.invalid_request_detail_reason

        out["reason"] = (
            capo_comprehend.types.invalid_request_detail_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InvalidRequestDetail) -> dict:
    out: dict = {}
    if "reason" in value:
        import capo_comprehend.types.invalid_request_detail_reason

        out["Reason"] = (
            capo_comprehend.types.invalid_request_detail_reason.serialize_cbor(
                value["reason"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> InvalidRequestDetail:
    out: InvalidRequestDetail = {}  # type: ignore[typeddict-item]
    if data.get("Reason") is not None:
        import capo_comprehend.types.invalid_request_detail_reason

        out["reason"] = (
            capo_comprehend.types.invalid_request_detail_reason.deserialize_cbor(
                data["Reason"]
            )
        )
    return out
