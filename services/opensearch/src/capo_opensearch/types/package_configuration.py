"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.license_filepath
    import capo_opensearch.types.requirement_level


class PackageConfiguration(TypedDict, closed=True):
    license_requirement: "capo_opensearch.types.requirement_level.RequirementLevel"
    """<p>The license requirements for the package.</p>"""
    license_filepath: NotRequired[
        "capo_opensearch.types.license_filepath.LicenseFilepath"
    ]
    """<p>The relative file path for the license associated with the package.</p>"""
    configuration_requirement: (
        "capo_opensearch.types.requirement_level.RequirementLevel"
    )
    """<p>The configuration requirements for the package.</p>"""
    requires_restart_for_configuration_update: NotRequired[
        "capo_opensearch.types.boolean.Boolean"
    ]
    """<p>This indicates whether a B/G deployment is required for updating the configuration that the plugin is prerequisite for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageConfiguration) -> dict:
    out: dict = {}
    import capo_opensearch.types.requirement_level

    out["LicenseRequirement"] = capo_opensearch.types.requirement_level.serialize_json(
        value["license_requirement"]
    )
    if "license_filepath" in value:
        out["LicenseFilepath"] = value["license_filepath"]
    import capo_opensearch.types.requirement_level

    out["ConfigurationRequirement"] = (
        capo_opensearch.types.requirement_level.serialize_json(
            value["configuration_requirement"]
        )
    )
    if "requires_restart_for_configuration_update" in value:
        out["RequiresRestartForConfigurationUpdate"] = value[
            "requires_restart_for_configuration_update"
        ]
    return out


def deserialize_json(data: dict) -> PackageConfiguration:
    out: PackageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LicenseRequirement") is not None:
        import capo_opensearch.types.requirement_level

        out["license_requirement"] = (
            capo_opensearch.types.requirement_level.deserialize_json(
                data["LicenseRequirement"]
            )
        )
    else:
        import typing

        out["license_requirement"] = typing.cast(
            "capo_opensearch.types.requirement_level.RequirementLevel", ""
        )
    if data.get("LicenseFilepath") is not None:
        out["license_filepath"] = data["LicenseFilepath"]
    if data.get("ConfigurationRequirement") is not None:
        import capo_opensearch.types.requirement_level

        out["configuration_requirement"] = (
            capo_opensearch.types.requirement_level.deserialize_json(
                data["ConfigurationRequirement"]
            )
        )
    else:
        import typing

        out["configuration_requirement"] = typing.cast(
            "capo_opensearch.types.requirement_level.RequirementLevel", ""
        )
    if data.get("RequiresRestartForConfigurationUpdate") is not None:
        out["requires_restart_for_configuration_update"] = data[
            "RequiresRestartForConfigurationUpdate"
        ]
    return out
