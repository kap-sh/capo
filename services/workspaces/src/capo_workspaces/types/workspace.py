"""Generated from Smithy shape ``com.amazonaws.workspaces#Workspace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.boolean_object
    import capo_workspaces.types.bundle_id
    import capo_workspaces.types.computer_name
    import capo_workspaces.types.data_replication_settings
    import capo_workspaces.types.description
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.ip_address
    import capo_workspaces.types.ipv6_address
    import capo_workspaces.types.modification_state_list
    import capo_workspaces.types.related_workspaces
    import capo_workspaces.types.standby_workspaces_properties_list
    import capo_workspaces.types.subnet_id
    import capo_workspaces.types.user_name
    import capo_workspaces.types.volume_encryption_key
    import capo_workspaces.types.workspace_error_code
    import capo_workspaces.types.workspace_id
    import capo_workspaces.types.workspace_name
    import capo_workspaces.types.workspace_properties
    import capo_workspaces.types.workspace_state


class Workspace(TypedDict, closed=True):
    workspace_id: NotRequired["capo_workspaces.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the WorkSpace.</p>"""
    directory_id: NotRequired["capo_workspaces.types.directory_id.DirectoryId"]
    """<p>The identifier of the Directory Service directory for the WorkSpace.</p>"""
    user_name: NotRequired["capo_workspaces.types.user_name.UserName"]
    """<p>The user for the WorkSpace.</p>"""
    ip_address: NotRequired["capo_workspaces.types.ip_address.IpAddress"]
    """<p>The IP address of the WorkSpace.</p>"""
    ipv6_address: NotRequired["capo_workspaces.types.ipv6_address.Ipv6Address"]
    """<p>The IPv6 address of the WorkSpace.</p>"""
    state: NotRequired["capo_workspaces.types.workspace_state.WorkspaceState"]
    """<p>The operational state of the WorkSpace.</p> <ul> <li> <p> <code>PENDING</code> – The WorkSpace is in a waiting state (for example, the WorkSpace is being created).</p> </li> <li> <p> <code>AVAILABLE</code> – The WorkSpace is running and has passed the health checks.</p> </li> <li> <p> <code>IMPAIRED</code> – Refer to <code>UNHEALTHY</code> state.</p> </li> <li> <p> <code>UNHEALTHY</code> – The WorkSpace is not responding to health checks.</p> </li> <li> <p> <code>REBOOTING</code> – The WorkSpace is being rebooted (restarted).</p> </li> <li> <p> <code>STARTING</code> – The WorkSpace is starting up and health checks are being run.</p> </li> <li> <p> <code>REBUILDING</code> – The WorkSpace is being rebuilt.</p> </li> <li> <p> <code>RESTORING</code> – The WorkSpace is being restored.</p> </li> <li> <p> <code>MAINTENANCE</code> – The WorkSpace is undergoing scheduled maintenance by Amazon Web Services.</p> </li> <li> <p> <code>ADMIN_MAINTENANCE</code> – The WorkSpace is undergoing maintenance by the WorkSpaces administrator.</p> </li> <li> <p> <code>TERMINATING</code> – The WorkSpace is being deleted.</p> </li> <li> <p> <code>TERMINATED</code> – The WorkSpace has been deleted.</p> </li> <li> <p> <code>SUSPENDED</code> – The WorkSpace has been suspended for image creation.</p> </li> <li> <p> <code>UPDATING</code> – The WorkSpace is undergoing an update.</p> </li> <li> <p> <code>STOPPING</code> – The WorkSpace is being stopped.</p> </li> <li> <p> <code>STOPPED</code> – The WorkSpace has been stopped.</p> </li> <li> <p> <code>ERROR </code> – The WorkSpace is an error state (for example, an error occurred during startup).</p> </li> </ul> <note> <p>After a WorkSpace is terminated, the <code>TERMINATED</code> state is returned only briefly before the WorkSpace directory metadata is cleaned up, so this state is rarely returned. To confirm that a WorkSpace is terminated, check for the WorkSpace ID by using <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html"> DescribeWorkSpaces</a>. If the WorkSpace ID isn't returned, then the WorkSpace has been successfully terminated.</p> </note>"""
    bundle_id: NotRequired["capo_workspaces.types.bundle_id.BundleId"]
    """<p>The identifier of the bundle used to create the WorkSpace.</p>"""
    subnet_id: NotRequired["capo_workspaces.types.subnet_id.SubnetId"]
    """<p>The identifier of the subnet for the WorkSpace.</p>"""
    error_message: NotRequired["capo_workspaces.types.description.Description"]
    """<p>The text of the error message that is returned if the WorkSpace cannot be created.</p>"""
    error_code: NotRequired[
        "capo_workspaces.types.workspace_error_code.WorkspaceErrorCode"
    ]
    """<p>The error code that is returned if the WorkSpace cannot be created.</p>"""
    computer_name: NotRequired["capo_workspaces.types.computer_name.ComputerName"]
    """<p>The name of the WorkSpace, as seen by the operating system. The format of this name varies. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspaces-tutorials.html"> Launch a WorkSpace</a>. </p>"""
    volume_encryption_key: NotRequired[
        "capo_workspaces.types.volume_encryption_key.VolumeEncryptionKey"
    ]
    """<p>The ARN of the symmetric KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.</p>"""
    user_volume_encryption_enabled: NotRequired[
        "capo_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether the data stored on the user volume is encrypted.</p>"""
    root_volume_encryption_enabled: NotRequired[
        "capo_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether the data stored on the root volume is encrypted.</p>"""
    workspace_name: NotRequired["capo_workspaces.types.workspace_name.WorkspaceName"]
    """<p>The name of the user-decoupled WorkSpace.</p>"""
    workspace_properties: NotRequired[
        "capo_workspaces.types.workspace_properties.WorkspaceProperties"
    ]
    """<p>The properties of the WorkSpace.</p>"""
    modification_states: NotRequired[
        "capo_workspaces.types.modification_state_list.ModificationStateList"
    ]
    """<p>The modification states of the WorkSpace.</p>"""
    related_workspaces: NotRequired[
        "capo_workspaces.types.related_workspaces.RelatedWorkspaces"
    ]
    """<p>The standby WorkSpace or primary WorkSpace related to the specified WorkSpace.</p>"""
    data_replication_settings: NotRequired[
        "capo_workspaces.types.data_replication_settings.DataReplicationSettings"
    ]
    """<p>Indicates the settings of the data replication.</p>"""
    standby_workspaces_properties: NotRequired[
        "capo_workspaces.types.standby_workspaces_properties_list.StandbyWorkspacesPropertiesList"
    ]
    """<p>The properties of the standby WorkSpace</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Workspace) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["WorkspaceId"] = value["workspace_id"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "ipv6_address" in value:
        out["Ipv6Address"] = value["ipv6_address"]
    if "state" in value:
        import capo_workspaces.types.workspace_state

        out["State"] = capo_workspaces.types.workspace_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "computer_name" in value:
        out["ComputerName"] = value["computer_name"]
    if "volume_encryption_key" in value:
        out["VolumeEncryptionKey"] = value["volume_encryption_key"]
    if "user_volume_encryption_enabled" in value:
        out["UserVolumeEncryptionEnabled"] = value["user_volume_encryption_enabled"]
    if "root_volume_encryption_enabled" in value:
        out["RootVolumeEncryptionEnabled"] = value["root_volume_encryption_enabled"]
    if "workspace_name" in value:
        out["WorkspaceName"] = value["workspace_name"]
    if "workspace_properties" in value:
        import capo_workspaces.types.workspace_properties

        out["WorkspaceProperties"] = (
            capo_workspaces.types.workspace_properties.serialize_aws_json_1_1(
                value["workspace_properties"]
            )
        )
    if "modification_states" in value:
        import capo_workspaces.types.modification_state_list

        out["ModificationStates"] = (
            capo_workspaces.types.modification_state_list.serialize_aws_json_1_1(
                value["modification_states"]
            )
        )
    if "related_workspaces" in value:
        import capo_workspaces.types.related_workspaces

        out["RelatedWorkspaces"] = (
            capo_workspaces.types.related_workspaces.serialize_aws_json_1_1(
                value["related_workspaces"]
            )
        )
    if "data_replication_settings" in value:
        import capo_workspaces.types.data_replication_settings

        out["DataReplicationSettings"] = (
            capo_workspaces.types.data_replication_settings.serialize_aws_json_1_1(
                value["data_replication_settings"]
            )
        )
    if "standby_workspaces_properties" in value:
        import capo_workspaces.types.standby_workspaces_properties_list

        out["StandbyWorkspacesProperties"] = (
            capo_workspaces.types.standby_workspaces_properties_list.serialize_aws_json_1_1(
                value["standby_workspaces_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Workspace:
    out: Workspace = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceId") is not None:
        out["workspace_id"] = data["WorkspaceId"]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("Ipv6Address") is not None:
        out["ipv6_address"] = data["Ipv6Address"]
    if data.get("State") is not None:
        import capo_workspaces.types.workspace_state

        out["state"] = capo_workspaces.types.workspace_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("BundleId") is not None:
        out["bundle_id"] = data["BundleId"]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ComputerName") is not None:
        out["computer_name"] = data["ComputerName"]
    if data.get("VolumeEncryptionKey") is not None:
        out["volume_encryption_key"] = data["VolumeEncryptionKey"]
    if data.get("UserVolumeEncryptionEnabled") is not None:
        out["user_volume_encryption_enabled"] = data["UserVolumeEncryptionEnabled"]
    if data.get("RootVolumeEncryptionEnabled") is not None:
        out["root_volume_encryption_enabled"] = data["RootVolumeEncryptionEnabled"]
    if data.get("WorkspaceName") is not None:
        out["workspace_name"] = data["WorkspaceName"]
    if data.get("WorkspaceProperties") is not None:
        import capo_workspaces.types.workspace_properties

        out["workspace_properties"] = (
            capo_workspaces.types.workspace_properties.deserialize_aws_json_1_1(
                data["WorkspaceProperties"]
            )
        )
    if data.get("ModificationStates") is not None:
        import capo_workspaces.types.modification_state_list

        out["modification_states"] = (
            capo_workspaces.types.modification_state_list.deserialize_aws_json_1_1(
                data["ModificationStates"]
            )
        )
    if data.get("RelatedWorkspaces") is not None:
        import capo_workspaces.types.related_workspaces

        out["related_workspaces"] = (
            capo_workspaces.types.related_workspaces.deserialize_aws_json_1_1(
                data["RelatedWorkspaces"]
            )
        )
    if data.get("DataReplicationSettings") is not None:
        import capo_workspaces.types.data_replication_settings

        out["data_replication_settings"] = (
            capo_workspaces.types.data_replication_settings.deserialize_aws_json_1_1(
                data["DataReplicationSettings"]
            )
        )
    if data.get("StandbyWorkspacesProperties") is not None:
        import capo_workspaces.types.standby_workspaces_properties_list

        out["standby_workspaces_properties"] = (
            capo_workspaces.types.standby_workspaces_properties_list.deserialize_aws_json_1_1(
                data["StandbyWorkspacesProperties"]
            )
        )
    return out
