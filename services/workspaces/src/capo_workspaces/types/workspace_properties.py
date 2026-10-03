"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.boolean_object
    import capo_workspaces.types.compute
    import capo_workspaces.types.global_accelerator_for_work_space
    import capo_workspaces.types.operating_system_name
    import capo_workspaces.types.protocol_list
    import capo_workspaces.types.root_volume_size_gib
    import capo_workspaces.types.running_mode
    import capo_workspaces.types.running_mode_auto_stop_timeout_in_minutes
    import capo_workspaces.types.user_volume_size_gib


class WorkspaceProperties(TypedDict, closed=True):
    running_mode: NotRequired["capo_workspaces.types.running_mode.RunningMode"]
    """<p>The running mode. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html">Manage the WorkSpace Running Mode</a>.</p> <note> <p>The <code>MANUAL</code> value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see <a href="http://aws.amazon.com/workspaces/core/">Amazon WorkSpaces Core</a>.</p> </note> <p>Review your running mode to ensure you are using one that is optimal for your needs and budget. For more information on switching running modes, see <a href="http://aws.amazon.com/workspaces-family/workspaces/faqs/#:~:text=Can%20I%20switch%20between%20hourly%20and%20monthly%20billing%20on%20WorkSpaces%20Personal%3F"> Can I switch between hourly and monthly billing?</a> </p>"""
    running_mode_auto_stop_timeout_in_minutes: NotRequired[
        "capo_workspaces.types.running_mode_auto_stop_timeout_in_minutes.RunningModeAutoStopTimeoutInMinutes"
    ]
    """<p>The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.</p>"""
    root_volume_size_gib: NotRequired[
        "capo_workspaces.types.root_volume_size_gib.RootVolumeSizeGib"
    ]
    """<p>The size of the root volume. For important information about how to modify the size of the root and user volumes, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html">Modify a WorkSpace</a>.</p>"""
    user_volume_size_gib: NotRequired[
        "capo_workspaces.types.user_volume_size_gib.UserVolumeSizeGib"
    ]
    """<p>The size of the user storage. For important information about how to modify the size of the root and user volumes, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html">Modify a WorkSpace</a>.</p>"""
    compute_type_name: NotRequired["capo_workspaces.types.compute.Compute"]
    """<p>The compute type. For more information, see <a href="http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles">Amazon WorkSpaces Bundles</a>.</p>"""
    protocols: NotRequired["capo_workspaces.types.protocol_list.ProtocolList"]
    """<p>The protocol. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-protocols.html"> Protocols for Amazon WorkSpaces</a>.</p> <note> <ul> <li> <p>Only available for WorkSpaces created with PCoIP bundles.</p> </li> <li> <p>The <code>Protocols</code> property is case sensitive. Ensure you use <code>PCOIP</code> or <code>DCV</code> (formerly WSP).</p> </li> <li> <p>Unavailable for Windows 7 WorkSpaces and WorkSpaces using GPU-based bundles (Graphics, GraphicsPro, Graphics.g4dn, GraphicsPro.g4dn, Graphics.g6, and Graphics.g7).</p> </li> </ul> </note>"""
    operating_system_name: NotRequired[
        "capo_workspaces.types.operating_system_name.OperatingSystemName"
    ]
    """<p>The name of the operating system.</p>"""
    global_accelerator: NotRequired[
        "capo_workspaces.types.global_accelerator_for_work_space.GlobalAcceleratorForWorkSpace"
    ]
    """<p>Indicates the Global Accelerator properties.</p>"""
    nested_virtualization_enabled: NotRequired[
        "capo_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Specifies whether nested virtualization is enabled for the WorkSpace.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/nested-virtualization.html">Nested virtualization for Amazon WorkSpaces</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceProperties) -> dict:
    out: dict = {}
    if "running_mode" in value:
        import capo_workspaces.types.running_mode

        out["RunningMode"] = capo_workspaces.types.running_mode.serialize_aws_json_1_1(
            value["running_mode"]
        )
    if "running_mode_auto_stop_timeout_in_minutes" in value:
        out["RunningModeAutoStopTimeoutInMinutes"] = value[
            "running_mode_auto_stop_timeout_in_minutes"
        ]
    if "root_volume_size_gib" in value:
        out["RootVolumeSizeGib"] = value["root_volume_size_gib"]
    if "user_volume_size_gib" in value:
        out["UserVolumeSizeGib"] = value["user_volume_size_gib"]
    if "compute_type_name" in value:
        import capo_workspaces.types.compute

        out["ComputeTypeName"] = capo_workspaces.types.compute.serialize_aws_json_1_1(
            value["compute_type_name"]
        )
    if "protocols" in value:
        import capo_workspaces.types.protocol_list

        out["Protocols"] = capo_workspaces.types.protocol_list.serialize_aws_json_1_1(
            value["protocols"]
        )
    if "operating_system_name" in value:
        import capo_workspaces.types.operating_system_name

        out["OperatingSystemName"] = (
            capo_workspaces.types.operating_system_name.serialize_aws_json_1_1(
                value["operating_system_name"]
            )
        )
    if "global_accelerator" in value:
        import capo_workspaces.types.global_accelerator_for_work_space

        out["GlobalAccelerator"] = (
            capo_workspaces.types.global_accelerator_for_work_space.serialize_aws_json_1_1(
                value["global_accelerator"]
            )
        )
    if "nested_virtualization_enabled" in value:
        out["NestedVirtualizationEnabled"] = value["nested_virtualization_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceProperties:
    out: WorkspaceProperties = {}  # type: ignore[typeddict-item]
    if data.get("RunningMode") is not None:
        import capo_workspaces.types.running_mode

        out["running_mode"] = (
            capo_workspaces.types.running_mode.deserialize_aws_json_1_1(
                data["RunningMode"]
            )
        )
    if data.get("RunningModeAutoStopTimeoutInMinutes") is not None:
        out["running_mode_auto_stop_timeout_in_minutes"] = data[
            "RunningModeAutoStopTimeoutInMinutes"
        ]
    if data.get("RootVolumeSizeGib") is not None:
        out["root_volume_size_gib"] = data["RootVolumeSizeGib"]
    if data.get("UserVolumeSizeGib") is not None:
        out["user_volume_size_gib"] = data["UserVolumeSizeGib"]
    if data.get("ComputeTypeName") is not None:
        import capo_workspaces.types.compute

        out["compute_type_name"] = (
            capo_workspaces.types.compute.deserialize_aws_json_1_1(
                data["ComputeTypeName"]
            )
        )
    if data.get("Protocols") is not None:
        import capo_workspaces.types.protocol_list

        out["protocols"] = capo_workspaces.types.protocol_list.deserialize_aws_json_1_1(
            data["Protocols"]
        )
    if data.get("OperatingSystemName") is not None:
        import capo_workspaces.types.operating_system_name

        out["operating_system_name"] = (
            capo_workspaces.types.operating_system_name.deserialize_aws_json_1_1(
                data["OperatingSystemName"]
            )
        )
    if data.get("GlobalAccelerator") is not None:
        import capo_workspaces.types.global_accelerator_for_work_space

        out["global_accelerator"] = (
            capo_workspaces.types.global_accelerator_for_work_space.deserialize_aws_json_1_1(
                data["GlobalAccelerator"]
            )
        )
    if data.get("NestedVirtualizationEnabled") is not None:
        out["nested_virtualization_enabled"] = data["NestedVirtualizationEnabled"]
    return out
