"""Generated from Smithy shape ``com.amazonaws.rds#DBEngineVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.ca_certificate_identifiers_list
    import capo_rds.types.character_set
    import capo_rds.types.custom_db_engine_version_ami
    import capo_rds.types.custom_db_engine_version_manifest
    import capo_rds.types.engine_mode_list
    import capo_rds.types.feature_name_list
    import capo_rds.types.log_type_list
    import capo_rds.types.serverless_v2_features_support
    import capo_rds.types.string
    import capo_rds.types.string_list
    import capo_rds.types.supported_character_sets_list
    import capo_rds.types.supported_timezones_list
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list
    import capo_rds.types.valid_upgrade_target_list


class DBEngineVersion(TypedDict, closed=True):
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database engine.</p>"""
    major_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The major engine version of the CEV.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version number of the database engine.</p>"""
    database_installation_files_s3_bucket_name: NotRequired[
        "capo_rds.types.string.String"
    ]
    """<p>The name of the Amazon S3 bucket that contains your database installation files.</p>"""
    database_installation_files_s3_prefix: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon S3 directory that contains the database installation files. If not specified, then no prefix is assumed.</p>"""
    database_installation_files: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The database installation files (ISO and EXE) that were uploaded to Amazon S3 and used to import the database engine version to Amazon RDS. Returned for RDS for SQL Server engine versions (<code>sqlserver-ee</code>, <code>sqlserver-se</code>, and <code>sqlserver-dev-ee</code>) created from customer-supplied installation media.</p>"""
    custom_db_engine_version_manifest: NotRequired[
        "capo_rds.types.custom_db_engine_version_manifest.CustomDBEngineVersionManifest"
    ]
    """<p>JSON string that lists the installation files and parameters that RDS Custom uses to create a custom engine version (CEV). RDS Custom applies the patches in the order in which they're listed in the manifest. You can set the Oracle home, Oracle base, and UNIX/Linux user and group using the installation parameters. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.preparing.html#custom-cev.preparing.manifest.fields">JSON fields in the CEV manifest</a> in the <i>Amazon RDS User Guide</i>. </p>"""
    db_parameter_group_family: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB parameter group family for the database engine.</p>"""
    db_engine_description: NotRequired["capo_rds.types.string.String"]
    """<p>The description of the database engine.</p>"""
    db_engine_version_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN of the custom engine version.</p>"""
    db_engine_version_description: NotRequired["capo_rds.types.string.String"]
    """<p>The description of the database engine version.</p>"""
    default_character_set: NotRequired["capo_rds.types.character_set.CharacterSet"]
    """<p>The default character set for new instances of this engine version, if the <code>CharacterSetName</code> parameter of the CreateDBInstance API isn't specified.</p>"""
    failure_reason: NotRequired["capo_rds.types.string.String"]
    """<p>The reason that the custom engine version creation failed with an <code>incompatible-installation-media</code> status. Applicable to RDS for SQL Server engine versions (<code>sqlserver-ee</code>, <code>sqlserver-se</code>, and <code>sqlserver-dev-ee</code>).</p>"""
    image: NotRequired[
        "capo_rds.types.custom_db_engine_version_ami.CustomDBEngineVersionAMI"
    ]
    """<p>The EC2 image</p>"""
    db_engine_media_type: NotRequired["capo_rds.types.string.String"]
    """<p>The source of the installation media for this engine version. A value of <code>Customer Provided</code> indicates that the engine version was created from customer-supplied installation media using <code>CreateCustomDBEngineVersion</code>. Applicable to RDS Custom for SQL Server and to RDS for SQL Server engine versions (<code>sqlserver-ee</code> and <code>sqlserver-se</code> with the <code>bring-your-own-media</code> license model, and <code>sqlserver-dev-ee</code>).</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for an encrypted CEV. This parameter is required for RDS Custom, but optional for Amazon RDS.</p>"""
    create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The creation time of the DB engine version.</p>"""
    supported_character_sets: NotRequired[
        "capo_rds.types.supported_character_sets_list.SupportedCharacterSetsList"
    ]
    """<p>A list of the character sets supported by this engine for the <code>CharacterSetName</code> parameter of the <code>CreateDBInstance</code> operation.</p>"""
    supported_nchar_character_sets: NotRequired[
        "capo_rds.types.supported_character_sets_list.SupportedCharacterSetsList"
    ]
    """<p>A list of the character sets supported by the Oracle DB engine for the <code>NcharCharacterSetName</code> parameter of the <code>CreateDBInstance</code> operation.</p>"""
    valid_upgrade_target: NotRequired[
        "capo_rds.types.valid_upgrade_target_list.ValidUpgradeTargetList"
    ]
    """<p>A list of engine versions that this database engine version can be upgraded to.</p>"""
    supported_timezones: NotRequired[
        "capo_rds.types.supported_timezones_list.SupportedTimezonesList"
    ]
    """<p>A list of the time zones supported by this engine for the <code>Timezone</code> parameter of the <code>CreateDBInstance</code> action.</p>"""
    exportable_log_types: NotRequired["capo_rds.types.log_type_list.LogTypeList"]
    """<p>The types of logs that the database engine has available for export to CloudWatch Logs.</p>"""
    supports_log_exports_to_cloudwatch_logs: NotRequired[
        "capo_rds.types.boolean.Boolean"
    ]
    """<p>Indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.</p>"""
    supports_read_replica: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the database engine version supports read replicas.</p>"""
    supported_engine_modes: NotRequired[
        "capo_rds.types.engine_mode_list.EngineModeList"
    ]
    """<p>A list of the supported DB engine modes.</p>"""
    supported_feature_names: NotRequired[
        "capo_rds.types.feature_name_list.FeatureNameList"
    ]
    """<p>A list of features supported by the DB engine.</p> <p>The supported features vary by DB engine and DB engine version.</p> <p>To determine the supported features for a specific DB engine and DB engine version using the CLI, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine &lt;engine_name&gt; --engine-version &lt;engine_version&gt;</code> </p> <p>For example, to determine the supported features for RDS for PostgreSQL version 13.3 using the CLI, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --engine-version 13.3</code> </p> <p>The supported features are listed under <code>SupportedFeatureNames</code> in the output.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the DB engine version, either <code>available</code> or <code>deprecated</code>.</p>"""
    supports_parallel_query: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether you can use Aurora parallel query with a specific DB engine version.</p>"""
    supports_global_databases: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether you can use Aurora global databases with a specific DB engine version.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]
    supports_babelfish: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the engine version supports Babelfish for Aurora PostgreSQL.</p>"""
    supports_limitless_database: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB engine version supports Aurora Limitless Database.</p>"""
    supports_certificate_rotation_without_restart: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the engine version supports rotating the server certificate without rebooting the DB instance.</p>"""
    supported_ca_certificate_identifiers: NotRequired[
        "capo_rds.types.ca_certificate_identifiers_list.CACertificateIdentifiersList"
    ]
    """<p>A list of the supported CA certificate identifiers.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"> Using SSL/TLS to encrypt a connection to a DB cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    supports_local_write_forwarding: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the DB engine version supports forwarding write operations from reader DB instances to the writer DB instance in the DB cluster. By default, write operations aren't allowed on reader DB instances.</p> <p>Valid for: Aurora DB clusters only</p>"""
    supports_integrations: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB engine version supports zero-ETL integrations with Amazon Redshift.</p>"""
    serverless_v2_features_support: NotRequired[
        "capo_rds.types.serverless_v2_features_support.ServerlessV2FeaturesSupport"
    ]
    """<p>Specifies any Aurora Serverless v2 properties or limits that differ between Aurora engine versions. You can test the values of this attribute when deciding which Aurora version to use in a new or upgraded DB cluster. You can also retrieve the version of an existing DB cluster and check whether that version supports certain Aurora Serverless v2 features before you attempt to use those features. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBEngineVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{key_prefix}MajorEngineVersion", str(value["major_engine_version"]))
        )
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "database_installation_files_s3_bucket_name" in value:
        pairs.append(
            (
                f"{key_prefix}DatabaseInstallationFilesS3BucketName",
                str(value["database_installation_files_s3_bucket_name"]),
            )
        )
    if "database_installation_files_s3_prefix" in value:
        pairs.append(
            (
                f"{key_prefix}DatabaseInstallationFilesS3Prefix",
                str(value["database_installation_files_s3_prefix"]),
            )
        )
    if "database_installation_files" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["database_installation_files"],
            pairs,
            f"{key_prefix}DatabaseInstallationFiles",
        )
    if "custom_db_engine_version_manifest" in value:
        pairs.append(
            (
                f"{key_prefix}CustomDBEngineVersionManifest",
                str(value["custom_db_engine_version_manifest"]),
            )
        )
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{key_prefix}DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
        )
    if "db_engine_description" in value:
        pairs.append(
            (f"{key_prefix}DBEngineDescription", str(value["db_engine_description"]))
        )
    if "db_engine_version_arn" in value:
        pairs.append(
            (f"{key_prefix}DBEngineVersionArn", str(value["db_engine_version_arn"]))
        )
    if "db_engine_version_description" in value:
        pairs.append(
            (
                f"{key_prefix}DBEngineVersionDescription",
                str(value["db_engine_version_description"]),
            )
        )
    if "default_character_set" in value:
        import capo_rds.types.character_set

        capo_rds.types.character_set.serialize_query(
            value["default_character_set"], pairs, f"{key_prefix}DefaultCharacterSet"
        )
    if "failure_reason" in value:
        pairs.append((f"{key_prefix}FailureReason", str(value["failure_reason"])))
    if "image" in value:
        import capo_rds.types.custom_db_engine_version_ami

        capo_rds.types.custom_db_engine_version_ami.serialize_query(
            value["image"], pairs, f"{key_prefix}Image"
        )
    if "db_engine_media_type" in value:
        pairs.append(
            (f"{key_prefix}DBEngineMediaType", str(value["db_engine_media_type"]))
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KMSKeyId", str(value["kms_key_id"])))
    if "create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "supported_character_sets" in value:
        import capo_rds.types.supported_character_sets_list

        capo_rds.types.supported_character_sets_list.serialize_query(
            value["supported_character_sets"],
            pairs,
            f"{key_prefix}SupportedCharacterSets",
        )
    if "supported_nchar_character_sets" in value:
        import capo_rds.types.supported_character_sets_list

        capo_rds.types.supported_character_sets_list.serialize_query(
            value["supported_nchar_character_sets"],
            pairs,
            f"{key_prefix}SupportedNcharCharacterSets",
        )
    if "valid_upgrade_target" in value:
        import capo_rds.types.valid_upgrade_target_list

        capo_rds.types.valid_upgrade_target_list.serialize_query(
            value["valid_upgrade_target"], pairs, f"{key_prefix}ValidUpgradeTarget"
        )
    if "supported_timezones" in value:
        import capo_rds.types.supported_timezones_list

        capo_rds.types.supported_timezones_list.serialize_query(
            value["supported_timezones"], pairs, f"{key_prefix}SupportedTimezones"
        )
    if "exportable_log_types" in value:
        import capo_rds.types.log_type_list

        capo_rds.types.log_type_list.serialize_query(
            value["exportable_log_types"], pairs, f"{key_prefix}ExportableLogTypes"
        )
    if "supports_log_exports_to_cloudwatch_logs" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsLogExportsToCloudwatchLogs",
                "true" if value["supports_log_exports_to_cloudwatch_logs"] else "false",
            )
        )
    if "supports_read_replica" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsReadReplica",
                "true" if value["supports_read_replica"] else "false",
            )
        )
    if "supported_engine_modes" in value:
        import capo_rds.types.engine_mode_list

        capo_rds.types.engine_mode_list.serialize_query(
            value["supported_engine_modes"], pairs, f"{key_prefix}SupportedEngineModes"
        )
    if "supported_feature_names" in value:
        import capo_rds.types.feature_name_list

        capo_rds.types.feature_name_list.serialize_query(
            value["supported_feature_names"],
            pairs,
            f"{key_prefix}SupportedFeatureNames",
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "supports_parallel_query" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsParallelQuery",
                "true" if value["supports_parallel_query"] else "false",
            )
        )
    if "supports_global_databases" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsGlobalDatabases",
                "true" if value["supports_global_databases"] else "false",
            )
        )
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )
    if "supports_babelfish" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsBabelfish",
                "true" if value["supports_babelfish"] else "false",
            )
        )
    if "supports_limitless_database" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsLimitlessDatabase",
                "true" if value["supports_limitless_database"] else "false",
            )
        )
    if "supports_certificate_rotation_without_restart" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsCertificateRotationWithoutRestart",
                "true"
                if value["supports_certificate_rotation_without_restart"]
                else "false",
            )
        )
    if "supported_ca_certificate_identifiers" in value:
        import capo_rds.types.ca_certificate_identifiers_list

        capo_rds.types.ca_certificate_identifiers_list.serialize_query(
            value["supported_ca_certificate_identifiers"],
            pairs,
            f"{key_prefix}SupportedCACertificateIdentifiers",
        )
    if "supports_local_write_forwarding" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsLocalWriteForwarding",
                "true" if value["supports_local_write_forwarding"] else "false",
            )
        )
    if "supports_integrations" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsIntegrations",
                "true" if value["supports_integrations"] else "false",
            )
        )
    if "serverless_v2_features_support" in value:
        import capo_rds.types.serverless_v2_features_support

        capo_rds.types.serverless_v2_features_support.serialize_query(
            value["serverless_v2_features_support"],
            pairs,
            f"{key_prefix}ServerlessV2FeaturesSupport",
        )


