"""Generated from Smithy shape ``com.amazonaws.workspaces#SelfservicePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.reconnect_enum


class SelfservicePermissions(TypedDict, closed=True):
    restart_workspace: NotRequired["capo_workspaces.types.reconnect_enum.ReconnectEnum"]
    """<p>Specifies whether users can restart their WorkSpace.</p>"""
    increase_volume_size: NotRequired[
        "capo_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can increase the volume size of the drives on their WorkSpace.</p>"""
    change_compute_type: NotRequired[
        "capo_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can change the compute type (bundle) for their WorkSpace.</p>"""
    switch_running_mode: NotRequired[
        "capo_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can switch the running mode of their WorkSpace.</p>"""
    rebuild_workspace: NotRequired["capo_workspaces.types.reconnect_enum.ReconnectEnum"]
    """<p>Specifies whether users can rebuild the operating system of a WorkSpace to its original state.</p>"""
    nested_virtualization: NotRequired[
        "capo_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can enable or disable nested virtualization on their WorkSpace. The default value is <code>DISABLED</code>. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/nested-virtualization.html">Nested virtualization for Amazon WorkSpaces</a>.</p>"""
    enable_end_user_advisor: NotRequired[
        "capo_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can use End User Advisor in the WorkSpaces client for Windows to see their session health and get recommended actions for common issues. The default value is <code>ENABLED</code>. For more information, see Proactive troubleshooting for your WorkSpaces users.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelfservicePermissions) -> dict:
    out: dict = {}
    if "restart_workspace" in value:
        import capo_workspaces.types.reconnect_enum

        out["RestartWorkspace"] = (
            capo_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["restart_workspace"]
            )
        )
    if "increase_volume_size" in value:
        import capo_workspaces.types.reconnect_enum

        out["IncreaseVolumeSize"] = (
            capo_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["increase_volume_size"]
            )
        )
    if "change_compute_type" in value:
        import capo_workspaces.types.reconnect_enum

        out["ChangeComputeType"] = (
            capo_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["change_compute_type"]
            )
        )
    if "switch_running_mode" in value:
        import capo_workspaces.types.reconnect_enum

        out["SwitchRunningMode"] = (
            capo_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["switch_running_mode"]
            )
        )
    if "rebuild_workspace" in value:
        import capo_workspaces.types.reconnect_enum

        out["RebuildWorkspace"] = (
            capo_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["rebuild_workspace"]
            )
        )
    if "nested_virtualization" in value:
        import capo_workspaces.types.reconnect_enum

        out["NestedVirtualization"] = (
            capo_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["nested_virtualization"]
            )
        )
    if "enable_end_user_advisor" in value:
        import capo_workspaces.types.reconnect_enum

        out["EnableEndUserAdvisor"] = (
            capo_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["enable_end_user_advisor"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SelfservicePermissions:
    out: SelfservicePermissions = {}  # type: ignore[typeddict-item]
    if data.get("RestartWorkspace") is not None:
        import capo_workspaces.types.reconnect_enum

        out["restart_workspace"] = (
            capo_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["RestartWorkspace"]
            )
        )
    if data.get("IncreaseVolumeSize") is not None:
        import capo_workspaces.types.reconnect_enum

        out["increase_volume_size"] = (
            capo_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["IncreaseVolumeSize"]
            )
        )
    if data.get("ChangeComputeType") is not None:
        import capo_workspaces.types.reconnect_enum

        out["change_compute_type"] = (
            capo_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["ChangeComputeType"]
            )
        )
    if data.get("SwitchRunningMode") is not None:
        import capo_workspaces.types.reconnect_enum

        out["switch_running_mode"] = (
            capo_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["SwitchRunningMode"]
            )
        )
    if data.get("RebuildWorkspace") is not None:
        import capo_workspaces.types.reconnect_enum

        out["rebuild_workspace"] = (
            capo_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["RebuildWorkspace"]
            )
        )
    if data.get("NestedVirtualization") is not None:
        import capo_workspaces.types.reconnect_enum

        out["nested_virtualization"] = (
            capo_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["NestedVirtualization"]
            )
        )
    if data.get("EnableEndUserAdvisor") is not None:
        import capo_workspaces.types.reconnect_enum

        out["enable_end_user_advisor"] = (
            capo_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["EnableEndUserAdvisor"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SelfservicePermissions) -> dict:
    out: dict = {}
    if "restart_workspace" in value:
        import capo_workspaces.types.reconnect_enum

        out["RestartWorkspace"] = capo_workspaces.types.reconnect_enum.serialize_cbor(
            value["restart_workspace"]
        )
    if "increase_volume_size" in value:
        import capo_workspaces.types.reconnect_enum

        out["IncreaseVolumeSize"] = capo_workspaces.types.reconnect_enum.serialize_cbor(
            value["increase_volume_size"]
        )
    if "change_compute_type" in value:
        import capo_workspaces.types.reconnect_enum

        out["ChangeComputeType"] = capo_workspaces.types.reconnect_enum.serialize_cbor(
            value["change_compute_type"]
        )
    if "switch_running_mode" in value:
        import capo_workspaces.types.reconnect_enum

        out["SwitchRunningMode"] = capo_workspaces.types.reconnect_enum.serialize_cbor(
            value["switch_running_mode"]
        )
    if "rebuild_workspace" in value:
        import capo_workspaces.types.reconnect_enum

        out["RebuildWorkspace"] = capo_workspaces.types.reconnect_enum.serialize_cbor(
            value["rebuild_workspace"]
        )
    if "nested_virtualization" in value:
        import capo_workspaces.types.reconnect_enum

        out["NestedVirtualization"] = (
            capo_workspaces.types.reconnect_enum.serialize_cbor(
                value["nested_virtualization"]
            )
        )
    if "enable_end_user_advisor" in value:
        import capo_workspaces.types.reconnect_enum

        out["EnableEndUserAdvisor"] = (
            capo_workspaces.types.reconnect_enum.serialize_cbor(
                value["enable_end_user_advisor"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SelfservicePermissions:
    out: SelfservicePermissions = {}  # type: ignore[typeddict-item]
    if data.get("RestartWorkspace") is not None:
        import capo_workspaces.types.reconnect_enum

        out["restart_workspace"] = (
            capo_workspaces.types.reconnect_enum.deserialize_cbor(
                data["RestartWorkspace"]
            )
        )
    if data.get("IncreaseVolumeSize") is not None:
        import capo_workspaces.types.reconnect_enum

        out["increase_volume_size"] = (
            capo_workspaces.types.reconnect_enum.deserialize_cbor(
                data["IncreaseVolumeSize"]
            )
        )
    if data.get("ChangeComputeType") is not None:
        import capo_workspaces.types.reconnect_enum

        out["change_compute_type"] = (
            capo_workspaces.types.reconnect_enum.deserialize_cbor(
                data["ChangeComputeType"]
            )
        )
    if data.get("SwitchRunningMode") is not None:
        import capo_workspaces.types.reconnect_enum

        out["switch_running_mode"] = (
            capo_workspaces.types.reconnect_enum.deserialize_cbor(
                data["SwitchRunningMode"]
            )
        )
    if data.get("RebuildWorkspace") is not None:
        import capo_workspaces.types.reconnect_enum

        out["rebuild_workspace"] = (
            capo_workspaces.types.reconnect_enum.deserialize_cbor(
                data["RebuildWorkspace"]
            )
        )
    if data.get("NestedVirtualization") is not None:
        import capo_workspaces.types.reconnect_enum

        out["nested_virtualization"] = (
            capo_workspaces.types.reconnect_enum.deserialize_cbor(
                data["NestedVirtualization"]
            )
        )
    if data.get("EnableEndUserAdvisor") is not None:
        import capo_workspaces.types.reconnect_enum

        out["enable_end_user_advisor"] = (
            capo_workspaces.types.reconnect_enum.deserialize_cbor(
                data["EnableEndUserAdvisor"]
            )
        )
    return out
