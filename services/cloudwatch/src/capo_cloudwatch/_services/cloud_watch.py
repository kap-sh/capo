"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GraniteServiceVersion20100801``."""

import time
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cloudwatch._auth._signers
import capo_cloudwatch._auth._sigv4
from capo_cloudwatch._auth._identity import Credentials
from capo_cloudwatch._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudwatch._auth._zapros_handler import AuthMiddleware
from capo_cloudwatch._pagination import resolve_path as _resolve_path
from capo_cloudwatch._services._aws_config import aws_config
from capo_cloudwatch._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)
from capo_cloudwatch.errors import ServiceError, WaiterTimeoutError

if TYPE_CHECKING:
    import capo_cloudwatch.types.account_id
    import capo_cloudwatch.types.action_log_line_count
    import capo_cloudwatch.types.action_log_line_role_arn
    import capo_cloudwatch.types.action_prefix
    import capo_cloudwatch.types.actions_enabled
    import capo_cloudwatch.types.alarm_arn
    import capo_cloudwatch.types.alarm_description
    import capo_cloudwatch.types.alarm_history_item
    import capo_cloudwatch.types.alarm_mute_rule_statuses
    import capo_cloudwatch.types.alarm_mute_rule_summary
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.alarm_name_prefix
    import capo_cloudwatch.types.alarm_names
    import capo_cloudwatch.types.alarm_rule
    import capo_cloudwatch.types.alarm_types
    import capo_cloudwatch.types.amazon_resource_name
    import capo_cloudwatch.types.anomaly_detector
    import capo_cloudwatch.types.anomaly_detector_configuration
    import capo_cloudwatch.types.anomaly_detector_id
    import capo_cloudwatch.types.anomaly_detector_ids
    import capo_cloudwatch.types.anomaly_detector_metric_stat
    import capo_cloudwatch.types.anomaly_detector_types
    import capo_cloudwatch.types.associate_dataset_kms_key_input
    import capo_cloudwatch.types.associate_dataset_kms_key_output
    import capo_cloudwatch.types.comparison_operator
    import capo_cloudwatch.types.contributor_id
    import capo_cloudwatch.types.create_resource_metrics_configuration_input
    import capo_cloudwatch.types.create_resource_metrics_configuration_output
    import capo_cloudwatch.types.dashboard_body
    import capo_cloudwatch.types.dashboard_entry
    import capo_cloudwatch.types.dashboard_name
    import capo_cloudwatch.types.dashboard_name_prefix
    import capo_cloudwatch.types.dashboard_names
    import capo_cloudwatch.types.datapoints_to_alarm
    import capo_cloudwatch.types.dataset_identifier
    import capo_cloudwatch.types.delete_alarm_mute_rule_input
    import capo_cloudwatch.types.delete_alarms_input
    import capo_cloudwatch.types.delete_anomaly_detector_input
    import capo_cloudwatch.types.delete_anomaly_detector_output
    import capo_cloudwatch.types.delete_dashboards_input
    import capo_cloudwatch.types.delete_dashboards_output
    import capo_cloudwatch.types.delete_insight_rules_input
    import capo_cloudwatch.types.delete_insight_rules_output
    import capo_cloudwatch.types.delete_metric_stream_input
    import capo_cloudwatch.types.delete_metric_stream_output
    import capo_cloudwatch.types.delete_resource_metrics_configuration_input
    import capo_cloudwatch.types.delete_resource_metrics_configuration_output
    import capo_cloudwatch.types.describe_alarm_contributors_input
    import capo_cloudwatch.types.describe_alarm_contributors_output
    import capo_cloudwatch.types.describe_alarm_history_input
    import capo_cloudwatch.types.describe_alarm_history_output
    import capo_cloudwatch.types.describe_alarms_for_metric_input
    import capo_cloudwatch.types.describe_alarms_for_metric_output
    import capo_cloudwatch.types.describe_alarms_input
    import capo_cloudwatch.types.describe_alarms_output
    import capo_cloudwatch.types.describe_anomaly_detectors_input
    import capo_cloudwatch.types.describe_anomaly_detectors_output
    import capo_cloudwatch.types.describe_insight_rules_input
    import capo_cloudwatch.types.describe_insight_rules_output
    import capo_cloudwatch.types.dimension_filters
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.disable_alarm_actions_input
    import capo_cloudwatch.types.disable_insight_rules_input
    import capo_cloudwatch.types.disable_insight_rules_output
    import capo_cloudwatch.types.disassociate_dataset_kms_key_input
    import capo_cloudwatch.types.disassociate_dataset_kms_key_output
    import capo_cloudwatch.types.enable_alarm_actions_input
    import capo_cloudwatch.types.enable_insight_rules_input
    import capo_cloudwatch.types.enable_insight_rules_output
    import capo_cloudwatch.types.entity_metric_data_list
    import capo_cloudwatch.types.evaluate_low_sample_count_percentile
    import capo_cloudwatch.types.evaluation_criteria
    import capo_cloudwatch.types.evaluation_interval
    import capo_cloudwatch.types.evaluation_periods
    import capo_cloudwatch.types.evaluation_window
    import capo_cloudwatch.types.extended_statistic
    import capo_cloudwatch.types.extended_statistics
    import capo_cloudwatch.types.get_alarm_mute_rule_input
    import capo_cloudwatch.types.get_alarm_mute_rule_output
    import capo_cloudwatch.types.get_dashboard_input
    import capo_cloudwatch.types.get_dashboard_output
    import capo_cloudwatch.types.get_dataset_input
    import capo_cloudwatch.types.get_dataset_output
    import capo_cloudwatch.types.get_insight_rule_report_input
    import capo_cloudwatch.types.get_insight_rule_report_output
    import capo_cloudwatch.types.get_metric_data_input
    import capo_cloudwatch.types.get_metric_data_max_datapoints
    import capo_cloudwatch.types.get_metric_data_output
    import capo_cloudwatch.types.get_metric_statistics_input
    import capo_cloudwatch.types.get_metric_statistics_output
    import capo_cloudwatch.types.get_metric_stream_input
    import capo_cloudwatch.types.get_metric_stream_output
    import capo_cloudwatch.types.get_metric_widget_image_input
    import capo_cloudwatch.types.get_metric_widget_image_output
    import capo_cloudwatch.types.get_o_tel_enrichment_input
    import capo_cloudwatch.types.get_o_tel_enrichment_output
    import capo_cloudwatch.types.get_resource_metrics_configuration_input
    import capo_cloudwatch.types.get_resource_metrics_configuration_output
    import capo_cloudwatch.types.history_item_type
    import capo_cloudwatch.types.include_linked_accounts
    import capo_cloudwatch.types.include_linked_accounts_metrics
    import capo_cloudwatch.types.insight_rule_definition
    import capo_cloudwatch.types.insight_rule_max_results
    import capo_cloudwatch.types.insight_rule_metric_list
    import capo_cloudwatch.types.insight_rule_name
    import capo_cloudwatch.types.insight_rule_names
    import capo_cloudwatch.types.insight_rule_on_transformed_logs
    import capo_cloudwatch.types.insight_rule_order_by
    import capo_cloudwatch.types.insight_rule_state
    import capo_cloudwatch.types.insight_rule_unbound_integer
    import capo_cloudwatch.types.kms_key_arn
    import capo_cloudwatch.types.label_options
    import capo_cloudwatch.types.list_alarm_mute_rules_input
    import capo_cloudwatch.types.list_alarm_mute_rules_output
    import capo_cloudwatch.types.list_dashboards_input
    import capo_cloudwatch.types.list_dashboards_output
    import capo_cloudwatch.types.list_managed_insight_rules_input
    import capo_cloudwatch.types.list_managed_insight_rules_output
    import capo_cloudwatch.types.list_metric_streams_input
    import capo_cloudwatch.types.list_metric_streams_max_results
    import capo_cloudwatch.types.list_metric_streams_output
    import capo_cloudwatch.types.list_metrics_input
    import capo_cloudwatch.types.list_metrics_output
    import capo_cloudwatch.types.list_tags_for_resource_input
    import capo_cloudwatch.types.list_tags_for_resource_output
    import capo_cloudwatch.types.managed_rules
    import capo_cloudwatch.types.max_records
    import capo_cloudwatch.types.max_returned_results_count
    import capo_cloudwatch.types.metric_characteristics
    import capo_cloudwatch.types.metric_data
    import capo_cloudwatch.types.metric_data_queries
    import capo_cloudwatch.types.metric_id
    import capo_cloudwatch.types.metric_math_anomaly_detector
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.metric_stream_filters
    import capo_cloudwatch.types.metric_stream_name
    import capo_cloudwatch.types.metric_stream_names
    import capo_cloudwatch.types.metric_stream_output_format
    import capo_cloudwatch.types.metric_stream_statistics_configurations
    import capo_cloudwatch.types.metric_widget
    import capo_cloudwatch.types.mute_targets
    import capo_cloudwatch.types.name
    import capo_cloudwatch.types.namespace
    import capo_cloudwatch.types.next_token
    import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list
    import capo_cloudwatch.types.output_format
    import capo_cloudwatch.types.period
    import capo_cloudwatch.types.put_alarm_mute_rule_input
    import capo_cloudwatch.types.put_anomaly_detector_input
    import capo_cloudwatch.types.put_anomaly_detector_output
    import capo_cloudwatch.types.put_composite_alarm_input
    import capo_cloudwatch.types.put_dashboard_input
    import capo_cloudwatch.types.put_dashboard_output
    import capo_cloudwatch.types.put_insight_rule_input
    import capo_cloudwatch.types.put_insight_rule_output
    import capo_cloudwatch.types.put_log_alarm_input
    import capo_cloudwatch.types.put_managed_insight_rules_input
    import capo_cloudwatch.types.put_managed_insight_rules_output
    import capo_cloudwatch.types.put_metric_alarm_input
    import capo_cloudwatch.types.put_metric_data_input
    import capo_cloudwatch.types.put_metric_stream_input
    import capo_cloudwatch.types.put_metric_stream_output
    import capo_cloudwatch.types.query_results_to_alarm
    import capo_cloudwatch.types.query_results_to_evaluate
    import capo_cloudwatch.types.recently_active
    import capo_cloudwatch.types.resource_arn
    import capo_cloudwatch.types.resource_list
    import capo_cloudwatch.types.resource_metric_selection_list
    import capo_cloudwatch.types.rule
    import capo_cloudwatch.types.scan_by
    import capo_cloudwatch.types.scheduled_query_configuration
    import capo_cloudwatch.types.set_alarm_state_input
    import capo_cloudwatch.types.single_metric_anomaly_detector
    import capo_cloudwatch.types.standard_unit
    import capo_cloudwatch.types.start_metric_streams_input
    import capo_cloudwatch.types.start_metric_streams_output
    import capo_cloudwatch.types.start_o_tel_enrichment_input
    import capo_cloudwatch.types.start_o_tel_enrichment_output
    import capo_cloudwatch.types.state_reason
    import capo_cloudwatch.types.state_reason_data
    import capo_cloudwatch.types.state_value
    import capo_cloudwatch.types.statistic
    import capo_cloudwatch.types.statistics
    import capo_cloudwatch.types.stop_metric_streams_input
    import capo_cloudwatch.types.stop_metric_streams_output
    import capo_cloudwatch.types.stop_o_tel_enrichment_input
    import capo_cloudwatch.types.stop_o_tel_enrichment_output
    import capo_cloudwatch.types.strict_entity_validation
    import capo_cloudwatch.types.suppressor_period
    import capo_cloudwatch.types.tag_key_list
    import capo_cloudwatch.types.tag_list
    import capo_cloudwatch.types.tag_resource_input
    import capo_cloudwatch.types.tag_resource_output
    import capo_cloudwatch.types.threshold
    import capo_cloudwatch.types.timestamp
    import capo_cloudwatch.types.treat_missing_data
    import capo_cloudwatch.types.untag_resource_input
    import capo_cloudwatch.types.untag_resource_output
    import capo_cloudwatch.types.update_o_tel_enrichment_input
    import capo_cloudwatch.types.update_o_tel_enrichment_output
    import capo_cloudwatch.types.update_resource_metrics_configuration_input
    import capo_cloudwatch.types.update_resource_metrics_configuration_output
    import capo_cloudwatch.types.warm_up_configuration


class CloudWatchClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class CloudWatchClient:
    """A client for the ``CloudWatch`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = CloudWatchClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[CloudWatchClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudWatchClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def associate_dataset_kms_key(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        dataset_identifier: Optional[
            "capo_cloudwatch.types.dataset_identifier.DatasetIdentifier"
        ] = None,
        kms_key_arn: Optional["capo_cloudwatch.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> "capo_cloudwatch.types.associate_dataset_kms_key_output.AssociateDatasetKmsKeyOutput":
        """<p>Associates an Amazon Web Services Key Management Service (Amazon Web Services KMS) customer managed key with the specified dataset. After this operation completes, all data published to the dataset is encrypted at rest using the specified KMS key. Callers must have <code>kms:Decrypt</code> permission on the key to read the encrypted data.</p> <p>Only the <code>default</code> dataset is supported. The <code>default</code> dataset is implicit for every account in every Region — you do not need to create it before calling this operation.</p> <p>You can call <code>AssociateDatasetKmsKey</code> on a dataset that is already associated with a KMS key to replace the existing key with a different one. The caller must have <code>kms:Decrypt</code> permission on both the current key and the new key.</p> <note> <p>If the currently associated key has been deleted, is scheduled for deletion, is pending import, is unavailable, or has been disabled, Amazon CloudWatch does not require <code>kms:Decrypt</code> permission on the current key and the rotation proceeds. If the key was only disabled, consider re-enabling it instead of rotating, because re-enabling allows Amazon CloudWatch to resume decrypting your existing metric data encrypted with that key.</p> </note> <p>The KMS key that you specify must meet all of the following requirements:</p> <ul> <li> <p>It must be a symmetric encryption KMS key (key spec <code>SYMMETRIC_DEFAULT</code>, key usage <code>ENCRYPT_DECRYPT</code>). Asymmetric keys, HMAC keys, and key material types other than <code>SYMMETRIC_DEFAULT</code> are not supported.</p> </li> <li> <p>It must be enabled and not pending deletion.</p> </li> <li> <p>Its key policy must grant the CloudWatch service principal (<code>cloudwatch.amazonaws.com</code>) these permissions: <code>kms:DescribeKey</code>, <code>kms:GenerateDataKey</code>, <code>kms:Encrypt</code>, <code>kms:Decrypt</code>, and <code>kms:ReEncrypt*</code>. Amazon CloudWatch requires these permissions to manage the data on your behalf.</p> </li> <li> <p>The calling principal must have <code>kms:Decrypt</code> permission on the key.</p> </li> <li> <p>It must be specified as a fully qualified key ARN. Key IDs, aliases, and alias ARNs are not accepted.</p> </li> <li> <p>It must be in the same Amazon Web Services Region as the dataset.</p> </li> </ul> <p>Before completing the association, Amazon CloudWatch validates the key by performing a series of dry-run KMS operations. Service-principal checks run first to verify that the key policy grants the required access to Amazon CloudWatch. These checks include <code>kms:DescribeKey</code>, <code>kms:GenerateDataKey</code>, <code>kms:Encrypt</code>, <code>kms:Decrypt</code>, and <code>kms:ReEncrypt*</code>. After those succeed, a <code>kms:Decrypt</code> dry-run is run with the caller's credentials to verify that the calling principal can use the new key. When you are replacing an existing key, the caller's <code>kms:Decrypt</code> dry-run is also run on the current key.</p> <p>If any of these checks on the new key fails, the operation fails and the existing key association (if any) remains unchanged. Common failure causes include the new key being disabled, the key policy not granting the required permissions to Amazon CloudWatch, or the caller lacking <code>kms:Decrypt</code> permission on the new key.</p> <p>For more information about using customer managed keys with Amazon CloudWatch, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cmk-encryption.html">Encryption at rest with customer managed keys</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            dataset_identifier: <p>Specifies the identifier of the dataset that you want to associate the KMS key with. For the <code>default</code> dataset, you can specify either <code>default</code> or the full dataset Amazon Resource Name (ARN) in the format <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:dataset/default</code>.</p>
            kms_key_arn: <p>Specifies the Amazon Resource Name (ARN) of the customer managed KMS key to associate with the dataset. The key must be a symmetric encryption KMS key (<code>SYMMETRIC_DEFAULT</code>) in the same Amazon Web Services Region as the dataset.</p> <p>The ARN must be in the format <code>arn:aws:kms:<i>Region</i>:<i>account-id</i>:key/<i>key-id</i> </code>. Key IDs, aliases, and alias ARNs are not accepted.</p> <p>For more information about KMS key ARNs, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key ARN</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>

        Raises:
            capo_cloudwatch.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>The operation was denied because either the calling principal lacks the required Amazon Web Services Key Management Service (Amazon Web Services KMS) permission on the key, or the key policy does not grant Amazon CloudWatch the permissions it needs to use the key. Verify that the caller has <code>kms:Decrypt</code> permission on the key, and that the key policy grants the CloudWatch service principal the <code>kms:DescribeKey</code>, <code>kms:GenerateDataKey</code>, <code>kms:Encrypt</code>, <code>kms:Decrypt</code>, and <code>kms:ReEncrypt*</code> permissions described in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AssociateDatasetKmsKey.html">AssociateDatasetKmsKey</a>.</p>
            capo_cloudwatch.errors.kms_key_disabled_exception.KmsKeyDisabledException: <p>The specified Amazon Web Services Key Management Service (Amazon Web Services KMS) key is disabled or pending deletion. Re-enable the key (or restore it, if it is pending deletion) and retry the operation.</p>
            capo_cloudwatch.errors.kms_key_not_found_exception.KmsKeyNotFoundException: <p>The specified Amazon Web Services Key Management Service (Amazon Web Services KMS) key could not be found. Verify that the key Amazon Resource Name (ARN) is correct, that the key exists, and that it is in the same Amazon Web Services Region as the resource.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.associate_dataset_kms_key_input.AssociateDatasetKmsKeyInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.associate_dataset_kms_key_output.AssociateDatasetKmsKeyOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.associate_dataset_kms_key

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.associate_dataset_kms_key.associate_dataset_kms_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.associate_dataset_kms_key_input.AssociateDatasetKmsKeyInput = {}
        if dataset_identifier is not None:
            input_["dataset_identifier"] = dataset_identifier
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_resource_metrics_configuration(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        resource_arn: Optional["capo_cloudwatch.types.resource_arn.ResourceArn"] = None,
        metric_selections: Optional[
            "capo_cloudwatch.types.resource_metric_selection_list.ResourceMetricSelectionList"
        ] = None,
    ) -> "capo_cloudwatch.types.create_resource_metrics_configuration_output.CreateResourceMetricsConfigurationOutput":
        """<p>Creates a resource metrics configuration for an Amazon Web Services resource. After you create a configuration, Amazon CloudWatch collects detailed metrics for that resource.</p> <p>Each Amazon Web Services resource can have only one resource metrics configuration. If a configuration already exists for the specified resource ARN, this operation returns a <code>ConflictException</code>. To modify an existing configuration, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateResourceMetricsConfiguration.html">UpdateResourceMetricsConfiguration</a>.</p> <p>If the Amazon Web Services resource that you specify in <code>ResourceArn</code> does not exist, this operation returns a <code>ResourceNotFoundException</code>. Verify that the resource ARN is correct and that the resource exists before you retry the request.</p> <p>To create a resource metrics configuration, you must have the <code>cloudwatch:CreateResourceMetricsConfiguration</code> permission. For information about scoping this permission to specific resources, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html">Condition keys for resource metrics configuration access</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to enable detailed monitoring for.</p>
            metric_selections: <p>Specifies which metrics Amazon CloudWatch collects for the resource. If you omit this parameter, Amazon CloudWatch collects all available detailed metrics for the resource.</p>

        Raises:
            capo_cloudwatch.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.create_resource_metrics_configuration_input.CreateResourceMetricsConfigurationInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.create_resource_metrics_configuration_output.CreateResourceMetricsConfigurationOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.create_resource_metrics_configuration

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.create_resource_metrics_configuration.create_resource_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.create_resource_metrics_configuration_input.CreateResourceMetricsConfigurationInput = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if metric_selections is not None:
            input_["metric_selections"] = metric_selections

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_alarm_mute_rule(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_mute_rule_name: Optional["capo_cloudwatch.types.name.Name"] = None,
    ) -> None:
        """<p>Deletes a specific alarm mute rule.</p> <p>When you delete a mute rule, any alarms that are currently being muted by that rule are immediately unmuted. If those alarms are in an ALARM state, their configured actions will trigger.</p> <p>This operation is idempotent. If you delete a mute rule that does not exist, the operation succeeds without returning an error.</p> <p> <b>Permissions</b> </p> <p>To delete a mute rule, you need the <code>cloudwatch:DeleteAlarmMuteRule</code> permission on the alarm mute rule resource.</p>

        Args:
            alarm_mute_rule_name: <p>The name of the alarm mute rule to delete.</p>

        Raises:
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.delete_alarm_mute_rule_input.DeleteAlarmMuteRuleInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.delete_alarm_mute_rule

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.delete_alarm_mute_rule.delete_alarm_mute_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.delete_alarm_mute_rule_input.DeleteAlarmMuteRuleInput = {}
        if alarm_mute_rule_name is not None:
            input_["alarm_mute_rule_name"] = alarm_mute_rule_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_alarms(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_names: Optional["capo_cloudwatch.types.alarm_names.AlarmNames"] = None,
    ) -> None:
        """<p>Deletes the specified alarms. You can delete up to 100 alarms in one operation. However, this total can include no more than one composite alarm. For example, you could delete 99 metric alarms and one composite alarms with one operation, but you can't delete two composite alarms with one operation. Log alarms cannot be batch deleted.</p> <p> If you specify any incorrect alarm names, the alarms you specify with correct names are still deleted. Other syntax errors might result in no alarms being deleted. To confirm that alarms were deleted successfully, you can use the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html">DescribeAlarms</a> operation after using <code>DeleteAlarms</code>.</p> <note> <p>It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you can't delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.</p> <p>To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the <code>AlarmRule</code> of one of the alarms to <code>false</code>. </p> <p>Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path. </p> </note>

        Args:
            alarm_names: <p>The alarms to be deleted. Do not enclose the alarm names in quote marks.</p>

        Raises:
            capo_cloudwatch.errors.resource_conflict.ResourceConflict: <p>The operation could not be completed because the request conflicts with the current state of the alarm or its underlying scheduled query resource.</p>
            capo_cloudwatch.errors.resource_not_found.ResourceNotFound: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.delete_alarms_input.DeleteAlarmsInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.delete_alarms

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.delete_alarms.delete_alarms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.delete_alarms_input.DeleteAlarmsInput = {}
        if alarm_names is not None:
            input_["alarm_names"] = alarm_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_anomaly_detector(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        anomaly_detector_id: Optional[
            "capo_cloudwatch.types.anomaly_detector_id.AnomalyDetectorId"
        ] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        metric_name: Optional["capo_cloudwatch.types.metric_name.MetricName"] = None,
        dimensions: Optional["capo_cloudwatch.types.dimensions.Dimensions"] = None,
        stat: Optional[
            "capo_cloudwatch.types.anomaly_detector_metric_stat.AnomalyDetectorMetricStat"
        ] = None,
        single_metric_anomaly_detector: Optional[
            "capo_cloudwatch.types.single_metric_anomaly_detector.SingleMetricAnomalyDetector"
        ] = None,
        metric_math_anomaly_detector: Optional[
            "capo_cloudwatch.types.metric_math_anomaly_detector.MetricMathAnomalyDetector"
        ] = None,
    ) -> "capo_cloudwatch.types.delete_anomaly_detector_output.DeleteAnomalyDetectorOutput":
        """<p> Deletes the specified anomaly detection model from your account. For more information about how to delete an anomaly detection model, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html#Delete_Anomaly_Detection_Model">Deleting an anomaly detection model</a> in the <i>CloudWatch User Guide</i>. </p>

        Args:
            anomaly_detector_id: <p>Specifies the unique identifier of the anomaly detector to delete. If you specify this parameter, you do not need to specify a metric to identify the detector.</p>
            namespace: <p>The namespace associated with the anomaly detection model to delete.</p>
            metric_name: <p>The metric name associated with the anomaly detection model to delete.</p>
            dimensions: <p>The metric dimensions associated with the anomaly detection model to delete.</p>
            stat: <p>The statistic associated with the anomaly detection model to delete.</p>
            single_metric_anomaly_detector: <p>A single metric anomaly detector to be deleted.</p> <p>When using <code>SingleMetricAnomalyDetector</code>, you cannot include the following parameters in the same operation:</p> <ul> <li> <p> <code>Dimensions</code>,</p> </li> <li> <p> <code>MetricName</code> </p> </li> <li> <p> <code>Namespace</code> </p> </li> <li> <p> <code>Stat</code> </p> </li> <li> <p>the <code>MetricMathAnomalyDetector</code> parameters of <code>DeleteAnomalyDetectorInput</code> </p> </li> </ul> <p>Instead, specify the single metric anomaly detector attributes as part of the <code>SingleMetricAnomalyDetector</code> property.</p>
            metric_math_anomaly_detector: <p>The metric math anomaly detector to be deleted.</p> <p>When using <code>MetricMathAnomalyDetector</code>, you cannot include following parameters in the same operation:</p> <ul> <li> <p> <code>Dimensions</code>,</p> </li> <li> <p> <code>MetricName</code> </p> </li> <li> <p> <code>Namespace</code> </p> </li> <li> <p> <code>Stat</code> </p> </li> <li> <p>the <code>SingleMetricAnomalyDetector</code> parameters of <code>DeleteAnomalyDetectorInput</code> </p> </li> </ul> <p>Instead, specify the metric math anomaly detector attributes as part of the <code>MetricMathAnomalyDetector</code> property.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Parameters were used together that cannot be used together.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.delete_anomaly_detector_input.DeleteAnomalyDetectorInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.delete_anomaly_detector_output.DeleteAnomalyDetectorOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.delete_anomaly_detector

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.delete_anomaly_detector.delete_anomaly_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.delete_anomaly_detector_input.DeleteAnomalyDetectorInput = {}
        if anomaly_detector_id is not None:
            input_["anomaly_detector_id"] = anomaly_detector_id
        if namespace is not None:
            input_["namespace"] = namespace
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if dimensions is not None:
            input_["dimensions"] = dimensions
        if stat is not None:
            input_["stat"] = stat
        if single_metric_anomaly_detector is not None:
            input_["single_metric_anomaly_detector"] = single_metric_anomaly_detector
        if metric_math_anomaly_detector is not None:
            input_["metric_math_anomaly_detector"] = metric_math_anomaly_detector

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_dashboards(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        dashboard_names: Optional[
            "capo_cloudwatch.types.dashboard_names.DashboardNames"
        ] = None,
    ) -> "capo_cloudwatch.types.delete_dashboards_output.DeleteDashboardsOutput":
        """<p>Deletes all dashboards that you specify. You can specify up to 100 dashboards to delete. If there is an error during this call, the operation attempts to delete as many dashboards as possible.</p>

        Args:
            dashboard_names: <p>The dashboards to be deleted. This parameter is required.</p>

        Raises:
            capo_cloudwatch.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.delete_dashboards_input.DeleteDashboardsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.delete_dashboards_output.DeleteDashboardsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.delete_dashboards

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.delete_dashboards.delete_dashboards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.delete_dashboards_input.DeleteDashboardsInput = {}
        if dashboard_names is not None:
            input_["dashboard_names"] = dashboard_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_insight_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        rule_names: Optional[
            "capo_cloudwatch.types.insight_rule_names.InsightRuleNames"
        ] = None,
    ) -> "capo_cloudwatch.types.delete_insight_rules_output.DeleteInsightRulesOutput":
        """<p>Permanently deletes the specified Contributor Insights rules.</p> <p>If you create a rule, delete it, and then re-create it with the same name, historical data from the first time the rule was created might not be available.</p>

        Args:
            rule_names: <p>An array of the rule names to delete. If you need to find out the names of your rules, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html">DescribeInsightRules</a>.</p>

        Raises:
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.delete_insight_rules_input.DeleteInsightRulesInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.delete_insight_rules_output.DeleteInsightRulesOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.delete_insight_rules

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.delete_insight_rules.delete_insight_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.delete_insight_rules_input.DeleteInsightRulesInput = {}
        if rule_names is not None:
            input_["rule_names"] = rule_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_metric_stream(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        name: Optional[
            "capo_cloudwatch.types.metric_stream_name.MetricStreamName"
        ] = None,
    ) -> "capo_cloudwatch.types.delete_metric_stream_output.DeleteMetricStreamOutput":
        """<p>Permanently deletes the metric stream that you specify.</p>

        Args:
            name: <p>The name of the metric stream to delete.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.delete_metric_stream_input.DeleteMetricStreamInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.delete_metric_stream_output.DeleteMetricStreamOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.delete_metric_stream

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.delete_metric_stream.delete_metric_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.delete_metric_stream_input.DeleteMetricStreamInput = {}
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_metrics_configuration(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        resource_arn: Optional["capo_cloudwatch.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_cloudwatch.types.delete_resource_metrics_configuration_output.DeleteResourceMetricsConfigurationOutput":
        """<p>Deletes the resource metrics configuration for an Amazon Web Services resource. After you delete the configuration, Amazon CloudWatch stops collecting detailed metrics for the resource. Metric data that Amazon CloudWatch already collected for the resource is not deleted.</p> <p>This operation returns a <code>ResourceNotFoundException</code> if no resource metrics configuration exists for the specified resource ARN. Verify that the resource ARN is correct.</p> <p>To delete a resource metrics configuration, you must have the <code>cloudwatch:DeleteResourceMetricsConfiguration</code> permission. For information about scoping this permission to specific resources, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html">Condition keys for resource metrics configuration access</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to delete the resource metrics configuration for.</p>

        Raises:
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.delete_resource_metrics_configuration_input.DeleteResourceMetricsConfigurationInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.delete_resource_metrics_configuration_output.DeleteResourceMetricsConfigurationOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.delete_resource_metrics_configuration

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.delete_resource_metrics_configuration.delete_resource_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.delete_resource_metrics_configuration_input.DeleteResourceMetricsConfigurationInput = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_alarm_contributors(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_name: Optional["capo_cloudwatch.types.alarm_name.AlarmName"] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch.types.describe_alarm_contributors_output.DescribeAlarmContributorsOutput":
        """<p>Returns the information of the current alarm contributors that are in <code>ALARM</code> state. This operation returns details about the individual time series that contribute to the alarm's state.</p>

        Args:
            alarm_name: <p>The name of the alarm for which to retrieve contributor information.</p>
            next_token: <p>The token returned by a previous call to indicate that there is more data available.</p>

        Raises:
            capo_cloudwatch.errors.invalid_next_token.InvalidNextToken: <p>The next token specified is invalid.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.describe_alarm_contributors_input.DescribeAlarmContributorsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.describe_alarm_contributors_output.DescribeAlarmContributorsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.describe_alarm_contributors

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.describe_alarm_contributors.describe_alarm_contributors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.describe_alarm_contributors_input.DescribeAlarmContributorsInput = {}
        if alarm_name is not None:
            input_["alarm_name"] = alarm_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_alarm_history(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_name: Optional["capo_cloudwatch.types.alarm_name.AlarmName"] = None,
        alarm_contributor_id: Optional[
            "capo_cloudwatch.types.contributor_id.ContributorId"
        ] = None,
        alarm_types: Optional["capo_cloudwatch.types.alarm_types.AlarmTypes"] = None,
        history_item_type: Optional[
            "capo_cloudwatch.types.history_item_type.HistoryItemType"
        ] = None,
        start_date: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        end_date: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        max_records: Optional["capo_cloudwatch.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        scan_by: Optional["capo_cloudwatch.types.scan_by.ScanBy"] = None,
    ) -> (
        "capo_cloudwatch.types.describe_alarm_history_output.DescribeAlarmHistoryOutput"
    ):
        """<p>Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for either all metric alarms or all composite alarms are returned.</p> <p>CloudWatch retains the history of an alarm even if you delete the alarm.</p> <p>To use this operation and return information about a composite alarm, you must be signed on with the <code>cloudwatch:DescribeAlarmHistory</code> permission that is scoped to <code>*</code>. You can't return information about composite alarms if your <code>cloudwatch:DescribeAlarmHistory</code> permission has a narrower scope.</p>

        Args:
            alarm_name: <p>The name of the alarm.</p>
            alarm_contributor_id: <p>The unique identifier of a specific alarm contributor to filter the alarm history results.</p>
            alarm_types: <p>Use this parameter to specify whether you want the operation to return metric alarms, composite alarms, or log alarms. If you omit this parameter, only metric alarms are returned.</p>
            history_item_type: <p>The type of alarm histories to retrieve.</p>
            start_date: <p>The starting date to retrieve alarm history.</p>
            end_date: <p>The ending date to retrieve alarm history.</p>
            max_records: <p>The maximum number of alarm history records to retrieve.</p>
            next_token: <p>The token returned by a previous call to indicate that there is more data available.</p>
            scan_by: <p>Specified whether to return the newest or oldest alarm history first. Specify <code>TimestampDescending</code> to have the newest event history returned first, and specify <code>TimestampAscending</code> to have the oldest history returned first.</p>

        Raises:
            capo_cloudwatch.errors.invalid_next_token.InvalidNextToken: <p>The next token specified is invalid.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.describe_alarm_history_input.DescribeAlarmHistoryInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.describe_alarm_history_output.DescribeAlarmHistoryOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.describe_alarm_history

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.describe_alarm_history.describe_alarm_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.describe_alarm_history_input.DescribeAlarmHistoryInput = {}
        if alarm_name is not None:
            input_["alarm_name"] = alarm_name
        if alarm_contributor_id is not None:
            input_["alarm_contributor_id"] = alarm_contributor_id
        if alarm_types is not None:
            input_["alarm_types"] = alarm_types
        if history_item_type is not None:
            input_["history_item_type"] = history_item_type
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token
        if scan_by is not None:
            input_["scan_by"] = scan_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_alarm_history(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_name: Optional["capo_cloudwatch.types.alarm_name.AlarmName"] = None,
        alarm_contributor_id: Optional[
            "capo_cloudwatch.types.contributor_id.ContributorId"
        ] = None,
        alarm_types: Optional["capo_cloudwatch.types.alarm_types.AlarmTypes"] = None,
        history_item_type: Optional[
            "capo_cloudwatch.types.history_item_type.HistoryItemType"
        ] = None,
        start_date: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        end_date: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        max_records: Optional["capo_cloudwatch.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        scan_by: Optional["capo_cloudwatch.types.scan_by.ScanBy"] = None,
    ) -> "Iterator[capo_cloudwatch.types.alarm_history_item.AlarmHistoryItem]":
        _token = next_token
        while True:
            _response = self.describe_alarm_history(
                config_overrides=config_overrides,
                alarm_name=alarm_name,
                alarm_contributor_id=alarm_contributor_id,
                alarm_types=alarm_types,
                history_item_type=history_item_type,
                start_date=start_date,
                end_date=end_date,
                max_records=max_records,
                next_token=_token,
                scan_by=scan_by,
            )
            _page = _resolve_path(_response, ("alarm_history_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_alarms(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_names: Optional["capo_cloudwatch.types.alarm_names.AlarmNames"] = None,
        alarm_name_prefix: Optional[
            "capo_cloudwatch.types.alarm_name_prefix.AlarmNamePrefix"
        ] = None,
        alarm_types: Optional["capo_cloudwatch.types.alarm_types.AlarmTypes"] = None,
        children_of_alarm_name: Optional[
            "capo_cloudwatch.types.alarm_name.AlarmName"
        ] = None,
        parents_of_alarm_name: Optional[
            "capo_cloudwatch.types.alarm_name.AlarmName"
        ] = None,
        state_value: Optional["capo_cloudwatch.types.state_value.StateValue"] = None,
        action_prefix: Optional[
            "capo_cloudwatch.types.action_prefix.ActionPrefix"
        ] = None,
        max_records: Optional["capo_cloudwatch.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch.types.describe_alarms_output.DescribeAlarmsOutput":
        """<p>Retrieves the specified alarms. You can filter the results by specifying a prefix for the alarm name, the alarm state, or a prefix for any action.</p> <p>To use this operation and return information about composite alarms, you must be signed on with the <code>cloudwatch:DescribeAlarms</code> permission that is scoped to <code>*</code>. You can't return information about composite alarms if your <code>cloudwatch:DescribeAlarms</code> permission has a narrower scope.</p>

        Args:
            alarm_names: <p>The names of the alarms to retrieve information about.</p>
            alarm_name_prefix: <p>An alarm name prefix. If you specify this parameter, you receive information about all alarms that have names that start with this prefix.</p> <p>If this parameter is specified, you cannot specify <code>AlarmNames</code>.</p>
            alarm_types: <p>Use this parameter to specify whether you want the operation to return metric alarms, composite alarms, or log alarms. If you omit this parameter, only metric alarms are returned, even if composite alarms or log alarms exist in the account.</p> <p>For example, if you omit this parameter or specify <code>MetricAlarms</code>, the operation returns only a list of metric alarms. It does not return any composite alarms or log alarms, even if they exist in the account.</p> <p>If you specify <code>CompositeAlarms</code>, the operation returns only a list of composite alarms, and does not return any metric alarms or log alarms.</p> <p>If you specify <code>LogAlarms</code>, the operation returns only a list of log alarms, and does not return any metric alarms or composite alarms.</p>
            children_of_alarm_name: <p>If you use this parameter and specify the name of a composite alarm, the operation returns information about the "children" alarms of the alarm you specify. These are the metric alarms and composite alarms referenced in the <code>AlarmRule</code> field of the composite alarm that you specify in <code>ChildrenOfAlarmName</code>. Information about the composite alarm that you name in <code>ChildrenOfAlarmName</code> is not returned.</p> <p>If you specify <code>ChildrenOfAlarmName</code>, you cannot specify any other parameters in the request except for <code>MaxRecords</code> and <code>NextToken</code>. If you do so, you receive a validation error.</p> <note> <p>Only the <code>Alarm Name</code>, <code>ARN</code>, <code>StateValue</code> (OK/ALARM/INSUFFICIENT_DATA), and <code>StateUpdatedTimestamp</code> information are returned by this operation when you use this parameter. To get complete information about these alarms, perform another <code>DescribeAlarms</code> operation and specify the parent alarm names in the <code>AlarmNames</code> parameter.</p> </note>
            parents_of_alarm_name: <p>If you use this parameter and specify the name of a metric or composite alarm, the operation returns information about the "parent" alarms of the alarm you specify. These are the composite alarms that have <code>AlarmRule</code> parameters that reference the alarm named in <code>ParentsOfAlarmName</code>. Information about the alarm that you specify in <code>ParentsOfAlarmName</code> is not returned.</p> <p>If you specify <code>ParentsOfAlarmName</code>, you cannot specify any other parameters in the request except for <code>MaxRecords</code> and <code>NextToken</code>. If you do so, you receive a validation error.</p> <note> <p>Only the Alarm Name and ARN are returned by this operation when you use this parameter. To get complete information about these alarms, perform another <code>DescribeAlarms</code> operation and specify the parent alarm names in the <code>AlarmNames</code> parameter.</p> </note>
            state_value: <p>Specify this parameter to receive information only about alarms that are currently in the state that you specify.</p>
            action_prefix: <p>Use this parameter to filter the results of the operation to only those alarms that use a certain alarm action. For example, you could specify the ARN of an SNS topic to find all alarms that send notifications to that topic.</p>
            max_records: <p>The maximum number of alarm descriptions to retrieve.</p>
            next_token: <p>The token returned by a previous call to indicate that there is more data available.</p>

        Raises:
            capo_cloudwatch.errors.invalid_next_token.InvalidNextToken: <p>The next token specified is invalid.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.describe_alarms_input.DescribeAlarmsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.describe_alarms_output.DescribeAlarmsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.describe_alarms

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.describe_alarms.describe_alarms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.describe_alarms_input.DescribeAlarmsInput = {}
        if alarm_names is not None:
            input_["alarm_names"] = alarm_names
        if alarm_name_prefix is not None:
            input_["alarm_name_prefix"] = alarm_name_prefix
        if alarm_types is not None:
            input_["alarm_types"] = alarm_types
        if children_of_alarm_name is not None:
            input_["children_of_alarm_name"] = children_of_alarm_name
        if parents_of_alarm_name is not None:
            input_["parents_of_alarm_name"] = parents_of_alarm_name
        if state_value is not None:
            input_["state_value"] = state_value
        if action_prefix is not None:
            input_["action_prefix"] = action_prefix
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_alarms(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_names: Optional["capo_cloudwatch.types.alarm_names.AlarmNames"] = None,
        alarm_name_prefix: Optional[
            "capo_cloudwatch.types.alarm_name_prefix.AlarmNamePrefix"
        ] = None,
        alarm_types: Optional["capo_cloudwatch.types.alarm_types.AlarmTypes"] = None,
        children_of_alarm_name: Optional[
            "capo_cloudwatch.types.alarm_name.AlarmName"
        ] = None,
        parents_of_alarm_name: Optional[
            "capo_cloudwatch.types.alarm_name.AlarmName"
        ] = None,
        state_value: Optional["capo_cloudwatch.types.state_value.StateValue"] = None,
        action_prefix: Optional[
            "capo_cloudwatch.types.action_prefix.ActionPrefix"
        ] = None,
        max_records: Optional["capo_cloudwatch.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudwatch.types.describe_alarms_output.DescribeAlarmsOutput]":
        _token = next_token
        while True:
            _response = self.describe_alarms(
                config_overrides=config_overrides,
                alarm_names=alarm_names,
                alarm_name_prefix=alarm_name_prefix,
                alarm_types=alarm_types,
                children_of_alarm_name=children_of_alarm_name,
                parents_of_alarm_name=parents_of_alarm_name,
                state_value=state_value,
                action_prefix=action_prefix,
                max_records=max_records,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_alarms_for_metric(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        metric_name: Optional["capo_cloudwatch.types.metric_name.MetricName"] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        statistic: Optional["capo_cloudwatch.types.statistic.Statistic"] = None,
        extended_statistic: Optional[
            "capo_cloudwatch.types.extended_statistic.ExtendedStatistic"
        ] = None,
        dimensions: Optional["capo_cloudwatch.types.dimensions.Dimensions"] = None,
        period: Optional["capo_cloudwatch.types.period.Period"] = None,
        unit: Optional["capo_cloudwatch.types.standard_unit.StandardUnit"] = None,
    ) -> "capo_cloudwatch.types.describe_alarms_for_metric_output.DescribeAlarmsForMetricOutput":
        """<p>Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period, or unit.</p> <p>This operation retrieves only standard alarms that are based on the specified metric. It does not return alarms based on math expressions that use the specified metric, or composite alarms that use the specified metric.</p>

        Args:
            metric_name: <p>The name of the metric.</p>
            namespace: <p>The namespace of the metric.</p>
            statistic: <p>The statistic for the metric, other than percentiles. For percentile statistics, use <code>ExtendedStatistics</code>.</p>
            extended_statistic: <p>The percentile statistic for the metric. Specify a value between p0.0 and p100.</p>
            dimensions: <p>The dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the call to succeed.</p>
            period: <p>The period, in seconds, over which the statistic is applied.</p>
            unit: <p>The unit for the metric.</p>

        Raises:
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.describe_alarms_for_metric_input.DescribeAlarmsForMetricInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.describe_alarms_for_metric_output.DescribeAlarmsForMetricOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.describe_alarms_for_metric

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.describe_alarms_for_metric.describe_alarms_for_metric(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.describe_alarms_for_metric_input.DescribeAlarmsForMetricInput = {}
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if namespace is not None:
            input_["namespace"] = namespace
        if statistic is not None:
            input_["statistic"] = statistic
        if extended_statistic is not None:
            input_["extended_statistic"] = extended_statistic
        if dimensions is not None:
            input_["dimensions"] = dimensions
        if period is not None:
            input_["period"] = period
        if unit is not None:
            input_["unit"] = unit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_anomaly_detectors(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        anomaly_detector_ids: Optional[
            "capo_cloudwatch.types.anomaly_detector_ids.AnomalyDetectorIds"
        ] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch.types.max_returned_results_count.MaxReturnedResultsCount"
        ] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        metric_name: Optional["capo_cloudwatch.types.metric_name.MetricName"] = None,
        dimensions: Optional["capo_cloudwatch.types.dimensions.Dimensions"] = None,
        anomaly_detector_types: Optional[
            "capo_cloudwatch.types.anomaly_detector_types.AnomalyDetectorTypes"
        ] = None,
    ) -> "capo_cloudwatch.types.describe_anomaly_detectors_output.DescribeAnomalyDetectorsOutput":
        """<p>Lists the anomaly detection models that you have created in your account. For single metric anomaly detectors, you can list all of the models in your account or filter the results to only the models that are related to a certain namespace, metric name, or metric dimension. For metric math anomaly detectors, you can list them by adding <code>METRIC_MATH</code> to the <code>AnomalyDetectorTypes</code> array. This will return all metric math anomaly detectors in your account.</p>

        Args:
            anomaly_detector_ids: <p>Specifies the unique identifiers of the anomaly detectors to describe. You can specify up to 50 identifiers. If you specify this parameter, you cannot also specify the <code>Namespace</code>, <code>MetricName</code>, <code>Dimensions</code>, or <code>AnomalyDetectorTypes</code> metric filters.</p>
            next_token: <p>Use the token returned by the previous operation to request the next page of results.</p>
            max_results: <p>The maximum number of results to return in one operation. The maximum value that you can specify is 100.</p> <p>To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. </p>
            namespace: <p>Limits the results to only the anomaly detection models that are associated with the specified namespace.</p>
            metric_name: <p>Limits the results to only the anomaly detection models that are associated with the specified metric name. If there are multiple metrics with this name in different namespaces that have anomaly detection models, they're all returned.</p>
            dimensions: <p>Limits the results to only the anomaly detection models that are associated with the specified metric dimensions. If there are multiple metrics that have these dimensions and have anomaly detection models associated, they're all returned.</p>
            anomaly_detector_types: <p>The anomaly detector types to request when using <code>DescribeAnomalyDetectorsInput</code>. If empty, defaults to <code>SINGLE_METRIC</code>.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_next_token.InvalidNextToken: <p>The next token specified is invalid.</p>
            capo_cloudwatch.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Parameters were used together that cannot be used together.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.describe_anomaly_detectors_input.DescribeAnomalyDetectorsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.describe_anomaly_detectors_output.DescribeAnomalyDetectorsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.describe_anomaly_detectors

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.describe_anomaly_detectors.describe_anomaly_detectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.describe_anomaly_detectors_input.DescribeAnomalyDetectorsInput = {}
        if anomaly_detector_ids is not None:
            input_["anomaly_detector_ids"] = anomaly_detector_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace is not None:
            input_["namespace"] = namespace
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if dimensions is not None:
            input_["dimensions"] = dimensions
        if anomaly_detector_types is not None:
            input_["anomaly_detector_types"] = anomaly_detector_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_anomaly_detectors(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        anomaly_detector_ids: Optional[
            "capo_cloudwatch.types.anomaly_detector_ids.AnomalyDetectorIds"
        ] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch.types.max_returned_results_count.MaxReturnedResultsCount"
        ] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        metric_name: Optional["capo_cloudwatch.types.metric_name.MetricName"] = None,
        dimensions: Optional["capo_cloudwatch.types.dimensions.Dimensions"] = None,
        anomaly_detector_types: Optional[
            "capo_cloudwatch.types.anomaly_detector_types.AnomalyDetectorTypes"
        ] = None,
    ) -> "Iterator[capo_cloudwatch.types.anomaly_detector.AnomalyDetector]":
        _token = next_token
        while True:
            _response = self.describe_anomaly_detectors(
                config_overrides=config_overrides,
                anomaly_detector_ids=anomaly_detector_ids,
                next_token=_token,
                max_results=max_results,
                namespace=namespace,
                metric_name=metric_name,
                dimensions=dimensions,
                anomaly_detector_types=anomaly_detector_types,
            )
            _page = _resolve_path(_response, ("anomaly_detectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_insight_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch.types.insight_rule_max_results.InsightRuleMaxResults"
        ] = None,
    ) -> (
        "capo_cloudwatch.types.describe_insight_rules_output.DescribeInsightRulesOutput"
    ):
        """<p>Returns a list of all the Contributor Insights rules in your account.</p> <p>For more information about Contributor Insights, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html">Using Contributor Insights to Analyze High-Cardinality Data</a>.</p>

        Args:
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of rules.</p>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 500 is used.</p>

        Raises:
            capo_cloudwatch.errors.invalid_next_token.InvalidNextToken: <p>The next token specified is invalid.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.describe_insight_rules_input.DescribeInsightRulesInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.describe_insight_rules_output.DescribeInsightRulesOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.describe_insight_rules

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.describe_insight_rules.describe_insight_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.describe_insight_rules_input.DescribeInsightRulesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_insight_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch.types.insight_rule_max_results.InsightRuleMaxResults"
        ] = None,
    ) -> "Iterator[capo_cloudwatch.types.describe_insight_rules_output.DescribeInsightRulesOutput]":
        _token = next_token
        while True:
            _response = self.describe_insight_rules(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def disable_alarm_actions(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_names: Optional["capo_cloudwatch.types.alarm_names.AlarmNames"] = None,
    ) -> None:
        """<p>Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions do not execute when the alarm state changes.</p>

        Args:
            alarm_names: <p>The names of the alarms.</p>

        Raises:
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.disable_alarm_actions_input.DisableAlarmActionsInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.disable_alarm_actions

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.disable_alarm_actions.disable_alarm_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.disable_alarm_actions_input.DisableAlarmActionsInput = {}
        if alarm_names is not None:
            input_["alarm_names"] = alarm_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_insight_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        rule_names: Optional[
            "capo_cloudwatch.types.insight_rule_names.InsightRuleNames"
        ] = None,
    ) -> "capo_cloudwatch.types.disable_insight_rules_output.DisableInsightRulesOutput":
        """<p>Disables the specified Contributor Insights rules. When rules are disabled, they do not analyze log groups and do not incur costs.</p>

        Args:
            rule_names: <p>An array of the rule names to disable. If you need to find out the names of your rules, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html">DescribeInsightRules</a>.</p>

        Raises:
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.disable_insight_rules_input.DisableInsightRulesInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.disable_insight_rules_output.DisableInsightRulesOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.disable_insight_rules

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.disable_insight_rules.disable_insight_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.disable_insight_rules_input.DisableInsightRulesInput = {}
        if rule_names is not None:
            input_["rule_names"] = rule_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_dataset_kms_key(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        dataset_identifier: Optional[
            "capo_cloudwatch.types.dataset_identifier.DatasetIdentifier"
        ] = None,
    ) -> "capo_cloudwatch.types.disassociate_dataset_kms_key_output.DisassociateDatasetKmsKeyOutput":
        """<p>Removes the customer managed Amazon Web Services Key Management Service (Amazon Web Services KMS) key association from the specified dataset. After this operation completes, data that you publish to the dataset is encrypted at rest using an Amazon Web Services owned key managed by Amazon CloudWatch.</p> <p>Only the <code>default</code> dataset is supported. To call this operation, the dataset must currently have a customer managed KMS key associated with it. If the dataset has no associated KMS key, the operation fails with <code>ResourceNotFoundException</code>.</p> <p>Amazon CloudWatch performs a dry-run <code>kms:Decrypt</code> call on the currently associated key as part of this operation. The caller must have <code>kms:Decrypt</code> permission on the currently associated key. If the key is accessible but the caller lacks <code>kms:Decrypt</code> permission, the operation fails with <code>AccessDeniedException</code>.</p> <note> <p>If the currently associated key has been deleted, is scheduled for deletion, is pending import, is unavailable, or has been disabled, Amazon CloudWatch does not require <code>kms:Decrypt</code> permission on that key and the disassociation proceeds. If the key was only disabled, consider re-enabling it instead of disassociating, because re-enabling allows Amazon CloudWatch to resume decrypting your existing metric data.</p> </note> <important> <p>Disassociating a KMS key from a dataset does not immediately remove the <code>kms:Decrypt</code> requirement on data plane operations. For up to three hours after disassociation, callers must continue to have <code>kms:Decrypt</code> permission on the previously associated key. Some data might still be encrypted with that key during this window. After this enforcement window elapses, the <code>kms:Decrypt</code> requirement is lifted.</p> </important> <p>For more information about using customer managed keys with Amazon CloudWatch, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cmk-encryption.html">Encryption at rest with customer managed keys</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            dataset_identifier: <p>Specifies the identifier of the dataset from which to remove the KMS key association. For the <code>default</code> dataset, you can specify either <code>default</code> or the full dataset Amazon Resource Name (ARN) in the format <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:dataset/default</code>.</p>

        Raises:
            capo_cloudwatch.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.disassociate_dataset_kms_key_input.DisassociateDatasetKmsKeyInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.disassociate_dataset_kms_key_output.DisassociateDatasetKmsKeyOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.disassociate_dataset_kms_key

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.disassociate_dataset_kms_key.disassociate_dataset_kms_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.disassociate_dataset_kms_key_input.DisassociateDatasetKmsKeyInput = {}
        if dataset_identifier is not None:
            input_["dataset_identifier"] = dataset_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_alarm_actions(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_names: Optional["capo_cloudwatch.types.alarm_names.AlarmNames"] = None,
    ) -> None:
        """<p>Enables the actions for the specified alarms.</p>

        Args:
            alarm_names: <p>The names of the alarms.</p>

        Raises:
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.enable_alarm_actions_input.EnableAlarmActionsInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.enable_alarm_actions

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.enable_alarm_actions.enable_alarm_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.enable_alarm_actions_input.EnableAlarmActionsInput = {}
        if alarm_names is not None:
            input_["alarm_names"] = alarm_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_insight_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        rule_names: Optional[
            "capo_cloudwatch.types.insight_rule_names.InsightRuleNames"
        ] = None,
    ) -> "capo_cloudwatch.types.enable_insight_rules_output.EnableInsightRulesOutput":
        """<p>Enables the specified Contributor Insights rules. When rules are enabled, they immediately begin analyzing log data.</p>

        Args:
            rule_names: <p>An array of the rule names to enable. If you need to find out the names of your rules, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html">DescribeInsightRules</a>.</p>

        Raises:
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeded one or more limits.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.enable_insight_rules_input.EnableInsightRulesInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.enable_insight_rules_output.EnableInsightRulesOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.enable_insight_rules

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.enable_insight_rules.enable_insight_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.enable_insight_rules_input.EnableInsightRulesInput = {}
        if rule_names is not None:
            input_["rule_names"] = rule_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_alarm_mute_rule(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_mute_rule_name: Optional["capo_cloudwatch.types.name.Name"] = None,
    ) -> "capo_cloudwatch.types.get_alarm_mute_rule_output.GetAlarmMuteRuleOutput":
        """<p>Retrieves details for a specific alarm mute rule.</p> <p>This operation returns complete information about the mute rule, including its configuration, status, targeted alarms, and metadata.</p> <p>The returned status indicates the current state of the mute rule:</p> <ul> <li> <p> <b>SCHEDULED</b>: The mute rule is configured and will become active in the future</p> </li> <li> <p> <b>ACTIVE</b>: The mute rule is currently muting alarm actions</p> </li> <li> <p> <b>EXPIRED</b>: The mute rule has passed its expiration date and will no longer become active</p> </li> </ul> <p> <b>Permissions</b> </p> <p>To retrieve details for a mute rule, you need the <code>cloudwatch:GetAlarmMuteRule</code> permission on the alarm mute rule resource.</p>

        Args:
            alarm_mute_rule_name: <p>The name of the alarm mute rule to retrieve.</p>

        Raises:
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_alarm_mute_rule_input.GetAlarmMuteRuleInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_alarm_mute_rule_output.GetAlarmMuteRuleOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_alarm_mute_rule

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_alarm_mute_rule.get_alarm_mute_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_alarm_mute_rule_input.GetAlarmMuteRuleInput = {}
        if alarm_mute_rule_name is not None:
            input_["alarm_mute_rule_name"] = alarm_mute_rule_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def wait_until_alarm_mute_rule_exists(
        self,
        *,
        max_wait_time: float,
        min_delay: float = 5,
        max_delay: float = 120,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_mute_rule_name: Optional["capo_cloudwatch.types.name.Name"] = None,
    ) -> "capo_cloudwatch.types.get_alarm_mute_rule_output.GetAlarmMuteRuleOutput":
        """Wait for alarm_mute_rule_exists.

        Args:
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
            alarm_mute_rule_name: <p>The name of the alarm mute rule to retrieve.</p>
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_cloudwatch.types.get_alarm_mute_rule_output.GetAlarmMuteRuleOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = self.get_alarm_mute_rule(  # noqa: F841
                    config_overrides=config_overrides,
                    alarm_mute_rule_name=alarm_mute_rule_name,
                )
            except ServiceError as e:
                op_error = e
            if op_output is not None:
                return op_output
            elif op_error is not None and op_error.code == "ResourceNotFoundException":
                pass

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("alarm_mute_rule_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            time.sleep(delay)
            attempt += 1

    def get_dashboard(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        dashboard_name: Optional[
            "capo_cloudwatch.types.dashboard_name.DashboardName"
        ] = None,
    ) -> "capo_cloudwatch.types.get_dashboard_output.GetDashboardOutput":
        """<p>Displays the details of the dashboard that you specify.</p> <p>To copy an existing dashboard, use <code>GetDashboard</code>, and then use the data returned within <code>DashboardBody</code> as the template for the new dashboard when you call <code>PutDashboard</code> to create the copy.</p> <p>You might have recently enabled an <a href="https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#optinregion">opt-in Region (Region that is disabled by default)</a> for your account. In that Region, <code>GetDashboard</code> can return an access denied error for up to 24 hours after you enable the Region. This delay occurs while dashboard data propagates. The error does not indicate a problem with your permissions. Because dashboards are global, you can call <code>GetDashboard</code> in any other enabled Region, or retry after propagation completes.</p>

        Args:
            dashboard_name: <p>The name of the dashboard to be described.</p>

        Raises:
            capo_cloudwatch.errors.dashboard_not_found_error.DashboardNotFoundError: <p>The specified dashboard does not exist.</p>
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_dashboard_input.GetDashboardInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_dashboard_output.GetDashboardOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_dashboard

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_dashboard.get_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_dashboard_input.GetDashboardInput = {}
        if dashboard_name is not None:
            input_["dashboard_name"] = dashboard_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dataset(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        dataset_identifier: Optional[
            "capo_cloudwatch.types.dataset_identifier.DatasetIdentifier"
        ] = None,
    ) -> "capo_cloudwatch.types.get_dataset_output.GetDatasetOutput":
        """<p>Returns information about the specified dataset. This includes its identifier, Amazon Resource Name (ARN), and any customer managed Amazon Web Services Key Management Service (Amazon Web Services KMS) key that is currently associated with it.</p> <p>Only the <code>default</code> dataset is supported. The <code>default</code> dataset is implicit for every account in every Region — you can call <code>GetDataset</code> for it without first creating it. If no customer managed KMS key has been associated with the dataset, the response omits the <code>KmsKeyArn</code> field, indicating that data is encrypted at rest using an Amazon Web Services owned key managed by Amazon CloudWatch.</p> <p>To associate a customer managed KMS key with a dataset, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AssociateDatasetKmsKey.html">AssociateDatasetKmsKey</a>. To remove the association, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisassociateDatasetKmsKey.html">DisassociateDatasetKmsKey</a>.</p>

        Args:
            dataset_identifier: <p>Specifies the identifier of the dataset to retrieve. For the <code>default</code> dataset, you can specify either <code>default</code> or the full dataset Amazon Resource Name (ARN) in the format <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:dataset/default</code>.</p>

        Raises:
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_dataset_input.GetDatasetInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_dataset_output.GetDatasetOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_dataset

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_dataset.get_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_dataset_input.GetDatasetInput = {}
        if dataset_identifier is not None:
            input_["dataset_identifier"] = dataset_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_insight_rule_report(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        rule_name: Optional[
            "capo_cloudwatch.types.insight_rule_name.InsightRuleName"
        ] = None,
        start_time: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        period: Optional["capo_cloudwatch.types.period.Period"] = None,
        max_contributor_count: Optional[
            "capo_cloudwatch.types.insight_rule_unbound_integer.InsightRuleUnboundInteger"
        ] = None,
        metrics: Optional[
            "capo_cloudwatch.types.insight_rule_metric_list.InsightRuleMetricList"
        ] = None,
        order_by: Optional[
            "capo_cloudwatch.types.insight_rule_order_by.InsightRuleOrderBy"
        ] = None,
    ) -> "capo_cloudwatch.types.get_insight_rule_report_output.GetInsightRuleReportOutput":
        """<p>This operation returns the time series data collected by a Contributor Insights rule. The data includes the identity and number of contributors to the log group.</p> <p>You can also optionally return one or more statistics about each data point in the time series. These statistics can include the following:</p> <ul> <li> <p> <code>UniqueContributors</code> -- the number of unique contributors for each data point.</p> </li> <li> <p> <code>MaxContributorValue</code> -- the value of the top contributor for each data point. The identity of the contributor might change for each data point in the graph.</p> <p>If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the rule's <code>Value</code>, during that period.</p> </li> <li> <p> <code>SampleCount</code> -- the number of data points matched by the rule.</p> </li> <li> <p> <code>Sum</code> -- the sum of the values from all contributors during the time period represented by that data point.</p> </li> <li> <p> <code>Minimum</code> -- the minimum value from a single observation during the time period represented by that data point.</p> </li> <li> <p> <code>Maximum</code> -- the maximum value from a single observation during the time period represented by that data point.</p> </li> <li> <p> <code>Average</code> -- the average value from all contributors during the time period represented by that data point.</p> </li> </ul>

        Args:
            rule_name: <p>The name of the rule that you want to see data from.</p>
            start_time: <p>The start time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>
            end_time: <p>The end time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>
            period: <p>The period, in seconds, to use for the statistics in the <code>InsightRuleMetricDatapoint</code> results.</p>
            max_contributor_count: <p>The maximum number of contributors to include in the report. The range is 1 to 100. If you omit this, the default of 10 is used.</p>
            metrics: <p>Specifies which metrics to use for aggregation of contributor values for the report. You can specify one or more of the following metrics:</p> <ul> <li> <p> <code>UniqueContributors</code> -- the number of unique contributors for each data point.</p> </li> <li> <p> <code>MaxContributorValue</code> -- the value of the top contributor for each data point. The identity of the contributor might change for each data point in the graph.</p> <p>If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the rule's <code>Value</code>, during that period.</p> </li> <li> <p> <code>SampleCount</code> -- the number of data points matched by the rule.</p> </li> <li> <p> <code>Sum</code> -- the sum of the values from all contributors during the time period represented by that data point.</p> </li> <li> <p> <code>Minimum</code> -- the minimum value from a single observation during the time period represented by that data point.</p> </li> <li> <p> <code>Maximum</code> -- the maximum value from a single observation during the time period represented by that data point.</p> </li> <li> <p> <code>Average</code> -- the average value from all contributors during the time period represented by that data point.</p> </li> </ul>
            order_by: <p>Determines what statistic to use to rank the contributors. Valid values are <code>Sum</code> and <code>Maximum</code>.</p>

        Raises:
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_insight_rule_report_input.GetInsightRuleReportInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_insight_rule_report_output.GetInsightRuleReportOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_insight_rule_report

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_insight_rule_report.get_insight_rule_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_insight_rule_report_input.GetInsightRuleReportInput = {}
        if rule_name is not None:
            input_["rule_name"] = rule_name
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if period is not None:
            input_["period"] = period
        if max_contributor_count is not None:
            input_["max_contributor_count"] = max_contributor_count
        if metrics is not None:
            input_["metrics"] = metrics
        if order_by is not None:
            input_["order_by"] = order_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_metric_data(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        metric_data_queries: Optional[
            "capo_cloudwatch.types.metric_data_queries.MetricDataQueries"
        ] = None,
        start_time: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        scan_by: Optional["capo_cloudwatch.types.scan_by.ScanBy"] = None,
        max_datapoints: Optional[
            "capo_cloudwatch.types.get_metric_data_max_datapoints.GetMetricDataMaxDatapoints"
        ] = None,
        label_options: Optional[
            "capo_cloudwatch.types.label_options.LabelOptions"
        ] = None,
    ) -> "capo_cloudwatch.types.get_metric_data_output.GetMetricDataOutput":
        """<p>You can use the <code>GetMetricData</code> API to retrieve CloudWatch metric values. The operation can also include a CloudWatch Metrics Insights query, and one or more metric math functions.</p> <p>A <code>GetMetricData</code> operation that does not include a query can retrieve as many as 500 different metrics in a single request, with a total of as many as 100,800 data points. You can also optionally perform metric math expressions on the values of the returned statistics, to create new time series that represent new insights into your data. For example, using Lambda metrics, you could divide the Errors metric by the Invocations metric to get an error rate time series. For more information about metric math expressions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax">Metric Math Syntax and Functions</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>If you include a Metrics Insights query, each <code>GetMetricData</code> operation can include only one query. But the same <code>GetMetricData</code> operation can also retrieve other metrics. Metrics Insights queries can query the most recent two weeks of metric data. For alarm condition evaluations, Metrics Insights queries can query only the most recent three hours of metric data. For more information about Metrics Insights, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html">Query your metrics with CloudWatch Metrics Insights</a>.</p> <p>Calls to the <code>GetMetricData</code> API have a different pricing structure than calls to <code>GetMetricStatistics</code>. For more information about pricing, see <a href="https://aws.amazon.com/cloudwatch/pricing/">Amazon CloudWatch Pricing</a>.</p> <p>Amazon CloudWatch retains metric data as follows:</p> <ul> <li> <p>Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a <code>StorageResolution</code> of 1.</p> </li> <li> <p>Data points with a period of 60 seconds (1-minute) are available for 15 days.</p> </li> <li> <p>Data points with a period of 300 seconds (5-minute) are available for 63 days.</p> </li> <li> <p>Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).</p> </li> </ul> <p>Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.</p> <p>If you omit <code>Unit</code> in your request, all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.</p> <p> <b>Using Metrics Insights queries with metric math</b> </p> <p>You can't mix a Metric Insights query and metric math syntax in the same expression, but you can reference results from a Metrics Insights query within other Metric math expressions. A Metrics Insights query without a <b>GROUP BY</b> clause returns a single time-series (TS), and can be used as input for a metric math expression that expects a single time series. A Metrics Insights query with a <b>GROUP BY</b> clause returns an array of time-series (TS[]), and can be used as input for a metric math expression that expects an array of time series. </p>

        Args:
            metric_data_queries: <p>The metric queries to be returned. A single <code>GetMetricData</code> call can include as many as 500 <code>MetricDataQuery</code> structures. Each of these structures can specify either a metric to retrieve, a Metrics Insights query, or a math expression to perform on retrieved data. </p>
            start_time: <p>The time stamp indicating the earliest data to be returned.</p> <p>The value specified is inclusive; results include data points with the specified time stamp. </p> <p>CloudWatch rounds the specified time stamp as follows:</p> <ul> <li> <p>Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.</p> </li> <li> <p>Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.</p> </li> <li> <p>Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.</p> </li> </ul> <p>If you set <code>Period</code> to 5, 10, 20, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, 20-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. </p> <p>For better performance, specify <code>StartTime</code> and <code>EndTime</code> values that align with the value of the metric's <code>Period</code> and sync up with the beginning and end of an hour. For example, if the <code>Period</code> of a metric is 5 minutes, specifying 12:05 or 12:30 as <code>StartTime</code> can get a faster response from CloudWatch than setting 12:07 or 12:29 as the <code>StartTime</code>.</p>
            end_time: <p>The time stamp indicating the latest data to be returned.</p> <p>The value specified is exclusive; results include data points up to the specified time stamp.</p> <p>For better performance, specify <code>StartTime</code> and <code>EndTime</code> values that align with the value of the metric's <code>Period</code> and sync up with the beginning and end of an hour. For example, if the <code>Period</code> of a metric is 5 minutes, specifying 12:05 or 12:30 as <code>EndTime</code> can get a faster response from CloudWatch than setting 12:07 or 12:29 as the <code>EndTime</code>.</p>
            next_token: <p>Include this value, if it was returned by the previous <code>GetMetricData</code> operation, to get the next set of data points.</p>
            scan_by: <p>The order in which data points should be returned. <code>TimestampDescending</code> returns the newest data first and paginates when the <code>MaxDatapoints</code> limit is reached. <code>TimestampAscending</code> returns the oldest data first and paginates when the <code>MaxDatapoints</code> limit is reached.</p> <p>If you omit this parameter, the default of <code>TimestampDescending</code> is used.</p>
            max_datapoints: <p>The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used.</p>
            label_options: <p>This structure includes the <code>Timezone</code> parameter, which you can use to specify your time zone so that the labels of returned data display the correct time for your time zone. </p>

        Raises:
            capo_cloudwatch.errors.invalid_next_token.InvalidNextToken: <p>The next token specified is invalid.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_metric_data_input.GetMetricDataInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_metric_data_output.GetMetricDataOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_metric_data

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_metric_data.get_metric_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_metric_data_input.GetMetricDataInput = {}
        if metric_data_queries is not None:
            input_["metric_data_queries"] = metric_data_queries
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if scan_by is not None:
            input_["scan_by"] = scan_by
        if max_datapoints is not None:
            input_["max_datapoints"] = max_datapoints
        if label_options is not None:
            input_["label_options"] = label_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_metric_data(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        metric_data_queries: Optional[
            "capo_cloudwatch.types.metric_data_queries.MetricDataQueries"
        ] = None,
        start_time: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        scan_by: Optional["capo_cloudwatch.types.scan_by.ScanBy"] = None,
        max_datapoints: Optional[
            "capo_cloudwatch.types.get_metric_data_max_datapoints.GetMetricDataMaxDatapoints"
        ] = None,
        label_options: Optional[
            "capo_cloudwatch.types.label_options.LabelOptions"
        ] = None,
    ) -> "Iterator[capo_cloudwatch.types.get_metric_data_output.GetMetricDataOutput]":
        _token = next_token
        while True:
            _response = self.get_metric_data(
                config_overrides=config_overrides,
                metric_data_queries=metric_data_queries,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                scan_by=scan_by,
                max_datapoints=max_datapoints,
                label_options=label_options,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_metric_statistics(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        metric_name: Optional["capo_cloudwatch.types.metric_name.MetricName"] = None,
        dimensions: Optional["capo_cloudwatch.types.dimensions.Dimensions"] = None,
        start_time: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        period: Optional["capo_cloudwatch.types.period.Period"] = None,
        statistics: Optional["capo_cloudwatch.types.statistics.Statistics"] = None,
        extended_statistics: Optional[
            "capo_cloudwatch.types.extended_statistics.ExtendedStatistics"
        ] = None,
        unit: Optional["capo_cloudwatch.types.standard_unit.StandardUnit"] = None,
    ) -> "capo_cloudwatch.types.get_metric_statistics_output.GetMetricStatisticsOutput":
        """<p>Gets statistics for the specified metric.</p> <p>The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. Data points are not returned in chronological order.</p> <p>CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned.</p> <p>CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:</p> <ul> <li> <p>The SampleCount value of the statistic set is 1.</p> </li> <li> <p>The Min and the Max values of the statistic set are equal.</p> </li> </ul> <p>Percentile statistics are not available for metrics when any of the metric values are negative numbers.</p> <p>Amazon CloudWatch retains metric data as follows:</p> <ul> <li> <p>Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a <code>StorageResolution</code> of 1.</p> </li> <li> <p>Data points with a period of 60 seconds (1-minute) are available for 15 days.</p> </li> <li> <p>Data points with a period of 300 seconds (5-minute) are available for 63 days.</p> </li> <li> <p>Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).</p> </li> </ul> <p>Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.</p> <p>CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.</p> <p>For information about metrics and dimensions supported by Amazon Web Services services, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html">Amazon CloudWatch Metrics and Dimensions Reference</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            namespace: <p>The namespace of the metric, with or without spaces.</p>
            metric_name: <p>The name of the metric, with or without spaces.</p>
            dimensions: <p>The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a specific combination of dimensions was not published, you can't retrieve statistics for it. You must specify the same dimensions that were used when the metrics were created. For an example, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#dimension-combinations">Dimension Combinations</a> in the <i>Amazon CloudWatch User Guide</i>. For more information about specifying dimensions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html">Publishing Metrics</a> in the <i>Amazon CloudWatch User Guide</i>.</p>
            start_time: <p>The time stamp that determines the first data point to return. Start times are evaluated relative to the time that CloudWatch receives the request.</p> <p>The value specified is inclusive; results include data points with the specified time stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).</p> <p>CloudWatch rounds the specified time stamp as follows:</p> <ul> <li> <p>Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.</p> </li> <li> <p>Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.</p> </li> <li> <p>Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.</p> </li> </ul> <p>If you set <code>Period</code> to 5, 10, 20, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, 20-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. </p>
            end_time: <p>The time stamp that determines the last data point to return.</p> <p>The value specified is exclusive; results include data points up to the specified time stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).</p>
            period: <p>The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 20, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a <code>PutMetricData</code> call that includes a <code>StorageResolution</code> of 1 second.</p> <p>If the <code>StartTime</code> parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:</p> <ul> <li> <p>Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).</p> </li> <li> <p>Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).</p> </li> <li> <p>Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).</p> </li> </ul>
            statistics: <p>The metric statistics, other than percentile. For percentile statistics, use <code>ExtendedStatistics</code>. When calling <code>GetMetricStatistics</code>, you must specify either <code>Statistics</code> or <code>ExtendedStatistics</code>, but not both.</p>
            extended_statistics: <p>The percentile statistics. Specify values between p0.0 and p100. When calling <code>GetMetricStatistics</code>, you must specify either <code>Statistics</code> or <code>ExtendedStatistics</code>, but not both. Percentile statistics are not available for metrics when any of the metric values are negative numbers.</p>
            unit: <p>The unit for a given metric. If you omit <code>Unit</code>, all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Parameters were used together that cannot be used together.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_metric_statistics_input.GetMetricStatisticsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_metric_statistics_output.GetMetricStatisticsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_metric_statistics

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_metric_statistics.get_metric_statistics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_metric_statistics_input.GetMetricStatisticsInput = {}
        if namespace is not None:
            input_["namespace"] = namespace
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if dimensions is not None:
            input_["dimensions"] = dimensions
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if period is not None:
            input_["period"] = period
        if statistics is not None:
            input_["statistics"] = statistics
        if extended_statistics is not None:
            input_["extended_statistics"] = extended_statistics
        if unit is not None:
            input_["unit"] = unit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_metric_stream(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        name: Optional[
            "capo_cloudwatch.types.metric_stream_name.MetricStreamName"
        ] = None,
    ) -> "capo_cloudwatch.types.get_metric_stream_output.GetMetricStreamOutput":
        """<p>Returns information about the metric stream that you specify.</p>

        Args:
            name: <p>The name of the metric stream to retrieve information about.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Parameters were used together that cannot be used together.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_metric_stream_input.GetMetricStreamInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_metric_stream_output.GetMetricStreamOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_metric_stream

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_metric_stream.get_metric_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_metric_stream_input.GetMetricStreamInput = {}
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_metric_widget_image(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        metric_widget: Optional[
            "capo_cloudwatch.types.metric_widget.MetricWidget"
        ] = None,
        output_format: Optional[
            "capo_cloudwatch.types.output_format.OutputFormat"
        ] = None,
    ) -> "capo_cloudwatch.types.get_metric_widget_image_output.GetMetricWidgetImageOutput":
        """<p>You can use the <code>GetMetricWidgetImage</code> API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image. You can then embed this image into your services and products, such as wiki pages, reports, and documents. You could also retrieve images regularly, such as every minute, and create your own custom live dashboard.</p> <p>The graph you retrieve can include all CloudWatch metric graph features, including metric math and horizontal and vertical annotations.</p> <p>There is a limit of 20 transactions per second for this API. Each <code>GetMetricWidgetImage</code> action has the following limits:</p> <ul> <li> <p>As many as 100 metrics in the graph.</p> </li> <li> <p>Up to 100 KB uncompressed payload.</p> </li> </ul>

        Args:
            metric_widget: <p>A JSON string that defines the bitmap graph to be retrieved. The string includes the metrics to include in the graph, statistics, annotations, title, axis limits, and so on. You can include only one <code>MetricWidget</code> parameter in each <code>GetMetricWidgetImage</code> call.</p> <p>For more information about the syntax of <code>MetricWidget</code> see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Widget-Structure.html">GetMetricWidgetImage: Metric Widget Structure and Syntax</a>.</p> <p>If any metric on the graph could not load all the requested data points, an orange triangle with an exclamation point appears next to the graph legend.</p>
            output_format: <p>The format of the resulting image. Only PNG images are supported.</p> <p>The default is <code>png</code>. If you specify <code>png</code>, the API returns an HTTP response with the content-type set to <code>text/xml</code>. The image data is in a <code>MetricWidgetImage</code> field. For example:</p> <p> <code> <GetMetricWidgetImageResponse xmlns=<URLstring>></code> </p> <p> <code> <GetMetricWidgetImageResult></code> </p> <p> <code> <MetricWidgetImage></code> </p> <p> <code> iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip...</code> </p> <p> <code> </MetricWidgetImage></code> </p> <p> <code> </GetMetricWidgetImageResult></code> </p> <p> <code> <ResponseMetadata></code> </p> <p> <code> <RequestId>6f0d4192-4d42-11e8-82c1-f539a07e0e3b</RequestId></code> </p> <p> <code> </ResponseMetadata></code> </p> <p> <code></GetMetricWidgetImageResponse></code> </p> <p>The <code>image/png</code> setting is intended only for custom HTTP requests. For most use cases, and all actions using an Amazon Web Services SDK, you should use <code>png</code>. If you specify <code>image/png</code>, the HTTP response has a content-type set to <code>image/png</code>, and the body of the response is a PNG image.</p>

        Raises:
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_metric_widget_image_input.GetMetricWidgetImageInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_metric_widget_image_output.GetMetricWidgetImageOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_metric_widget_image

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_metric_widget_image.get_metric_widget_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_metric_widget_image_input.GetMetricWidgetImageInput = {}
        if metric_widget is not None:
            input_["metric_widget"] = metric_widget
        if output_format is not None:
            input_["output_format"] = output_format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_o_tel_enrichment(
        self, *, config_overrides: Optional[CloudWatchClientConfig] = None
    ) -> "capo_cloudwatch.types.get_o_tel_enrichment_output.GetOTelEnrichmentOutput":
        """<p>Returns the current status of vended metric enrichment for the account, including whether CloudWatch vended metrics are enriched with resource ARN and resource tag labels and queryable using PromQL. For the list of supported resources, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html">Supported Amazon Web Services infrastructure metrics</a>.</p>

        Raises:
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_o_tel_enrichment_input.GetOTelEnrichmentInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_o_tel_enrichment_output.GetOTelEnrichmentOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_o_tel_enrichment

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_o_tel_enrichment.get_o_tel_enrichment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_o_tel_enrichment_input.GetOTelEnrichmentInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_metrics_configuration(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        resource_arn: Optional["capo_cloudwatch.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_cloudwatch.types.get_resource_metrics_configuration_output.GetResourceMetricsConfigurationOutput":
        """<p>Retrieves the current resource metrics configuration for an Amazon Web Services resource. The response includes the resource ARN, any metric selections, and the times at which the configuration was created and last updated.</p> <p>This operation returns a <code>ResourceNotFoundException</code> if no resource metrics configuration exists for the specified resource ARN. To create a configuration, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html">CreateResourceMetricsConfiguration</a>.</p> <p>To retrieve a resource metrics configuration, you must have the <code>cloudwatch:GetResourceMetricsConfiguration</code> permission. For information about scoping this permission to specific resources, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html">Condition keys for resource metrics configuration access</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to retrieve the resource metrics configuration for.</p>

        Raises:
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.get_resource_metrics_configuration_input.GetResourceMetricsConfigurationInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.get_resource_metrics_configuration_output.GetResourceMetricsConfigurationOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.get_resource_metrics_configuration

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.get_resource_metrics_configuration.get_resource_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.get_resource_metrics_configuration_input.GetResourceMetricsConfigurationInput = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_alarm_mute_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_name: Optional["capo_cloudwatch.types.name.Name"] = None,
        statuses: Optional[
            "capo_cloudwatch.types.alarm_mute_rule_statuses.AlarmMuteRuleStatuses"
        ] = None,
        max_records: Optional["capo_cloudwatch.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch.types.list_alarm_mute_rules_output.ListAlarmMuteRulesOutput":
        """<p>Lists alarm mute rules in your Amazon Web Services account and region.</p> <p>You can filter the results by alarm name to find all mute rules targeting a specific alarm, or by status to find rules that are scheduled, active, or expired.</p> <p>This operation supports pagination for accounts with many mute rules. Use the <code>MaxRecords</code> and <code>NextToken</code> parameters to retrieve results in multiple calls.</p> <p> <b>Permissions</b> </p> <p>To list mute rules, you need the <code>cloudwatch:ListAlarmMuteRules</code> permission.</p>

        Args:
            alarm_name: <p>Filter results to show only mute rules that target the specified alarm name.</p>
            statuses: <p>Filter results to show only mute rules with the specified statuses. Valid values are <code>SCHEDULED</code>, <code>ACTIVE</code>, or <code>EXPIRED</code>.</p>
            max_records: <p>The maximum number of mute rules to return in one call. The default is 50.</p>
            next_token: <p>The token returned from a previous call to indicate where to continue retrieving results.</p>

        Raises:
            capo_cloudwatch.errors.invalid_next_token.InvalidNextToken: <p>The next token specified is invalid.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.list_alarm_mute_rules_input.ListAlarmMuteRulesInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.list_alarm_mute_rules_output.ListAlarmMuteRulesOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.list_alarm_mute_rules

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.list_alarm_mute_rules.list_alarm_mute_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.list_alarm_mute_rules_input.ListAlarmMuteRulesInput = {}
        if alarm_name is not None:
            input_["alarm_name"] = alarm_name
        if statuses is not None:
            input_["statuses"] = statuses
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_alarm_mute_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_name: Optional["capo_cloudwatch.types.name.Name"] = None,
        statuses: Optional[
            "capo_cloudwatch.types.alarm_mute_rule_statuses.AlarmMuteRuleStatuses"
        ] = None,
        max_records: Optional["capo_cloudwatch.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudwatch.types.alarm_mute_rule_summary.AlarmMuteRuleSummary]":
        _token = next_token
        while True:
            _response = self.list_alarm_mute_rules(
                config_overrides=config_overrides,
                alarm_name=alarm_name,
                statuses=statuses,
                max_records=max_records,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("alarm_mute_rule_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_dashboards(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        dashboard_name_prefix: Optional[
            "capo_cloudwatch.types.dashboard_name_prefix.DashboardNamePrefix"
        ] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch.types.list_dashboards_output.ListDashboardsOutput":
        """<p>Returns a list of the dashboards for your account. If you include <code>DashboardNamePrefix</code>, only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed. </p> <p> <code>ListDashboards</code> returns up to 1000 results on one page. If there are more than 1000 dashboards, you can call <code>ListDashboards</code> again and include the value you received for <code>NextToken</code> in the first call, to receive the next 1000 results.</p> <p>You might have recently enabled an <a href="https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#optinregion">opt-in Region (Region that is disabled by default)</a> for your account. In that Region, <code>ListDashboards</code> can return an access denied error for up to 24 hours after you enable the Region. This delay occurs while dashboard data propagates. The error does not indicate a problem with your permissions. Because dashboards are global, you can call <code>ListDashboards</code> in any other enabled Region, or retry after propagation completes.</p>

        Args:
            dashboard_name_prefix: <p>If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, ".", "-", and "_". </p>
            next_token: <p>The token returned by a previous call to indicate that there is more data available.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.list_dashboards_input.ListDashboardsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.list_dashboards_output.ListDashboardsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.list_dashboards

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.list_dashboards.list_dashboards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.list_dashboards_input.ListDashboardsInput = {}
        if dashboard_name_prefix is not None:
            input_["dashboard_name_prefix"] = dashboard_name_prefix
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_dashboards(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        dashboard_name_prefix: Optional[
            "capo_cloudwatch.types.dashboard_name_prefix.DashboardNamePrefix"
        ] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudwatch.types.dashboard_entry.DashboardEntry]":
        _token = next_token
        while True:
            _response = self.list_dashboards(
                config_overrides=config_overrides,
                dashboard_name_prefix=dashboard_name_prefix,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dashboard_entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_managed_insight_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        resource_arn: Optional[
            "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch.types.insight_rule_max_results.InsightRuleMaxResults"
        ] = None,
    ) -> "capo_cloudwatch.types.list_managed_insight_rules_output.ListManagedInsightRulesOutput":
        """<p> Returns a list that contains the number of managed Contributor Insights rules in your account. </p>

        Args:
            resource_arn: <p> The ARN of an Amazon Web Services resource that has managed Contributor Insights rules. </p>
            next_token: <p> Include this value to get the next set of rules if the value was returned by the previous operation. </p>
            max_results: <p> The maximum number of results to return in one operation. If you omit this parameter, the default number is used. The default number is <code>100</code>. </p>

        Raises:
            capo_cloudwatch.errors.invalid_next_token.InvalidNextToken: <p>The next token specified is invalid.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.list_managed_insight_rules_input.ListManagedInsightRulesInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.list_managed_insight_rules_output.ListManagedInsightRulesOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.list_managed_insight_rules

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.list_managed_insight_rules.list_managed_insight_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.list_managed_insight_rules_input.ListManagedInsightRulesInput = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_managed_insight_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        resource_arn: Optional[
            "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch.types.insight_rule_max_results.InsightRuleMaxResults"
        ] = None,
    ) -> "Iterator[capo_cloudwatch.types.list_managed_insight_rules_output.ListManagedInsightRulesOutput]":
        _token = next_token
        while True:
            _response = self.list_managed_insight_rules(
                config_overrides=config_overrides,
                resource_arn=resource_arn,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_metrics(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        metric_name: Optional["capo_cloudwatch.types.metric_name.MetricName"] = None,
        dimensions: Optional[
            "capo_cloudwatch.types.dimension_filters.DimensionFilters"
        ] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        recently_active: Optional[
            "capo_cloudwatch.types.recently_active.RecentlyActive"
        ] = None,
        include_linked_accounts: Optional[
            "capo_cloudwatch.types.include_linked_accounts.IncludeLinkedAccounts"
        ] = None,
        owning_account: Optional["capo_cloudwatch.types.account_id.AccountId"] = None,
    ) -> "capo_cloudwatch.types.list_metrics_output.ListMetricsOutput":
        """<p>List the specified metrics. You can use the returned metrics with <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html">GetMetricData</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html">GetMetricStatistics</a> to get statistical data.</p> <p>Up to 500 results are returned for any one call. To retrieve additional results, use the returned token with subsequent calls.</p> <p>After you create a metric, allow up to 15 minutes for the metric to appear. To see metric statistics sooner, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html">GetMetricData</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html">GetMetricStatistics</a>.</p> <p>If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view metrics from the linked source accounts. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p> <p> <code>ListMetrics</code> doesn't return information about metrics if those metrics haven't reported data in the past two weeks. To retrieve those metrics, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html">GetMetricData</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html">GetMetricStatistics</a>.</p>

        Args:
            namespace: <p>The metric namespace to filter against. Only the namespace that matches exactly will be returned.</p>
            metric_name: <p>The name of the metric to filter against. Only the metrics with names that match exactly will be returned.</p>
            dimensions: <p>The dimensions to filter against. Only the dimension with names that match exactly will be returned. If you specify one dimension name and a metric has that dimension and also other dimensions, it will be returned.</p>
            next_token: <p>The token returned by a previous call to indicate that there is more data available.</p>
            recently_active: <p>To filter the results to show only metrics that have had data points published in the past three hours, specify this parameter with a value of <code>PT3H</code>. This is the only valid value for this parameter.</p> <p>The results that are returned are an approximation of the value you specify. There is a low probability that the returned results include metrics with last published data as much as 50 minutes more than the specified time interval.</p>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include metrics from source accounts in the returned data.</p> <p>The default is <code>false</code>.</p>
            owning_account: <p>When you use this operation in a monitoring account, use this field to return metrics only from one source account. To do so, specify that source account ID in this field, and also specify <code>true</code> for <code>IncludeLinkedAccounts</code>.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.list_metrics_input.ListMetricsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.list_metrics_output.ListMetricsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.list_metrics

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.list_metrics.list_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.list_metrics_input.ListMetricsInput = {}
        if namespace is not None:
            input_["namespace"] = namespace
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if dimensions is not None:
            input_["dimensions"] = dimensions
        if next_token is not None:
            input_["next_token"] = next_token
        if recently_active is not None:
            input_["recently_active"] = recently_active
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if owning_account is not None:
            input_["owning_account"] = owning_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_metrics(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        metric_name: Optional["capo_cloudwatch.types.metric_name.MetricName"] = None,
        dimensions: Optional[
            "capo_cloudwatch.types.dimension_filters.DimensionFilters"
        ] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        recently_active: Optional[
            "capo_cloudwatch.types.recently_active.RecentlyActive"
        ] = None,
        include_linked_accounts: Optional[
            "capo_cloudwatch.types.include_linked_accounts.IncludeLinkedAccounts"
        ] = None,
        owning_account: Optional["capo_cloudwatch.types.account_id.AccountId"] = None,
    ) -> "Iterator[capo_cloudwatch.types.list_metrics_output.ListMetricsOutput]":
        _token = next_token
        while True:
            _response = self.list_metrics(
                config_overrides=config_overrides,
                namespace=namespace,
                metric_name=metric_name,
                dimensions=dimensions,
                next_token=_token,
                recently_active=recently_active,
                include_linked_accounts=include_linked_accounts,
                owning_account=owning_account,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_metric_streams(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch.types.list_metric_streams_max_results.ListMetricStreamsMaxResults"
        ] = None,
    ) -> "capo_cloudwatch.types.list_metric_streams_output.ListMetricStreamsOutput":
        """<p>Returns a list of metric streams in this account.</p>

        Args:
            next_token: <p>Include this value, if it was returned by the previous call, to get the next set of metric streams.</p>
            max_results: <p>The maximum number of results to return in one operation.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_next_token.InvalidNextToken: <p>The next token specified is invalid.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.list_metric_streams_input.ListMetricStreamsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.list_metric_streams_output.ListMetricStreamsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.list_metric_streams

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.list_metric_streams.list_metric_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.list_metric_streams_input.ListMetricStreamsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_metric_streams(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        next_token: Optional["capo_cloudwatch.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch.types.list_metric_streams_max_results.ListMetricStreamsMaxResults"
        ] = None,
    ) -> "Iterator[capo_cloudwatch.types.list_metric_streams_output.ListMetricStreamsOutput]":
        _token = next_token
        while True:
            _response = self.list_metric_streams(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        resource_arn: Optional[
            "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
        ] = None,
    ) -> (
        "capo_cloudwatch.types.list_tags_for_resource_output.ListTagsForResourceOutput"
    ):
        """<p>Displays the tags associated with a CloudWatch resource. Currently, alarms, dashboards, metric streams and Contributor Insights rules support tagging.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch resource that you want to view tags for.</p> <p>The ARN format of an alarm is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:alarm:<i>alarm-name</i> </code> </p> <p>The ARN format of a Contributor Insights rule is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:insight-rule/<i>insight-rule-name</i> </code> </p> <p>The ARN format of a dashboard is <code>arn:aws:cloudwatch::<i>account-id</i>:dashboard/<i>dashboard-name</i> </code> </p> <p>The ARN format of a metric stream is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:metric-stream/<i>metric-stream-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.list_tags_for_resource

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.list_tags_for_resource_input.ListTagsForResourceInput = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_alarm_mute_rule(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        name: Optional["capo_cloudwatch.types.name.Name"] = None,
        description: Optional[
            "capo_cloudwatch.types.alarm_description.AlarmDescription"
        ] = None,
        rule: Optional["capo_cloudwatch.types.rule.Rule"] = None,
        mute_targets: Optional["capo_cloudwatch.types.mute_targets.MuteTargets"] = None,
        tags: Optional["capo_cloudwatch.types.tag_list.TagList"] = None,
        start_date: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
        expire_date: Optional["capo_cloudwatch.types.timestamp.Timestamp"] = None,
    ) -> None:
        """<p>Creates or updates an alarm mute rule.</p> <p>Alarm mute rules automatically mute alarm actions during predefined time windows. When a mute rule is active, targeted alarms continue to evaluate metrics and transition between states, but their configured actions (such as Amazon SNS notifications or Auto Scaling actions) are muted.</p> <p>You can create mute rules with recurring schedules using <code>cron</code> expressions or one-time mute windows using <code>at</code> expressions. Each mute rule can target up to 100 specific alarms by name.</p> <p>If you specify a rule name that already exists, this operation updates the existing rule with the new configuration.</p> <p> <b>Permissions</b> </p> <p>To create or update a mute rule, you must have the <code>cloudwatch:PutAlarmMuteRule</code> permission on two types of resources: the alarm mute rule resource itself, and each alarm that the rule targets.</p> <p>For example, If you want to allow a user to create mute rules that target only specific alarms named "WebServerCPUAlarm" and "DatabaseConnectionAlarm", you would create an IAM policy with one statement granting <code>cloudwatch:PutAlarmMuteRule</code> on the alarm mute rule resource (<code>arn:aws:cloudwatch:[REGION]:123456789012:alarm-mute-rule:*</code>), and another statement granting <code>cloudwatch:PutAlarmMuteRule</code> on the targeted alarm resources (<code>arn:aws:cloudwatch:[REGION]:123456789012:alarm:WebServerCPUAlarm</code> and <code>arn:aws:cloudwatch:[REGION]:123456789012:alarm:DatabaseConnectionAlarm</code>).</p> <p>You can also use IAM policy conditions to allow targeting alarms based on resource tags. For example, you can restrict users to create/update mute rules to only target alarms that have a specific tag key-value pair, such as <code>Team=TeamA</code>.</p>

        Args:
            name: <p>The name of the alarm mute rule. This name must be unique within your Amazon Web Services account and region.</p>
            description: <p>A description of the alarm mute rule that helps you identify its purpose.</p>
            rule: <p>The configuration that defines when and how long alarms should be muted.</p>
            mute_targets: <p>Specifies which alarms this rule applies to.</p>
            tags: <p>A list of key-value pairs to associate with the alarm mute rule. You can use tags to categorize and manage your mute rules.</p>
            start_date: <p>The date and time after which the mute rule takes effect, specified as a timestamp in ISO 8601 format (for example, <code>2026-04-15T08:00:00Z</code>). If not specified, the mute rule takes effect immediately upon creation and the mutes are applied as per the schedule expression.</p>
            expire_date: <p>The date and time when the mute rule expires and is no longer evaluated, specified as a timestamp in ISO 8601 format (for example, <code>2026-12-31T23:59:59Z</code>). After this time, the rule status becomes EXPIRED and will no longer mute the targeted alarms.</p>

        Raises:
            capo_cloudwatch.errors.limit_exceeded_fault.LimitExceededFault: <p>The quota for alarms for this customer has already been reached.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_alarm_mute_rule_input.PutAlarmMuteRuleInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_alarm_mute_rule

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_alarm_mute_rule.put_alarm_mute_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_alarm_mute_rule_input.PutAlarmMuteRuleInput = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule
        if mute_targets is not None:
            input_["mute_targets"] = mute_targets
        if tags is not None:
            input_["tags"] = tags
        if start_date is not None:
            input_["start_date"] = start_date
        if expire_date is not None:
            input_["expire_date"] = expire_date

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_anomaly_detector(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        metric_name: Optional["capo_cloudwatch.types.metric_name.MetricName"] = None,
        dimensions: Optional["capo_cloudwatch.types.dimensions.Dimensions"] = None,
        stat: Optional[
            "capo_cloudwatch.types.anomaly_detector_metric_stat.AnomalyDetectorMetricStat"
        ] = None,
        configuration: Optional[
            "capo_cloudwatch.types.anomaly_detector_configuration.AnomalyDetectorConfiguration"
        ] = None,
        metric_characteristics: Optional[
            "capo_cloudwatch.types.metric_characteristics.MetricCharacteristics"
        ] = None,
        single_metric_anomaly_detector: Optional[
            "capo_cloudwatch.types.single_metric_anomaly_detector.SingleMetricAnomalyDetector"
        ] = None,
        metric_math_anomaly_detector: Optional[
            "capo_cloudwatch.types.metric_math_anomaly_detector.MetricMathAnomalyDetector"
        ] = None,
    ) -> "capo_cloudwatch.types.put_anomaly_detector_output.PutAnomalyDetectorOutput":
        """<p>Creates an anomaly detection model for a CloudWatch metric. You can use the model to display a band of expected normal values when the metric is graphed.</p> <p>If you have enabled unified cross-account observability, and this account is a monitoring account, the metric can be in the same account or a source account. You can specify the account ID in the object you specify in the <code>SingleMetricAnomalyDetector</code> parameter.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html">CloudWatch Anomaly Detection</a>.</p>

        Args:
            namespace: <p>The namespace of the metric to create the anomaly detection model for.</p>
            metric_name: <p>The name of the metric to create the anomaly detection model for.</p>
            dimensions: <p>The metric dimensions to create the anomaly detection model for.</p>
            stat: <p>The statistic to use for the metric and the anomaly detection model.</p>
            configuration: <p>The configuration specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model. You can specify as many as 10 time ranges.</p> <p>The configuration can also include the time zone to use for the metric.</p>
            metric_characteristics: <p>Use this object to include parameters to provide information about your metric to CloudWatch to help it build more accurate anomaly detection models. Currently, it includes the <code>PeriodicSpikes</code> parameter.</p>
            single_metric_anomaly_detector: <p>A single metric anomaly detector to be created.</p> <p>When using <code>SingleMetricAnomalyDetector</code>, you cannot include the following parameters in the same operation:</p> <ul> <li> <p> <code>Dimensions</code> </p> </li> <li> <p> <code>MetricName</code> </p> </li> <li> <p> <code>Namespace</code> </p> </li> <li> <p> <code>Stat</code> </p> </li> <li> <p>the <code>MetricMathAnomalyDetector</code> parameters of <code>PutAnomalyDetectorInput</code> </p> </li> </ul> <p>Instead, specify the single metric anomaly detector attributes as part of the property <code>SingleMetricAnomalyDetector</code>.</p>
            metric_math_anomaly_detector: <p>The metric math anomaly detector to be created.</p> <p>When using <code>MetricMathAnomalyDetector</code>, you cannot include the following parameters in the same operation:</p> <ul> <li> <p> <code>Dimensions</code> </p> </li> <li> <p> <code>MetricName</code> </p> </li> <li> <p> <code>Namespace</code> </p> </li> <li> <p> <code>Stat</code> </p> </li> <li> <p>the <code>SingleMetricAnomalyDetector</code> parameters of <code>PutAnomalyDetectorInput</code> </p> </li> </ul> <p>Instead, specify the metric math anomaly detector attributes as part of the property <code>MetricMathAnomalyDetector</code>.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Parameters were used together that cannot be used together.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeded one or more limits.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_anomaly_detector_input.PutAnomalyDetectorInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.put_anomaly_detector_output.PutAnomalyDetectorOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_anomaly_detector

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_anomaly_detector.put_anomaly_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_anomaly_detector_input.PutAnomalyDetectorInput = {}
        if namespace is not None:
            input_["namespace"] = namespace
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if dimensions is not None:
            input_["dimensions"] = dimensions
        if stat is not None:
            input_["stat"] = stat
        if configuration is not None:
            input_["configuration"] = configuration
        if metric_characteristics is not None:
            input_["metric_characteristics"] = metric_characteristics
        if single_metric_anomaly_detector is not None:
            input_["single_metric_anomaly_detector"] = single_metric_anomaly_detector
        if metric_math_anomaly_detector is not None:
            input_["metric_math_anomaly_detector"] = metric_math_anomaly_detector

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_composite_alarm(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        actions_enabled: Optional[
            "capo_cloudwatch.types.actions_enabled.ActionsEnabled"
        ] = None,
        alarm_actions: Optional[
            "capo_cloudwatch.types.resource_list.ResourceList"
        ] = None,
        alarm_description: Optional[
            "capo_cloudwatch.types.alarm_description.AlarmDescription"
        ] = None,
        alarm_name: Optional["capo_cloudwatch.types.alarm_name.AlarmName"] = None,
        alarm_rule: Optional["capo_cloudwatch.types.alarm_rule.AlarmRule"] = None,
        insufficient_data_actions: Optional[
            "capo_cloudwatch.types.resource_list.ResourceList"
        ] = None,
        ok_actions: Optional["capo_cloudwatch.types.resource_list.ResourceList"] = None,
        tags: Optional["capo_cloudwatch.types.tag_list.TagList"] = None,
        actions_suppressor: Optional["capo_cloudwatch.types.alarm_arn.AlarmArn"] = None,
        actions_suppressor_wait_period: Optional[
            "capo_cloudwatch.types.suppressor_period.SuppressorPeriod"
        ] = None,
        actions_suppressor_extension_period: Optional[
            "capo_cloudwatch.types.suppressor_period.SuppressorPeriod"
        ] = None,
    ) -> None:
        """<p>Creates or updates a <i>composite alarm</i>. When you create a composite alarm, you specify a rule expression for the alarm that takes into account the alarm states of other alarms that you have created. The composite alarm goes into ALARM state only if all conditions of the rule are met.</p> <p>The alarms specified in a composite alarm's rule expression can include metric alarms and other composite alarms. The rule expression of a composite alarm can include as many as 100 underlying alarms. Any single alarm can be included in the rule expressions of as many as 150 composite alarms.</p> <p>Using composite alarms can reduce alarm noise. You can create multiple metric alarms, and also create a composite alarm and set up alerts only for the composite alarm. For example, you could create a composite alarm that goes into ALARM state only when more than one of the underlying metric alarms are in ALARM state.</p> <p>Composite alarms can take the following actions:</p> <ul> <li> <p>Notify Amazon SNS topics.</p> </li> <li> <p>Invoke Lambda functions.</p> </li> <li> <p>Create OpsItems in Systems Manager Ops Center.</p> </li> <li> <p>Create incidents in Systems Manager Incident Manager.</p> </li> </ul> <note> <p>It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you can't delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.</p> <p>To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the <code>AlarmRule</code> of one of the alarms to <code>false</code>. </p> <p>Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path. </p> </note> <p>When this operation creates an alarm, the alarm state is immediately set to <code>INSUFFICIENT_DATA</code>. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed. For a composite alarm, this initial time after creation is the only time that the alarm can be in <code>INSUFFICIENT_DATA</code> state.</p> <p>When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.</p> <p>To use this operation, you must be signed on with the <code>cloudwatch:PutCompositeAlarm</code> permission that is scoped to <code>*</code>. You can't create a composite alarms if your <code>cloudwatch:PutCompositeAlarm</code> permission has a narrower scope.</p> <p>If you are an IAM user, you must have <code>iam:CreateServiceLinkedRole</code> to create a composite alarm that has Systems Manager OpsItem actions.</p>

        Args:
            actions_enabled: <p>Indicates whether actions should be executed during any changes to the alarm state of the composite alarm. The default is <code>TRUE</code>.</p>
            alarm_actions: <p>The actions to execute when this alarm transitions to the <code>ALARM</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values: ]</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>Systems Manager actions:</b> </p> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i> </code> </p> <p> <b>Start a Amazon Q Developer operational investigation</b> </p> <p> <code>arn:aws:aiops:<i>region</i>:<i>account-id</i>:investigation-group:<i>investigation-group-id</i> </code> </p>
            alarm_description: <p>The description for the composite alarm.</p>
            alarm_name: <p>The name for the composite alarm. This name must be unique within the Region.</p>
            alarm_rule: <p>An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression.</p> <p>You can use either alarm names or ARNs to reference the other alarms that are to be evaluated.</p> <p>Functions can include the following:</p> <ul> <li> <p> <code>ALARM("<i>alarm-name</i> or <i>alarm-ARN</i>")</code> is TRUE if the named alarm is in ALARM state.</p> </li> <li> <p> <code>OK("<i>alarm-name</i> or <i>alarm-ARN</i>")</code> is TRUE if the named alarm is in OK state.</p> </li> <li> <p> <code>INSUFFICIENT_DATA("<i>alarm-name</i> or <i>alarm-ARN</i>")</code> is TRUE if the named alarm is in INSUFFICIENT_DATA state.</p> </li> <li> <p> <code>TRUE</code> always evaluates to TRUE.</p> </li> <li> <p> <code>FALSE</code> always evaluates to FALSE.</p> </li> </ul> <p>TRUE and FALSE are useful for testing a complex <code>AlarmRule</code> structure, and for testing your alarm actions.</p> <p>Alarm names specified in <code>AlarmRule</code> can be surrounded with double-quotes ("), but do not have to be.</p> <p>The following are some examples of <code>AlarmRule</code>:</p> <ul> <li> <p> <code>ALARM(CPUUtilizationTooHigh) AND ALARM(DiskReadOpsTooHigh)</code> specifies that the composite alarm goes into ALARM state only if both CPUUtilizationTooHigh and DiskReadOpsTooHigh alarms are in ALARM state.</p> </li> <li> <p> <code>ALARM(CPUUtilizationTooHigh) AND NOT ALARM(DeploymentInProgress)</code> specifies that the alarm goes to ALARM state if CPUUtilizationTooHigh is in ALARM state and DeploymentInProgress is not in ALARM state. This example reduces alarm noise during a known deployment window.</p> </li> <li> <p> <code>(ALARM(CPUUtilizationTooHigh) OR ALARM(DiskReadOpsTooHigh)) AND OK(NetworkOutTooHigh)</code> goes into ALARM state if CPUUtilizationTooHigh OR DiskReadOpsTooHigh is in ALARM state, and if NetworkOutTooHigh is in OK state. This provides another example of using a composite alarm to prevent noise. This rule ensures that you are not notified with an alarm action on high CPU or disk usage if a known network problem is also occurring.</p> </li> </ul> <p>The <code>AlarmRule</code> can specify as many as 100 "children" alarms. The <code>AlarmRule</code> expression can have as many as 500 elements. Elements are child alarms, TRUE or FALSE statements, and parentheses.</p>
            insufficient_data_actions: <p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values: ]</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul>
            ok_actions: <p>The actions to execute when this alarm transitions to an <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values: ]</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul>
            tags: <p>A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>If you are using this operation to update an existing alarm, any tags you specify in this parameter are ignored. To change the tags of an existing alarm, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html">TagResource</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p>
            actions_suppressor: <p> Actions will be suppressed if the suppressor alarm is in the <code>ALARM</code> state. <code>ActionsSuppressor</code> can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm. </p>
            actions_suppressor_wait_period: <p> The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the <code>ALARM</code> state. After this time, the composite alarm performs its actions. </p> <important> <p> <code>WaitPeriod</code> is required only when <code>ActionsSuppressor</code> is specified. </p> </important>
            actions_suppressor_extension_period: <p> The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the <code>ALARM</code> state. After this time, the composite alarm performs its actions. </p> <important> <p> <code>ExtensionPeriod</code> is required only when <code>ActionsSuppressor</code> is specified. </p> </important>

        Raises:
            capo_cloudwatch.errors.limit_exceeded_fault.LimitExceededFault: <p>The quota for alarms for this customer has already been reached.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_composite_alarm_input.PutCompositeAlarmInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_composite_alarm

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_composite_alarm.put_composite_alarm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_composite_alarm_input.PutCompositeAlarmInput = {}
        if actions_enabled is not None:
            input_["actions_enabled"] = actions_enabled
        if alarm_actions is not None:
            input_["alarm_actions"] = alarm_actions
        if alarm_description is not None:
            input_["alarm_description"] = alarm_description
        if alarm_name is not None:
            input_["alarm_name"] = alarm_name
        if alarm_rule is not None:
            input_["alarm_rule"] = alarm_rule
        if insufficient_data_actions is not None:
            input_["insufficient_data_actions"] = insufficient_data_actions
        if ok_actions is not None:
            input_["ok_actions"] = ok_actions
        if tags is not None:
            input_["tags"] = tags
        if actions_suppressor is not None:
            input_["actions_suppressor"] = actions_suppressor
        if actions_suppressor_wait_period is not None:
            input_["actions_suppressor_wait_period"] = actions_suppressor_wait_period
        if actions_suppressor_extension_period is not None:
            input_["actions_suppressor_extension_period"] = (
                actions_suppressor_extension_period
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_dashboard(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        dashboard_name: Optional[
            "capo_cloudwatch.types.dashboard_name.DashboardName"
        ] = None,
        dashboard_body: Optional[
            "capo_cloudwatch.types.dashboard_body.DashboardBody"
        ] = None,
        tags: Optional["capo_cloudwatch.types.tag_list.TagList"] = None,
    ) -> "capo_cloudwatch.types.put_dashboard_output.PutDashboardOutput":
        """<p>Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a dashboard, the entire contents are replaced with what you specify here.</p> <p>All dashboards in your account are global, not region-specific.</p> <p>A simple way to create a dashboard using <code>PutDashboard</code> is to copy an existing dashboard. To copy an existing dashboard using the console, you can load the dashboard and then use the View/edit source command in the Actions menu to display the JSON block for that dashboard. Another way to copy a dashboard is to use <code>GetDashboard</code>, and then use the data returned within <code>DashboardBody</code> as the template for the new dashboard when you call <code>PutDashboard</code>.</p> <p>When you create a dashboard with <code>PutDashboard</code>, a good practice is to add a text widget at the top of the dashboard with a message that the dashboard was created by script and should not be changed in the console. This message could also point console users to the location of the <code>DashboardBody</code> script or the CloudFormation template used to create the dashboard.</p>

        Args:
            dashboard_name: <p>The name of the dashboard. If a dashboard with this name already exists, this call modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, "-", and "_". This parameter is required.</p>
            dashboard_body: <p>The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required.</p> <p>For more information about the syntax, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Dashboard-Body-Structure.html">Dashboard Body Structure and Syntax</a>.</p>
            tags: <p>A list of key-value pairs to associate with the dashboard. You can associate as many as 50 tags with a dashboard.</p> <p>Tags can help you organize and categorize your dashboards. You can also use them to scope user permissions by granting a user permission to access or change only dashboards with certain tag values.</p> <p>You can use this parameter only when creating a new dashboard. If you specify <code>Tags</code> when updating an existing dashboard, the tag updates are ignored. To add or update tags on an existing dashboard, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html">TagResource</a>. To remove tags, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p>

        Raises:
            capo_cloudwatch.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch.errors.dashboard_invalid_input_error.DashboardInvalidInputError: <p>Some part of the dashboard data is invalid.</p>
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_dashboard_input.PutDashboardInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.put_dashboard_output.PutDashboardOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_dashboard

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_dashboard.put_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_dashboard_input.PutDashboardInput = {}
        if dashboard_name is not None:
            input_["dashboard_name"] = dashboard_name
        if dashboard_body is not None:
            input_["dashboard_body"] = dashboard_body
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_insight_rule(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        rule_name: Optional[
            "capo_cloudwatch.types.insight_rule_name.InsightRuleName"
        ] = None,
        rule_state: Optional[
            "capo_cloudwatch.types.insight_rule_state.InsightRuleState"
        ] = None,
        rule_definition: Optional[
            "capo_cloudwatch.types.insight_rule_definition.InsightRuleDefinition"
        ] = None,
        tags: Optional["capo_cloudwatch.types.tag_list.TagList"] = None,
        apply_on_transformed_logs: Optional[
            "capo_cloudwatch.types.insight_rule_on_transformed_logs.InsightRuleOnTransformedLogs"
        ] = None,
    ) -> "capo_cloudwatch.types.put_insight_rule_output.PutInsightRuleOutput":
        """<p>Creates a Contributor Insights rule. Rules evaluate log events in a CloudWatch Logs log group, enabling you to find contributor data for the log events in that log group. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html">Using Contributor Insights to Analyze High-Cardinality Data</a>.</p> <p>If you create a rule, delete it, and then re-create it with the same name, historical data from the first time the rule was created might not be available.</p>

        Args:
            rule_name: <p>A unique name for the rule.</p>
            rule_state: <p>The state of the rule. Valid values are ENABLED and DISABLED.</p>
            rule_definition: <p>The definition of the rule, as a JSON object. For details on the valid syntax, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html">Contributor Insights Rule Syntax</a>.</p>
            tags: <p>A list of key-value pairs to associate with the Contributor Insights rule. You can associate as many as 50 tags with a rule.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.</p> <p>To be able to associate tags with a rule, you must have the <code>cloudwatch:TagResource</code> permission in addition to the <code>cloudwatch:PutInsightRule</code> permission.</p> <p>If you are using this operation to update an existing Contributor Insights rule, any tags you specify in this parameter are ignored. To change the tags of an existing rule, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html">TagResource</a>.</p>
            apply_on_transformed_logs: <p>Specify <code>true</code> to have this rule evaluate log events after they have been transformed by <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html">Log transformation</a>. If you specify <code>true</code>, then the log events in log groups that have transformers will be evaluated by Contributor Insights after being transformed. Log groups that don't have transformers will still have their original log events evaluated by Contributor Insights.</p> <p>The default is <code>false</code> </p> <note> <p>If a log group has a transformer, and transformation fails for some log events, those log events won't be evaluated by Contributor Insights. For information about investigating log transformation failures, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Transformation-Errors-Metrics.html">Transformation metrics and errors</a>.</p> </note>

        Raises:
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeded one or more limits.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_insight_rule_input.PutInsightRuleInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.put_insight_rule_output.PutInsightRuleOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_insight_rule

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_insight_rule.put_insight_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_insight_rule_input.PutInsightRuleInput = {}
        if rule_name is not None:
            input_["rule_name"] = rule_name
        if rule_state is not None:
            input_["rule_state"] = rule_state
        if rule_definition is not None:
            input_["rule_definition"] = rule_definition
        if tags is not None:
            input_["tags"] = tags
        if apply_on_transformed_logs is not None:
            input_["apply_on_transformed_logs"] = apply_on_transformed_logs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_log_alarm(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_name: Optional["capo_cloudwatch.types.alarm_name.AlarmName"] = None,
        alarm_description: Optional[
            "capo_cloudwatch.types.alarm_description.AlarmDescription"
        ] = None,
        scheduled_query_configuration: Optional[
            "capo_cloudwatch.types.scheduled_query_configuration.ScheduledQueryConfiguration"
        ] = None,
        action_log_line_count: Optional[
            "capo_cloudwatch.types.action_log_line_count.ActionLogLineCount"
        ] = None,
        action_log_line_role_arn: Optional[
            "capo_cloudwatch.types.action_log_line_role_arn.ActionLogLineRoleArn"
        ] = None,
        actions_enabled: Optional[
            "capo_cloudwatch.types.actions_enabled.ActionsEnabled"
        ] = None,
        ok_actions: Optional["capo_cloudwatch.types.resource_list.ResourceList"] = None,
        alarm_actions: Optional[
            "capo_cloudwatch.types.resource_list.ResourceList"
        ] = None,
        insufficient_data_actions: Optional[
            "capo_cloudwatch.types.resource_list.ResourceList"
        ] = None,
        query_results_to_evaluate: Optional[
            "capo_cloudwatch.types.query_results_to_evaluate.QueryResultsToEvaluate"
        ] = None,
        query_results_to_alarm: Optional[
            "capo_cloudwatch.types.query_results_to_alarm.QueryResultsToAlarm"
        ] = None,
        threshold: Optional["capo_cloudwatch.types.threshold.Threshold"] = None,
        comparison_operator: Optional[
            "capo_cloudwatch.types.comparison_operator.ComparisonOperator"
        ] = None,
        treat_missing_data: Optional[
            "capo_cloudwatch.types.treat_missing_data.TreatMissingData"
        ] = None,
        tags: Optional["capo_cloudwatch.types.tag_list.TagList"] = None,
        warm_up_configuration: Optional[
            "capo_cloudwatch.types.warm_up_configuration.WarmUpConfiguration"
        ] = None,
    ) -> None:
        """<p>Creates or updates a log alarm. A log alarm evaluates the results of a CloudWatch Logs scheduled query against the configured threshold and comparison operator to determine its state.</p> <p>When you create a log alarm, the operation creates a service-managed CloudWatch Logs scheduled query that runs the query string you provide on the schedule you configure. Each scheduled query execution returns one or more aggregated values determined by the <code>AggregationExpression</code>, and each aggregated value is compared against the alarm <code>Threshold</code> to determine the alarm state. The alarm uses M-out-of-N evaluation: if <code>QueryResultsToAlarm</code> out of the most recent <code>QueryResultsToEvaluate</code> query results breach the threshold, the alarm transitions to <code>ALARM</code>.</p> <p>Log alarms support the alarm states (<code>OK</code>, <code>ALARM</code>, <code>INSUFFICIENT_DATA</code>). Configure transition actions using <code>OKActions</code>, <code>AlarmActions</code>, and <code>InsufficientDataActions</code>.</p> <p>If you call this operation with the name of an existing log alarm, the operation replaces the previous configuration of that alarm.</p> <p> <b>Permissions</b> </p> <p>To create or update a log alarm, you must have the <code>cloudwatch:PutLogAlarm</code> permission. The IAM role specified in <code>ScheduledQueryRoleARN</code> must grant the CloudWatch Alarms service permission to execute scheduled queries on the specified log groups. If you set <code>ActionLogLineCount</code>, the role specified in <code>ActionLogLineRoleArn</code> must grant permission to retrieve log events for inclusion in alarm notifications.</p>

        Args:
            alarm_name: <p>The name for the alarm. This name must be unique within the Amazon Web Services account and Region.</p>
            alarm_description: <p>The description for the alarm.</p>
            scheduled_query_configuration: <p>The configuration of the underlying CloudWatch Logs scheduled query that this alarm evaluates, including the query string, log groups, schedule, and aggregation expression.</p>
            action_log_line_count: <p>The number of log lines from the most recent scheduled query execution to include in alarm action notifications. Valid range is 0 through 50. The default is 0, which means no log lines are included.</p>
            action_log_line_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that CloudWatch assumes to retrieve log events for inclusion in alarm action notifications. Required when <code>ActionLogLineCount</code> is greater than 0.</p>
            actions_enabled: <p>Indicates whether actions should be executed during any changes to the alarm state. The default is <code>true</code>.</p>
            ok_actions: <p>The actions to execute when this alarm transitions to the <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values:</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul>
            alarm_actions: <p>The actions to execute when this alarm transitions to the <code>ALARM</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values:</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>Systems Manager actions:</b> </p> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i> </code> </p>
            insufficient_data_actions: <p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values:</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul>
            query_results_to_evaluate: <p>The number of most recent scheduled query results to evaluate against the threshold (the N in M-of-N evaluation). Valid range is 1 through 100.</p>
            query_results_to_alarm: <p>The number of query results, out of the most recent <code>QueryResultsToEvaluate</code> results, that must breach the threshold to trigger the alarm to transition to <code>ALARM</code> (the M in M-of-N evaluation). Must be less than or equal to <code>QueryResultsToEvaluate</code>.</p>
            threshold: <p>The value to compare with the aggregated query result.</p>
            comparison_operator: <p>The arithmetic operation to use when comparing the aggregated query result and the threshold. The aggregated query result is used as the first operand. Valid values are <code>GreaterThanThreshold</code>, <code>GreaterThanOrEqualToThreshold</code>, <code>LessThanThreshold</code>, and <code>LessThanOrEqualToThreshold</code>.</p>
            treat_missing_data: <p>Sets how this alarm is to handle missing data points. Valid values are <code>breaching</code>, <code>notBreaching</code>, <code>ignore</code>, and <code>missing</code>. If this parameter is omitted, the default behavior of <code>missing</code> is used.</p>
            tags: <p>A list of key-value pairs to associate with the alarm. You can use tags to categorize and manage your alarms.</p>
            warm_up_configuration: <p>The warm-up configuration for the alarm. A warm-up period delays alarm evaluation after you create or update the alarm. The warm-up period reduces alarm noise from missing data while a new resource or service starts publishing data.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html">Alarm warm-up periods</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Raises:
            capo_cloudwatch.errors.limit_exceeded_fault.LimitExceededFault: <p>The quota for alarms for this customer has already been reached.</p>
            capo_cloudwatch.errors.resource_conflict.ResourceConflict: <p>The operation could not be completed because the request conflicts with the current state of the alarm or its underlying scheduled query resource.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_log_alarm_input.PutLogAlarmInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_log_alarm

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_log_alarm.put_log_alarm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_log_alarm_input.PutLogAlarmInput = {}
        if alarm_name is not None:
            input_["alarm_name"] = alarm_name
        if alarm_description is not None:
            input_["alarm_description"] = alarm_description
        if scheduled_query_configuration is not None:
            input_["scheduled_query_configuration"] = scheduled_query_configuration
        if action_log_line_count is not None:
            input_["action_log_line_count"] = action_log_line_count
        if action_log_line_role_arn is not None:
            input_["action_log_line_role_arn"] = action_log_line_role_arn
        if actions_enabled is not None:
            input_["actions_enabled"] = actions_enabled
        if ok_actions is not None:
            input_["ok_actions"] = ok_actions
        if alarm_actions is not None:
            input_["alarm_actions"] = alarm_actions
        if insufficient_data_actions is not None:
            input_["insufficient_data_actions"] = insufficient_data_actions
        if query_results_to_evaluate is not None:
            input_["query_results_to_evaluate"] = query_results_to_evaluate
        if query_results_to_alarm is not None:
            input_["query_results_to_alarm"] = query_results_to_alarm
        if threshold is not None:
            input_["threshold"] = threshold
        if comparison_operator is not None:
            input_["comparison_operator"] = comparison_operator
        if treat_missing_data is not None:
            input_["treat_missing_data"] = treat_missing_data
        if tags is not None:
            input_["tags"] = tags
        if warm_up_configuration is not None:
            input_["warm_up_configuration"] = warm_up_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_managed_insight_rules(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        managed_rules: Optional[
            "capo_cloudwatch.types.managed_rules.ManagedRules"
        ] = None,
    ) -> "capo_cloudwatch.types.put_managed_insight_rules_output.PutManagedInsightRulesOutput":
        """<p> Creates a managed Contributor Insights rule for a specified Amazon Web Services resource. When you enable a managed rule, you create a Contributor Insights rule that collects data from Amazon Web Services services. You cannot edit these rules with <code>PutInsightRule</code>. The rules can be enabled, disabled, and deleted using <code>EnableInsightRules</code>, <code>DisableInsightRules</code>, and <code>DeleteInsightRules</code>. If a previously created managed rule is currently disabled, a subsequent call to this API will re-enable it. Use <code>ListManagedInsightRules</code> to describe all available rules. </p>

        Args:
            managed_rules: <p> A list of <code>ManagedRules</code> to enable. </p>

        Raises:
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_managed_insight_rules_input.PutManagedInsightRulesInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.put_managed_insight_rules_output.PutManagedInsightRulesOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_managed_insight_rules

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_managed_insight_rules.put_managed_insight_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_managed_insight_rules_input.PutManagedInsightRulesInput = {}
        if managed_rules is not None:
            input_["managed_rules"] = managed_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_metric_alarm(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_name: Optional["capo_cloudwatch.types.alarm_name.AlarmName"] = None,
        alarm_description: Optional[
            "capo_cloudwatch.types.alarm_description.AlarmDescription"
        ] = None,
        actions_enabled: Optional[
            "capo_cloudwatch.types.actions_enabled.ActionsEnabled"
        ] = None,
        ok_actions: Optional["capo_cloudwatch.types.resource_list.ResourceList"] = None,
        alarm_actions: Optional[
            "capo_cloudwatch.types.resource_list.ResourceList"
        ] = None,
        insufficient_data_actions: Optional[
            "capo_cloudwatch.types.resource_list.ResourceList"
        ] = None,
        metric_name: Optional["capo_cloudwatch.types.metric_name.MetricName"] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        statistic: Optional["capo_cloudwatch.types.statistic.Statistic"] = None,
        extended_statistic: Optional[
            "capo_cloudwatch.types.extended_statistic.ExtendedStatistic"
        ] = None,
        dimensions: Optional["capo_cloudwatch.types.dimensions.Dimensions"] = None,
        period: Optional["capo_cloudwatch.types.period.Period"] = None,
        unit: Optional["capo_cloudwatch.types.standard_unit.StandardUnit"] = None,
        evaluation_periods: Optional[
            "capo_cloudwatch.types.evaluation_periods.EvaluationPeriods"
        ] = None,
        datapoints_to_alarm: Optional[
            "capo_cloudwatch.types.datapoints_to_alarm.DatapointsToAlarm"
        ] = None,
        threshold: Optional["capo_cloudwatch.types.threshold.Threshold"] = None,
        comparison_operator: Optional[
            "capo_cloudwatch.types.comparison_operator.ComparisonOperator"
        ] = None,
        treat_missing_data: Optional[
            "capo_cloudwatch.types.treat_missing_data.TreatMissingData"
        ] = None,
        evaluate_low_sample_count_percentile: Optional[
            "capo_cloudwatch.types.evaluate_low_sample_count_percentile.EvaluateLowSampleCountPercentile"
        ] = None,
        metrics: Optional[
            "capo_cloudwatch.types.metric_data_queries.MetricDataQueries"
        ] = None,
        tags: Optional["capo_cloudwatch.types.tag_list.TagList"] = None,
        threshold_metric_id: Optional[
            "capo_cloudwatch.types.metric_id.MetricId"
        ] = None,
        evaluation_window: Optional[
            "capo_cloudwatch.types.evaluation_window.EvaluationWindow"
        ] = None,
        warm_up_configuration: Optional[
            "capo_cloudwatch.types.warm_up_configuration.WarmUpConfiguration"
        ] = None,
        evaluation_criteria: Optional[
            "capo_cloudwatch.types.evaluation_criteria.EvaluationCriteria"
        ] = None,
        evaluation_interval: Optional[
            "capo_cloudwatch.types.evaluation_interval.EvaluationInterval"
        ] = None,
    ) -> None:
        """<p>Creates or updates an alarm and associates it with the specified metric, metric math expression, anomaly detection model, Metrics Insights query, or PromQL query. For more information about using a Metrics Insights query for an alarm, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html">Create alarms on Metrics Insights queries</a>.</p> <p>Alarms based on anomaly detection models cannot have Auto Scaling actions.</p> <p>When this operation creates an alarm, the alarm state is immediately set to <code>INSUFFICIENT_DATA</code>. For PromQL alarms, the alarm state is instead immediately set to <code>OK</code>. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.</p> <p>When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.</p> <p>If you are an IAM user, you must have Amazon EC2 permissions for some alarm operations:</p> <ul> <li> <p>The <code>iam:CreateServiceLinkedRole</code> permission for all alarms with EC2 actions</p> </li> <li> <p>The <code>iam:CreateServiceLinkedRole</code> permissions to create an alarm with Systems Manager OpsItem or response plan actions.</p> </li> </ul> <p>The first time you create an alarm in the Amazon Web Services Management Console, the CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The service-linked roles are called <code>AWSServiceRoleForCloudWatchEvents</code> and <code>AWSServiceRoleForCloudWatchAlarms_ActionSSM</code>. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role">Amazon Web Services service-linked role</a>.</p> <p>Each <code>PutMetricAlarm</code> action has a maximum uncompressed payload of 120 KB.</p> <p> <b>Cross-account alarms</b> </p> <p>You can set an alarm on metrics in the current account, or in another account. To create a cross-account alarm that watches a metric in a different account, you must have completed the following pre-requisites:</p> <ul> <li> <p>The account where the metrics are located (the <i>sharing account</i>) must already have a sharing role named <b>CloudWatch-CrossAccountSharingRole</b>. If it does not already have this role, you must create it using the instructions in <b>Set up a sharing account</b> in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region"> Cross-account cross-Region CloudWatch console</a>. The policy for that role must grant access to the ID of the account where you are creating the alarm. </p> </li> <li> <p>The account where you are creating the alarm (the <i>monitoring account</i>) must already have a service-linked role named <b>AWSServiceRoleForCloudWatchCrossAccount</b> to allow CloudWatch to assume the sharing role in the sharing account. If it does not, you must create it following the directions in <b>Set up a monitoring account</b> in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region"> Cross-account cross-Region CloudWatch console</a>.</p> </li> </ul>

        Args:
            alarm_name: <p>The name for the alarm. This name must be unique within the Region.</p> <p>The name must contain only UTF-8 characters, and can't contain ASCII control characters</p>
            alarm_description: <p>The description for the alarm.</p>
            actions_enabled: <p>Indicates whether actions should be executed during any changes to the alarm state. The default is <code>TRUE</code>.</p>
            ok_actions: <p>The actions to execute when this alarm transitions to an <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:</p> <p> <b>EC2 actions:</b> </p> <ul> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:stop</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:recover</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p> </li> </ul> <p> <b>Autoscaling action:</b> </p> <ul> <li> <p> <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>SNS notification action:</b> </p> <ul> <li> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> </li> </ul> <p> <b>SSM integration actions:</b> </p> <ul> <li> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i>#CATEGORY=<i>category-name</i> </code> </p> </li> <li> <p> <code>arn:aws:ssm-incidents::<i>account-id</i>:responseplan/<i>response-plan-name</i> </code> </p> </li> </ul>
            alarm_actions: <p>The actions to execute when this alarm transitions to the <code>ALARM</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:</p> <p> <b>EC2 actions:</b> </p> <ul> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:stop</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:recover</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p> </li> </ul> <p> <b>Autoscaling action:</b> </p> <ul> <li> <p> <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>SNS notification action:</b> </p> <ul> <li> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> </li> </ul> <p> <b>SSM integration actions:</b> </p> <ul> <li> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i>#CATEGORY=<i>category-name</i> </code> </p> </li> <li> <p> <code>arn:aws:ssm-incidents::<i>account-id</i>:responseplan/<i>response-plan-name</i> </code> </p> </li> </ul> <p> <b>Start a Amazon Q Developer operational investigation</b> </p> <p> <code>arn:aws:aiops:<i>region</i>:<i>account-id</i>:investigation-group:<i>investigation-group-id</i> </code> </p>
            insufficient_data_actions: <p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:</p> <p> <b>EC2 actions:</b> </p> <ul> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:stop</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:recover</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p> </li> </ul> <p> <b>Autoscaling action:</b> </p> <ul> <li> <p> <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>SNS notification action:</b> </p> <ul> <li> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> </li> </ul> <p> <b>SSM integration actions:</b> </p> <ul> <li> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i>#CATEGORY=<i>category-name</i> </code> </p> </li> <li> <p> <code>arn:aws:ssm-incidents::<i>account-id</i>:responseplan/<i>response-plan-name</i> </code> </p> </li> </ul>
            metric_name: <p>The name for the metric associated with the alarm. For each <code>PutMetricAlarm</code> operation, you must specify either <code>MetricName</code>, a <code>Metrics</code> array, or an <code>EvaluationCriteria</code>.</p> <p>If you are creating an alarm based on a math expression, you cannot specify this parameter, or any of the <code>Namespace</code>, <code>Dimensions</code>, <code>Period</code>, <code>Unit</code>, <code>Statistic</code>, or <code>ExtendedStatistic</code> parameters. Instead, you specify all this information in the <code>Metrics</code> array.</p>
            namespace: <p>The namespace for the metric associated specified in <code>MetricName</code>.</p>
            statistic: <p>The statistic for the metric specified in <code>MetricName</code>, other than percentile. For percentile statistics, use <code>ExtendedStatistic</code>. When you call <code>PutMetricAlarm</code> and specify a <code>MetricName</code>, you must specify either <code>Statistic</code> or <code>ExtendedStatistic,</code> but not both.</p>
            extended_statistic: <p>The extended statistic for the metric specified in <code>MetricName</code>. When you call <code>PutMetricAlarm</code> and specify a <code>MetricName</code>, you must specify either <code>Statistic</code> or <code>ExtendedStatistic</code> but not both.</p> <p>If you specify <code>ExtendedStatistic</code>, the following are valid values:</p> <ul> <li> <p> <code>p90</code> </p> </li> <li> <p> <code>tm90</code> </p> </li> <li> <p> <code>tc90</code> </p> </li> <li> <p> <code>ts90</code> </p> </li> <li> <p> <code>wm90</code> </p> </li> <li> <p> <code>IQM</code> </p> </li> <li> <p> <code>PR(<i>n</i>:<i>m</i>)</code> where n and m are values of the metric</p> </li> <li> <p> <code>TC(<i>X</i>%:<i>X</i>%)</code> where X is between 10 and 90 inclusive.</p> </li> <li> <p> <code>TM(<i>X</i>%:<i>X</i>%)</code> where X is between 10 and 90 inclusive.</p> </li> <li> <p> <code>TS(<i>X</i>%:<i>X</i>%)</code> where X is between 10 and 90 inclusive.</p> </li> <li> <p> <code>WM(<i>X</i>%:<i>X</i>%)</code> where X is between 10 and 90 inclusive.</p> </li> </ul> <p>For more information about these extended statistics, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html">CloudWatch statistics definitions</a>.</p>
            dimensions: <p>The dimensions for the metric specified in <code>MetricName</code>.</p>
            period: <p>The length, in seconds, used each time the metric specified in <code>MetricName</code> is evaluated. Valid values are 10, 20, 30, and any multiple of 60.</p> <p> <code>Period</code> is required for alarms based on static thresholds. If you are creating an alarm based on a metric math expression, you specify the period for each metric within the objects in the <code>Metrics</code> array.</p> <p>Be sure to specify 10, 20, or 30 only for metrics that are stored by a <code>PutMetricData</code> call with a <code>StorageResolution</code> of 1. If you specify a period of 10, 20, or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm might often lapse into INSUFFICENT_DATA status. Specifying 10, 20, or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see <a href="https://aws.amazon.com/cloudwatch/pricing/">Amazon CloudWatch Pricing</a>.</p> <p>An alarm's total current evaluation period can be no longer than seven days, so <code>Period</code> multiplied by <code>EvaluationPeriods</code> can't be more than 604,800 seconds. For alarms with a period of less than one hour (3,600 seconds), the total evaluation period can't be longer than one day (86,400 seconds).</p>
            unit: <p>The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately. If you are creating an alarm based on a metric math expression, you can specify the unit for each metric (if needed) within the objects in the <code>Metrics</code> array.</p> <p>If you don't specify <code>Unit</code>, CloudWatch retrieves all unit types that have been published for the metric and attempts to evaluate the alarm. Usually, metrics are published with only one unit, so the alarm works as intended.</p> <p>However, if the metric is published with multiple types of units and you don't specify a unit, the alarm's behavior is not defined and it behaves unpredictably.</p> <p>We recommend omitting <code>Unit</code> so that you don't inadvertently specify an incorrect unit that is not published for this metric. Doing so causes the alarm to be stuck in the <code>INSUFFICIENT DATA</code> state.</p>
            evaluation_periods: <p>The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N.</p>
            datapoints_to_alarm: <p>The number of data points that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation">Evaluating an Alarm</a> in the <i>Amazon CloudWatch User Guide</i>.</p>
            threshold: <p>The value against which the specified statistic is compared.</p> <p>This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.</p>
            comparison_operator: <p> The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.</p> <p>The values <code>LessThanLowerOrGreaterThanUpperThreshold</code>, <code>LessThanLowerThreshold</code>, and <code>GreaterThanUpperThreshold</code> are used only for alarms based on anomaly detection models.</p>
            treat_missing_data: <p> Sets how this alarm is to handle missing data points. If <code>TreatMissingData</code> is omitted, the default behavior of <code>missing</code> is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data">Configuring How CloudWatch Alarms Treats Missing Data</a>.</p> <p>Valid Values: <code>breaching | notBreaching | ignore | missing</code> </p> <note> <p>Alarms that evaluate metrics in the <code>AWS/DynamoDB</code> namespace always <code>ignore</code> missing data even if you choose a different option for <code>TreatMissingData</code>. When an <code>AWS/DynamoDB</code> metric has missing data, alarms that evaluate that metric remain in their current state.</p> </note> <note> <p>This parameter is not applicable to PromQL alarms.</p> </note>
            evaluate_low_sample_count_percentile: <p> Used only for alarms based on percentiles. If you specify <code>ignore</code>, the alarm state does not change during periods with too few data points to be statistically significant. If you specify <code>evaluate</code> or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-with-low-samples">Percentile-Based CloudWatch Alarms and Low Data Samples</a>.</p> <p>Valid Values: <code>evaluate | ignore</code> </p>
            metrics: <p>An array of <code>MetricDataQuery</code> structures that enable you to create an alarm based on the result of a metric math expression. For each <code>PutMetricAlarm</code> operation, you must specify either <code>MetricName</code>, a <code>Metrics</code> array, or an <code>EvaluationCriteria</code>.</p> <p>Each item in the <code>Metrics</code> array either retrieves a metric or performs a math expression.</p> <p>One item in the <code>Metrics</code> array is the expression that the alarm watches. You designate this expression by setting <code>ReturnData</code> to true for this object in the array. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDataQuery.html">MetricDataQuery</a>.</p> <p>If you use the <code>Metrics</code> parameter, you cannot include the <code>Namespace</code>, <code>MetricName</code>, <code>Dimensions</code>, <code>Period</code>, <code>Unit</code>, <code>Statistic</code>, or <code>ExtendedStatistic</code> parameters of <code>PutMetricAlarm</code> in the same operation. Instead, you retrieve the metrics you are using in your math expression as part of the <code>Metrics</code> array.</p>
            tags: <p>A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>If you are using this operation to update an existing alarm, any tags you specify in this parameter are ignored. To change the tags of an existing alarm, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html">TagResource</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p> <p>To use this field to set tags for an alarm when you create it, you must be signed on with both the <code>cloudwatch:PutMetricAlarm</code> and <code>cloudwatch:TagResource</code> permissions.</p>
            threshold_metric_id: <p>If this is an alarm based on an anomaly detection model, make this value match the ID of the <code>ANOMALY_DETECTION_BAND</code> function.</p> <p>For an example of how to use this parameter, see the <b>Anomaly Detection Model Alarm</b> example on this page.</p> <p>If your alarm uses this parameter, it cannot have Auto Scaling actions.</p>
            evaluation_window: <p>The evaluation window that the alarm uses to select the range of metric data that it evaluates. Specify either a sliding window or a wall clock window. If you omit this parameter, the alarm uses a sliding window.</p> <p>A sliding window advances each time the alarm is evaluated, forming a rolling time window. A wall clock window aligns the evaluated range to fixed clock boundaries, such as the top of the hour or the start of the day.</p> <p>You can use <code>EvaluationWindow</code> with any type of metric alarm except alarms that are based on a PromQL query.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation-window.html">Alarm evaluation windows</a> in the <i>CloudWatch User Guide</i>.</p>
            warm_up_configuration: <p>The warm-up configuration for the alarm. A warm-up period delays alarm evaluation after you create or update the alarm. The warm-up period reduces alarm noise from missing data while a new resource or service starts publishing metrics.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html">Alarm warm-up periods</a> in the <i>Amazon CloudWatch User Guide</i>.</p>
            evaluation_criteria: <p>The evaluation criteria for the alarm. For each <code>PutMetricAlarm</code> operation, you must specify either <code>MetricName</code>, a <code>Metrics</code> array, or an <code>EvaluationCriteria</code>.</p> <p>If you use the <code>EvaluationCriteria</code> parameter, you cannot include the <code>Namespace</code>, <code>MetricName</code>, <code>Dimensions</code>, <code>Period</code>, <code>Unit</code>, <code>Statistic</code>, <code>ExtendedStatistic</code>, <code>Metrics</code>, <code>Threshold</code>, <code>ComparisonOperator</code>, <code>ThresholdMetricId</code>, <code>EvaluationPeriods</code>, or <code>DatapointsToAlarm</code> parameters of <code>PutMetricAlarm</code> in the same operation. Instead, all evaluation parameters are defined within this structure.</p> <p>For an example of how to use this parameter, see the <b>PromQL alarm</b> example on this page.</p>
            evaluation_interval: <p>The frequency, in seconds, at which the alarm is evaluated. Valid values are 10, 20, 30, and any multiple of 60.</p> <p>This parameter is required for alarms that use <code>EvaluationCriteria</code>, and cannot be specified for alarms configured with <code>MetricName</code> or <code>Metrics</code>.</p>

        Raises:
            capo_cloudwatch.errors.limit_exceeded_fault.LimitExceededFault: <p>The quota for alarms for this customer has already been reached.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_metric_alarm_input.PutMetricAlarmInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_metric_alarm

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_metric_alarm.put_metric_alarm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_metric_alarm_input.PutMetricAlarmInput = {}
        if alarm_name is not None:
            input_["alarm_name"] = alarm_name
        if alarm_description is not None:
            input_["alarm_description"] = alarm_description
        if actions_enabled is not None:
            input_["actions_enabled"] = actions_enabled
        if ok_actions is not None:
            input_["ok_actions"] = ok_actions
        if alarm_actions is not None:
            input_["alarm_actions"] = alarm_actions
        if insufficient_data_actions is not None:
            input_["insufficient_data_actions"] = insufficient_data_actions
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if namespace is not None:
            input_["namespace"] = namespace
        if statistic is not None:
            input_["statistic"] = statistic
        if extended_statistic is not None:
            input_["extended_statistic"] = extended_statistic
        if dimensions is not None:
            input_["dimensions"] = dimensions
        if period is not None:
            input_["period"] = period
        if unit is not None:
            input_["unit"] = unit
        if evaluation_periods is not None:
            input_["evaluation_periods"] = evaluation_periods
        if datapoints_to_alarm is not None:
            input_["datapoints_to_alarm"] = datapoints_to_alarm
        if threshold is not None:
            input_["threshold"] = threshold
        if comparison_operator is not None:
            input_["comparison_operator"] = comparison_operator
        if treat_missing_data is not None:
            input_["treat_missing_data"] = treat_missing_data
        if evaluate_low_sample_count_percentile is not None:
            input_["evaluate_low_sample_count_percentile"] = (
                evaluate_low_sample_count_percentile
            )
        if metrics is not None:
            input_["metrics"] = metrics
        if tags is not None:
            input_["tags"] = tags
        if threshold_metric_id is not None:
            input_["threshold_metric_id"] = threshold_metric_id
        if evaluation_window is not None:
            input_["evaluation_window"] = evaluation_window
        if warm_up_configuration is not None:
            input_["warm_up_configuration"] = warm_up_configuration
        if evaluation_criteria is not None:
            input_["evaluation_criteria"] = evaluation_criteria
        if evaluation_interval is not None:
            input_["evaluation_interval"] = evaluation_interval

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_metric_data(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        namespace: Optional["capo_cloudwatch.types.namespace.Namespace"] = None,
        metric_data: Optional["capo_cloudwatch.types.metric_data.MetricData"] = None,
        entity_metric_data: Optional[
            "capo_cloudwatch.types.entity_metric_data_list.EntityMetricDataList"
        ] = None,
        strict_entity_validation: Optional[
            "capo_cloudwatch.types.strict_entity_validation.StrictEntityValidation"
        ] = None,
    ) -> None:
        """<p>Publishes metric data to Amazon CloudWatch. CloudWatch associates the data with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html">ListMetrics</a>.</p> <p>You can publish metrics with associated entity data (so that related telemetry can be found and viewed together), or publish metric data by itself. To send entity data with your metrics, use the <code>EntityMetricData</code> parameter. To send metrics without entity data, use the <code>MetricData</code> parameter. The <code>EntityMetricData</code> structure includes <code>MetricData</code> structures for the metric data.</p> <p>You can publish either individual values in the <code>Value</code> field, or arrays of values and the number of times each value occurred during the period by using the <code>Values</code> and <code>Counts</code> fields in the <code>MetricData</code> structure. Using the <code>Values</code> and <code>Counts</code> method enables you to publish up to 150 values per metric with one <code>PutMetricData</code> request, and supports retrieving percentile statistics on this data.</p> <p>Each <code>PutMetricData</code> request is limited to 1 MB in size for HTTP POST requests. You can send a payload compressed by gzip. Each request is also limited to no more than 1000 different metrics (across both the <code>MetricData</code> and <code>EntityMetricData</code> properties).</p> <p>Although the <code>Value</code> parameter accepts numbers of type <code>Double</code>, CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.</p> <p>You can use up to 30 dimensions per metric to further clarify what data the metric collects. Each dimension consists of a Name and Value pair. For more information about specifying dimensions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html">Publishing Metrics</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>You specify the time stamp to be associated with each data point. You can specify time stamps that are as much as two weeks before the current date, and as much as 2 hours after the current day and time.</p> <p>Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html">GetMetricData</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html">GetMetricStatistics</a> from the time they are submitted. Data points with time stamps between 3 and 24 hours ago can take as much as 2 hours to become available for <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html">GetMetricData</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html">GetMetricStatistics</a>.</p> <p>CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:</p> <ul> <li> <p>The <code>SampleCount</code> value of the statistic set is 1 and <code>Min</code>, <code>Max</code>, and <code>Sum</code> are all equal.</p> </li> <li> <p>The <code>Min</code> and <code>Max</code> are equal, and <code>Sum</code> is equal to <code>Min</code> multiplied by <code>SampleCount</code>.</p> </li> </ul>

        Args:
            namespace: <p>The namespace for the metric data. You can use ASCII characters for the namespace, except for control characters which are not supported.</p> <p>To avoid conflicts with Amazon Web Services service namespaces, you should not specify a namespace that begins with <code>AWS/</code> </p>
            metric_data: <p>The data for the metrics. Use this parameter if your metrics do not contain associated entities. The array can include no more than 1000 metrics per call.</p> <p>The limit of metrics allowed, 1000, is the sum of both <code>EntityMetricData</code> and <code>MetricData</code> metrics.</p>
            entity_metric_data: <p>Data for metrics that contain associated entity information. You can include up to two <code>EntityMetricData</code> objects, each of which can contain a single <code>Entity</code> and associated metrics.</p> <p>The limit of metrics allowed, 1000, is the sum of both <code>EntityMetricData</code> and <code>MetricData</code> metrics.</p>
            strict_entity_validation: <p>Whether to accept valid metric data when an invalid entity is sent.</p> <ul> <li> <p>When set to <code>true</code>: Any validation error (for entity or metric data) will fail the entire request, and no data will be ingested. The failed operation will return a 400 result with the error.</p> </li> <li> <p>When set to <code>false</code>: Validation errors in the entity will not associate the metric with the entity, but the metric data will still be accepted and ingested. Validation errors in the metric data will fail the entire request, and no data will be ingested.</p> <p>In the case of an invalid entity, the operation will return a <code>200</code> status, but an additional response header will contain information about the validation errors. The new header, <code>X-Amzn-Failure-Message</code> is an enumeration of the following values:</p> <ul> <li> <p> <code>InvalidEntity</code> - The provided entity is invalid.</p> </li> <li> <p> <code>InvalidKeyAttributes</code> - The provided <code>KeyAttributes</code> of an entity is invalid.</p> </li> <li> <p> <code>InvalidAttributes</code> - The provided <code>Attributes</code> of an entity is invalid.</p> </li> <li> <p> <code>InvalidTypeValue</code> - The provided <code>Type</code> in the <code>KeyAttributes</code> of an entity is invalid.</p> </li> <li> <p> <code>EntitySizeTooLarge</code> - The number of <code>EntityMetricData</code> objects allowed is 2.</p> </li> <li> <p> <code>MissingRequiredFields</code> - There are missing required fields in the <code>KeyAttributes</code> for the provided <code>Type</code>.</p> </li> </ul> <p>For details of the requirements for specifying an entity, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html">How to add related information to telemetry</a> in the <i>CloudWatch User Guide</i>.</p> </li> </ul> <p>This parameter is <i>required</i> when <code>EntityMetricData</code> is included.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Parameters were used together that cannot be used together.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_metric_data_input.PutMetricDataInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_metric_data

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_metric_data.put_metric_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_metric_data_input.PutMetricDataInput = {}
        if namespace is not None:
            input_["namespace"] = namespace
        if metric_data is not None:
            input_["metric_data"] = metric_data
        if entity_metric_data is not None:
            input_["entity_metric_data"] = entity_metric_data
        if strict_entity_validation is not None:
            input_["strict_entity_validation"] = strict_entity_validation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_metric_stream(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        name: Optional[
            "capo_cloudwatch.types.metric_stream_name.MetricStreamName"
        ] = None,
        include_filters: Optional[
            "capo_cloudwatch.types.metric_stream_filters.MetricStreamFilters"
        ] = None,
        exclude_filters: Optional[
            "capo_cloudwatch.types.metric_stream_filters.MetricStreamFilters"
        ] = None,
        firehose_arn: Optional[
            "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        role_arn: Optional[
            "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        output_format: Optional[
            "capo_cloudwatch.types.metric_stream_output_format.MetricStreamOutputFormat"
        ] = None,
        tags: Optional["capo_cloudwatch.types.tag_list.TagList"] = None,
        statistics_configurations: Optional[
            "capo_cloudwatch.types.metric_stream_statistics_configurations.MetricStreamStatisticsConfigurations"
        ] = None,
        include_linked_accounts_metrics: Optional[
            "capo_cloudwatch.types.include_linked_accounts_metrics.IncludeLinkedAccountsMetrics"
        ] = None,
    ) -> "capo_cloudwatch.types.put_metric_stream_output.PutMetricStreamOutput":
        """<p>Creates or updates a metric stream. Metric streams can automatically stream CloudWatch metrics to Amazon Web Services destinations, including Amazon S3, and to many third-party solutions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html"> Using Metric Streams</a>.</p> <p>To create a metric stream, you must be signed in to an account that has the <code>iam:PassRole</code> permission and either the <code>CloudWatchFullAccess</code> policy or the <code>cloudwatch:PutMetricStream</code> permission.</p> <p>When you create or update a metric stream, you choose one of the following:</p> <ul> <li> <p>Stream metrics from all metric namespaces in the account.</p> </li> <li> <p>Stream metrics from all metric namespaces in the account, except for the namespaces that you list in <code>ExcludeFilters</code>.</p> </li> <li> <p>Stream metrics from only the metric namespaces that you list in <code>IncludeFilters</code>.</p> </li> </ul> <p>By default, a metric stream always sends the <code>MAX</code>, <code>MIN</code>, <code>SUM</code>, and <code>SAMPLECOUNT</code> statistics for each metric that is streamed. You can use the <code>StatisticsConfigurations</code> parameter to have the metric stream send additional statistics in the stream. Streaming additional statistics incurs additional costs. For more information, see <a href="https://aws.amazon.com/cloudwatch/pricing/">Amazon CloudWatch Pricing</a>. </p> <p>When you use <code>PutMetricStream</code> to create a new metric stream, the stream is created in the <code>running</code> state. If you use it to update an existing stream, the state of the stream is not changed.</p> <p>If you are using CloudWatch cross-account observability and you create a metric stream in a monitoring account, you can choose whether to include metrics from source accounts in the stream. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p>

        Args:
            name: <p>If you are creating a new metric stream, this is the name for the new stream. The name must be different than the names of other metric streams in this account and Region.</p> <p>If you are updating a metric stream, specify the name of that stream here.</p> <p>Valid characters are A-Z, a-z, 0-9, "-" and "_".</p>
            include_filters: <p>If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.</p> <p>You cannot include <code>IncludeFilters</code> and <code>ExcludeFilters</code> in the same operation.</p>
            exclude_filters: <p>If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.</p> <p>You cannot include <code>ExcludeFilters</code> and <code>IncludeFilters</code> in the same operation.</p>
            firehose_arn: <p>The ARN of the Amazon Kinesis Data Firehose delivery stream to use for this metric stream. This Amazon Kinesis Data Firehose delivery stream must already exist and must be in the same account as the metric stream.</p>
            role_arn: <p>The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Data Firehose resources. This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the following permissions:</p> <ul> <li> <p>firehose:PutRecord</p> </li> <li> <p>firehose:PutRecordBatch</p> </li> </ul>
            output_format: <p>The output format for the stream. Valid values are <code>json</code>, <code>opentelemetry1.0</code>, and <code>opentelemetry0.7</code>. For more information about metric stream output formats, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html"> Metric streams output formats</a>.</p>
            tags: <p>A list of key-value pairs to associate with the metric stream. You can associate as many as 50 tags with a metric stream.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>You can use this parameter only when you are creating a new metric stream. If you are using this operation to update an existing metric stream, any tags you specify in this parameter are ignored. To change the tags of an existing metric stream, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html">TagResource</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p>
            statistics_configurations: <p>By default, a metric stream always sends the <code>MAX</code>, <code>MIN</code>, <code>SUM</code>, and <code>SAMPLECOUNT</code> statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.</p> <p>For each entry in this array, you specify one or more metrics and the list of additional statistics to stream for those metrics. The additional statistics that you can stream depend on the stream's <code>OutputFormat</code>. If the <code>OutputFormat</code> is <code>json</code>, you can stream any additional statistic that is supported by CloudWatch, listed in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html"> CloudWatch statistics definitions</a>. If the <code>OutputFormat</code> is <code>opentelemetry1.0</code> or <code>opentelemetry0.7</code>, you can stream percentile statistics such as p95, p99.9, and so on.</p>
            include_linked_accounts_metrics: <p>If you are creating a metric stream in a monitoring account, specify <code>true</code> to include metrics from source accounts in the metric stream.</p>

        Raises:
            capo_cloudwatch.errors.concurrent_modification_exception.ConcurrentModificationException: <p>More than one process tried to modify a resource at the same time.</p>
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Parameters were used together that cannot be used together.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.put_metric_stream_input.PutMetricStreamInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.put_metric_stream_output.PutMetricStreamOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.put_metric_stream

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.put_metric_stream.put_metric_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.put_metric_stream_input.PutMetricStreamInput = {}
        if name is not None:
            input_["name"] = name
        if include_filters is not None:
            input_["include_filters"] = include_filters
        if exclude_filters is not None:
            input_["exclude_filters"] = exclude_filters
        if firehose_arn is not None:
            input_["firehose_arn"] = firehose_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if output_format is not None:
            input_["output_format"] = output_format
        if tags is not None:
            input_["tags"] = tags
        if statistics_configurations is not None:
            input_["statistics_configurations"] = statistics_configurations
        if include_linked_accounts_metrics is not None:
            input_["include_linked_accounts_metrics"] = include_linked_accounts_metrics

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_alarm_state(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        alarm_name: Optional["capo_cloudwatch.types.alarm_name.AlarmName"] = None,
        state_value: Optional["capo_cloudwatch.types.state_value.StateValue"] = None,
        state_reason: Optional["capo_cloudwatch.types.state_reason.StateReason"] = None,
        state_reason_data: Optional[
            "capo_cloudwatch.types.state_reason_data.StateReasonData"
        ] = None,
    ) -> None:
        """<p>Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to <code>ALARM</code> sends an SNS message.</p> <p>Metric alarms returns to their actual state quickly, often within seconds. Because the metric alarm state change happens quickly, it is typically only visible in the alarm's <b>History</b> tab in the Amazon CloudWatch console or through <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html">DescribeAlarmHistory</a>.</p> <p>If you use <code>SetAlarmState</code> on a composite alarm, the composite alarm is not guaranteed to return to its actual state. It returns to its actual state only once any of its children alarms change state. It is also reevaluated if you update its configuration.</p> <p>If an alarm triggers EC2 Auto Scaling policies or application Auto Scaling policies, you must include information in the <code>StateReasonData</code> parameter to enable the policy to take the correct action.</p>

        Args:
            alarm_name: <p>The name of the alarm.</p>
            state_value: <p>The value of the state.</p>
            state_reason: <p>The reason that this alarm is set to this specific state, in text format.</p>
            state_reason_data: <p>The reason that this alarm is set to this specific state, in JSON format.</p> <p>For SNS or EC2 alarm actions, this is just informational. But for EC2 Auto Scaling or application Auto Scaling alarm actions, the Auto Scaling policy uses the information in this field to take the correct action.</p>

        Raises:
            capo_cloudwatch.errors.invalid_format_fault.InvalidFormatFault: <p>Data was not syntactically valid JSON.</p>
            capo_cloudwatch.errors.resource_not_found.ResourceNotFound: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.set_alarm_state_input.SetAlarmStateInput]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch._operations.granite_service_version20100801.set_alarm_state

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.set_alarm_state.set_alarm_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.set_alarm_state_input.SetAlarmStateInput = {}
        if alarm_name is not None:
            input_["alarm_name"] = alarm_name
        if state_value is not None:
            input_["state_value"] = state_value
        if state_reason is not None:
            input_["state_reason"] = state_reason
        if state_reason_data is not None:
            input_["state_reason_data"] = state_reason_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_metric_streams(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        names: Optional[
            "capo_cloudwatch.types.metric_stream_names.MetricStreamNames"
        ] = None,
    ) -> "capo_cloudwatch.types.start_metric_streams_output.StartMetricStreamsOutput":
        """<p>Starts the streaming of metrics for one or more of your metric streams.</p>

        Args:
            names: <p>The array of the names of metric streams to start streaming.</p> <p>This is an "all or nothing" operation. If you do not have permission to access all of the metric streams that you list here, then none of the streams that you list in the operation will start streaming.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.start_metric_streams_input.StartMetricStreamsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.start_metric_streams_output.StartMetricStreamsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.start_metric_streams

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.start_metric_streams.start_metric_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.start_metric_streams_input.StartMetricStreamsInput = {}
        if names is not None:
            input_["names"] = names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_o_tel_enrichment(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        include_filters: Optional[
            "capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.OTelEnrichmentMetricSelectorList"
        ] = None,
        exclude_filters: Optional[
            "capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.OTelEnrichmentMetricSelectorList"
        ] = None,
    ) -> (
        "capo_cloudwatch.types.start_o_tel_enrichment_output.StartOTelEnrichmentOutput"
    ):
        """<p>Enables enrichment and PromQL access for CloudWatch vended metrics for <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html">supported Amazon Web Services resources</a> in the account. Once enabled, metrics that contain a resource identifier dimension (for example, EC2 <code>CPUUtilization</code> with an <code>InstanceId</code> dimension) are enriched with resource ARN and resource tag labels and become queryable using PromQL.</p> <p>Before calling this operation, you must enable resource tags on telemetry for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/EnableResourceTagsOnTelemetry.html">Enable resource tags on telemetry</a>.</p> <p>Optionally, <code>IncludeFilters</code> and <code>ExcludeFilters</code> limit enrichment to a subset of the account's metrics. These filters are stored only when this operation starts enrichment. Calling <code>StartOTelEnrichment</code> for an account where enrichment is already running has no effect and does not modify the filters that are applied. To change them, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateOTelEnrichment.html">UpdateOTelEnrichment</a>.</p>

        Args:
            include_filters: <p>The metric namespaces, and the metric names, to enrich. If this parameter is omitted, every namespace that Amazon CloudWatch supports for enrichment is in scope.</p> <p>A maximum of 100 filters is allowed across <code>IncludeFilters</code> and <code>ExcludeFilters</code> combined.</p>
            exclude_filters: <p>The metric namespaces, and the metric names, to leave unenriched. If this parameter is omitted, nothing is excluded.</p> <p>Amazon CloudWatch applies <code>ExcludeFilters</code> after <code>IncludeFilters</code>, so a metric that both parameters match is not enriched.</p> <p>A maximum of 100 filters is allowed across <code>IncludeFilters</code> and <code>ExcludeFilters</code> combined.</p>

        Raises:
            capo_cloudwatch.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters do not satisfy the constraints that the operation requires.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.start_o_tel_enrichment_input.StartOTelEnrichmentInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.start_o_tel_enrichment_output.StartOTelEnrichmentOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.start_o_tel_enrichment

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.start_o_tel_enrichment.start_o_tel_enrichment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.start_o_tel_enrichment_input.StartOTelEnrichmentInput = {}
        if include_filters is not None:
            input_["include_filters"] = include_filters
        if exclude_filters is not None:
            input_["exclude_filters"] = exclude_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_metric_streams(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        names: Optional[
            "capo_cloudwatch.types.metric_stream_names.MetricStreamNames"
        ] = None,
    ) -> "capo_cloudwatch.types.stop_metric_streams_output.StopMetricStreamsOutput":
        """<p>Stops the streaming of metrics for one or more of your metric streams.</p>

        Args:
            names: <p>The array of the names of metric streams to stop streaming.</p> <p>This is an "all or nothing" operation. If you do not have permission to access all of the metric streams that you list here, then none of the streams that you list in the operation will stop streaming.</p>

        Raises:
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>An input parameter that is required is missing.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.stop_metric_streams_input.StopMetricStreamsInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.stop_metric_streams_output.StopMetricStreamsOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.stop_metric_streams

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.stop_metric_streams.stop_metric_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.stop_metric_streams_input.StopMetricStreamsInput = {}
        if names is not None:
            input_["names"] = names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_o_tel_enrichment(
        self, *, config_overrides: Optional[CloudWatchClientConfig] = None
    ) -> "capo_cloudwatch.types.stop_o_tel_enrichment_output.StopOTelEnrichmentOutput":
        """<p>Disables enrichment and PromQL access for CloudWatch vended metrics for <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html">supported Amazon Web Services resources</a> in the account. After disabling, these metrics are no longer enriched with resource ARN and resource tag labels, and cannot be queried using PromQL.</p>

        Raises:
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.stop_o_tel_enrichment_input.StopOTelEnrichmentInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.stop_o_tel_enrichment_output.StopOTelEnrichmentOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.stop_o_tel_enrichment

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.stop_o_tel_enrichment.stop_o_tel_enrichment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.stop_o_tel_enrichment_input.StopOTelEnrichmentInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        resource_arn: Optional[
            "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        tags: Optional["capo_cloudwatch.types.tag_list.TagList"] = None,
    ) -> "capo_cloudwatch.types.tag_resource_output.TagResourceOutput":
        """<p>Assigns one or more tags (key-value pairs) to the specified CloudWatch resource. Currently, the only CloudWatch resources that can be tagged are alarms, dashboards, metric streams and Contributor Insights rules.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with an alarm that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a CloudWatch resource.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch resource that you're adding tags to.</p> <p>The ARN format of an alarm is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:alarm:<i>alarm-name</i> </code> </p> <p>The ARN format of a Contributor Insights rule is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:insight-rule/<i>insight-rule-name</i> </code> </p> <p>The ARN format of a dashboard is <code>arn:aws:cloudwatch::<i>account-id</i>:dashboard/<i>dashboard-name</i> </code> </p> <p>The ARN format of a metric stream is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:metric-stream/<i>metric-stream-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tags: <p>The list of key-value pairs to associate with the alarm.</p>

        Raises:
            capo_cloudwatch.errors.concurrent_modification_exception.ConcurrentModificationException: <p>More than one process tried to modify a resource at the same time.</p>
            capo_cloudwatch.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.tag_resource

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.tag_resource_input.TagResourceInput = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        resource_arn: Optional[
            "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        tag_keys: Optional["capo_cloudwatch.types.tag_key_list.TagKeyList"] = None,
    ) -> "capo_cloudwatch.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from the specified resource. Currently, alarms, dashboards, metric streams and Contributor Insights rules support tagging.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch resource that you're removing tags from.</p> <p>The ARN format of an alarm is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:alarm:<i>alarm-name</i> </code> </p> <p>The ARN format of a Contributor Insights rule is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:insight-rule/<i>insight-rule-name</i> </code> </p> <p>The ARN format of a dashboard is <code>arn:aws:cloudwatch::<i>account-id</i>:dashboard/<i>dashboard-name</i> </code> </p> <p>The ARN format of a metric stream is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:metric-stream/<i>metric-stream-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_cloudwatch.errors.concurrent_modification_exception.ConcurrentModificationException: <p>More than one process tried to modify a resource at the same time.</p>
            capo_cloudwatch.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch.errors.internal_service_fault.InternalServiceFault: <p>Request processing has failed due to some unknown error, exception, or failure.</p>
            capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of an input parameter is bad or out-of-range.</p>
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.untag_resource

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.untag_resource_input.UntagResourceInput = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_o_tel_enrichment(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        include_filters: Optional[
            "capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.OTelEnrichmentMetricSelectorList"
        ] = None,
        exclude_filters: Optional[
            "capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.OTelEnrichmentMetricSelectorList"
        ] = None,
    ) -> "capo_cloudwatch.types.update_o_tel_enrichment_output.UpdateOTelEnrichmentOutput":
        """<p>Replaces the filters that determine which CloudWatch vended metrics are enriched with resource ARN and resource tag labels for the account. Enrichment must already be running for the account. If it is not, this operation returns a <code>ResourceNotFoundException</code>. To start enrichment, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartOTelEnrichment.html">StartOTelEnrichment</a>.</p> <p>The filters in the request completely replace the stored filters; they are not merged with them. <code>IncludeFilters</code> and <code>ExcludeFilters</code> are replaced as a pair, so a request that specifies only <code>IncludeFilters</code> also clears the stored <code>ExcludeFilters</code>, and a request that specifies neither clears both.</p>

        Args:
            include_filters: <p>The metric namespaces, and the metric names, to enrich. If this parameter is omitted, every namespace that Amazon CloudWatch supports for enrichment is in scope.</p> <p>A maximum of 100 filters is allowed across <code>IncludeFilters</code> and <code>ExcludeFilters</code> combined.</p>
            exclude_filters: <p>The metric namespaces, and the metric names, to leave unenriched. If this parameter is omitted, nothing is excluded.</p> <p>Amazon CloudWatch applies <code>ExcludeFilters</code> after <code>IncludeFilters</code>, so a metric that both parameters match is not enriched.</p> <p>A maximum of 100 filters is allowed across <code>IncludeFilters</code> and <code>ExcludeFilters</code> combined.</p>

        Raises:
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters do not satisfy the constraints that the operation requires.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.update_o_tel_enrichment_input.UpdateOTelEnrichmentInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.update_o_tel_enrichment_output.UpdateOTelEnrichmentOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.update_o_tel_enrichment

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.update_o_tel_enrichment.update_o_tel_enrichment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.update_o_tel_enrichment_input.UpdateOTelEnrichmentInput = {}
        if include_filters is not None:
            input_["include_filters"] = include_filters
        if exclude_filters is not None:
            input_["exclude_filters"] = exclude_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resource_metrics_configuration(
        self,
        *,
        config_overrides: Optional[CloudWatchClientConfig] = None,
        resource_arn: Optional["capo_cloudwatch.types.resource_arn.ResourceArn"] = None,
        metric_selections: Optional[
            "capo_cloudwatch.types.resource_metric_selection_list.ResourceMetricSelectionList"
        ] = None,
    ) -> "capo_cloudwatch.types.update_resource_metrics_configuration_output.UpdateResourceMetricsConfigurationOutput":
        """<p>Updates the resource metrics configuration for an Amazon Web Services resource. The <code>MetricSelections</code> value that you provide replaces any existing metric selections for the resource; it is not merged with them.</p> <p>If you omit <code>MetricSelections</code>, Amazon CloudWatch removes any existing metric selection filter and collects all available detailed metrics for the resource.</p> <p>This operation returns a <code>ResourceNotFoundException</code> if no resource metrics configuration exists for the specified resource ARN. To create a configuration, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html">CreateResourceMetricsConfiguration</a>.</p> <p>To update a resource metrics configuration, you must have the <code>cloudwatch:UpdateResourceMetricsConfiguration</code> permission. For information about scoping this permission to specific resources, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html">Condition keys for resource metrics configuration access</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to update the resource metrics configuration for.</p>
            metric_selections: <p>Specifies which metrics Amazon CloudWatch collects for the resource. The selections that you provide completely replace any existing metric selections.</p> <p>If you omit this parameter, Amazon CloudWatch removes any existing metric selection filter and collects all available detailed metrics for the resource.</p>

        Raises:
            capo_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The named resource does not exist.</p>
            capo_cloudwatch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch.types.update_resource_metrics_configuration_input.UpdateResourceMetricsConfigurationInput]",
        ) -> OperationResponse[
            "capo_cloudwatch.types.update_resource_metrics_configuration_output.UpdateResourceMetricsConfigurationOutput"
        ]:
            import capo_cloudwatch._operations.granite_service_version20100801.update_resource_metrics_configuration

            output, http_response = (
                capo_cloudwatch._operations.granite_service_version20100801.update_resource_metrics_configuration.update_resource_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch.types.update_resource_metrics_configuration_input.UpdateResourceMetricsConfigurationInput = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if metric_selections is not None:
            input_["metric_selections"] = metric_selections

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
