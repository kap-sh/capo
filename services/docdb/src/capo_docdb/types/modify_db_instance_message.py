"""Generated from Smithy shape ``com.amazonaws.docdb#ModifyDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean
    import capo_docdb.types.boolean_optional
    import capo_docdb.types.integer_optional
    import capo_docdb.types.string


class ModifyDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The instance identifier. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBInstance</code>.</p> </li> </ul>"""
    db_instance_class: NotRequired["capo_docdb.types.string.String"]
    """<p>The new compute and memory capacity of the instance; for example, <code>db.r5.large</code>. Not all instance classes are available in all Amazon Web Services Regions. </p> <p>If you modify the instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless <code>ApplyImmediately</code> is specified as <code>true</code> for this request. </p> <p>Default: Uses existing setting.</p>"""
    apply_immediately: NotRequired["capo_docdb.types.boolean.Boolean"]
    """<p>Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the instance. </p> <p> If this parameter is set to <code>false</code>, changes to the instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next reboot.</p> <p>Default: <code>false</code> </p>"""
    preferred_maintenance_window: NotRequired["capo_docdb.types.string.String"]
    """<p>The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn't result in an outage except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, changing this parameter causes a reboot of the instance. If you are moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure that pending changes are applied.</p> <p>Default: Uses existing setting.</p> <p>Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p>Constraints: Must be at least 30 minutes.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.</p>"""
    new_db_instance_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p> The new instance identifier for the instance when renaming an instance. When you change the instance identifier, an instance reboot occurs immediately if you set <code>Apply Immediately</code> to <code>true</code>. It occurs during the next maintenance window if you set <code>Apply Immediately</code> to <code>false</code>. This value is stored as a lowercase string. </p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>"""
    ca_certificate_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>Indicates the certificate that needs to be associated with the instance.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.</p>"""
    promotion_tier: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p>A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.</p> <p>Default: 1</p> <p>Valid values: 0-15</p>"""
    enable_performance_insights: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates whether to enable Performance Insights for the DB Instance. For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/performance-insights.html">Using Amazon Performance Insights</a>.</p>"""
    performance_insights_kms_key_id: NotRequired["capo_docdb.types.string.String"]
    """<p>The KMS key identifier for encryption of Performance Insights data.</p> <p>The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you do not specify a value for PerformanceInsightsKMSKeyId, then Amazon DocumentDB uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services region.</p>"""
    certificate_rotation_restart: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate.</p> <p>By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not updated until the DB instance is restarted.</p> <important> <p>Set this parameter only if you are <i>not</i> using SSL/TLS to connect to the DB instance.</p> </important> <p>If you are using SSL/TLS to connect to the DB instance, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/ca_cert_rotation.html">Updating Your Amazon DocumentDB TLS Certificates</a> and <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/security.encryption.ssl.html"> Encrypting Data in Transit</a> in the <i>Amazon DocumentDB Developer Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{key_prefix}ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "new_db_instance_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}NewDBInstanceIdentifier",
                str(value["new_db_instance_identifier"]),
            )
        )
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )
    if "promotion_tier" in value:
        pairs.append((f"{key_prefix}PromotionTier", str(value["promotion_tier"])))
    if "enable_performance_insights" in value:
        pairs.append(
            (
                f"{key_prefix}EnablePerformanceInsights",
                "true" if value["enable_performance_insights"] else "false",
            )
        )
    if "performance_insights_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}PerformanceInsightsKMSKeyId",
                str(value["performance_insights_kms_key_id"]),
            )
        )
    if "certificate_rotation_restart" in value:
        pairs.append(
            (
                f"{key_prefix}CertificateRotationRestart",
                "true" if value["certificate_rotation_restart"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyDBInstanceMessage:
    out: ModifyDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_new_db_instance_identifier = el.find("NewDBInstanceIdentifier")
    if child_new_db_instance_identifier is not None:
        out["new_db_instance_identifier"] = str(
            child_new_db_instance_identifier.text or ""
        )
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_promotion_tier = el.find("PromotionTier")
    if child_promotion_tier is not None:
        out["promotion_tier"] = int(child_promotion_tier.text or "")
    child_enable_performance_insights = el.find("EnablePerformanceInsights")
    if child_enable_performance_insights is not None:
        out["enable_performance_insights"] = (
            child_enable_performance_insights.text or ""
        ).lower() == "true"
    child_performance_insights_kms_key_id = el.find("PerformanceInsightsKMSKeyId")
    if child_performance_insights_kms_key_id is not None:
        out["performance_insights_kms_key_id"] = str(
            child_performance_insights_kms_key_id.text or ""
        )
    child_certificate_rotation_restart = el.find("CertificateRotationRestart")
    if child_certificate_rotation_restart is not None:
        out["certificate_rotation_restart"] = (
            child_certificate_rotation_restart.text or ""
        ).lower() == "true"
    return out
