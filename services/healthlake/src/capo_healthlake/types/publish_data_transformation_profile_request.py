"""Generated from Smithy shape ``com.amazonaws.healthlake#PublishDataTransformationProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.change_description
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.profile_version
    import capo_healthlake.types.source_format


class PublishDataTransformationProfileRequest(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the profile to publish.</p>"""
    source_format: "capo_healthlake.types.source_format.SourceFormat"
    """<p>The source data format of the profile.</p>"""
    from_existing_version: NotRequired[
        "capo_healthlake.types.profile_version.ProfileVersion"
    ]
    """<p>The version number of a previously published version to republish as the new latest version. Use this parameter for rollback scenarios. If you omit this parameter, the service publishes the current DRAFT version.</p>"""
    change_description: NotRequired[
        "capo_healthlake.types.change_description.ChangeDescription"
    ]
    """<p>A description of what changed or why this version is being published.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublishDataTransformationProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    import capo_healthlake.types.source_format

    out["SourceFormat"] = capo_healthlake.types.source_format.serialize_aws_json_1_0(
        value["source_format"]
    )
    if "from_existing_version" in value:
        out["FromExistingVersion"] = value["from_existing_version"]
    if "change_description" in value:
        out["ChangeDescription"] = value["change_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PublishDataTransformationProfileRequest:
    out: PublishDataTransformationProfileRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("FromExistingVersion") is not None:
        out["from_existing_version"] = data["FromExistingVersion"]
    if data.get("ChangeDescription") is not None:
        out["change_description"] = data["ChangeDescription"]
    return out
