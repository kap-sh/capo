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
    import capo_partnercentral_selling.types.create_resource_snapshot_job_request
    import capo_partnercentral_selling.types.create_resource_snapshot_job_response
    import capo_partnercentral_selling.types.delete_resource_snapshot_job_request
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.get_resource_snapshot_job_request
    import capo_partnercentral_selling.types.get_resource_snapshot_job_response
    import capo_partnercentral_selling.types.list_resource_snapshot_jobs_request
    import capo_partnercentral_selling.types.list_resource_snapshot_jobs_response
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_status
    import capo_partnercentral_selling.types.resource_snapshot_job_summary
    import capo_partnercentral_selling.types.resource_template_name
    import capo_partnercentral_selling.types.resource_type
    import capo_partnercentral_selling.types.sort_object
    import capo_partnercentral_selling.types.start_resource_snapshot_job_request
    import capo_partnercentral_selling.types.stop_resource_snapshot_job_request
    import capo_partnercentral_selling.types.tag_list
    from capo_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from capo_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class ResourceSnapshotJob:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "capo_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse":
        """<p>Use this action to create a job to generate a snapshot of the specified resource within an engagement. It initiates an asynchronous process to create a resource snapshot. The job creates a new snapshot only if the resource state has changed, adhering to the same access control and immutability rules as direct snapshot creation.</p>

        Args:
            catalog: <p>Specifies the catalog in which to create the snapshot job. Valid values are <code>AWS</code> and <code> Sandbox</code>.</p>
            client_token: <p>A client-generated UUID used for idempotency check. The token helps prevent duplicate job creations.</p>
            engagement_identifier: <p>Specifies the identifier of the engagement associated with the resource to be snapshotted.</p>
            resource_type: <p>The type of resource for which the snapshot job is being created. Must be one of the supported resource types i.e. <code>Opportunity</code> </p>
            resource_identifier: <p>Specifies the identifier of the specific resource to be snapshotted. The format depends on the <code> ResourceType</code>.</p>
            resource_snapshot_template_identifier: <p>Specifies the name of the template that defines the schema for the snapshot.</p>
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
            req: "OperationRequest[capo_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job.create_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "engagement_identifier": engagement_identifier,
            "resource_type": resource_type,
            "resource_identifier": resource_identifier,
            "resource_snapshot_template_identifier": resource_snapshot_template_identifier,
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

    def read(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse":
        """<p>Use this action to retrieves information about a specific resource snapshot job.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p> AWS: Retrieves the snapshot job from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the snapshot job from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            resource_snapshot_job_identifier: <p>The unique identifier of the resource snapshot job to be retrieved. This identifier is crucial for pinpointing the specific job you want to query. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job.get_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p> Use this action to deletes a previously created resource snapshot job. The job must be in a stopped state before it can be deleted. </p>

        Args:
            catalog: <p> Specifies the catalog from which to delete the snapshot job. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>
            resource_snapshot_job_identifier: <p> The unique identifier of the resource snapshot job to be deleted. </p>

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
            req: "OperationRequest[capo_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job.delete_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
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
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.sort_object.SortObject"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse":
        """<p> Lists resource snapshot jobs owned by the customer. This operation supports various filtering scenarios, including listing all jobs owned by the caller, jobs for a specific engagement, jobs with a specific status, or any combination of these filters. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            max_results: <p> The maximum number of results to return in a single call. If omitted, defaults to 50. </p>
            next_token: <p> The token for the next set of results. </p>
            engagement_identifier: <p> The identifier of the engagement to filter the response. </p>
            status: <p> The status of the jobs to filter the response. </p>
            sort: <p> Configures the sorting of the response. If omitted, results are sorted by <code>CreatedDate</code> in descending order. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs.list_resource_snapshot_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if status is not None:
            input_["status"] = status
        if sort is not None:
            input_["sort"] = sort

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_resource_snapshot_job(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Starts a resource snapshot job that has been previously created.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Starts the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Starts the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the resource snapshot job to start.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job.start_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_resource_snapshot_job(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Stops a resource snapshot job. The job must be started prior to being stopped.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Stops the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Stops the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the job to stop.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job.stop_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncResourceSnapshotJob:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "capo_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse":
        """<p>Use this action to create a job to generate a snapshot of the specified resource within an engagement. It initiates an asynchronous process to create a resource snapshot. The job creates a new snapshot only if the resource state has changed, adhering to the same access control and immutability rules as direct snapshot creation.</p>

        Args:
            catalog: <p>Specifies the catalog in which to create the snapshot job. Valid values are <code>AWS</code> and <code> Sandbox</code>.</p>
            client_token: <p>A client-generated UUID used for idempotency check. The token helps prevent duplicate job creations.</p>
            engagement_identifier: <p>Specifies the identifier of the engagement associated with the resource to be snapshotted.</p>
            resource_type: <p>The type of resource for which the snapshot job is being created. Must be one of the supported resource types i.e. <code>Opportunity</code> </p>
            resource_identifier: <p>Specifies the identifier of the specific resource to be snapshotted. The format depends on the <code> ResourceType</code>.</p>
            resource_snapshot_template_identifier: <p>Specifies the name of the template that defines the schema for the snapshot.</p>
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
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job.async_create_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "engagement_identifier": engagement_identifier,
            "resource_type": resource_type,
            "resource_identifier": resource_identifier,
            "resource_snapshot_template_identifier": resource_snapshot_template_identifier,
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

    async def read(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse":
        """<p>Use this action to retrieves information about a specific resource snapshot job.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p> AWS: Retrieves the snapshot job from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the snapshot job from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            resource_snapshot_job_identifier: <p>The unique identifier of the resource snapshot job to be retrieved. This identifier is crucial for pinpointing the specific job you want to query. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job.async_get_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p> Use this action to deletes a previously created resource snapshot job. The job must be in a stopped state before it can be deleted. </p>

        Args:
            catalog: <p> Specifies the catalog from which to delete the snapshot job. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>
            resource_snapshot_job_identifier: <p> The unique identifier of the resource snapshot job to be deleted. </p>

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
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job.async_delete_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
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
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.sort_object.SortObject"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse":
        """<p> Lists resource snapshot jobs owned by the customer. This operation supports various filtering scenarios, including listing all jobs owned by the caller, jobs for a specific engagement, jobs with a specific status, or any combination of these filters. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            max_results: <p> The maximum number of results to return in a single call. If omitted, defaults to 50. </p>
            next_token: <p> The token for the next set of results. </p>
            engagement_identifier: <p> The identifier of the engagement to filter the response. </p>
            status: <p> The status of the jobs to filter the response. </p>
            sort: <p> Configures the sorting of the response. If omitted, results are sorted by <code>CreatedDate</code> in descending order. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs.async_list_resource_snapshot_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if status is not None:
            input_["status"] = status
        if sort is not None:
            input_["sort"] = sort

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_resource_snapshot_job(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Starts a resource snapshot job that has been previously created.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Starts the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Starts the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the resource snapshot job to start.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job.async_start_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_resource_snapshot_job(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Stops a resource snapshot job. The job must be started prior to being stopped.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Stops the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Stops the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the job to stop.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job.async_stop_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
