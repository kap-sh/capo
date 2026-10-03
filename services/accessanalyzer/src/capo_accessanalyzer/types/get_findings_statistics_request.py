"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingsStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn


class GetFindingsStatisticsRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> used to generate the statistics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsStatisticsRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    return out


def deserialize_json(data: dict) -> GetFindingsStatisticsRequest:
    out: GetFindingsStatisticsRequest = {}  # type: ignore[typeddict-item]
    if data.get("analyzerArn") is not None:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError("GetFindingsStatisticsRequest.analyzer_arn required")
    return out
