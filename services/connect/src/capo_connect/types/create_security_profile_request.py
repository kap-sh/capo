"""Generated from Smithy shape ``com.amazonaws.connect#CreateSecurityProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.allowed_access_control_tags
    import capo_connect.types.allowed_ai_agents
    import capo_connect.types.allowed_flow_modules
    import capo_connect.types.applications
    import capo_connect.types.create_security_profile_name
    import capo_connect.types.granular_access_control_configuration
    import capo_connect.types.hierarchy_group_id
    import capo_connect.types.hierarchy_restricted_resource_list
    import capo_connect.types.instance_id
    import capo_connect.types.permissions_list
    import capo_connect.types.security_profile_description
    import capo_connect.types.tag_map
    import capo_connect.types.tag_restricted_resource_list


class CreateSecurityProfileRequest(TypedDict, closed=True):
    security_profile_name: (
        "capo_connect.types.create_security_profile_name.CreateSecurityProfileName"
    )
    """<p>The name of the security profile.</p>"""
    description: NotRequired[
        "capo_connect.types.security_profile_description.SecurityProfileDescription"
    ]
    """<p>The description of the security profile.</p>"""
    permissions: NotRequired["capo_connect.types.permissions_list.PermissionsList"]
    """<p>Permissions assigned to the security profile. For a list of valid permissions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html">List of security profile permissions</a>. </p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    allowed_access_control_tags: NotRequired[
        "capo_connect.types.allowed_access_control_tags.AllowedAccessControlTags"
    ]
    """<p>The list of tags that a security profile uses to restrict access to resources in Connect Customer.</p>"""
    tag_restricted_resources: NotRequired[
        "capo_connect.types.tag_restricted_resource_list.TagRestrictedResourceList"
    ]
    """<p>The list of resources that a security profile applies tag restrictions to in Connect Customer. For a list of Connect Customer resources that you can tag, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/tagging.html">Add tags to resources in Connect Customer</a> in the <i>Connect Customer Administrator Guide</i>. </p>"""
    applications: NotRequired["capo_connect.types.applications.Applications"]
    """<p>A list of third-party applications or MCP Servers that the security profile will give access to.</p>"""
    hierarchy_restricted_resources: NotRequired[
        "capo_connect.types.hierarchy_restricted_resource_list.HierarchyRestrictedResourceList"
    ]
    """<p>The list of resources that a security profile applies hierarchy restrictions to in Connect Customer. Following are acceptable ResourceNames: <code>User</code>.</p>"""
    allowed_access_control_hierarchy_group_id: NotRequired[
        "capo_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier of the hierarchy group that a security profile uses to restrict access to resources in Connect Customer.</p>"""
    allowed_flow_modules: NotRequired[
        "capo_connect.types.allowed_flow_modules.AllowedFlowModules"
    ]
    """<p> A list of Flow Modules an AI Agent can invoke as a tool. </p>"""
    allowed_ai_agents: NotRequired[
        "capo_connect.types.allowed_ai_agents.AllowedAIAgents"
    ]
    """<p>A list of AI agents that the security profile will give access to.</p>"""
    granular_access_control_configuration: NotRequired[
        "capo_connect.types.granular_access_control_configuration.GranularAccessControlConfiguration"
    ]
    """<p>The granular access control configuration for the security profile, including data table permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityProfileRequest) -> dict:
    out: dict = {}
    out["SecurityProfileName"] = value["security_profile_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "permissions" in value:
        import capo_connect.types.permissions_list

        out["Permissions"] = capo_connect.types.permissions_list.serialize_json(
            value["permissions"]
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "allowed_access_control_tags" in value:
        import capo_connect.types.allowed_access_control_tags

        out["AllowedAccessControlTags"] = (
            capo_connect.types.allowed_access_control_tags.serialize_json(
                value["allowed_access_control_tags"]
            )
        )
    if "tag_restricted_resources" in value:
        import capo_connect.types.tag_restricted_resource_list

        out["TagRestrictedResources"] = (
            capo_connect.types.tag_restricted_resource_list.serialize_json(
                value["tag_restricted_resources"]
            )
        )
    if "applications" in value:
        import capo_connect.types.applications

        out["Applications"] = capo_connect.types.applications.serialize_json(
            value["applications"]
        )
    if "hierarchy_restricted_resources" in value:
        import capo_connect.types.hierarchy_restricted_resource_list

        out["HierarchyRestrictedResources"] = (
            capo_connect.types.hierarchy_restricted_resource_list.serialize_json(
                value["hierarchy_restricted_resources"]
            )
        )
    if "allowed_access_control_hierarchy_group_id" in value:
        out["AllowedAccessControlHierarchyGroupId"] = value[
            "allowed_access_control_hierarchy_group_id"
        ]
    if "allowed_flow_modules" in value:
        import capo_connect.types.allowed_flow_modules

        out["AllowedFlowModules"] = (
            capo_connect.types.allowed_flow_modules.serialize_json(
                value["allowed_flow_modules"]
            )
        )
    if "allowed_ai_agents" in value:
        import capo_connect.types.allowed_ai_agents

        out["AllowedAIAgents"] = capo_connect.types.allowed_ai_agents.serialize_json(
            value["allowed_ai_agents"]
        )
    if "granular_access_control_configuration" in value:
        import capo_connect.types.granular_access_control_configuration

        out["GranularAccessControlConfiguration"] = (
            capo_connect.types.granular_access_control_configuration.serialize_json(
                value["granular_access_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSecurityProfileRequest:
    out: CreateSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecurityProfileName") is not None:
        out["security_profile_name"] = data["SecurityProfileName"]
    else:
        raise DeserializationError(
            "CreateSecurityProfileRequest.security_profile_name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Permissions") is not None:
        import capo_connect.types.permissions_list

        out["permissions"] = capo_connect.types.permissions_list.deserialize_json(
            data["Permissions"]
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("AllowedAccessControlTags") is not None:
        import capo_connect.types.allowed_access_control_tags

        out["allowed_access_control_tags"] = (
            capo_connect.types.allowed_access_control_tags.deserialize_json(
                data["AllowedAccessControlTags"]
            )
        )
    if data.get("TagRestrictedResources") is not None:
        import capo_connect.types.tag_restricted_resource_list

        out["tag_restricted_resources"] = (
            capo_connect.types.tag_restricted_resource_list.deserialize_json(
                data["TagRestrictedResources"]
            )
        )
    if data.get("Applications") is not None:
        import capo_connect.types.applications

        out["applications"] = capo_connect.types.applications.deserialize_json(
            data["Applications"]
        )
    if data.get("HierarchyRestrictedResources") is not None:
        import capo_connect.types.hierarchy_restricted_resource_list

        out["hierarchy_restricted_resources"] = (
            capo_connect.types.hierarchy_restricted_resource_list.deserialize_json(
                data["HierarchyRestrictedResources"]
            )
        )
    if data.get("AllowedAccessControlHierarchyGroupId") is not None:
        out["allowed_access_control_hierarchy_group_id"] = data[
            "AllowedAccessControlHierarchyGroupId"
        ]
    if data.get("AllowedFlowModules") is not None:
        import capo_connect.types.allowed_flow_modules

        out["allowed_flow_modules"] = (
            capo_connect.types.allowed_flow_modules.deserialize_json(
                data["AllowedFlowModules"]
            )
        )
    if data.get("AllowedAIAgents") is not None:
        import capo_connect.types.allowed_ai_agents

        out["allowed_ai_agents"] = (
            capo_connect.types.allowed_ai_agents.deserialize_json(
                data["AllowedAIAgents"]
            )
        )
    if data.get("GranularAccessControlConfiguration") is not None:
        import capo_connect.types.granular_access_control_configuration

        out["granular_access_control_configuration"] = (
            capo_connect.types.granular_access_control_configuration.deserialize_json(
                data["GranularAccessControlConfiguration"]
            )
        )
    return out
