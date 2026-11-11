"""Generated from Smithy shape ``com.amazonaws.glue#StopJobUpgradeAnalysisResponse``."""

from typing_extensions import TypedDict


class StopJobUpgradeAnalysisResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopJobUpgradeAnalysisResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopJobUpgradeAnalysisResponse:
    out: StopJobUpgradeAnalysisResponse = {}  # type: ignore[typeddict-item]
    return out
