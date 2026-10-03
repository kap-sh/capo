from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_pca_connector_scep._auth._signers
import capo_pca_connector_scep._auth._sigv4
from capo_pca_connector_scep._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.challenge_arn
    import capo_pca_connector_scep.types.challenge_metadata_summary
    import capo_pca_connector_scep.types.client_token
    import capo_pca_connector_scep.types.connector_arn
    import capo_pca_connector_scep.types.create_challenge_request
    import capo_pca_connector_scep.types.create_challenge_response
    import capo_pca_connector_scep.types.delete_challenge_request
    import capo_pca_connector_scep.types.get_challenge_metadata_request
    import capo_pca_connector_scep.types.get_challenge_metadata_response
    import capo_pca_connector_scep.types.get_challenge_password_request
    import capo_pca_connector_scep.types.get_challenge_password_response
    import capo_pca_connector_scep.types.list_challenge_metadata_request
    import capo_pca_connector_scep.types.list_challenge_metadata_response
    import capo_pca_connector_scep.types.max_results
    import capo_pca_connector_scep.types.next_token
    import capo_pca_connector_scep.types.tags
    from capo_pca_connector_scep._services.async_pca_connector_scep import (
        AsyncPcaConnectorScepClient,
        AsyncPcaConnectorScepClientConfig,
    )
    from capo_pca_connector_scep._services.pca_connector_scep import (
        PcaConnectorScepClient,
        PcaConnectorScepClientConfig,
    )


class ChallengeResource:
    def __init__(self, service: PcaConnectorScepClient) -> None:
        self._service = service

    def create(
        self,
        connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_scep.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_scep.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse":
        """<p>For general-purpose connectors. Creates a <i>challenge password</i> for the specified connector. The SCEP protocol uses a challenge password to authenticate a request before issuing a certificate from a certificate authority (CA). Your SCEP clients include the challenge password as part of their certificate request to Connector for SCEP. To retrieve the connector Amazon Resource Names (ARNs) for the connectors in your account, call <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html">ListConnectors</a>.</p> <p>To create additional challenge passwords for the connector, call <code>CreateChallenge</code> again. We recommend frequently rotating your challenge passwords.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that you want to create a challenge for.</p>
            client_token: <p>Custom string that can be used to distinguish between calls to the <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>
            tags: <p>The key-value pairs to associate with the resource.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_pca_connector_scep.errors.conflict_exception.ConflictException: <p>This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.create_challenge

            output, http_response = (
                capo_pca_connector_scep._operations.pca_connector_scep.create_challenge.create_challenge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest = {
            "connector_arn": connector_arn
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
        challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
    ) -> "capo_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse":
        """<p>Retrieves the metadata for the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata

            output, http_response = (
                capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata.get_challenge_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest = {
            "challenge_arn": challenge_arn
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
        challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge password to delete.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.conflict_exception.ConflictException: <p>This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest]",
        ) -> OperationResponse[None]:
            import capo_pca_connector_scep._operations.pca_connector_scep.delete_challenge

            output, http_response = (
                capo_pca_connector_scep._operations.pca_connector_scep.delete_challenge.delete_challenge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest = {
            "challenge_arn": challenge_arn
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
        connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> "capo_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse":
        """<p>Retrieves the challenge metadata for the specified ARN.</p>

        Args:
            max_results: <p>The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata

            output, http_response = (
                capo_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata.list_challenge_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest = {
            "connector_arn": connector_arn
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

    def get_challenge_password(
        self,
        challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
    ) -> "capo_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse":
        """<p>Retrieves the challenge password for the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_password

            output, http_response = (
                capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_password.get_challenge_password(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest = {
            "challenge_arn": challenge_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncChallengeResource:
    def __init__(self, service: AsyncPcaConnectorScepClient) -> None:
        self._service = service

    async def create(
        self,
        connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_scep.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_scep.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse":
        """<p>For general-purpose connectors. Creates a <i>challenge password</i> for the specified connector. The SCEP protocol uses a challenge password to authenticate a request before issuing a certificate from a certificate authority (CA). Your SCEP clients include the challenge password as part of their certificate request to Connector for SCEP. To retrieve the connector Amazon Resource Names (ARNs) for the connectors in your account, call <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html">ListConnectors</a>.</p> <p>To create additional challenge passwords for the connector, call <code>CreateChallenge</code> again. We recommend frequently rotating your challenge passwords.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that you want to create a challenge for.</p>
            client_token: <p>Custom string that can be used to distinguish between calls to the <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>
            tags: <p>The key-value pairs to associate with the resource.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_pca_connector_scep.errors.conflict_exception.ConflictException: <p>This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.create_challenge

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.create_challenge.async_create_challenge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest = {
            "connector_arn": connector_arn
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
        challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> "capo_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse":
        """<p>Retrieves the metadata for the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata.async_get_challenge_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest = {
            "challenge_arn": challenge_arn
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
        challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge password to delete.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.conflict_exception.ConflictException: <p>This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_scep._operations.pca_connector_scep.delete_challenge

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.delete_challenge.async_delete_challenge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest = {
            "challenge_arn": challenge_arn
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
        connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> "capo_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse":
        """<p>Retrieves the challenge metadata for the specified ARN.</p>

        Args:
            max_results: <p>The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata.async_list_challenge_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest = {
            "connector_arn": connector_arn
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

    async def get_challenge_password(
        self,
        challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> "capo_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse":
        """<p>Retrieves the challenge password for the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_password

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_password.async_get_challenge_password(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest = {
            "challenge_arn": challenge_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
