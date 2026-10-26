"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCisScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_name
    import capo_inspector2.types.cis_security_level
    import capo_inspector2.types.cis_tag_map
    import capo_inspector2.types.create_cis_targets
    import capo_inspector2.types.schedule


class CreateCisScanConfigurationRequest(TypedDict, closed=True):
    scan_name: "capo_inspector2.types.cis_scan_name.CisScanName"
    """<p>The scan name for the CIS scan configuration.</p>"""
    security_level: "capo_inspector2.types.cis_security_level.CisSecurityLevel"
    """<p> The security level for the CIS scan configuration. Security level refers to the Benchmark levels that CIS assigns to a profile. </p>"""
    schedule: "capo_inspector2.types.schedule.Schedule"
    """<p>The schedule for the CIS scan configuration.</p>"""
    targets: "capo_inspector2.types.create_cis_targets.CreateCisTargets"
    """<p>The targets for the CIS scan configuration.</p>"""
    tags: NotRequired["capo_inspector2.types.cis_tag_map.CisTagMap"]
    """<p>The tags for the CIS scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCisScanConfigurationRequest) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    import capo_inspector2.types.cis_security_level

    out["securityLevel"] = capo_inspector2.types.cis_security_level.serialize_json(
        value["security_level"]
    )
    import capo_inspector2.types.schedule

    out["schedule"] = capo_inspector2.types.schedule.serialize_json(value["schedule"])
    import capo_inspector2.types.create_cis_targets

    out["targets"] = capo_inspector2.types.create_cis_targets.serialize_json(
        value["targets"]
    )
    if "tags" in value:
        import capo_inspector2.types.cis_tag_map

        out["tags"] = capo_inspector2.types.cis_tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCisScanConfigurationRequest:
    out: CreateCisScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanName") is not None:
        out["scan_name"] = data["scanName"]
    else:
        out["scan_name"] = ""
    if data.get("securityLevel") is not None:
        import capo_inspector2.types.cis_security_level

        out["security_level"] = (
            capo_inspector2.types.cis_security_level.deserialize_json(
                data["securityLevel"]
            )
        )
    else:
        import typing

        out["security_level"] = typing.cast(
            "capo_inspector2.types.cis_security_level.CisSecurityLevel", ""
        )
    if data.get("schedule") is not None:
        import capo_inspector2.types.schedule

        out["schedule"] = capo_inspector2.types.schedule.deserialize_json(
            data["schedule"]
        )
    else:
        out["schedule"] = {"$unknown": {"name": ""}}
    if data.get("targets") is not None:
        import capo_inspector2.types.create_cis_targets

        out["targets"] = capo_inspector2.types.create_cis_targets.deserialize_json(
            data["targets"]
        )
    else:
        raise DeserializationError("CreateCisScanConfigurationRequest.targets required")
    if data.get("tags") is not None:
        import capo_inspector2.types.cis_tag_map

        out["tags"] = capo_inspector2.types.cis_tag_map.deserialize_json(data["tags"])
    return out
