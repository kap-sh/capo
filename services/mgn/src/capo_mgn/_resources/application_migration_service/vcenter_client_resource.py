from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_mgn._auth._signers
import capo_mgn._auth._sigv4
from capo_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mgn.types.delete_vcenter_client_request
    import capo_mgn.types.describe_vcenter_clients_request
    import capo_mgn.types.describe_vcenter_clients_response
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.vcenter_client
    import capo_mgn.types.vcenter_client_id
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class VcenterClientResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def delete(
        self,
        vcenter_client_id: "capo_mgn.types.vcenter_client_id.VcenterClientID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> None:
        """<p>Deletes a given vCenter client by ID.</p>

        Args:
            vcenter_client_id: <p>ID of resource to be deleted.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest]",
        ) -> OperationResponse[None]:
            import capo_mgn._operations.application_migration_service.delete_vcenter_client

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_vcenter_client.delete_vcenter_client(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteVcenterClient")
        )
        input_: capo_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest = {
            "vcenter_client_id": vcenter_client_id
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
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse":
        """<p>Returns a list of the installed vCenter clients.</p>

        Args:
            max_results: <p>Maximum results to be returned in DescribeVcenterClients.</p>
            next_token: <p>Next pagination token to be provided for DescribeVcenterClients.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_vcenter_clients

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_vcenter_clients.describe_vcenter_clients(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_vcenter_clients_response

            return capo_mgn.types.describe_vcenter_clients_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeVcenterClients", redact_output=_redact_output),
        )
        input_: capo_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest = {}
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


class AsyncVcenterClientResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def delete(
        self,
        vcenter_client_id: "capo_mgn.types.vcenter_client_id.VcenterClientID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> None:
        """<p>Deletes a given vCenter client by ID.</p>

        Args:
            vcenter_client_id: <p>ID of resource to be deleted.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_mgn._operations.application_migration_service.delete_vcenter_client

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.delete_vcenter_client.async_delete_vcenter_client(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteVcenterClient")
        )
        input_: capo_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest = {
            "vcenter_client_id": vcenter_client_id
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
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse":
        """<p>Returns a list of the installed vCenter clients.</p>

        Args:
            max_results: <p>Maximum results to be returned in DescribeVcenterClients.</p>
            next_token: <p>Next pagination token to be provided for DescribeVcenterClients.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_vcenter_clients

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.describe_vcenter_clients.async_describe_vcenter_clients(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_vcenter_clients_response

            return capo_mgn.types.describe_vcenter_clients_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeVcenterClients", redact_output=_redact_output),
        )
        input_: capo_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest = {}
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
