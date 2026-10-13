from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_artifact._auth._signers
import capo_artifact._auth._sigv4
from capo_artifact._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_artifact.types.customer_agreement_summary
    import capo_artifact.types.list_customer_agreements_request
    import capo_artifact.types.list_customer_agreements_response
    import capo_artifact.types.max_results_attribute
    import capo_artifact.types.next_token_attribute
    from capo_artifact._services.artifact import ArtifactClient, ArtifactClientConfig
    from capo_artifact._services.async_artifact import (
        AsyncArtifactClient,
        AsyncArtifactClientConfig,
    )


class CustomerAgreementResource:
    def __init__(self, service: ArtifactClient) -> None:
        self._service = service

    def list_customer_agreements(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse":
        """<p>List active customer-agreements applicable to calling identity.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListCustomerAgreements operation
            The ListCustomerAgreements operation returns a collection of customer-agreement resources in the ACTIVE state for the calling credential.

            >>> client.list_customer_agreements()
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse"
        ]:
            import capo_artifact._operations.artifact.list_customer_agreements

            output, http_response = (
                capo_artifact._operations.artifact.list_customer_agreements.list_customer_agreements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCustomerAgreements")
        )
        input_: capo_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest = {}
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


class AsyncCustomerAgreementResource:
    def __init__(self, service: AsyncArtifactClient) -> None:
        self._service = service

    async def list_customer_agreements(
        self,
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse":
        """<p>List active customer-agreements applicable to calling identity.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListCustomerAgreements operation
            The ListCustomerAgreements operation returns a collection of customer-agreement resources in the ACTIVE state for the calling credential.

            >>> await client.list_customer_agreements()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse"
        ]:
            import capo_artifact._operations.artifact.list_customer_agreements

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.list_customer_agreements.async_list_customer_agreements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCustomerAgreements")
        )
        input_: capo_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest = {}
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
