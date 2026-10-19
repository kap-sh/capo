"""Generated from Smithy shape ``com.amazonaws.glue#ResponseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.json_path_string


class ResponseConfiguration(TypedDict, closed=True):
    result_path: "capo_glue.types.json_path_string.JsonPathString"
    """<p>The JSON path expression that identifies where the actual result data is located within the API response.</p>"""
    error_path: NotRequired["capo_glue.types.json_path_string.JsonPathString"]
    """<p>The JSON path expression that identifies where error information is located within API responses when requests fail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseConfiguration) -> dict:
    out: dict = {}
    out["ResultPath"] = value["result_path"]
    if "error_path" in value:
        out["ErrorPath"] = value["error_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseConfiguration:
    out: ResponseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ResultPath") is not None:
        out["result_path"] = data["ResultPath"]
    else:
        out["result_path"] = ""
    if data.get("ErrorPath") is not None:
        out["error_path"] = data["ErrorPath"]
    return out
