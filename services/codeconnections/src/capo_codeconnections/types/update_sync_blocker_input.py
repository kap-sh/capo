"""Generated from Smithy shape ``com.amazonaws.codeconnections#UpdateSyncBlockerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.id
    import capo_codeconnections.types.resolved_reason
    import capo_codeconnections.types.resource_name
    import capo_codeconnections.types.sync_configuration_type


class UpdateSyncBlockerInput(TypedDict, closed=True):
    id: "capo_codeconnections.types.id.Id"
    """<p>The ID of the sync blocker to be updated.</p>"""
    sync_type: (
        "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The sync type of the sync blocker to be updated.</p>"""
    resource_name: "capo_codeconnections.types.resource_name.ResourceName"
    """<p>The name of the resource for the sync blocker to be updated.</p>"""
    resolved_reason: "capo_codeconnections.types.resolved_reason.ResolvedReason"
    """<p>The reason for resolving the sync blocker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSyncBlockerInput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_codeconnections.types.sync_configuration_type

    out["SyncType"] = (
        capo_codeconnections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    out["ResourceName"] = value["resource_name"]
    out["ResolvedReason"] = value["resolved_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSyncBlockerInput:
    out: UpdateSyncBlockerInput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("SyncType") is not None:
        import capo_codeconnections.types.sync_configuration_type

        out["sync_type"] = (
            capo_codeconnections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        import typing

        out["sync_type"] = typing.cast(
            "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
            "",
        )
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    else:
        out["resource_name"] = ""
    if data.get("ResolvedReason") is not None:
        out["resolved_reason"] = data["ResolvedReason"]
    else:
        out["resolved_reason"] = ""
    return out
