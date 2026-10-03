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
    import capo_partnercentral_selling.types.aws_submission
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.engagement_identifiers
    import capo_partnercentral_selling.types.list_engagement_from_opportunity_task_summary
    import capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request
    import capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response
    import capo_partnercentral_selling.types.list_tasks_sort_base
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.opportunity_identifiers
    import capo_partnercentral_selling.types.start_engagement_from_opportunity_task_request
    import capo_partnercentral_selling.types.start_engagement_from_opportunity_task_response
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


class EngagementFromOpportunityTask:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        aws_submission: "capo_partnercentral_selling.types.aws_submission.AwsSubmission",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse":
        """<p>Similar to <code>StartEngagementByAcceptingInvitationTask</code>, this action is asynchronous and performs multiple steps before completion. This action orchestrates a comprehensive workflow that combines multiple API operations into a single task to create and initiate an engagement from an existing opportunity. It automatically executes a sequence of operations including <code>GetOpportunity</code>, <code>CreateEngagement</code> (if it doesn't exist), <code>CreateResourceSnapshot</code>, <code>CreateResourceSnapshotJob</code>, <code>CreateEngagementInvitation</code> (if not already invited/accepted), and <code>SubmitOpportunity</code>. </p>

        Args:
            catalog: <p>Specifies the catalog in which the engagement is tracked. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            client_token: <p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>
            identifier: <p>The unique identifier of the opportunity from which the engagement task is to be initiated. This helps ensure that the task is applied to the correct opportunity.</p>
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
            req: "OperationRequest[capo_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task.start_engagement_from_opportunity_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "identifier": identifier,
            "aws_submission": aws_submission,
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
    ) -> "capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse":
        """<p> Lists all in-progress, completed, or failed <code>EngagementFromOpportunity</code> tasks that were initiated by the caller's account. </p>

        Args:
            max_results: <p> Specifies the maximum number of results to return in a single page of the response.Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets. </p>
            next_token: <p> The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages. </p>
            sort: <p> Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes. </p>
            catalog: <p> Specifies the catalog related to the request. Valid values are: </p> <ul> <li> <p> AWS: Retrieves the request from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            task_status: <p> Filters the tasks based on their current status. This allows you to focus on tasks in specific states. </p>
            task_identifier: <p> Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. </p>
            opportunity_identifier: <p> The identifier of the original opportunity associated with this task. </p>
            engagement_identifier: <p> Filters tasks by the identifiers of the engagements they created or are associated with. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks.list_engagement_from_opportunity_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest = {
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEngagementFromOpportunityTask:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        aws_submission: "capo_partnercentral_selling.types.aws_submission.AwsSubmission",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse":
        """<p>Similar to <code>StartEngagementByAcceptingInvitationTask</code>, this action is asynchronous and performs multiple steps before completion. This action orchestrates a comprehensive workflow that combines multiple API operations into a single task to create and initiate an engagement from an existing opportunity. It automatically executes a sequence of operations including <code>GetOpportunity</code>, <code>CreateEngagement</code> (if it doesn't exist), <code>CreateResourceSnapshot</code>, <code>CreateResourceSnapshotJob</code>, <code>CreateEngagementInvitation</code> (if not already invited/accepted), and <code>SubmitOpportunity</code>. </p>

        Args:
            catalog: <p>Specifies the catalog in which the engagement is tracked. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            client_token: <p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>
            identifier: <p>The unique identifier of the opportunity from which the engagement task is to be initiated. This helps ensure that the task is applied to the correct opportunity.</p>
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
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task.async_start_engagement_from_opportunity_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "identifier": identifier,
            "aws_submission": aws_submission,
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
    ) -> "capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse":
        """<p> Lists all in-progress, completed, or failed <code>EngagementFromOpportunity</code> tasks that were initiated by the caller's account. </p>

        Args:
            max_results: <p> Specifies the maximum number of results to return in a single page of the response.Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets. </p>
            next_token: <p> The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages. </p>
            sort: <p> Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes. </p>
            catalog: <p> Specifies the catalog related to the request. Valid values are: </p> <ul> <li> <p> AWS: Retrieves the request from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            task_status: <p> Filters the tasks based on their current status. This allows you to focus on tasks in specific states. </p>
            task_identifier: <p> Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. </p>
            opportunity_identifier: <p> The identifier of the original opportunity associated with this task. </p>
            engagement_identifier: <p> Filters tasks by the identifiers of the engagements they created or are associated with. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks.async_list_engagement_from_opportunity_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest = {
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
