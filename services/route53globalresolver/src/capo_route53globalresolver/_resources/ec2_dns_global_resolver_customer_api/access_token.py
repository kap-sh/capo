from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_route53globalresolver._auth._signers
import capo_route53globalresolver._auth._sigv4
from capo_route53globalresolver._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_route53globalresolver.types.access_token_item
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.create_access_token_input
    import capo_route53globalresolver.types.create_access_token_output
    import capo_route53globalresolver.types.delete_access_token_input
    import capo_route53globalresolver.types.delete_access_token_output
    import capo_route53globalresolver.types.filters
    import capo_route53globalresolver.types.get_access_token_input
    import capo_route53globalresolver.types.get_access_token_output
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.list_access_tokens_input
    import capo_route53globalresolver.types.list_access_tokens_output
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name_short
    import capo_route53globalresolver.types.tags
    import capo_route53globalresolver.types.update_access_token_input
    import capo_route53globalresolver.types.update_access_token_output
    from capo_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from capo_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class AccessToken:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        expires_at: Optional[
            "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_access_token_output.CreateAccessTokenOutput":
        """<p>Creates an access token for a DNS view. Access tokens provide token-based authentication for DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) connections to the Route 53 Global Resolver.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this token.</p>
            expires_at: <p>The date and time when the token expires. Tokens can have a minimum expiration of 30 days and maximum of 365 days from creation.</p>
            name: <p>A descriptive name for the access token.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.create_access_token_input.CreateAccessTokenInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.create_access_token_output.CreateAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_token

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_token.create_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_route53globalresolver.types.create_access_token_output.CreateAccessTokenOutput",
        ) -> dict[str, Any]:
            import capo_route53globalresolver.types.create_access_token_output

            return capo_route53globalresolver.types.create_access_token_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateAccessToken", redact_output=_redact_output),
        )
        input_: capo_route53globalresolver.types.create_access_token_input.CreateAccessTokenInput = {
            "dns_view_id": dns_view_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if expires_at is not None:
            input_["expires_at"] = expires_at
        if name is not None:
            input_["name"] = name
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
        access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> (
        "capo_route53globalresolver.types.get_access_token_output.GetAccessTokenOutput"
    ):
        """<p>Retrieves information about an access token.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_token_id: <p>ID of the token.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.get_access_token_input.GetAccessTokenInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.get_access_token_output.GetAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_token

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_token.get_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_route53globalresolver.types.get_access_token_output.GetAccessTokenOutput",
        ) -> dict[str, Any]:
            import capo_route53globalresolver.types.get_access_token_output

            return capo_route53globalresolver.types.get_access_token_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAccessToken", redact_output=_redact_output),
        )
        input_: capo_route53globalresolver.types.get_access_token_input.GetAccessTokenInput = {
            "access_token_id": access_token_id
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
        access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        name: "capo_route53globalresolver.types.resource_name_short.ResourceNameShort",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.update_access_token_output.UpdateAccessTokenOutput":
        """<p>Updates the configuration of an access token.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_token_id: <p>The ID of the token.</p>
            name: <p>The new name of the token.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.update_access_token_input.UpdateAccessTokenInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.update_access_token_output.UpdateAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_token

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_token.update_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAccessToken")
        )
        input_: capo_route53globalresolver.types.update_access_token_input.UpdateAccessTokenInput = {
            "access_token_id": access_token_id,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_access_token_output.DeleteAccessTokenOutput":
        """<p>Deletes an access token. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_token_id: <p>The unique identifier of the access token to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.delete_access_token_input.DeleteAccessTokenInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.delete_access_token_output.DeleteAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_token

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_token.delete_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAccessToken")
        )
        input_: capo_route53globalresolver.types.delete_access_token_input.DeleteAccessTokenInput = {
            "access_token_id": access_token_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_access_tokens_output.ListAccessTokensOutput":
        """<p>Lists all access tokens for a DNS view with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            dns_view_id: <p>The ID of the DNS view to list the tokens for.</p>
            filters: <p>Filtering parameters.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.list_access_tokens_input.ListAccessTokensInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.list_access_tokens_output.ListAccessTokensOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_tokens

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_tokens.list_access_tokens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAccessTokens")
        )
        input_: capo_route53globalresolver.types.list_access_tokens_input.ListAccessTokensInput = {
            "dns_view_id": dns_view_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAccessToken:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        expires_at: Optional[
            "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_access_token_output.CreateAccessTokenOutput":
        """<p>Creates an access token for a DNS view. Access tokens provide token-based authentication for DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) connections to the Route 53 Global Resolver.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this token.</p>
            expires_at: <p>The date and time when the token expires. Tokens can have a minimum expiration of 30 days and maximum of 365 days from creation.</p>
            name: <p>A descriptive name for the access token.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_access_token_input.CreateAccessTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_access_token_output.CreateAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_token

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_token.async_create_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_route53globalresolver.types.create_access_token_output.CreateAccessTokenOutput",
        ) -> dict[str, Any]:
            import capo_route53globalresolver.types.create_access_token_output

            return capo_route53globalresolver.types.create_access_token_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateAccessToken", redact_output=_redact_output),
        )
        input_: capo_route53globalresolver.types.create_access_token_input.CreateAccessTokenInput = {
            "dns_view_id": dns_view_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if expires_at is not None:
            input_["expires_at"] = expires_at
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

    async def read(
        self,
        access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> (
        "capo_route53globalresolver.types.get_access_token_output.GetAccessTokenOutput"
    ):
        """<p>Retrieves information about an access token.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_token_id: <p>ID of the token.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_access_token_input.GetAccessTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_access_token_output.GetAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_token

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_token.async_get_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_route53globalresolver.types.get_access_token_output.GetAccessTokenOutput",
        ) -> dict[str, Any]:
            import capo_route53globalresolver.types.get_access_token_output

            return capo_route53globalresolver.types.get_access_token_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAccessToken", redact_output=_redact_output),
        )
        input_: capo_route53globalresolver.types.get_access_token_input.GetAccessTokenInput = {
            "access_token_id": access_token_id
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
        access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        name: "capo_route53globalresolver.types.resource_name_short.ResourceNameShort",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.update_access_token_output.UpdateAccessTokenOutput":
        """<p>Updates the configuration of an access token.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_token_id: <p>The ID of the token.</p>
            name: <p>The new name of the token.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_access_token_input.UpdateAccessTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_access_token_output.UpdateAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_token

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_token.async_update_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAccessToken")
        )
        input_: capo_route53globalresolver.types.update_access_token_input.UpdateAccessTokenInput = {
            "access_token_id": access_token_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_access_token_output.DeleteAccessTokenOutput":
        """<p>Deletes an access token. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_token_id: <p>The unique identifier of the access token to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_access_token_input.DeleteAccessTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_access_token_output.DeleteAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_token

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_token.async_delete_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAccessToken")
        )
        input_: capo_route53globalresolver.types.delete_access_token_input.DeleteAccessTokenInput = {
            "access_token_id": access_token_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_access_tokens_output.ListAccessTokensOutput":
        """<p>Lists all access tokens for a DNS view with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            dns_view_id: <p>The ID of the DNS view to list the tokens for.</p>
            filters: <p>Filtering parameters.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_access_tokens_input.ListAccessTokensInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_access_tokens_output.ListAccessTokensOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_tokens

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_tokens.async_list_access_tokens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAccessTokens")
        )
        input_: capo_route53globalresolver.types.list_access_tokens_input.ListAccessTokensInput = {
            "dns_view_id": dns_view_id
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
