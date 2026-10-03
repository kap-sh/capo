"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boxed_boolean
    import capo_athena.types.bytes_scanned_cutoff_value
    import capo_athena.types.customer_content_encryption_configuration
    import capo_athena.types.engine_configuration
    import capo_athena.types.engine_version
    import capo_athena.types.identity_center_configuration
    import capo_athena.types.managed_query_results_configuration
    import capo_athena.types.monitoring_configuration
    import capo_athena.types.name_string
    import capo_athena.types.query_results_s3_access_grants_configuration
    import capo_athena.types.result_configuration
    import capo_athena.types.role_arn


class WorkGroupConfiguration(TypedDict, closed=True):
    result_configuration: NotRequired[
        "capo_athena.types.result_configuration.ResultConfiguration"
    ]
    """<p>The configuration for the workgroup, which includes the location in Amazon S3 where query and calculation results are stored and the encryption option, if any, used for query and calculation results. To run the query, you must specify the query results location using one of the ways: either in the workgroup using this setting, or for individual queries (client-side), using <a>ResultConfiguration$OutputLocation</a>. If none of them is set, Athena issues an error that no output location is provided.</p>"""
    managed_query_results_configuration: NotRequired[
        "capo_athena.types.managed_query_results_configuration.ManagedQueryResultsConfiguration"
    ]
    """<p> The configuration for storing results in Athena owned storage, which includes whether this feature is enabled; whether encryption configuration, if any, is used for encrypting query results. </p>"""
    enforce_work_group_configuration: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>If set to "true", the settings for the workgroup override client-side settings. If set to "false", client-side settings are used. This property is not required for Apache Spark enabled workgroups. For more information, see <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""
    publish_cloud_watch_metrics_enabled: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.</p>"""
    bytes_scanned_cutoff_per_query: NotRequired[
        "capo_athena.types.bytes_scanned_cutoff_value.BytesScannedCutoffValue"
    ]
    """<p>The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.</p>"""
    requester_pays_enabled: NotRequired["capo_athena.types.boxed_boolean.BoxedBoolean"]
    """<p>If set to <code>true</code>, allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries. If set to <code>false</code>, workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is <code>false</code>. For more information about Requester Pays buckets, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html">Requester Pays Buckets</a> in the <i>Amazon Simple Storage Service Developer Guide</i>.</p>"""
    engine_version: NotRequired["capo_athena.types.engine_version.EngineVersion"]
    """<p>The engine version that all queries running on the workgroup use. Queries on the <code>AmazonAthenaPreviewFunctionality</code> workgroup run on the preview engine regardless of this setting.</p>"""
    additional_configuration: NotRequired["capo_athena.types.name_string.NameString"]
    """<p>Specifies a user defined JSON string that is passed to the notebook engine.</p>"""
    execution_role: NotRequired["capo_athena.types.role_arn.RoleArn"]
    """<p>The ARN of the execution role used to access user resources for Spark sessions and IAM Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and IAM Identity Center enabled workgroups. The property is required for IAM Identity Center enabled workgroups.</p>"""
    monitoring_configuration: NotRequired[
        "capo_athena.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>Contains the configuration settings for managed log persistence, delivering logs to Amazon S3 buckets, Amazon CloudWatch log groups etc.</p>"""
    engine_configuration: NotRequired[
        "capo_athena.types.engine_configuration.EngineConfiguration"
    ]
    customer_content_encryption_configuration: NotRequired[
        "capo_athena.types.customer_content_encryption_configuration.CustomerContentEncryptionConfiguration"
    ]
    """<p>Specifies the KMS key that is used to encrypt the user's data stores in Athena. This setting does not apply to Athena SQL workgroups.</p>"""
    enable_minimum_encryption_configuration: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Enforces a minimal level of encryption for the workgroup for query and calculation results that are written to Amazon S3. When enabled, workgroup users can set encryption only to the minimum level set by the administrator or higher when they submit queries.</p> <p>The <code>EnforceWorkGroupConfiguration</code> setting takes precedence over the <code>EnableMinimumEncryptionConfiguration</code> flag. This means that if <code>EnforceWorkGroupConfiguration</code> is true, the <code>EnableMinimumEncryptionConfiguration</code> flag is ignored, and the workgroup configuration for encryption is used.</p>"""
    identity_center_configuration: NotRequired[
        "capo_athena.types.identity_center_configuration.IdentityCenterConfiguration"
    ]
    """<p>Specifies whether the workgroup is IAM Identity Center supported.</p>"""
    query_results_s3_access_grants_configuration: NotRequired[
        "capo_athena.types.query_results_s3_access_grants_configuration.QueryResultsS3AccessGrantsConfiguration"
    ]
    """<p>Specifies whether Amazon S3 access grants are enabled for query results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkGroupConfiguration) -> dict:
    out: dict = {}
    if "result_configuration" in value:
        import capo_athena.types.result_configuration

        out["ResultConfiguration"] = (
            capo_athena.types.result_configuration.serialize_aws_json_1_1(
                value["result_configuration"]
            )
        )
    if "managed_query_results_configuration" in value:
        import capo_athena.types.managed_query_results_configuration

        out["ManagedQueryResultsConfiguration"] = (
            capo_athena.types.managed_query_results_configuration.serialize_aws_json_1_1(
                value["managed_query_results_configuration"]
            )
        )
    if "enforce_work_group_configuration" in value:
        out["EnforceWorkGroupConfiguration"] = value["enforce_work_group_configuration"]
    if "publish_cloud_watch_metrics_enabled" in value:
        out["PublishCloudWatchMetricsEnabled"] = value[
            "publish_cloud_watch_metrics_enabled"
        ]
    if "bytes_scanned_cutoff_per_query" in value:
        out["BytesScannedCutoffPerQuery"] = value["bytes_scanned_cutoff_per_query"]
    if "requester_pays_enabled" in value:
        out["RequesterPaysEnabled"] = value["requester_pays_enabled"]
    if "engine_version" in value:
        import capo_athena.types.engine_version

        out["EngineVersion"] = capo_athena.types.engine_version.serialize_aws_json_1_1(
            value["engine_version"]
        )
    if "additional_configuration" in value:
        out["AdditionalConfiguration"] = value["additional_configuration"]
    if "execution_role" in value:
        out["ExecutionRole"] = value["execution_role"]
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
    if "identity_center_configuration" in value:
        import capo_athena.types.identity_center_configuration

        out["IdentityCenterConfiguration"] = (
            capo_athena.types.identity_center_configuration.serialize_aws_json_1_1(
                value["identity_center_configuration"]
            )
        )
    if "query_results_s3_access_grants_configuration" in value:
        import capo_athena.types.query_results_s3_access_grants_configuration

        out["QueryResultsS3AccessGrantsConfiguration"] = (
            capo_athena.types.query_results_s3_access_grants_configuration.serialize_aws_json_1_1(
                value["query_results_s3_access_grants_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkGroupConfiguration:
    out: WorkGroupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ResultConfiguration") is not None:
        import capo_athena.types.result_configuration

        out["result_configuration"] = (
            capo_athena.types.result_configuration.deserialize_aws_json_1_1(
                data["ResultConfiguration"]
            )
        )
    if data.get("ManagedQueryResultsConfiguration") is not None:
        import capo_athena.types.managed_query_results_configuration

        out["managed_query_results_configuration"] = (
            capo_athena.types.managed_query_results_configuration.deserialize_aws_json_1_1(
                data["ManagedQueryResultsConfiguration"]
            )
        )
    if data.get("EnforceWorkGroupConfiguration") is not None:
        out["enforce_work_group_configuration"] = data["EnforceWorkGroupConfiguration"]
    if data.get("PublishCloudWatchMetricsEnabled") is not None:
        out["publish_cloud_watch_metrics_enabled"] = data[
            "PublishCloudWatchMetricsEnabled"
        ]
    if data.get("BytesScannedCutoffPerQuery") is not None:
        out["bytes_scanned_cutoff_per_query"] = data["BytesScannedCutoffPerQuery"]
    if data.get("RequesterPaysEnabled") is not None:
        out["requester_pays_enabled"] = data["RequesterPaysEnabled"]
    if data.get("EngineVersion") is not None:
        import capo_athena.types.engine_version

        out["engine_version"] = (
            capo_athena.types.engine_version.deserialize_aws_json_1_1(
                data["EngineVersion"]
            )
        )
    if data.get("AdditionalConfiguration") is not None:
        out["additional_configuration"] = data["AdditionalConfiguration"]
    if data.get("ExecutionRole") is not None:
        out["execution_role"] = data["ExecutionRole"]
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
    if data.get("IdentityCenterConfiguration") is not None:
        import capo_athena.types.identity_center_configuration

        out["identity_center_configuration"] = (
            capo_athena.types.identity_center_configuration.deserialize_aws_json_1_1(
                data["IdentityCenterConfiguration"]
            )
        )
    if data.get("QueryResultsS3AccessGrantsConfiguration") is not None:
        import capo_athena.types.query_results_s3_access_grants_configuration

        out["query_results_s3_access_grants_configuration"] = (
            capo_athena.types.query_results_s3_access_grants_configuration.deserialize_aws_json_1_1(
                data["QueryResultsS3AccessGrantsConfiguration"]
            )
        )
    return out
