"""Generated from Smithy shape ``com.amazonaws.healthlake#UpdateDataTransformationProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.date_time
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.profile_name_string
    import capo_healthlake.types.source_format
    import capo_healthlake.types.target_format


class UpdateDataTransformationProfileResponse(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the updated profile.</p>"""
    source_format: "capo_healthlake.types.source_format.SourceFormat"
    """<p>The source data format of the profile.</p>"""
    target_format: "capo_healthlake.types.target_format.TargetFormat"
    """<p>The target output format of the profile.</p>"""
    profile_name: NotRequired[
        "capo_healthlake.types.profile_name_string.ProfileNameString"
    ]
    """<p>The name of the updated profile.</p>"""
    last_updated_at: "capo_healthlake.types.date_time.DateTime"
    """<p>The timestamp when the profile was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDataTransformationProfileResponse) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    import capo_healthlake.types.source_format

    out["SourceFormat"] = capo_healthlake.types.source_format.serialize_aws_json_1_0(
        value["source_format"]
    )
    import capo_healthlake.types.target_format

    out["TargetFormat"] = capo_healthlake.types.target_format.serialize_aws_json_1_0(
        value["target_format"]
    )
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    import capo_healthlake.types.date_time

    out["LastUpdatedAt"] = capo_healthlake.types.date_time.serialize_aws_json_1_0(
        value["last_updated_at"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDataTransformationProfileResponse:
    out: UpdateDataTransformationProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("SourceFormat") is not None:
        import capo_healthlake.types.source_format

        out["source_format"] = (
            capo_healthlake.types.source_format.deserialize_aws_json_1_0(
                data["SourceFormat"]
            )
        )
    else:
        import typing

        out["source_format"] = typing.cast(
            "capo_healthlake.types.source_format.SourceFormat", ""
        )
    if data.get("TargetFormat") is not None:
        import capo_healthlake.types.target_format

        out["target_format"] = (
            capo_healthlake.types.target_format.deserialize_aws_json_1_0(
                data["TargetFormat"]
            )
        )
    else:
        import typing

        out["target_format"] = typing.cast(
            "capo_healthlake.types.target_format.TargetFormat", ""
        )
    if data.get("ProfileName") is not None:
        out["profile_name"] = data["ProfileName"]
    if data.get("LastUpdatedAt") is not None:
        import capo_healthlake.types.date_time

        out["last_updated_at"] = (
            capo_healthlake.types.date_time.deserialize_aws_json_1_0(
                data["LastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
