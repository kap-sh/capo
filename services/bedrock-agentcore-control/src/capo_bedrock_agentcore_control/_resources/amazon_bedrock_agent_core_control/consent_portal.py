from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.consent_portal_description_type
    import capo_bedrock_agentcore_control.types.consent_portal_identifier
    import capo_bedrock_agentcore_control.types.consent_portal_idp_config
    import capo_bedrock_agentcore_control.types.consent_portal_name_type
    import capo_bedrock_agentcore_control.types.consent_portal_sources
    import capo_bedrock_agentcore_control.types.consent_portal_summary
    import capo_bedrock_agentcore_control.types.create_consent_portal_request
    import capo_bedrock_agentcore_control.types.create_consent_portal_response
    import capo_bedrock_agentcore_control.types.delete_consent_portal_request
    import capo_bedrock_agentcore_control.types.delete_consent_portal_response
    import capo_bedrock_agentcore_control.types.execution_role_arn_type
    import capo_bedrock_agentcore_control.types.get_consent_portal_request
    import capo_bedrock_agentcore_control.types.get_consent_portal_response
    import capo_bedrock_agentcore_control.types.list_consent_portals_request
    import capo_bedrock_agentcore_control.types.list_consent_portals_response
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_consent_portal_request
    import capo_bedrock_agentcore_control.types.update_consent_portal_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class ConsentPortal:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        execution_role_arn: "capo_bedrock_agentcore_control.types.execution_role_arn_type.ExecutionRoleArnType",
        idp_config: "capo_bedrock_agentcore_control.types.consent_portal_idp_config.ConsentPortalIdpConfig",
        name: "capo_bedrock_agentcore_control.types.consent_portal_name_type.ConsentPortalNameType",
        sources: "capo_bedrock_agentcore_control.types.consent_portal_sources.ConsentPortalSources",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_consent_portal_response.CreateConsentPortalResponse":
        """<p>Creates a new consent portal.</p>

        Args:
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.</p>
            idp_config: <p>The identity provider configuration that the consent portal uses to authenticate end users.</p>
            name: <p>The name of the consent portal. The name must be unique within your account.</p>
            sources: <p>The resources served by the consent portal. Currently, we only support type <code>agentcore-gateway</code>.</p>
            description: <p>The description of the consent portal.</p>
            tags: <p>A map of tag keys and values to assign to the consent portal. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_consent_portal_request.CreateConsentPortalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_consent_portal_response.CreateConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_consent_portal

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_consent_portal.create_consent_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConsentPortal")
        )
        input_: capo_bedrock_agentcore_control.types.create_consent_portal_request.CreateConsentPortalRequest = {
            "execution_role_arn": execution_role_arn,
            "idp_config": idp_config,
            "name": name,
            "sources": sources,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_consent_portal_response.GetConsentPortalResponse":
        """<p>Retrieves information about a consent portal.</p>

        Args:
            consent_portal_identifier: <p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_consent_portal_request.GetConsentPortalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_consent_portal_response.GetConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_consent_portal

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_consent_portal.get_consent_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConsentPortal")
        )
        input_: capo_bedrock_agentcore_control.types.get_consent_portal_request.GetConsentPortalRequest = {
            "consent_portal_identifier": consent_portal_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.execution_role_arn_type.ExecutionRoleArnType"
        ] = None,
        idp_config: Optional[
            "capo_bedrock_agentcore_control.types.consent_portal_idp_config.ConsentPortalIdpConfig"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_consent_portal_response.UpdateConsentPortalResponse":
        """<p>Updates an existing consent portal.</p>

        Args:
            consent_portal_identifier: <p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.</p>
            idp_config: <p>The identity provider configuration that the consent portal uses to authenticate end users.</p>
            description: <p>The description of the consent portal.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_consent_portal_request.UpdateConsentPortalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_consent_portal_response.UpdateConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_consent_portal

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_consent_portal.update_consent_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConsentPortal")
        )
        input_: capo_bedrock_agentcore_control.types.update_consent_portal_request.UpdateConsentPortalRequest = {
            "consent_portal_identifier": consent_portal_identifier
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if idp_config is not None:
            input_["idp_config"] = idp_config
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_consent_portal_response.DeleteConsentPortalResponse":
        """<p>Deletes a consent portal.</p>

        Args:
            consent_portal_identifier: <p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_consent_portal_request.DeleteConsentPortalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_consent_portal_response.DeleteConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_consent_portal

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_consent_portal.delete_consent_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConsentPortal")
        )
        input_: capo_bedrock_agentcore_control.types.delete_consent_portal_request.DeleteConsentPortalRequest = {
            "consent_portal_identifier": consent_portal_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_consent_portals(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_consent_portals_response.ListConsentPortalsResponse":
        """<p>Lists all of the consent portals in your account.</p>

        Args:
            max_results: <p>The maximum number of consent portals to return in a single call.</p>
            next_token: <p>A token to retrieve the next page of results. Use the value returned in a previous response to request the next page.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_consent_portals_request.ListConsentPortalsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_consent_portals_response.ListConsentPortalsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_consent_portals

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_consent_portals.list_consent_portals(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConsentPortals")
        )
        input_: capo_bedrock_agentcore_control.types.list_consent_portals_request.ListConsentPortalsRequest = {}
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


class AsyncConsentPortal:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        execution_role_arn: "capo_bedrock_agentcore_control.types.execution_role_arn_type.ExecutionRoleArnType",
        idp_config: "capo_bedrock_agentcore_control.types.consent_portal_idp_config.ConsentPortalIdpConfig",
        name: "capo_bedrock_agentcore_control.types.consent_portal_name_type.ConsentPortalNameType",
        sources: "capo_bedrock_agentcore_control.types.consent_portal_sources.ConsentPortalSources",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_consent_portal_response.CreateConsentPortalResponse":
        """<p>Creates a new consent portal.</p>

        Args:
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.</p>
            idp_config: <p>The identity provider configuration that the consent portal uses to authenticate end users.</p>
            name: <p>The name of the consent portal. The name must be unique within your account.</p>
            sources: <p>The resources served by the consent portal. Currently, we only support type <code>agentcore-gateway</code>.</p>
            description: <p>The description of the consent portal.</p>
            tags: <p>A map of tag keys and values to assign to the consent portal. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_consent_portal_request.CreateConsentPortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_consent_portal_response.CreateConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_consent_portal

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_consent_portal.async_create_consent_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConsentPortal")
        )
        input_: capo_bedrock_agentcore_control.types.create_consent_portal_request.CreateConsentPortalRequest = {
            "execution_role_arn": execution_role_arn,
            "idp_config": idp_config,
            "name": name,
            "sources": sources,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_consent_portal_response.GetConsentPortalResponse":
        """<p>Retrieves information about a consent portal.</p>

        Args:
            consent_portal_identifier: <p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_consent_portal_request.GetConsentPortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_consent_portal_response.GetConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_consent_portal

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_consent_portal.async_get_consent_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConsentPortal")
        )
        input_: capo_bedrock_agentcore_control.types.get_consent_portal_request.GetConsentPortalRequest = {
            "consent_portal_identifier": consent_portal_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.execution_role_arn_type.ExecutionRoleArnType"
        ] = None,
        idp_config: Optional[
            "capo_bedrock_agentcore_control.types.consent_portal_idp_config.ConsentPortalIdpConfig"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_consent_portal_response.UpdateConsentPortalResponse":
        """<p>Updates an existing consent portal.</p>

        Args:
            consent_portal_identifier: <p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.</p>
            idp_config: <p>The identity provider configuration that the consent portal uses to authenticate end users.</p>
            description: <p>The description of the consent portal.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_consent_portal_request.UpdateConsentPortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_consent_portal_response.UpdateConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_consent_portal

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_consent_portal.async_update_consent_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConsentPortal")
        )
        input_: capo_bedrock_agentcore_control.types.update_consent_portal_request.UpdateConsentPortalRequest = {
            "consent_portal_identifier": consent_portal_identifier
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if idp_config is not None:
            input_["idp_config"] = idp_config
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_consent_portal_response.DeleteConsentPortalResponse":
        """<p>Deletes a consent portal.</p>

        Args:
            consent_portal_identifier: <p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_consent_portal_request.DeleteConsentPortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_consent_portal_response.DeleteConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_consent_portal

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_consent_portal.async_delete_consent_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConsentPortal")
        )
        input_: capo_bedrock_agentcore_control.types.delete_consent_portal_request.DeleteConsentPortalRequest = {
            "consent_portal_identifier": consent_portal_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_consent_portals(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_consent_portals_response.ListConsentPortalsResponse":
        """<p>Lists all of the consent portals in your account.</p>

        Args:
            max_results: <p>The maximum number of consent portals to return in a single call.</p>
            next_token: <p>A token to retrieve the next page of results. Use the value returned in a previous response to request the next page.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_consent_portals_request.ListConsentPortalsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_consent_portals_response.ListConsentPortalsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_consent_portals

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_consent_portals.async_list_consent_portals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConsentPortals")
        )
        input_: capo_bedrock_agentcore_control.types.list_consent_portals_request.ListConsentPortalsRequest = {}
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
