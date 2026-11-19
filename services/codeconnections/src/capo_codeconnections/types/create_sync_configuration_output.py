"""Generated from Smithy shape ``com.amazonaws.codeconnections#CreateSyncConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.sync_configuration


class CreateSyncConfigurationOutput(TypedDict, closed=True):
    sync_configuration: (
        "capo_codeconnections.types.sync_configuration.SyncConfiguration"
    )
    """<p>The created sync configuration for the connection. A sync configuration allows Amazon Web Services to sync content from a Git repository to update a specified Amazon Web Services resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSyncConfigurationOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.sync_configuration

    out["SyncConfiguration"] = (
        capo_codeconnections.types.sync_configuration.serialize_aws_json_1_0(
            value["sync_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateSyncConfigurationOutput:
    out: CreateSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("SyncConfiguration") is not None:
        import capo_codeconnections.types.sync_configuration

        out["sync_configuration"] = (
            capo_codeconnections.types.sync_configuration.deserialize_aws_json_1_0(
                data["SyncConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSyncConfigurationOutput.sync_configuration required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSyncConfigurationOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.sync_configuration

    out["SyncConfiguration"] = (
        capo_codeconnections.types.sync_configuration.serialize_cbor(
            value["sync_configuration"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> CreateSyncConfigurationOutput:
    out: CreateSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("SyncConfiguration") is not None:
        import capo_codeconnections.types.sync_configuration

        out["sync_configuration"] = (
            capo_codeconnections.types.sync_configuration.deserialize_cbor(
                data["SyncConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSyncConfigurationOutput.sync_configuration required"
        )
    return out
