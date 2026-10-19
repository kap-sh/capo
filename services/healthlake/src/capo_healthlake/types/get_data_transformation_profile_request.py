"""Generated from Smithy shape ``com.amazonaws.healthlake#GetDataTransformationProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.profile_version


class GetDataTransformationProfileRequest(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the profile to retrieve.</p>"""
    profile_version: NotRequired["capo_healthlake.types.profile_version.ProfileVersion"]
    """<p>The version number to retrieve. Specify 0 to retrieve the DRAFT version. If you omit this parameter, the service returns the latest published version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDataTransformationProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    if "profile_version" in value:
        out["ProfileVersion"] = value["profile_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDataTransformationProfileRequest:
    out: GetDataTransformationProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("ProfileVersion") is not None:
        out["profile_version"] = data["ProfileVersion"]
    return out
