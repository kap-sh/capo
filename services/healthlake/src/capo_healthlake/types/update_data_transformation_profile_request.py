"""Generated from Smithy shape ``com.amazonaws.healthlake#UpdateDataTransformationProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.change_description
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.profile_mapping


class UpdateDataTransformationProfileRequest(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the profile to update.</p>"""
    profile_mapping: "capo_healthlake.types.profile_mapping.ProfileMapping"
    """<p>The new profile content for the DRAFT version. This is a full replacement of all profile files.</p>"""
    change_description: NotRequired[
        "capo_healthlake.types.change_description.ChangeDescription"
    ]
    """<p>A description of what changed in this update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDataTransformationProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    import capo_healthlake.types.profile_mapping

    out["ProfileMapping"] = (
        capo_healthlake.types.profile_mapping.serialize_aws_json_1_0(
            value["profile_mapping"]
        )
    )
    if "change_description" in value:
        out["ChangeDescription"] = value["change_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDataTransformationProfileRequest:
    out: UpdateDataTransformationProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("ProfileMapping") is not None:
        import capo_healthlake.types.profile_mapping

        out["profile_mapping"] = (
            capo_healthlake.types.profile_mapping.deserialize_aws_json_1_0(
                data["ProfileMapping"]
            )
        )
    else:
        out["profile_mapping"] = {}
    if data.get("ChangeDescription") is not None:
        out["change_description"] = data["ChangeDescription"]
    return out


def redact_sensitive(value: UpdateDataTransformationProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "profile_mapping" in value:
        out["profile_mapping"] = "*** Sensitive Data Redacted ***"
    return out
