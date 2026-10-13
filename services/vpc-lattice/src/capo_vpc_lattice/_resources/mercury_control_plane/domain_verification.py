from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_vpc_lattice._auth._signers
import capo_vpc_lattice._auth._sigv4
from capo_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.delete_domain_verification_request
    import capo_vpc_lattice.types.delete_domain_verification_response
    import capo_vpc_lattice.types.domain_name
    import capo_vpc_lattice.types.domain_verification_identifier
    import capo_vpc_lattice.types.domain_verification_summary
    import capo_vpc_lattice.types.get_domain_verification_request
    import capo_vpc_lattice.types.get_domain_verification_response
    import capo_vpc_lattice.types.list_domain_verifications_request
    import capo_vpc_lattice.types.list_domain_verifications_response
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.start_domain_verification_request
    import capo_vpc_lattice.types.start_domain_verification_response
    import capo_vpc_lattice.types.tag_map
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class DomainVerification:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        domain_name: "capo_vpc_lattice.types.domain_name.DomainName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse":
        """<p> Starts the domain verification process for a custom domain name. </p>

        Args:
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails. </p>
            domain_name: <p> The domain name to verify ownership for. </p>
            tags: <p> The tags for the domain verification. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.start_domain_verification

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.start_domain_verification.start_domain_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartDomainVerification")
        )
        input_: capo_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest = {
            "domain_name": domain_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        domain_verification_identifier: "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse":
        """<p> Retrieves information about a domain verification.ß </p>

        Args:
            domain_verification_identifier: <p> The ID or ARN of the domain verification to retrieve. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_domain_verification

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_domain_verification.get_domain_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDomainVerification")
        )
        input_: capo_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest = {
            "domain_verification_identifier": domain_verification_identifier
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
        domain_verification_identifier: "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse":
        """<p> Deletes the specified domain verification. </p>

        Args:
            domain_verification_identifier: <p> The ID of the domain verification to delete. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_domain_verification

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_domain_verification.delete_domain_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDomainVerification")
        )
        input_: capo_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest = {
            "domain_verification_identifier": domain_verification_identifier
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
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse":
        """<p> Lists the domain verifications. </p>

        Args:
            max_results: <p> The maximum number of results to return. </p>
            next_token: <p> A pagination token for the next page of results. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_domain_verifications

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_domain_verifications.list_domain_verifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDomainVerifications")
        )
        input_: capo_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest = {}
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


class AsyncDomainVerification:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        domain_name: "capo_vpc_lattice.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse":
        """<p> Starts the domain verification process for a custom domain name. </p>

        Args:
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails. </p>
            domain_name: <p> The domain name to verify ownership for. </p>
            tags: <p> The tags for the domain verification. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.start_domain_verification

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.start_domain_verification.async_start_domain_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartDomainVerification")
        )
        input_: capo_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest = {
            "domain_name": domain_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        domain_verification_identifier: "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse":
        """<p> Retrieves information about a domain verification.ß </p>

        Args:
            domain_verification_identifier: <p> The ID or ARN of the domain verification to retrieve. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_domain_verification

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.get_domain_verification.async_get_domain_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDomainVerification")
        )
        input_: capo_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest = {
            "domain_verification_identifier": domain_verification_identifier
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
        domain_verification_identifier: "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse":
        """<p> Deletes the specified domain verification. </p>

        Args:
            domain_verification_identifier: <p> The ID of the domain verification to delete. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_domain_verification

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.delete_domain_verification.async_delete_domain_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDomainVerification")
        )
        input_: capo_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest = {
            "domain_verification_identifier": domain_verification_identifier
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
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse":
        """<p> Lists the domain verifications. </p>

        Args:
            max_results: <p> The maximum number of results to return. </p>
            next_token: <p> A pagination token for the next page of results. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_domain_verifications

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.list_domain_verifications.async_list_domain_verifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDomainVerifications")
        )
        input_: capo_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest = {}
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
