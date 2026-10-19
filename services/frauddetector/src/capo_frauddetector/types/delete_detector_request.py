"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier


class DeleteDetectorRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The ID of the detector to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDetectorRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDetectorRequest:
    out: DeleteDetectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        out["detector_id"] = ""
    return out
