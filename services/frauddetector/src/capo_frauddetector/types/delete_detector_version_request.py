"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteDetectorVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.whole_number_version_string


class DeleteDetectorVersionRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The ID of the parent detector for the detector version to delete.</p>"""
    detector_version_id: (
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    )
    """<p>The ID of the detector version to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDetectorVersionRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["detectorVersionId"] = value["detector_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDetectorVersionRequest:
    out: DeleteDetectorVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        out["detector_id"] = ""
    if data.get("detectorVersionId") is not None:
        out["detector_version_id"] = data["detectorVersionId"]
    else:
        out["detector_version_id"] = ""
    return out
