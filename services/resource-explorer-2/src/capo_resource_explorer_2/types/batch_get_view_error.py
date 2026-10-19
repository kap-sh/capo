"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#BatchGetViewError``."""

from typing_extensions import TypedDict


class BatchGetViewError(TypedDict, closed=True):
    view_arn: "str"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view for which Resource Explorer failed to retrieve details.</p>"""
    error_message: "str"
    """<p>The description of the error for the specified view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetViewError) -> dict:
    out: dict = {}
    out["ViewArn"] = value["view_arn"]
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchGetViewError:
    out: BatchGetViewError = {}  # type: ignore[typeddict-item]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    else:
        out["view_arn"] = ""
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    else:
        out["error_message"] = ""
    return out
