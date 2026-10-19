"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCodeSecurityScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_scan_configuration
    import capo_inspector2.types.configuration_level
    import capo_inspector2.types.scan_configuration_name
    import capo_inspector2.types.scope_settings
    import capo_inspector2.types.tag_map


class CreateCodeSecurityScanConfigurationRequest(TypedDict, closed=True):
    name: "capo_inspector2.types.scan_configuration_name.ScanConfigurationName"
    """<p>The name of the scan configuration.</p>"""
    level: "capo_inspector2.types.configuration_level.ConfigurationLevel"
    """<p>The security level for the scan configuration.</p>"""
    configuration: "capo_inspector2.types.code_security_scan_configuration.CodeSecurityScanConfiguration"
    """<p>The configuration settings for the code security scan.</p>"""
    scope_settings: NotRequired["capo_inspector2.types.scope_settings.ScopeSettings"]
    """<p>The scope settings that define which repositories will be scanned. Include this parameter to create a default scan configuration. Otherwise Amazon Inspector creates a general scan configuration. </p> <p>A default scan configuration automatically applies to all existing and future projects imported into Amazon Inspector. Use the <code>BatchAssociateCodeSecurityScanConfiguration</code> operation to associate a general scan configuration with projects.</p>"""
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags to apply to the scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSecurityScanConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_inspector2.types.configuration_level

    out["level"] = capo_inspector2.types.configuration_level.serialize_json(
        value["level"]
    )
    import capo_inspector2.types.code_security_scan_configuration

    out["configuration"] = (
        capo_inspector2.types.code_security_scan_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "scope_settings" in value:
        import capo_inspector2.types.scope_settings

        out["scopeSettings"] = capo_inspector2.types.scope_settings.serialize_json(
            value["scope_settings"]
        )
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCodeSecurityScanConfigurationRequest:
    out: CreateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("level") is not None:
        import capo_inspector2.types.configuration_level

        out["level"] = capo_inspector2.types.configuration_level.deserialize_json(
            data["level"]
        )
    else:
        import typing

        out["level"] = typing.cast(
            "capo_inspector2.types.configuration_level.ConfigurationLevel", ""
        )
    if data.get("configuration") is not None:
        import capo_inspector2.types.code_security_scan_configuration

        out["configuration"] = (
            capo_inspector2.types.code_security_scan_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCodeSecurityScanConfigurationRequest.configuration required"
        )
    if data.get("scopeSettings") is not None:
        import capo_inspector2.types.scope_settings

        out["scope_settings"] = capo_inspector2.types.scope_settings.deserialize_json(
            data["scopeSettings"]
        )
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    return out
