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
    import capo_partnercentral_selling.types.context_identifier
    import capo_partnercentral_selling.types.context_identifiers
    import capo_partnercentral_selling.types.engagement_arn_or_identifier
    import capo_partnercentral_selling.types.engagement_identifiers
    import capo_partnercentral_selling.types.list_opportunity_from_engagement_task_summary
    import capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_request
    import capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_response
    import capo_partnercentral_selling.types.list_tasks_sort_base
    import capo_partnercentral_selling.types.opportunity_identifiers
    import capo_partnercentral_selling.types.start_opportunity_from_engagement_task_request
    import capo_partnercentral_selling.types.start_opportunity_from_engagement_task_response
    import capo_partnercentral_selling.types.tag_list
    import capo_partnercentral_selling.types.task_identifiers
    import capo_partnercentral_selling.types.task_statuses
    from capo_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from capo_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class OpportunityFromEngagementTask:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        context_identifier: "capo_partnercentral_selling.types.context_identifier.ContextIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.start_opportunity_from_engagement_task_response.StartOpportunityFromEngagementTaskResponse":
        """<p>This action creates an opportunity from an existing engagement context. The task is asynchronous and orchestrates the process of converting engagement contextual information into a structured opportunity record within the partner's account.</p>

        Args:
            catalog: <p>Specifies the catalog in which the opportunity creation task is executed. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            client_token: <p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>
            identifier: <p>The unique identifier of the engagement from which the opportunity creation task is to be initiated. This helps ensure that the task is applied to the correct engagement.</p>
            context_identifier: <p>The unique identifier of the engagement context from which to create the opportunity. This specifies the specific contextual information within the engagement that will be used for opportunity creation.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.start_opportunity_from_engagement_task_request.StartOpportunityFromEngagementTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.start_opportunity_from_engagement_task_response.StartOpportunityFromEngagementTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_opportunity_from_engagement_task

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.start_opportunity_from_engagement_task.start_opportunity_from_engagement_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_opportunity_from_engagement_task_request.StartOpportunityFromEngagementTaskRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "identifier": identifier,
            "context_identifier": context_identifier,
        }
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
        opportunity_identifier: Optional[
            "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
        context_identifier: Optional[
            "capo_partnercentral_selling.types.context_identifiers.ContextIdentifiers"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_response.ListOpportunityFromEngagementTasksResponse":
        """<p>Lists all in-progress, completed, or failed opportunity creation tasks from engagements that were initiated by the caller's account.</p>

        Args:
            max_results: <p>Specifies the maximum number of results to return in a single page of the response. Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets.</p>
            next_token: <p>The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages.</p>
            catalog: <p>Specifies the catalog related to the request. Valid values are <code>AWS</code> for production environments and <code>Sandbox</code> for testing or development purposes. The catalog determines which environment the task data is retrieved from.</p>
            task_status: <p>Filters the tasks based on their current status. This allows you to focus on tasks in specific states. Valid values are <code>COMPLETE</code> for tasks that have finished successfully, <code>INPROGRESS</code> for tasks that are currently running, and <code>FAILED</code> for tasks that have encountered an error and failed to complete.</p>
            task_identifier: <p>Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. Provide the task ID to get details about a particular opportunity creation task.</p>
            opportunity_identifier: <p>Filters tasks by the identifiers of the opportunities they created or are associated with. Use this to find tasks related to specific opportunity creation processes.</p>
            engagement_identifier: <p>Filters tasks by the identifiers of the engagements from which opportunities are being created. Use this to find all opportunity creation tasks associated with a specific engagement.</p>
            context_identifier: <p>Filters tasks by the identifiers of the engagement contexts associated with the opportunity creation. Use this to find tasks related to specific contextual information within engagements that are being converted to opportunities.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_request.ListOpportunityFromEngagementTasksRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_response.ListOpportunityFromEngagementTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunity_from_engagement_tasks

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunity_from_engagement_tasks.list_opportunity_from_engagement_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_request.ListOpportunityFromEngagementTasksRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if task_status is not None:
            input_["task_status"] = task_status
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier
        if opportunity_identifier is not None:
            input_["opportunity_identifier"] = opportunity_identifier
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if context_identifier is not None:
            input_["context_identifier"] = context_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncOpportunityFromEngagementTask:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        context_identifier: "capo_partnercentral_selling.types.context_identifier.ContextIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.start_opportunity_from_engagement_task_response.StartOpportunityFromEngagementTaskResponse":
        """<p>This action creates an opportunity from an existing engagement context. The task is asynchronous and orchestrates the process of converting engagement contextual information into a structured opportunity record within the partner's account.</p>

        Args:
            catalog: <p>Specifies the catalog in which the opportunity creation task is executed. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            client_token: <p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>
            identifier: <p>The unique identifier of the engagement from which the opportunity creation task is to be initiated. This helps ensure that the task is applied to the correct engagement.</p>
            context_identifier: <p>The unique identifier of the engagement context from which to create the opportunity. This specifies the specific contextual information within the engagement that will be used for opportunity creation.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.start_opportunity_from_engagement_task_request.StartOpportunityFromEngagementTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.start_opportunity_from_engagement_task_response.StartOpportunityFromEngagementTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_opportunity_from_engagement_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.start_opportunity_from_engagement_task.async_start_opportunity_from_engagement_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_opportunity_from_engagement_task_request.StartOpportunityFromEngagementTaskRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "identifier": identifier,
            "context_identifier": context_identifier,
        }
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
        opportunity_identifier: Optional[
            "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
        context_identifier: Optional[
            "capo_partnercentral_selling.types.context_identifiers.ContextIdentifiers"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_response.ListOpportunityFromEngagementTasksResponse":
        """<p>Lists all in-progress, completed, or failed opportunity creation tasks from engagements that were initiated by the caller's account.</p>

        Args:
            max_results: <p>Specifies the maximum number of results to return in a single page of the response. Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets.</p>
            next_token: <p>The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages.</p>
            catalog: <p>Specifies the catalog related to the request. Valid values are <code>AWS</code> for production environments and <code>Sandbox</code> for testing or development purposes. The catalog determines which environment the task data is retrieved from.</p>
            task_status: <p>Filters the tasks based on their current status. This allows you to focus on tasks in specific states. Valid values are <code>COMPLETE</code> for tasks that have finished successfully, <code>INPROGRESS</code> for tasks that are currently running, and <code>FAILED</code> for tasks that have encountered an error and failed to complete.</p>
            task_identifier: <p>Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. Provide the task ID to get details about a particular opportunity creation task.</p>
            opportunity_identifier: <p>Filters tasks by the identifiers of the opportunities they created or are associated with. Use this to find tasks related to specific opportunity creation processes.</p>
            engagement_identifier: <p>Filters tasks by the identifiers of the engagements from which opportunities are being created. Use this to find all opportunity creation tasks associated with a specific engagement.</p>
            context_identifier: <p>Filters tasks by the identifiers of the engagement contexts associated with the opportunity creation. Use this to find tasks related to specific contextual information within engagements that are being converted to opportunities.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_request.ListOpportunityFromEngagementTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_response.ListOpportunityFromEngagementTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunity_from_engagement_tasks

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunity_from_engagement_tasks.async_list_opportunity_from_engagement_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_request.ListOpportunityFromEngagementTasksRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if task_status is not None:
            input_["task_status"] = task_status
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier
        if opportunity_identifier is not None:
            input_["opportunity_identifier"] = opportunity_identifier
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if context_identifier is not None:
            input_["context_identifier"] = context_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
