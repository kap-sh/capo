"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ComputeOptimizerService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_compute_optimizer._auth._signers
import capo_compute_optimizer._auth._sigv4
from capo_compute_optimizer._auth._identity import Credentials
from capo_compute_optimizer._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_compute_optimizer._auth._zapros_handler import AuthMiddleware
from capo_compute_optimizer._pagination import resolve_path as _resolve_path
from capo_compute_optimizer._services._aws_config import aws_config
from capo_compute_optimizer._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_enrollment_status
    import capo_compute_optimizer.types.account_ids
    import capo_compute_optimizer.types.auto_scaling_group_arns
    import capo_compute_optimizer.types.delete_recommendation_preferences_request
    import capo_compute_optimizer.types.delete_recommendation_preferences_response
    import capo_compute_optimizer.types.describe_recommendation_export_jobs_request
    import capo_compute_optimizer.types.describe_recommendation_export_jobs_response
    import capo_compute_optimizer.types.ebs_filters
    import capo_compute_optimizer.types.ecs_service_recommendation_filters
    import capo_compute_optimizer.types.enhanced_infrastructure_metrics
    import capo_compute_optimizer.types.enrollment_filters
    import capo_compute_optimizer.types.export_auto_scaling_group_recommendations_request
    import capo_compute_optimizer.types.export_auto_scaling_group_recommendations_response
    import capo_compute_optimizer.types.export_ebs_volume_recommendations_request
    import capo_compute_optimizer.types.export_ebs_volume_recommendations_response
    import capo_compute_optimizer.types.export_ec2_instance_recommendations_request
    import capo_compute_optimizer.types.export_ec2_instance_recommendations_response
    import capo_compute_optimizer.types.export_ecs_service_recommendations_request
    import capo_compute_optimizer.types.export_ecs_service_recommendations_response
    import capo_compute_optimizer.types.export_idle_recommendations_request
    import capo_compute_optimizer.types.export_idle_recommendations_response
    import capo_compute_optimizer.types.export_lambda_function_recommendations_request
    import capo_compute_optimizer.types.export_lambda_function_recommendations_response
    import capo_compute_optimizer.types.export_license_recommendations_request
    import capo_compute_optimizer.types.export_license_recommendations_response
    import capo_compute_optimizer.types.export_rds_database_recommendations_request
    import capo_compute_optimizer.types.export_rds_database_recommendations_response
    import capo_compute_optimizer.types.exportable_auto_scaling_group_fields
    import capo_compute_optimizer.types.exportable_ecs_service_fields
    import capo_compute_optimizer.types.exportable_idle_fields
    import capo_compute_optimizer.types.exportable_instance_fields
    import capo_compute_optimizer.types.exportable_lambda_function_fields
    import capo_compute_optimizer.types.exportable_license_fields
    import capo_compute_optimizer.types.exportable_rdsdb_fields
    import capo_compute_optimizer.types.exportable_volume_fields
    import capo_compute_optimizer.types.external_metrics_preference
    import capo_compute_optimizer.types.file_format
    import capo_compute_optimizer.types.filters
    import capo_compute_optimizer.types.function_arns
    import capo_compute_optimizer.types.get_auto_scaling_group_recommendations_request
    import capo_compute_optimizer.types.get_auto_scaling_group_recommendations_response
    import capo_compute_optimizer.types.get_ebs_volume_recommendations_request
    import capo_compute_optimizer.types.get_ebs_volume_recommendations_response
    import capo_compute_optimizer.types.get_ec2_instance_recommendations_request
    import capo_compute_optimizer.types.get_ec2_instance_recommendations_response
    import capo_compute_optimizer.types.get_ec2_recommendation_projected_metrics_request
    import capo_compute_optimizer.types.get_ec2_recommendation_projected_metrics_response
    import capo_compute_optimizer.types.get_ecs_service_recommendation_projected_metrics_request
    import capo_compute_optimizer.types.get_ecs_service_recommendation_projected_metrics_response
    import capo_compute_optimizer.types.get_ecs_service_recommendations_request
    import capo_compute_optimizer.types.get_ecs_service_recommendations_response
    import capo_compute_optimizer.types.get_effective_recommendation_preferences_request
    import capo_compute_optimizer.types.get_effective_recommendation_preferences_response
    import capo_compute_optimizer.types.get_enrollment_status_request
    import capo_compute_optimizer.types.get_enrollment_status_response
    import capo_compute_optimizer.types.get_enrollment_statuses_for_organization_request
    import capo_compute_optimizer.types.get_enrollment_statuses_for_organization_response
    import capo_compute_optimizer.types.get_idle_recommendations_request
    import capo_compute_optimizer.types.get_idle_recommendations_response
    import capo_compute_optimizer.types.get_lambda_function_recommendations_request
    import capo_compute_optimizer.types.get_lambda_function_recommendations_response
    import capo_compute_optimizer.types.get_license_recommendations_request
    import capo_compute_optimizer.types.get_license_recommendations_response
    import capo_compute_optimizer.types.get_rds_database_recommendation_projected_metrics_request
    import capo_compute_optimizer.types.get_rds_database_recommendation_projected_metrics_response
    import capo_compute_optimizer.types.get_rds_database_recommendations_request
    import capo_compute_optimizer.types.get_rds_database_recommendations_response
    import capo_compute_optimizer.types.get_recommendation_preferences_request
    import capo_compute_optimizer.types.get_recommendation_preferences_response
    import capo_compute_optimizer.types.get_recommendation_summaries_request
    import capo_compute_optimizer.types.get_recommendation_summaries_response
    import capo_compute_optimizer.types.idle_max_results
    import capo_compute_optimizer.types.idle_recommendation_filters
    import capo_compute_optimizer.types.include_member_accounts
    import capo_compute_optimizer.types.inferred_workload_types_preference
    import capo_compute_optimizer.types.instance_arn
    import capo_compute_optimizer.types.instance_arns
    import capo_compute_optimizer.types.job_filters
    import capo_compute_optimizer.types.job_ids
    import capo_compute_optimizer.types.lambda_function_recommendation
    import capo_compute_optimizer.types.lambda_function_recommendation_filters
    import capo_compute_optimizer.types.license_recommendation_filters
    import capo_compute_optimizer.types.look_back_period_preference
    import capo_compute_optimizer.types.max_results
    import capo_compute_optimizer.types.metric_statistic
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.order_by
    import capo_compute_optimizer.types.period
    import capo_compute_optimizer.types.preferred_resources
    import capo_compute_optimizer.types.put_recommendation_preferences_request
    import capo_compute_optimizer.types.put_recommendation_preferences_response
    import capo_compute_optimizer.types.rdsdb_recommendation_filters
    import capo_compute_optimizer.types.recommendation_export_job
    import capo_compute_optimizer.types.recommendation_preference_names
    import capo_compute_optimizer.types.recommendation_preferences
    import capo_compute_optimizer.types.recommendation_preferences_detail
    import capo_compute_optimizer.types.recommendation_summary
    import capo_compute_optimizer.types.resource_arn
    import capo_compute_optimizer.types.resource_arns
    import capo_compute_optimizer.types.resource_type
    import capo_compute_optimizer.types.s3_destination_config
    import capo_compute_optimizer.types.savings_estimation_mode
    import capo_compute_optimizer.types.scope
    import capo_compute_optimizer.types.service_arn
    import capo_compute_optimizer.types.service_arns
    import capo_compute_optimizer.types.status
    import capo_compute_optimizer.types.timestamp
    import capo_compute_optimizer.types.update_enrollment_status_request
    import capo_compute_optimizer.types.update_enrollment_status_response
    import capo_compute_optimizer.types.utilization_preferences
    import capo_compute_optimizer.types.volume_arns


class ComputeOptimizerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ComputeOptimizerClient:
    """A client for the ``ComputeOptimizer`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = ComputeOptimizerClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[ComputeOptimizerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ComputeOptimizerClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def delete_recommendation_preferences(
        self,
        resource_type: "capo_compute_optimizer.types.resource_type.ResourceType",
        recommendation_preference_names: "capo_compute_optimizer.types.recommendation_preference_names.RecommendationPreferenceNames",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        scope: Optional["capo_compute_optimizer.types.scope.Scope"] = None,
    ) -> "capo_compute_optimizer.types.delete_recommendation_preferences_response.DeleteRecommendationPreferencesResponse":
        """<p>Deletes a recommendation preference, such as enhanced infrastructure metrics.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            resource_type: <p>The target resource type of the recommendation preference to delete.</p> <p>The <code>Ec2Instance</code> option encompasses standalone instances and instances that are part of Auto Scaling groups. The <code>AutoScalingGroup</code> option encompasses only instances that are part of an Auto Scaling group.</p>
            scope: <p>An object that describes the scope of the recommendation preference to delete.</p> <p>You can delete recommendation preferences that are created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>
            recommendation_preference_names: <p>The name of the recommendation preference to delete.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.delete_recommendation_preferences_request.DeleteRecommendationPreferencesRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.delete_recommendation_preferences_response.DeleteRecommendationPreferencesResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.delete_recommendation_preferences

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.delete_recommendation_preferences.delete_recommendation_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.delete_recommendation_preferences_request.DeleteRecommendationPreferencesRequest = {
            "resource_type": resource_type,
            "recommendation_preference_names": recommendation_preference_names,
        }
        if scope is not None:
            input_["scope"] = scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_recommendation_export_jobs(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        job_ids: Optional["capo_compute_optimizer.types.job_ids.JobIds"] = None,
        filters: Optional["capo_compute_optimizer.types.job_filters.JobFilters"] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_compute_optimizer.types.describe_recommendation_export_jobs_response.DescribeRecommendationExportJobsResponse":
        """<p>Describes recommendation export jobs created in the last seven days.</p> <p>Use the <a>ExportAutoScalingGroupRecommendations</a> or <a>ExportEC2InstanceRecommendations</a> actions to request an export of your recommendations. Then use the <a>DescribeRecommendationExportJobs</a> action to view your export jobs.</p>

        Args:
            job_ids: <p>The identification numbers of the export jobs to return.</p> <p>An export job ID is returned when you create an export using the <a>ExportAutoScalingGroupRecommendations</a> or <a>ExportEC2InstanceRecommendations</a> actions.</p> <p>All export jobs created in the last seven days are returned if this parameter is omitted.</p>
            filters: <p>An array of objects to specify a filter that returns a more specific list of export jobs.</p>
            next_token: <p>The token to advance to the next page of export jobs.</p>
            max_results: <p>The maximum number of export jobs to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.describe_recommendation_export_jobs_request.DescribeRecommendationExportJobsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.describe_recommendation_export_jobs_response.DescribeRecommendationExportJobsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.describe_recommendation_export_jobs

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.describe_recommendation_export_jobs.describe_recommendation_export_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.describe_recommendation_export_jobs_request.DescribeRecommendationExportJobsRequest = {}
        if job_ids is not None:
            input_["job_ids"] = job_ids
        if filters is not None:
            input_["filters"] = filters
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

    def iter_describe_recommendation_export_jobs(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        job_ids: Optional["capo_compute_optimizer.types.job_ids.JobIds"] = None,
        filters: Optional["capo_compute_optimizer.types.job_filters.JobFilters"] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_compute_optimizer.types.recommendation_export_job.RecommendationExportJob]":
        _token = next_token
        while True:
            _response = self.describe_recommendation_export_jobs(
                config_overrides=config_overrides,
                job_ids=job_ids,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("recommendation_export_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def export_auto_scaling_group_recommendations(
        self,
        s3_destination_config: "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional["capo_compute_optimizer.types.filters.Filters"] = None,
        fields_to_export: Optional[
            "capo_compute_optimizer.types.exportable_auto_scaling_group_fields.ExportableAutoScalingGroupFields"
        ] = None,
        file_format: Optional[
            "capo_compute_optimizer.types.file_format.FileFormat"
        ] = None,
        include_member_accounts: Optional[
            "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
        ] = None,
        recommendation_preferences: Optional[
            "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
        ] = None,
    ) -> "capo_compute_optimizer.types.export_auto_scaling_group_recommendations_response.ExportAutoScalingGroupRecommendationsResponse":
        """<p>Exports optimization recommendations for Auto Scaling groups.</p> <p>Recommendations are exported in a comma-separated values (.csv) file, and its metadata in a JavaScript Object Notation (JSON) (.json) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html">Exporting Recommendations</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>You can have only one Auto Scaling group export job in progress per Amazon Web Services Region.</p>

        Args:
            account_ids: <p>The IDs of the Amazon Web Services accounts for which to export Auto Scaling group recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.</p> <p>This parameter cannot be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the include member accounts parameter, is omitted.</p> <p>You can specify multiple account IDs per request.</p>
            filters: <p>An array of objects to specify a filter that exports a more specific set of Auto Scaling group recommendations.</p>
            fields_to_export: <p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>
            s3_destination_config: <p>An object to specify the destination Amazon Simple Storage Service (Amazon S3) bucket name and key prefix for the export job.</p> <p>You must create the destination Amazon S3 bucket for your recommendations export before you create the export job. Compute Optimizer does not create the S3 bucket for you. After you create the S3 bucket, ensure that it has the required permissions policy to allow Compute Optimizer to write the export file to it. If you plan to specify an object prefix when you create the export job, you must include the object prefix in the policy that you add to the S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html">Amazon S3 Bucket Policy for Compute Optimizer</a> in the <i>Compute Optimizer User Guide</i>.</p>
            file_format: <p>The format of the export file.</p> <p>The only export file format currently supported is <code>Csv</code>.</p>
            include_member_accounts: <p>Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>Recommendations for member accounts of the organization are not included in the export file if this parameter is omitted.</p> <p>This parameter cannot be specified together with the account IDs parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the account IDs parameter, is omitted.</p>
            recommendation_preferences: <p>An object to specify the preferences for the Auto Scaling group recommendations to export.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a limit of the service.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.export_auto_scaling_group_recommendations_request.ExportAutoScalingGroupRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.export_auto_scaling_group_recommendations_response.ExportAutoScalingGroupRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.export_auto_scaling_group_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.export_auto_scaling_group_recommendations.export_auto_scaling_group_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.export_auto_scaling_group_recommendations_request.ExportAutoScalingGroupRecommendationsRequest = {
            "s3_destination_config": s3_destination_config
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if filters is not None:
            input_["filters"] = filters
        if fields_to_export is not None:
            input_["fields_to_export"] = fields_to_export
        if file_format is not None:
            input_["file_format"] = file_format
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts
        if recommendation_preferences is not None:
            input_["recommendation_preferences"] = recommendation_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_ebs_volume_recommendations(
        self,
        s3_destination_config: "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional["capo_compute_optimizer.types.ebs_filters.EBSFilters"] = None,
        fields_to_export: Optional[
            "capo_compute_optimizer.types.exportable_volume_fields.ExportableVolumeFields"
        ] = None,
        file_format: Optional[
            "capo_compute_optimizer.types.file_format.FileFormat"
        ] = None,
        include_member_accounts: Optional[
            "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
        ] = None,
    ) -> "capo_compute_optimizer.types.export_ebs_volume_recommendations_response.ExportEBSVolumeRecommendationsResponse":
        """<p>Exports optimization recommendations for Amazon EBS volumes.</p> <p>Recommendations are exported in a comma-separated values (.csv) file, and its metadata in a JavaScript Object Notation (JSON) (.json) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html">Exporting Recommendations</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>You can have only one Amazon EBS volume export job in progress per Amazon Web Services Region.</p>

        Args:
            account_ids: <p>The IDs of the Amazon Web Services accounts for which to export Amazon EBS volume recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.</p> <p>This parameter cannot be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the include member accounts parameter, is omitted.</p> <p>You can specify multiple account IDs per request.</p>
            filters: <p>An array of objects to specify a filter that exports a more specific set of Amazon EBS volume recommendations.</p>
            fields_to_export: <p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>
            file_format: <p>The format of the export file.</p> <p>The only export file format currently supported is <code>Csv</code>.</p>
            include_member_accounts: <p>Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>Recommendations for member accounts of the organization are not included in the export file if this parameter is omitted.</p> <p>This parameter cannot be specified together with the account IDs parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the account IDs parameter, is omitted.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a limit of the service.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.export_ebs_volume_recommendations_request.ExportEBSVolumeRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.export_ebs_volume_recommendations_response.ExportEBSVolumeRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.export_ebs_volume_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.export_ebs_volume_recommendations.export_ebs_volume_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.export_ebs_volume_recommendations_request.ExportEBSVolumeRecommendationsRequest = {
            "s3_destination_config": s3_destination_config
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if filters is not None:
            input_["filters"] = filters
        if fields_to_export is not None:
            input_["fields_to_export"] = fields_to_export
        if file_format is not None:
            input_["file_format"] = file_format
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_ec2_instance_recommendations(
        self,
        s3_destination_config: "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional["capo_compute_optimizer.types.filters.Filters"] = None,
        fields_to_export: Optional[
            "capo_compute_optimizer.types.exportable_instance_fields.ExportableInstanceFields"
        ] = None,
        file_format: Optional[
            "capo_compute_optimizer.types.file_format.FileFormat"
        ] = None,
        include_member_accounts: Optional[
            "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
        ] = None,
        recommendation_preferences: Optional[
            "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
        ] = None,
    ) -> "capo_compute_optimizer.types.export_ec2_instance_recommendations_response.ExportEC2InstanceRecommendationsResponse":
        """<p>Exports optimization recommendations for Amazon EC2 instances.</p> <p>Recommendations are exported in a comma-separated values (.csv) file, and its metadata in a JavaScript Object Notation (JSON) (.json) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html">Exporting Recommendations</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>You can have only one Amazon EC2 instance export job in progress per Amazon Web Services Region.</p>

        Args:
            account_ids: <p>The IDs of the Amazon Web Services accounts for which to export instance recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.</p> <p>This parameter cannot be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the include member accounts parameter, is omitted.</p> <p>You can specify multiple account IDs per request.</p>
            filters: <p>An array of objects to specify a filter that exports a more specific set of instance recommendations.</p>
            fields_to_export: <p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>
            s3_destination_config: <p>An object to specify the destination Amazon Simple Storage Service (Amazon S3) bucket name and key prefix for the export job.</p> <p>You must create the destination Amazon S3 bucket for your recommendations export before you create the export job. Compute Optimizer does not create the S3 bucket for you. After you create the S3 bucket, ensure that it has the required permissions policy to allow Compute Optimizer to write the export file to it. If you plan to specify an object prefix when you create the export job, you must include the object prefix in the policy that you add to the S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html">Amazon S3 Bucket Policy for Compute Optimizer</a> in the <i>Compute Optimizer User Guide</i>.</p>
            file_format: <p>The format of the export file.</p> <p>The only export file format currently supported is <code>Csv</code>.</p>
            include_member_accounts: <p>Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>Recommendations for member accounts of the organization are not included in the export file if this parameter is omitted.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the account IDs parameter, is omitted.</p>
            recommendation_preferences: <p>An object to specify the preferences for the Amazon EC2 instance recommendations to export.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a limit of the service.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.export_ec2_instance_recommendations_request.ExportEC2InstanceRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.export_ec2_instance_recommendations_response.ExportEC2InstanceRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.export_ec2_instance_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.export_ec2_instance_recommendations.export_ec2_instance_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.export_ec2_instance_recommendations_request.ExportEC2InstanceRecommendationsRequest = {
            "s3_destination_config": s3_destination_config
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if filters is not None:
            input_["filters"] = filters
        if fields_to_export is not None:
            input_["fields_to_export"] = fields_to_export
        if file_format is not None:
            input_["file_format"] = file_format
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts
        if recommendation_preferences is not None:
            input_["recommendation_preferences"] = recommendation_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_ecs_service_recommendations(
        self,
        s3_destination_config: "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.ecs_service_recommendation_filters.ECSServiceRecommendationFilters"
        ] = None,
        fields_to_export: Optional[
            "capo_compute_optimizer.types.exportable_ecs_service_fields.ExportableECSServiceFields"
        ] = None,
        file_format: Optional[
            "capo_compute_optimizer.types.file_format.FileFormat"
        ] = None,
        include_member_accounts: Optional[
            "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
        ] = None,
    ) -> "capo_compute_optimizer.types.export_ecs_service_recommendations_response.ExportECSServiceRecommendationsResponse":
        """<p> Exports optimization recommendations for Amazon ECS services on Fargate. </p> <p>Recommendations are exported in a CSV file, and its metadata in a JSON file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html">Exporting Recommendations</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>You can only have one Amazon ECS service export job in progress per Amazon Web Services Region.</p>

        Args:
            account_ids: <p> The Amazon Web Services account IDs for the export Amazon ECS service recommendations. </p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to specify the member account you want to export recommendations to.</p> <p>This parameter can't be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>If this parameter or the include member accounts parameter is omitted, the recommendations for member accounts aren't included in the export.</p> <p>You can specify multiple account IDs per request.</p>
            filters: <p> An array of objects to specify a filter that exports a more specific set of Amazon ECS service recommendations. </p>
            fields_to_export: <p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>
            file_format: <p> The format of the export file. </p> <p>The CSV file is the only export file format currently supported.</p>
            include_member_accounts: <p>If your account is the management account or the delegated administrator of an organization, this parameter indicates whether to include recommendations for resources in all member accounts of the organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>If this parameter is omitted, recommendations for member accounts of the organization aren't included in the export file.</p> <p>If this parameter or the account ID parameter is omitted, recommendations for member accounts aren't included in the export.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a limit of the service.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.export_ecs_service_recommendations_request.ExportECSServiceRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.export_ecs_service_recommendations_response.ExportECSServiceRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.export_ecs_service_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.export_ecs_service_recommendations.export_ecs_service_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.export_ecs_service_recommendations_request.ExportECSServiceRecommendationsRequest = {
            "s3_destination_config": s3_destination_config
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if filters is not None:
            input_["filters"] = filters
        if fields_to_export is not None:
            input_["fields_to_export"] = fields_to_export
        if file_format is not None:
            input_["file_format"] = file_format
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_idle_recommendations(
        self,
        s3_destination_config: "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.idle_recommendation_filters.IdleRecommendationFilters"
        ] = None,
        fields_to_export: Optional[
            "capo_compute_optimizer.types.exportable_idle_fields.ExportableIdleFields"
        ] = None,
        file_format: Optional[
            "capo_compute_optimizer.types.file_format.FileFormat"
        ] = None,
        include_member_accounts: Optional[
            "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
        ] = None,
    ) -> "capo_compute_optimizer.types.export_idle_recommendations_response.ExportIdleRecommendationsResponse":
        """<p> Export optimization recommendations for your idle resources. </p> <p>Recommendations are exported in a comma-separated values (CSV) file, and its metadata in a JavaScript Object Notation (JSON) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html">Exporting Recommendations</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>You can have only one idle resource export job in progress per Amazon Web Services Region.</p>

        Args:
            account_ids: <p> The Amazon Web Services account IDs for the export idle resource recommendations. </p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to specify the member account you want to export recommendations to.</p> <p>This parameter can't be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>If this parameter or the include member accounts parameter is omitted, the recommendations for member accounts aren't included in the export.</p> <p>You can specify multiple account IDs per request.</p>
            filters: <p>An array of objects to specify a filter that exports a more specific set of idle resource recommendations.</p>
            fields_to_export: <p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>
            file_format: <p>The format of the export file. The CSV file is the only export file format currently supported.</p>
            include_member_accounts: <p>If your account is the management account or the delegated administrator of an organization, this parameter indicates whether to include recommendations for resources in all member accounts of the organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>If this parameter is omitted, recommendations for member accounts of the organization aren't included in the export file.</p> <p>If this parameter or the account ID parameter is omitted, recommendations for member accounts aren't included in the export.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a limit of the service.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.export_idle_recommendations_request.ExportIdleRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.export_idle_recommendations_response.ExportIdleRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.export_idle_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.export_idle_recommendations.export_idle_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.export_idle_recommendations_request.ExportIdleRecommendationsRequest = {
            "s3_destination_config": s3_destination_config
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if filters is not None:
            input_["filters"] = filters
        if fields_to_export is not None:
            input_["fields_to_export"] = fields_to_export
        if file_format is not None:
            input_["file_format"] = file_format
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_lambda_function_recommendations(
        self,
        s3_destination_config: "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.lambda_function_recommendation_filters.LambdaFunctionRecommendationFilters"
        ] = None,
        fields_to_export: Optional[
            "capo_compute_optimizer.types.exportable_lambda_function_fields.ExportableLambdaFunctionFields"
        ] = None,
        file_format: Optional[
            "capo_compute_optimizer.types.file_format.FileFormat"
        ] = None,
        include_member_accounts: Optional[
            "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
        ] = None,
    ) -> "capo_compute_optimizer.types.export_lambda_function_recommendations_response.ExportLambdaFunctionRecommendationsResponse":
        """<p>Exports optimization recommendations for Lambda functions.</p> <p>Recommendations are exported in a comma-separated values (.csv) file, and its metadata in a JavaScript Object Notation (JSON) (.json) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html">Exporting Recommendations</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>You can have only one Lambda function export job in progress per Amazon Web Services Region.</p>

        Args:
            account_ids: <p>The IDs of the Amazon Web Services accounts for which to export Lambda function recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.</p> <p>This parameter cannot be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the include member accounts parameter, is omitted.</p> <p>You can specify multiple account IDs per request.</p>
            filters: <p>An array of objects to specify a filter that exports a more specific set of Lambda function recommendations.</p>
            fields_to_export: <p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>
            file_format: <p>The format of the export file.</p> <p>The only export file format currently supported is <code>Csv</code>.</p>
            include_member_accounts: <p>Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>Recommendations for member accounts of the organization are not included in the export file if this parameter is omitted.</p> <p>This parameter cannot be specified together with the account IDs parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the account IDs parameter, is omitted.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a limit of the service.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.export_lambda_function_recommendations_request.ExportLambdaFunctionRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.export_lambda_function_recommendations_response.ExportLambdaFunctionRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.export_lambda_function_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.export_lambda_function_recommendations.export_lambda_function_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.export_lambda_function_recommendations_request.ExportLambdaFunctionRecommendationsRequest = {
            "s3_destination_config": s3_destination_config
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if filters is not None:
            input_["filters"] = filters
        if fields_to_export is not None:
            input_["fields_to_export"] = fields_to_export
        if file_format is not None:
            input_["file_format"] = file_format
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_license_recommendations(
        self,
        s3_destination_config: "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.license_recommendation_filters.LicenseRecommendationFilters"
        ] = None,
        fields_to_export: Optional[
            "capo_compute_optimizer.types.exportable_license_fields.ExportableLicenseFields"
        ] = None,
        file_format: Optional[
            "capo_compute_optimizer.types.file_format.FileFormat"
        ] = None,
        include_member_accounts: Optional[
            "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
        ] = None,
    ) -> "capo_compute_optimizer.types.export_license_recommendations_response.ExportLicenseRecommendationsResponse":
        """<p> Export optimization recommendations for your licenses. </p> <p>Recommendations are exported in a comma-separated values (CSV) file, and its metadata in a JavaScript Object Notation (JSON) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html">Exporting Recommendations</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>You can have only one license export job in progress per Amazon Web Services Region.</p>

        Args:
            account_ids: <p>The IDs of the Amazon Web Services accounts for which to export license recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.</p> <p>This parameter can't be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>If this parameter is omitted, recommendations for member accounts aren't included in the export.</p> <p>You can specify multiple account IDs per request.</p>
            filters: <p> An array of objects to specify a filter that exports a more specific set of license recommendations. </p>
            fields_to_export: <p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>
            file_format: <p>The format of the export file.</p> <p>A CSV file is the only export format currently supported.</p>
            include_member_accounts: <p>Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>If this parameter is omitted, recommendations for member accounts of the organization aren't included in the export file .</p> <p>This parameter cannot be specified together with the account IDs parameter. The parameters are mutually exclusive.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a limit of the service.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.export_license_recommendations_request.ExportLicenseRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.export_license_recommendations_response.ExportLicenseRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.export_license_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.export_license_recommendations.export_license_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.export_license_recommendations_request.ExportLicenseRecommendationsRequest = {
            "s3_destination_config": s3_destination_config
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if filters is not None:
            input_["filters"] = filters
        if fields_to_export is not None:
            input_["fields_to_export"] = fields_to_export
        if file_format is not None:
            input_["file_format"] = file_format
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_rds_database_recommendations(
        self,
        s3_destination_config: "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.rdsdb_recommendation_filters.RDSDBRecommendationFilters"
        ] = None,
        fields_to_export: Optional[
            "capo_compute_optimizer.types.exportable_rdsdb_fields.ExportableRDSDBFields"
        ] = None,
        file_format: Optional[
            "capo_compute_optimizer.types.file_format.FileFormat"
        ] = None,
        include_member_accounts: Optional[
            "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
        ] = None,
        recommendation_preferences: Optional[
            "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
        ] = None,
    ) -> "capo_compute_optimizer.types.export_rds_database_recommendations_response.ExportRDSDatabaseRecommendationsResponse":
        """<p> Export optimization recommendations for your Amazon Aurora and Amazon Relational Database Service (Amazon RDS) databases. </p> <p>Recommendations are exported in a comma-separated values (CSV) file, and its metadata in a JavaScript Object Notation (JSON) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html">Exporting Recommendations</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>You can have only one Amazon Aurora or RDS export job in progress per Amazon Web Services Region.</p>

        Args:
            account_ids: <p> The Amazon Web Services account IDs for the export Amazon Aurora and RDS database recommendations. </p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to specify the member account you want to export recommendations to.</p> <p>This parameter can't be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>If this parameter or the include member accounts parameter is omitted, the recommendations for member accounts aren't included in the export.</p> <p>You can specify multiple account IDs per request.</p>
            filters: <p> An array of objects to specify a filter that exports a more specific set of Amazon Aurora and RDS recommendations. </p>
            fields_to_export: <p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>
            file_format: <p> The format of the export file. </p> <p>The CSV file is the only export file format currently supported.</p>
            include_member_accounts: <p>If your account is the management account or the delegated administrator of an organization, this parameter indicates whether to include recommendations for resources in all member accounts of the organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>If this parameter is omitted, recommendations for member accounts of the organization aren't included in the export file.</p> <p>If this parameter or the account ID parameter is omitted, recommendations for member accounts aren't included in the export.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a limit of the service.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.export_rds_database_recommendations_request.ExportRDSDatabaseRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.export_rds_database_recommendations_response.ExportRDSDatabaseRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.export_rds_database_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.export_rds_database_recommendations.export_rds_database_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.export_rds_database_recommendations_request.ExportRDSDatabaseRecommendationsRequest = {
            "s3_destination_config": s3_destination_config
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if filters is not None:
            input_["filters"] = filters
        if fields_to_export is not None:
            input_["fields_to_export"] = fields_to_export
        if file_format is not None:
            input_["file_format"] = file_format
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts
        if recommendation_preferences is not None:
            input_["recommendation_preferences"] = recommendation_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_auto_scaling_group_recommendations(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        auto_scaling_group_arns: Optional[
            "capo_compute_optimizer.types.auto_scaling_group_arns.AutoScalingGroupArns"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
        filters: Optional["capo_compute_optimizer.types.filters.Filters"] = None,
        recommendation_preferences: Optional[
            "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_auto_scaling_group_recommendations_response.GetAutoScalingGroupRecommendationsResponse":
        """<p>Returns Auto Scaling group recommendations.</p> <p>Compute Optimizer generates recommendations for Amazon EC2 Auto Scaling groups that meet a specific set of requirements. For more information, see the <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html">Supported resources and requirements</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            account_ids: <p>The ID of the Amazon Web Services account for which to return Auto Scaling group recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return Auto Scaling group recommendations.</p> <p>Only one account ID can be specified per request.</p>
            auto_scaling_group_arns: <p>The Amazon Resource Name (ARN) of the Auto Scaling groups for which to return recommendations.</p>
            next_token: <p>The token to advance to the next page of Auto Scaling group recommendations.</p>
            max_results: <p>The maximum number of Auto Scaling group recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>
            filters: <p>An array of objects to specify a filter that returns a more specific list of Auto Scaling group recommendations.</p>
            recommendation_preferences: <p>An object to specify the preferences for the Auto Scaling group recommendations to return in the response.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_auto_scaling_group_recommendations_request.GetAutoScalingGroupRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_auto_scaling_group_recommendations_response.GetAutoScalingGroupRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_auto_scaling_group_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_auto_scaling_group_recommendations.get_auto_scaling_group_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_auto_scaling_group_recommendations_request.GetAutoScalingGroupRecommendationsRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if auto_scaling_group_arns is not None:
            input_["auto_scaling_group_arns"] = auto_scaling_group_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if recommendation_preferences is not None:
            input_["recommendation_preferences"] = recommendation_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ebs_volume_recommendations(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        volume_arns: Optional[
            "capo_compute_optimizer.types.volume_arns.VolumeArns"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
        filters: Optional["capo_compute_optimizer.types.ebs_filters.EBSFilters"] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_ebs_volume_recommendations_response.GetEBSVolumeRecommendationsResponse":
        """<p>Returns Amazon Elastic Block Store (Amazon EBS) volume recommendations.</p> <p>Compute Optimizer generates recommendations for Amazon EBS volumes that meet a specific set of requirements. For more information, see the <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html">Supported resources and requirements</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            volume_arns: <p>The Amazon Resource Name (ARN) of the volumes for which to return recommendations.</p>
            next_token: <p>The token to advance to the next page of volume recommendations.</p>
            max_results: <p>The maximum number of volume recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>
            filters: <p>An array of objects to specify a filter that returns a more specific list of volume recommendations.</p>
            account_ids: <p>The ID of the Amazon Web Services account for which to return volume recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return volume recommendations.</p> <p>Only one account ID can be specified per request.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_ebs_volume_recommendations_request.GetEBSVolumeRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_ebs_volume_recommendations_response.GetEBSVolumeRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_ebs_volume_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_ebs_volume_recommendations.get_ebs_volume_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_ebs_volume_recommendations_request.GetEBSVolumeRecommendationsRequest = {}
        if volume_arns is not None:
            input_["volume_arns"] = volume_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ec2_instance_recommendations(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        instance_arns: Optional[
            "capo_compute_optimizer.types.instance_arns.InstanceArns"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
        filters: Optional["capo_compute_optimizer.types.filters.Filters"] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        recommendation_preferences: Optional[
            "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_ec2_instance_recommendations_response.GetEC2InstanceRecommendationsResponse":
        """<p>Returns Amazon EC2 instance recommendations.</p> <p>Compute Optimizer generates recommendations for Amazon Elastic Compute Cloud (Amazon EC2) instances that meet a specific set of requirements. For more information, see the <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html">Supported resources and requirements</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            instance_arns: <p>The Amazon Resource Name (ARN) of the instances for which to return recommendations.</p>
            next_token: <p>The token to advance to the next page of instance recommendations.</p>
            max_results: <p>The maximum number of instance recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>
            filters: <p>An array of objects to specify a filter that returns a more specific list of instance recommendations.</p>
            account_ids: <p>The ID of the Amazon Web Services account for which to return instance recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return instance recommendations.</p> <p>Only one account ID can be specified per request.</p>
            recommendation_preferences: <p>An object to specify the preferences for the Amazon EC2 instance recommendations to return in the response.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_ec2_instance_recommendations_request.GetEC2InstanceRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_ec2_instance_recommendations_response.GetEC2InstanceRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_ec2_instance_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_ec2_instance_recommendations.get_ec2_instance_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_ec2_instance_recommendations_request.GetEC2InstanceRecommendationsRequest = {}
        if instance_arns is not None:
            input_["instance_arns"] = instance_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if recommendation_preferences is not None:
            input_["recommendation_preferences"] = recommendation_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ec2_recommendation_projected_metrics(
        self,
        instance_arn: "capo_compute_optimizer.types.instance_arn.InstanceArn",
        stat: "capo_compute_optimizer.types.metric_statistic.MetricStatistic",
        period: "capo_compute_optimizer.types.period.Period",
        start_time: "capo_compute_optimizer.types.timestamp.Timestamp",
        end_time: "capo_compute_optimizer.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        recommendation_preferences: Optional[
            "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_ec2_recommendation_projected_metrics_response.GetEC2RecommendationProjectedMetricsResponse":
        """<p>Returns the projected utilization metrics of Amazon EC2 instance recommendations.</p> <note> <p>The <code>Cpu</code> and <code>Memory</code> metrics are the only projected utilization metrics returned when you run this action. Additionally, the <code>Memory</code> metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent">Enabling Memory Utilization with the CloudWatch Agent</a>.</p> </note>

        Args:
            instance_arn: <p>The Amazon Resource Name (ARN) of the instances for which to return recommendation projected metrics.</p>
            stat: <p>The statistic of the projected metrics.</p>
            period: <p>The granularity, in seconds, of the projected metrics data points.</p>
            start_time: <p>The timestamp of the first projected metrics data point to return.</p>
            end_time: <p>The timestamp of the last projected metrics data point to return.</p>
            recommendation_preferences: <p>An object to specify the preferences for the Amazon EC2 recommendation projected metrics to return in the response.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_ec2_recommendation_projected_metrics_request.GetEC2RecommendationProjectedMetricsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_ec2_recommendation_projected_metrics_response.GetEC2RecommendationProjectedMetricsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_ec2_recommendation_projected_metrics

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_ec2_recommendation_projected_metrics.get_ec2_recommendation_projected_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_ec2_recommendation_projected_metrics_request.GetEC2RecommendationProjectedMetricsRequest = {
            "instance_arn": instance_arn,
            "stat": stat,
            "period": period,
            "start_time": start_time,
            "end_time": end_time,
        }
        if recommendation_preferences is not None:
            input_["recommendation_preferences"] = recommendation_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ecs_service_recommendation_projected_metrics(
        self,
        service_arn: "capo_compute_optimizer.types.service_arn.ServiceArn",
        stat: "capo_compute_optimizer.types.metric_statistic.MetricStatistic",
        period: "capo_compute_optimizer.types.period.Period",
        start_time: "capo_compute_optimizer.types.timestamp.Timestamp",
        end_time: "capo_compute_optimizer.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
    ) -> "capo_compute_optimizer.types.get_ecs_service_recommendation_projected_metrics_response.GetECSServiceRecommendationProjectedMetricsResponse":
        """<p> Returns the projected metrics of Amazon ECS service recommendations. </p>

        Args:
            service_arn: <p> The ARN that identifies the Amazon ECS service. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name</code> </p>
            stat: <p> The statistic of the projected metrics. </p>
            period: <p> The granularity, in seconds, of the projected metrics data points. </p>
            start_time: <p> The timestamp of the first projected metrics data point to return. </p>
            end_time: <p> The timestamp of the last projected metrics data point to return. </p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_ecs_service_recommendation_projected_metrics_request.GetECSServiceRecommendationProjectedMetricsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_ecs_service_recommendation_projected_metrics_response.GetECSServiceRecommendationProjectedMetricsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_ecs_service_recommendation_projected_metrics

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_ecs_service_recommendation_projected_metrics.get_ecs_service_recommendation_projected_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_ecs_service_recommendation_projected_metrics_request.GetECSServiceRecommendationProjectedMetricsRequest = {
            "service_arn": service_arn,
            "stat": stat,
            "period": period,
            "start_time": start_time,
            "end_time": end_time,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ecs_service_recommendations(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        service_arns: Optional[
            "capo_compute_optimizer.types.service_arns.ServiceArns"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.ecs_service_recommendation_filters.ECSServiceRecommendationFilters"
        ] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_ecs_service_recommendations_response.GetECSServiceRecommendationsResponse":
        """<p> Returns Amazon ECS service recommendations. </p> <p> Compute Optimizer generates recommendations for Amazon ECS services on Fargate that meet a specific set of requirements. For more information, see the <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html">Supported resources and requirements</a> in the <i>Compute Optimizer User Guide</i>. </p>

        Args:
            service_arns: <p> The ARN that identifies the Amazon ECS service. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name</code> </p>
            next_token: <p> The token to advance to the next page of Amazon ECS service recommendations. </p>
            max_results: <p> The maximum number of Amazon ECS service recommendations to return with a single request. </p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>
            filters: <p> An array of objects to specify a filter that returns a more specific list of Amazon ECS service recommendations. </p>
            account_ids: <p> Return the Amazon ECS service recommendations to the specified Amazon Web Services account IDs. </p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to return the Amazon ECS service recommendations to specific member accounts.</p> <p>You can only specify one account ID per request.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_ecs_service_recommendations_request.GetECSServiceRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_ecs_service_recommendations_response.GetECSServiceRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_ecs_service_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_ecs_service_recommendations.get_ecs_service_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_ecs_service_recommendations_request.GetECSServiceRecommendationsRequest = {}
        if service_arns is not None:
            input_["service_arns"] = service_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_effective_recommendation_preferences(
        self,
        resource_arn: "capo_compute_optimizer.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
    ) -> "capo_compute_optimizer.types.get_effective_recommendation_preferences_response.GetEffectiveRecommendationPreferencesResponse":
        """<p>Returns the recommendation preferences that are in effect for a given resource, such as enhanced infrastructure metrics. Considers all applicable preferences that you might have set at the resource, account, and organization level.</p> <p>When you create a recommendation preference, you can set its status to <code>Active</code> or <code>Inactive</code>. Use this action to view the recommendation preferences that are in effect, or <code>Active</code>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to confirm effective recommendation preferences. Only EC2 instance and Auto Scaling group ARNs are currently supported.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_effective_recommendation_preferences_request.GetEffectiveRecommendationPreferencesRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_effective_recommendation_preferences_response.GetEffectiveRecommendationPreferencesResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_effective_recommendation_preferences

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_effective_recommendation_preferences.get_effective_recommendation_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_effective_recommendation_preferences_request.GetEffectiveRecommendationPreferencesRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_enrollment_status(
        self, *, config_overrides: Optional[ComputeOptimizerClientConfig] = None
    ) -> "capo_compute_optimizer.types.get_enrollment_status_response.GetEnrollmentStatusResponse":
        """<p>Returns the enrollment (opt in) status of an account to the Compute Optimizer service.</p> <p>If the account is the management account of an organization, this action also confirms the enrollment status of member accounts of the organization. Use the <a>GetEnrollmentStatusesForOrganization</a> action to get detailed information about the enrollment status of member accounts of an organization.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_enrollment_status_request.GetEnrollmentStatusRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_enrollment_status_response.GetEnrollmentStatusResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_enrollment_status

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_enrollment_status.get_enrollment_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_enrollment_status_request.GetEnrollmentStatusRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_enrollment_statuses_for_organization(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        filters: Optional[
            "capo_compute_optimizer.types.enrollment_filters.EnrollmentFilters"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_enrollment_statuses_for_organization_response.GetEnrollmentStatusesForOrganizationResponse":
        """<p>Returns the Compute Optimizer enrollment (opt-in) status of organization member accounts, if your account is an organization management account.</p> <p>To get the enrollment status of standalone accounts, use the <a>GetEnrollmentStatus</a> action.</p>

        Args:
            filters: <p>An array of objects to specify a filter that returns a more specific list of account enrollment statuses.</p>
            next_token: <p>The token to advance to the next page of account enrollment statuses.</p>
            max_results: <p>The maximum number of account enrollment statuses to return with a single request. You can specify up to 100 statuses to return with each request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_enrollment_statuses_for_organization_request.GetEnrollmentStatusesForOrganizationRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_enrollment_statuses_for_organization_response.GetEnrollmentStatusesForOrganizationResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_enrollment_statuses_for_organization

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_enrollment_statuses_for_organization.get_enrollment_statuses_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_enrollment_statuses_for_organization_request.GetEnrollmentStatusesForOrganizationRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_get_enrollment_statuses_for_organization(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        filters: Optional[
            "capo_compute_optimizer.types.enrollment_filters.EnrollmentFilters"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_compute_optimizer.types.account_enrollment_status.AccountEnrollmentStatus]":
        _token = next_token
        while True:
            _response = self.get_enrollment_statuses_for_organization(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("account_enrollment_statuses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_idle_recommendations(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        resource_arns: Optional[
            "capo_compute_optimizer.types.resource_arns.ResourceArns"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.idle_max_results.IdleMaxResults"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.idle_recommendation_filters.IdleRecommendationFilters"
        ] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        order_by: Optional["capo_compute_optimizer.types.order_by.OrderBy"] = None,
    ) -> "capo_compute_optimizer.types.get_idle_recommendations_response.GetIdleRecommendationsResponse":
        """<p>Returns idle resource recommendations. Compute Optimizer generates recommendations for idle resources that meet a specific set of requirements. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html">Resource requirements</a> in the <i>Compute Optimizer User Guide</i> </p>

        Args:
            resource_arns: <p>The ARN that identifies the idle resource.</p>
            next_token: <p>The token to advance to the next page of idle resource recommendations.</p>
            max_results: <p>The maximum number of idle resource recommendations to return with a single request. </p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>
            filters: <p>An array of objects to specify a filter that returns a more specific list of idle resource recommendations.</p>
            account_ids: <p>Return the idle resource recommendations to the specified Amazon Web Services account IDs.</p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to return the idle resource recommendations to specific member accounts.</p> <p>You can only specify one account ID per request.</p>
            order_by: <p>The order to sort the idle resource recommendations.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_idle_recommendations_request.GetIdleRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_idle_recommendations_response.GetIdleRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_idle_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_idle_recommendations.get_idle_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_idle_recommendations_request.GetIdleRecommendationsRequest = {}
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if order_by is not None:
            input_["order_by"] = order_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_lambda_function_recommendations(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        function_arns: Optional[
            "capo_compute_optimizer.types.function_arns.FunctionArns"
        ] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.lambda_function_recommendation_filters.LambdaFunctionRecommendationFilters"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_lambda_function_recommendations_response.GetLambdaFunctionRecommendationsResponse":
        """<p>Returns Lambda function recommendations.</p> <p>Compute Optimizer generates recommendations for functions that meet a specific set of requirements. For more information, see the <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html">Supported resources and requirements</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            function_arns: <p>The Amazon Resource Name (ARN) of the functions for which to return recommendations.</p> <p>You can specify a qualified or unqualified ARN. If you specify an unqualified ARN without a function version suffix, Compute Optimizer will return recommendations for the latest (<code>$LATEST</code>) version of the function. If you specify a qualified ARN with a version suffix, Compute Optimizer will return recommendations for the specified function version. For more information about using function versions, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html#versioning-versions-using">Using versions</a> in the <i>Lambda Developer Guide</i>.</p>
            account_ids: <p>The ID of the Amazon Web Services account for which to return function recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return function recommendations.</p> <p>Only one account ID can be specified per request.</p>
            filters: <p>An array of objects to specify a filter that returns a more specific list of function recommendations.</p>
            next_token: <p>The token to advance to the next page of function recommendations.</p>
            max_results: <p>The maximum number of function recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a limit of the service.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_lambda_function_recommendations_request.GetLambdaFunctionRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_lambda_function_recommendations_response.GetLambdaFunctionRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_lambda_function_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_lambda_function_recommendations.get_lambda_function_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_lambda_function_recommendations_request.GetLambdaFunctionRecommendationsRequest = {}
        if function_arns is not None:
            input_["function_arns"] = function_arns
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if filters is not None:
            input_["filters"] = filters
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

    def iter_get_lambda_function_recommendations(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        function_arns: Optional[
            "capo_compute_optimizer.types.function_arns.FunctionArns"
        ] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.lambda_function_recommendation_filters.LambdaFunctionRecommendationFilters"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_compute_optimizer.types.lambda_function_recommendation.LambdaFunctionRecommendation]":
        _token = next_token
        while True:
            _response = self.get_lambda_function_recommendations(
                config_overrides=config_overrides,
                function_arns=function_arns,
                account_ids=account_ids,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("lambda_function_recommendations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_license_recommendations(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        resource_arns: Optional[
            "capo_compute_optimizer.types.resource_arns.ResourceArns"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.license_recommendation_filters.LicenseRecommendationFilters"
        ] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_license_recommendations_response.GetLicenseRecommendationsResponse":
        """<p>Returns license recommendations for Amazon EC2 instances that run on a specific license.</p> <p>Compute Optimizer generates recommendations for licenses that meet a specific set of requirements. For more information, see the <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html">Supported resources and requirements</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            resource_arns: <p> The ARN that identifies the Amazon EC2 instance. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:ec2:region:aws_account_id:instance/instance-id</code> </p>
            next_token: <p> The token to advance to the next page of license recommendations. </p>
            max_results: <p> The maximum number of license recommendations to return with a single request. </p> <p> To retrieve the remaining results, make another request with the returned <code>nextToken</code> value. </p>
            filters: <p> An array of objects to specify a filter that returns a more specific list of license recommendations. </p>
            account_ids: <p>The ID of the Amazon Web Services account for which to return license recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return license recommendations.</p> <p>Only one account ID can be specified per request.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_license_recommendations_request.GetLicenseRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_license_recommendations_response.GetLicenseRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_license_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_license_recommendations.get_license_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_license_recommendations_request.GetLicenseRecommendationsRequest = {}
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_rds_database_recommendation_projected_metrics(
        self,
        resource_arn: "capo_compute_optimizer.types.resource_arn.ResourceArn",
        stat: "capo_compute_optimizer.types.metric_statistic.MetricStatistic",
        period: "capo_compute_optimizer.types.period.Period",
        start_time: "capo_compute_optimizer.types.timestamp.Timestamp",
        end_time: "capo_compute_optimizer.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        recommendation_preferences: Optional[
            "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_rds_database_recommendation_projected_metrics_response.GetRDSDatabaseRecommendationProjectedMetricsResponse":
        """<p> Returns the projected metrics of Aurora and RDS database recommendations. </p>

        Args:
            resource_arn: <p> The ARN that identifies the Amazon Aurora or RDS database. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:rds:{region}:{accountId}:db:{resourceName}</code> </p>
            stat: <p> The statistic of the projected metrics. </p>
            period: <p> The granularity, in seconds, of the projected metrics data points. </p>
            start_time: <p> The timestamp of the first projected metrics data point to return. </p>
            end_time: <p> The timestamp of the last projected metrics data point to return. </p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_rds_database_recommendation_projected_metrics_request.GetRDSDatabaseRecommendationProjectedMetricsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_rds_database_recommendation_projected_metrics_response.GetRDSDatabaseRecommendationProjectedMetricsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_rds_database_recommendation_projected_metrics

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_rds_database_recommendation_projected_metrics.get_rds_database_recommendation_projected_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_rds_database_recommendation_projected_metrics_request.GetRDSDatabaseRecommendationProjectedMetricsRequest = {
            "resource_arn": resource_arn,
            "stat": stat,
            "period": period,
            "start_time": start_time,
            "end_time": end_time,
        }
        if recommendation_preferences is not None:
            input_["recommendation_preferences"] = recommendation_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_rds_database_recommendations(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        resource_arns: Optional[
            "capo_compute_optimizer.types.resource_arns.ResourceArns"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_compute_optimizer.types.rdsdb_recommendation_filters.RDSDBRecommendationFilters"
        ] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        recommendation_preferences: Optional[
            "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_rds_database_recommendations_response.GetRDSDatabaseRecommendationsResponse":
        """<p> Returns Amazon Aurora and RDS database recommendations. </p> <p>Compute Optimizer generates recommendations for Amazon Aurora and RDS databases that meet a specific set of requirements. For more information, see the <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html">Supported resources and requirements</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            resource_arns: <p> The ARN that identifies the Amazon Aurora or RDS database. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:rds:{region}:{accountId}:db:{resourceName}</code> </p> <p> The following is the format of a DB Cluster ARN: </p> <p> <code>arn:aws:rds:{region}:{accountId}:cluster:{resourceName}</code> </p>
            next_token: <p> The token to advance to the next page of Amazon Aurora and RDS database recommendations. </p>
            max_results: <p>The maximum number of Amazon Aurora and RDS database recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>
            filters: <p> An array of objects to specify a filter that returns a more specific list of Amazon Aurora and RDS database recommendations. </p>
            account_ids: <p> Return the Amazon Aurora and RDS database recommendations to the specified Amazon Web Services account IDs. </p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to return the Amazon Aurora and RDS database recommendations to specific member accounts.</p> <p>You can only specify one account ID per request.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_rds_database_recommendations_request.GetRDSDatabaseRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_rds_database_recommendations_response.GetRDSDatabaseRecommendationsResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_rds_database_recommendations

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_rds_database_recommendations.get_rds_database_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_rds_database_recommendations_request.GetRDSDatabaseRecommendationsRequest = {}
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if recommendation_preferences is not None:
            input_["recommendation_preferences"] = recommendation_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommendation_preferences(
        self,
        resource_type: "capo_compute_optimizer.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        scope: Optional["capo_compute_optimizer.types.scope.Scope"] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_recommendation_preferences_response.GetRecommendationPreferencesResponse":
        """<p>Returns existing recommendation preferences, such as enhanced infrastructure metrics.</p> <p>Use the <code>scope</code> parameter to specify which preferences to return. You can specify to return preferences for an organization, a specific account ID, or a specific EC2 instance or Auto Scaling group Amazon Resource Name (ARN).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            resource_type: <p>The target resource type of the recommendation preference for which to return preferences.</p> <p>The <code>Ec2Instance</code> option encompasses standalone instances and instances that are part of Auto Scaling groups. The <code>AutoScalingGroup</code> option encompasses only instances that are part of an Auto Scaling group.</p>
            scope: <p>An object that describes the scope of the recommendation preference to return.</p> <p>You can return recommendation preferences that are created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>
            next_token: <p>The token to advance to the next page of recommendation preferences.</p>
            max_results: <p>The maximum number of recommendation preferences to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_recommendation_preferences_request.GetRecommendationPreferencesRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_recommendation_preferences_response.GetRecommendationPreferencesResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_recommendation_preferences

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_recommendation_preferences.get_recommendation_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_recommendation_preferences_request.GetRecommendationPreferencesRequest = {
            "resource_type": resource_type
        }
        if scope is not None:
            input_["scope"] = scope
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

    def iter_get_recommendation_preferences(
        self,
        resource_type: "capo_compute_optimizer.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        scope: Optional["capo_compute_optimizer.types.scope.Scope"] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_compute_optimizer.types.recommendation_preferences_detail.RecommendationPreferencesDetail]":
        _token = next_token
        while True:
            _response = self.get_recommendation_preferences(
                resource_type,
                config_overrides=config_overrides,
                scope=scope,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("recommendation_preferences_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_recommendation_summaries(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_compute_optimizer.types.get_recommendation_summaries_response.GetRecommendationSummariesResponse":
        """<p>Returns the optimization findings for an account.</p> <p>It returns the number of:</p> <ul> <li> <p>Amazon EC2 instances in an account that are <code>Underprovisioned</code>, <code>Overprovisioned</code>, or <code>Optimized</code>.</p> </li> <li> <p>EC2Auto Scaling groups in an account that are <code>NotOptimized</code>, or <code>Optimized</code>.</p> </li> <li> <p>Amazon EBS volumes in an account that are <code>NotOptimized</code>, or <code>Optimized</code>.</p> </li> <li> <p>Lambda functions in an account that are <code>NotOptimized</code>, or <code>Optimized</code>.</p> </li> <li> <p>Amazon ECS services in an account that are <code>Underprovisioned</code>, <code>Overprovisioned</code>, or <code>Optimized</code>.</p> </li> <li> <p>Commercial software licenses in an account that are <code>InsufficientMetrics</code>, <code>NotOptimized</code> or <code>Optimized</code>.</p> </li> <li> <p>Amazon Aurora and Amazon RDS databases in an account that are <code>Underprovisioned</code>, <code>Overprovisioned</code>, <code>Optimized</code>, or <code>NotOptimized</code>.</p> </li> </ul>

        Args:
            account_ids: <p>The ID of the Amazon Web Services account for which to return recommendation summaries.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return recommendation summaries.</p> <p>Only one account ID can be specified per request.</p>
            next_token: <p>The token to advance to the next page of recommendation summaries.</p>
            max_results: <p>The maximum number of recommendation summaries to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.get_recommendation_summaries_request.GetRecommendationSummariesRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.get_recommendation_summaries_response.GetRecommendationSummariesResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.get_recommendation_summaries

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.get_recommendation_summaries.get_recommendation_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.get_recommendation_summaries_request.GetRecommendationSummariesRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids
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

    def iter_get_recommendation_summaries(
        self,
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        account_ids: Optional[
            "capo_compute_optimizer.types.account_ids.AccountIds"
        ] = None,
        next_token: Optional[
            "capo_compute_optimizer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_compute_optimizer.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_compute_optimizer.types.recommendation_summary.RecommendationSummary]":
        _token = next_token
        while True:
            _response = self.get_recommendation_summaries(
                config_overrides=config_overrides,
                account_ids=account_ids,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("recommendation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_recommendation_preferences(
        self,
        resource_type: "capo_compute_optimizer.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        scope: Optional["capo_compute_optimizer.types.scope.Scope"] = None,
        enhanced_infrastructure_metrics: Optional[
            "capo_compute_optimizer.types.enhanced_infrastructure_metrics.EnhancedInfrastructureMetrics"
        ] = None,
        inferred_workload_types: Optional[
            "capo_compute_optimizer.types.inferred_workload_types_preference.InferredWorkloadTypesPreference"
        ] = None,
        external_metrics_preference: Optional[
            "capo_compute_optimizer.types.external_metrics_preference.ExternalMetricsPreference"
        ] = None,
        look_back_period: Optional[
            "capo_compute_optimizer.types.look_back_period_preference.LookBackPeriodPreference"
        ] = None,
        utilization_preferences: Optional[
            "capo_compute_optimizer.types.utilization_preferences.UtilizationPreferences"
        ] = None,
        preferred_resources: Optional[
            "capo_compute_optimizer.types.preferred_resources.PreferredResources"
        ] = None,
        savings_estimation_mode: Optional[
            "capo_compute_optimizer.types.savings_estimation_mode.SavingsEstimationMode"
        ] = None,
    ) -> "capo_compute_optimizer.types.put_recommendation_preferences_response.PutRecommendationPreferencesResponse":
        """<p>Creates a new recommendation preference or updates an existing recommendation preference, such as enhanced infrastructure metrics.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            resource_type: <p>The target resource type of the recommendation preference to create.</p> <p>The <code>Ec2Instance</code> option encompasses standalone instances and instances that are part of Auto Scaling groups. The <code>AutoScalingGroup</code> option encompasses only instances that are part of an Auto Scaling group.</p>
            scope: <p>An object that describes the scope of the recommendation preference to create.</p> <p>You can create recommendation preferences at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p> <note> <p>You cannot create recommendation preferences for Auto Scaling groups at the organization and account levels. You can create recommendation preferences for Auto Scaling groups only at the resource level by specifying a scope name of <code>ResourceArn</code> and a scope value of the Auto Scaling group Amazon Resource Name (ARN). This will configure the preference for all instances that are part of the specified Auto Scaling group. You also cannot create recommendation preferences at the resource level for instances that are part of an Auto Scaling group. You can create recommendation preferences at the resource level only for standalone instances.</p> </note>
            enhanced_infrastructure_metrics: <p>The status of the enhanced infrastructure metrics recommendation preference to create or update.</p> <p>Specify the <code>Active</code> status to activate the preference, or specify <code>Inactive</code> to deactivate the preference.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>
            inferred_workload_types: <p>The status of the inferred workload types recommendation preference to create or update.</p> <note> <p>The inferred workload type feature is active by default. To deactivate it, create a recommendation preference.</p> </note> <p>Specify the <code>Inactive</code> status to deactivate the feature, or specify <code>Active</code> to activate it.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/inferred-workload-types.html">Inferred workload types</a> in the <i>Compute Optimizer User Guide</i>.</p>
            external_metrics_preference: <p>The provider of the external metrics recommendation preference to create or update.</p> <p>Specify a valid provider in the <code>source</code> field to activate the preference. To delete this preference, see the <a>DeleteRecommendationPreferences</a> action.</p> <p>This preference can only be set for the <code>Ec2Instance</code> resource type.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html">External metrics ingestion</a> in the <i>Compute Optimizer User Guide</i>.</p>
            look_back_period: <p> The preference to control the number of days the utilization metrics of the Amazon Web Services resource are analyzed. When this preference isn't specified, we use the default value <code>DAYS_14</code>. </p> <p>You can only set this preference for the Amazon EC2 instance, Auto Scaling group, Amazon EBS volume, Amazon ECS service on Fargate, Amazon RDS DB instance, and Aurora DB cluster storage resource types. </p> <note> <ul> <li> <p>Lookback period preferences for Amazon EC2 instances, Amazon EBS volumes, Amazon ECS services, Amazon RDS DB instances, and Aurora DB cluster storage resource types can be set at the organization, account, and resource levels.</p> </li> <li> <p>Auto Scaling group lookback preferences can only be set at the resource level.</p> </li> <li> <p>Amazon EBS volume lookback preferences can be set at the organization, account, and resource levels.</p> </li> <li> <p>Amazon ECS service on Fargate lookback preferences can be set at the organization, account, and resource levels.</p> </li> <li> <p>Amazon RDS DB instance lookback preferences can be set at the organization, account, and resource levels.</p> </li> <li> <p>Aurora DB cluster storage lookback preferences can be set at the organization, account, and resource levels.</p> </li> <li> <p>Changing the lookback period for Amazon EBS volumes to 14 days does not affect the 32-day lookback period used to determine whether an Amazon EBS volume is unattached.</p> </li> </ul> </note>
            utilization_preferences: <p> The preference to control the resource’s CPU utilization threshold, CPU utilization headroom, and memory utilization headroom. When this preference isn't specified, we use the following default values. </p> <p>CPU utilization:</p> <ul> <li> <p> <code>P99_5</code> for threshold</p> </li> <li> <p> <code>PERCENT_20</code> for headroom</p> </li> </ul> <p>Memory utilization:</p> <ul> <li> <p> <code>PERCENT_20</code> for headroom</p> </li> </ul> <note> <ul> <li> <p>You can only set CPU and memory utilization preferences for the Amazon EC2 instance resource type.</p> </li> <li> <p>The threshold setting isn’t available for memory utilization.</p> </li> </ul> </note>
            preferred_resources: <p> The preference to control which resource type values are considered when generating rightsizing recommendations. You can specify this preference as a combination of include and exclude lists. You must specify either an <code>includeList</code> or <code>excludeList</code>. If the preference is an empty set of resource type values, an error occurs. </p> <note> <p>You can only set this preference for the Amazon EC2 instance, Auto Scaling group, Amazon EBS volume, Amazon ECS service, Amazon RDS DB instance, and Aurora DB cluster storage resource types.</p> </note>
            savings_estimation_mode: <p> The status of the savings estimation mode preference to create or update. </p> <p>Specify the <code>AfterDiscounts</code> status to activate the preference, or specify <code>BeforeDiscounts</code> to deactivate the preference.</p> <p>Only the account manager or delegated administrator of your organization can activate this preference.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode.html"> Savings estimation mode</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException: <p>The account is not opted in to Compute Optimizer.</p>
            capo_compute_optimizer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.put_recommendation_preferences_request.PutRecommendationPreferencesRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.put_recommendation_preferences_response.PutRecommendationPreferencesResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.put_recommendation_preferences

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.put_recommendation_preferences.put_recommendation_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.put_recommendation_preferences_request.PutRecommendationPreferencesRequest = {
            "resource_type": resource_type
        }
        if scope is not None:
            input_["scope"] = scope
        if enhanced_infrastructure_metrics is not None:
            input_["enhanced_infrastructure_metrics"] = enhanced_infrastructure_metrics
        if inferred_workload_types is not None:
            input_["inferred_workload_types"] = inferred_workload_types
        if external_metrics_preference is not None:
            input_["external_metrics_preference"] = external_metrics_preference
        if look_back_period is not None:
            input_["look_back_period"] = look_back_period
        if utilization_preferences is not None:
            input_["utilization_preferences"] = utilization_preferences
        if preferred_resources is not None:
            input_["preferred_resources"] = preferred_resources
        if savings_estimation_mode is not None:
            input_["savings_estimation_mode"] = savings_estimation_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_enrollment_status(
        self,
        status: "capo_compute_optimizer.types.status.Status",
        *,
        config_overrides: Optional[ComputeOptimizerClientConfig] = None,
        include_member_accounts: Optional[
            "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
        ] = None,
    ) -> "capo_compute_optimizer.types.update_enrollment_status_response.UpdateEnrollmentStatusResponse":
        """<p>Updates the enrollment (opt in and opt out) status of an account to the Compute Optimizer service.</p> <p>If the account is a management account of an organization, this action can also be used to enroll member accounts of the organization.</p> <p>You must have the appropriate permissions to opt in to Compute Optimizer, to view its recommendations, and to opt out. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html">Controlling access with Amazon Web Services Identity and Access Management</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>When you opt in, Compute Optimizer automatically creates a service-linked role in your account to access its data. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/using-service-linked-roles.html">Using Service-Linked Roles for Compute Optimizer</a> in the <i>Compute Optimizer User Guide</i>.</p>

        Args:
            status: <p>The new enrollment status of the account.</p> <p>The following status options are available:</p> <ul> <li> <p> <code>Active</code> - Opts in your account to the Compute Optimizer service. Compute Optimizer begins analyzing the configuration and utilization metrics of your Amazon Web Services resources after you opt in. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html">Metrics analyzed by Compute Optimizer</a> in the <i>Compute Optimizer User Guide</i>.</p> </li> <li> <p> <code>Inactive</code> - Opts out your account from the Compute Optimizer service. Your account's recommendations and related metrics data will be deleted from Compute Optimizer after you opt out.</p> </li> </ul> <note> <p>The <code>Pending</code> and <code>Failed</code> options cannot be used to update the enrollment status of an account. They are returned in the response of a request to update the enrollment status of an account.</p> </note>
            include_member_accounts: <p>Indicates whether to enroll member accounts of the organization if the account is the management account of an organization.</p>

        Raises:
            capo_compute_optimizer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_compute_optimizer.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Try your call again.</p>
            capo_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value supplied for the input parameter is out of range or not valid.</p>
            capo_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken: <p>The request must contain either a valid (registered) Amazon Web Services access key ID or X.509 certificate.</p>
            capo_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the server.</p>
            capo_compute_optimizer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_compute_optimizer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_compute_optimizer.types.update_enrollment_status_request.UpdateEnrollmentStatusRequest]",
        ) -> OperationResponse[
            "capo_compute_optimizer.types.update_enrollment_status_response.UpdateEnrollmentStatusResponse"
        ]:
            import capo_compute_optimizer._operations.compute_optimizer_service.update_enrollment_status

            output, http_response = (
                capo_compute_optimizer._operations.compute_optimizer_service.update_enrollment_status.update_enrollment_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_compute_optimizer.types.update_enrollment_status_request.UpdateEnrollmentStatusRequest = {
            "status": status
        }
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts

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
