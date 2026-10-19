"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class GetDataQualityModelRequest(TypedDict, closed=True):
    statistic_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The Statistic ID.</p>"""
    profile_id: "capo_glue.types.hash_string.HashString"
    """<p>The Profile ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityModelRequest) -> dict:
    out: dict = {}
    if "statistic_id" in value:
        out["StatisticId"] = value["statistic_id"]
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityModelRequest:
    out: GetDataQualityModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("StatisticId") is not None:
        out["statistic_id"] = data["StatisticId"]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    return out
