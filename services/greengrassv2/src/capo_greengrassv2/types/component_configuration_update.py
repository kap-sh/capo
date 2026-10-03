"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_configuration_path_list
    import capo_greengrassv2.types.component_configuration_string


class ComponentConfigurationUpdate(TypedDict, closed=True):
    merge: NotRequired[
        "capo_greengrassv2.types.component_configuration_string.ComponentConfigurationString"
    ]
    """<p>A serialized JSON string that contains the configuration object to merge to target devices. The core device merges this configuration with the component's existing configuration. If this is the first time a component deploys on a device, the core device merges this configuration with the component's default configuration. This means that the core device keeps it's existing configuration for keys and values that you don't specify in this object. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#merge-configuration-update">Merge configuration updates</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""
    reset: NotRequired[
        "capo_greengrassv2.types.component_configuration_path_list.ComponentConfigurationPathList"
    ]
    """<p>The list of configuration nodes to reset to default values on target devices. Use JSON pointers to specify each node to reset. JSON pointers start with a forward slash (<code>/</code>) and use forward slashes to separate the key for each level in the object. For more information, see the <a href="https://tools.ietf.org/html/rfc6901">JSON pointer specification</a> and <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#reset-configuration-update">Reset configuration updates</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConfigurationUpdate) -> dict:
    out: dict = {}
    if "merge" in value:
        out["merge"] = value["merge"]
    if "reset" in value:
        import capo_greengrassv2.types.component_configuration_path_list

        out["reset"] = (
            capo_greengrassv2.types.component_configuration_path_list.serialize_json(
                value["reset"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentConfigurationUpdate:
    out: ComponentConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("merge") is not None:
        out["merge"] = data["merge"]
    if data.get("reset") is not None:
        import capo_greengrassv2.types.component_configuration_path_list

        out["reset"] = (
            capo_greengrassv2.types.component_configuration_path_list.deserialize_json(
                data["reset"]
            )
        )
    return out
