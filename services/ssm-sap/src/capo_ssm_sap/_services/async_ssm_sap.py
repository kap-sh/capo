"""Generated from Smithy shape ``com.amazonaws.ssmsap#SsmSap``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_ssm_sap._auth._signers
import capo_ssm_sap._auth._sigv4
from capo_ssm_sap._auth._identity import Credentials
from capo_ssm_sap._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ssm_sap._auth._zapros_handler import AuthMiddleware
from capo_ssm_sap._pagination import resolve_path as _resolve_path
from capo_ssm_sap._services._aws_config import aaws_config
from capo_ssm_sap._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_ssm_sap.types.app_registry_arn
    import capo_ssm_sap.types.application_credential_list
    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.application_summary
    import capo_ssm_sap.types.application_type
    import capo_ssm_sap.types.arn
    import capo_ssm_sap.types.backint_config
    import capo_ssm_sap.types.component_id
    import capo_ssm_sap.types.component_info_list
    import capo_ssm_sap.types.component_summary
    import capo_ssm_sap.types.configuration_check_definition
    import capo_ssm_sap.types.configuration_check_operation
    import capo_ssm_sap.types.configuration_check_operation_listing_mode
    import capo_ssm_sap.types.configuration_check_type_list
    import capo_ssm_sap.types.connected_entity_type
    import capo_ssm_sap.types.database_id
    import capo_ssm_sap.types.database_summary
    import capo_ssm_sap.types.delete_resource_permission_input
    import capo_ssm_sap.types.delete_resource_permission_output
    import capo_ssm_sap.types.deregister_application_input
    import capo_ssm_sap.types.deregister_application_output
    import capo_ssm_sap.types.filter_list
    import capo_ssm_sap.types.get_application_input
    import capo_ssm_sap.types.get_application_output
    import capo_ssm_sap.types.get_component_input
    import capo_ssm_sap.types.get_component_output
    import capo_ssm_sap.types.get_configuration_check_operation_input
    import capo_ssm_sap.types.get_configuration_check_operation_output
    import capo_ssm_sap.types.get_database_input
    import capo_ssm_sap.types.get_database_output
    import capo_ssm_sap.types.get_operation_input
    import capo_ssm_sap.types.get_operation_output
    import capo_ssm_sap.types.get_resource_permission_input
    import capo_ssm_sap.types.get_resource_permission_output
    import capo_ssm_sap.types.instance_list
    import capo_ssm_sap.types.list_applications_input
    import capo_ssm_sap.types.list_applications_output
    import capo_ssm_sap.types.list_components_input
    import capo_ssm_sap.types.list_components_output
    import capo_ssm_sap.types.list_configuration_check_definitions_input
    import capo_ssm_sap.types.list_configuration_check_definitions_output
    import capo_ssm_sap.types.list_configuration_check_operations_input
    import capo_ssm_sap.types.list_configuration_check_operations_output
    import capo_ssm_sap.types.list_databases_input
    import capo_ssm_sap.types.list_databases_output
    import capo_ssm_sap.types.list_operation_events_input
    import capo_ssm_sap.types.list_operation_events_output
    import capo_ssm_sap.types.list_operations_input
    import capo_ssm_sap.types.list_operations_output
    import capo_ssm_sap.types.list_sub_check_results_input
    import capo_ssm_sap.types.list_sub_check_results_output
    import capo_ssm_sap.types.list_sub_check_rule_results_input
    import capo_ssm_sap.types.list_sub_check_rule_results_output
    import capo_ssm_sap.types.list_tags_for_resource_request
    import capo_ssm_sap.types.list_tags_for_resource_response
    import capo_ssm_sap.types.max_results
    import capo_ssm_sap.types.next_token
    import capo_ssm_sap.types.operation
    import capo_ssm_sap.types.operation_event
    import capo_ssm_sap.types.operation_id
    import capo_ssm_sap.types.permission_action_type
    import capo_ssm_sap.types.put_resource_permission_input
    import capo_ssm_sap.types.put_resource_permission_output
    import capo_ssm_sap.types.register_application_input
    import capo_ssm_sap.types.register_application_output
    import capo_ssm_sap.types.rule_result
    import capo_ssm_sap.types.sap_instance_number
    import capo_ssm_sap.types.sid
    import capo_ssm_sap.types.ssm_sap_arn
    import capo_ssm_sap.types.start_application_input
    import capo_ssm_sap.types.start_application_output
    import capo_ssm_sap.types.start_application_refresh_input
    import capo_ssm_sap.types.start_application_refresh_output
    import capo_ssm_sap.types.start_configuration_checks_input
    import capo_ssm_sap.types.start_configuration_checks_output
    import capo_ssm_sap.types.stop_application_input
    import capo_ssm_sap.types.stop_application_output
    import capo_ssm_sap.types.sub_check_result
    import capo_ssm_sap.types.sub_check_result_id
    import capo_ssm_sap.types.tag_key_list
    import capo_ssm_sap.types.tag_map
    import capo_ssm_sap.types.tag_resource_request
    import capo_ssm_sap.types.tag_resource_response
    import capo_ssm_sap.types.untag_resource_request
    import capo_ssm_sap.types.untag_resource_response
    import capo_ssm_sap.types.update_application_settings_input
    import capo_ssm_sap.types.update_application_settings_output


class AsyncSsmSapClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSsmSapClient:
    """A client for the ``SsmSap`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AsyncSsmSapClientConfig(
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
        self, config_overrides: Optional[AsyncSsmSapClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSsmSapClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def delete_resource_permission(
        self,
        resource_arn: "capo_ssm_sap.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        action_type: Optional[
            "capo_ssm_sap.types.permission_action_type.PermissionActionType"
        ] = None,
        source_resource_arn: Optional["capo_ssm_sap.types.arn.Arn"] = None,
    ) -> "capo_ssm_sap.types.delete_resource_permission_output.DeleteResourcePermissionOutput":
        """<p>Removes permissions associated with the target database.</p>

        Args:
            action_type: <p>Delete or restore the permissions on the target database.</p>
            source_resource_arn: <p>The Amazon Resource Name (ARN) of the source resource.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.delete_resource_permission_input.DeleteResourcePermissionInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.delete_resource_permission_output.DeleteResourcePermissionOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.delete_resource_permission

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.delete_resource_permission.async_delete_resource_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.delete_resource_permission_input.DeleteResourcePermissionInput = {
            "resource_arn": resource_arn
        }
        if action_type is not None:
            input_["action_type"] = action_type
        if source_resource_arn is not None:
            input_["source_resource_arn"] = source_resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_application(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> "capo_ssm_sap.types.deregister_application_output.DeregisterApplicationOutput":
        """<p>Deregister an SAP application with AWS Systems Manager for SAP. This action does not aﬀect the existing setup of your SAP workloads on Amazon EC2.</p>

        Args:
            application_id: <p>The ID of the application.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.unauthorized_exception.UnauthorizedException: <p>The request is not authorized.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.deregister_application_input.DeregisterApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.deregister_application_output.DeregisterApplicationOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.deregister_application

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.deregister_application.async_deregister_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.deregister_application_input.DeregisterApplicationInput = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_application(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        application_id: Optional[
            "capo_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        application_arn: Optional["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"] = None,
        app_registry_arn: Optional[
            "capo_ssm_sap.types.app_registry_arn.AppRegistryArn"
        ] = None,
    ) -> "capo_ssm_sap.types.get_application_output.GetApplicationOutput":
        """<p>Gets an application registered with AWS Systems Manager for SAP. It also returns the components of the application.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            application_arn: <p>The Amazon Resource Name (ARN) of the application. </p>
            app_registry_arn: <p>The Amazon Resource Name (ARN) of the application registry.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.get_application_input.GetApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.get_application_output.GetApplicationOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.get_application

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.get_application_input.GetApplicationInput = {}
        if application_id is not None:
            input_["application_id"] = application_id
        if application_arn is not None:
            input_["application_arn"] = application_arn
        if app_registry_arn is not None:
            input_["app_registry_arn"] = app_registry_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_component(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        component_id: "capo_ssm_sap.types.component_id.ComponentId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> "capo_ssm_sap.types.get_component_output.GetComponentOutput":
        """<p>Gets the component of an application registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            component_id: <p>The ID of the component.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.unauthorized_exception.UnauthorizedException: <p>The request is not authorized.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.get_component_input.GetComponentInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.get_component_output.GetComponentOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.get_component

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.get_component.async_get_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.get_component_input.GetComponentInput = {
            "application_id": application_id,
            "component_id": component_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration_check_operation(
        self,
        operation_id: "capo_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> "capo_ssm_sap.types.get_configuration_check_operation_output.GetConfigurationCheckOperationOutput":
        """<p>Gets the details of a configuration check operation by specifying the operation ID.</p>

        Args:
            operation_id: <p>The ID of the configuration check operation.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.get_configuration_check_operation_input.GetConfigurationCheckOperationInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.get_configuration_check_operation_output.GetConfigurationCheckOperationOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.get_configuration_check_operation

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.get_configuration_check_operation.async_get_configuration_check_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.get_configuration_check_operation_input.GetConfigurationCheckOperationInput = {
            "operation_id": operation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_database(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        application_id: Optional[
            "capo_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        component_id: Optional["capo_ssm_sap.types.component_id.ComponentId"] = None,
        database_id: Optional["capo_ssm_sap.types.database_id.DatabaseId"] = None,
        database_arn: Optional["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"] = None,
    ) -> "capo_ssm_sap.types.get_database_output.GetDatabaseOutput":
        """<p>Gets the SAP HANA database of an application registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            component_id: <p>The ID of the component.</p>
            database_id: <p>The ID of the database.</p>
            database_arn: <p>The Amazon Resource Name (ARN) of the database.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.get_database_input.GetDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.get_database_output.GetDatabaseOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.get_database

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.get_database.async_get_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.get_database_input.GetDatabaseInput = {}
        if application_id is not None:
            input_["application_id"] = application_id
        if component_id is not None:
            input_["component_id"] = component_id
        if database_id is not None:
            input_["database_id"] = database_id
        if database_arn is not None:
            input_["database_arn"] = database_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_operation(
        self,
        operation_id: "capo_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> "capo_ssm_sap.types.get_operation_output.GetOperationOutput":
        """<p>Gets the details of an operation by specifying the operation ID.</p>

        Args:
            operation_id: <p>The ID of the operation.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.get_operation_input.GetOperationInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.get_operation_output.GetOperationOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.get_operation

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.get_operation.async_get_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.get_operation_input.GetOperationInput = {
            "operation_id": operation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_permission(
        self,
        resource_arn: "capo_ssm_sap.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        action_type: Optional[
            "capo_ssm_sap.types.permission_action_type.PermissionActionType"
        ] = None,
    ) -> (
        "capo_ssm_sap.types.get_resource_permission_output.GetResourcePermissionOutput"
    ):
        """<p>Gets permissions associated with the target database.</p>

        Args:
            action_type: <p/>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.get_resource_permission_input.GetResourcePermissionInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.get_resource_permission_output.GetResourcePermissionOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.get_resource_permission

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.get_resource_permission.async_get_resource_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.get_resource_permission_input.GetResourcePermissionInput = {
            "resource_arn": resource_arn
        }
        if action_type is not None:
            input_["action_type"] = action_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_applications(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        filters: Optional["capo_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "capo_ssm_sap.types.list_applications_output.ListApplicationsOutput":
        """<p>Lists all the applications registered with AWS Systems Manager for SAP.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            filters: <p>The filter of name, value, and operator.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_applications_input.ListApplicationsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_applications_output.ListApplicationsOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_applications

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_applications_input.ListApplicationsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        filters: Optional["capo_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "AsyncIterator[capo_ssm_sap.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_components(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        application_id: Optional[
            "capo_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm_sap.types.list_components_output.ListComponentsOutput":
        """<p>Lists all the components registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p> <p>If you do not specify a value for MaxResults, the request returns 50 items per page by default.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.unauthorized_exception.UnauthorizedException: <p>The request is not authorized.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_components_input.ListComponentsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_components_output.ListComponentsOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_components

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_components.async_list_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_components_input.ListComponentsInput = {}
        if application_id is not None:
            input_["application_id"] = application_id
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

    async def iter_list_components(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        application_id: Optional[
            "capo_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm_sap.types.component_summary.ComponentSummary]":
        _token = next_token
        while True:
            _response = await self.list_components(
                config_overrides=config_overrides,
                application_id=application_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("components",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_configuration_check_definitions(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "capo_ssm_sap.types.list_configuration_check_definitions_output.ListConfigurationCheckDefinitionsOutput":
        """<p>Lists all configuration check types supported by AWS Systems Manager for SAP.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_configuration_check_definitions_input.ListConfigurationCheckDefinitionsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_configuration_check_definitions_output.ListConfigurationCheckDefinitionsOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_configuration_check_definitions

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_configuration_check_definitions.async_list_configuration_check_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_configuration_check_definitions_input.ListConfigurationCheckDefinitionsInput = {}
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

    async def iter_list_configuration_check_definitions(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm_sap.types.configuration_check_definition.ConfigurationCheckDefinition]":
        _token = next_token
        while True:
            _response = await self.list_configuration_check_definitions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("configuration_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_configuration_check_operations(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        list_mode: Optional[
            "capo_ssm_sap.types.configuration_check_operation_listing_mode.ConfigurationCheckOperationListingMode"
        ] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["capo_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "capo_ssm_sap.types.list_configuration_check_operations_output.ListConfigurationCheckOperationsOutput":
        """<p>Lists the configuration check operations performed by AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            list_mode: <p>The mode for listing configuration check operations. Defaults to "LATEST_PER_CHECK".</p> <ul> <li> <p>LATEST_PER_CHECK - Will list the latest configuration check operation per check type.</p> </li> <li> <p>ALL_OPERATIONS - Will list all configuration check operations performed on the application.</p> </li> </ul>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>
            filters: <p>The filters of an operation.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_configuration_check_operations_input.ListConfigurationCheckOperationsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_configuration_check_operations_output.ListConfigurationCheckOperationsOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_configuration_check_operations

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_configuration_check_operations.async_list_configuration_check_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_configuration_check_operations_input.ListConfigurationCheckOperationsInput = {
            "application_id": application_id
        }
        if list_mode is not None:
            input_["list_mode"] = list_mode
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_configuration_check_operations(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        list_mode: Optional[
            "capo_ssm_sap.types.configuration_check_operation_listing_mode.ConfigurationCheckOperationListingMode"
        ] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["capo_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "AsyncIterator[capo_ssm_sap.types.configuration_check_operation.ConfigurationCheckOperation]":
        _token = next_token
        while True:
            _response = await self.list_configuration_check_operations(
                application_id,
                config_overrides=config_overrides,
                list_mode=list_mode,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("configuration_check_operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_databases(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        application_id: Optional[
            "capo_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        component_id: Optional["capo_ssm_sap.types.component_id.ComponentId"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm_sap.types.list_databases_output.ListDatabasesOutput":
        """<p>Lists the SAP HANA databases of an application registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            component_id: <p>The ID of the component.</p>
            next_token: <p>The token for the next page of results. </p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value. If you do not specify a value for MaxResults, the request returns 50 items per page by default.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_databases_input.ListDatabasesInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_databases_output.ListDatabasesOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_databases

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_databases.async_list_databases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_databases_input.ListDatabasesInput = {}
        if application_id is not None:
            input_["application_id"] = application_id
        if component_id is not None:
            input_["component_id"] = component_id
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

    async def iter_list_databases(
        self,
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        application_id: Optional[
            "capo_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        component_id: Optional["capo_ssm_sap.types.component_id.ComponentId"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm_sap.types.database_summary.DatabaseSummary]":
        _token = next_token
        while True:
            _response = await self.list_databases(
                config_overrides=config_overrides,
                application_id=application_id,
                component_id=component_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("databases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_operation_events(
        self,
        operation_id: "capo_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["capo_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "capo_ssm_sap.types.list_operation_events_output.ListOperationEventsOutput":
        """<p>Returns a list of operations events.</p> <p>Available parameters include <code>OperationID</code>, as well as optional parameters <code>MaxResults</code>, <code>NextToken</code>, and <code>Filters</code>.</p>

        Args:
            operation_id: <p>The ID of the operation.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p> <p>If you do not specify a value for <code>MaxResults</code>, the request returns 50 items per page by default.</p>
            next_token: <p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>
            filters: <p>Optionally specify filters to narrow the returned operation event items.</p> <p>Valid filter names include <code>status</code>, <code>resourceID</code>, and <code>resourceType</code>. The valid operator for all three filters is <code>Equals</code>.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_operation_events_input.ListOperationEventsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_operation_events_output.ListOperationEventsOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_operation_events

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_operation_events.async_list_operation_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_operation_events_input.ListOperationEventsInput = {
            "operation_id": operation_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_operation_events(
        self,
        operation_id: "capo_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["capo_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "AsyncIterator[capo_ssm_sap.types.operation_event.OperationEvent]":
        _token = next_token
        while True:
            _response = await self.list_operation_events(
                operation_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("operation_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_operations(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["capo_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "capo_ssm_sap.types.list_operations_output.ListOperationsOutput":
        """<p>Lists the operations performed by AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value. If you do not specify a value for MaxResults, the request returns 50 items per page by default.</p>
            next_token: <p>The token for the next page of results. </p>
            filters: <p>The filters of an operation.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_operations_input.ListOperationsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_operations_output.ListOperationsOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_operations

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_operations.async_list_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_operations_input.ListOperationsInput = {
            "application_id": application_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_operations(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["capo_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "AsyncIterator[capo_ssm_sap.types.operation.Operation]":
        _token = next_token
        while True:
            _response = await self.list_operations(
                application_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sub_check_results(
        self,
        operation_id: "capo_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "capo_ssm_sap.types.list_sub_check_results_output.ListSubCheckResultsOutput":
        """<p>Lists the sub-check results of a specified configuration check operation.</p>

        Args:
            operation_id: <p>The ID of the configuration check operation.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_sub_check_results_input.ListSubCheckResultsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_sub_check_results_output.ListSubCheckResultsOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_sub_check_results

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_sub_check_results.async_list_sub_check_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_sub_check_results_input.ListSubCheckResultsInput = {
            "operation_id": operation_id
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

    async def iter_list_sub_check_results(
        self,
        operation_id: "capo_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm_sap.types.sub_check_result.SubCheckResult]":
        _token = next_token
        while True:
            _response = await self.list_sub_check_results(
                operation_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sub_check_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sub_check_rule_results(
        self,
        sub_check_result_id: "capo_ssm_sap.types.sub_check_result_id.SubCheckResultId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "capo_ssm_sap.types.list_sub_check_rule_results_output.ListSubCheckRuleResultsOutput":
        """<p>Lists the rules of a specified sub-check belonging to a configuration check operation.</p>

        Args:
            sub_check_result_id: <p>The ID of the sub check result.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_sub_check_rule_results_input.ListSubCheckRuleResultsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_sub_check_rule_results_output.ListSubCheckRuleResultsOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_sub_check_rule_results

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_sub_check_rule_results.async_list_sub_check_rule_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_sub_check_rule_results_input.ListSubCheckRuleResultsInput = {
            "sub_check_result_id": sub_check_result_id
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

    async def iter_list_sub_check_rule_results(
        self,
        sub_check_result_id: "capo_ssm_sap.types.sub_check_result_id.SubCheckResultId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        max_results: Optional["capo_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm_sap.types.rule_result.RuleResult]":
        _token = next_token
        while True:
            _response = await self.list_sub_check_rule_results(
                sub_check_result_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("rule_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_ssm_sap.types.ssm_sap_arn.SsmSapArn",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> (
        "capo_ssm_sap.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists all tags on an SAP HANA application and/or database registered with AWS Systems Manager for SAP.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_ssm_sap.errors.conflict_exception.ConflictException: <p>A conflict has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ssm_sap._operations.ssm_sap.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_permission(
        self,
        action_type: "capo_ssm_sap.types.permission_action_type.PermissionActionType",
        source_resource_arn: "capo_ssm_sap.types.arn.Arn",
        resource_arn: "capo_ssm_sap.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> (
        "capo_ssm_sap.types.put_resource_permission_output.PutResourcePermissionOutput"
    ):
        """<p>Adds permissions to the target database.</p>

        Args:
            action_type: <p/>
            source_resource_arn: <p/>
            resource_arn: <p/>

        Raises:
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.put_resource_permission_input.PutResourcePermissionInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.put_resource_permission_output.PutResourcePermissionOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.put_resource_permission

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.put_resource_permission.async_put_resource_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.put_resource_permission_input.PutResourcePermissionInput = {
            "action_type": action_type,
            "source_resource_arn": source_resource_arn,
            "resource_arn": resource_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_application(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        application_type: "capo_ssm_sap.types.application_type.ApplicationType",
        instances: "capo_ssm_sap.types.instance_list.InstanceList",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        sap_instance_number: Optional[
            "capo_ssm_sap.types.sap_instance_number.SAPInstanceNumber"
        ] = None,
        sid: Optional["capo_ssm_sap.types.sid.SID"] = None,
        tags: Optional["capo_ssm_sap.types.tag_map.TagMap"] = None,
        credentials: Optional[
            "capo_ssm_sap.types.application_credential_list.ApplicationCredentialList"
        ] = None,
        database_arn: Optional["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"] = None,
        components_info: Optional[
            "capo_ssm_sap.types.component_info_list.ComponentInfoList"
        ] = None,
    ) -> "capo_ssm_sap.types.register_application_output.RegisterApplicationOutput":
        """<p>Register an SAP application with AWS Systems Manager for SAP. You must meet the following requirements before registering. </p> <p>The SAP application you want to register with AWS Systems Manager for SAP is running on Amazon EC2.</p> <p>AWS Systems Manager Agent must be setup on an Amazon EC2 instance along with the required IAM permissions.</p> <p>Amazon EC2 instance(s) must have access to the secrets created in AWS Secrets Manager to manage SAP applications and components.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            application_type: <p>The type of the application.</p>
            instances: <p>The Amazon EC2 instances on which your SAP application is running.</p>
            sap_instance_number: <p>The SAP instance number of the application.</p>
            sid: <p>The System ID of the application.</p>
            tags: <p>The tags to be attached to the SAP application.</p>
            credentials: <p>The credentials of the SAP application.</p>
            database_arn: <p>The Amazon Resource Name of the SAP HANA database.</p>
            components_info: <p>This is an optional parameter for component details to which the SAP ABAP application is attached, such as Web Dispatcher.</p> <p>This is an array of ApplicationComponent objects. You may input 0 to 5 items.</p>

        Raises:
            capo_ssm_sap.errors.conflict_exception.ConflictException: <p>A conflict has occurred.</p>
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.register_application_input.RegisterApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.register_application_output.RegisterApplicationOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.register_application

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.register_application.async_register_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.register_application_input.RegisterApplicationInput = {
            "application_id": application_id,
            "application_type": application_type,
            "instances": instances,
        }
        if sap_instance_number is not None:
            input_["sap_instance_number"] = sap_instance_number
        if sid is not None:
            input_["sid"] = sid
        if tags is not None:
            input_["tags"] = tags
        if credentials is not None:
            input_["credentials"] = credentials
        if database_arn is not None:
            input_["database_arn"] = database_arn
        if components_info is not None:
            input_["components_info"] = components_info

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_application(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> "capo_ssm_sap.types.start_application_output.StartApplicationOutput":
        """<p>Request is an operation which starts an application.</p> <p>Parameter <code>ApplicationId</code> is required.</p>

        Args:
            application_id: <p>The ID of the application.</p>

        Raises:
            capo_ssm_sap.errors.conflict_exception.ConflictException: <p>A conflict has occurred.</p>
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.start_application_input.StartApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.start_application_output.StartApplicationOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.start_application

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.start_application.async_start_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.start_application_input.StartApplicationInput = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_application_refresh(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> "capo_ssm_sap.types.start_application_refresh_output.StartApplicationRefreshOutput":
        """<p>Refreshes a registered application.</p>

        Args:
            application_id: <p>The ID of the application.</p>

        Raises:
            capo_ssm_sap.errors.conflict_exception.ConflictException: <p>A conflict has occurred.</p>
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.unauthorized_exception.UnauthorizedException: <p>The request is not authorized.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.start_application_refresh_input.StartApplicationRefreshInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.start_application_refresh_output.StartApplicationRefreshOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.start_application_refresh

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.start_application_refresh.async_start_application_refresh(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.start_application_refresh_input.StartApplicationRefreshInput = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_configuration_checks(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        configuration_check_ids: Optional[
            "capo_ssm_sap.types.configuration_check_type_list.ConfigurationCheckTypeList"
        ] = None,
    ) -> "capo_ssm_sap.types.start_configuration_checks_output.StartConfigurationChecksOutput":
        """<p>Initiates configuration check operations against a specified application.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            configuration_check_ids: <p>The list of configuration checks to perform.</p>

        Raises:
            capo_ssm_sap.errors.conflict_exception.ConflictException: <p>A conflict has occurred.</p>
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.start_configuration_checks_input.StartConfigurationChecksInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.start_configuration_checks_output.StartConfigurationChecksOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.start_configuration_checks

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.start_configuration_checks.async_start_configuration_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.start_configuration_checks_input.StartConfigurationChecksInput = {
            "application_id": application_id
        }
        if configuration_check_ids is not None:
            input_["configuration_check_ids"] = configuration_check_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_application(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        stop_connected_entity: Optional[
            "capo_ssm_sap.types.connected_entity_type.ConnectedEntityType"
        ] = None,
        include_ec2_instance_shutdown: Optional[bool] = None,
    ) -> "capo_ssm_sap.types.stop_application_output.StopApplicationOutput":
        """<p>Request is an operation to stop an application.</p> <p>Parameter <code>ApplicationId</code> is required. Parameters <code>StopConnectedEntity</code> and <code>IncludeEc2InstanceShutdown</code> are optional.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            stop_connected_entity: <p>Specify the <code>ConnectedEntityType</code>. Accepted type is <code>DBMS</code>.</p> <p>If this parameter is included, the connected DBMS (Database Management System) will be stopped.</p>
            include_ec2_instance_shutdown: <p>Boolean. If included and if set to <code>True</code>, the StopApplication operation will shut down the associated Amazon EC2 instance in addition to the application.</p>

        Raises:
            capo_ssm_sap.errors.conflict_exception.ConflictException: <p>A conflict has occurred.</p>
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.stop_application_input.StopApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.stop_application_output.StopApplicationOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.stop_application

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.stop_application.async_stop_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.stop_application_input.StopApplicationInput = {
            "application_id": application_id
        }
        if stop_connected_entity is not None:
            input_["stop_connected_entity"] = stop_connected_entity
        if include_ec2_instance_shutdown is not None:
            input_["include_ec2_instance_shutdown"] = include_ec2_instance_shutdown

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_ssm_sap.types.ssm_sap_arn.SsmSapArn",
        tags: "capo_ssm_sap.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> "capo_ssm_sap.types.tag_resource_response.TagResourceResponse":
        """<p>Creates tag for a resource by specifying the ARN.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags on a resource.</p>

        Raises:
            capo_ssm_sap.errors.conflict_exception.ConflictException: <p>A conflict has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ssm_sap._operations.ssm_sap.tag_resource

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_ssm_sap.types.ssm_sap_arn.SsmSapArn",
        tag_keys: "capo_ssm_sap.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
    ) -> "capo_ssm_sap.types.untag_resource_response.UntagResourceResponse":
        """<p>Delete the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Adds/updates or removes credentials for applications registered with AWS Systems Manager for SAP.</p>

        Raises:
            capo_ssm_sap.errors.conflict_exception.ConflictException: <p>A conflict has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ssm_sap._operations.ssm_sap.untag_resource

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_application_settings(
        self,
        application_id: "capo_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSsmSapClientConfig] = None,
        credentials_to_add_or_update: Optional[
            "capo_ssm_sap.types.application_credential_list.ApplicationCredentialList"
        ] = None,
        credentials_to_remove: Optional[
            "capo_ssm_sap.types.application_credential_list.ApplicationCredentialList"
        ] = None,
        backint: Optional["capo_ssm_sap.types.backint_config.BackintConfig"] = None,
        database_arn: Optional["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"] = None,
    ) -> "capo_ssm_sap.types.update_application_settings_output.UpdateApplicationSettingsOutput":
        """<p>Updates the settings of an application registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            credentials_to_add_or_update: <p>The credentials to be added or updated.</p>
            credentials_to_remove: <p>The credentials to be removed.</p>
            backint: <p>Installation of AWS Backint Agent for SAP HANA.</p>
            database_arn: <p>The Amazon Resource Name of the SAP HANA database that replaces the current SAP HANA connection with the SAP_ABAP application.</p>

        Raises:
            capo_ssm_sap.errors.conflict_exception.ConflictException: <p>A conflict has occurred.</p>
            capo_ssm_sap.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_ssm_sap.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_ssm_sap.errors.unauthorized_exception.UnauthorizedException: <p>The request is not authorized.</p>
            capo_ssm_sap.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service. </p>
            capo_ssm_sap.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_sap.types.update_application_settings_input.UpdateApplicationSettingsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_sap.types.update_application_settings_output.UpdateApplicationSettingsOutput"
        ]:
            import capo_ssm_sap._operations.ssm_sap.update_application_settings

            (
                output,
                http_response,
            ) = await capo_ssm_sap._operations.ssm_sap.update_application_settings.async_update_application_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_sap.types.update_application_settings_input.UpdateApplicationSettingsInput = {
            "application_id": application_id
        }
        if credentials_to_add_or_update is not None:
            input_["credentials_to_add_or_update"] = credentials_to_add_or_update
        if credentials_to_remove is not None:
            input_["credentials_to_remove"] = credentials_to_remove
        if backint is not None:
            input_["backint"] = backint
        if database_arn is not None:
            input_["database_arn"] = database_arn

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