def deserialize_query(el: Element) -> DBEngineVersion:
    out: DBEngineVersion = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_database_installation_files_s3_bucket_name = el.find(
        "DatabaseInstallationFilesS3BucketName"
    )
    if child_database_installation_files_s3_bucket_name is not None:
        out["database_installation_files_s3_bucket_name"] = str(
            child_database_installation_files_s3_bucket_name.text or ""
        )
    child_database_installation_files_s3_prefix = el.find(
        "DatabaseInstallationFilesS3Prefix"
    )
    if child_database_installation_files_s3_prefix is not None:
        out["database_installation_files_s3_prefix"] = str(
            child_database_installation_files_s3_prefix.text or ""
        )
    child_database_installation_files = el.find("DatabaseInstallationFiles")
    if child_database_installation_files is not None:
        import capo_rds.types.string_list

        out["database_installation_files"] = (
            capo_rds.types.string_list.deserialize_query(
                child_database_installation_files
            )
        )
    child_custom_db_engine_version_manifest = el.find("CustomDBEngineVersionManifest")
    if child_custom_db_engine_version_manifest is not None:
        out["custom_db_engine_version_manifest"] = str(
            child_custom_db_engine_version_manifest.text or ""
        )
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
    child_db_engine_description = el.find("DBEngineDescription")
    if child_db_engine_description is not None:
        out["db_engine_description"] = str(child_db_engine_description.text or "")
    child_db_engine_version_arn = el.find("DBEngineVersionArn")
    if child_db_engine_version_arn is not None:
        out["db_engine_version_arn"] = str(child_db_engine_version_arn.text or "")
    child_db_engine_version_description = el.find("DBEngineVersionDescription")
    if child_db_engine_version_description is not None:
        out["db_engine_version_description"] = str(
            child_db_engine_version_description.text or ""
        )
    child_default_character_set = el.find("DefaultCharacterSet")
    if child_default_character_set is not None:
        import capo_rds.types.character_set

        out["default_character_set"] = capo_rds.types.character_set.deserialize_query(
            child_default_character_set
        )
    child_failure_reason = el.find("FailureReason")
    if child_failure_reason is not None:
        out["failure_reason"] = str(child_failure_reason.text or "")
    child_image = el.find("Image")
    if child_image is not None:
        import capo_rds.types.custom_db_engine_version_ami

        out["image"] = capo_rds.types.custom_db_engine_version_ami.deserialize_query(
            child_image
        )
    child_db_engine_media_type = el.find("DBEngineMediaType")
    if child_db_engine_media_type is not None:
        out["db_engine_media_type"] = str(child_db_engine_media_type.text or "")
    child_kms_key_id = el.find("KMSKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import capo_rds.types.t_stamp

        out["create_time"] = capo_rds.types.t_stamp.deserialize_query(child_create_time)
    child_supported_character_sets = el.find("SupportedCharacterSets")
    if child_supported_character_sets is not None:
        import capo_rds.types.supported_character_sets_list

        out["supported_character_sets"] = (
            capo_rds.types.supported_character_sets_list.deserialize_query(
                child_supported_character_sets
            )
        )
    child_supported_nchar_character_sets = el.find("SupportedNcharCharacterSets")
    if child_supported_nchar_character_sets is not None:
        import capo_rds.types.supported_character_sets_list

        out["supported_nchar_character_sets"] = (
            capo_rds.types.supported_character_sets_list.deserialize_query(
                child_supported_nchar_character_sets
            )
        )
    child_valid_upgrade_target = el.find("ValidUpgradeTarget")
    if child_valid_upgrade_target is not None:
        import capo_rds.types.valid_upgrade_target_list

        out["valid_upgrade_target"] = (
            capo_rds.types.valid_upgrade_target_list.deserialize_query(
                child_valid_upgrade_target
            )
        )
    child_supported_timezones = el.find("SupportedTimezones")
    if child_supported_timezones is not None:
        import capo_rds.types.supported_timezones_list

        out["supported_timezones"] = (
            capo_rds.types.supported_timezones_list.deserialize_query(
                child_supported_timezones
            )
        )
    child_exportable_log_types = el.find("ExportableLogTypes")
    if child_exportable_log_types is not None:
        import capo_rds.types.log_type_list

        out["exportable_log_types"] = capo_rds.types.log_type_list.deserialize_query(
            child_exportable_log_types
        )
    child_supports_log_exports_to_cloudwatch_logs = el.find(
        "SupportsLogExportsToCloudwatchLogs"
    )
    if child_supports_log_exports_to_cloudwatch_logs is not None:
        out["supports_log_exports_to_cloudwatch_logs"] = (
            child_supports_log_exports_to_cloudwatch_logs.text or ""
        ).lower() == "true"
    child_supports_read_replica = el.find("SupportsReadReplica")
    if child_supports_read_replica is not None:
        out["supports_read_replica"] = (
            child_supports_read_replica.text or ""
        ).lower() == "true"
    child_supported_engine_modes = el.find("SupportedEngineModes")
    if child_supported_engine_modes is not None:
        import capo_rds.types.engine_mode_list

        out["supported_engine_modes"] = (
            capo_rds.types.engine_mode_list.deserialize_query(
                child_supported_engine_modes
            )
        )
    child_supported_feature_names = el.find("SupportedFeatureNames")
    if child_supported_feature_names is not None:
        import capo_rds.types.feature_name_list

        out["supported_feature_names"] = (
            capo_rds.types.feature_name_list.deserialize_query(
                child_supported_feature_names
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_supports_parallel_query = el.find("SupportsParallelQuery")
    if child_supports_parallel_query is not None:
        out["supports_parallel_query"] = (
            child_supports_parallel_query.text or ""
        ).lower() == "true"
    child_supports_global_databases = el.find("SupportsGlobalDatabases")
    if child_supports_global_databases is not None:
        out["supports_global_databases"] = (
            child_supports_global_databases.text or ""
        ).lower() == "true"
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    child_supports_babelfish = el.find("SupportsBabelfish")
    if child_supports_babelfish is not None:
        out["supports_babelfish"] = (
            child_supports_babelfish.text or ""
        ).lower() == "true"
    child_supports_limitless_database = el.find("SupportsLimitlessDatabase")
    if child_supports_limitless_database is not None:
        out["supports_limitless_database"] = (
            child_supports_limitless_database.text or ""
        ).lower() == "true"
    child_supports_certificate_rotation_without_restart = el.find(
        "SupportsCertificateRotationWithoutRestart"
    )
    if child_supports_certificate_rotation_without_restart is not None:
        out["supports_certificate_rotation_without_restart"] = (
            child_supports_certificate_rotation_without_restart.text or ""
        ).lower() == "true"
    child_supported_ca_certificate_identifiers = el.find(
        "SupportedCACertificateIdentifiers"
    )
    if child_supported_ca_certificate_identifiers is not None:
        import capo_rds.types.ca_certificate_identifiers_list

        out["supported_ca_certificate_identifiers"] = (
            capo_rds.types.ca_certificate_identifiers_list.deserialize_query(
                child_supported_ca_certificate_identifiers
            )
        )
    child_supports_local_write_forwarding = el.find("SupportsLocalWriteForwarding")
    if child_supports_local_write_forwarding is not None:
        out["supports_local_write_forwarding"] = (
            child_supports_local_write_forwarding.text or ""
        ).lower() == "true"
    child_supports_integrations = el.find("SupportsIntegrations")
    if child_supports_integrations is not None:
        out["supports_integrations"] = (
            child_supports_integrations.text or ""
        ).lower() == "true"
    child_serverless_v2_features_support = el.find("ServerlessV2FeaturesSupport")
    if child_serverless_v2_features_support is not None:
        import capo_rds.types.serverless_v2_features_support

        out["serverless_v2_features_support"] = (
            capo_rds.types.serverless_v2_features_support.deserialize_query(
                child_serverless_v2_features_support
            )
        )
    return out
