"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_owner_id
    import capo_inspector2.types.cis_scan_configuration_arn
    import capo_inspector2.types.cis_scan_name
    import capo_inspector2.types.cis_security_level
    import capo_inspector2.types.cis_tag_map
    import capo_inspector2.types.cis_targets
    import capo_inspector2.types.schedule


class CisScanConfiguration(TypedDict, closed=True):
    scan_configuration_arn: (
        "capo_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn"
    )
    """<p>The CIS scan configuration's scan configuration ARN.</p>"""
    owner_id: NotRequired["capo_inspector2.types.cis_owner_id.CisOwnerId"]
    """<p>The CIS scan configuration's owner ID.</p>"""
    scan_name: NotRequired["capo_inspector2.types.cis_scan_name.CisScanName"]
    """<p>The name of the CIS scan configuration.</p>"""
    security_level: NotRequired[
        "capo_inspector2.types.cis_security_level.CisSecurityLevel"
    ]
    """<p>The CIS scan configuration's security level.</p>"""
    schedule: NotRequired["capo_inspector2.types.schedule.Schedule"]
    """<p>The CIS scan configuration's schedule.</p>"""
    targets: NotRequired["capo_inspector2.types.cis_targets.CisTargets"]
    """<p>The CIS scan configuration's targets.</p>"""
    tags: NotRequired["capo_inspector2.types.cis_tag_map.CisTagMap"]
    """<p>The CIS scan configuration's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisScanConfiguration) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    if "owner_id" in value:
        out["ownerId"] = value["owner_id"]
    if "scan_name" in value:
        out["scanName"] = value["scan_name"]
    if "security_level" in value:
        import capo_inspector2.types.cis_security_level

        out["securityLevel"] = capo_inspector2.types.cis_security_level.serialize_json(
            value["security_level"]
        )
    if "schedule" in value:
        import capo_inspector2.types.schedule

        out["schedule"] = capo_inspector2.types.schedule.serialize_json(
            value["schedule"]
        )
    if "targets" in value:
        import capo_inspector2.types.cis_targets

        out["targets"] = capo_inspector2.types.cis_targets.serialize_json(
            value["targets"]
        )
    if "tags" in value:
        import capo_inspector2.types.cis_tag_map

        out["tags"] = capo_inspector2.types.cis_tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CisScanConfiguration:
    out: CisScanConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scanConfigurationArn") is not None:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        out["scan_configuration_arn"] = ""
    if data.get("ownerId") is not None:
        out["owner_id"] = data["ownerId"]
    if data.get("scanName") is not None:
        out["scan_name"] = data["scanName"]
    if data.get("securityLevel") is not None:
        import capo_inspector2.types.cis_security_level

        out["security_level"] = (
            capo_inspector2.types.cis_security_level.deserialize_json(
                data["securityLevel"]
            )
        )
    if data.get("schedule") is not None:
        import capo_inspector2.types.schedule

        out["schedule"] = capo_inspector2.types.schedule.deserialize_json(
            data["schedule"]
        )
    if data.get("targets") is not None:
        import capo_inspector2.types.cis_targets

        out["targets"] = capo_inspector2.types.cis_targets.deserialize_json(
            data["targets"]
        )
    if data.get("tags") is not None:
        import capo_inspector2.types.cis_tag_map

        out["tags"] = capo_inspector2.types.cis_tag_map.deserialize_json(data["tags"])
    return out
