"""Generated from Smithy shape ``com.amazonaws.iotevents#IotColumboService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_iot_events._auth._signers
import capo_iot_events._auth._sigv4
from capo_iot_events._auth._identity import Credentials
from capo_iot_events._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iot_events._auth._zapros_handler import AuthMiddleware
from capo_iot_events._services._aws_config import aaws_config
from capo_iot_events._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_iot_events.types.alarm_capabilities
    import capo_iot_events.types.alarm_event_actions
    import capo_iot_events.types.alarm_model_description
    import capo_iot_events.types.alarm_model_name
    import capo_iot_events.types.alarm_model_version
    import capo_iot_events.types.alarm_notification
    import capo_iot_events.types.alarm_rule
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.analysis_id
    import capo_iot_events.types.attribute_json_path
    import capo_iot_events.types.create_alarm_model_request
    import capo_iot_events.types.create_alarm_model_response
    import capo_iot_events.types.create_detector_model_request
    import capo_iot_events.types.create_detector_model_response
    import capo_iot_events.types.create_input_request
    import capo_iot_events.types.create_input_response
    import capo_iot_events.types.delete_alarm_model_request
    import capo_iot_events.types.delete_alarm_model_response
    import capo_iot_events.types.delete_detector_model_request
    import capo_iot_events.types.delete_detector_model_response
    import capo_iot_events.types.delete_input_request
    import capo_iot_events.types.delete_input_response
    import capo_iot_events.types.describe_alarm_model_request
    import capo_iot_events.types.describe_alarm_model_response
    import capo_iot_events.types.describe_detector_model_analysis_request
    import capo_iot_events.types.describe_detector_model_analysis_response
    import capo_iot_events.types.describe_detector_model_request
    import capo_iot_events.types.describe_detector_model_response
    import capo_iot_events.types.describe_input_request
    import capo_iot_events.types.describe_input_response
    import capo_iot_events.types.describe_logging_options_request
    import capo_iot_events.types.describe_logging_options_response
    import capo_iot_events.types.detector_model_definition
    import capo_iot_events.types.detector_model_description
    import capo_iot_events.types.detector_model_name
    import capo_iot_events.types.detector_model_version
    import capo_iot_events.types.evaluation_method
    import capo_iot_events.types.get_detector_model_analysis_results_request
    import capo_iot_events.types.get_detector_model_analysis_results_response
    import capo_iot_events.types.input_definition
    import capo_iot_events.types.input_description
    import capo_iot_events.types.input_identifier
    import capo_iot_events.types.input_name
    import capo_iot_events.types.list_alarm_model_versions_request
    import capo_iot_events.types.list_alarm_model_versions_response
    import capo_iot_events.types.list_alarm_models_request
    import capo_iot_events.types.list_alarm_models_response
    import capo_iot_events.types.list_detector_model_versions_request
    import capo_iot_events.types.list_detector_model_versions_response
    import capo_iot_events.types.list_detector_models_request
    import capo_iot_events.types.list_detector_models_response
    import capo_iot_events.types.list_input_routings_request
    import capo_iot_events.types.list_input_routings_response
    import capo_iot_events.types.list_inputs_request
    import capo_iot_events.types.list_inputs_response
    import capo_iot_events.types.list_tags_for_resource_request
    import capo_iot_events.types.list_tags_for_resource_response
    import capo_iot_events.types.logging_options
    import capo_iot_events.types.max_analysis_results
    import capo_iot_events.types.max_results
    import capo_iot_events.types.next_token
    import capo_iot_events.types.put_logging_options_request
    import capo_iot_events.types.severity
    import capo_iot_events.types.start_detector_model_analysis_request
    import capo_iot_events.types.start_detector_model_analysis_response
    import capo_iot_events.types.tag_keys
    import capo_iot_events.types.tag_resource_request
    import capo_iot_events.types.tag_resource_response
    import capo_iot_events.types.tags
    import capo_iot_events.types.untag_resource_request
    import capo_iot_events.types.untag_resource_response
    import capo_iot_events.types.update_alarm_model_request
    import capo_iot_events.types.update_alarm_model_response
    import capo_iot_events.types.update_detector_model_request
    import capo_iot_events.types.update_detector_model_response
    import capo_iot_events.types.update_input_request
    import capo_iot_events.types.update_input_response


class AsyncIoTEventsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncIoTEventsClient:
    """A client for the ``IoTEvents`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncIoTEventsClientConfig(
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
        self, config_overrides: Optional[AsyncIoTEventsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTEventsClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def create_alarm_model(
        self,
        alarm_model_name: "capo_iot_events.types.alarm_model_name.AlarmModelName",
        role_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName",
        alarm_rule: "capo_iot_events.types.alarm_rule.AlarmRule",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        alarm_model_description: Optional[
            "capo_iot_events.types.alarm_model_description.AlarmModelDescription"
        ] = None,
        tags: Optional["capo_iot_events.types.tags.Tags"] = None,
        key: Optional[
            "capo_iot_events.types.attribute_json_path.AttributeJsonPath"
        ] = None,
        severity: Optional["capo_iot_events.types.severity.Severity"] = None,
        alarm_notification: Optional[
            "capo_iot_events.types.alarm_notification.AlarmNotification"
        ] = None,
        alarm_event_actions: Optional[
            "capo_iot_events.types.alarm_event_actions.AlarmEventActions"
        ] = None,
        alarm_capabilities: Optional[
            "capo_iot_events.types.alarm_capabilities.AlarmCapabilities"
        ] = None,
    ) -> "capo_iot_events.types.create_alarm_model_response.CreateAlarmModelResponse":
        """<p>Creates an alarm model to monitor an AWS IoT Events input attribute. You can use the alarm to get notified when the value is outside a specified range. For more information, see <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/create-alarms.html">Create an alarm model</a> in the <i>AWS IoT Events Developer Guide</i>.</p>

        Args:
            alarm_model_name: <p>A unique name that helps you identify the alarm model. You can't change this name after you create the alarm model.</p>
            alarm_model_description: <p>A description that tells you what the alarm model detects.</p>
            role_arn: <p>The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>.</p>
            tags: <p>A list of key-value pairs that contain metadata for the alarm model. The tags help you manage the alarm model. For more information, see <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/tagging-iotevents.html">Tagging your AWS IoT Events resources</a> in the <i>AWS IoT Events Developer Guide</i>.</p> <p>You can create up to 50 tags for one alarm model.</p>
            key: <p>An input attribute used as a key to create an alarm. AWS IoT Events routes <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html">inputs</a> associated with this key to the alarm.</p>
            severity: <p>A non-negative integer that reflects the severity level of the alarm.</p>
            alarm_rule: <p>Defines when your alarm is invoked.</p>
            alarm_notification: <p>Contains information about one or more notification actions.</p>
            alarm_event_actions: <p>Contains information about one or more alarm actions.</p>
            alarm_capabilities: <p>Contains the configuration information of alarm state changes.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.limit_exceeded_exception.LimitExceededException: <p>A limit was exceeded.</p>
            capo_iot_events.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.create_alarm_model_request.CreateAlarmModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.create_alarm_model_response.CreateAlarmModelResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.create_alarm_model

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.create_alarm_model.async_create_alarm_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.create_alarm_model_request.CreateAlarmModelRequest = {
            "alarm_model_name": alarm_model_name,
            "role_arn": role_arn,
            "alarm_rule": alarm_rule,
        }
        if alarm_model_description is not None:
            input_["alarm_model_description"] = alarm_model_description
        if tags is not None:
            input_["tags"] = tags
        if key is not None:
            input_["key"] = key
        if severity is not None:
            input_["severity"] = severity
        if alarm_notification is not None:
            input_["alarm_notification"] = alarm_notification
        if alarm_event_actions is not None:
            input_["alarm_event_actions"] = alarm_event_actions
        if alarm_capabilities is not None:
            input_["alarm_capabilities"] = alarm_capabilities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_detector_model(
        self,
        detector_model_name: "capo_iot_events.types.detector_model_name.DetectorModelName",
        detector_model_definition: "capo_iot_events.types.detector_model_definition.DetectorModelDefinition",
        role_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        detector_model_description: Optional[
            "capo_iot_events.types.detector_model_description.DetectorModelDescription"
        ] = None,
        key: Optional[
            "capo_iot_events.types.attribute_json_path.AttributeJsonPath"
        ] = None,
        tags: Optional["capo_iot_events.types.tags.Tags"] = None,
        evaluation_method: Optional[
            "capo_iot_events.types.evaluation_method.EvaluationMethod"
        ] = None,
    ) -> "capo_iot_events.types.create_detector_model_response.CreateDetectorModelResponse":
        """<p>Creates a detector model.</p>

        Args:
            detector_model_name: <p>The name of the detector model.</p>
            detector_model_definition: <p>Information that defines how the detectors operate.</p>
            detector_model_description: <p>A brief description of the detector model.</p>
            key: <p>The input attribute key used to identify a device or system to create a detector (an instance of the detector model) and then to route each input received to the appropriate detector (instance). This parameter uses a JSON-path expression in the message payload of each input to specify the attribute-value pair that is used to identify the device associated with the input.</p>
            role_arn: <p>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</p>
            tags: <p>Metadata that can be used to manage the detector model.</p>
            evaluation_method: <p>Information about the order in which events are evaluated and how actions are executed. </p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.limit_exceeded_exception.LimitExceededException: <p>A limit was exceeded.</p>
            capo_iot_events.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.create_detector_model_request.CreateDetectorModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.create_detector_model_response.CreateDetectorModelResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.create_detector_model

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.create_detector_model.async_create_detector_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.create_detector_model_request.CreateDetectorModelRequest = {
            "detector_model_name": detector_model_name,
            "detector_model_definition": detector_model_definition,
            "role_arn": role_arn,
        }
        if detector_model_description is not None:
            input_["detector_model_description"] = detector_model_description
        if key is not None:
            input_["key"] = key
        if tags is not None:
            input_["tags"] = tags
        if evaluation_method is not None:
            input_["evaluation_method"] = evaluation_method

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_input(
        self,
        input_name: "capo_iot_events.types.input_name.InputName",
        input_definition: "capo_iot_events.types.input_definition.InputDefinition",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        input_description: Optional[
            "capo_iot_events.types.input_description.InputDescription"
        ] = None,
        tags: Optional["capo_iot_events.types.tags.Tags"] = None,
    ) -> "capo_iot_events.types.create_input_response.CreateInputResponse":
        """<p>Creates an input.</p>

        Args:
            input_name: <p>The name you want to give to the input.</p>
            input_description: <p>A brief description of the input.</p>
            input_definition: <p>The definition of the input.</p>
            tags: <p>Metadata that can be used to manage the input.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.create_input_request.CreateInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.create_input_response.CreateInputResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.create_input

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.create_input.async_create_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.create_input_request.CreateInputRequest = {
            "input_name": input_name,
            "input_definition": input_definition,
        }
        if input_description is not None:
            input_["input_description"] = input_description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_alarm_model(
        self,
        alarm_model_name: "capo_iot_events.types.alarm_model_name.AlarmModelName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> "capo_iot_events.types.delete_alarm_model_response.DeleteAlarmModelResponse":
        """<p>Deletes an alarm model. Any alarm instances that were created based on this alarm model are also deleted. This action can't be undone.</p>

        Args:
            alarm_model_name: <p>The name of the alarm model.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.delete_alarm_model_request.DeleteAlarmModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.delete_alarm_model_response.DeleteAlarmModelResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.delete_alarm_model

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.delete_alarm_model.async_delete_alarm_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.delete_alarm_model_request.DeleteAlarmModelRequest = {
            "alarm_model_name": alarm_model_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_detector_model(
        self,
        detector_model_name: "capo_iot_events.types.detector_model_name.DetectorModelName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> "capo_iot_events.types.delete_detector_model_response.DeleteDetectorModelResponse":
        """<p>Deletes a detector model. Any active instances of the detector model are also deleted.</p>

        Args:
            detector_model_name: <p>The name of the detector model to be deleted.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.delete_detector_model_request.DeleteDetectorModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.delete_detector_model_response.DeleteDetectorModelResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.delete_detector_model

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.delete_detector_model.async_delete_detector_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.delete_detector_model_request.DeleteDetectorModelRequest = {
            "detector_model_name": detector_model_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_input(
        self,
        input_name: "capo_iot_events.types.input_name.InputName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> "capo_iot_events.types.delete_input_response.DeleteInputResponse":
        """<p>Deletes an input.</p>

        Args:
            input_name: <p>The name of the input to delete.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.delete_input_request.DeleteInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.delete_input_response.DeleteInputResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.delete_input

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.delete_input.async_delete_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.delete_input_request.DeleteInputRequest = {
            "input_name": input_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_alarm_model(
        self,
        alarm_model_name: "capo_iot_events.types.alarm_model_name.AlarmModelName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        alarm_model_version: Optional[
            "capo_iot_events.types.alarm_model_version.AlarmModelVersion"
        ] = None,
    ) -> (
        "capo_iot_events.types.describe_alarm_model_response.DescribeAlarmModelResponse"
    ):
        """<p>Retrieves information about an alarm model. If you don't specify a value for the <code>alarmModelVersion</code> parameter, the latest version is returned.</p>

        Args:
            alarm_model_name: <p>The name of the alarm model.</p>
            alarm_model_version: <p>The version of the alarm model.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.describe_alarm_model_request.DescribeAlarmModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.describe_alarm_model_response.DescribeAlarmModelResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.describe_alarm_model

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.describe_alarm_model.async_describe_alarm_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.describe_alarm_model_request.DescribeAlarmModelRequest = {
            "alarm_model_name": alarm_model_name
        }
        if alarm_model_version is not None:
            input_["alarm_model_version"] = alarm_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_detector_model(
        self,
        detector_model_name: "capo_iot_events.types.detector_model_name.DetectorModelName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        detector_model_version: Optional[
            "capo_iot_events.types.detector_model_version.DetectorModelVersion"
        ] = None,
    ) -> "capo_iot_events.types.describe_detector_model_response.DescribeDetectorModelResponse":
        """<p>Describes a detector model. If the <code>version</code> parameter is not specified, information about the latest version is returned.</p>

        Args:
            detector_model_name: <p>The name of the detector model.</p>
            detector_model_version: <p>The version of the detector model.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.describe_detector_model_request.DescribeDetectorModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.describe_detector_model_response.DescribeDetectorModelResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.describe_detector_model

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.describe_detector_model.async_describe_detector_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.describe_detector_model_request.DescribeDetectorModelRequest = {
            "detector_model_name": detector_model_name
        }
        if detector_model_version is not None:
            input_["detector_model_version"] = detector_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_detector_model_analysis(
        self,
        analysis_id: "capo_iot_events.types.analysis_id.AnalysisId",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> "capo_iot_events.types.describe_detector_model_analysis_response.DescribeDetectorModelAnalysisResponse":
        """<p>Retrieves runtime information about a detector model analysis.</p> <note> <p>After AWS IoT Events starts analyzing your detector model, you have up to 24 hours to retrieve the analysis results.</p> </note>

        Args:
            analysis_id: <p>The ID of the analysis result that you want to retrieve.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.describe_detector_model_analysis_request.DescribeDetectorModelAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.describe_detector_model_analysis_response.DescribeDetectorModelAnalysisResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.describe_detector_model_analysis

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.describe_detector_model_analysis.async_describe_detector_model_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.describe_detector_model_analysis_request.DescribeDetectorModelAnalysisRequest = {
            "analysis_id": analysis_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_input(
        self,
        input_name: "capo_iot_events.types.input_name.InputName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> "capo_iot_events.types.describe_input_response.DescribeInputResponse":
        """<p>Describes an input.</p>

        Args:
            input_name: <p>The name of the input.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.describe_input_request.DescribeInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.describe_input_response.DescribeInputResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.describe_input

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.describe_input.async_describe_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.describe_input_request.DescribeInputRequest = {
            "input_name": input_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_logging_options(
        self, *, config_overrides: Optional[AsyncIoTEventsClientConfig] = None
    ) -> "capo_iot_events.types.describe_logging_options_response.DescribeLoggingOptionsResponse":
        """<p>Retrieves the current settings of the AWS IoT Events logging options.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The requested operation is not supported.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.describe_logging_options_request.DescribeLoggingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.describe_logging_options_response.DescribeLoggingOptionsResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.describe_logging_options

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.describe_logging_options.async_describe_logging_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.describe_logging_options_request.DescribeLoggingOptionsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_detector_model_analysis_results(
        self,
        analysis_id: "capo_iot_events.types.analysis_id.AnalysisId",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        next_token: Optional["capo_iot_events.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iot_events.types.max_analysis_results.MaxAnalysisResults"
        ] = None,
    ) -> "capo_iot_events.types.get_detector_model_analysis_results_response.GetDetectorModelAnalysisResultsResponse":
        """<p>Retrieves one or more analysis results of the detector model.</p> <note> <p>After AWS IoT Events starts analyzing your detector model, you have up to 24 hours to retrieve the analysis results.</p> </note>

        Args:
            analysis_id: <p>The ID of the analysis result that you want to retrieve.</p>
            next_token: <p>The token that you can use to return the next set of results.</p>
            max_results: <p>The maximum number of results to be returned per request.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.get_detector_model_analysis_results_request.GetDetectorModelAnalysisResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.get_detector_model_analysis_results_response.GetDetectorModelAnalysisResultsResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.get_detector_model_analysis_results

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.get_detector_model_analysis_results.async_get_detector_model_analysis_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.get_detector_model_analysis_results_request.GetDetectorModelAnalysisResultsRequest = {
            "analysis_id": analysis_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_alarm_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        next_token: Optional["capo_iot_events.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_events.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_events.types.list_alarm_models_response.ListAlarmModelsResponse":
        """<p>Lists the alarm models that you created. The operation returns only the metadata associated with each alarm model.</p>

        Args:
            next_token: <p>The token that you can use to return the next set of results.</p>
            max_results: <p>The maximum number of results to be returned per request.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.list_alarm_models_request.ListAlarmModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.list_alarm_models_response.ListAlarmModelsResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.list_alarm_models

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.list_alarm_models.async_list_alarm_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.list_alarm_models_request.ListAlarmModelsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_alarm_model_versions(
        self,
        alarm_model_name: "capo_iot_events.types.alarm_model_name.AlarmModelName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        next_token: Optional["capo_iot_events.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_events.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_events.types.list_alarm_model_versions_response.ListAlarmModelVersionsResponse":
        """<p>Lists all the versions of an alarm model. The operation returns only the metadata associated with each alarm model version.</p>

        Args:
            alarm_model_name: <p>The name of the alarm model.</p>
            next_token: <p>The token that you can use to return the next set of results.</p>
            max_results: <p>The maximum number of results to be returned per request.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.list_alarm_model_versions_request.ListAlarmModelVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.list_alarm_model_versions_response.ListAlarmModelVersionsResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.list_alarm_model_versions

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.list_alarm_model_versions.async_list_alarm_model_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.list_alarm_model_versions_request.ListAlarmModelVersionsRequest = {
            "alarm_model_name": alarm_model_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_detector_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        next_token: Optional["capo_iot_events.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_events.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_iot_events.types.list_detector_models_response.ListDetectorModelsResponse"
    ):
        """<p>Lists the detector models you have created. Only the metadata associated with each detector model is returned.</p>

        Args:
            next_token: <p>The token that you can use to return the next set of results.</p>
            max_results: <p>The maximum number of results to be returned per request.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.list_detector_models_request.ListDetectorModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.list_detector_models_response.ListDetectorModelsResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.list_detector_models

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.list_detector_models.async_list_detector_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.list_detector_models_request.ListDetectorModelsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_detector_model_versions(
        self,
        detector_model_name: "capo_iot_events.types.detector_model_name.DetectorModelName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        next_token: Optional["capo_iot_events.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_events.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_events.types.list_detector_model_versions_response.ListDetectorModelVersionsResponse":
        """<p>Lists all the versions of a detector model. Only the metadata associated with each detector model version is returned.</p>

        Args:
            detector_model_name: <p>The name of the detector model whose versions are returned.</p>
            next_token: <p>The token that you can use to return the next set of results.</p>
            max_results: <p>The maximum number of results to be returned per request.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.list_detector_model_versions_request.ListDetectorModelVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.list_detector_model_versions_response.ListDetectorModelVersionsResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.list_detector_model_versions

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.list_detector_model_versions.async_list_detector_model_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.list_detector_model_versions_request.ListDetectorModelVersionsRequest = {
            "detector_model_name": detector_model_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_input_routings(
        self,
        input_identifier: "capo_iot_events.types.input_identifier.InputIdentifier",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        max_results: Optional["capo_iot_events.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_events.types.next_token.NextToken"] = None,
    ) -> "capo_iot_events.types.list_input_routings_response.ListInputRoutingsResponse":
        """<p> Lists one or more input routings. </p>

        Args:
            input_identifier: <p> The identifer of the routed input. </p>
            max_results: <p> The maximum number of results to be returned per request. </p>
            next_token: <p> The token that you can use to return the next set of results. </p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.list_input_routings_request.ListInputRoutingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.list_input_routings_response.ListInputRoutingsResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.list_input_routings

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.list_input_routings.async_list_input_routings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.list_input_routings_request.ListInputRoutingsRequest = {
            "input_identifier": input_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_inputs(
        self,
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        next_token: Optional["capo_iot_events.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_events.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_events.types.list_inputs_response.ListInputsResponse":
        """<p>Lists the inputs you have created.</p>

        Args:
            next_token: <p>The token that you can use to return the next set of results.</p>
            max_results: <p>The maximum number of results to be returned per request.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.list_inputs_request.ListInputsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.list_inputs_response.ListInputsResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.list_inputs

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.list_inputs.async_list_inputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.list_inputs_request.ListInputsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> "capo_iot_events.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags (metadata) you have assigned to the resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_logging_options(
        self,
        logging_options: "capo_iot_events.types.logging_options.LoggingOptions",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> None:
        """<p>Sets or updates the AWS IoT Events logging options.</p> <p>If you update the value of any <code>loggingOptions</code> field, it takes up to one minute for the change to take effect. If you change the policy attached to the role you specified in the <code>roleArn</code> field (for example, to correct an invalid policy), it takes up to five minutes for that change to take effect.</p>

        Args:
            logging_options: <p>The new values of the AWS IoT Events logging options.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The requested operation is not supported.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.put_logging_options_request.PutLoggingOptionsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_events._operations.iot_columbo_service.put_logging_options

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.put_logging_options.async_put_logging_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.put_logging_options_request.PutLoggingOptionsRequest = {
            "logging_options": logging_options
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_detector_model_analysis(
        self,
        detector_model_definition: "capo_iot_events.types.detector_model_definition.DetectorModelDefinition",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> "capo_iot_events.types.start_detector_model_analysis_response.StartDetectorModelAnalysisResponse":
        """<p>Performs an analysis of your detector model. For more information, see <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-analyze-api.html">Troubleshooting a detector model</a> in the <i>AWS IoT Events Developer Guide</i>.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.limit_exceeded_exception.LimitExceededException: <p>A limit was exceeded.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.start_detector_model_analysis_request.StartDetectorModelAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.start_detector_model_analysis_response.StartDetectorModelAnalysisResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.start_detector_model_analysis

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.start_detector_model_analysis.async_start_detector_model_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.start_detector_model_analysis_request.StartDetectorModelAnalysisRequest = {
            "detector_model_definition": detector_model_definition
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_iot_events.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> "capo_iot_events.types.tag_resource_response.TagResourceResponse":
        """<p>Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The new or modified tags for the resource.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.limit_exceeded_exception.LimitExceededException: <p>A limit was exceeded.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_iot_events.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
    ) -> "capo_iot_events.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the given tags (metadata) from the resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>A list of the keys of the tags to be removed from the resource.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_alarm_model(
        self,
        alarm_model_name: "capo_iot_events.types.alarm_model_name.AlarmModelName",
        role_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName",
        alarm_rule: "capo_iot_events.types.alarm_rule.AlarmRule",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        alarm_model_description: Optional[
            "capo_iot_events.types.alarm_model_description.AlarmModelDescription"
        ] = None,
        severity: Optional["capo_iot_events.types.severity.Severity"] = None,
        alarm_notification: Optional[
            "capo_iot_events.types.alarm_notification.AlarmNotification"
        ] = None,
        alarm_event_actions: Optional[
            "capo_iot_events.types.alarm_event_actions.AlarmEventActions"
        ] = None,
        alarm_capabilities: Optional[
            "capo_iot_events.types.alarm_capabilities.AlarmCapabilities"
        ] = None,
    ) -> "capo_iot_events.types.update_alarm_model_response.UpdateAlarmModelResponse":
        """<p>Updates an alarm model. Any alarms that were created based on the previous version are deleted and then created again as new data arrives.</p>

        Args:
            alarm_model_name: <p>The name of the alarm model.</p>
            alarm_model_description: <p>The description of the alarm model.</p>
            role_arn: <p>The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>.</p>
            severity: <p>A non-negative integer that reflects the severity level of the alarm.</p>
            alarm_rule: <p>Defines when your alarm is invoked.</p>
            alarm_notification: <p>Contains information about one or more notification actions.</p>
            alarm_event_actions: <p>Contains information about one or more alarm actions.</p>
            alarm_capabilities: <p>Contains the configuration information of alarm state changes.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.update_alarm_model_request.UpdateAlarmModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.update_alarm_model_response.UpdateAlarmModelResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.update_alarm_model

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.update_alarm_model.async_update_alarm_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.update_alarm_model_request.UpdateAlarmModelRequest = {
            "alarm_model_name": alarm_model_name,
            "role_arn": role_arn,
            "alarm_rule": alarm_rule,
        }
        if alarm_model_description is not None:
            input_["alarm_model_description"] = alarm_model_description
        if severity is not None:
            input_["severity"] = severity
        if alarm_notification is not None:
            input_["alarm_notification"] = alarm_notification
        if alarm_event_actions is not None:
            input_["alarm_event_actions"] = alarm_event_actions
        if alarm_capabilities is not None:
            input_["alarm_capabilities"] = alarm_capabilities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_detector_model(
        self,
        detector_model_name: "capo_iot_events.types.detector_model_name.DetectorModelName",
        detector_model_definition: "capo_iot_events.types.detector_model_definition.DetectorModelDefinition",
        role_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        detector_model_description: Optional[
            "capo_iot_events.types.detector_model_description.DetectorModelDescription"
        ] = None,
        evaluation_method: Optional[
            "capo_iot_events.types.evaluation_method.EvaluationMethod"
        ] = None,
    ) -> "capo_iot_events.types.update_detector_model_response.UpdateDetectorModelResponse":
        """<p>Updates a detector model. Detectors (instances) spawned by the previous version are deleted and then re-created as new inputs arrive.</p>

        Args:
            detector_model_name: <p>The name of the detector model that is updated.</p>
            detector_model_definition: <p>Information that defines how a detector operates.</p>
            detector_model_description: <p>A brief description of the detector model.</p>
            role_arn: <p>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</p>
            evaluation_method: <p>Information about the order in which events are evaluated and how actions are executed. </p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.update_detector_model_request.UpdateDetectorModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.update_detector_model_response.UpdateDetectorModelResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.update_detector_model

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.update_detector_model.async_update_detector_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.update_detector_model_request.UpdateDetectorModelRequest = {
            "detector_model_name": detector_model_name,
            "detector_model_definition": detector_model_definition,
            "role_arn": role_arn,
        }
        if detector_model_description is not None:
            input_["detector_model_description"] = detector_model_description
        if evaluation_method is not None:
            input_["evaluation_method"] = evaluation_method

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_input(
        self,
        input_name: "capo_iot_events.types.input_name.InputName",
        input_definition: "capo_iot_events.types.input_definition.InputDefinition",
        *,
        config_overrides: Optional[AsyncIoTEventsClientConfig] = None,
        input_description: Optional[
            "capo_iot_events.types.input_description.InputDescription"
        ] = None,
    ) -> "capo_iot_events.types.update_input_response.UpdateInputResponse":
        """<p>Updates an input.</p>

        Args:
            input_name: <p>The name of the input you want to update.</p>
            input_description: <p>A brief description of the input.</p>
            input_definition: <p>The definition of the input.</p>

        Raises:
            capo_iot_events.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is in use.</p>
            capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_events.types.update_input_request.UpdateInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_events.types.update_input_response.UpdateInputResponse"
        ]:
            import capo_iot_events._operations.iot_columbo_service.update_input

            (
                output,
                http_response,
            ) = await capo_iot_events._operations.iot_columbo_service.update_input.async_update_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events.types.update_input_request.UpdateInputRequest = {
            "input_name": input_name,
            "input_definition": input_definition,
        }
        if input_description is not None:
            input_["input_description"] = input_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
