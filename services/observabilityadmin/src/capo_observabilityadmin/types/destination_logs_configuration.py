"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DestinationLogsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.deletion_protection
    import capo_observabilityadmin.types.log_group_name_configuration
    import capo_observabilityadmin.types.logs_backup_configuration
    import capo_observabilityadmin.types.logs_encryption_configuration
    import capo_observabilityadmin.types.tag_propagation_configuration


class DestinationLogsConfiguration(TypedDict, closed=True):
    logs_encryption_configuration: NotRequired[
        "capo_observabilityadmin.types.logs_encryption_configuration.LogsEncryptionConfiguration"
    ]
    """<p>The encryption configuration for centralization destination log groups.</p>"""
    backup_configuration: NotRequired[
        "capo_observabilityadmin.types.logs_backup_configuration.LogsBackupConfiguration"
    ]
    """<p>Configuration defining the backup region and an optional KMS key for the backup destination.</p>"""
    log_group_name_configuration: NotRequired[
        "capo_observabilityadmin.types.log_group_name_configuration.LogGroupNameConfiguration"
    ]
    """<p>Configuration that specifies a naming pattern for destination log groups created during centralization. The pattern supports static text and dynamic variables that are replaced with source attributes when log groups are created.</p>"""
    tag_propagation_configuration: NotRequired[
        "capo_observabilityadmin.types.tag_propagation_configuration.TagPropagationConfiguration"
    ]
    """<p>Specifies the tag propagation configuration for this centralization rule. When present, <code>LogGroupNameConfiguration</code> must use a <code>LogGroupNamePattern</code> that contains <code>${source.logGroup}</code>, <code>${source.accountId}</code>, and <code>${source.region}</code>.</p>"""
    log_group_deletion_protection: NotRequired[
        "capo_observabilityadmin.types.deletion_protection.DeletionProtection"
    ]
    """<p>Specifies whether this centralization rule enables deletion protection on the destination log groups that it creates. If you don't specify this setting, the rule doesn't enable deletion protection on the log groups that it creates. If you specify a backup Region in <code>BackupConfiguration</code>, the setting also applies to the log groups that the rule creates in the backup Region.</p> <p>When you set this to <code>ENABLED</code>, the rule enables deletion protection only on log groups that it creates after you enable the setting. It does not add deletion protection to log groups the rule created before you enabled the setting.</p> <p>If you remove this setting from the rule or delete the rule, deletion protection stays enabled on log groups that already have it. To delete one of these log groups, first disable deletion protection on the log group in the destination account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationLogsConfiguration) -> dict:
    out: dict = {}
    if "logs_encryption_configuration" in value:
        import capo_observabilityadmin.types.logs_encryption_configuration

        out["LogsEncryptionConfiguration"] = (
            capo_observabilityadmin.types.logs_encryption_configuration.serialize_json(
                value["logs_encryption_configuration"]
            )
        )
    if "backup_configuration" in value:
        import capo_observabilityadmin.types.logs_backup_configuration

        out["BackupConfiguration"] = (
            capo_observabilityadmin.types.logs_backup_configuration.serialize_json(
                value["backup_configuration"]
            )
        )
    if "log_group_name_configuration" in value:
        import capo_observabilityadmin.types.log_group_name_configuration

        out["LogGroupNameConfiguration"] = (
            capo_observabilityadmin.types.log_group_name_configuration.serialize_json(
                value["log_group_name_configuration"]
            )
        )
    if "tag_propagation_configuration" in value:
        import capo_observabilityadmin.types.tag_propagation_configuration

        out["TagPropagationConfiguration"] = (
            capo_observabilityadmin.types.tag_propagation_configuration.serialize_json(
                value["tag_propagation_configuration"]
            )
        )
    if "log_group_deletion_protection" in value:
        import capo_observabilityadmin.types.deletion_protection

        out["LogGroupDeletionProtection"] = (
            capo_observabilityadmin.types.deletion_protection.serialize_json(
                value["log_group_deletion_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationLogsConfiguration:
    out: DestinationLogsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LogsEncryptionConfiguration") is not None:
        import capo_observabilityadmin.types.logs_encryption_configuration

        out["logs_encryption_configuration"] = (
            capo_observabilityadmin.types.logs_encryption_configuration.deserialize_json(
                data["LogsEncryptionConfiguration"]
            )
        )
    if data.get("BackupConfiguration") is not None:
        import capo_observabilityadmin.types.logs_backup_configuration

        out["backup_configuration"] = (
            capo_observabilityadmin.types.logs_backup_configuration.deserialize_json(
                data["BackupConfiguration"]
            )
        )
    if data.get("LogGroupNameConfiguration") is not None:
        import capo_observabilityadmin.types.log_group_name_configuration

        out["log_group_name_configuration"] = (
            capo_observabilityadmin.types.log_group_name_configuration.deserialize_json(
                data["LogGroupNameConfiguration"]
            )
        )
    if data.get("TagPropagationConfiguration") is not None:
        import capo_observabilityadmin.types.tag_propagation_configuration

        out["tag_propagation_configuration"] = (
            capo_observabilityadmin.types.tag_propagation_configuration.deserialize_json(
                data["TagPropagationConfiguration"]
            )
        )
    if data.get("LogGroupDeletionProtection") is not None:
        import capo_observabilityadmin.types.deletion_protection

        out["log_group_deletion_protection"] = (
            capo_observabilityadmin.types.deletion_protection.deserialize_json(
                data["LogGroupDeletionProtection"]
            )
        )
    return out
