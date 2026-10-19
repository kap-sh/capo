"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSnippetError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_snippet_error_code
    import capo_inspector2.types.finding_arn
    import capo_inspector2.types.non_empty_string


class CodeSnippetError(TypedDict, closed=True):
    finding_arn: "capo_inspector2.types.finding_arn.FindingArn"
    """<p>The ARN of the finding that a code snippet couldn't be retrieved for.</p>"""
    error_code: "capo_inspector2.types.code_snippet_error_code.CodeSnippetErrorCode"
    """<p>The error code for the error that prevented a code snippet from being retrieved.</p>"""
    error_message: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The error message received when Amazon Inspector failed to retrieve a code snippet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSnippetError) -> dict:
    out: dict = {}
    out["findingArn"] = value["finding_arn"]
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> CodeSnippetError:
    out: CodeSnippetError = {}  # type: ignore[typeddict-item]
    if data.get("findingArn") is not None:
        out["finding_arn"] = data["findingArn"]
    else:
        out["finding_arn"] = ""
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
