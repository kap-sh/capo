"""Generated from Smithy shape ``com.amazonaws.healthlake#DeleteDataTransformationProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.date_time
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.profile_name_string


class DeleteDataTransformationProfileResponse(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the deleted profile.</p>"""
    profile_name: NotRequired[
        "capo_healthlake.types.profile_name_string.ProfileNameString"
    ]
    """<p>The name of the deleted profile.</p>"""
    deletion_time: "capo_healthlake.types.date_time.DateTime"
    """<p>The timestamp when the profile was deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDataTransformationProfileResponse) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    import capo_healthlake.types.date_time

    out["DeletionTime"] = capo_healthlake.types.date_time.serialize_aws_json_1_0(
        value["deletion_time"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDataTransformationProfileResponse:
    out: DeleteDataTransformationProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("ProfileName") is not None:
        out["profile_name"] = data["ProfileName"]
    if data.get("DeletionTime") is not None:
        import capo_healthlake.types.date_time

        out["deletion_time"] = capo_healthlake.types.date_time.deserialize_aws_json_1_0(
            data["DeletionTime"]
        )
    else:
        import datetime

        out["deletion_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
