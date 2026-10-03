from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_partnercentral_selling._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_identifier_list
    import capo_partnercentral_selling.types.get_prospecting_from_engagement_task_request
    import capo_partnercentral_selling.types.get_prospecting_from_engagement_task_response
    import capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_request
    import capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_response
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.prospecting_from_engagement_task_sort
    import capo_partnercentral_selling.types.prospecting_task_identifier
    import capo_partnercentral_selling.types.prospecting_task_summary
    import capo_partnercentral_selling.types.start_prospecting_from_engagement_task_request
    import capo_partnercentral_selling.types.start_prospecting_from_engagement_task_response
    import capo_partnercentral_selling.types.task_identifier_list
    import capo_partnercentral_selling.types.task_name
    import capo_partnercentral_selling.types.task_name_list
    from capo_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from capo_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class ProspectingFromEngagementTask:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifiers: "capo_partnercentral_selling.types.engagement_identifier_list.EngagementIdentifierList",
        task_name: "capo_partnercentral_selling.types.task_name.TaskName",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.start_prospecting_from_engagement_task_response.StartProspectingFromEngagementTaskResponse":
        """<p>Starts a task to convert one or more engagement contexts into new prospecting leads. The task runs asynchronously. To poll for status, use <code>GetProspectingFromEngagementTask</code>, or use <code>ListProspectingFromEngagementTasks</code> to monitor multiple tasks.</p>

        Args:
            catalog: <p>Specifies the catalog in which the task is initiated. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes.</p>
            identifiers: <p>The list of engagement identifiers to include in this prospecting task. Each identifier must correspond to an existing engagement in the specified catalog. Maximum of 100 identifiers per task.</p>
            task_name: <p>A descriptive name for the task. This name helps identify the task in list and get operations. The name must contain 1 to 128 characters.</p>
            client_token: <p>A unique, case-sensitive identifier provided by the client to ensure idempotency. Making the same request with the same <code>ClientToken</code> returns the same response without creating a duplicate task.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.start_prospecting_from_engagement_task_request.StartProspectingFromEngagementTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.start_prospecting_from_engagement_task_response.StartProspectingFromEngagementTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_prospecting_from_engagement_task

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.start_prospecting_from_engagement_task.start_prospecting_from_engagement_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_prospecting_from_engagement_task_request.StartProspectingFromEngagementTaskRequest = {
            "catalog": catalog,
            "identifiers": identifiers,
            "task_name": task_name,
            "client_token": client_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        task_identifier: "capo_partnercentral_selling.types.prospecting_task_identifier.ProspectingTaskIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_prospecting_from_engagement_task_response.GetProspectingFromEngagementTaskResponse":
        """<p>Retrieves the details and current status of a prospecting task previously started with <code>StartProspectingFromEngagementTask</code> to enable polling for completion and access to per-engagement processing results.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the task. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes. The value must match the catalog used when the task was created.</p>
            task_identifier: <p>The unique identifier of the prospecting task to retrieve. This value is returned in the <code>TaskId</code> field of the <code>StartProspectingFromEngagementTask</code> response.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.get_prospecting_from_engagement_task_request.GetProspectingFromEngagementTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.get_prospecting_from_engagement_task_response.GetProspectingFromEngagementTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_prospecting_from_engagement_task

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.get_prospecting_from_engagement_task.get_prospecting_from_engagement_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_prospecting_from_engagement_task_request.GetProspectingFromEngagementTaskRequest = {
            "catalog": catalog,
            "task_identifier": task_identifier,
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifier_list.TaskIdentifierList"
        ] = None,
        task_name: Optional[
            "capo_partnercentral_selling.types.task_name_list.TaskNameList"
        ] = None,
        start_after: Optional[
            "capo_partnercentral_selling.types.date_time.DateTime"
        ] = None,
        start_before: Optional[
            "capo_partnercentral_selling.types.date_time.DateTime"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.prospecting_from_engagement_task_sort.ProspectingFromEngagementTaskSort"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_response.ListProspectingFromEngagementTasksResponse":
        """<p>Lists all prospecting tasks initiated by the caller's account. Supports optional filters by task identifier, task name, or start time range. Results can be sorted using configurable options. The response is paginated. Use the <code>NextToken</code> value from each response to retrieve subsequent pages.</p>

        Args:
            catalog: <p>Specifies the catalog to list tasks from. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes.</p>
            max_results: <p>The maximum number of results to return in a single page. If additional results exist, the response includes a <code>NextToken</code> value for retrieving the next page. If omitted, the API uses a service-defined default page size.</p>
            next_token: <p>The pagination token from a previous call to this API. Include this value to retrieve the next page of results. If omitted, the first page is returned.</p>
            task_identifier: <p>Filters the results to include only the tasks with the specified identifiers. Provide up to 10 task IDs to narrow the list to specific tasks. If omitted, tasks are not filtered by identifier.</p>
            task_name: <p>Filters the results to include only tasks with the specified names. Provide up to 10 task names to narrow the list. If omitted, tasks are not filtered by name.</p>
            start_after: <p>Filters tasks to include only those that started after the specified timestamp. Use this with <code>StartBefore</code> to define a start-time range for your query. The format follows ISO 8601 date-time notation.</p>
            start_before: <p>Filters tasks to include only those that started before the specified timestamp. Use this with <code>StartAfter</code> to define a start-time range for your query. The format follows ISO 8601 date-time notation.</p>
            sort: <p>Specifies the field and order used to sort the returned tasks. If omitted, tasks are returned in the default sort order.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_request.ListProspectingFromEngagementTasksRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_response.ListProspectingFromEngagementTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_prospecting_from_engagement_tasks

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_prospecting_from_engagement_tasks.list_prospecting_from_engagement_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_request.ListProspectingFromEngagementTasksRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier
        if task_name is not None:
            input_["task_name"] = task_name
        if start_after is not None:
            input_["start_after"] = start_after
        if start_before is not None:
            input_["start_before"] = start_before
        if sort is not None:
            input_["sort"] = sort

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncProspectingFromEngagementTask:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifiers: "capo_partnercentral_selling.types.engagement_identifier_list.EngagementIdentifierList",
        task_name: "capo_partnercentral_selling.types.task_name.TaskName",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.start_prospecting_from_engagement_task_response.StartProspectingFromEngagementTaskResponse":
        """<p>Starts a task to convert one or more engagement contexts into new prospecting leads. The task runs asynchronously. To poll for status, use <code>GetProspectingFromEngagementTask</code>, or use <code>ListProspectingFromEngagementTasks</code> to monitor multiple tasks.</p>

        Args:
            catalog: <p>Specifies the catalog in which the task is initiated. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes.</p>
            identifiers: <p>The list of engagement identifiers to include in this prospecting task. Each identifier must correspond to an existing engagement in the specified catalog. Maximum of 100 identifiers per task.</p>
            task_name: <p>A descriptive name for the task. This name helps identify the task in list and get operations. The name must contain 1 to 128 characters.</p>
            client_token: <p>A unique, case-sensitive identifier provided by the client to ensure idempotency. Making the same request with the same <code>ClientToken</code> returns the same response without creating a duplicate task.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.start_prospecting_from_engagement_task_request.StartProspectingFromEngagementTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.start_prospecting_from_engagement_task_response.StartProspectingFromEngagementTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_prospecting_from_engagement_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.start_prospecting_from_engagement_task.async_start_prospecting_from_engagement_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_prospecting_from_engagement_task_request.StartProspectingFromEngagementTaskRequest = {
            "catalog": catalog,
            "identifiers": identifiers,
            "task_name": task_name,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        task_identifier: "capo_partnercentral_selling.types.prospecting_task_identifier.ProspectingTaskIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_prospecting_from_engagement_task_response.GetProspectingFromEngagementTaskResponse":
        """<p>Retrieves the details and current status of a prospecting task previously started with <code>StartProspectingFromEngagementTask</code> to enable polling for completion and access to per-engagement processing results.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the task. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes. The value must match the catalog used when the task was created.</p>
            task_identifier: <p>The unique identifier of the prospecting task to retrieve. This value is returned in the <code>TaskId</code> field of the <code>StartProspectingFromEngagementTask</code> response.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_prospecting_from_engagement_task_request.GetProspectingFromEngagementTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_prospecting_from_engagement_task_response.GetProspectingFromEngagementTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_prospecting_from_engagement_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_prospecting_from_engagement_task.async_get_prospecting_from_engagement_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_prospecting_from_engagement_task_request.GetProspectingFromEngagementTaskRequest = {
            "catalog": catalog,
            "task_identifier": task_identifier,
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifier_list.TaskIdentifierList"
        ] = None,
        task_name: Optional[
            "capo_partnercentral_selling.types.task_name_list.TaskNameList"
        ] = None,
        start_after: Optional[
            "capo_partnercentral_selling.types.date_time.DateTime"
        ] = None,
        start_before: Optional[
            "capo_partnercentral_selling.types.date_time.DateTime"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.prospecting_from_engagement_task_sort.ProspectingFromEngagementTaskSort"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_response.ListProspectingFromEngagementTasksResponse":
        """<p>Lists all prospecting tasks initiated by the caller's account. Supports optional filters by task identifier, task name, or start time range. Results can be sorted using configurable options. The response is paginated. Use the <code>NextToken</code> value from each response to retrieve subsequent pages.</p>

        Args:
            catalog: <p>Specifies the catalog to list tasks from. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes.</p>
            max_results: <p>The maximum number of results to return in a single page. If additional results exist, the response includes a <code>NextToken</code> value for retrieving the next page. If omitted, the API uses a service-defined default page size.</p>
            next_token: <p>The pagination token from a previous call to this API. Include this value to retrieve the next page of results. If omitted, the first page is returned.</p>
            task_identifier: <p>Filters the results to include only the tasks with the specified identifiers. Provide up to 10 task IDs to narrow the list to specific tasks. If omitted, tasks are not filtered by identifier.</p>
            task_name: <p>Filters the results to include only tasks with the specified names. Provide up to 10 task names to narrow the list. If omitted, tasks are not filtered by name.</p>
            start_after: <p>Filters tasks to include only those that started after the specified timestamp. Use this with <code>StartBefore</code> to define a start-time range for your query. The format follows ISO 8601 date-time notation.</p>
            start_before: <p>Filters tasks to include only those that started before the specified timestamp. Use this with <code>StartAfter</code> to define a start-time range for your query. The format follows ISO 8601 date-time notation.</p>
            sort: <p>Specifies the field and order used to sort the returned tasks. If omitted, tasks are returned in the default sort order.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_request.ListProspectingFromEngagementTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_response.ListProspectingFromEngagementTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_prospecting_from_engagement_tasks

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_prospecting_from_engagement_tasks.async_list_prospecting_from_engagement_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_request.ListProspectingFromEngagementTasksRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier
        if task_name is not None:
            input_["task_name"] = task_name
        if start_after is not None:
            input_["start_after"] = start_after
        if start_before is not None:
            input_["start_before"] = start_before
        if sort is not None:
            input_["sort"] = sort

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
