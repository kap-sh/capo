"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.landing_zone_drift_status_summary
    import capo_controltower.types.landing_zone_status
    import capo_controltower.types.landing_zone_version
    import capo_controltower.types.manifest
    import capo_controltower.types.remediation_types


class LandingZoneDetail(TypedDict, closed=True):
    version: "capo_controltower.types.landing_zone_version.LandingZoneVersion"
    """<p>The landing zone's current deployed version.</p>"""
    remediation_types: NotRequired[
        "capo_controltower.types.remediation_types.RemediationTypes"
    ]
    """<p>The types of remediation actions configured for the landing zone, such as automatic drift correction or compliance enforcement.</p>"""
    arn: NotRequired["capo_controltower.types.arn.Arn"]
    """<p>The ARN of the landing zone.</p>"""
    status: NotRequired["capo_controltower.types.landing_zone_status.LandingZoneStatus"]
    """<p>The landing zone deployment status. One of <code>ACTIVE</code>, <code>PROCESSING</code>, <code>FAILED</code>.</p>"""
    latest_available_version: NotRequired[
        "capo_controltower.types.landing_zone_version.LandingZoneVersion"
    ]
    """<p>The latest available version of the landing zone.</p>"""
    drift_status: NotRequired[
        "capo_controltower.types.landing_zone_drift_status_summary.LandingZoneDriftStatusSummary"
    ]
    """<p>The drift status of the landing zone.</p>"""
    manifest: "capo_controltower.types.manifest.Manifest"
    """<p>The landing zone manifest JSON text file that specifies the landing zone configurations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneDetail) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "remediation_types" in value:
        import capo_controltower.types.remediation_types

        out["remediationTypes"] = (
            capo_controltower.types.remediation_types.serialize_json(
                value["remediation_types"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        import capo_controltower.types.landing_zone_status

        out["status"] = capo_controltower.types.landing_zone_status.serialize_json(
            value["status"]
        )
    if "latest_available_version" in value:
        out["latestAvailableVersion"] = value["latest_available_version"]
    if "drift_status" in value:
        import capo_controltower.types.landing_zone_drift_status_summary

        out["driftStatus"] = (
            capo_controltower.types.landing_zone_drift_status_summary.serialize_json(
                value["drift_status"]
            )
        )
    out["manifest"] = value["manifest"]
    return out


def deserialize_json(data: dict) -> LandingZoneDetail:
    out: LandingZoneDetail = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("remediationTypes") is not None:
        import capo_controltower.types.remediation_types

        out["remediation_types"] = (
            capo_controltower.types.remediation_types.deserialize_json(
                data["remediationTypes"]
            )
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        import capo_controltower.types.landing_zone_status

        out["status"] = capo_controltower.types.landing_zone_status.deserialize_json(
            data["status"]
        )
    if data.get("latestAvailableVersion") is not None:
        out["latest_available_version"] = data["latestAvailableVersion"]
    if data.get("driftStatus") is not None:
        import capo_controltower.types.landing_zone_drift_status_summary

        out["drift_status"] = (
            capo_controltower.types.landing_zone_drift_status_summary.deserialize_json(
                data["driftStatus"]
            )
        )
    if data.get("manifest") is not None:
        out["manifest"] = data["manifest"]
    else:
        out["manifest"] = None
    return out
