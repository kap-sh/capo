"""Generated from Smithy shape ``com.amazonaws.comprehend#ErrorsListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.page_based_error_code
    import capo_comprehend.types.string


class ErrorsListItem(TypedDict, closed=True):
    page: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Page number where the error occurred.</p>"""
    error_code: NotRequired[
        "capo_comprehend.types.page_based_error_code.PageBasedErrorCode"
    ]
    """<p>Error code for the cause of the error.</p>"""
    error_message: NotRequired["capo_comprehend.types.string.String"]
    """<p>Text message explaining the reason for the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorsListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "error_code" in value:
        import capo_comprehend.types.page_based_error_code

        out["ErrorCode"] = (
            capo_comprehend.types.page_based_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorsListItem:
    out: ErrorsListItem = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("ErrorCode") is not None:
        import capo_comprehend.types.page_based_error_code

        out["error_code"] = (
            capo_comprehend.types.page_based_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ErrorsListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "error_code" in value:
        import capo_comprehend.types.page_based_error_code

        out["ErrorCode"] = capo_comprehend.types.page_based_error_code.serialize_cbor(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> ErrorsListItem:
    out: ErrorsListItem = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("ErrorCode") is not None:
        import capo_comprehend.types.page_based_error_code

        out["error_code"] = (
            capo_comprehend.types.page_based_error_code.deserialize_cbor(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
