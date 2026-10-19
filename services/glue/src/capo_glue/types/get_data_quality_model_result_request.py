"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityModelResultRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class GetDataQualityModelResultRequest(TypedDict, closed=True):
    statistic_id: "capo_glue.types.hash_string.HashString"
    """<p>The Statistic ID.</p>"""
    profile_id: "capo_glue.types.hash_string.HashString"
    """<p>The Profile ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityModelResultRequest) -> dict:
    out: dict = {}
    out["StatisticId"] = value["statistic_id"]
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityModelResultRequest:
    out: GetDataQualityModelResultRequest = {}  # type: ignore[typeddict-item]
    if data.get("StatisticId") is not None:
        out["statistic_id"] = data["StatisticId"]
    else:
        out["statistic_id"] = ""
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    return out
