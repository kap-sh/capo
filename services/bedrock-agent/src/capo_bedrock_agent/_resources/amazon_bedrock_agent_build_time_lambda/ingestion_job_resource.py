from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agent._auth._signers
import capo_bedrock_agent._auth._sigv4
from capo_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.get_ingestion_job_request
    import capo_bedrock_agent.types.get_ingestion_job_response
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.ingestion_job_filters
    import capo_bedrock_agent.types.ingestion_job_sort_by
    import capo_bedrock_agent.types.ingestion_job_summary
    import capo_bedrock_agent.types.list_ingestion_jobs_request
    import capo_bedrock_agent.types.list_ingestion_jobs_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.start_ingestion_job_request
    import capo_bedrock_agent.types.start_ingestion_job_response
    import capo_bedrock_agent.types.stop_ingestion_job_request
    import capo_bedrock_agent.types.stop_ingestion_job_response
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class IngestionJobResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def get_ingestion_job(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        ingestion_job_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse":
        """<p>Gets information about a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to get information on.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to get information on.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to get information on.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job.get_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "ingestion_job_id": ingestion_job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_ingestion_jobs(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        filters: Optional[
            "capo_bedrock_agent.types.ingestion_job_filters.IngestionJobFilters"
        ] = None,
        sort_by: Optional[
            "capo_bedrock_agent.types.ingestion_job_sort_by.IngestionJobSortBy"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse":
        """<p>Lists the data ingestion jobs for a data source. The list also includes information about each job.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the list of data ingestion jobs.</p>
            data_source_id: <p>The unique identifier of the data source for the list of data ingestion jobs.</p>
            filters: <p>Contains information about the filters for filtering the data.</p>
            sort_by: <p>Contains details about how to sort the data.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs.list_ingestion_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    def start_ingestion_job(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
    ) -> "capo_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse":
        """<p>Begins a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job.</p>
            data_source_id: <p>The unique identifier of the data source you want to ingest into your knowledge base.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p>A description of the data ingestion job.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job.start_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_ingestion_job(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        ingestion_job_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse"
    ):
        """<p>Stops a currently running data ingestion job. You can send a <code>StartIngestionJob</code> request again to ingest the rest of your data when you are ready.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to stop.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to stop.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to stop.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job.stop_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "ingestion_job_id": ingestion_job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncIngestionJobResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def get_ingestion_job(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        ingestion_job_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse":
        """<p>Gets information about a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to get information on.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to get information on.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to get information on.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job.async_get_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "ingestion_job_id": ingestion_job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ingestion_jobs(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        filters: Optional[
            "capo_bedrock_agent.types.ingestion_job_filters.IngestionJobFilters"
        ] = None,
        sort_by: Optional[
            "capo_bedrock_agent.types.ingestion_job_sort_by.IngestionJobSortBy"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse":
        """<p>Lists the data ingestion jobs for a data source. The list also includes information about each job.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the list of data ingestion jobs.</p>
            data_source_id: <p>The unique identifier of the data source for the list of data ingestion jobs.</p>
            filters: <p>Contains information about the filters for filtering the data.</p>
            sort_by: <p>Contains details about how to sort the data.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs.async_list_ingestion_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def start_ingestion_job(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
    ) -> "capo_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse":
        """<p>Begins a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job.</p>
            data_source_id: <p>The unique identifier of the data source you want to ingest into your knowledge base.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p>A description of the data ingestion job.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job.async_start_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_ingestion_job(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        ingestion_job_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse"
    ):
        """<p>Stops a currently running data ingestion job. You can send a <code>StartIngestionJob</code> request again to ingest the rest of your data when you are ready.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to stop.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to stop.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to stop.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job.async_stop_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "ingestion_job_id": ingestion_job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
