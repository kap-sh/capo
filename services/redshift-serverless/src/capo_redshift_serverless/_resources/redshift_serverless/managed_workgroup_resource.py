from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_redshift_serverless.types.list_managed_workgroups_request
    import capo_redshift_serverless.types.list_managed_workgroups_response
    import capo_redshift_serverless.types.managed_workgroup_list_item
    import capo_redshift_serverless.types.pagination_token
    import capo_redshift_serverless.types.source_arn
    from capo_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from capo_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class ManagedWorkgroupResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def list_managed_workgroups(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        source_arn: Optional[
            "capo_redshift_serverless.types.source_arn.SourceArn"
        ] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse":
        """<p>Returns information about a list of specified managed workgroups in your account.</p>

        Args:
            source_arn: <p>The Amazon Resource Name (ARN) for the managed workgroup in the Glue Data Catalog.</p>
            next_token: <p>If your initial ListManagedWorkgroups operation returns a nextToken, you can include the returned nextToken in following ListManagedWorkgroups operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_managed_workgroups

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.list_managed_workgroups.list_managed_workgroups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListManagedWorkgroups")
        )
        input_: capo_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest = {}
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncManagedWorkgroupResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def list_managed_workgroups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        source_arn: Optional[
            "capo_redshift_serverless.types.source_arn.SourceArn"
        ] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse":
        """<p>Returns information about a list of specified managed workgroups in your account.</p>

        Args:
            source_arn: <p>The Amazon Resource Name (ARN) for the managed workgroup in the Glue Data Catalog.</p>
            next_token: <p>If your initial ListManagedWorkgroups operation returns a nextToken, you can include the returned nextToken in following ListManagedWorkgroups operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_managed_workgroups

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_managed_workgroups.async_list_managed_workgroups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListManagedWorkgroups")
        )
        input_: capo_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest = {}
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
