"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceMaintenanceOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.auto_recovery_enum


class InstanceMaintenanceOptionsRequest(TypedDict, closed=True):
    auto_recovery: NotRequired[
        "capo_workspaces_instances.types.auto_recovery_enum.AutoRecoveryEnum"
    ]
    """<p>Enables or disables automatic instance recovery.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceMaintenanceOptionsRequest) -> dict:
    out: dict = {}
    if "auto_recovery" in value:
        import capo_workspaces_instances.types.auto_recovery_enum

        out["AutoRecovery"] = (
            capo_workspaces_instances.types.auto_recovery_enum.serialize_aws_json_1_0(
                value["auto_recovery"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceMaintenanceOptionsRequest:
    out: InstanceMaintenanceOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutoRecovery") is not None:
        import capo_workspaces_instances.types.auto_recovery_enum

        out["auto_recovery"] = (
            capo_workspaces_instances.types.auto_recovery_enum.deserialize_aws_json_1_0(
                data["AutoRecovery"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceMaintenanceOptionsRequest) -> dict:
    out: dict = {}
    if "auto_recovery" in value:
        import capo_workspaces_instances.types.auto_recovery_enum

        out["AutoRecovery"] = (
            capo_workspaces_instances.types.auto_recovery_enum.serialize_cbor(
                value["auto_recovery"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> InstanceMaintenanceOptionsRequest:
    out: InstanceMaintenanceOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutoRecovery") is not None:
        import capo_workspaces_instances.types.auto_recovery_enum

        out["auto_recovery"] = (
            capo_workspaces_instances.types.auto_recovery_enum.deserialize_cbor(
                data["AutoRecovery"]
            )
        )
    return out
