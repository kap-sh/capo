"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateHybridADResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_id
    import capo_directory_service.types.directory_id


class UpdateHybridADResult(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The identifier of the updated hybrid directory.</p>"""
    assessment_id: NotRequired[
        "capo_directory_service.types.assessment_id.AssessmentId"
    ]
    """<p>The identifier of the assessment performed to validate the update configuration. This assessment ensures the updated settings are compatible with your environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHybridADResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHybridADResult:
    out: UpdateHybridADResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("AssessmentId") is not None:
        out["assessment_id"] = data["AssessmentId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateHybridADResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    return out


def deserialize_cbor(data: dict) -> UpdateHybridADResult:
    out: UpdateHybridADResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("AssessmentId") is not None:
        out["assessment_id"] = data["AssessmentId"]
    return out
