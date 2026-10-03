"""Generated from Smithy shape ``com.amazonaws.controltower#UpdateLandingZoneInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_version
    import capo_controltower.types.manifest
    import capo_controltower.types.remediation_types


class UpdateLandingZoneInput(TypedDict, closed=True):
    version: "capo_controltower.types.landing_zone_version.LandingZoneVersion"
    """<p>The landing zone version, for example, 3.2.</p>"""
    remediation_types: NotRequired[
        "capo_controltower.types.remediation_types.RemediationTypes"
    ]
    """<p>Specifies the types of remediation actions to apply when updating the landing zone configuration.</p>"""
    landing_zone_identifier: "str"
    """<p>The unique identifier of the landing zone.</p>"""
    manifest: NotRequired["capo_controltower.types.manifest.Manifest"]
    """<p>The manifest file (JSON) is a text file that describes your Amazon Web Services resources. For an example, review <a href="https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch">Launch your landing zone</a>. The example manifest file contains each of the available parameters. The schema for the landing zone's JSON manifest file is not published, by design.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLandingZoneInput) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "remediation_types" in value:
        import capo_controltower.types.remediation_types

        out["remediationTypes"] = (
            capo_controltower.types.remediation_types.serialize_json(
                value["remediation_types"]
            )
        )
    out["landingZoneIdentifier"] = value["landing_zone_identifier"]
    if "manifest" in value:
        out["manifest"] = value["manifest"]
    return out


def deserialize_json(data: dict) -> UpdateLandingZoneInput:
    out: UpdateLandingZoneInput = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("UpdateLandingZoneInput.version required")
    if data.get("remediationTypes") is not None:
        import capo_controltower.types.remediation_types

        out["remediation_types"] = (
            capo_controltower.types.remediation_types.deserialize_json(
                data["remediationTypes"]
            )
        )
    if data.get("landingZoneIdentifier") is not None:
        out["landing_zone_identifier"] = data["landingZoneIdentifier"]
    else:
        raise DeserializationError(
            "UpdateLandingZoneInput.landing_zone_identifier required"
        )
    if data.get("manifest") is not None:
        out["manifest"] = data["manifest"]
    return out
