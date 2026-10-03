"""Generated from Smithy shape ``com.amazonaws.athena#AthenaError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boolean
    import capo_athena.types.error_category
    import capo_athena.types.error_type
    import capo_athena.types.string


class AthenaError(TypedDict, closed=True):
    error_category: NotRequired["capo_athena.types.error_category.ErrorCategory"]
    """<p>An integer value that specifies the category of a query failure error. The following list shows the category for each integer value.</p> <p> <b>1</b> - System</p> <p> <b>2</b> - User</p> <p> <b>3</b> - Other</p>"""
    error_type: NotRequired["capo_athena.types.error_type.ErrorType"]
    """<p>An integer value that provides specific information about an Athena query error. For the meaning of specific values, see the <a href="https://docs.aws.amazon.com/athena/latest/ug/error-reference.html#error-reference-error-type-reference">Error Type Reference</a> in the <i>Amazon Athena User Guide</i>.</p>"""
    retryable: "capo_athena.types.boolean.Boolean"
    """<p>True if the query might succeed if resubmitted.</p>"""
    error_message: NotRequired["capo_athena.types.string.String"]
    """<p>Contains a short description of the error that occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AthenaError) -> dict:
    out: dict = {}
    if "error_category" in value:
        out["ErrorCategory"] = value["error_category"]
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    out["Retryable"] = value.get("retryable", False)
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AthenaError:
    out: AthenaError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCategory") is not None:
        out["error_category"] = data["ErrorCategory"]
    if data.get("ErrorType") is not None:
        out["error_type"] = data["ErrorType"]
    if data.get("Retryable") is not None:
        out["retryable"] = data["Retryable"]
    else:
        out["retryable"] = False
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
