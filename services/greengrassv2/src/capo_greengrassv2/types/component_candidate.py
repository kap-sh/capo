"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentCandidate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_name_string
    import capo_greengrassv2.types.component_version_requirement_map
    import capo_greengrassv2.types.component_version_string


class ComponentCandidate(TypedDict, closed=True):
    component_name: NotRequired[
        "capo_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p>"""
    component_version: NotRequired[
        "capo_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p>"""
    version_requirements: NotRequired[
        "capo_greengrassv2.types.component_version_requirement_map.ComponentVersionRequirementMap"
    ]
    """<p>The version requirements for the component's dependencies. Greengrass core devices get the version requirements from component recipes.</p> <p>IoT Greengrass V2 uses semantic version constraints. For more information, see <a href="https://semver.org/">Semantic Versioning</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentCandidate) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "version_requirements" in value:
        import capo_greengrassv2.types.component_version_requirement_map

        out["versionRequirements"] = (
            capo_greengrassv2.types.component_version_requirement_map.serialize_json(
                value["version_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentCandidate:
    out: ComponentCandidate = {}  # type: ignore[typeddict-item]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("componentVersion") is not None:
        out["component_version"] = data["componentVersion"]
    if data.get("versionRequirements") is not None:
        import capo_greengrassv2.types.component_version_requirement_map

        out["version_requirements"] = (
            capo_greengrassv2.types.component_version_requirement_map.deserialize_json(
                data["versionRequirements"]
            )
        )
    return out
