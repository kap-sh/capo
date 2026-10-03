"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroupConfigurationUpdates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boxed_boolean
    import capo_athena.types.bytes_scanned_cutoff_value
    import capo_athena.types.customer_content_encryption_configuration
    import capo_athena.types.engine_configuration
    import capo_athena.types.engine_version
    import capo_athena.types.managed_query_results_configuration_updates
    import capo_athena.types.monitoring_configuration
    import capo_athena.types.name_string
    import capo_athena.types.query_results_s3_access_grants_configuration
    import capo_athena.types.result_configuration_updates
    import capo_athena.types.role_arn


class WorkGroupConfigurationUpdates(TypedDict, closed=True):
    enforce_work_group_configuration: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>If set to "true", the settings for the workgroup override client-side settings. If set to "false" client-side settings are used. For more information, see <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""
    result_configuration_updates: NotRequired[
        "capo_athena.types.result_configuration_updates.ResultConfigurationUpdates"
    ]
    """<p>The result configuration information about the queries in this workgroup that will be updated. Includes the updated results location and an updated option for encrypting query results.</p>"""
    managed_query_results_configuration_updates: NotRequired[
        "capo_athena.types.managed_query_results_configuration_updates.ManagedQueryResultsConfigurationUpdates"
    ]
    """<p>Updates configuration information for managed query results in the workgroup.</p>"""
    publish_cloud_watch_metrics_enabled: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Indicates whether this workgroup enables publishing metrics to Amazon CloudWatch.</p>"""
    bytes_scanned_cutoff_per_query: NotRequired[
        "capo_athena.types.bytes_scanned_cutoff_value.BytesScannedCutoffValue"
    ]
    """<p>The upper limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.</p>"""
    remove_bytes_scanned_cutoff_per_query: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Indicates that the data usage control limit per query is removed. <a>WorkGroupConfiguration$BytesScannedCutoffPerQuery</a> </p>"""
    requester_pays_enabled: NotRequired["capo_athena.types.boxed_boolean.BoxedBoolean"]
    """<p>If set to <code>true</code>, allows members assigned to a workgroup to specify Amazon S3 Requester Pays buckets in queries. If set to <code>false</code>, workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is <code>false</code>. For more information about Requester Pays buckets, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html">Requester Pays Buckets</a> in the <i>Amazon Simple Storage Service Developer Guide</i>.</p>"""
    engine_version: NotRequired["capo_athena.types.engine_version.EngineVersion"]
    """<p>The engine version requested when a workgroup is updated. After the update, all queries on the workgroup run on the requested engine version. If no value was previously set, the default is Auto. Queries on the <code>AmazonAthenaPreviewFunctionality</code> workgroup run on the preview engine regardless of this setting.</p>"""
    remove_customer_content_encryption_configuration: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Removes content encryption configuration from an Apache Spark-enabled Athena workgroup.</p>"""
    additional_configuration: NotRequired["capo_athena.types.name_string.NameString"]
    """<p>Contains a user defined string in JSON format for a Spark-enabled workgroup.</p>"""
    execution_role: NotRequired["capo_athena.types.role_arn.RoleArn"]
    """<p>The ARN of the execution role used to access user resources for Spark sessions and Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and Identity Center enabled workgroups.</p>"""
    customer_content_encryption_configuration: NotRequired[
        "capo_athena.types.customer_content_encryption_configuration.CustomerContentEncryptionConfiguration"
    ]
    enable_minimum_encryption_configuration: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Enforces a minimal level of encryption for the workgroup for query and calculation results that are written to Amazon S3. When enabled, workgroup users can set encryption only to the minimum level set by the administrator or higher when they submit queries. This setting does not apply to Spark-enabled workgroups.</p> <p>The <code>EnforceWorkGroupConfiguration</code> setting takes precedence over the <code>EnableMinimumEncryptionConfiguration</code> flag. This means that if <code>EnforceWorkGroupConfiguration</code> is true, the <code>EnableMinimumEncryptionConfiguration</code> flag is ignored, and the workgroup configuration for encryption is used.</p>"""
    query_results_s3_access_grants_configuration: NotRequired[
        "capo_athena.types.query_results_s3_access_grants_configuration.QueryResultsS3AccessGrantsConfiguration"
    ]
    """<p>Specifies whether Amazon S3 access grants are enabled for query results.</p>"""
    monitoring_configuration: NotRequired[
        "capo_athena.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>Contains the configuration settings for managed log persistence, delivering logs to Amazon S3 buckets, Amazon CloudWatch log groups etc.</p>"""
    engine_configuration: NotRequired[
        "capo_athena.types.engine_configuration.EngineConfiguration"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkGroupConfigurationUpdates) -> dict:
    out: dict = {}
    if "enforce_work_group_configuration" in value:
        out["EnforceWorkGroupConfiguration"] = value["enforce_work_group_configuration"]
    if "result_configuration_updates" in value:
        import capo_athena.types.result_configuration_updates

        out["ResultConfigurationUpdates"] = (
            capo_athena.types.result_configuration_updates.serialize_aws_json_1_1(
                value["result_configuration_updates"]
            )
        )
    if "managed_query_results_configuration_updates" in value:
        import capo_athena.types.managed_query_results_configuration_updates

        out["ManagedQueryResultsConfigurationUpdates"] = (
            capo_athena.types.managed_query_results_configuration_updates.serialize_aws_json_1_1(
                value["managed_query_results_configuration_updates"]
            )
        )
    if "publish_cloud_watch_metrics_enabled" in value:
        out["PublishCloudWatchMetricsEnabled"] = value[
            "publish_cloud_watch_metrics_enabled"
        ]
    if "bytes_scanned_cutoff_per_query" in value:
        out["BytesScannedCutoffPerQuery"] = value["bytes_scanned_cutoff_per_query"]
    if "remove_bytes_scanned_cutoff_per_query" in value:
        out["RemoveBytesScannedCutoffPerQuery"] = value[
            "remove_bytes_scanned_cutoff_per_query"
        ]
    if "requester_pays_enabled" in value:
        out["RequesterPaysEnabled"] = value["requester_pays_enabled"]
    if "engine_version" in value:
        import capo_athena.types.engine_version

        out["EngineVersion"] = capo_athena.types.engine_version.serialize_aws_json_1_1(
            value["engine_version"]
        )
    if "remove_customer_content_encryption_configuration" in value:
        out["RemoveCustomerContentEncryptionConfiguration"] = value[
            "remove_customer_content_encryption_configuration"
        ]
    if "additional_configuration" in value:
        out["AdditionalConfiguration"] = value["additional_configuration"]
    if "execution_role" in value:
        out["ExecutionRole"] = value["execution_role"]
    if "customer_content_encryption_configuration" in value:
        import capo_athena.types.customer_content_encryption_configuration

        out["CustomerContentEncryptionConfiguration"] = (
            capo_athena.types.customer_content_encryption_configuration.serialize_aws_json_1_1(
                value["customer_content_encryption_configuration"]
            )
        )
    if "enable_minimum_encryption_configuration" in value:
        out["EnableMinimumEncryptionConfiguration"] = value[
            "enable_minimum_encryption_configuration"
        ]
    if "query_results_s3_access_grants_configuration" in value:
        import capo_athena.types.query_results_s3_access_grants_configuration

        out["QueryResultsS3AccessGrantsConfiguration"] = (
            capo_athena.types.query_results_s3_access_grants_configuration.serialize_aws_json_1_1(
                value["query_results_s3_access_grants_configuration"]
            )
        )
    if "monitoring_configuration" in value:
        import capo_athena.types.monitoring_configuration

        out["MonitoringConfiguration"] = (
            capo_athena.types.monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring_configuration"]
            )
        )
    if "engine_configuration" in value:
        import capo_athena.types.engine_configuration

        out["EngineConfiguration"] = (
            capo_athena.types.engine_configuration.serialize_aws_json_1_1(
                value["engine_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkGroupConfigurationUpdates:
    out: WorkGroupConfigurationUpdates = {}  # type: ignore[typeddict-item]
    if data.get("EnforceWorkGroupConfiguration") is not None:
        out["enforce_work_group_configuration"] = data["EnforceWorkGroupConfiguration"]
    if data.get("ResultConfigurationUpdates") is not None:
        import capo_athena.types.result_configuration_updates

        out["result_configuration_updates"] = (
            capo_athena.types.result_configuration_updates.deserialize_aws_json_1_1(
                data["ResultConfigurationUpdates"]
            )
        )
    if data.get("ManagedQueryResultsConfigurationUpdates") is not None:
        import capo_athena.types.managed_query_results_configuration_updates

        out["managed_query_results_configuration_updates"] = (
            capo_athena.types.managed_query_results_configuration_updates.deserialize_aws_json_1_1(
                data["ManagedQueryResultsConfigurationUpdates"]
            )
        )
    if data.get("PublishCloudWatchMetricsEnabled") is not None:
        out["publish_cloud_watch_metrics_enabled"] = data[
            "PublishCloudWatchMetricsEnabled"
        ]
    if data.get("BytesScannedCutoffPerQuery") is not None:
        out["bytes_scanned_cutoff_per_query"] = data["BytesScannedCutoffPerQuery"]
    if data.get("RemoveBytesScannedCutoffPerQuery") is not None:
        out["remove_bytes_scanned_cutoff_per_query"] = data[
            "RemoveBytesScannedCutoffPerQuery"
        ]
    if data.get("RequesterPaysEnabled") is not None:
        out["requester_pays_enabled"] = data["RequesterPaysEnabled"]
    if data.get("EngineVersion") is not None:
        import capo_athena.types.engine_version

        out["engine_version"] = (
            capo_athena.types.engine_version.deserialize_aws_json_1_1(
                data["EngineVersion"]
            )
        )
    if data.get("RemoveCustomerContentEncryptionConfiguration") is not None:
        out["remove_customer_content_encryption_configuration"] = data[
            "RemoveCustomerContentEncryptionConfiguration"
        ]
    if data.get("AdditionalConfiguration") is not None:
        out["additional_configuration"] = data["AdditionalConfiguration"]
    if data.get("ExecutionRole") is not None:
        out["execution_role"] = data["ExecutionRole"]
    if data.get("CustomerContentEncryptionConfiguration") is not None:
        import capo_athena.types.customer_content_encryption_configuration

        out["customer_content_encryption_configuration"] = (
            capo_athena.types.customer_content_encryption_configuration.deserialize_aws_json_1_1(
                data["CustomerContentEncryptionConfiguration"]
            )
        )
    if data.get("EnableMinimumEncryptionConfiguration") is not None:
        out["enable_minimum_encryption_configuration"] = data[
            "EnableMinimumEncryptionConfiguration"
        ]
    if data.get("QueryResultsS3AccessGrantsConfiguration") is not None:
        import capo_athena.types.query_results_s3_access_grants_configuration

        out["query_results_s3_access_grants_configuration"] = (
            capo_athena.types.query_results_s3_access_grants_configuration.deserialize_aws_json_1_1(
                data["QueryResultsS3AccessGrantsConfiguration"]
            )
        )
    if data.get("MonitoringConfiguration") is not None:
        import capo_athena.types.monitoring_configuration

        out["monitoring_configuration"] = (
            capo_athena.types.monitoring_configuration.deserialize_aws_json_1_1(
                data["MonitoringConfiguration"]
            )
        )
    if data.get("EngineConfiguration") is not None:
        import capo_athena.types.engine_configuration

        out["engine_configuration"] = (
            capo_athena.types.engine_configuration.deserialize_aws_json_1_1(
                data["EngineConfiguration"]
            )
        )
    return out
