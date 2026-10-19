"""Generated from Smithy shape ``com.amazonaws.glue#PublishDataQualityResultV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class PublishDataQualityResultV2Response(TypedDict, closed=True):
    result_id: "capo_glue.types.hash_string.HashString"
    """<p>The ID of the result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublishDataQualityResultV2Response) -> dict:
    out: dict = {}
    out["ResultId"] = value["result_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PublishDataQualityResultV2Response:
    out: PublishDataQualityResultV2Response = {}  # type: ignore[typeddict-item]
    if data.get("ResultId") is not None:
        out["result_id"] = data["ResultId"]
    else:
        out["result_id"] = ""
    return out
