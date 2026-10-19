"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateDetectorVersionMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.whole_number_version_string


class UpdateDetectorVersionMetadataRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The detector ID.</p>"""
    detector_version_id: (
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    )
    """<p>The detector version ID. </p>"""
    description: "capo_frauddetector.types.description.description"
    """<p>The description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDetectorVersionMetadataRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["detectorVersionId"] = value["detector_version_id"]
    out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDetectorVersionMetadataRequest:
    out: UpdateDetectorVersionMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        out["detector_id"] = ""
    if data.get("detectorVersionId") is not None:
        out["detector_version_id"] = data["detectorVersionId"]
    else:
        out["detector_version_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
