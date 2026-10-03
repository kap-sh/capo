"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#IotColumboDataService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_iot_events_data._auth._signers
import capo_iot_events_data._auth._sigv4
from capo_iot_events_data._auth._identity import Credentials
from capo_iot_events_data._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iot_events_data._auth._zapros_handler import AuthMiddleware
from capo_iot_events_data._services._aws_config import aws_config
from capo_iot_events_data._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_iot_events_data.types.acknowledge_alarm_action_requests
    import capo_iot_events_data.types.alarm_model_name
    import capo_iot_events_data.types.batch_acknowledge_alarm_request
    import capo_iot_events_data.types.batch_acknowledge_alarm_response
    import capo_iot_events_data.types.batch_delete_detector_request
    import capo_iot_events_data.types.batch_delete_detector_response
    import capo_iot_events_data.types.batch_disable_alarm_request
    import capo_iot_events_data.types.batch_disable_alarm_response
    import capo_iot_events_data.types.batch_enable_alarm_request
    import capo_iot_events_data.types.batch_enable_alarm_response
    import capo_iot_events_data.types.batch_put_message_request
    import capo_iot_events_data.types.batch_put_message_response
    import capo_iot_events_data.types.batch_reset_alarm_request
    import capo_iot_events_data.types.batch_reset_alarm_response
    import capo_iot_events_data.types.batch_snooze_alarm_request
    import capo_iot_events_data.types.batch_snooze_alarm_response
    import capo_iot_events_data.types.batch_update_detector_request
    import capo_iot_events_data.types.batch_update_detector_response
    import capo_iot_events_data.types.delete_detector_requests
    import capo_iot_events_data.types.describe_alarm_request
    import capo_iot_events_data.types.describe_alarm_response
    import capo_iot_events_data.types.describe_detector_request
    import capo_iot_events_data.types.describe_detector_response
    import capo_iot_events_data.types.detector_model_name
    import capo_iot_events_data.types.disable_alarm_action_requests
    import capo_iot_events_data.types.enable_alarm_action_requests
    import capo_iot_events_data.types.key_value
    import capo_iot_events_data.types.list_alarms_request
    import capo_iot_events_data.types.list_alarms_response
    import capo_iot_events_data.types.list_detectors_request
    import capo_iot_events_data.types.list_detectors_response
    import capo_iot_events_data.types.max_results
    import capo_iot_events_data.types.messages
    import capo_iot_events_data.types.next_token
    import capo_iot_events_data.types.reset_alarm_action_requests
    import capo_iot_events_data.types.snooze_alarm_action_requests
    import capo_iot_events_data.types.state_name
    import capo_iot_events_data.types.update_detector_requests


class IoTEventsDataClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class IoTEventsDataClient:
    """A client for the ``IoTEventsData`` service.

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
        self._config = IoTEventsDataClientConfig(
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
        self, config_overrides: Optional[IoTEventsDataClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: IoTEventsDataClientConfig = config_overrides or {}
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

    def batch_acknowledge_alarm(
        self,
        acknowledge_action_requests: "capo_iot_events_data.types.acknowledge_alarm_action_requests.AcknowledgeAlarmActionRequests",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
    ) -> "capo_iot_events_data.types.batch_acknowledge_alarm_response.BatchAcknowledgeAlarmResponse":
        """<p>Acknowledges one or more alarms. The alarms change to the <code>ACKNOWLEDGED</code> state after you acknowledge them.</p>

        Args:
            acknowledge_action_requests: <p>The list of acknowledge action requests. You can specify up to 10 requests per operation.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.batch_acknowledge_alarm_request.BatchAcknowledgeAlarmRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.batch_acknowledge_alarm_response.BatchAcknowledgeAlarmResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.batch_acknowledge_alarm

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.batch_acknowledge_alarm.batch_acknowledge_alarm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.batch_acknowledge_alarm_request.BatchAcknowledgeAlarmRequest = {
            "acknowledge_action_requests": acknowledge_action_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_detector(
        self,
        detectors: "capo_iot_events_data.types.delete_detector_requests.DeleteDetectorRequests",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
    ) -> "capo_iot_events_data.types.batch_delete_detector_response.BatchDeleteDetectorResponse":
        """<p>Deletes one or more detectors that were created. When a detector is deleted, its state will be cleared and the detector will be removed from the list of detectors. The deleted detector will no longer appear if referenced in the <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_ListDetectors.html">ListDetectors</a> API call.</p>

        Args:
            detectors: <p>The list of one or more detectors to be deleted.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.batch_delete_detector_request.BatchDeleteDetectorRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.batch_delete_detector_response.BatchDeleteDetectorResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.batch_delete_detector

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.batch_delete_detector.batch_delete_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.batch_delete_detector_request.BatchDeleteDetectorRequest = {
            "detectors": detectors
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_disable_alarm(
        self,
        disable_action_requests: "capo_iot_events_data.types.disable_alarm_action_requests.DisableAlarmActionRequests",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
    ) -> "capo_iot_events_data.types.batch_disable_alarm_response.BatchDisableAlarmResponse":
        """<p>Disables one or more alarms. The alarms change to the <code>DISABLED</code> state after you disable them.</p>

        Args:
            disable_action_requests: <p>The list of disable action requests. You can specify up to 10 requests per operation.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.batch_disable_alarm_request.BatchDisableAlarmRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.batch_disable_alarm_response.BatchDisableAlarmResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.batch_disable_alarm

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.batch_disable_alarm.batch_disable_alarm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.batch_disable_alarm_request.BatchDisableAlarmRequest = {
            "disable_action_requests": disable_action_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_enable_alarm(
        self,
        enable_action_requests: "capo_iot_events_data.types.enable_alarm_action_requests.EnableAlarmActionRequests",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
    ) -> "capo_iot_events_data.types.batch_enable_alarm_response.BatchEnableAlarmResponse":
        """<p>Enables one or more alarms. The alarms change to the <code>NORMAL</code> state after you enable them.</p>

        Args:
            enable_action_requests: <p>The list of enable action requests. You can specify up to 10 requests per operation.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.batch_enable_alarm_request.BatchEnableAlarmRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.batch_enable_alarm_response.BatchEnableAlarmResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.batch_enable_alarm

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.batch_enable_alarm.batch_enable_alarm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.batch_enable_alarm_request.BatchEnableAlarmRequest = {
            "enable_action_requests": enable_action_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_put_message(
        self,
        messages: "capo_iot_events_data.types.messages.Messages",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
    ) -> (
        "capo_iot_events_data.types.batch_put_message_response.BatchPutMessageResponse"
    ):
        """<p>Sends a set of messages to the IoT Events system. Each message payload is transformed into the input you specify (<code>"inputName"</code>) and ingested into any detectors that monitor that input. If multiple messages are sent, the order in which the messages are processed isn't guaranteed. To guarantee ordering, you must send messages one at a time and wait for a successful response.</p>

        Args:
            messages: <p>The list of messages to send. Each message has the following format: <code>'{ "messageId": "string", "inputName": "string", "payload": "string"}'</code> </p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.batch_put_message_request.BatchPutMessageRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.batch_put_message_response.BatchPutMessageResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.batch_put_message

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.batch_put_message.batch_put_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.batch_put_message_request.BatchPutMessageRequest = {
            "messages": messages
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_reset_alarm(
        self,
        reset_action_requests: "capo_iot_events_data.types.reset_alarm_action_requests.ResetAlarmActionRequests",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
    ) -> (
        "capo_iot_events_data.types.batch_reset_alarm_response.BatchResetAlarmResponse"
    ):
        """<p>Resets one or more alarms. The alarms return to the <code>NORMAL</code> state after you reset them.</p>

        Args:
            reset_action_requests: <p>The list of reset action requests. You can specify up to 10 requests per operation.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.batch_reset_alarm_request.BatchResetAlarmRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.batch_reset_alarm_response.BatchResetAlarmResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.batch_reset_alarm

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.batch_reset_alarm.batch_reset_alarm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.batch_reset_alarm_request.BatchResetAlarmRequest = {
            "reset_action_requests": reset_action_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_snooze_alarm(
        self,
        snooze_action_requests: "capo_iot_events_data.types.snooze_alarm_action_requests.SnoozeAlarmActionRequests",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
    ) -> "capo_iot_events_data.types.batch_snooze_alarm_response.BatchSnoozeAlarmResponse":
        """<p>Changes one or more alarms to the snooze mode. The alarms change to the <code>SNOOZE_DISABLED</code> state after you set them to the snooze mode.</p>

        Args:
            snooze_action_requests: <p>The list of snooze action requests. You can specify up to 10 requests per operation.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.batch_snooze_alarm_request.BatchSnoozeAlarmRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.batch_snooze_alarm_response.BatchSnoozeAlarmResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.batch_snooze_alarm

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.batch_snooze_alarm.batch_snooze_alarm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.batch_snooze_alarm_request.BatchSnoozeAlarmRequest = {
            "snooze_action_requests": snooze_action_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_detector(
        self,
        detectors: "capo_iot_events_data.types.update_detector_requests.UpdateDetectorRequests",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
    ) -> "capo_iot_events_data.types.batch_update_detector_response.BatchUpdateDetectorResponse":
        """<p>Updates the state, variable values, and timer settings of one or more detectors (instances) of a specified detector model.</p>

        Args:
            detectors: <p>The list of detectors (instances) to update, along with the values to update.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.batch_update_detector_request.BatchUpdateDetectorRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.batch_update_detector_response.BatchUpdateDetectorResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.batch_update_detector

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.batch_update_detector.batch_update_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.batch_update_detector_request.BatchUpdateDetectorRequest = {
            "detectors": detectors
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_alarm(
        self,
        alarm_model_name: "capo_iot_events_data.types.alarm_model_name.AlarmModelName",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
        key_value: Optional["capo_iot_events_data.types.key_value.KeyValue"] = None,
    ) -> "capo_iot_events_data.types.describe_alarm_response.DescribeAlarmResponse":
        """<p>Retrieves information about an alarm.</p>

        Args:
            alarm_model_name: <p>The name of the alarm model.</p>
            key_value: <p>The value of the key used as a filter to select only the alarms associated with the <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key">key</a>.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.describe_alarm_request.DescribeAlarmRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.describe_alarm_response.DescribeAlarmResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.describe_alarm

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.describe_alarm.describe_alarm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.describe_alarm_request.DescribeAlarmRequest = {
            "alarm_model_name": alarm_model_name
        }
        if key_value is not None:
            input_["key_value"] = key_value

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_detector(
        self,
        detector_model_name: "capo_iot_events_data.types.detector_model_name.DetectorModelName",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
        key_value: Optional["capo_iot_events_data.types.key_value.KeyValue"] = None,
    ) -> (
        "capo_iot_events_data.types.describe_detector_response.DescribeDetectorResponse"
    ):
        """<p>Returns information about the specified detector (instance).</p>

        Args:
            detector_model_name: <p>The name of the detector model whose detectors (instances) you want information about.</p>
            key_value: <p>A filter used to limit results to detectors (instances) created because of the given key ID.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.describe_detector_request.DescribeDetectorRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.describe_detector_response.DescribeDetectorResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.describe_detector

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.describe_detector.describe_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.describe_detector_request.DescribeDetectorRequest = {
            "detector_model_name": detector_model_name
        }
        if key_value is not None:
            input_["key_value"] = key_value

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_alarms(
        self,
        alarm_model_name: "capo_iot_events_data.types.alarm_model_name.AlarmModelName",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
        next_token: Optional["capo_iot_events_data.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iot_events_data.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_events_data.types.list_alarms_response.ListAlarmsResponse":
        """<p>Lists one or more alarms. The operation returns only the metadata associated with each alarm.</p>

        Args:
            alarm_model_name: <p>The name of the alarm model.</p>
            next_token: <p>The token that you can use to return the next set of results.</p>
            max_results: <p>The maximum number of results to be returned per request.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.list_alarms_request.ListAlarmsRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.list_alarms_response.ListAlarmsResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.list_alarms

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.list_alarms.list_alarms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.list_alarms_request.ListAlarmsRequest = {
            "alarm_model_name": alarm_model_name
        }
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

    def list_detectors(
        self,
        detector_model_name: "capo_iot_events_data.types.detector_model_name.DetectorModelName",
        *,
        config_overrides: Optional[IoTEventsDataClientConfig] = None,
        state_name: Optional["capo_iot_events_data.types.state_name.StateName"] = None,
        next_token: Optional["capo_iot_events_data.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iot_events_data.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_events_data.types.list_detectors_response.ListDetectorsResponse":
        """<p>Lists detectors (the instances of a detector model).</p>

        Args:
            detector_model_name: <p>The name of the detector model whose detectors (instances) are listed.</p>
            state_name: <p>A filter that limits results to those detectors (instances) in the given state.</p>
            next_token: <p>The token that you can use to return the next set of results.</p>
            max_results: <p>The maximum number of results to be returned per request.</p>

        Raises:
            capo_iot_events_data.errors.internal_failure_exception.InternalFailureException: <p>An internal failure occurred.</p>
            capo_iot_events_data.errors.invalid_request_exception.InvalidRequestException: <p>The request was invalid.</p>
            capo_iot_events_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_iot_events_data.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_iot_events_data.errors.throttling_exception.ThrottlingException: <p>The request could not be completed due to throttling.</p>
            capo_iot_events_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_events_data.types.list_detectors_request.ListDetectorsRequest]",
        ) -> OperationResponse[
            "capo_iot_events_data.types.list_detectors_response.ListDetectorsResponse"
        ]:
            import capo_iot_events_data._operations.iot_columbo_data_service.list_detectors

            output, http_response = (
                capo_iot_events_data._operations.iot_columbo_data_service.list_detectors.list_detectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_events_data.types.list_detectors_request.ListDetectorsRequest = {
            "detector_model_name": detector_model_name
        }
        if state_name is not None:
            input_["state_name"] = state_name
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
