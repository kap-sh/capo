"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.dynamic_parameter_map
    import capo_appconfig.types.tag_map


class DeploymentParameters(TypedDict, closed=True):
    dynamic_extension_parameters: NotRequired[
        "capo_appconfig.types.dynamic_parameter_map.DynamicParameterMap"
    ]
    """<p>A map of extension parameters for the deployment.</p>"""
    tags: NotRequired["capo_appconfig.types.tag_map.TagMap"]
    """<p>The tags to assign to the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentParameters) -> dict:
    out: dict = {}
    if "dynamic_extension_parameters" in value:
        import capo_appconfig.types.dynamic_parameter_map

        out["DynamicExtensionParameters"] = (
            capo_appconfig.types.dynamic_parameter_map.serialize_json(
                value["dynamic_extension_parameters"]
            )
        )
    if "tags" in value:
        import capo_appconfig.types.tag_map

        out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DeploymentParameters:
    out: DeploymentParameters = {}  # type: ignore[typeddict-item]
    if data.get("DynamicExtensionParameters") is not None:
        import capo_appconfig.types.dynamic_parameter_map

        out["dynamic_extension_parameters"] = (
            capo_appconfig.types.dynamic_parameter_map.deserialize_json(
                data["DynamicExtensionParameters"]
            )
        )
    if data.get("Tags") is not None:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: DeploymentParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dynamic_extension_parameters" in value:
        out["dynamic_extension_parameters"] = "*** Sensitive Data Redacted ***"
    return out
