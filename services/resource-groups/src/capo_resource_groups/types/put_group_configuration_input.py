"""Generated from Smithy shape ``com.amazonaws.resourcegroups#PutGroupConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_configuration_list
    import capo_resource_groups.types.group_string


class PutGroupConfigurationInput(TypedDict, closed=True):
    group: NotRequired["capo_resource_groups.types.group_string.GroupString"]
    """<p>The name or Amazon resource name (ARN) of the resource group with the configuration that you want to update.</p>"""
    configuration: NotRequired[
        "capo_resource_groups.types.group_configuration_list.GroupConfigurationList"
    ]
    """<p>The new configuration to associate with the specified group. A configuration associates the resource group with an Amazon Web Services service and specifies how the service can interact with the resources in the group. A configuration is an array of <a>GroupConfigurationItem</a> elements.</p> <p>For information about the syntax of a service configuration, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html">Service configurations for Resource Groups</a>.</p> <note> <p>A resource group can contain either a <code>Configuration</code> or a <code>ResourceQuery</code>, but not both.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutGroupConfigurationInput) -> dict:
    out: dict = {}
    if "group" in value:
        out["Group"] = value["group"]
    if "configuration" in value:
        import capo_resource_groups.types.group_configuration_list

        out["Configuration"] = (
            capo_resource_groups.types.group_configuration_list.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutGroupConfigurationInput:
    out: PutGroupConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("Group") is not None:
        out["group"] = data["Group"]
    if data.get("Configuration") is not None:
        import capo_resource_groups.types.group_configuration_list

        out["configuration"] = (
            capo_resource_groups.types.group_configuration_list.deserialize_json(
                data["Configuration"]
            )
        )
    return out
