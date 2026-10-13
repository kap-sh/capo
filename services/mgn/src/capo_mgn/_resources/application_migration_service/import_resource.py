from __future__ import annotations

import uuid
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
    import capo_mgn.types.client_idempotency_token
    import capo_mgn.types.import_id
    import capo_mgn.types.import_task
    import capo_mgn.types.import_task_error
    import capo_mgn.types.list_import_errors_request
    import capo_mgn.types.list_import_errors_response
    import capo_mgn.types.list_imports_request
    import capo_mgn.types.list_imports_request_filters
    import capo_mgn.types.list_imports_response
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.s3_bucket_source
    import capo_mgn.types.start_import_request
    import capo_mgn.types.start_import_response
    import capo_mgn.types.tags_map
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class ImportResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        s3_bucket_source: "capo_mgn.types.s3_bucket_source.S3BucketSource",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        client_token: Optional[
            "capo_mgn.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
    ) -> "capo_mgn.types.start_import_response.StartImportResponse":
        """<p>Start import.</p>

        Args:
            client_token: <p>Start import request client token.</p>
            s3_bucket_source: <p>Start import request s3 bucket source.</p>
            tags: <p>Start import request tags.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_import_request.StartImportRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_import_response.StartImportResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_import

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_import.start_import(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_import_request.StartImportRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_import_request

            return capo_mgn.types.start_import_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.start_import_response.StartImportResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_import_response

            return capo_mgn.types.start_import_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartImport", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.start_import_request.StartImportRequest = {
            "s3_bucket_source": s3_bucket_source
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

    def list(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_imports_request_filters.ListImportsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_imports_response.ListImportsResponse":
        """<p>List imports.</p>

        Args:
            filters: <p>List imports request filters.</p>
            max_results: <p>List imports request max results.</p>
            next_token: <p>List imports request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_imports_request.ListImportsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_imports_response.ListImportsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_imports

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_imports.list_imports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_imports_response.ListImportsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_imports_response

            return capo_mgn.types.list_imports_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListImports", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_imports_request.ListImportsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def list_import_errors(
        self,
        import_id: "capo_mgn.types.import_id.ImportID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_import_errors_response.ListImportErrorsResponse":
        """<p>List import errors.</p>

        Args:
            import_id: <p>List import errors request import id.</p>
            max_results: <p>List import errors request max results.</p>
            next_token: <p>List import errors request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_import_errors_request.ListImportErrorsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_import_errors_response.ListImportErrorsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_import_errors

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_import_errors.list_import_errors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListImportErrors")
        )
        input_: capo_mgn.types.list_import_errors_request.ListImportErrorsRequest = {
            "import_id": import_id
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


class AsyncImportResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        s3_bucket_source: "capo_mgn.types.s3_bucket_source.S3BucketSource",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        client_token: Optional[
            "capo_mgn.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
    ) -> "capo_mgn.types.start_import_response.StartImportResponse":
        """<p>Start import.</p>

        Args:
            client_token: <p>Start import request client token.</p>
            s3_bucket_source: <p>Start import request s3 bucket source.</p>
            tags: <p>Start import request tags.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.start_import_request.StartImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.start_import_response.StartImportResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_import

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.start_import.async_start_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_import_request.StartImportRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_import_request

            return capo_mgn.types.start_import_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.start_import_response.StartImportResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_import_response

            return capo_mgn.types.start_import_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartImport", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.start_import_request.StartImportRequest = {
            "s3_bucket_source": s3_bucket_source
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

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_imports_request_filters.ListImportsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_imports_response.ListImportsResponse":
        """<p>List imports.</p>

        Args:
            filters: <p>List imports request filters.</p>
            max_results: <p>List imports request max results.</p>
            next_token: <p>List imports request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_imports_request.ListImportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_imports_response.ListImportsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_imports

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_imports.async_list_imports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_imports_response.ListImportsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_imports_response

            return capo_mgn.types.list_imports_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListImports", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_imports_request.ListImportsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def list_import_errors(
        self,
        import_id: "capo_mgn.types.import_id.ImportID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_import_errors_response.ListImportErrorsResponse":
        """<p>List import errors.</p>

        Args:
            import_id: <p>List import errors request import id.</p>
            max_results: <p>List import errors request max results.</p>
            next_token: <p>List import errors request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_import_errors_request.ListImportErrorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_import_errors_response.ListImportErrorsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_import_errors

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_import_errors.async_list_import_errors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListImportErrors")
        )
        input_: capo_mgn.types.list_import_errors_request.ListImportErrorsRequest = {
            "import_id": import_id
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
