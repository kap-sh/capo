"""Generated from Smithy shape ``com.amazonaws.resourcegroups#CreateGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_groups.types.create_group_name
    import capo_resource_groups.types.criticality
    import capo_resource_groups.types.description
    import capo_resource_groups.types.display_name
    import capo_resource_groups.types.group_configuration_list
    import capo_resource_groups.types.owner
    import capo_resource_groups.types.resource_query
    import capo_resource_groups.types.tags


class CreateGroupInput(TypedDict, closed=True):
    name: "capo_resource_groups.types.create_group_name.CreateGroupName"
    """<p>The name of the group, which is the identifier of the group in other operations. You can't change the name of a resource group after you create it. A resource group name can consist of letters, numbers, hyphens, periods, and underscores. The name cannot start with <code>AWS</code>, <code>aws</code>, or any other possible capitalization; these are reserved. A resource group name must be unique within each Amazon Web Services Region in your Amazon Web Services account.</p>"""
    description: NotRequired["capo_resource_groups.types.description.Description"]
    """<p>The description of the resource group. Descriptions can consist of letters, numbers, hyphens, underscores, periods, and spaces.</p>"""
    resource_query: NotRequired[
        "capo_resource_groups.types.resource_query.ResourceQuery"
    ]
    """<p>The resource query that determines which Amazon Web Services resources are members of this group. For more information about resource queries, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag">Create a tag-based group in Resource Groups</a>. </p> <note> <p>A resource group can contain either a <code>ResourceQuery</code> or a <code>Configuration</code>, but not both.</p> </note>"""
    tags: NotRequired["capo_resource_groups.types.tags.Tags"]
    """<p>The tags to add to the group. A tag is key-value pair string.</p>"""
    configuration: NotRequired[
        "capo_resource_groups.types.group_configuration_list.GroupConfigurationList"
    ]
    """<p>A configuration associates the resource group with an Amazon Web Services service and specifies how the service can interact with the resources in the group. A configuration is an array of <a>GroupConfigurationItem</a> elements. For details about the syntax of service configurations, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html">Service configurations for Resource Groups</a>.</p> <note> <p>A resource group can contain either a <code>Configuration</code> or a <code>ResourceQuery</code>, but not both.</p> </note>"""
    criticality: NotRequired["capo_resource_groups.types.criticality.Criticality"]
    """<p>The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.</p>"""
    owner: NotRequired["capo_resource_groups.types.owner.Owner"]
    """<p>A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization. </p>"""
    display_name: NotRequired["capo_resource_groups.types.display_name.DisplayName"]
    """<p>The name of the application group, which you can change at any time. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "resource_query" in value:
        import capo_resource_groups.types.resource_query

        out["ResourceQuery"] = capo_resource_groups.types.resource_query.serialize_json(
            value["resource_query"]
        )
    if "tags" in value:
        import capo_resource_groups.types.tags

        out["Tags"] = capo_resource_groups.types.tags.serialize_json(value["tags"])
    if "configuration" in value:
        import capo_resource_groups.types.group_configuration_list

        out["Configuration"] = (
            capo_resource_groups.types.group_configuration_list.serialize_json(
                value["configuration"]
            )
        )
    if "criticality" in value:
        out["Criticality"] = value["criticality"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> CreateGroupInput:
    out: CreateGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateGroupInput.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
    if data.get("Configuration") is not None:
        import capo_resource_groups.types.group_configuration_list

        out["configuration"] = (
            capo_resource_groups.types.group_configuration_list.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("Criticality") is not None:
        out["criticality"] = data["Criticality"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    return out
