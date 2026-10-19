"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_encryption_configuration
    import capo_securitylake.types.data_lake_lifecycle_configuration
    import capo_securitylake.types.data_lake_replication_configuration
    import capo_securitylake.types.region


class DataLakeConfiguration(TypedDict, closed=True):
    region: "capo_securitylake.types.region.Region"
    """<p>The Amazon Web Services Regions where Security Lake is automatically enabled.</p>"""
    encryption_configuration: NotRequired[
        "capo_securitylake.types.data_lake_encryption_configuration.DataLakeEncryptionConfiguration"
    ]
    """<p>Provides encryption details of Amazon Security Lake object.</p>"""
    lifecycle_configuration: NotRequired[
        "capo_securitylake.types.data_lake_lifecycle_configuration.DataLakeLifecycleConfiguration"
    ]
    """<p>Provides lifecycle details of Amazon Security Lake object.</p>"""
    replication_configuration: NotRequired[
        "capo_securitylake.types.data_lake_replication_configuration.DataLakeReplicationConfiguration"
    ]
    """<p>Provides replication details of Amazon Security Lake object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeConfiguration) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    if "encryption_configuration" in value:
        import capo_securitylake.types.data_lake_encryption_configuration

        out["encryptionConfiguration"] = (
            capo_securitylake.types.data_lake_encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "lifecycle_configuration" in value:
        import capo_securitylake.types.data_lake_lifecycle_configuration

        out["lifecycleConfiguration"] = (
            capo_securitylake.types.data_lake_lifecycle_configuration.serialize_json(
                value["lifecycle_configuration"]
            )
        )
    if "replication_configuration" in value:
        import capo_securitylake.types.data_lake_replication_configuration

        out["replicationConfiguration"] = (
            capo_securitylake.types.data_lake_replication_configuration.serialize_json(
                value["replication_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeConfiguration:
    out: DataLakeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("encryptionConfiguration") is not None:
        import capo_securitylake.types.data_lake_encryption_configuration

        out["encryption_configuration"] = (
            capo_securitylake.types.data_lake_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("lifecycleConfiguration") is not None:
        import capo_securitylake.types.data_lake_lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_securitylake.types.data_lake_lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    if data.get("replicationConfiguration") is not None:
        import capo_securitylake.types.data_lake_replication_configuration

        out["replication_configuration"] = (
            capo_securitylake.types.data_lake_replication_configuration.deserialize_json(
                data["replicationConfiguration"]
            )
        )
    return out
