"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetGroupConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_configuration


class GetGroupConfigurationOutput(TypedDict, closed=True):
    group_configuration: NotRequired[
        "capo_resource_groups.types.group_configuration.GroupConfiguration"
    ]
    """<p>A structure that describes the service configuration attached with the specified group. For details about the service configuration syntax, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html">Service configurations for Resource Groups</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupConfigurationOutput) -> dict:
    out: dict = {}
    if "group_configuration" in value:
        import capo_resource_groups.types.group_configuration

        out["GroupConfiguration"] = (
            capo_resource_groups.types.group_configuration.serialize_json(
                value["group_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGroupConfigurationOutput:
    out: GetGroupConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("GroupConfiguration") is not None:
        import capo_resource_groups.types.group_configuration

        out["group_configuration"] = (
            capo_resource_groups.types.group_configuration.deserialize_json(
                data["GroupConfiguration"]
            )
        )
    return out
