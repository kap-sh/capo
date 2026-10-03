"""Generated from Smithy shape ``com.amazonaws.rds#OrderableDBInstanceOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.activity_stream_mode_list
    import capo_rds.types.availability_zone_list
    import capo_rds.types.available_additional_storage_volumes_option_list
    import capo_rds.types.available_processor_feature_list
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.double_optional
    import capo_rds.types.engine_mode_list
    import capo_rds.types.integer_optional
    import capo_rds.types.string
    import capo_rds.types.string_list


class OrderableDBInstanceOption(TypedDict, closed=True):
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The engine type of a DB instance.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The engine version of a DB instance.</p>"""
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The DB instance class for a DB instance.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model for a DB instance.</p>"""
    availability_zone_group: NotRequired["capo_rds.types.string.String"]
    """<p>The Availability Zone group for a DB instance.</p>"""
    availability_zones: NotRequired[
        "capo_rds.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>A list of Availability Zones for a DB instance.</p>"""
    multi_az_capable: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance is Multi-AZ capable.</p>"""
    read_replica_capable: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance can have a read replica.</p>"""
    vpc: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance is in a VPC.</p>"""
    supports_storage_encryption: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports encrypted storage.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type for a DB instance.</p>"""
    supports_iops: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports provisioned IOPS.</p>"""
    supports_storage_throughput: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports storage throughput.</p>"""
    supports_enhanced_monitoring: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.</p>"""
    supports_iam_database_authentication: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports IAM database authentication.</p>"""
    supports_performance_insights: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports Performance Insights.</p>"""
    min_storage_size: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>Minimum storage size for a DB instance.</p>"""
    max_storage_size: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>Maximum storage size for a DB instance.</p>"""
    min_iops_per_db_instance: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>Minimum total provisioned IOPS for a DB instance.</p>"""
    max_iops_per_db_instance: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>Maximum total provisioned IOPS for a DB instance.</p>"""
    min_iops_per_gib: NotRequired["capo_rds.types.double_optional.DoubleOptional"]
    """<p>Minimum provisioned IOPS per GiB for a DB instance.</p>"""
    max_iops_per_gib: NotRequired["capo_rds.types.double_optional.DoubleOptional"]
    """<p>Maximum provisioned IOPS per GiB for a DB instance.</p>"""
    min_storage_throughput_per_db_instance: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>Minimum storage throughput for a DB instance.</p>"""
    max_storage_throughput_per_db_instance: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>Maximum storage throughput for a DB instance.</p>"""
    min_storage_throughput_per_iops: NotRequired[
        "capo_rds.types.double_optional.DoubleOptional"
    ]
    """<p>Minimum storage throughput to provisioned IOPS ratio for a DB instance.</p>"""
    max_storage_throughput_per_iops: NotRequired[
        "capo_rds.types.double_optional.DoubleOptional"
    ]
    """<p>Maximum storage throughput to provisioned IOPS ratio for a DB instance.</p>"""
    available_processor_features: NotRequired[
        "capo_rds.types.available_processor_feature_list.AvailableProcessorFeatureList"
    ]
    """<p>A list of the available processor features for the DB instance class of a DB instance.</p>"""
    supported_engine_modes: NotRequired[
        "capo_rds.types.engine_mode_list.EngineModeList"
    ]
    """<p>A list of the supported DB engine modes.</p>"""
    supports_storage_autoscaling: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether Amazon RDS can automatically scale storage for DB instances that use the specified DB instance class.</p>"""
    supports_kerberos_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether a DB instance supports Kerberos Authentication.</p>"""
    outpost_capable: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports RDS on Outposts.</p> <p>For more information about RDS on Outposts, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html">Amazon RDS on Amazon Web Services Outposts</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    supported_activity_stream_modes: NotRequired[
        "capo_rds.types.activity_stream_mode_list.ActivityStreamModeList"
    ]
    """<p>The list of supported modes for Database Activity Streams. Aurora PostgreSQL returns the value <code>[sync, async]</code>. Aurora MySQL and RDS for Oracle return <code>[async]</code> only. If Database Activity Streams isn't supported, the return value is an empty list.</p>"""
    supports_global_databases: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether you can use Aurora global databases with a specific combination of other DB engine attributes.</p>"""
    supported_network_types: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The network types supported by the DB instance (<code>IPV4</code> or <code>DUAL</code>).</p> <p>A DB instance can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    supports_clusters: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether DB instances can be configured as a Multi-AZ DB cluster.</p> <p>For more information on Multi-AZ DB clusters, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html"> Multi-AZ deployments with two readable standby DB instances</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    supports_dedicated_log_volume: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports using a dedicated log volume (DLV).</p>"""
    supports_additional_storage_volumes: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the DB instance class supports additional storage volumes.</p>"""
    supports_http_endpoint: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports HTTP endpoints.</p>"""
    available_additional_storage_volumes_options: NotRequired[
        "capo_rds.types.available_additional_storage_volumes_option_list.AvailableAdditionalStorageVolumesOptionList"
    ]
    """<p>The available options for additional storage volumes for the DB instance class.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableDBInstanceOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "availability_zone_group" in value:
        pairs.append(
            (
                f"{key_prefix}AvailabilityZoneGroup",
                str(value["availability_zone_group"]),
            )
        )
    if "availability_zones" in value:
        import capo_rds.types.availability_zone_list

        capo_rds.types.availability_zone_list.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "multi_az_capable" in value:
        pairs.append(
            (
                f"{key_prefix}MultiAZCapable",
                "true" if value["multi_az_capable"] else "false",
            )
        )
    if "read_replica_capable" in value:
        pairs.append(
            (
                f"{key_prefix}ReadReplicaCapable",
                "true" if value["read_replica_capable"] else "false",
            )
        )
    if "vpc" in value:
        pairs.append((f"{key_prefix}Vpc", "true" if value["vpc"] else "false"))
    if "supports_storage_encryption" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsStorageEncryption",
                "true" if value["supports_storage_encryption"] else "false",
            )
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "supports_iops" in value:
        pairs.append(
            (f"{key_prefix}SupportsIops", "true" if value["supports_iops"] else "false")
        )
    if "supports_storage_throughput" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsStorageThroughput",
                "true" if value["supports_storage_throughput"] else "false",
            )
        )
    if "supports_enhanced_monitoring" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsEnhancedMonitoring",
                "true" if value["supports_enhanced_monitoring"] else "false",
            )
        )
    if "supports_iam_database_authentication" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsIAMDatabaseAuthentication",
                "true" if value["supports_iam_database_authentication"] else "false",
            )
        )
    if "supports_performance_insights" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsPerformanceInsights",
                "true" if value["supports_performance_insights"] else "false",
            )
        )
    if "min_storage_size" in value:
        pairs.append((f"{key_prefix}MinStorageSize", str(value["min_storage_size"])))
    if "max_storage_size" in value:
        pairs.append((f"{key_prefix}MaxStorageSize", str(value["max_storage_size"])))
    if "min_iops_per_db_instance" in value:
        pairs.append(
            (
                f"{key_prefix}MinIopsPerDbInstance",
                str(value["min_iops_per_db_instance"]),
            )
        )
    if "max_iops_per_db_instance" in value:
        pairs.append(
            (
                f"{key_prefix}MaxIopsPerDbInstance",
                str(value["max_iops_per_db_instance"]),
            )
        )
    if "min_iops_per_gib" in value:
        pairs.append(
            (
                f"{key_prefix}MinIopsPerGib",
                (
                    "NaN"
                    if value["min_iops_per_gib"] != value["min_iops_per_gib"]
                    else "Infinity"
                    if value["min_iops_per_gib"] == float("inf")
                    else "-Infinity"
                    if value["min_iops_per_gib"] == float("-inf")
                    else str(value["min_iops_per_gib"])
                ),
            )
        )
    if "max_iops_per_gib" in value:
        pairs.append(
            (
                f"{key_prefix}MaxIopsPerGib",
                (
                    "NaN"
                    if value["max_iops_per_gib"] != value["max_iops_per_gib"]
                    else "Infinity"
                    if value["max_iops_per_gib"] == float("inf")
                    else "-Infinity"
                    if value["max_iops_per_gib"] == float("-inf")
                    else str(value["max_iops_per_gib"])
                ),
            )
        )
    if "min_storage_throughput_per_db_instance" in value:
        pairs.append(
            (
                f"{key_prefix}MinStorageThroughputPerDbInstance",
                str(value["min_storage_throughput_per_db_instance"]),
            )
        )
    if "max_storage_throughput_per_db_instance" in value:
        pairs.append(
            (
                f"{key_prefix}MaxStorageThroughputPerDbInstance",
                str(value["max_storage_throughput_per_db_instance"]),
            )
        )
    if "min_storage_throughput_per_iops" in value:
        pairs.append(
            (
                f"{key_prefix}MinStorageThroughputPerIops",
                (
                    "NaN"
                    if value["min_storage_throughput_per_iops"]
                    != value["min_storage_throughput_per_iops"]
                    else "Infinity"
                    if value["min_storage_throughput_per_iops"] == float("inf")
                    else "-Infinity"
                    if value["min_storage_throughput_per_iops"] == float("-inf")
                    else str(value["min_storage_throughput_per_iops"])
                ),
            )
        )
    if "max_storage_throughput_per_iops" in value:
        pairs.append(
            (
                f"{key_prefix}MaxStorageThroughputPerIops",
                (
                    "NaN"
                    if value["max_storage_throughput_per_iops"]
                    != value["max_storage_throughput_per_iops"]
                    else "Infinity"
                    if value["max_storage_throughput_per_iops"] == float("inf")
                    else "-Infinity"
                    if value["max_storage_throughput_per_iops"] == float("-inf")
                    else str(value["max_storage_throughput_per_iops"])
                ),
            )
        )
    if "available_processor_features" in value:
        import capo_rds.types.available_processor_feature_list

        capo_rds.types.available_processor_feature_list.serialize_query(
            value["available_processor_features"],
            pairs,
            f"{key_prefix}AvailableProcessorFeatures",
        )
    if "supported_engine_modes" in value:
        import capo_rds.types.engine_mode_list

        capo_rds.types.engine_mode_list.serialize_query(
            value["supported_engine_modes"], pairs, f"{key_prefix}SupportedEngineModes"
        )
    if "supports_storage_autoscaling" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsStorageAutoscaling",
                "true" if value["supports_storage_autoscaling"] else "false",
            )
        )
    if "supports_kerberos_authentication" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsKerberosAuthentication",
                "true" if value["supports_kerberos_authentication"] else "false",
            )
        )
    if "outpost_capable" in value:
        pairs.append(
            (
                f"{key_prefix}OutpostCapable",
                "true" if value["outpost_capable"] else "false",
            )
        )
    if "supported_activity_stream_modes" in value:
        import capo_rds.types.activity_stream_mode_list

        capo_rds.types.activity_stream_mode_list.serialize_query(
            value["supported_activity_stream_modes"],
            pairs,
            f"{key_prefix}SupportedActivityStreamModes",
        )
    if "supports_global_databases" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsGlobalDatabases",
                "true" if value["supports_global_databases"] else "false",
            )
        )
    if "supported_network_types" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["supported_network_types"],
            pairs,
            f"{key_prefix}SupportedNetworkTypes",
        )
    if "supports_clusters" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsClusters",
                "true" if value["supports_clusters"] else "false",
            )
        )
    if "supports_dedicated_log_volume" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsDedicatedLogVolume",
                "true" if value["supports_dedicated_log_volume"] else "false",
            )
        )
    if "supports_additional_storage_volumes" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsAdditionalStorageVolumes",
                "true" if value["supports_additional_storage_volumes"] else "false",
            )
        )
    if "supports_http_endpoint" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsHttpEndpoint",
                "true" if value["supports_http_endpoint"] else "false",
            )
        )
    if "available_additional_storage_volumes_options" in value:
        import capo_rds.types.available_additional_storage_volumes_option_list

        capo_rds.types.available_additional_storage_volumes_option_list.serialize_query(
            value["available_additional_storage_volumes_options"],
            pairs,
            f"{key_prefix}AvailableAdditionalStorageVolumesOptions",
        )


def deserialize_query(el: Element) -> OrderableDBInstanceOption:
    out: OrderableDBInstanceOption = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_availability_zone_group = el.find("AvailabilityZoneGroup")
    if child_availability_zone_group is not None:
        out["availability_zone_group"] = str(child_availability_zone_group.text or "")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_rds.types.availability_zone_list

        out["availability_zones"] = (
            capo_rds.types.availability_zone_list.deserialize_query(
                child_availability_zones
            )
        )
    child_multi_az_capable = el.find("MultiAZCapable")
    if child_multi_az_capable is not None:
        out["multi_az_capable"] = (child_multi_az_capable.text or "").lower() == "true"
    child_read_replica_capable = el.find("ReadReplicaCapable")
    if child_read_replica_capable is not None:
        out["read_replica_capable"] = (
            child_read_replica_capable.text or ""
        ).lower() == "true"
    child_vpc = el.find("Vpc")
    if child_vpc is not None:
        out["vpc"] = (child_vpc.text or "").lower() == "true"
    child_supports_storage_encryption = el.find("SupportsStorageEncryption")
    if child_supports_storage_encryption is not None:
        out["supports_storage_encryption"] = (
            child_supports_storage_encryption.text or ""
        ).lower() == "true"
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_supports_iops = el.find("SupportsIops")
    if child_supports_iops is not None:
        out["supports_iops"] = (child_supports_iops.text or "").lower() == "true"
    child_supports_storage_throughput = el.find("SupportsStorageThroughput")
    if child_supports_storage_throughput is not None:
        out["supports_storage_throughput"] = (
            child_supports_storage_throughput.text or ""
        ).lower() == "true"
    child_supports_enhanced_monitoring = el.find("SupportsEnhancedMonitoring")
    if child_supports_enhanced_monitoring is not None:
        out["supports_enhanced_monitoring"] = (
            child_supports_enhanced_monitoring.text or ""
        ).lower() == "true"
    child_supports_iam_database_authentication = el.find(
        "SupportsIAMDatabaseAuthentication"
    )
    if child_supports_iam_database_authentication is not None:
        out["supports_iam_database_authentication"] = (
            child_supports_iam_database_authentication.text or ""
        ).lower() == "true"
    child_supports_performance_insights = el.find("SupportsPerformanceInsights")
    if child_supports_performance_insights is not None:
        out["supports_performance_insights"] = (
            child_supports_performance_insights.text or ""
        ).lower() == "true"
    child_min_storage_size = el.find("MinStorageSize")
    if child_min_storage_size is not None:
        out["min_storage_size"] = int(child_min_storage_size.text or "")
    child_max_storage_size = el.find("MaxStorageSize")
    if child_max_storage_size is not None:
        out["max_storage_size"] = int(child_max_storage_size.text or "")
    child_min_iops_per_db_instance = el.find("MinIopsPerDbInstance")
    if child_min_iops_per_db_instance is not None:
        out["min_iops_per_db_instance"] = int(child_min_iops_per_db_instance.text or "")
    child_max_iops_per_db_instance = el.find("MaxIopsPerDbInstance")
    if child_max_iops_per_db_instance is not None:
        out["max_iops_per_db_instance"] = int(child_max_iops_per_db_instance.text or "")
    child_min_iops_per_gib = el.find("MinIopsPerGib")
    if child_min_iops_per_gib is not None:
        out["min_iops_per_gib"] = float(child_min_iops_per_gib.text or "")
    child_max_iops_per_gib = el.find("MaxIopsPerGib")
    if child_max_iops_per_gib is not None:
        out["max_iops_per_gib"] = float(child_max_iops_per_gib.text or "")
    child_min_storage_throughput_per_db_instance = el.find(
        "MinStorageThroughputPerDbInstance"
    )
    if child_min_storage_throughput_per_db_instance is not None:
        out["min_storage_throughput_per_db_instance"] = int(
            child_min_storage_throughput_per_db_instance.text or ""
        )
    child_max_storage_throughput_per_db_instance = el.find(
        "MaxStorageThroughputPerDbInstance"
    )
    if child_max_storage_throughput_per_db_instance is not None:
        out["max_storage_throughput_per_db_instance"] = int(
            child_max_storage_throughput_per_db_instance.text or ""
        )
    child_min_storage_throughput_per_iops = el.find("MinStorageThroughputPerIops")
    if child_min_storage_throughput_per_iops is not None:
        out["min_storage_throughput_per_iops"] = float(
            child_min_storage_throughput_per_iops.text or ""
        )
    child_max_storage_throughput_per_iops = el.find("MaxStorageThroughputPerIops")
    if child_max_storage_throughput_per_iops is not None:
        out["max_storage_throughput_per_iops"] = float(
            child_max_storage_throughput_per_iops.text or ""
        )
    child_available_processor_features = el.find("AvailableProcessorFeatures")
    if child_available_processor_features is not None:
        import capo_rds.types.available_processor_feature_list

        out["available_processor_features"] = (
            capo_rds.types.available_processor_feature_list.deserialize_query(
                child_available_processor_features
            )
        )
    child_supported_engine_modes = el.find("SupportedEngineModes")
    if child_supported_engine_modes is not None:
        import capo_rds.types.engine_mode_list

        out["supported_engine_modes"] = (
            capo_rds.types.engine_mode_list.deserialize_query(
                child_supported_engine_modes
            )
        )
    child_supports_storage_autoscaling = el.find("SupportsStorageAutoscaling")
    if child_supports_storage_autoscaling is not None:
        out["supports_storage_autoscaling"] = (
            child_supports_storage_autoscaling.text or ""
        ).lower() == "true"
    child_supports_kerberos_authentication = el.find("SupportsKerberosAuthentication")
    if child_supports_kerberos_authentication is not None:
        out["supports_kerberos_authentication"] = (
            child_supports_kerberos_authentication.text or ""
        ).lower() == "true"
    child_outpost_capable = el.find("OutpostCapable")
    if child_outpost_capable is not None:
        out["outpost_capable"] = (child_outpost_capable.text or "").lower() == "true"
    child_supported_activity_stream_modes = el.find("SupportedActivityStreamModes")
    if child_supported_activity_stream_modes is not None:
        import capo_rds.types.activity_stream_mode_list

        out["supported_activity_stream_modes"] = (
            capo_rds.types.activity_stream_mode_list.deserialize_query(
                child_supported_activity_stream_modes
            )
        )
    child_supports_global_databases = el.find("SupportsGlobalDatabases")
    if child_supports_global_databases is not None:
        out["supports_global_databases"] = (
            child_supports_global_databases.text or ""
        ).lower() == "true"
    child_supported_network_types = el.find("SupportedNetworkTypes")
    if child_supported_network_types is not None:
        import capo_rds.types.string_list

        out["supported_network_types"] = capo_rds.types.string_list.deserialize_query(
            child_supported_network_types
        )
    child_supports_clusters = el.find("SupportsClusters")
    if child_supports_clusters is not None:
        out["supports_clusters"] = (
            child_supports_clusters.text or ""
        ).lower() == "true"
    child_supports_dedicated_log_volume = el.find("SupportsDedicatedLogVolume")
    if child_supports_dedicated_log_volume is not None:
        out["supports_dedicated_log_volume"] = (
            child_supports_dedicated_log_volume.text or ""
        ).lower() == "true"
    child_supports_additional_storage_volumes = el.find(
        "SupportsAdditionalStorageVolumes"
    )
    if child_supports_additional_storage_volumes is not None:
        out["supports_additional_storage_volumes"] = (
            child_supports_additional_storage_volumes.text or ""
        ).lower() == "true"
    child_supports_http_endpoint = el.find("SupportsHttpEndpoint")
    if child_supports_http_endpoint is not None:
        out["supports_http_endpoint"] = (
            child_supports_http_endpoint.text or ""
        ).lower() == "true"
    child_available_additional_storage_volumes_options = el.find(
        "AvailableAdditionalStorageVolumesOptions"
    )
    if child_available_additional_storage_volumes_options is not None:
        import capo_rds.types.available_additional_storage_volumes_option_list

        out["available_additional_storage_volumes_options"] = (
            capo_rds.types.available_additional_storage_volumes_option_list.deserialize_query(
                child_available_additional_storage_volumes_options
            )
        )
    return out
