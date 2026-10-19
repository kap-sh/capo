"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCisScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_configuration_arn
    import capo_inspector2.types.cis_scan_name
    import capo_inspector2.types.cis_security_level
    import capo_inspector2.types.schedule
    import capo_inspector2.types.update_cis_targets


class UpdateCisScanConfigurationRequest(TypedDict, closed=True):
    scan_configuration_arn: (
        "capo_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn"
    )
    """<p>The CIS scan configuration ARN.</p>"""
    scan_name: NotRequired["capo_inspector2.types.cis_scan_name.CisScanName"]
    """<p>The scan name for the CIS scan configuration.</p>"""
    security_level: NotRequired[
        "capo_inspector2.types.cis_security_level.CisSecurityLevel"
    ]
    """<p> The security level for the CIS scan configuration. Security level refers to the Benchmark levels that CIS assigns to a profile. </p>"""
    schedule: NotRequired["capo_inspector2.types.schedule.Schedule"]
    """<p>The schedule for the CIS scan configuration.</p>"""
    targets: NotRequired["capo_inspector2.types.update_cis_targets.UpdateCisTargets"]
    """<p>The targets for the CIS scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCisScanConfigurationRequest) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
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
        import capo_inspector2.types.update_cis_targets

        out["targets"] = capo_inspector2.types.update_cis_targets.serialize_json(
            value["targets"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCisScanConfigurationRequest:
    out: UpdateCisScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanConfigurationArn") is not None:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        out["scan_configuration_arn"] = ""
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
        import capo_inspector2.types.update_cis_targets

        out["targets"] = capo_inspector2.types.update_cis_targets.deserialize_json(
            data["targets"]
        )
    return out
