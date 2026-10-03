"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupConfigurationItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_groups.types.group_configuration_type
    import capo_resource_groups.types.group_parameter_list


class GroupConfigurationItem(TypedDict, closed=True):
    type: "capo_resource_groups.types.group_configuration_type.GroupConfigurationType"
    """<p>Specifies the type of group configuration item. Each item must have a unique value for <code>type</code>. For the list of types that you can specify for a configuration item, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types">Supported resource types and parameters</a>.</p>"""
    parameters: NotRequired[
        "capo_resource_groups.types.group_parameter_list.GroupParameterList"
    ]
    """<p>A collection of parameters for this group configuration item. For the list of parameters that you can use with each configuration item type, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types">Supported resource types and parameters</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupConfigurationItem) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    if "parameters" in value:
        import capo_resource_groups.types.group_parameter_list

        out["Parameters"] = (
            capo_resource_groups.types.group_parameter_list.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GroupConfigurationItem:
    out: GroupConfigurationItem = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("GroupConfigurationItem.type required")
    if data.get("Parameters") is not None:
        import capo_resource_groups.types.group_parameter_list

        out["parameters"] = (
            capo_resource_groups.types.group_parameter_list.deserialize_json(
                data["Parameters"]
            )
        )
    return out
