"""Generated from Smithy shape ``com.amazonaws.frauddetector#DescribeDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.detector_version_max_results
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.string


class DescribeDetectorRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The detector ID.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token from the previous response.</p>"""
    max_results: NotRequired[
        "capo_frauddetector.types.detector_version_max_results.DetectorVersionMaxResults"
    ]
    """<p>The maximum number of results to return for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDetectorRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDetectorRequest:
    out: DescribeDetectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        out["detector_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
