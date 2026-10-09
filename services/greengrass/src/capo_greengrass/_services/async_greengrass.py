"""Generated from Smithy shape ``com.amazonaws.greengrass#Greengrass``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_greengrass._auth._signers
import capo_greengrass._auth._sigv4
from capo_greengrass._auth._identity import Credentials
from capo_greengrass._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_greengrass._auth._zapros_handler import AuthMiddleware
from capo_greengrass._services._aws_config import aaws_config
from capo_greengrass._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_greengrass.types.__boolean
    import capo_greengrass.types.__list_of__string
    import capo_greengrass.types.__list_of_connectivity_info
    import capo_greengrass.types.__list_of_connector
    import capo_greengrass.types.__list_of_core
    import capo_greengrass.types.__list_of_device
    import capo_greengrass.types.__list_of_function
    import capo_greengrass.types.__list_of_logger
    import capo_greengrass.types.__list_of_resource
    import capo_greengrass.types.__list_of_subscription
    import capo_greengrass.types.__string
    import capo_greengrass.types.associate_role_to_group_request
    import capo_greengrass.types.associate_role_to_group_response
    import capo_greengrass.types.associate_service_role_to_account_request
    import capo_greengrass.types.associate_service_role_to_account_response
    import capo_greengrass.types.connector_definition_version
    import capo_greengrass.types.core_definition_version
    import capo_greengrass.types.create_connector_definition_request
    import capo_greengrass.types.create_connector_definition_response
    import capo_greengrass.types.create_connector_definition_version_request
    import capo_greengrass.types.create_connector_definition_version_response
    import capo_greengrass.types.create_core_definition_request
    import capo_greengrass.types.create_core_definition_response
    import capo_greengrass.types.create_core_definition_version_request
    import capo_greengrass.types.create_core_definition_version_response
    import capo_greengrass.types.create_deployment_request
    import capo_greengrass.types.create_deployment_response
    import capo_greengrass.types.create_device_definition_request
    import capo_greengrass.types.create_device_definition_response
    import capo_greengrass.types.create_device_definition_version_request
    import capo_greengrass.types.create_device_definition_version_response
    import capo_greengrass.types.create_function_definition_request
    import capo_greengrass.types.create_function_definition_response
    import capo_greengrass.types.create_function_definition_version_request
    import capo_greengrass.types.create_function_definition_version_response
    import capo_greengrass.types.create_group_certificate_authority_request
    import capo_greengrass.types.create_group_certificate_authority_response
    import capo_greengrass.types.create_group_request
    import capo_greengrass.types.create_group_response
    import capo_greengrass.types.create_group_version_request
    import capo_greengrass.types.create_group_version_response
    import capo_greengrass.types.create_logger_definition_request
    import capo_greengrass.types.create_logger_definition_response
    import capo_greengrass.types.create_logger_definition_version_request
    import capo_greengrass.types.create_logger_definition_version_response
    import capo_greengrass.types.create_resource_definition_request
    import capo_greengrass.types.create_resource_definition_response
    import capo_greengrass.types.create_resource_definition_version_request
    import capo_greengrass.types.create_resource_definition_version_response
    import capo_greengrass.types.create_software_update_job_request
    import capo_greengrass.types.create_software_update_job_response
    import capo_greengrass.types.create_subscription_definition_request
    import capo_greengrass.types.create_subscription_definition_response
    import capo_greengrass.types.create_subscription_definition_version_request
    import capo_greengrass.types.create_subscription_definition_version_response
    import capo_greengrass.types.delete_connector_definition_request
    import capo_greengrass.types.delete_connector_definition_response
    import capo_greengrass.types.delete_core_definition_request
    import capo_greengrass.types.delete_core_definition_response
    import capo_greengrass.types.delete_device_definition_request
    import capo_greengrass.types.delete_device_definition_response
    import capo_greengrass.types.delete_function_definition_request
    import capo_greengrass.types.delete_function_definition_response
    import capo_greengrass.types.delete_group_request
    import capo_greengrass.types.delete_group_response
    import capo_greengrass.types.delete_logger_definition_request
    import capo_greengrass.types.delete_logger_definition_response
    import capo_greengrass.types.delete_resource_definition_request
    import capo_greengrass.types.delete_resource_definition_response
    import capo_greengrass.types.delete_subscription_definition_request
    import capo_greengrass.types.delete_subscription_definition_response
    import capo_greengrass.types.deployment_type
    import capo_greengrass.types.device_definition_version
    import capo_greengrass.types.disassociate_role_from_group_request
    import capo_greengrass.types.disassociate_role_from_group_response
    import capo_greengrass.types.disassociate_service_role_from_account_request
    import capo_greengrass.types.disassociate_service_role_from_account_response
    import capo_greengrass.types.function_default_config
    import capo_greengrass.types.function_definition_version
    import capo_greengrass.types.get_associated_role_request
    import capo_greengrass.types.get_associated_role_response
    import capo_greengrass.types.get_bulk_deployment_status_request
    import capo_greengrass.types.get_bulk_deployment_status_response
    import capo_greengrass.types.get_connectivity_info_request
    import capo_greengrass.types.get_connectivity_info_response
    import capo_greengrass.types.get_connector_definition_request
    import capo_greengrass.types.get_connector_definition_response
    import capo_greengrass.types.get_connector_definition_version_request
    import capo_greengrass.types.get_connector_definition_version_response
    import capo_greengrass.types.get_core_definition_request
    import capo_greengrass.types.get_core_definition_response
    import capo_greengrass.types.get_core_definition_version_request
    import capo_greengrass.types.get_core_definition_version_response
    import capo_greengrass.types.get_deployment_status_request
    import capo_greengrass.types.get_deployment_status_response
    import capo_greengrass.types.get_device_definition_request
    import capo_greengrass.types.get_device_definition_response
    import capo_greengrass.types.get_device_definition_version_request
    import capo_greengrass.types.get_device_definition_version_response
    import capo_greengrass.types.get_function_definition_request
    import capo_greengrass.types.get_function_definition_response
    import capo_greengrass.types.get_function_definition_version_request
    import capo_greengrass.types.get_function_definition_version_response
    import capo_greengrass.types.get_group_certificate_authority_request
    import capo_greengrass.types.get_group_certificate_authority_response
    import capo_greengrass.types.get_group_certificate_configuration_request
    import capo_greengrass.types.get_group_certificate_configuration_response
    import capo_greengrass.types.get_group_request
    import capo_greengrass.types.get_group_response
    import capo_greengrass.types.get_group_version_request
    import capo_greengrass.types.get_group_version_response
    import capo_greengrass.types.get_logger_definition_request
    import capo_greengrass.types.get_logger_definition_response
    import capo_greengrass.types.get_logger_definition_version_request
    import capo_greengrass.types.get_logger_definition_version_response
    import capo_greengrass.types.get_resource_definition_request
    import capo_greengrass.types.get_resource_definition_response
    import capo_greengrass.types.get_resource_definition_version_request
    import capo_greengrass.types.get_resource_definition_version_response
    import capo_greengrass.types.get_service_role_for_account_request
    import capo_greengrass.types.get_service_role_for_account_response
    import capo_greengrass.types.get_subscription_definition_request
    import capo_greengrass.types.get_subscription_definition_response
    import capo_greengrass.types.get_subscription_definition_version_request
    import capo_greengrass.types.get_subscription_definition_version_response
    import capo_greengrass.types.get_thing_runtime_configuration_request
    import capo_greengrass.types.get_thing_runtime_configuration_response
    import capo_greengrass.types.group_version
    import capo_greengrass.types.list_bulk_deployment_detailed_reports_request
    import capo_greengrass.types.list_bulk_deployment_detailed_reports_response
    import capo_greengrass.types.list_bulk_deployments_request
    import capo_greengrass.types.list_bulk_deployments_response
    import capo_greengrass.types.list_connector_definition_versions_request
    import capo_greengrass.types.list_connector_definition_versions_response
    import capo_greengrass.types.list_connector_definitions_request
    import capo_greengrass.types.list_connector_definitions_response
    import capo_greengrass.types.list_core_definition_versions_request
    import capo_greengrass.types.list_core_definition_versions_response
    import capo_greengrass.types.list_core_definitions_request
    import capo_greengrass.types.list_core_definitions_response
    import capo_greengrass.types.list_deployments_request
    import capo_greengrass.types.list_deployments_response
    import capo_greengrass.types.list_device_definition_versions_request
    import capo_greengrass.types.list_device_definition_versions_response
    import capo_greengrass.types.list_device_definitions_request
    import capo_greengrass.types.list_device_definitions_response
    import capo_greengrass.types.list_function_definition_versions_request
    import capo_greengrass.types.list_function_definition_versions_response
    import capo_greengrass.types.list_function_definitions_request
    import capo_greengrass.types.list_function_definitions_response
    import capo_greengrass.types.list_group_certificate_authorities_request
    import capo_greengrass.types.list_group_certificate_authorities_response
    import capo_greengrass.types.list_group_versions_request
    import capo_greengrass.types.list_group_versions_response
    import capo_greengrass.types.list_groups_request
    import capo_greengrass.types.list_groups_response
    import capo_greengrass.types.list_logger_definition_versions_request
    import capo_greengrass.types.list_logger_definition_versions_response
    import capo_greengrass.types.list_logger_definitions_request
    import capo_greengrass.types.list_logger_definitions_response
    import capo_greengrass.types.list_resource_definition_versions_request
    import capo_greengrass.types.list_resource_definition_versions_response
    import capo_greengrass.types.list_resource_definitions_request
    import capo_greengrass.types.list_resource_definitions_response
    import capo_greengrass.types.list_subscription_definition_versions_request
    import capo_greengrass.types.list_subscription_definition_versions_response
    import capo_greengrass.types.list_subscription_definitions_request
    import capo_greengrass.types.list_subscription_definitions_response
    import capo_greengrass.types.list_tags_for_resource_request
    import capo_greengrass.types.list_tags_for_resource_response
    import capo_greengrass.types.logger_definition_version
    import capo_greengrass.types.reset_deployments_request
    import capo_greengrass.types.reset_deployments_response
    import capo_greengrass.types.resource_definition_version
    import capo_greengrass.types.s3_url_signer_role
    import capo_greengrass.types.software_to_update
    import capo_greengrass.types.start_bulk_deployment_request
    import capo_greengrass.types.start_bulk_deployment_response
    import capo_greengrass.types.stop_bulk_deployment_request
    import capo_greengrass.types.stop_bulk_deployment_response
    import capo_greengrass.types.subscription_definition_version
    import capo_greengrass.types.tag_resource_request
    import capo_greengrass.types.tags
    import capo_greengrass.types.telemetry_configuration_update
    import capo_greengrass.types.untag_resource_request
    import capo_greengrass.types.update_agent_log_level
    import capo_greengrass.types.update_connectivity_info_request
    import capo_greengrass.types.update_connectivity_info_response
    import capo_greengrass.types.update_connector_definition_request
    import capo_greengrass.types.update_connector_definition_response
    import capo_greengrass.types.update_core_definition_request
    import capo_greengrass.types.update_core_definition_response
    import capo_greengrass.types.update_device_definition_request
    import capo_greengrass.types.update_device_definition_response
    import capo_greengrass.types.update_function_definition_request
    import capo_greengrass.types.update_function_definition_response
    import capo_greengrass.types.update_group_certificate_configuration_request
    import capo_greengrass.types.update_group_certificate_configuration_response
    import capo_greengrass.types.update_group_request
    import capo_greengrass.types.update_group_response
    import capo_greengrass.types.update_logger_definition_request
    import capo_greengrass.types.update_logger_definition_response
    import capo_greengrass.types.update_resource_definition_request
    import capo_greengrass.types.update_resource_definition_response
    import capo_greengrass.types.update_subscription_definition_request
    import capo_greengrass.types.update_subscription_definition_response
    import capo_greengrass.types.update_targets
    import capo_greengrass.types.update_targets_architecture
    import capo_greengrass.types.update_targets_operating_system
    import capo_greengrass.types.update_thing_runtime_configuration_request
    import capo_greengrass.types.update_thing_runtime_configuration_response


class AsyncGreengrassClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncGreengrassClient:
    """A client for the ``Greengrass`` service.

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
        self._config = AsyncGreengrassClientConfig(
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
        self, config_overrides: Optional[AsyncGreengrassClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncGreengrassClientConfig = config_overrides or {}
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

    async def associate_role_to_group(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        role_arn: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.associate_role_to_group_response.AssociateRoleToGroupResponse":
        """Associates a role with a group. Your Greengrass core will use the role to access AWS cloud services. The role's permissions should allow Greengrass core Lambda functions to perform actions against the cloud.

        Args:
            group_id: The ID of the Greengrass group.
            role_arn: The ARN of the role you wish to associate with this group. The existence of the role is not validated.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.associate_role_to_group_request.AssociateRoleToGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.associate_role_to_group_response.AssociateRoleToGroupResponse"
        ]:
            import capo_greengrass._operations.greengrass.associate_role_to_group

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.associate_role_to_group.async_associate_role_to_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.associate_role_to_group_request.AssociateRoleToGroupRequest = {
            "group_id": group_id
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_service_role_to_account(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        role_arn: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.associate_service_role_to_account_response.AssociateServiceRoleToAccountResponse":
        """Associates a role with your account. AWS IoT Greengrass will use the role to access your Lambda functions and AWS IoT resources. This is necessary for deployments to succeed. The role must have at least minimum permissions in the policy ''AWSGreengrassResourceAccessRolePolicy''.

        Args:
            role_arn: The ARN of the service role you wish to associate with your account.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.associate_service_role_to_account_request.AssociateServiceRoleToAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.associate_service_role_to_account_response.AssociateServiceRoleToAccountResponse"
        ]:
            import capo_greengrass._operations.greengrass.associate_service_role_to_account

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.associate_service_role_to_account.async_associate_service_role_to_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.associate_service_role_to_account_request.AssociateServiceRoleToAccountRequest = {}
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_connector_definition(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        initial_version: Optional[
            "capo_greengrass.types.connector_definition_version.ConnectorDefinitionVersion"
        ] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> "capo_greengrass.types.create_connector_definition_response.CreateConnectorDefinitionResponse":
        """Creates a connector definition. You may provide the initial version of the connector definition now or use ''CreateConnectorDefinitionVersion'' at a later time.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            initial_version: Information about the initial version of the connector definition.
            name: The name of the connector definition.
            tags: Tag(s) to add to the new resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_connector_definition_request.CreateConnectorDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_connector_definition_response.CreateConnectorDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_connector_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_connector_definition.async_create_connector_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_connector_definition_request.CreateConnectorDefinitionRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if initial_version is not None:
            input_["initial_version"] = initial_version
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_connector_definition_version(
        self,
        connector_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        connectors: Optional[
            "capo_greengrass.types.__list_of_connector.__listOfConnector"
        ] = None,
    ) -> "capo_greengrass.types.create_connector_definition_version_response.CreateConnectorDefinitionVersionResponse":
        """Creates a version of a connector definition which has already been defined.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            connector_definition_id: The ID of the connector definition.
            connectors: A list of references to connectors in this version, with their corresponding configuration settings.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_connector_definition_version_request.CreateConnectorDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_connector_definition_version_response.CreateConnectorDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_connector_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_connector_definition_version.async_create_connector_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_connector_definition_version_request.CreateConnectorDefinitionVersionRequest = {
            "connector_definition_id": connector_definition_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if connectors is not None:
            input_["connectors"] = connectors

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_core_definition(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        initial_version: Optional[
            "capo_greengrass.types.core_definition_version.CoreDefinitionVersion"
        ] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> "capo_greengrass.types.create_core_definition_response.CreateCoreDefinitionResponse":
        """Creates a core definition. You may provide the initial version of the core definition now or use ''CreateCoreDefinitionVersion'' at a later time. Greengrass groups must each contain exactly one Greengrass core.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            initial_version: Information about the initial version of the core definition.
            name: The name of the core definition.
            tags: Tag(s) to add to the new resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_core_definition_request.CreateCoreDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_core_definition_response.CreateCoreDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_core_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_core_definition.async_create_core_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_core_definition_request.CreateCoreDefinitionRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if initial_version is not None:
            input_["initial_version"] = initial_version
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_core_definition_version(
        self,
        core_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        cores: Optional["capo_greengrass.types.__list_of_core.__listOfCore"] = None,
    ) -> "capo_greengrass.types.create_core_definition_version_response.CreateCoreDefinitionVersionResponse":
        """Creates a version of a core definition that has already been defined. Greengrass groups must each contain exactly one Greengrass core.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            core_definition_id: The ID of the core definition.
            cores: A list of cores in the core definition version.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_core_definition_version_request.CreateCoreDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_core_definition_version_response.CreateCoreDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_core_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_core_definition_version.async_create_core_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_core_definition_version_request.CreateCoreDefinitionVersionRequest = {
            "core_definition_id": core_definition_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if cores is not None:
            input_["cores"] = cores

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_deployment(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        deployment_id: Optional["capo_greengrass.types.__string.__string"] = None,
        deployment_type: Optional[
            "capo_greengrass.types.deployment_type.DeploymentType"
        ] = None,
        group_version_id: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.create_deployment_response.CreateDeploymentResponse":
        """Creates a deployment. ''CreateDeployment'' requests are idempotent with respect to the ''X-Amzn-Client-Token'' token and the request parameters.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            deployment_id: The ID of the deployment if you wish to redeploy a previous deployment.
            deployment_type: The type of deployment. When used for ''CreateDeployment'', only ''NewDeployment'' and ''Redeployment'' are valid.
            group_id: The ID of the Greengrass group.
            group_version_id: The ID of the group version to be deployed.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_deployment_request.CreateDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_deployment_response.CreateDeploymentResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_deployment

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_deployment.async_create_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_deployment_request.CreateDeploymentRequest = {
            "group_id": group_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id
        if deployment_type is not None:
            input_["deployment_type"] = deployment_type
        if group_version_id is not None:
            input_["group_version_id"] = group_version_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_device_definition(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        initial_version: Optional[
            "capo_greengrass.types.device_definition_version.DeviceDefinitionVersion"
        ] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> "capo_greengrass.types.create_device_definition_response.CreateDeviceDefinitionResponse":
        """Creates a device definition. You may provide the initial version of the device definition now or use ''CreateDeviceDefinitionVersion'' at a later time.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            initial_version: Information about the initial version of the device definition.
            name: The name of the device definition.
            tags: Tag(s) to add to the new resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_device_definition_request.CreateDeviceDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_device_definition_response.CreateDeviceDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_device_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_device_definition.async_create_device_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_device_definition_request.CreateDeviceDefinitionRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if initial_version is not None:
            input_["initial_version"] = initial_version
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_device_definition_version(
        self,
        device_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        devices: Optional[
            "capo_greengrass.types.__list_of_device.__listOfDevice"
        ] = None,
    ) -> "capo_greengrass.types.create_device_definition_version_response.CreateDeviceDefinitionVersionResponse":
        """Creates a version of a device definition that has already been defined.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            device_definition_id: The ID of the device definition.
            devices: A list of devices in the definition version.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_device_definition_version_request.CreateDeviceDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_device_definition_version_response.CreateDeviceDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_device_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_device_definition_version.async_create_device_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_device_definition_version_request.CreateDeviceDefinitionVersionRequest = {
            "device_definition_id": device_definition_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if devices is not None:
            input_["devices"] = devices

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_function_definition(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        initial_version: Optional[
            "capo_greengrass.types.function_definition_version.FunctionDefinitionVersion"
        ] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> "capo_greengrass.types.create_function_definition_response.CreateFunctionDefinitionResponse":
        """Creates a Lambda function definition which contains a list of Lambda functions and their configurations to be used in a group. You can create an initial version of the definition by providing a list of Lambda functions and their configurations now, or use ''CreateFunctionDefinitionVersion'' later.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            initial_version: Information about the initial version of the function definition.
            name: The name of the function definition.
            tags: Tag(s) to add to the new resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_function_definition_request.CreateFunctionDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_function_definition_response.CreateFunctionDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_function_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_function_definition.async_create_function_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_function_definition_request.CreateFunctionDefinitionRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if initial_version is not None:
            input_["initial_version"] = initial_version
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_function_definition_version(
        self,
        function_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        default_config: Optional[
            "capo_greengrass.types.function_default_config.FunctionDefaultConfig"
        ] = None,
        functions: Optional[
            "capo_greengrass.types.__list_of_function.__listOfFunction"
        ] = None,
    ) -> "capo_greengrass.types.create_function_definition_version_response.CreateFunctionDefinitionVersionResponse":
        """Creates a version of a Lambda function definition that has already been defined.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            default_config: The default configuration that applies to all Lambda functions in this function definition version. Individual Lambda functions can override these settings.
            function_definition_id: The ID of the Lambda function definition.
            functions: A list of Lambda functions in this function definition version.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_function_definition_version_request.CreateFunctionDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_function_definition_version_response.CreateFunctionDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_function_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_function_definition_version.async_create_function_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_function_definition_version_request.CreateFunctionDefinitionVersionRequest = {
            "function_definition_id": function_definition_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if default_config is not None:
            input_["default_config"] = default_config
        if functions is not None:
            input_["functions"] = functions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_group(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        initial_version: Optional[
            "capo_greengrass.types.group_version.GroupVersion"
        ] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> "capo_greengrass.types.create_group_response.CreateGroupResponse":
        """Creates a group. You may provide the initial version of the group or use ''CreateGroupVersion'' at a later time. Tip: You can use the ''gg_group_setup'' package (https://github.com/awslabs/aws-greengrass-group-setup) as a library or command-line application to create and deploy Greengrass groups.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            initial_version: Information about the initial version of the group.
            name: The name of the group.
            tags: Tag(s) to add to the new resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_group_request.CreateGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_group_response.CreateGroupResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_group

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_group.async_create_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_group_request.CreateGroupRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if initial_version is not None:
            input_["initial_version"] = initial_version
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_group_certificate_authority(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.create_group_certificate_authority_response.CreateGroupCertificateAuthorityResponse":
        """Creates a CA for the group. If a CA already exists, it will rotate the existing CA.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_group_certificate_authority_request.CreateGroupCertificateAuthorityRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_group_certificate_authority_response.CreateGroupCertificateAuthorityResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_group_certificate_authority

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_group_certificate_authority.async_create_group_certificate_authority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_group_certificate_authority_request.CreateGroupCertificateAuthorityRequest = {
            "group_id": group_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_group_version(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        connector_definition_version_arn: Optional[
            "capo_greengrass.types.__string.__string"
        ] = None,
        core_definition_version_arn: Optional[
            "capo_greengrass.types.__string.__string"
        ] = None,
        device_definition_version_arn: Optional[
            "capo_greengrass.types.__string.__string"
        ] = None,
        function_definition_version_arn: Optional[
            "capo_greengrass.types.__string.__string"
        ] = None,
        logger_definition_version_arn: Optional[
            "capo_greengrass.types.__string.__string"
        ] = None,
        resource_definition_version_arn: Optional[
            "capo_greengrass.types.__string.__string"
        ] = None,
        subscription_definition_version_arn: Optional[
            "capo_greengrass.types.__string.__string"
        ] = None,
    ) -> (
        "capo_greengrass.types.create_group_version_response.CreateGroupVersionResponse"
    ):
        """Creates a version of a group which has already been defined.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            connector_definition_version_arn: The ARN of the connector definition version for this group.
            core_definition_version_arn: The ARN of the core definition version for this group.
            device_definition_version_arn: The ARN of the device definition version for this group.
            function_definition_version_arn: The ARN of the function definition version for this group.
            group_id: The ID of the Greengrass group.
            logger_definition_version_arn: The ARN of the logger definition version for this group.
            resource_definition_version_arn: The ARN of the resource definition version for this group.
            subscription_definition_version_arn: The ARN of the subscription definition version for this group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_group_version_request.CreateGroupVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_group_version_response.CreateGroupVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_group_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_group_version.async_create_group_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_group_version_request.CreateGroupVersionRequest = {
            "group_id": group_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if connector_definition_version_arn is not None:
            input_["connector_definition_version_arn"] = (
                connector_definition_version_arn
            )
        if core_definition_version_arn is not None:
            input_["core_definition_version_arn"] = core_definition_version_arn
        if device_definition_version_arn is not None:
            input_["device_definition_version_arn"] = device_definition_version_arn
        if function_definition_version_arn is not None:
            input_["function_definition_version_arn"] = function_definition_version_arn
        if logger_definition_version_arn is not None:
            input_["logger_definition_version_arn"] = logger_definition_version_arn
        if resource_definition_version_arn is not None:
            input_["resource_definition_version_arn"] = resource_definition_version_arn
        if subscription_definition_version_arn is not None:
            input_["subscription_definition_version_arn"] = (
                subscription_definition_version_arn
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_logger_definition(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        initial_version: Optional[
            "capo_greengrass.types.logger_definition_version.LoggerDefinitionVersion"
        ] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> "capo_greengrass.types.create_logger_definition_response.CreateLoggerDefinitionResponse":
        """Creates a logger definition. You may provide the initial version of the logger definition now or use ''CreateLoggerDefinitionVersion'' at a later time.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            initial_version: Information about the initial version of the logger definition.
            name: The name of the logger definition.
            tags: Tag(s) to add to the new resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_logger_definition_request.CreateLoggerDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_logger_definition_response.CreateLoggerDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_logger_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_logger_definition.async_create_logger_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_logger_definition_request.CreateLoggerDefinitionRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if initial_version is not None:
            input_["initial_version"] = initial_version
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_logger_definition_version(
        self,
        logger_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        loggers: Optional[
            "capo_greengrass.types.__list_of_logger.__listOfLogger"
        ] = None,
    ) -> "capo_greengrass.types.create_logger_definition_version_response.CreateLoggerDefinitionVersionResponse":
        """Creates a version of a logger definition that has already been defined.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            logger_definition_id: The ID of the logger definition.
            loggers: A list of loggers.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_logger_definition_version_request.CreateLoggerDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_logger_definition_version_response.CreateLoggerDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_logger_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_logger_definition_version.async_create_logger_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_logger_definition_version_request.CreateLoggerDefinitionVersionRequest = {
            "logger_definition_id": logger_definition_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if loggers is not None:
            input_["loggers"] = loggers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resource_definition(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        initial_version: Optional[
            "capo_greengrass.types.resource_definition_version.ResourceDefinitionVersion"
        ] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> "capo_greengrass.types.create_resource_definition_response.CreateResourceDefinitionResponse":
        """Creates a resource definition which contains a list of resources to be used in a group. You can create an initial version of the definition by providing a list of resources now, or use ''CreateResourceDefinitionVersion'' later.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            initial_version: Information about the initial version of the resource definition.
            name: The name of the resource definition.
            tags: Tag(s) to add to the new resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_resource_definition_request.CreateResourceDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_resource_definition_response.CreateResourceDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_resource_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_resource_definition.async_create_resource_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_resource_definition_request.CreateResourceDefinitionRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if initial_version is not None:
            input_["initial_version"] = initial_version
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resource_definition_version(
        self,
        resource_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        resources: Optional[
            "capo_greengrass.types.__list_of_resource.__listOfResource"
        ] = None,
    ) -> "capo_greengrass.types.create_resource_definition_version_response.CreateResourceDefinitionVersionResponse":
        """Creates a version of a resource definition that has already been defined.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            resource_definition_id: The ID of the resource definition.
            resources: A list of resources.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_resource_definition_version_request.CreateResourceDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_resource_definition_version_response.CreateResourceDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_resource_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_resource_definition_version.async_create_resource_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_resource_definition_version_request.CreateResourceDefinitionVersionRequest = {
            "resource_definition_id": resource_definition_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if resources is not None:
            input_["resources"] = resources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_software_update_job(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        s3_url_signer_role: Optional[
            "capo_greengrass.types.s3_url_signer_role.S3UrlSignerRole"
        ] = None,
        software_to_update: Optional[
            "capo_greengrass.types.software_to_update.SoftwareToUpdate"
        ] = None,
        update_agent_log_level: Optional[
            "capo_greengrass.types.update_agent_log_level.UpdateAgentLogLevel"
        ] = None,
        update_targets: Optional[
            "capo_greengrass.types.update_targets.UpdateTargets"
        ] = None,
        update_targets_architecture: Optional[
            "capo_greengrass.types.update_targets_architecture.UpdateTargetsArchitecture"
        ] = None,
        update_targets_operating_system: Optional[
            "capo_greengrass.types.update_targets_operating_system.UpdateTargetsOperatingSystem"
        ] = None,
    ) -> "capo_greengrass.types.create_software_update_job_response.CreateSoftwareUpdateJobResponse":
        """Creates a software update for a core or group of cores (specified as an IoT thing group.) Use this to update the OTA Agent as well as the Greengrass core software. It makes use of the IoT Jobs feature which provides additional commands to manage a Greengrass core software update job.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_software_update_job_request.CreateSoftwareUpdateJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_software_update_job_response.CreateSoftwareUpdateJobResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_software_update_job

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_software_update_job.async_create_software_update_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_software_update_job_request.CreateSoftwareUpdateJobRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if s3_url_signer_role is not None:
            input_["s3_url_signer_role"] = s3_url_signer_role
        if software_to_update is not None:
            input_["software_to_update"] = software_to_update
        if update_agent_log_level is not None:
            input_["update_agent_log_level"] = update_agent_log_level
        if update_targets is not None:
            input_["update_targets"] = update_targets
        if update_targets_architecture is not None:
            input_["update_targets_architecture"] = update_targets_architecture
        if update_targets_operating_system is not None:
            input_["update_targets_operating_system"] = update_targets_operating_system

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_subscription_definition(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        initial_version: Optional[
            "capo_greengrass.types.subscription_definition_version.SubscriptionDefinitionVersion"
        ] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> "capo_greengrass.types.create_subscription_definition_response.CreateSubscriptionDefinitionResponse":
        """Creates a subscription definition. You may provide the initial version of the subscription definition now or use ''CreateSubscriptionDefinitionVersion'' at a later time.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            initial_version: Information about the initial version of the subscription definition.
            name: The name of the subscription definition.
            tags: Tag(s) to add to the new resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_subscription_definition_request.CreateSubscriptionDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_subscription_definition_response.CreateSubscriptionDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_subscription_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_subscription_definition.async_create_subscription_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_subscription_definition_request.CreateSubscriptionDefinitionRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if initial_version is not None:
            input_["initial_version"] = initial_version
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_subscription_definition_version(
        self,
        subscription_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        subscriptions: Optional[
            "capo_greengrass.types.__list_of_subscription.__listOfSubscription"
        ] = None,
    ) -> "capo_greengrass.types.create_subscription_definition_version_response.CreateSubscriptionDefinitionVersionResponse":
        """Creates a version of a subscription definition which has already been defined.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            subscription_definition_id: The ID of the subscription definition.
            subscriptions: A list of subscriptions.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.create_subscription_definition_version_request.CreateSubscriptionDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.create_subscription_definition_version_response.CreateSubscriptionDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.create_subscription_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.create_subscription_definition_version.async_create_subscription_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.create_subscription_definition_version_request.CreateSubscriptionDefinitionVersionRequest = {
            "subscription_definition_id": subscription_definition_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if subscriptions is not None:
            input_["subscriptions"] = subscriptions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connector_definition(
        self,
        connector_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.delete_connector_definition_response.DeleteConnectorDefinitionResponse":
        """Deletes a connector definition.

        Args:
            connector_definition_id: The ID of the connector definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.delete_connector_definition_request.DeleteConnectorDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.delete_connector_definition_response.DeleteConnectorDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.delete_connector_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.delete_connector_definition.async_delete_connector_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.delete_connector_definition_request.DeleteConnectorDefinitionRequest = {
            "connector_definition_id": connector_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_core_definition(
        self,
        core_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.delete_core_definition_response.DeleteCoreDefinitionResponse":
        """Deletes a core definition.

        Args:
            core_definition_id: The ID of the core definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.delete_core_definition_request.DeleteCoreDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.delete_core_definition_response.DeleteCoreDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.delete_core_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.delete_core_definition.async_delete_core_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.delete_core_definition_request.DeleteCoreDefinitionRequest = {
            "core_definition_id": core_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_device_definition(
        self,
        device_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.delete_device_definition_response.DeleteDeviceDefinitionResponse":
        """Deletes a device definition.

        Args:
            device_definition_id: The ID of the device definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.delete_device_definition_request.DeleteDeviceDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.delete_device_definition_response.DeleteDeviceDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.delete_device_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.delete_device_definition.async_delete_device_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.delete_device_definition_request.DeleteDeviceDefinitionRequest = {
            "device_definition_id": device_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_function_definition(
        self,
        function_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.delete_function_definition_response.DeleteFunctionDefinitionResponse":
        """Deletes a Lambda function definition.

        Args:
            function_definition_id: The ID of the Lambda function definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.delete_function_definition_request.DeleteFunctionDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.delete_function_definition_response.DeleteFunctionDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.delete_function_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.delete_function_definition.async_delete_function_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.delete_function_definition_request.DeleteFunctionDefinitionRequest = {
            "function_definition_id": function_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_group(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.delete_group_response.DeleteGroupResponse":
        """Deletes a group.

        Args:
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.delete_group_request.DeleteGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.delete_group_response.DeleteGroupResponse"
        ]:
            import capo_greengrass._operations.greengrass.delete_group

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.delete_group.async_delete_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.delete_group_request.DeleteGroupRequest = {
            "group_id": group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_logger_definition(
        self,
        logger_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.delete_logger_definition_response.DeleteLoggerDefinitionResponse":
        """Deletes a logger definition.

        Args:
            logger_definition_id: The ID of the logger definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.delete_logger_definition_request.DeleteLoggerDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.delete_logger_definition_response.DeleteLoggerDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.delete_logger_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.delete_logger_definition.async_delete_logger_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.delete_logger_definition_request.DeleteLoggerDefinitionRequest = {
            "logger_definition_id": logger_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_definition(
        self,
        resource_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.delete_resource_definition_response.DeleteResourceDefinitionResponse":
        """Deletes a resource definition.

        Args:
            resource_definition_id: The ID of the resource definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.delete_resource_definition_request.DeleteResourceDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.delete_resource_definition_response.DeleteResourceDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.delete_resource_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.delete_resource_definition.async_delete_resource_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.delete_resource_definition_request.DeleteResourceDefinitionRequest = {
            "resource_definition_id": resource_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_subscription_definition(
        self,
        subscription_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.delete_subscription_definition_response.DeleteSubscriptionDefinitionResponse":
        """Deletes a subscription definition.

        Args:
            subscription_definition_id: The ID of the subscription definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.delete_subscription_definition_request.DeleteSubscriptionDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.delete_subscription_definition_response.DeleteSubscriptionDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.delete_subscription_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.delete_subscription_definition.async_delete_subscription_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.delete_subscription_definition_request.DeleteSubscriptionDefinitionRequest = {
            "subscription_definition_id": subscription_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_role_from_group(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.disassociate_role_from_group_response.DisassociateRoleFromGroupResponse":
        """Disassociates the role from a group.

        Args:
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.disassociate_role_from_group_request.DisassociateRoleFromGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.disassociate_role_from_group_response.DisassociateRoleFromGroupResponse"
        ]:
            import capo_greengrass._operations.greengrass.disassociate_role_from_group

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.disassociate_role_from_group.async_disassociate_role_from_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.disassociate_role_from_group_request.DisassociateRoleFromGroupRequest = {
            "group_id": group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_service_role_from_account(
        self, *, config_overrides: Optional[AsyncGreengrassClientConfig] = None
    ) -> "capo_greengrass.types.disassociate_service_role_from_account_response.DisassociateServiceRoleFromAccountResponse":
        """Disassociates the service role from your account. Without a service role, deployments will not work.

        Raises:
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.disassociate_service_role_from_account_request.DisassociateServiceRoleFromAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.disassociate_service_role_from_account_response.DisassociateServiceRoleFromAccountResponse"
        ]:
            import capo_greengrass._operations.greengrass.disassociate_service_role_from_account

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.disassociate_service_role_from_account.async_disassociate_service_role_from_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.disassociate_service_role_from_account_request.DisassociateServiceRoleFromAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_associated_role(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_associated_role_response.GetAssociatedRoleResponse":
        """Retrieves the role associated with a particular group.

        Args:
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_associated_role_request.GetAssociatedRoleRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_associated_role_response.GetAssociatedRoleResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_associated_role

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_associated_role.async_get_associated_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_associated_role_request.GetAssociatedRoleRequest = {
            "group_id": group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bulk_deployment_status(
        self,
        bulk_deployment_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_bulk_deployment_status_response.GetBulkDeploymentStatusResponse":
        """Returns the status of a bulk deployment.

        Args:
            bulk_deployment_id: The ID of the bulk deployment.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_bulk_deployment_status_request.GetBulkDeploymentStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_bulk_deployment_status_response.GetBulkDeploymentStatusResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_bulk_deployment_status

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_bulk_deployment_status.async_get_bulk_deployment_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_bulk_deployment_status_request.GetBulkDeploymentStatusRequest = {
            "bulk_deployment_id": bulk_deployment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connectivity_info(
        self,
        thing_name: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_connectivity_info_response.GetConnectivityInfoResponse":
        """Retrieves the connectivity information for a core.

        Args:
            thing_name: The thing name.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_connectivity_info_request.GetConnectivityInfoRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_connectivity_info_response.GetConnectivityInfoResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_connectivity_info

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_connectivity_info.async_get_connectivity_info(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_connectivity_info_request.GetConnectivityInfoRequest = {
            "thing_name": thing_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connector_definition(
        self,
        connector_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_connector_definition_response.GetConnectorDefinitionResponse":
        """Retrieves information about a connector definition.

        Args:
            connector_definition_id: The ID of the connector definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_connector_definition_request.GetConnectorDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_connector_definition_response.GetConnectorDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_connector_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_connector_definition.async_get_connector_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_connector_definition_request.GetConnectorDefinitionRequest = {
            "connector_definition_id": connector_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connector_definition_version(
        self,
        connector_definition_id: "capo_greengrass.types.__string.__string",
        connector_definition_version_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.get_connector_definition_version_response.GetConnectorDefinitionVersionResponse":
        """Retrieves information about a connector definition version, including the connectors that the version contains. Connectors are prebuilt modules that interact with local infrastructure, device protocols, AWS, and other cloud services.

        Args:
            connector_definition_id: The ID of the connector definition.
            connector_definition_version_id: The ID of the connector definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListConnectorDefinitionVersions'' requests. If the version is the last one that was associated with a connector definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_connector_definition_version_request.GetConnectorDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_connector_definition_version_response.GetConnectorDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_connector_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_connector_definition_version.async_get_connector_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_connector_definition_version_request.GetConnectorDefinitionVersionRequest = {
            "connector_definition_id": connector_definition_id,
            "connector_definition_version_id": connector_definition_version_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_core_definition(
        self,
        core_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_core_definition_response.GetCoreDefinitionResponse":
        """Retrieves information about a core definition version.

        Args:
            core_definition_id: The ID of the core definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_core_definition_request.GetCoreDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_core_definition_response.GetCoreDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_core_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_core_definition.async_get_core_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_core_definition_request.GetCoreDefinitionRequest = {
            "core_definition_id": core_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_core_definition_version(
        self,
        core_definition_id: "capo_greengrass.types.__string.__string",
        core_definition_version_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_core_definition_version_response.GetCoreDefinitionVersionResponse":
        """Retrieves information about a core definition version.

        Args:
            core_definition_id: The ID of the core definition.
            core_definition_version_id: The ID of the core definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListCoreDefinitionVersions'' requests. If the version is the last one that was associated with a core definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_core_definition_version_request.GetCoreDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_core_definition_version_response.GetCoreDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_core_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_core_definition_version.async_get_core_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_core_definition_version_request.GetCoreDefinitionVersionRequest = {
            "core_definition_id": core_definition_id,
            "core_definition_version_id": core_definition_version_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_deployment_status(
        self,
        deployment_id: "capo_greengrass.types.__string.__string",
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_deployment_status_response.GetDeploymentStatusResponse":
        """Returns the status of a deployment.

        Args:
            deployment_id: The ID of the deployment.
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_deployment_status_request.GetDeploymentStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_deployment_status_response.GetDeploymentStatusResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_deployment_status

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_deployment_status.async_get_deployment_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_deployment_status_request.GetDeploymentStatusRequest = {
            "deployment_id": deployment_id,
            "group_id": group_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_device_definition(
        self,
        device_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_device_definition_response.GetDeviceDefinitionResponse":
        """Retrieves information about a device definition.

        Args:
            device_definition_id: The ID of the device definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_device_definition_request.GetDeviceDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_device_definition_response.GetDeviceDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_device_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_device_definition.async_get_device_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_device_definition_request.GetDeviceDefinitionRequest = {
            "device_definition_id": device_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_device_definition_version(
        self,
        device_definition_id: "capo_greengrass.types.__string.__string",
        device_definition_version_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.get_device_definition_version_response.GetDeviceDefinitionVersionResponse":
        """Retrieves information about a device definition version.

        Args:
            device_definition_id: The ID of the device definition.
            device_definition_version_id: The ID of the device definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListDeviceDefinitionVersions'' requests. If the version is the last one that was associated with a device definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_device_definition_version_request.GetDeviceDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_device_definition_version_response.GetDeviceDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_device_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_device_definition_version.async_get_device_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_device_definition_version_request.GetDeviceDefinitionVersionRequest = {
            "device_definition_id": device_definition_id,
            "device_definition_version_id": device_definition_version_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_function_definition(
        self,
        function_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_function_definition_response.GetFunctionDefinitionResponse":
        """Retrieves information about a Lambda function definition, including its creation time and latest version.

        Args:
            function_definition_id: The ID of the Lambda function definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_function_definition_request.GetFunctionDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_function_definition_response.GetFunctionDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_function_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_function_definition.async_get_function_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_function_definition_request.GetFunctionDefinitionRequest = {
            "function_definition_id": function_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_function_definition_version(
        self,
        function_definition_id: "capo_greengrass.types.__string.__string",
        function_definition_version_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.get_function_definition_version_response.GetFunctionDefinitionVersionResponse":
        """Retrieves information about a Lambda function definition version, including which Lambda functions are included in the version and their configurations.

        Args:
            function_definition_id: The ID of the Lambda function definition.
            function_definition_version_id: The ID of the function definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListFunctionDefinitionVersions'' requests. If the version is the last one that was associated with a function definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_function_definition_version_request.GetFunctionDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_function_definition_version_response.GetFunctionDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_function_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_function_definition_version.async_get_function_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_function_definition_version_request.GetFunctionDefinitionVersionRequest = {
            "function_definition_id": function_definition_id,
            "function_definition_version_id": function_definition_version_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_group_response.GetGroupResponse":
        """Retrieves information about a group.

        Args:
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_group_request.GetGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_group_response.GetGroupResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_group

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_group.async_get_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_group_request.GetGroupRequest = {
            "group_id": group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group_certificate_authority(
        self,
        certificate_authority_id: "capo_greengrass.types.__string.__string",
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_group_certificate_authority_response.GetGroupCertificateAuthorityResponse":
        """Retreives the CA associated with a group. Returns the public key of the CA.

        Args:
            certificate_authority_id: The ID of the certificate authority.
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_group_certificate_authority_request.GetGroupCertificateAuthorityRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_group_certificate_authority_response.GetGroupCertificateAuthorityResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_group_certificate_authority

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_group_certificate_authority.async_get_group_certificate_authority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_group_certificate_authority_request.GetGroupCertificateAuthorityRequest = {
            "certificate_authority_id": certificate_authority_id,
            "group_id": group_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group_certificate_configuration(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_group_certificate_configuration_response.GetGroupCertificateConfigurationResponse":
        """Retrieves the current configuration for the CA used by the group.

        Args:
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_group_certificate_configuration_request.GetGroupCertificateConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_group_certificate_configuration_response.GetGroupCertificateConfigurationResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_group_certificate_configuration

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_group_certificate_configuration.async_get_group_certificate_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_group_certificate_configuration_request.GetGroupCertificateConfigurationRequest = {
            "group_id": group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group_version(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        group_version_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_group_version_response.GetGroupVersionResponse":
        """Retrieves information about a group version.

        Args:
            group_id: The ID of the Greengrass group.
            group_version_id: The ID of the group version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListGroupVersions'' requests. If the version is the last one that was associated with a group, the value also maps to the ''LatestVersion'' property of the corresponding ''GroupInformation'' object.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_group_version_request.GetGroupVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_group_version_response.GetGroupVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_group_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_group_version.async_get_group_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_group_version_request.GetGroupVersionRequest = {
            "group_id": group_id,
            "group_version_id": group_version_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_logger_definition(
        self,
        logger_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_logger_definition_response.GetLoggerDefinitionResponse":
        """Retrieves information about a logger definition.

        Args:
            logger_definition_id: The ID of the logger definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_logger_definition_request.GetLoggerDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_logger_definition_response.GetLoggerDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_logger_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_logger_definition.async_get_logger_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_logger_definition_request.GetLoggerDefinitionRequest = {
            "logger_definition_id": logger_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_logger_definition_version(
        self,
        logger_definition_id: "capo_greengrass.types.__string.__string",
        logger_definition_version_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.get_logger_definition_version_response.GetLoggerDefinitionVersionResponse":
        """Retrieves information about a logger definition version.

        Args:
            logger_definition_id: The ID of the logger definition.
            logger_definition_version_id: The ID of the logger definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListLoggerDefinitionVersions'' requests. If the version is the last one that was associated with a logger definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_logger_definition_version_request.GetLoggerDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_logger_definition_version_response.GetLoggerDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_logger_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_logger_definition_version.async_get_logger_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_logger_definition_version_request.GetLoggerDefinitionVersionRequest = {
            "logger_definition_id": logger_definition_id,
            "logger_definition_version_id": logger_definition_version_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_definition(
        self,
        resource_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_resource_definition_response.GetResourceDefinitionResponse":
        """Retrieves information about a resource definition, including its creation time and latest version.

        Args:
            resource_definition_id: The ID of the resource definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_resource_definition_request.GetResourceDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_resource_definition_response.GetResourceDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_resource_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_resource_definition.async_get_resource_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_resource_definition_request.GetResourceDefinitionRequest = {
            "resource_definition_id": resource_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_definition_version(
        self,
        resource_definition_id: "capo_greengrass.types.__string.__string",
        resource_definition_version_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_resource_definition_version_response.GetResourceDefinitionVersionResponse":
        """Retrieves information about a resource definition version, including which resources are included in the version.

        Args:
            resource_definition_id: The ID of the resource definition.
            resource_definition_version_id: The ID of the resource definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListResourceDefinitionVersions'' requests. If the version is the last one that was associated with a resource definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_resource_definition_version_request.GetResourceDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_resource_definition_version_response.GetResourceDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_resource_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_resource_definition_version.async_get_resource_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_resource_definition_version_request.GetResourceDefinitionVersionRequest = {
            "resource_definition_id": resource_definition_id,
            "resource_definition_version_id": resource_definition_version_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_role_for_account(
        self, *, config_overrides: Optional[AsyncGreengrassClientConfig] = None
    ) -> "capo_greengrass.types.get_service_role_for_account_response.GetServiceRoleForAccountResponse":
        """Retrieves the service role that is attached to your account.

        Raises:
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_service_role_for_account_request.GetServiceRoleForAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_service_role_for_account_response.GetServiceRoleForAccountResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_service_role_for_account

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_service_role_for_account.async_get_service_role_for_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_service_role_for_account_request.GetServiceRoleForAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subscription_definition(
        self,
        subscription_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_subscription_definition_response.GetSubscriptionDefinitionResponse":
        """Retrieves information about a subscription definition.

        Args:
            subscription_definition_id: The ID of the subscription definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_subscription_definition_request.GetSubscriptionDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_subscription_definition_response.GetSubscriptionDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_subscription_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_subscription_definition.async_get_subscription_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_subscription_definition_request.GetSubscriptionDefinitionRequest = {
            "subscription_definition_id": subscription_definition_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subscription_definition_version(
        self,
        subscription_definition_id: "capo_greengrass.types.__string.__string",
        subscription_definition_version_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.get_subscription_definition_version_response.GetSubscriptionDefinitionVersionResponse":
        """Retrieves information about a subscription definition version.

        Args:
            next_token: The token for the next set of results, or ''null'' if there are no additional results.
            subscription_definition_id: The ID of the subscription definition.
            subscription_definition_version_id: The ID of the subscription definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListSubscriptionDefinitionVersions'' requests. If the version is the last one that was associated with a subscription definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_subscription_definition_version_request.GetSubscriptionDefinitionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_subscription_definition_version_response.GetSubscriptionDefinitionVersionResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_subscription_definition_version

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_subscription_definition_version.async_get_subscription_definition_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_subscription_definition_version_request.GetSubscriptionDefinitionVersionRequest = {
            "subscription_definition_id": subscription_definition_id,
            "subscription_definition_version_id": subscription_definition_version_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_thing_runtime_configuration(
        self,
        thing_name: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.get_thing_runtime_configuration_response.GetThingRuntimeConfigurationResponse":
        """Get the runtime configuration of a thing.

        Args:
            thing_name: The thing name.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.get_thing_runtime_configuration_request.GetThingRuntimeConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.get_thing_runtime_configuration_response.GetThingRuntimeConfigurationResponse"
        ]:
            import capo_greengrass._operations.greengrass.get_thing_runtime_configuration

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.get_thing_runtime_configuration.async_get_thing_runtime_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.get_thing_runtime_configuration_request.GetThingRuntimeConfigurationRequest = {
            "thing_name": thing_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_bulk_deployment_detailed_reports(
        self,
        bulk_deployment_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_bulk_deployment_detailed_reports_response.ListBulkDeploymentDetailedReportsResponse":
        """Gets a paginated list of the deployments that have been started in a bulk deployment operation, and their current deployment status.

        Args:
            bulk_deployment_id: The ID of the bulk deployment.
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_bulk_deployment_detailed_reports_request.ListBulkDeploymentDetailedReportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_bulk_deployment_detailed_reports_response.ListBulkDeploymentDetailedReportsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_bulk_deployment_detailed_reports

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_bulk_deployment_detailed_reports.async_list_bulk_deployment_detailed_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_bulk_deployment_detailed_reports_request.ListBulkDeploymentDetailedReportsRequest = {
            "bulk_deployment_id": bulk_deployment_id
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

    async def list_bulk_deployments(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_bulk_deployments_response.ListBulkDeploymentsResponse":
        """Returns a list of bulk deployments.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_bulk_deployments_request.ListBulkDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_bulk_deployments_response.ListBulkDeploymentsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_bulk_deployments

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_bulk_deployments.async_list_bulk_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_bulk_deployments_request.ListBulkDeploymentsRequest = {}
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

    async def list_connector_definitions(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_connector_definitions_response.ListConnectorDefinitionsResponse":
        """Retrieves a list of connector definitions.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_connector_definitions_request.ListConnectorDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_connector_definitions_response.ListConnectorDefinitionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_connector_definitions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_connector_definitions.async_list_connector_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_connector_definitions_request.ListConnectorDefinitionsRequest = {}
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

    async def list_connector_definition_versions(
        self,
        connector_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_connector_definition_versions_response.ListConnectorDefinitionVersionsResponse":
        """Lists the versions of a connector definition, which are containers for connectors. Connectors run on the Greengrass core and contain built-in integration with local infrastructure, device protocols, AWS, and other cloud services.

        Args:
            connector_definition_id: The ID of the connector definition.
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_connector_definition_versions_request.ListConnectorDefinitionVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_connector_definition_versions_response.ListConnectorDefinitionVersionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_connector_definition_versions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_connector_definition_versions.async_list_connector_definition_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_connector_definition_versions_request.ListConnectorDefinitionVersionsRequest = {
            "connector_definition_id": connector_definition_id
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

    async def list_core_definitions(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_core_definitions_response.ListCoreDefinitionsResponse":
        """Retrieves a list of core definitions.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_core_definitions_request.ListCoreDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_core_definitions_response.ListCoreDefinitionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_core_definitions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_core_definitions.async_list_core_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_core_definitions_request.ListCoreDefinitionsRequest = {}
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

    async def list_core_definition_versions(
        self,
        core_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_core_definition_versions_response.ListCoreDefinitionVersionsResponse":
        """Lists the versions of a core definition.

        Args:
            core_definition_id: The ID of the core definition.
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_core_definition_versions_request.ListCoreDefinitionVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_core_definition_versions_response.ListCoreDefinitionVersionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_core_definition_versions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_core_definition_versions.async_list_core_definition_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_core_definition_versions_request.ListCoreDefinitionVersionsRequest = {
            "core_definition_id": core_definition_id
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

    async def list_deployments(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_deployments_response.ListDeploymentsResponse":
        """Returns a history of deployments for the group.

        Args:
            group_id: The ID of the Greengrass group.
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_deployments_request.ListDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_deployments_response.ListDeploymentsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_deployments

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_deployments.async_list_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_deployments_request.ListDeploymentsRequest = {
            "group_id": group_id
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

    async def list_device_definitions(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_device_definitions_response.ListDeviceDefinitionsResponse":
        """Retrieves a list of device definitions.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_device_definitions_request.ListDeviceDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_device_definitions_response.ListDeviceDefinitionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_device_definitions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_device_definitions.async_list_device_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_device_definitions_request.ListDeviceDefinitionsRequest = {}
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

    async def list_device_definition_versions(
        self,
        device_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_device_definition_versions_response.ListDeviceDefinitionVersionsResponse":
        """Lists the versions of a device definition.

        Args:
            device_definition_id: The ID of the device definition.
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_device_definition_versions_request.ListDeviceDefinitionVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_device_definition_versions_response.ListDeviceDefinitionVersionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_device_definition_versions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_device_definition_versions.async_list_device_definition_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_device_definition_versions_request.ListDeviceDefinitionVersionsRequest = {
            "device_definition_id": device_definition_id
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

    async def list_function_definitions(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_function_definitions_response.ListFunctionDefinitionsResponse":
        """Retrieves a list of Lambda function definitions.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_function_definitions_request.ListFunctionDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_function_definitions_response.ListFunctionDefinitionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_function_definitions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_function_definitions.async_list_function_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_function_definitions_request.ListFunctionDefinitionsRequest = {}
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

    async def list_function_definition_versions(
        self,
        function_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_function_definition_versions_response.ListFunctionDefinitionVersionsResponse":
        """Lists the versions of a Lambda function definition.

        Args:
            function_definition_id: The ID of the Lambda function definition.
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_function_definition_versions_request.ListFunctionDefinitionVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_function_definition_versions_response.ListFunctionDefinitionVersionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_function_definition_versions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_function_definition_versions.async_list_function_definition_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_function_definition_versions_request.ListFunctionDefinitionVersionsRequest = {
            "function_definition_id": function_definition_id
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

    async def list_group_certificate_authorities(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.list_group_certificate_authorities_response.ListGroupCertificateAuthoritiesResponse":
        """Retrieves the current CAs for a group.

        Args:
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_group_certificate_authorities_request.ListGroupCertificateAuthoritiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_group_certificate_authorities_response.ListGroupCertificateAuthoritiesResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_group_certificate_authorities

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_group_certificate_authorities.async_list_group_certificate_authorities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_group_certificate_authorities_request.ListGroupCertificateAuthoritiesRequest = {
            "group_id": group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_groups(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_groups_response.ListGroupsResponse":
        """Retrieves a list of groups.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_groups_request.ListGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_groups_response.ListGroupsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_groups

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_groups.async_list_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_groups_request.ListGroupsRequest = {}
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

    async def list_group_versions(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_group_versions_response.ListGroupVersionsResponse":
        """Lists the versions of a group.

        Args:
            group_id: The ID of the Greengrass group.
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_group_versions_request.ListGroupVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_group_versions_response.ListGroupVersionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_group_versions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_group_versions.async_list_group_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_group_versions_request.ListGroupVersionsRequest = {
            "group_id": group_id
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

    async def list_logger_definitions(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_logger_definitions_response.ListLoggerDefinitionsResponse":
        """Retrieves a list of logger definitions.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_logger_definitions_request.ListLoggerDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_logger_definitions_response.ListLoggerDefinitionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_logger_definitions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_logger_definitions.async_list_logger_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_logger_definitions_request.ListLoggerDefinitionsRequest = {}
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

    async def list_logger_definition_versions(
        self,
        logger_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_logger_definition_versions_response.ListLoggerDefinitionVersionsResponse":
        """Lists the versions of a logger definition.

        Args:
            logger_definition_id: The ID of the logger definition.
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_logger_definition_versions_request.ListLoggerDefinitionVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_logger_definition_versions_response.ListLoggerDefinitionVersionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_logger_definition_versions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_logger_definition_versions.async_list_logger_definition_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_logger_definition_versions_request.ListLoggerDefinitionVersionsRequest = {
            "logger_definition_id": logger_definition_id
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

    async def list_resource_definitions(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_resource_definitions_response.ListResourceDefinitionsResponse":
        """Retrieves a list of resource definitions.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_resource_definitions_request.ListResourceDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_resource_definitions_response.ListResourceDefinitionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_resource_definitions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_resource_definitions.async_list_resource_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_resource_definitions_request.ListResourceDefinitionsRequest = {}
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

    async def list_resource_definition_versions(
        self,
        resource_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_resource_definition_versions_response.ListResourceDefinitionVersionsResponse":
        """Lists the versions of a resource definition.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.
            resource_definition_id: The ID of the resource definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_resource_definition_versions_request.ListResourceDefinitionVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_resource_definition_versions_response.ListResourceDefinitionVersionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_resource_definition_versions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_resource_definition_versions.async_list_resource_definition_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_resource_definition_versions_request.ListResourceDefinitionVersionsRequest = {
            "resource_definition_id": resource_definition_id
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

    async def list_subscription_definitions(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_subscription_definitions_response.ListSubscriptionDefinitionsResponse":
        """Retrieves a list of subscription definitions.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.

        Raises:
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_subscription_definitions_request.ListSubscriptionDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_subscription_definitions_response.ListSubscriptionDefinitionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_subscription_definitions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_subscription_definitions.async_list_subscription_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_subscription_definitions_request.ListSubscriptionDefinitionsRequest = {}
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

    async def list_subscription_definition_versions(
        self,
        subscription_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        max_results: Optional["capo_greengrass.types.__string.__string"] = None,
        next_token: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.list_subscription_definition_versions_response.ListSubscriptionDefinitionVersionsResponse":
        """Lists the versions of a subscription definition.

        Args:
            max_results: The maximum number of results to be returned per request.
            next_token: The token for the next set of results, or ''null'' if there are no additional results.
            subscription_definition_id: The ID of the subscription definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_subscription_definition_versions_request.ListSubscriptionDefinitionVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_subscription_definition_versions_response.ListSubscriptionDefinitionVersionsResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_subscription_definition_versions

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_subscription_definition_versions.async_list_subscription_definition_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_subscription_definition_versions_request.ListSubscriptionDefinitionVersionsRequest = {
            "subscription_definition_id": subscription_definition_id
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> "capo_greengrass.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """Retrieves a list of resource tags for a resource arn.

        Args:
            resource_arn: The Amazon Resource Name (ARN) of the resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_greengrass._operations.greengrass.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_deployments(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        force: Optional["capo_greengrass.types.__boolean.__boolean"] = None,
    ) -> "capo_greengrass.types.reset_deployments_response.ResetDeploymentsResponse":
        """Resets a group's deployments.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            force: If true, performs a best-effort only core reset.
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.reset_deployments_request.ResetDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.reset_deployments_response.ResetDeploymentsResponse"
        ]:
            import capo_greengrass._operations.greengrass.reset_deployments

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.reset_deployments.async_reset_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.reset_deployments_request.ResetDeploymentsRequest = {
            "group_id": group_id
        }
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_bulk_deployment(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        amzn_client_token: Optional["capo_greengrass.types.__string.__string"] = None,
        execution_role_arn: Optional["capo_greengrass.types.__string.__string"] = None,
        input_file_uri: Optional["capo_greengrass.types.__string.__string"] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> "capo_greengrass.types.start_bulk_deployment_response.StartBulkDeploymentResponse":
        """Deploys multiple groups in one operation. This action starts the bulk deployment of a specified set of group versions. Each group version deployment will be triggered with an adaptive rate that has a fixed upper limit. We recommend that you include an ''X-Amzn-Client-Token'' token in every ''StartBulkDeployment'' request. These requests are idempotent with respect to the token and the request parameters.

        Args:
            amzn_client_token: A client token used to correlate requests and responses.
            execution_role_arn: The ARN of the execution role to associate with the bulk deployment operation. This IAM role must allow the ''greengrass:CreateDeployment'' action for all group versions that are listed in the input file. This IAM role must have access to the S3 bucket containing the input file.
            input_file_uri: The URI of the input file contained in the S3 bucket. The execution role must have ''getObject'' permissions on this bucket to access the input file. The input file is a JSON-serialized, line delimited file with UTF-8 encoding that provides a list of group and version IDs and the deployment type. This file must be less than 100 MB. Currently, AWS IoT Greengrass supports only ''NewDeployment'' deployment types.
            tags: Tag(s) to add to the new resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.start_bulk_deployment_request.StartBulkDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.start_bulk_deployment_response.StartBulkDeploymentResponse"
        ]:
            import capo_greengrass._operations.greengrass.start_bulk_deployment

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.start_bulk_deployment.async_start_bulk_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.start_bulk_deployment_request.StartBulkDeploymentRequest = {}
        if amzn_client_token is not None:
            input_["amzn_client_token"] = amzn_client_token
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if input_file_uri is not None:
            input_["input_file_uri"] = input_file_uri
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_bulk_deployment(
        self,
        bulk_deployment_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
    ) -> (
        "capo_greengrass.types.stop_bulk_deployment_response.StopBulkDeploymentResponse"
    ):
        """Stops the execution of a bulk deployment. This action returns a status of ''Stopping'' until the deployment is stopped. You cannot start a new bulk deployment while a previous deployment is in the ''Stopping'' state. This action doesn't rollback completed deployments or cancel pending deployments.

        Args:
            bulk_deployment_id: The ID of the bulk deployment.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.stop_bulk_deployment_request.StopBulkDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.stop_bulk_deployment_response.StopBulkDeploymentResponse"
        ]:
            import capo_greengrass._operations.greengrass.stop_bulk_deployment

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.stop_bulk_deployment.async_stop_bulk_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.stop_bulk_deployment_request.StopBulkDeploymentRequest = {
            "bulk_deployment_id": bulk_deployment_id
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
        resource_arn: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        tags: Optional["capo_greengrass.types.tags.Tags"] = None,
    ) -> None:
        """Adds tags to a Greengrass resource. Valid resources are 'Group', 'ConnectorDefinition', 'CoreDefinition', 'DeviceDefinition', 'FunctionDefinition', 'LoggerDefinition', 'SubscriptionDefinition', 'ResourceDefinition', and 'BulkDeployment'.

        Args:
            resource_arn: The Amazon Resource Name (ARN) of the resource.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_greengrass._operations.greengrass.tag_resource

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        tag_keys: Optional[
            "capo_greengrass.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> None:
        """Remove resource tags from a Greengrass Resource.

        Args:
            resource_arn: The Amazon Resource Name (ARN) of the resource.
            tag_keys: An array of tag keys to delete

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_greengrass._operations.greengrass.untag_resource

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connectivity_info(
        self,
        thing_name: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        connectivity_info: Optional[
            "capo_greengrass.types.__list_of_connectivity_info.__listOfConnectivityInfo"
        ] = None,
    ) -> "capo_greengrass.types.update_connectivity_info_response.UpdateConnectivityInfoResponse":
        """Updates the connectivity information for the core. Any devices that belong to the group which has this core will receive this information in order to find the location of the core and connect to it.

        Args:
            connectivity_info: A list of connectivity info.
            thing_name: The thing name.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_connectivity_info_request.UpdateConnectivityInfoRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_connectivity_info_response.UpdateConnectivityInfoResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_connectivity_info

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_connectivity_info.async_update_connectivity_info(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_connectivity_info_request.UpdateConnectivityInfoRequest = {
            "thing_name": thing_name
        }
        if connectivity_info is not None:
            input_["connectivity_info"] = connectivity_info

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connector_definition(
        self,
        connector_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.update_connector_definition_response.UpdateConnectorDefinitionResponse":
        """Updates a connector definition.

        Args:
            connector_definition_id: The ID of the connector definition.
            name: The name of the definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_connector_definition_request.UpdateConnectorDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_connector_definition_response.UpdateConnectorDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_connector_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_connector_definition.async_update_connector_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_connector_definition_request.UpdateConnectorDefinitionRequest = {
            "connector_definition_id": connector_definition_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_core_definition(
        self,
        core_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.update_core_definition_response.UpdateCoreDefinitionResponse":
        """Updates a core definition.

        Args:
            core_definition_id: The ID of the core definition.
            name: The name of the definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_core_definition_request.UpdateCoreDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_core_definition_response.UpdateCoreDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_core_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_core_definition.async_update_core_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_core_definition_request.UpdateCoreDefinitionRequest = {
            "core_definition_id": core_definition_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_device_definition(
        self,
        device_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.update_device_definition_response.UpdateDeviceDefinitionResponse":
        """Updates a device definition.

        Args:
            device_definition_id: The ID of the device definition.
            name: The name of the definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_device_definition_request.UpdateDeviceDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_device_definition_response.UpdateDeviceDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_device_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_device_definition.async_update_device_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_device_definition_request.UpdateDeviceDefinitionRequest = {
            "device_definition_id": device_definition_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_function_definition(
        self,
        function_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.update_function_definition_response.UpdateFunctionDefinitionResponse":
        """Updates a Lambda function definition.

        Args:
            function_definition_id: The ID of the Lambda function definition.
            name: The name of the definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_function_definition_request.UpdateFunctionDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_function_definition_response.UpdateFunctionDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_function_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_function_definition.async_update_function_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_function_definition_request.UpdateFunctionDefinitionRequest = {
            "function_definition_id": function_definition_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_group(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.update_group_response.UpdateGroupResponse":
        """Updates a group.

        Args:
            group_id: The ID of the Greengrass group.
            name: The name of the definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_group_request.UpdateGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_group_response.UpdateGroupResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_group

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_group.async_update_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_group_request.UpdateGroupRequest = {
            "group_id": group_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_group_certificate_configuration(
        self,
        group_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        certificate_expiry_in_milliseconds: Optional[
            "capo_greengrass.types.__string.__string"
        ] = None,
    ) -> "capo_greengrass.types.update_group_certificate_configuration_response.UpdateGroupCertificateConfigurationResponse":
        """Updates the Certificate expiry time for a group.

        Args:
            certificate_expiry_in_milliseconds: The amount of time remaining before the certificate expires, in milliseconds.
            group_id: The ID of the Greengrass group.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_group_certificate_configuration_request.UpdateGroupCertificateConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_group_certificate_configuration_response.UpdateGroupCertificateConfigurationResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_group_certificate_configuration

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_group_certificate_configuration.async_update_group_certificate_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_group_certificate_configuration_request.UpdateGroupCertificateConfigurationRequest = {
            "group_id": group_id
        }
        if certificate_expiry_in_milliseconds is not None:
            input_["certificate_expiry_in_milliseconds"] = (
                certificate_expiry_in_milliseconds
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_logger_definition(
        self,
        logger_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.update_logger_definition_response.UpdateLoggerDefinitionResponse":
        """Updates a logger definition.

        Args:
            logger_definition_id: The ID of the logger definition.
            name: The name of the definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_logger_definition_request.UpdateLoggerDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_logger_definition_response.UpdateLoggerDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_logger_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_logger_definition.async_update_logger_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_logger_definition_request.UpdateLoggerDefinitionRequest = {
            "logger_definition_id": logger_definition_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resource_definition(
        self,
        resource_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.update_resource_definition_response.UpdateResourceDefinitionResponse":
        """Updates a resource definition.

        Args:
            name: The name of the definition.
            resource_definition_id: The ID of the resource definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_resource_definition_request.UpdateResourceDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_resource_definition_response.UpdateResourceDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_resource_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_resource_definition.async_update_resource_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_resource_definition_request.UpdateResourceDefinitionRequest = {
            "resource_definition_id": resource_definition_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_subscription_definition(
        self,
        subscription_definition_id: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        name: Optional["capo_greengrass.types.__string.__string"] = None,
    ) -> "capo_greengrass.types.update_subscription_definition_response.UpdateSubscriptionDefinitionResponse":
        """Updates a subscription definition.

        Args:
            name: The name of the definition.
            subscription_definition_id: The ID of the subscription definition.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_subscription_definition_request.UpdateSubscriptionDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_subscription_definition_response.UpdateSubscriptionDefinitionResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_subscription_definition

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_subscription_definition.async_update_subscription_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_subscription_definition_request.UpdateSubscriptionDefinitionRequest = {
            "subscription_definition_id": subscription_definition_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_thing_runtime_configuration(
        self,
        thing_name: "capo_greengrass.types.__string.__string",
        *,
        config_overrides: Optional[AsyncGreengrassClientConfig] = None,
        telemetry_configuration: Optional[
            "capo_greengrass.types.telemetry_configuration_update.TelemetryConfigurationUpdate"
        ] = None,
    ) -> "capo_greengrass.types.update_thing_runtime_configuration_response.UpdateThingRuntimeConfigurationResponse":
        """Updates the runtime configuration of a thing.

        Args:
            telemetry_configuration: Configuration for telemetry service.
            thing_name: The thing name.

        Raises:
            capo_greengrass.errors.bad_request_exception.BadRequestException: General error information.
            capo_greengrass.errors.internal_server_error_exception.InternalServerErrorException: General error information.
            capo_greengrass.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrass.types.update_thing_runtime_configuration_request.UpdateThingRuntimeConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrass.types.update_thing_runtime_configuration_response.UpdateThingRuntimeConfigurationResponse"
        ]:
            import capo_greengrass._operations.greengrass.update_thing_runtime_configuration

            (
                output,
                http_response,
            ) = await capo_greengrass._operations.greengrass.update_thing_runtime_configuration.async_update_thing_runtime_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrass.types.update_thing_runtime_configuration_request.UpdateThingRuntimeConfigurationRequest = {
            "thing_name": thing_name
        }
        if telemetry_configuration is not None:
            input_["telemetry_configuration"] = telemetry_configuration

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
