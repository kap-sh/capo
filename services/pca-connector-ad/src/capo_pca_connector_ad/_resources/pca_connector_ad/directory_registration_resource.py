from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_pca_connector_ad._auth._signers
import capo_pca_connector_ad._auth._sigv4
from capo_pca_connector_ad._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.client_token
    import capo_pca_connector_ad.types.create_directory_registration_request
    import capo_pca_connector_ad.types.create_directory_registration_response
    import capo_pca_connector_ad.types.delete_directory_registration_request
    import capo_pca_connector_ad.types.directory_id
    import capo_pca_connector_ad.types.directory_registration_arn
    import capo_pca_connector_ad.types.directory_registration_summary
    import capo_pca_connector_ad.types.get_directory_registration_request
    import capo_pca_connector_ad.types.get_directory_registration_response
    import capo_pca_connector_ad.types.list_directory_registrations_request
    import capo_pca_connector_ad.types.list_directory_registrations_response
    import capo_pca_connector_ad.types.max_results
    import capo_pca_connector_ad.types.next_token
    import capo_pca_connector_ad.types.tags
    from capo_pca_connector_ad._services.async_pca_connector_ad import (
        AsyncPcaConnectorAdClient,
        AsyncPcaConnectorAdClientConfig,
    )
    from capo_pca_connector_ad._services.pca_connector_ad import (
        PcaConnectorAdClient,
        PcaConnectorAdClientConfig,
    )


class DirectoryRegistrationResource:
    def __init__(self, service: PcaConnectorAdClient) -> None:
        self._service = service

    def create(
        self,
        directory_id: "capo_pca_connector_ad.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_ad.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_ad.types.create_directory_registration_response.CreateDirectoryRegistrationResponse":
        """<p>Creates a directory registration that authorizes communication between Amazon Web Services Private CA and an Active Directory</p>

        Args:
            directory_id: <p> The identifier of the Active Directory.</p>
            client_token: <p>Idempotency token.</p>
            tags: <p>Metadata assigned to a directory registration consisting of a key-value pair.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.create_directory_registration_request.CreateDirectoryRegistrationRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_ad.types.create_directory_registration_response.CreateDirectoryRegistrationResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_directory_registration

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.create_directory_registration.create_directory_registration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_directory_registration_request.CreateDirectoryRegistrationRequest = {
            "directory_id": directory_id
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
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_directory_registration_response.GetDirectoryRegistrationResponse":
        """<p>A structure that contains information about your directory registration.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.get_directory_registration_request.GetDirectoryRegistrationRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_ad.types.get_directory_registration_response.GetDirectoryRegistrationResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_directory_registration

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.get_directory_registration.get_directory_registration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_directory_registration_request.GetDirectoryRegistrationRequest = {
            "directory_registration_arn": directory_registration_arn
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
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a directory registration. Deleting a directory registration deauthorizes Amazon Web Services Private CA with the directory. </p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.delete_directory_registration_request.DeleteDirectoryRegistrationRequest]",
        ) -> OperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_directory_registration

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.delete_directory_registration.delete_directory_registration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_directory_registration_request.DeleteDirectoryRegistrationRequest = {
            "directory_registration_arn": directory_registration_arn
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
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_directory_registrations_response.ListDirectoryRegistrationsResponse":
        """<p>Lists the directory registrations that you created by using the <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration</a> action.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.list_directory_registrations_request.ListDirectoryRegistrationsRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_ad.types.list_directory_registrations_response.ListDirectoryRegistrationsResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_directory_registrations

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.list_directory_registrations.list_directory_registrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_directory_registrations_request.ListDirectoryRegistrationsRequest = {}
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


class AsyncDirectoryRegistrationResource:
    def __init__(self, service: AsyncPcaConnectorAdClient) -> None:
        self._service = service

    async def create(
        self,
        directory_id: "capo_pca_connector_ad.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_ad.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_ad.types.create_directory_registration_response.CreateDirectoryRegistrationResponse":
        """<p>Creates a directory registration that authorizes communication between Amazon Web Services Private CA and an Active Directory</p>

        Args:
            directory_id: <p> The identifier of the Active Directory.</p>
            client_token: <p>Idempotency token.</p>
            tags: <p>Metadata assigned to a directory registration consisting of a key-value pair.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.create_directory_registration_request.CreateDirectoryRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.create_directory_registration_response.CreateDirectoryRegistrationResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_directory_registration

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.create_directory_registration.async_create_directory_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_directory_registration_request.CreateDirectoryRegistrationRequest = {
            "directory_id": directory_id
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
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_directory_registration_response.GetDirectoryRegistrationResponse":
        """<p>A structure that contains information about your directory registration.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.get_directory_registration_request.GetDirectoryRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.get_directory_registration_response.GetDirectoryRegistrationResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_directory_registration

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.get_directory_registration.async_get_directory_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_directory_registration_request.GetDirectoryRegistrationRequest = {
            "directory_registration_arn": directory_registration_arn
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
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a directory registration. Deleting a directory registration deauthorizes Amazon Web Services Private CA with the directory. </p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.delete_directory_registration_request.DeleteDirectoryRegistrationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_directory_registration

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.delete_directory_registration.async_delete_directory_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_directory_registration_request.DeleteDirectoryRegistrationRequest = {
            "directory_registration_arn": directory_registration_arn
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
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_directory_registrations_response.ListDirectoryRegistrationsResponse":
        """<p>Lists the directory registrations that you created by using the <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration</a> action.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.list_directory_registrations_request.ListDirectoryRegistrationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.list_directory_registrations_response.ListDirectoryRegistrationsResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_directory_registrations

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.list_directory_registrations.async_list_directory_registrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_directory_registrations_request.ListDirectoryRegistrationsRequest = {}
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
