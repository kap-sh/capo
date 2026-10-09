"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#IotSenateService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_iotdeviceadvisor._auth._signers
import capo_iotdeviceadvisor._auth._sigv4
from capo_iotdeviceadvisor._auth._identity import Credentials
from capo_iotdeviceadvisor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iotdeviceadvisor._auth._zapros_handler import AuthMiddleware
from capo_iotdeviceadvisor._pagination import resolve_path as _resolve_path
from capo_iotdeviceadvisor._services._aws_config import aws_config
from capo_iotdeviceadvisor._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.amazon_resource_name
    import capo_iotdeviceadvisor.types.authentication_method
    import capo_iotdeviceadvisor.types.client_token
    import capo_iotdeviceadvisor.types.create_suite_definition_request
    import capo_iotdeviceadvisor.types.create_suite_definition_response
    import capo_iotdeviceadvisor.types.delete_suite_definition_request
    import capo_iotdeviceadvisor.types.delete_suite_definition_response
    import capo_iotdeviceadvisor.types.get_endpoint_request
    import capo_iotdeviceadvisor.types.get_endpoint_response
    import capo_iotdeviceadvisor.types.get_suite_definition_request
    import capo_iotdeviceadvisor.types.get_suite_definition_response
    import capo_iotdeviceadvisor.types.get_suite_run_report_request
    import capo_iotdeviceadvisor.types.get_suite_run_report_response
    import capo_iotdeviceadvisor.types.get_suite_run_request
    import capo_iotdeviceadvisor.types.get_suite_run_response
    import capo_iotdeviceadvisor.types.list_suite_definitions_request
    import capo_iotdeviceadvisor.types.list_suite_definitions_response
    import capo_iotdeviceadvisor.types.list_suite_runs_request
    import capo_iotdeviceadvisor.types.list_suite_runs_response
    import capo_iotdeviceadvisor.types.list_tags_for_resource_request
    import capo_iotdeviceadvisor.types.list_tags_for_resource_response
    import capo_iotdeviceadvisor.types.max_results
    import capo_iotdeviceadvisor.types.start_suite_run_request
    import capo_iotdeviceadvisor.types.start_suite_run_response
    import capo_iotdeviceadvisor.types.stop_suite_run_request
    import capo_iotdeviceadvisor.types.stop_suite_run_response
    import capo_iotdeviceadvisor.types.suite_definition_configuration
    import capo_iotdeviceadvisor.types.suite_definition_version
    import capo_iotdeviceadvisor.types.suite_run_configuration
    import capo_iotdeviceadvisor.types.tag_key_list
    import capo_iotdeviceadvisor.types.tag_map
    import capo_iotdeviceadvisor.types.tag_resource_request
    import capo_iotdeviceadvisor.types.tag_resource_response
    import capo_iotdeviceadvisor.types.token
    import capo_iotdeviceadvisor.types.untag_resource_request
    import capo_iotdeviceadvisor.types.untag_resource_response
    import capo_iotdeviceadvisor.types.update_suite_definition_request
    import capo_iotdeviceadvisor.types.update_suite_definition_response
    import capo_iotdeviceadvisor.types.uuid


class IotDeviceAdvisorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class IotDeviceAdvisorClient:
    """A client for the ``IotDeviceAdvisor`` service.

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
        self._config = IotDeviceAdvisorClientConfig(
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
        self, config_overrides: Optional[IotDeviceAdvisorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: IotDeviceAdvisorClientConfig = config_overrides or {}
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

    def create_suite_definition(
        self,
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        suite_definition_configuration: Optional[
            "capo_iotdeviceadvisor.types.suite_definition_configuration.SuiteDefinitionConfiguration"
        ] = None,
        tags: Optional["capo_iotdeviceadvisor.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_iotdeviceadvisor.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotdeviceadvisor.types.create_suite_definition_response.CreateSuiteDefinitionResponse":
        """<p>Creates a Device Advisor test suite.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">CreateSuiteDefinition</a> action.</p>

        Args:
            suite_definition_configuration: <p>Creates a Device Advisor test suite with suite definition configuration.</p>
            tags: <p>The tags to be attached to the suite definition.</p>
            client_token: <p>The client token for the test suite definition creation. This token is used for tracking test suite definition creation using retries and obtaining its status. This parameter is optional.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.create_suite_definition_request.CreateSuiteDefinitionRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.create_suite_definition_response.CreateSuiteDefinitionResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.create_suite_definition

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.create_suite_definition.create_suite_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.create_suite_definition_request.CreateSuiteDefinitionRequest = {}
        if suite_definition_configuration is not None:
            input_["suite_definition_configuration"] = suite_definition_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_suite_definition(
        self,
        suite_definition_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
    ) -> "capo_iotdeviceadvisor.types.delete_suite_definition_response.DeleteSuiteDefinitionResponse":
        """<p>Deletes a Device Advisor test suite.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">DeleteSuiteDefinition</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite to be deleted.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.delete_suite_definition_request.DeleteSuiteDefinitionRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.delete_suite_definition_response.DeleteSuiteDefinitionResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.delete_suite_definition

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.delete_suite_definition.delete_suite_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.delete_suite_definition_request.DeleteSuiteDefinitionRequest = {
            "suite_definition_id": suite_definition_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_endpoint(
        self,
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        thing_arn: Optional[
            "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        certificate_arn: Optional[
            "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        device_role_arn: Optional[
            "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        authentication_method: Optional[
            "capo_iotdeviceadvisor.types.authentication_method.AuthenticationMethod"
        ] = None,
    ) -> "capo_iotdeviceadvisor.types.get_endpoint_response.GetEndpointResponse":
        """<p>Gets information about an Device Advisor endpoint.</p>

        Args:
            thing_arn: <p>The thing ARN of the device. This is an optional parameter.</p>
            certificate_arn: <p>The certificate ARN of the device. This is an optional parameter.</p>
            device_role_arn: <p>The device role ARN of the device. This is an optional parameter.</p>
            authentication_method: <p>The authentication method used during the device connection.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Sends a Resource Not Found exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.get_endpoint_request.GetEndpointRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.get_endpoint_response.GetEndpointResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.get_endpoint

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.get_endpoint.get_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.get_endpoint_request.GetEndpointRequest = {}
        if thing_arn is not None:
            input_["thing_arn"] = thing_arn
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if device_role_arn is not None:
            input_["device_role_arn"] = device_role_arn
        if authentication_method is not None:
            input_["authentication_method"] = authentication_method

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_suite_definition(
        self,
        suite_definition_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        suite_definition_version: Optional[
            "capo_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
        ] = None,
    ) -> "capo_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse":
        """<p>Gets information about a Device Advisor test suite.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">GetSuiteDefinition</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite to get.</p>
            suite_definition_version: <p>Suite definition version of the test suite to get.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Sends a Resource Not Found exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.get_suite_definition_request.GetSuiteDefinitionRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.get_suite_definition

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.get_suite_definition.get_suite_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.get_suite_definition_request.GetSuiteDefinitionRequest = {
            "suite_definition_id": suite_definition_id
        }
        if suite_definition_version is not None:
            input_["suite_definition_version"] = suite_definition_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_suite_run(
        self,
        suite_definition_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        suite_run_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
    ) -> "capo_iotdeviceadvisor.types.get_suite_run_response.GetSuiteRunResponse":
        """<p>Gets information about a Device Advisor test suite run.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">GetSuiteRun</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID for the test suite run.</p>
            suite_run_id: <p>Suite run ID for the test suite run.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Sends a Resource Not Found exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.get_suite_run_request.GetSuiteRunRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.get_suite_run_response.GetSuiteRunResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.get_suite_run

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.get_suite_run.get_suite_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.get_suite_run_request.GetSuiteRunRequest = {
            "suite_definition_id": suite_definition_id,
            "suite_run_id": suite_run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_suite_run_report(
        self,
        suite_definition_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        suite_run_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
    ) -> "capo_iotdeviceadvisor.types.get_suite_run_report_response.GetSuiteRunReportResponse":
        """<p>Gets a report download link for a successful Device Advisor qualifying test suite run.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">GetSuiteRunReport</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite.</p>
            suite_run_id: <p>Suite run ID of the test suite run.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Sends a Resource Not Found exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.get_suite_run_report_request.GetSuiteRunReportRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.get_suite_run_report_response.GetSuiteRunReportResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.get_suite_run_report

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.get_suite_run_report.get_suite_run_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.get_suite_run_report_request.GetSuiteRunReportRequest = {
            "suite_definition_id": suite_definition_id,
            "suite_run_id": suite_run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_suite_definitions(
        self,
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        max_results: Optional[
            "capo_iotdeviceadvisor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_iotdeviceadvisor.types.token.Token"] = None,
    ) -> "capo_iotdeviceadvisor.types.list_suite_definitions_response.ListSuiteDefinitionsResponse":
        """<p>Lists the Device Advisor test suites you have created.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">ListSuiteDefinitions</a> action.</p>

        Args:
            max_results: <p>The maximum number of results to return at once.</p>
            next_token: <p>A token used to get the next set of results.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.list_suite_definitions_request.ListSuiteDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.list_suite_definitions_response.ListSuiteDefinitionsResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.list_suite_definitions

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.list_suite_definitions.list_suite_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.list_suite_definitions_request.ListSuiteDefinitionsRequest = {}
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

    def iter_list_suite_definitions(
        self,
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        max_results: Optional[
            "capo_iotdeviceadvisor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_iotdeviceadvisor.types.token.Token"] = None,
    ) -> "Iterator[capo_iotdeviceadvisor.types.list_suite_definitions_response.ListSuiteDefinitionsResponse]":
        _token = next_token
        while True:
            _response = self.list_suite_definitions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_suite_runs(
        self,
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        suite_definition_id: Optional["capo_iotdeviceadvisor.types.uuid.UUID"] = None,
        suite_definition_version: Optional[
            "capo_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
        ] = None,
        max_results: Optional[
            "capo_iotdeviceadvisor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_iotdeviceadvisor.types.token.Token"] = None,
    ) -> "capo_iotdeviceadvisor.types.list_suite_runs_response.ListSuiteRunsResponse":
        """<p>Lists runs of the specified Device Advisor test suite. You can list all runs of the test suite, or the runs of a specific version of the test suite.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">ListSuiteRuns</a> action.</p>

        Args:
            suite_definition_id: <p>Lists the test suite runs of the specified test suite based on suite definition ID.</p>
            suite_definition_version: <p>Must be passed along with <code>suiteDefinitionId</code>. Lists the test suite runs of the specified test suite based on suite definition version.</p>
            max_results: <p>The maximum number of results to return at once.</p>
            next_token: <p>A token to retrieve the next set of results.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.list_suite_runs_request.ListSuiteRunsRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.list_suite_runs_response.ListSuiteRunsResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.list_suite_runs

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.list_suite_runs.list_suite_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.list_suite_runs_request.ListSuiteRunsRequest = {}
        if suite_definition_id is not None:
            input_["suite_definition_id"] = suite_definition_id
        if suite_definition_version is not None:
            input_["suite_definition_version"] = suite_definition_version
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

    def iter_list_suite_runs(
        self,
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        suite_definition_id: Optional["capo_iotdeviceadvisor.types.uuid.UUID"] = None,
        suite_definition_version: Optional[
            "capo_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
        ] = None,
        max_results: Optional[
            "capo_iotdeviceadvisor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_iotdeviceadvisor.types.token.Token"] = None,
    ) -> "Iterator[capo_iotdeviceadvisor.types.list_suite_runs_response.ListSuiteRunsResponse]":
        _token = next_token
        while True:
            _response = self.list_suite_runs(
                config_overrides=config_overrides,
                suite_definition_id=suite_definition_id,
                suite_definition_version=suite_definition_version,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
    ) -> "capo_iotdeviceadvisor.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags attached to an IoT Device Advisor resource.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">ListTagsForResource</a> action.</p>

        Args:
            resource_arn: <p>The resource ARN of the IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Sends a Resource Not Found exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.list_tags_for_resource

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_suite_run(
        self,
        suite_definition_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        suite_definition_version: Optional[
            "capo_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
        ] = None,
        suite_run_configuration: Optional[
            "capo_iotdeviceadvisor.types.suite_run_configuration.SuiteRunConfiguration"
        ] = None,
        tags: Optional["capo_iotdeviceadvisor.types.tag_map.TagMap"] = None,
    ) -> "capo_iotdeviceadvisor.types.start_suite_run_response.StartSuiteRunResponse":
        """<p>Starts a Device Advisor test suite run.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">StartSuiteRun</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite.</p>
            suite_definition_version: <p>Suite definition version of the test suite.</p>
            suite_run_configuration: <p>Suite run configuration.</p>
            tags: <p>The tags to be attached to the suite run.</p>

        Raises:
            capo_iotdeviceadvisor.errors.conflict_exception.ConflictException: <p>Sends a Conflict Exception.</p>
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.start_suite_run_request.StartSuiteRunRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.start_suite_run_response.StartSuiteRunResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.start_suite_run

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.start_suite_run.start_suite_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.start_suite_run_request.StartSuiteRunRequest = {
            "suite_definition_id": suite_definition_id
        }
        if suite_definition_version is not None:
            input_["suite_definition_version"] = suite_definition_version
        if suite_run_configuration is not None:
            input_["suite_run_configuration"] = suite_run_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_suite_run(
        self,
        suite_definition_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        suite_run_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
    ) -> "capo_iotdeviceadvisor.types.stop_suite_run_response.StopSuiteRunResponse":
        """<p>Stops a Device Advisor test suite run that is currently running.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">StopSuiteRun</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite run to be stopped.</p>
            suite_run_id: <p>Suite run ID of the test suite run to be stopped.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Sends a Resource Not Found exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.stop_suite_run_request.StopSuiteRunRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.stop_suite_run_response.StopSuiteRunResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.stop_suite_run

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.stop_suite_run.stop_suite_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.stop_suite_run_request.StopSuiteRunRequest = {
            "suite_definition_id": suite_definition_id,
            "suite_run_id": suite_run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        tags: Optional["capo_iotdeviceadvisor.types.tag_map.TagMap"] = None,
    ) -> "capo_iotdeviceadvisor.types.tag_resource_response.TagResourceResponse":
        """<p>Adds to and modifies existing tags of an IoT Device Advisor resource.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">TagResource</a> action.</p>

        Args:
            resource_arn: <p>The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.</p>
            tags: <p>The tags to be attached to the IoT Device Advisor resource.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Sends a Resource Not Found exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.tag_resource

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
        }
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
        resource_arn: "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        tag_keys: Optional[
            "capo_iotdeviceadvisor.types.tag_key_list.TagKeyList"
        ] = None,
    ) -> "capo_iotdeviceadvisor.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from an IoT Device Advisor resource.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">UntagResource</a> action.</p>

        Args:
            resource_arn: <p>The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.</p>
            tag_keys: <p>List of tag keys to remove from the IoT Device Advisor resource.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Sends a Resource Not Found exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.untag_resource

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_suite_definition(
        self,
        suite_definition_id: "capo_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[IotDeviceAdvisorClientConfig] = None,
        suite_definition_configuration: Optional[
            "capo_iotdeviceadvisor.types.suite_definition_configuration.SuiteDefinitionConfiguration"
        ] = None,
    ) -> "capo_iotdeviceadvisor.types.update_suite_definition_response.UpdateSuiteDefinitionResponse":
        """<p>Updates a Device Advisor test suite.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">UpdateSuiteDefinition</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite to be updated.</p>
            suite_definition_configuration: <p>Updates a Device Advisor test suite with suite definition configuration.</p>

        Raises:
            capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException: <p>Sends an Internal Failure exception.</p>
            capo_iotdeviceadvisor.errors.validation_exception.ValidationException: <p>Sends a validation exception.</p>
            capo_iotdeviceadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotdeviceadvisor.types.update_suite_definition_request.UpdateSuiteDefinitionRequest]",
        ) -> OperationResponse[
            "capo_iotdeviceadvisor.types.update_suite_definition_response.UpdateSuiteDefinitionResponse"
        ]:
            import capo_iotdeviceadvisor._operations.iot_senate_service.update_suite_definition

            output, http_response = (
                capo_iotdeviceadvisor._operations.iot_senate_service.update_suite_definition.update_suite_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotdeviceadvisor.types.update_suite_definition_request.UpdateSuiteDefinitionRequest = {
            "suite_definition_id": suite_definition_id
        }
        if suite_definition_configuration is not None:
            input_["suite_definition_configuration"] = suite_definition_configuration

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
