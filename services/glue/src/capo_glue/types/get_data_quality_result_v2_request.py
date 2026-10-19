"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityResultV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class GetDataQualityResultV2Request(TypedDict, closed=True):
    result_id: "capo_glue.types.hash_string.HashString"
    """<p>A unique result ID for the data quality result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityResultV2Request) -> dict:
    out: dict = {}
    out["ResultId"] = value["result_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityResultV2Request:
    out: GetDataQualityResultV2Request = {}  # type: ignore[typeddict-item]
    if data.get("ResultId") is not None:
        out["result_id"] = data["ResultId"]
    else:
        out["result_id"] = ""
    return out
