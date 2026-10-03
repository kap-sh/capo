"""Generated from Smithy shape ``com.amazonaws.docdb#CreateDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean_optional
    import capo_docdb.types.integer_optional
    import capo_docdb.types.string
    import capo_docdb.types.tag_list


class CreateDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>"""
    db_instance_class: NotRequired["capo_docdb.types.string.String"]
    """<p>The compute and memory capacity of the instance; for example, <code>db.r5.large</code>. </p>"""
    engine: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the database engine to be used for this instance.</p> <p>Valid value: <code>docdb</code> </p>"""
    availability_zone: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon EC2 Availability Zone that the instance is created in. </p> <p>Default: A random, system-chosen Availability Zone in the endpoint's Amazon Web Services Region.</p> <p>Example: <code>us-east-1d</code> </p>"""
    preferred_maintenance_window: NotRequired["capo_docdb.types.string.String"]
    """<p>The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week. </p> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p>Constraints: Minimum 30-minute window.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.</p> <p>Default: <code>false</code> </p>"""
    tags: NotRequired["capo_docdb.types.tag_list.TagList"]
    """<p>The tags to be assigned to the instance. You can assign up to 10 tags to an instance.</p>"""
    db_cluster_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The identifier of the cluster that the instance will belong to.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.</p>"""
    promotion_tier: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p>A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.</p> <p>Default: 1</p> <p>Valid values: 0-15</p>"""
    enable_performance_insights: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates whether to enable Performance Insights for the DB Instance. For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/performance-insights.html">Using Amazon Performance Insights</a>.</p>"""
    performance_insights_kms_key_id: NotRequired["capo_docdb.types.string.String"]
    """<p>The KMS key identifier for encryption of Performance Insights data.</p> <p>The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you do not specify a value for PerformanceInsightsKMSKeyId, then Amazon DocumentDB uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services region.</p>"""
    ca_certificate_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The CA certificate identifier to use for the DB instance's server certificate.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/ca_cert_rotation.html">Updating Your Amazon DocumentDB TLS Certificates</a> and <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/security.encryption.ssl.html"> Encrypting Data in Transit</a> in the <i>Amazon DocumentDB Developer Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
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
    if "tags" in value:
        import capo_docdb.types.tag_list

        capo_docdb.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
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
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )


def deserialize_query(el: Element) -> CreateDBInstanceMessage:
    out: CreateDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
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
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_docdb.types.tag_list

        out["tags"] = capo_docdb.types.tag_list.deserialize_query(child_tags)
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
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
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    return out
