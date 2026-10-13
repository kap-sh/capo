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
    import capo_mgn.types.account_id
    import capo_mgn.types.export_id
    import capo_mgn.types.export_task
    import capo_mgn.types.export_task_error
    import capo_mgn.types.list_export_errors_request
    import capo_mgn.types.list_export_errors_response
    import capo_mgn.types.list_exports_request
    import capo_mgn.types.list_exports_request_filters
    import capo_mgn.types.list_exports_response
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.s3_bucket_name
    import capo_mgn.types.s3_key
    import capo_mgn.types.start_export_request
    import capo_mgn.types.start_export_response
    import capo_mgn.types.tags_map
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class ExportResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        s3_bucket: "capo_mgn.types.s3_bucket_name.S3BucketName",
        s3_key: "capo_mgn.types.s3_key.S3Key",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        s3_bucket_owner: Optional["capo_mgn.types.account_id.AccountID"] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
    ) -> "capo_mgn.types.start_export_response.StartExportResponse":
        """<p>Start export.</p>

        Args:
            s3_bucket: <p>Start export request s3 bucket.</p>
            s3_key: <p>Start export request s3key.</p>
            s3_bucket_owner: <p>Start export request s3 bucket owner.</p>
            tags: <p>Start export request tags.</p>

        Raises:
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_export_request.StartExportRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_export_response.StartExportResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_export

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_export.start_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_export_request.StartExportRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_export_request

            return capo_mgn.types.start_export_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.start_export_response.StartExportResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_export_response

            return capo_mgn.types.start_export_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartExport", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.start_export_request.StartExportRequest = {
            "s3_bucket": s3_bucket,
            "s3_key": s3_key,
        }
        if s3_bucket_owner is not None:
            input_["s3_bucket_owner"] = s3_bucket_owner
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
            "capo_mgn.types.list_exports_request_filters.ListExportsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_exports_response.ListExportsResponse":
        """<p>List exports.</p>

        Args:
            max_results: <p>List export request max results.</p>
            next_token: <p>List export request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_exports_request.ListExportsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_exports_response.ListExportsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_exports

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_exports.list_exports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_exports_response.ListExportsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_exports_response

            return capo_mgn.types.list_exports_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListExports", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_exports_request.ListExportsRequest = {}
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

    def list_export_errors(
        self,
        export_id: "capo_mgn.types.export_id.ExportID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_export_errors_response.ListExportErrorsResponse":
        """<p>List export errors.</p>

        Args:
            export_id: <p>List export errors request export id.</p>
            max_results: <p>List export errors request max results.</p>
            next_token: <p>List export errors request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_export_errors_request.ListExportErrorsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_export_errors_response.ListExportErrorsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_export_errors

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_export_errors.list_export_errors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListExportErrors")
        )
        input_: capo_mgn.types.list_export_errors_request.ListExportErrorsRequest = {
            "export_id": export_id
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


class AsyncExportResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        s3_bucket: "capo_mgn.types.s3_bucket_name.S3BucketName",
        s3_key: "capo_mgn.types.s3_key.S3Key",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        s3_bucket_owner: Optional["capo_mgn.types.account_id.AccountID"] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
    ) -> "capo_mgn.types.start_export_response.StartExportResponse":
        """<p>Start export.</p>

        Args:
            s3_bucket: <p>Start export request s3 bucket.</p>
            s3_key: <p>Start export request s3key.</p>
            s3_bucket_owner: <p>Start export request s3 bucket owner.</p>
            tags: <p>Start export request tags.</p>

        Raises:
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.start_export_request.StartExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.start_export_response.StartExportResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_export

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.start_export.async_start_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_export_request.StartExportRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_export_request

            return capo_mgn.types.start_export_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.start_export_response.StartExportResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_export_response

            return capo_mgn.types.start_export_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartExport", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.start_export_request.StartExportRequest = {
            "s3_bucket": s3_bucket,
            "s3_key": s3_key,
        }
        if s3_bucket_owner is not None:
            input_["s3_bucket_owner"] = s3_bucket_owner
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
            "capo_mgn.types.list_exports_request_filters.ListExportsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_exports_response.ListExportsResponse":
        """<p>List exports.</p>

        Args:
            max_results: <p>List export request max results.</p>
            next_token: <p>List export request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_exports_request.ListExportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_exports_response.ListExportsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_exports

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_exports.async_list_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_exports_response.ListExportsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_exports_response

            return capo_mgn.types.list_exports_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListExports", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_exports_request.ListExportsRequest = {}
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

    async def list_export_errors(
        self,
        export_id: "capo_mgn.types.export_id.ExportID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_export_errors_response.ListExportErrorsResponse":
        """<p>List export errors.</p>

        Args:
            export_id: <p>List export errors request export id.</p>
            max_results: <p>List export errors request max results.</p>
            next_token: <p>List export errors request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_export_errors_request.ListExportErrorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_export_errors_response.ListExportErrorsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_export_errors

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_export_errors.async_list_export_errors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListExportErrors")
        )
        input_: capo_mgn.types.list_export_errors_request.ListExportErrorsRequest = {
            "export_id": export_id
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
