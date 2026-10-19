"""Generated from Smithy shape ``com.amazonaws.workspaces#StorageConnector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.storage_connector_status_enum
    import capo_workspaces.types.storage_connector_type_enum


class StorageConnector(TypedDict, closed=True):
    connector_type: (
        "capo_workspaces.types.storage_connector_type_enum.StorageConnectorTypeEnum"
    )
    """<p>The type of connector used to save user files.</p>"""
    status: (
        "capo_workspaces.types.storage_connector_status_enum.StorageConnectorStatusEnum"
    )
    """<p>Indicates if the storage connetor is enabled or disabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnector) -> dict:
    out: dict = {}
    import capo_workspaces.types.storage_connector_type_enum

    out["ConnectorType"] = (
        capo_workspaces.types.storage_connector_type_enum.serialize_aws_json_1_1(
            value["connector_type"]
        )
    )
    import capo_workspaces.types.storage_connector_status_enum

    out["Status"] = (
        capo_workspaces.types.storage_connector_status_enum.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageConnector:
    out: StorageConnector = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorType") is not None:
        import capo_workspaces.types.storage_connector_type_enum

        out["connector_type"] = (
            capo_workspaces.types.storage_connector_type_enum.deserialize_aws_json_1_1(
                data["ConnectorType"]
            )
        )
    else:
        import typing

        out["connector_type"] = typing.cast(
            "capo_workspaces.types.storage_connector_type_enum.StorageConnectorTypeEnum",
            "",
        )
    if data.get("Status") is not None:
        import capo_workspaces.types.storage_connector_status_enum

        out["status"] = (
            capo_workspaces.types.storage_connector_status_enum.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_workspaces.types.storage_connector_status_enum.StorageConnectorStatusEnum",
            "",
        )
    return out
