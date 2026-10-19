"""Generated from Smithy shape ``com.amazonaws.healthlake#DeleteDataTransformationProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.profile_id_string


class DeleteDataTransformationProfileRequest(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the profile to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDataTransformationProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDataTransformationProfileRequest:
    out: DeleteDataTransformationProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    return out
