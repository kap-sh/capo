from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_appconfigdata._auth._signers
import capo_appconfigdata._auth._sigv4
from capo_appconfigdata._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_appconfigdata.types.identifier
    import capo_appconfigdata.types.optional_poll_seconds
    import capo_appconfigdata.types.start_configuration_session_request
    import capo_appconfigdata.types.start_configuration_session_response
    from capo_appconfigdata._services.app_config_data import (
        AppConfigDataClient,
        AppConfigDataClientConfig,
    )
    from capo_appconfigdata._services.async_app_config_data import (
        AsyncAppConfigDataClient,
        AsyncAppConfigDataClientConfig,
    )


class ConfigurationSession:
    def __init__(self, service: AppConfigDataClient) -> None:
        self._service = service

    def create(
        self,
        application_identifier: "capo_appconfigdata.types.identifier.Identifier",
        environment_identifier: "capo_appconfigdata.types.identifier.Identifier",
        configuration_profile_identifier: "capo_appconfigdata.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigDataClientConfig] = None,
        required_minimum_poll_interval_in_seconds: Optional[
            "capo_appconfigdata.types.optional_poll_seconds.OptionalPollSeconds"
        ] = None,
    ) -> "capo_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse":
        """<p>Starts a configuration session used to retrieve a deployed configuration. For more information about this API action and to view example CLI commands that show how to use it with the <a>GetLatestConfiguration</a> API action, see <a href="http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration">Retrieving the configuration</a> in the <i>AppConfig User Guide</i>. </p>

        Args:
            application_identifier: <p>The application ID or the application name.</p>
            environment_identifier: <p>The environment ID or the environment name.</p>
            configuration_profile_identifier: <p>The configuration profile ID or the configuration profile name.</p>
            required_minimum_poll_interval_in_seconds: <p>Sets a constraint on a session. If you specify a value of, for example, 60 seconds, then the client that established the session can't call <a>GetLatestConfiguration</a> more frequently than every 60 seconds.</p>

        Raises:
            capo_appconfigdata.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_appconfigdata.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the service.</p>
            capo_appconfigdata.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfigdata.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_appconfigdata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest]",
        ) -> OperationResponse[
            "capo_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse"
        ]:
            import capo_appconfigdata._operations.app_config_data.start_configuration_session

            output, http_response = (
                capo_appconfigdata._operations.app_config_data.start_configuration_session.start_configuration_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest = {
            "application_identifier": application_identifier,
            "environment_identifier": environment_identifier,
            "configuration_profile_identifier": configuration_profile_identifier,
        }
        if required_minimum_poll_interval_in_seconds is not None:
            input_["required_minimum_poll_interval_in_seconds"] = (
                required_minimum_poll_interval_in_seconds
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncConfigurationSession:
    def __init__(self, service: AsyncAppConfigDataClient) -> None:
        self._service = service

    async def create(
        self,
        application_identifier: "capo_appconfigdata.types.identifier.Identifier",
        environment_identifier: "capo_appconfigdata.types.identifier.Identifier",
        configuration_profile_identifier: "capo_appconfigdata.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppConfigDataClientConfig] = None,
        required_minimum_poll_interval_in_seconds: Optional[
            "capo_appconfigdata.types.optional_poll_seconds.OptionalPollSeconds"
        ] = None,
    ) -> "capo_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse":
        """<p>Starts a configuration session used to retrieve a deployed configuration. For more information about this API action and to view example CLI commands that show how to use it with the <a>GetLatestConfiguration</a> API action, see <a href="http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration">Retrieving the configuration</a> in the <i>AppConfig User Guide</i>. </p>

        Args:
            application_identifier: <p>The application ID or the application name.</p>
            environment_identifier: <p>The environment ID or the environment name.</p>
            configuration_profile_identifier: <p>The configuration profile ID or the configuration profile name.</p>
            required_minimum_poll_interval_in_seconds: <p>Sets a constraint on a session. If you specify a value of, for example, 60 seconds, then the client that established the session can't call <a>GetLatestConfiguration</a> more frequently than every 60 seconds.</p>

        Raises:
            capo_appconfigdata.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_appconfigdata.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the service.</p>
            capo_appconfigdata.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfigdata.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_appconfigdata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse"
        ]:
            import capo_appconfigdata._operations.app_config_data.start_configuration_session

            (
                output,
                http_response,
            ) = await capo_appconfigdata._operations.app_config_data.start_configuration_session.async_start_configuration_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest = {
            "application_identifier": application_identifier,
            "environment_identifier": environment_identifier,
            "configuration_profile_identifier": configuration_profile_identifier,
        }
        if required_minimum_poll_interval_in_seconds is not None:
            input_["required_minimum_poll_interval_in_seconds"] = (
                required_minimum_poll_interval_in_seconds
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
