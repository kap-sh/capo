"""Generated from Smithy shape ``com.amazonaws.controltower#CreateLandingZoneInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_version
    import capo_controltower.types.manifest
    import capo_controltower.types.remediation_types
    import capo_controltower.types.tag_map


class CreateLandingZoneInput(TypedDict, closed=True):
    version: "capo_controltower.types.landing_zone_version.LandingZoneVersion"
    """<p>The landing zone version, for example, 3.0.</p>"""
    remediation_types: NotRequired[
        "capo_controltower.types.remediation_types.RemediationTypes"
    ]
    """<p>Specifies the types of remediation actions to apply when creating the landing zone, such as automatic drift correction or compliance enforcement.</p>"""
    tags: NotRequired["capo_controltower.types.tag_map.TagMap"]
    """<p>Tags to be applied to the landing zone. </p>"""
    manifest: NotRequired["capo_controltower.types.manifest.Manifest"]
    """<p>The manifest JSON file is a text file that describes your Amazon Web Services resources. For examples, review <a href="https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch">Launch your landing zone</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLandingZoneInput) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "remediation_types" in value:
        import capo_controltower.types.remediation_types

        out["remediationTypes"] = (
            capo_controltower.types.remediation_types.serialize_json(
                value["remediation_types"]
            )
        )
    if "tags" in value:
        import capo_controltower.types.tag_map

        out["tags"] = capo_controltower.types.tag_map.serialize_json(value["tags"])
    if "manifest" in value:
        out["manifest"] = value["manifest"]
    return out


def deserialize_json(data: dict) -> CreateLandingZoneInput:
    out: CreateLandingZoneInput = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreateLandingZoneInput.version required")
    if data.get("remediationTypes") is not None:
        import capo_controltower.types.remediation_types

        out["remediation_types"] = (
            capo_controltower.types.remediation_types.deserialize_json(
                data["remediationTypes"]
            )
        )
    if data.get("tags") is not None:
        import capo_controltower.types.tag_map

        out["tags"] = capo_controltower.types.tag_map.deserialize_json(data["tags"])
    if data.get("manifest") is not None:
        out["manifest"] = data["manifest"]
    return out
