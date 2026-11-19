"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetSyncConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.sync_configuration


class GetSyncConfigurationOutput(TypedDict, closed=True):
    sync_configuration: (
        "capo_codeconnections.types.sync_configuration.SyncConfiguration"
    )
    """<p>The details about the sync configuration for which you want to retrieve information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSyncConfigurationOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.sync_configuration

    out["SyncConfiguration"] = (
        capo_codeconnections.types.sync_configuration.serialize_aws_json_1_0(
            value["sync_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSyncConfigurationOutput:
    out: GetSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("SyncConfiguration") is not None:
        import capo_codeconnections.types.sync_configuration

        out["sync_configuration"] = (
            capo_codeconnections.types.sync_configuration.deserialize_aws_json_1_0(
                data["SyncConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetSyncConfigurationOutput.sync_configuration required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSyncConfigurationOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.sync_configuration

    out["SyncConfiguration"] = (
        capo_codeconnections.types.sync_configuration.serialize_cbor(
            value["sync_configuration"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> GetSyncConfigurationOutput:
    out: GetSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("SyncConfiguration") is not None:
        import capo_codeconnections.types.sync_configuration

        out["sync_configuration"] = (
            capo_codeconnections.types.sync_configuration.deserialize_cbor(
                data["SyncConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetSyncConfigurationOutput.sync_configuration required"
        )
    return out
