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
    import capo_pca_connector_ad.types.connector_arn
    import capo_pca_connector_ad.types.create_service_principal_name_request
    import capo_pca_connector_ad.types.delete_service_principal_name_request
    import capo_pca_connector_ad.types.directory_registration_arn
    import capo_pca_connector_ad.types.get_service_principal_name_request
    import capo_pca_connector_ad.types.get_service_principal_name_response
    import capo_pca_connector_ad.types.list_service_principal_names_request
    import capo_pca_connector_ad.types.list_service_principal_names_response
    import capo_pca_connector_ad.types.max_results
    import capo_pca_connector_ad.types.next_token
    import capo_pca_connector_ad.types.service_principal_name_summary
    from capo_pca_connector_ad._services.async_pca_connector_ad import (
        AsyncPcaConnectorAdClient,
        AsyncPcaConnectorAdClientConfig,
    )
    from capo_pca_connector_ad._services.pca_connector_ad import (
        PcaConnectorAdClient,
        PcaConnectorAdClientConfig,
    )


class ServicePrincipalNameResource:
    def __init__(self, service: PcaConnectorAdClient) -> None:
        self._service = service

    def put(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Creates a service principal name (SPN) for the service account in Active Directory. Kerberos authentication uses SPNs to associate a service instance with a service sign-in account.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>
            client_token: <p>Idempotency token.</p>

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
            req: "OperationRequest[capo_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest]",
        ) -> OperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name.create_service_principal_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest = {
            "directory_registration_arn": directory_registration_arn,
            "connector_arn": connector_arn,
        }
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

    def read(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse":
        """<p>Lists the service principal name that the connector uses to authenticate with Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name.get_service_principal_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest = {
            "directory_registration_arn": directory_registration_arn,
            "connector_arn": connector_arn,
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
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes the service principal name (SPN) used by a connector to authenticate with your Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest]",
        ) -> OperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name.delete_service_principal_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest = {
            "directory_registration_arn": directory_registration_arn,
            "connector_arn": connector_arn,
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
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse":
        """<p>Lists the service principal names that the connector uses to authenticate with Active Directory.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
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
            req: "OperationRequest[capo_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names.list_service_principal_names(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest = {
            "directory_registration_arn": directory_registration_arn
        }
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


class AsyncServicePrincipalNameResource:
    def __init__(self, service: AsyncPcaConnectorAdClient) -> None:
        self._service = service

    async def put(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Creates a service principal name (SPN) for the service account in Active Directory. Kerberos authentication uses SPNs to associate a service instance with a service sign-in account.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>
            client_token: <p>Idempotency token.</p>

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
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name.async_create_service_principal_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest = {
            "directory_registration_arn": directory_registration_arn,
            "connector_arn": connector_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

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
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse":
        """<p>Lists the service principal name that the connector uses to authenticate with Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name.async_get_service_principal_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest = {
            "directory_registration_arn": directory_registration_arn,
            "connector_arn": connector_arn,
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
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes the service principal name (SPN) used by a connector to authenticate with your Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name.async_delete_service_principal_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest = {
            "directory_registration_arn": directory_registration_arn,
            "connector_arn": connector_arn,
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
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse":
        """<p>Lists the service principal names that the connector uses to authenticate with Active Directory.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
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
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names.async_list_service_principal_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest = {
            "directory_registration_arn": directory_registration_arn
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
