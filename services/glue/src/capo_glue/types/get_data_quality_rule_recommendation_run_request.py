"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityRuleRecommendationRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class GetDataQualityRuleRecommendationRunRequest(TypedDict, closed=True):
    run_id: "capo_glue.types.hash_string.HashString"
    """<p>The unique run identifier associated with this run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityRuleRecommendationRunRequest) -> dict:
    out: dict = {}
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityRuleRecommendationRunRequest:
    out: GetDataQualityRuleRecommendationRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    return out
