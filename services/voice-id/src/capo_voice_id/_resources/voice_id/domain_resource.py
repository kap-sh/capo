from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_voice_id._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_voice_id.types.client_token_string
    import capo_voice_id.types.create_domain_request
    import capo_voice_id.types.create_domain_response
    import capo_voice_id.types.delete_domain_request
    import capo_voice_id.types.describe_domain_request
    import capo_voice_id.types.describe_domain_response
    import capo_voice_id.types.description
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.domain_name
    import capo_voice_id.types.domain_summary
    import capo_voice_id.types.list_domains_request
    import capo_voice_id.types.list_domains_response
    import capo_voice_id.types.max_results_for_list_domain_fe
    import capo_voice_id.types.next_token
    import capo_voice_id.types.server_side_encryption_configuration
    import capo_voice_id.types.tag_list
    import capo_voice_id.types.update_domain_request
    import capo_voice_id.types.update_domain_response
    from capo_voice_id._services.async_voice_id import (
        AsyncVoiceIDClient,
        AsyncVoiceIDClientConfig,
    )
    from capo_voice_id._services.voice_id import VoiceIDClient, VoiceIDClientConfig


class DomainResource:
    def __init__(self, service: VoiceIDClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "capo_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        description: Optional["capo_voice_id.types.description.Description"] = None,
        client_token: Optional[
            "capo_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional["capo_voice_id.types.tag_list.TagList"] = None,
    ) -> "capo_voice_id.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a domain that contains all Amazon Connect Voice ID data, such as speakers, fraudsters, customer audio, and voiceprints. Every domain is created with a default watchlist that fraudsters can be a part of.</p>

        Args:
            name: <p>The name of the domain.</p>
            description: <p>A brief description of this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/encryption-at-rest.html#encryption-at-rest-voiceid"> Amazon Connect Voice ID encryption at rest</a> for more details on how the KMS key is used. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A list of tags you want added to the domain.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded the service quota. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas">Voice ID Service Quotas</a> and try your request again.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.create_domain_request.CreateDomainRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.create_domain_response.CreateDomainResponse"
        ]:
            import capo_voice_id._operations.voice_id.create_domain

            output, http_response = (
                capo_voice_id._operations.voice_id.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.create_domain_request.CreateDomainRequest = {
            "name": name,
            "server_side_encryption_configuration": server_side_encryption_configuration,
        }
        if description is not None:
            input_["description"] = description
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
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.describe_domain_response.DescribeDomainResponse":
        """<p>Describes the specified domain.</p>

        Args:
            domain_id: <p>The identifier of the domain that you are describing.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.describe_domain_request.DescribeDomainRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.describe_domain_response.DescribeDomainResponse"
        ]:
            import capo_voice_id._operations.voice_id.describe_domain

            output, http_response = (
                capo_voice_id._operations.voice_id.describe_domain.describe_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.describe_domain_request.DescribeDomainRequest = {
            "domain_id": domain_id
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
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        name: "capo_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "capo_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        description: Optional["capo_voice_id.types.description.Description"] = None,
    ) -> "capo_voice_id.types.update_domain_response.UpdateDomainResponse":
        """<p>Updates the specified domain. This API has clobber behavior, and clears and replaces all attributes. If an optional field, such as 'Description' is not provided, it is removed from the domain.</p>

        Args:
            domain_id: <p>The identifier of the domain to be updated.</p>
            name: <p>The name of the domain.</p>
            description: <p>A brief description about this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Changing the domain's associated KMS key immediately triggers an asynchronous process to remove dependency on the old KMS key, such that the domain's data can only be accessed using the new KMS key. The domain's <code>ServerSideEncryptionUpdateDetails</code> contains the details for this process.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.update_domain_request.UpdateDomainRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.update_domain_response.UpdateDomainResponse"
        ]:
            import capo_voice_id._operations.voice_id.update_domain

            output, http_response = (
                capo_voice_id._operations.voice_id.update_domain.update_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.update_domain_request.UpdateDomainRequest = {
            "domain_id": domain_id,
            "name": name,
            "server_side_encryption_configuration": server_side_encryption_configuration,
        }
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
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified domain from Voice ID.</p>

        Args:
            domain_id: <p>The identifier of the domain you want to delete.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.delete_domain_request.DeleteDomainRequest]",
        ) -> OperationResponse[None]:
            import capo_voice_id._operations.voice_id.delete_domain

            output, http_response = (
                capo_voice_id._operations.voice_id.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.delete_domain_request.DeleteDomainRequest = {
            "domain_id": domain_id
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
        config_overrides: Optional[VoiceIDClientConfig] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list_domain_fe.MaxResultsForListDomainFe"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "capo_voice_id.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all the domains in the Amazon Web Services account. </p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.</p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.list_domains_request.ListDomainsRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.list_domains_response.ListDomainsResponse"
        ]:
            import capo_voice_id._operations.voice_id.list_domains

            output, http_response = (
                capo_voice_id._operations.voice_id.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.list_domains_request.ListDomainsRequest = {}
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


class AsyncDomainResource:
    def __init__(self, service: AsyncVoiceIDClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "capo_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        description: Optional["capo_voice_id.types.description.Description"] = None,
        client_token: Optional[
            "capo_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional["capo_voice_id.types.tag_list.TagList"] = None,
    ) -> "capo_voice_id.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a domain that contains all Amazon Connect Voice ID data, such as speakers, fraudsters, customer audio, and voiceprints. Every domain is created with a default watchlist that fraudsters can be a part of.</p>

        Args:
            name: <p>The name of the domain.</p>
            description: <p>A brief description of this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/encryption-at-rest.html#encryption-at-rest-voiceid"> Amazon Connect Voice ID encryption at rest</a> for more details on how the KMS key is used. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A list of tags you want added to the domain.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded the service quota. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas">Voice ID Service Quotas</a> and try your request again.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_voice_id.types.create_domain_request.CreateDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_voice_id.types.create_domain_response.CreateDomainResponse"
        ]:
            import capo_voice_id._operations.voice_id.create_domain

            (
                output,
                http_response,
            ) = await capo_voice_id._operations.voice_id.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.create_domain_request.CreateDomainRequest = {
            "name": name,
            "server_side_encryption_configuration": server_side_encryption_configuration,
        }
        if description is not None:
            input_["description"] = description
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
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.describe_domain_response.DescribeDomainResponse":
        """<p>Describes the specified domain.</p>

        Args:
            domain_id: <p>The identifier of the domain that you are describing.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_voice_id.types.describe_domain_request.DescribeDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_voice_id.types.describe_domain_response.DescribeDomainResponse"
        ]:
            import capo_voice_id._operations.voice_id.describe_domain

            (
                output,
                http_response,
            ) = await capo_voice_id._operations.voice_id.describe_domain.async_describe_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.describe_domain_request.DescribeDomainRequest = {
            "domain_id": domain_id
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
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        name: "capo_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "capo_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        description: Optional["capo_voice_id.types.description.Description"] = None,
    ) -> "capo_voice_id.types.update_domain_response.UpdateDomainResponse":
        """<p>Updates the specified domain. This API has clobber behavior, and clears and replaces all attributes. If an optional field, such as 'Description' is not provided, it is removed from the domain.</p>

        Args:
            domain_id: <p>The identifier of the domain to be updated.</p>
            name: <p>The name of the domain.</p>
            description: <p>A brief description about this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Changing the domain's associated KMS key immediately triggers an asynchronous process to remove dependency on the old KMS key, such that the domain's data can only be accessed using the new KMS key. The domain's <code>ServerSideEncryptionUpdateDetails</code> contains the details for this process.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_voice_id.types.update_domain_request.UpdateDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_voice_id.types.update_domain_response.UpdateDomainResponse"
        ]:
            import capo_voice_id._operations.voice_id.update_domain

            (
                output,
                http_response,
            ) = await capo_voice_id._operations.voice_id.update_domain.async_update_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.update_domain_request.UpdateDomainRequest = {
            "domain_id": domain_id,
            "name": name,
            "server_side_encryption_configuration": server_side_encryption_configuration,
        }
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
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified domain from Voice ID.</p>

        Args:
            domain_id: <p>The identifier of the domain you want to delete.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_voice_id.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_voice_id._operations.voice_id.delete_domain

            (
                output,
                http_response,
            ) = await capo_voice_id._operations.voice_id.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.delete_domain_request.DeleteDomainRequest = {
            "domain_id": domain_id
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
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list_domain_fe.MaxResultsForListDomainFe"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "capo_voice_id.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all the domains in the Amazon Web Services account. </p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.</p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_voice_id.types.list_domains_request.ListDomainsRequest]",
        ) -> AsyncOperationResponse[
            "capo_voice_id.types.list_domains_response.ListDomainsResponse"
        ]:
            import capo_voice_id._operations.voice_id.list_domains

            (
                output,
                http_response,
            ) = await capo_voice_id._operations.voice_id.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_voice_id.types.list_domains_request.ListDomainsRequest = {}
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
