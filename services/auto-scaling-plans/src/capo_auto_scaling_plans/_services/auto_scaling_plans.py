"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#AnyScaleScalingPlannerFrontendService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_auto_scaling_plans._auth._signers
import capo_auto_scaling_plans._auth._sigv4
from capo_auto_scaling_plans._auth._identity import Credentials
from capo_auto_scaling_plans._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_auto_scaling_plans._auth._zapros_handler import AuthMiddleware
from capo_auto_scaling_plans._services._aws_config import aws_config
from capo_auto_scaling_plans._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.application_source
    import capo_auto_scaling_plans.types.application_sources
    import capo_auto_scaling_plans.types.create_scaling_plan_request
    import capo_auto_scaling_plans.types.create_scaling_plan_response
    import capo_auto_scaling_plans.types.delete_scaling_plan_request
    import capo_auto_scaling_plans.types.delete_scaling_plan_response
    import capo_auto_scaling_plans.types.describe_scaling_plan_resources_request
    import capo_auto_scaling_plans.types.describe_scaling_plan_resources_response
    import capo_auto_scaling_plans.types.describe_scaling_plans_request
    import capo_auto_scaling_plans.types.describe_scaling_plans_response
    import capo_auto_scaling_plans.types.forecast_data_type
    import capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request
    import capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response
    import capo_auto_scaling_plans.types.max_results
    import capo_auto_scaling_plans.types.next_token
    import capo_auto_scaling_plans.types.scalable_dimension
    import capo_auto_scaling_plans.types.scaling_instructions
    import capo_auto_scaling_plans.types.scaling_plan_name
    import capo_auto_scaling_plans.types.scaling_plan_names
    import capo_auto_scaling_plans.types.scaling_plan_version
    import capo_auto_scaling_plans.types.service_namespace
    import capo_auto_scaling_plans.types.timestamp_type
    import capo_auto_scaling_plans.types.update_scaling_plan_request
    import capo_auto_scaling_plans.types.update_scaling_plan_response
    import capo_auto_scaling_plans.types.xml_string


class AutoScalingPlansClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AutoScalingPlansClient:
    """A client for the ``AutoScalingPlans`` service.

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
        self._config = AutoScalingPlansClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AutoScalingPlansClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AutoScalingPlansClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def create_scaling_plan(
        self,
        scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        application_source: "capo_auto_scaling_plans.types.application_source.ApplicationSource",
        scaling_instructions: "capo_auto_scaling_plans.types.scaling_instructions.ScalingInstructions",
        *,
        config_overrides: Optional[AutoScalingPlansClientConfig] = None,
    ) -> "capo_auto_scaling_plans.types.create_scaling_plan_response.CreateScalingPlanResponse":
        """<p>Creates a scaling plan. </p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan. Names cannot contain vertical bars, colons, or forward slashes.</p>
            application_source: <p>A CloudFormation stack or set of tags. You can create one scaling plan per application source.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ApplicationSource.html">ApplicationSource</a> in the <i>AWS Auto Scaling API Reference</i>.</p>
            scaling_instructions: <p>The scaling instructions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingInstruction.html">ScalingInstruction</a> in the <i>AWS Auto Scaling API Reference</i>.</p>

        Raises:
            capo_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            capo_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_auto_scaling_plans.errors.limit_exceeded_exception.LimitExceededException: <p>Your account exceeded a limit. This exception is thrown when a per-account resource limit is exceeded.</p>
            capo_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            capo_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling_plans.types.create_scaling_plan_request.CreateScalingPlanRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling_plans.types.create_scaling_plan_response.CreateScalingPlanResponse"
        ]:
            import capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.create_scaling_plan

            output, http_response = (
                capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.create_scaling_plan.create_scaling_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling_plans.types.create_scaling_plan_request.CreateScalingPlanRequest = {
            "scaling_plan_name": scaling_plan_name,
            "application_source": application_source,
            "scaling_instructions": scaling_instructions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_scaling_plan(
        self,
        scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        scaling_plan_version: "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion",
        *,
        config_overrides: Optional[AutoScalingPlansClientConfig] = None,
    ) -> "capo_auto_scaling_plans.types.delete_scaling_plan_response.DeleteScalingPlanResponse":
        """<p>Deletes the specified scaling plan.</p> <p>Deleting a scaling plan deletes the underlying <a>ScalingInstruction</a> for all of the scalable resources that are covered by the plan.</p> <p>If the plan has launched resources or has scaling activities in progress, you must delete those resources separately.</p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan.</p>
            scaling_plan_version: <p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>

        Raises:
            capo_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            capo_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_auto_scaling_plans.errors.object_not_found_exception.ObjectNotFoundException: <p>The specified object could not be found.</p>
            capo_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            capo_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling_plans.types.delete_scaling_plan_request.DeleteScalingPlanRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling_plans.types.delete_scaling_plan_response.DeleteScalingPlanResponse"
        ]:
            import capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.delete_scaling_plan

            output, http_response = (
                capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.delete_scaling_plan.delete_scaling_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling_plans.types.delete_scaling_plan_request.DeleteScalingPlanRequest = {
            "scaling_plan_name": scaling_plan_name,
            "scaling_plan_version": scaling_plan_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_scaling_plan_resources(
        self,
        scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        scaling_plan_version: "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion",
        *,
        config_overrides: Optional[AutoScalingPlansClientConfig] = None,
        max_results: Optional[
            "capo_auto_scaling_plans.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_auto_scaling_plans.types.next_token.NextToken"
        ] = None,
    ) -> "capo_auto_scaling_plans.types.describe_scaling_plan_resources_response.DescribeScalingPlanResourcesResponse":
        """<p>Describes the scalable resources in the specified scaling plan.</p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan.</p>
            scaling_plan_version: <p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>
            max_results: <p>The maximum number of scalable resources to return. The value must be between 1 and 50. The default value is 50.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            capo_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_auto_scaling_plans.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token provided is not valid.</p>
            capo_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            capo_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling_plans.types.describe_scaling_plan_resources_request.DescribeScalingPlanResourcesRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling_plans.types.describe_scaling_plan_resources_response.DescribeScalingPlanResourcesResponse"
        ]:
            import capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.describe_scaling_plan_resources

            output, http_response = (
                capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.describe_scaling_plan_resources.describe_scaling_plan_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling_plans.types.describe_scaling_plan_resources_request.DescribeScalingPlanResourcesRequest = {
            "scaling_plan_name": scaling_plan_name,
            "scaling_plan_version": scaling_plan_version,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_scaling_plans(
        self,
        *,
        config_overrides: Optional[AutoScalingPlansClientConfig] = None,
        scaling_plan_names: Optional[
            "capo_auto_scaling_plans.types.scaling_plan_names.ScalingPlanNames"
        ] = None,
        scaling_plan_version: Optional[
            "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
        ] = None,
        application_sources: Optional[
            "capo_auto_scaling_plans.types.application_sources.ApplicationSources"
        ] = None,
        max_results: Optional[
            "capo_auto_scaling_plans.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_auto_scaling_plans.types.next_token.NextToken"
        ] = None,
    ) -> "capo_auto_scaling_plans.types.describe_scaling_plans_response.DescribeScalingPlansResponse":
        """<p>Describes one or more of your scaling plans.</p>

        Args:
            scaling_plan_names: <p>The names of the scaling plans (up to 10). If you specify application sources, you cannot specify scaling plan names.</p>
            scaling_plan_version: <p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p> <note> <p>If you specify a scaling plan version, you must also specify a scaling plan name.</p> </note>
            application_sources: <p>The sources for the applications (up to 10). If you specify scaling plan names, you cannot specify application sources.</p>
            max_results: <p>The maximum number of scalable resources to return. This value can be between 1 and 50. The default value is 50.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            capo_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_auto_scaling_plans.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token provided is not valid.</p>
            capo_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            capo_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling_plans.types.describe_scaling_plans_request.DescribeScalingPlansRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling_plans.types.describe_scaling_plans_response.DescribeScalingPlansResponse"
        ]:
            import capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.describe_scaling_plans

            output, http_response = (
                capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.describe_scaling_plans.describe_scaling_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling_plans.types.describe_scaling_plans_request.DescribeScalingPlansRequest = {}
        if scaling_plan_names is not None:
            input_["scaling_plan_names"] = scaling_plan_names
        if scaling_plan_version is not None:
            input_["scaling_plan_version"] = scaling_plan_version
        if application_sources is not None:
            input_["application_sources"] = application_sources
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_scaling_plan_resource_forecast_data(
        self,
        scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        scaling_plan_version: "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion",
        service_namespace: "capo_auto_scaling_plans.types.service_namespace.ServiceNamespace",
        resource_id: "capo_auto_scaling_plans.types.xml_string.XmlString",
        scalable_dimension: "capo_auto_scaling_plans.types.scalable_dimension.ScalableDimension",
        forecast_data_type: "capo_auto_scaling_plans.types.forecast_data_type.ForecastDataType",
        start_time: "capo_auto_scaling_plans.types.timestamp_type.TimestampType",
        end_time: "capo_auto_scaling_plans.types.timestamp_type.TimestampType",
        *,
        config_overrides: Optional[AutoScalingPlansClientConfig] = None,
    ) -> "capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse":
        """<p>Retrieves the forecast data for a scalable resource.</p> <p>Capacity forecasts are represented as predicted values, or data points, that are calculated using historical data points from a specified CloudWatch load metric. Data points are available for up to 56 days. </p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan.</p>
            scaling_plan_version: <p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>
            service_namespace: <p>The namespace of the AWS service. The only valid value is <code>autoscaling</code>. </p>
            resource_id: <p>The ID of the resource. This string consists of a prefix (<code>autoScalingGroup</code>) followed by the name of a specified Auto Scaling group (<code>my-asg</code>). Example: <code>autoScalingGroup/my-asg</code>. </p>
            scalable_dimension: <p>The scalable dimension for the resource. The only valid value is <code>autoscaling:autoScalingGroup:DesiredCapacity</code>. </p>
            forecast_data_type: <p>The type of forecast data to get.</p> <ul> <li> <p> <code>LoadForecast</code>: The load metric forecast. </p> </li> <li> <p> <code>CapacityForecast</code>: The capacity forecast. </p> </li> <li> <p> <code>ScheduledActionMinCapacity</code>: The minimum capacity for each scheduled scaling action. This data is calculated as the larger of two values: the capacity forecast or the minimum capacity in the scaling instruction.</p> </li> <li> <p> <code>ScheduledActionMaxCapacity</code>: The maximum capacity for each scheduled scaling action. The calculation used is determined by the predictive scaling maximum capacity behavior setting in the scaling instruction.</p> </li> </ul>
            start_time: <p>The inclusive start time of the time range for the forecast data to get. The date and time can be at most 56 days before the current date and time. </p>
            end_time: <p>The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is seven days. </p> <p>Although this parameter can accept a date and time that is more than two days in the future, the availability of forecast data has limits. AWS Auto Scaling only issues forecasts for periods of two days in advance.</p>

        Raises:
            capo_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            capo_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request.GetScalingPlanResourceForecastDataRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse"
        ]:
            import capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.get_scaling_plan_resource_forecast_data

            output, http_response = (
                capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.get_scaling_plan_resource_forecast_data.get_scaling_plan_resource_forecast_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request.GetScalingPlanResourceForecastDataRequest = {
            "scaling_plan_name": scaling_plan_name,
            "scaling_plan_version": scaling_plan_version,
            "service_namespace": service_namespace,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "forecast_data_type": forecast_data_type,
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

    def update_scaling_plan(
        self,
        scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        scaling_plan_version: "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion",
        *,
        config_overrides: Optional[AutoScalingPlansClientConfig] = None,
        application_source: Optional[
            "capo_auto_scaling_plans.types.application_source.ApplicationSource"
        ] = None,
        scaling_instructions: Optional[
            "capo_auto_scaling_plans.types.scaling_instructions.ScalingInstructions"
        ] = None,
    ) -> "capo_auto_scaling_plans.types.update_scaling_plan_response.UpdateScalingPlanResponse":
        """<p>Updates the specified scaling plan.</p> <p>You cannot update a scaling plan if it is in the process of being created, updated, or deleted.</p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan.</p>
            scaling_plan_version: <p>The version number of the scaling plan. The only valid value is <code>1</code>. Currently, you cannot have multiple scaling plan versions.</p>
            application_source: <p>A CloudFormation stack or set of tags.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ApplicationSource.html">ApplicationSource</a> in the <i>AWS Auto Scaling API Reference</i>.</p>
            scaling_instructions: <p>The scaling instructions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingInstruction.html">ScalingInstruction</a> in the <i>AWS Auto Scaling API Reference</i>.</p>

        Raises:
            capo_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            capo_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_auto_scaling_plans.errors.object_not_found_exception.ObjectNotFoundException: <p>The specified object could not be found.</p>
            capo_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            capo_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling_plans.types.update_scaling_plan_request.UpdateScalingPlanRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling_plans.types.update_scaling_plan_response.UpdateScalingPlanResponse"
        ]:
            import capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.update_scaling_plan

            output, http_response = (
                capo_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.update_scaling_plan.update_scaling_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling_plans.types.update_scaling_plan_request.UpdateScalingPlanRequest = {
            "scaling_plan_name": scaling_plan_name,
            "scaling_plan_version": scaling_plan_version,
        }
        if application_source is not None:
            input_["application_source"] = application_source
        if scaling_instructions is not None:
            input_["scaling_instructions"] = scaling_instructions

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
