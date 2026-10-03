"""Generated from Smithy shape ``com.amazonaws.resourcegroups#CreateGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group
    import capo_resource_groups.types.group_configuration
    import capo_resource_groups.types.resource_query
    import capo_resource_groups.types.tags


class CreateGroupOutput(TypedDict, closed=True):
    group: NotRequired["capo_resource_groups.types.group.Group"]
    """<p>The description of the resource group.</p>"""
    resource_query: NotRequired[
        "capo_resource_groups.types.resource_query.ResourceQuery"
    ]
    """<p>The resource query associated with the group. For more information about resource queries, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag">Create a tag-based group in Resource Groups</a>. </p>"""
    tags: NotRequired["capo_resource_groups.types.tags.Tags"]
    """<p>The tags associated with the group.</p>"""
    group_configuration: NotRequired[
        "capo_resource_groups.types.group_configuration.GroupConfiguration"
    ]
    """<p>The service configuration associated with the resource group. For details about the syntax of a service configuration, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html">Service configurations for Resource Groups</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupOutput) -> dict:
    out: dict = {}
    if "group" in value:
        import capo_resource_groups.types.group

        out["Group"] = capo_resource_groups.types.group.serialize_json(value["group"])
    if "resource_query" in value:
        import capo_resource_groups.types.resource_query

        out["ResourceQuery"] = capo_resource_groups.types.resource_query.serialize_json(
            value["resource_query"]
        )
    if "tags" in value:
        import capo_resource_groups.types.tags

        out["Tags"] = capo_resource_groups.types.tags.serialize_json(value["tags"])
    if "group_configuration" in value:
        import capo_resource_groups.types.group_configuration

        out["GroupConfiguration"] = (
            capo_resource_groups.types.group_configuration.serialize_json(
                value["group_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGroupOutput:
    out: CreateGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("Group") is not None:
        import capo_resource_groups.types.group

        out["group"] = capo_resource_groups.types.group.deserialize_json(data["Group"])
    if data.get("ResourceQuery") is not None:
        import capo_resource_groups.types.resource_query

        out["resource_query"] = (
            capo_resource_groups.types.resource_query.deserialize_json(
                data["ResourceQuery"]
            )
        )
    if data.get("Tags") is not None:
        import capo_resource_groups.types.tags

        out["tags"] = capo_resource_groups.types.tags.deserialize_json(data["Tags"])
    if data.get("GroupConfiguration") is not None:
        import capo_resource_groups.types.group_configuration

        out["group_configuration"] = (
            capo_resource_groups.types.group_configuration.deserialize_json(
                data["GroupConfiguration"]
            )
        )
    return out
