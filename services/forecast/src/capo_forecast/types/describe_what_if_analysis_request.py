"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeWhatIfAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DescribeWhatIfAnalysisRequest(TypedDict, closed=True):
    what_if_analysis_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the what-if analysis that you are interested in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWhatIfAnalysisRequest) -> dict:
    out: dict = {}
    out["WhatIfAnalysisArn"] = value["what_if_analysis_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWhatIfAnalysisRequest:
    out: DescribeWhatIfAnalysisRequest = {}  # type: ignore[typeddict-item]
    if data.get("WhatIfAnalysisArn") is not None:
        out["what_if_analysis_arn"] = data["WhatIfAnalysisArn"]
    else:
        out["what_if_analysis_arn"] = ""
    return out
