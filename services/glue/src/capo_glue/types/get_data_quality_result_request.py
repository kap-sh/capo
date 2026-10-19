"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityResultRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class GetDataQualityResultRequest(TypedDict, closed=True):
    result_id: "capo_glue.types.hash_string.HashString"
    """<p>A unique result ID for the data quality result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityResultRequest) -> dict:
    out: dict = {}
    out["ResultId"] = value["result_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityResultRequest:
    out: GetDataQualityResultRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResultId") is not None:
        out["result_id"] = data["ResultId"]
    else:
        out["result_id"] = ""
    return out
