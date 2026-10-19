"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateDetectorVersionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.detector_version_status
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.whole_number_version_string


class UpdateDetectorVersionStatusRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The detector ID. </p>"""
    detector_version_id: (
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    )
    """<p>The detector version ID. </p>"""
    status: "capo_frauddetector.types.detector_version_status.DetectorVersionStatus"
    """<p>The new status.</p> <p>The only supported values are <code>ACTIVE</code> and <code>INACTIVE</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDetectorVersionStatusRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["detectorVersionId"] = value["detector_version_id"]
    import capo_frauddetector.types.detector_version_status

    out["status"] = (
        capo_frauddetector.types.detector_version_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDetectorVersionStatusRequest:
    out: UpdateDetectorVersionStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        out["detector_id"] = ""
    if data.get("detectorVersionId") is not None:
        out["detector_version_id"] = data["detectorVersionId"]
    else:
        out["detector_version_id"] = ""
    if data.get("status") is not None:
        import capo_frauddetector.types.detector_version_status

        out["status"] = (
            capo_frauddetector.types.detector_version_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_frauddetector.types.detector_version_status.DetectorVersionStatus", ""
        )
    return out
