"""Generated from Smithy shape ``com.amazonaws.neptunedata#AmazonNeptuneDataplane``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_neptunedata._auth._signers
import capo_neptunedata._auth._sigv4
from capo_neptunedata._auth._identity import Credentials
from capo_neptunedata._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_neptunedata._auth._zapros_handler import AuthMiddleware
from capo_neptunedata._services._aws_config import aaws_config
from capo_neptunedata._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_neptunedata.types.action
    import capo_neptunedata.types.cancel_gremlin_query_input
    import capo_neptunedata.types.cancel_gremlin_query_output
    import capo_neptunedata.types.cancel_loader_job_input
    import capo_neptunedata.types.cancel_loader_job_output
    import capo_neptunedata.types.cancel_ml_data_processing_job_input
    import capo_neptunedata.types.cancel_ml_data_processing_job_output
    import capo_neptunedata.types.cancel_ml_model_training_job_input
    import capo_neptunedata.types.cancel_ml_model_training_job_output
    import capo_neptunedata.types.cancel_ml_model_transform_job_input
    import capo_neptunedata.types.cancel_ml_model_transform_job_output
    import capo_neptunedata.types.cancel_open_cypher_query_input
    import capo_neptunedata.types.cancel_open_cypher_query_output
    import capo_neptunedata.types.create_ml_endpoint_input
    import capo_neptunedata.types.create_ml_endpoint_output
    import capo_neptunedata.types.custom_model_training_parameters
    import capo_neptunedata.types.custom_model_transform_parameters
    import capo_neptunedata.types.delete_ml_endpoint_input
    import capo_neptunedata.types.delete_ml_endpoint_output
    import capo_neptunedata.types.delete_propertygraph_statistics_output
    import capo_neptunedata.types.delete_sparql_statistics_output
    import capo_neptunedata.types.encoding
    import capo_neptunedata.types.execute_fast_reset_input
    import capo_neptunedata.types.execute_fast_reset_output
    import capo_neptunedata.types.execute_gremlin_explain_query_input
    import capo_neptunedata.types.execute_gremlin_explain_query_output
    import capo_neptunedata.types.execute_gremlin_profile_query_input
    import capo_neptunedata.types.execute_gremlin_profile_query_output
    import capo_neptunedata.types.execute_gremlin_query_input
    import capo_neptunedata.types.execute_gremlin_query_output
    import capo_neptunedata.types.execute_open_cypher_explain_query_input
    import capo_neptunedata.types.execute_open_cypher_explain_query_output
    import capo_neptunedata.types.execute_open_cypher_query_input
    import capo_neptunedata.types.execute_open_cypher_query_output
    import capo_neptunedata.types.format
    import capo_neptunedata.types.get_engine_status_output
    import capo_neptunedata.types.get_gremlin_query_status_input
    import capo_neptunedata.types.get_gremlin_query_status_output
    import capo_neptunedata.types.get_loader_job_status_input
    import capo_neptunedata.types.get_loader_job_status_output
    import capo_neptunedata.types.get_ml_data_processing_job_input
    import capo_neptunedata.types.get_ml_data_processing_job_output
    import capo_neptunedata.types.get_ml_endpoint_input
    import capo_neptunedata.types.get_ml_endpoint_output
    import capo_neptunedata.types.get_ml_model_training_job_input
    import capo_neptunedata.types.get_ml_model_training_job_output
    import capo_neptunedata.types.get_ml_model_transform_job_input
    import capo_neptunedata.types.get_ml_model_transform_job_output
    import capo_neptunedata.types.get_open_cypher_query_status_input
    import capo_neptunedata.types.get_open_cypher_query_status_output
    import capo_neptunedata.types.get_propertygraph_statistics_output
    import capo_neptunedata.types.get_propertygraph_stream_input
    import capo_neptunedata.types.get_propertygraph_stream_output
    import capo_neptunedata.types.get_propertygraph_summary_input
    import capo_neptunedata.types.get_propertygraph_summary_output
    import capo_neptunedata.types.get_rdf_graph_summary_input
    import capo_neptunedata.types.get_rdf_graph_summary_output
    import capo_neptunedata.types.get_sparql_statistics_output
    import capo_neptunedata.types.get_sparql_stream_input
    import capo_neptunedata.types.get_sparql_stream_output
    import capo_neptunedata.types.graph_summary_type
    import capo_neptunedata.types.iterator_type
    import capo_neptunedata.types.list_gremlin_queries_input
    import capo_neptunedata.types.list_gremlin_queries_output
    import capo_neptunedata.types.list_loader_jobs_input
    import capo_neptunedata.types.list_loader_jobs_output
    import capo_neptunedata.types.list_ml_data_processing_jobs_input
    import capo_neptunedata.types.list_ml_data_processing_jobs_output
    import capo_neptunedata.types.list_ml_endpoints_input
    import capo_neptunedata.types.list_ml_endpoints_output
    import capo_neptunedata.types.list_ml_model_training_jobs_input
    import capo_neptunedata.types.list_ml_model_training_jobs_output
    import capo_neptunedata.types.list_ml_model_transform_jobs_input
    import capo_neptunedata.types.list_ml_model_transform_jobs_output
    import capo_neptunedata.types.list_open_cypher_queries_input
    import capo_neptunedata.types.list_open_cypher_queries_output
    import capo_neptunedata.types.manage_propertygraph_statistics_input
    import capo_neptunedata.types.manage_propertygraph_statistics_output
    import capo_neptunedata.types.manage_sparql_statistics_input
    import capo_neptunedata.types.manage_sparql_statistics_output
    import capo_neptunedata.types.mode
    import capo_neptunedata.types.open_cypher_explain_mode
    import capo_neptunedata.types.parallelism
    import capo_neptunedata.types.positive_integer
    import capo_neptunedata.types.s3_bucket_region
    import capo_neptunedata.types.start_loader_job_input
    import capo_neptunedata.types.start_loader_job_output
    import capo_neptunedata.types.start_ml_data_processing_job_input
    import capo_neptunedata.types.start_ml_data_processing_job_output
    import capo_neptunedata.types.start_ml_model_training_job_input
    import capo_neptunedata.types.start_ml_model_training_job_output
    import capo_neptunedata.types.start_ml_model_transform_job_input
    import capo_neptunedata.types.start_ml_model_transform_job_output
    import capo_neptunedata.types.statistics_auto_generation_mode
    import capo_neptunedata.types.string_list
    import capo_neptunedata.types.string_valued_map


class AsyncneptunedataClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncneptunedataClient:
    """A client for the ``neptunedata`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncneptunedataClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncneptunedataClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncneptunedataClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def cancel_gremlin_query(
        self,
        query_id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
    ) -> "capo_neptunedata.types.cancel_gremlin_query_output.CancelGremlinQueryOutput":
        """<p>Cancels a Gremlin query. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status-cancel.html">Gremlin query cancellation</a> for more information.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelquery">neptune-db:CancelQuery</a> IAM action in that cluster.</p>

        Args:
            query_id: <p>The unique identifier that identifies the query to be canceled.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.cancel_gremlin_query_input.CancelGremlinQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.cancel_gremlin_query_output.CancelGremlinQueryOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.cancel_gremlin_query

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.cancel_gremlin_query.async_cancel_gremlin_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.cancel_gremlin_query_input.CancelGremlinQueryInput = {
            "query_id": query_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_loader_job(
        self,
        load_id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
    ) -> "capo_neptunedata.types.cancel_loader_job_output.CancelLoaderJobOutput":
        """<p>Cancels a specified load job. This is an HTTP <code>DELETE</code> request. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-status.htm">Neptune Loader Get-Status API</a> for more information.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelloaderjob">neptune-db:CancelLoaderJob</a> IAM action in that cluster..</p>

        Args:
            load_id: <p>The ID of the load job to be deleted.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.bulk_load_id_not_found_exception.BulkLoadIdNotFoundException: <p>Raised when a specified bulk-load job ID cannot be found.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.internal_failure_exception.InternalFailureException: <p>Raised when the processing of the request failed unexpectedly.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.load_url_access_denied_exception.LoadUrlAccessDeniedException: <p>Raised when access is denied to a specified load URL.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.cancel_loader_job_input.CancelLoaderJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.cancel_loader_job_output.CancelLoaderJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.cancel_loader_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.cancel_loader_job.async_cancel_loader_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.cancel_loader_job_input.CancelLoaderJobInput = {
            "load_id": load_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_ml_data_processing_job(
        self,
        id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        neptune_iam_role_arn: Optional[str] = None,
        clean: Optional[bool] = None,
    ) -> "capo_neptunedata.types.cancel_ml_data_processing_job_output.CancelMLDataProcessingJobOutput":
        """<p>Cancels a Neptune ML data processing job. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-dataprocessing.html">The <code>dataprocessing</code> command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelmldataprocessingjob">neptune-db:CancelMLDataProcessingJob</a> IAM action in that cluster.</p>

        Args:
            id: <p>The unique identifier of the data-processing job.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>
            clean: <p>If set to <code>TRUE</code>, this flag specifies that all Neptune ML S3 artifacts should be deleted when the job is stopped. The default is <code>FALSE</code>.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.cancel_ml_data_processing_job_input.CancelMLDataProcessingJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.cancel_ml_data_processing_job_output.CancelMLDataProcessingJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.cancel_ml_data_processing_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.cancel_ml_data_processing_job.async_cancel_ml_data_processing_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.cancel_ml_data_processing_job_input.CancelMLDataProcessingJobInput = {
            "id": id
        }
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn
        if clean is not None:
            input_["clean"] = clean

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_ml_model_training_job(
        self,
        id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        neptune_iam_role_arn: Optional[str] = None,
        clean: Optional[bool] = None,
    ) -> "capo_neptunedata.types.cancel_ml_model_training_job_output.CancelMLModelTrainingJobOutput":
        """<p>Cancels a Neptune ML model training job. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-modeltraining.html">Model training using the <code>modeltraining</code> command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelmlmodeltrainingjob">neptune-db:CancelMLModelTrainingJob</a> IAM action in that cluster.</p>

        Args:
            id: <p>The unique identifier of the model-training job to be canceled.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>
            clean: <p>If set to <code>TRUE</code>, this flag specifies that all Amazon S3 artifacts should be deleted when the job is stopped. The default is <code>FALSE</code>.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.cancel_ml_model_training_job_input.CancelMLModelTrainingJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.cancel_ml_model_training_job_output.CancelMLModelTrainingJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.cancel_ml_model_training_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.cancel_ml_model_training_job.async_cancel_ml_model_training_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.cancel_ml_model_training_job_input.CancelMLModelTrainingJobInput = {
            "id": id
        }
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn
        if clean is not None:
            input_["clean"] = clean

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_ml_model_transform_job(
        self,
        id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        neptune_iam_role_arn: Optional[str] = None,
        clean: Optional[bool] = None,
    ) -> "capo_neptunedata.types.cancel_ml_model_transform_job_output.CancelMLModelTransformJobOutput":
        """<p>Cancels a specified model transform job. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-model-transform.html">Use a trained model to generate new model artifacts</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelmlmodeltransformjob">neptune-db:CancelMLModelTransformJob</a> IAM action in that cluster.</p>

        Args:
            id: <p>The unique ID of the model transform job to be canceled.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>
            clean: <p>If this flag is set to <code>TRUE</code>, all Neptune ML S3 artifacts should be deleted when the job is stopped. The default is <code>FALSE</code>.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.cancel_ml_model_transform_job_input.CancelMLModelTransformJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.cancel_ml_model_transform_job_output.CancelMLModelTransformJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.cancel_ml_model_transform_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.cancel_ml_model_transform_job.async_cancel_ml_model_transform_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.cancel_ml_model_transform_job_input.CancelMLModelTransformJobInput = {
            "id": id
        }
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn
        if clean is not None:
            input_["clean"] = clean

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_open_cypher_query(
        self,
        query_id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        silent: Optional[bool] = None,
    ) -> "capo_neptunedata.types.cancel_open_cypher_query_output.CancelOpenCypherQueryOutput":
        """<p>Cancels a specified openCypher query. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-status.html">Neptune openCypher status endpoint</a> for more information.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelquery">neptune-db:CancelQuery</a> IAM action in that cluster.</p>

        Args:
            query_id: <p>The unique ID of the openCypher query to cancel.</p>
            silent: <p>If set to <code>TRUE</code>, causes the cancelation of the openCypher query to happen silently.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_numeric_data_exception.InvalidNumericDataException: <p>Raised when invalid numerical data is encountered when servicing a request.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.cancel_open_cypher_query_input.CancelOpenCypherQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.cancel_open_cypher_query_output.CancelOpenCypherQueryOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.cancel_open_cypher_query

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.cancel_open_cypher_query.async_cancel_open_cypher_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.cancel_open_cypher_query_input.CancelOpenCypherQueryInput = {
            "query_id": query_id
        }
        if silent is not None:
            input_["silent"] = silent

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ml_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        id: Optional[str] = None,
        ml_model_training_job_id: Optional[str] = None,
        ml_model_transform_job_id: Optional[str] = None,
        update: Optional[bool] = None,
        neptune_iam_role_arn: Optional[str] = None,
        model_name: Optional[str] = None,
        instance_type: Optional[str] = None,
        instance_count: Optional[int] = None,
        volume_encryption_kms_key: Optional[str] = None,
    ) -> "capo_neptunedata.types.create_ml_endpoint_output.CreateMLEndpointOutput":
        """<p>Creates a new Neptune ML inference endpoint that lets you query one specific model that the model-training process constructed. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-endpoints.html">Managing inference endpoints using the endpoints command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#createmlendpoint">neptune-db:CreateMLEndpoint</a> IAM action in that cluster.</p>

        Args:
            id: <p>A unique identifier for the new inference endpoint. The default is an autogenerated timestamped name.</p>
            ml_model_training_job_id: <p>The job Id of the completed model-training job that has created the model that the inference endpoint will point to. You must supply either the <code>mlModelTrainingJobId</code> or the <code>mlModelTransformJobId</code>.</p>
            ml_model_transform_job_id: <p>The job Id of the completed model-transform job. You must supply either the <code>mlModelTrainingJobId</code> or the <code>mlModelTransformJobId</code>.</p>
            update: <p>If set to <code>true</code>, <code>update</code> indicates that this is an update request. The default is <code>false</code>. You must supply either the <code>mlModelTrainingJobId</code> or the <code>mlModelTransformJobId</code>.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role providing Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will be thrown.</p>
            model_name: <p>Model type for training. By default the Neptune ML model is automatically based on the <code>modelType</code> used in data processing, but you can specify a different model type here. The default is <code>rgcn</code> for heterogeneous graphs and <code>kge</code> for knowledge graphs. The only valid value for heterogeneous graphs is <code>rgcn</code>. Valid values for knowledge graphs are: <code>kge</code>, <code>transe</code>, <code>distmult</code>, and <code>rotate</code>.</p>
            instance_type: <p>The type of Neptune ML instance to use for online servicing. The default is <code>ml.m5.xlarge</code>. Choosing the ML instance for an inference endpoint depends on the task type, the graph size, and your budget.</p>
            instance_count: <p>The minimum number of Amazon EC2 instances to deploy to an endpoint for prediction. The default is 1</p>
            volume_encryption_kms_key: <p>The Amazon Key Management Service (Amazon KMS) key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instances that run the training job. The default is None.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.create_ml_endpoint_input.CreateMLEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.create_ml_endpoint_output.CreateMLEndpointOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.create_ml_endpoint

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.create_ml_endpoint.async_create_ml_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.create_ml_endpoint_input.CreateMLEndpointInput = {}
        if id is not None:
            input_["id"] = id
        if ml_model_training_job_id is not None:
            input_["ml_model_training_job_id"] = ml_model_training_job_id
        if ml_model_transform_job_id is not None:
            input_["ml_model_transform_job_id"] = ml_model_transform_job_id
        if update is not None:
            input_["update"] = update
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn
        if model_name is not None:
            input_["model_name"] = model_name
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if instance_count is not None:
            input_["instance_count"] = instance_count
        if volume_encryption_kms_key is not None:
            input_["volume_encryption_kms_key"] = volume_encryption_kms_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ml_endpoint(
        self,
        id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        neptune_iam_role_arn: Optional[str] = None,
        clean: Optional[bool] = None,
    ) -> "capo_neptunedata.types.delete_ml_endpoint_output.DeleteMLEndpointOutput":
        """<p>Cancels the creation of a Neptune ML inference endpoint. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-endpoints.html">Managing inference endpoints using the endpoints command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletemlendpoint">neptune-db:DeleteMLEndpoint</a> IAM action in that cluster.</p>

        Args:
            id: <p>The unique identifier of the inference endpoint.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role providing Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will be thrown.</p>
            clean: <p>If this flag is set to <code>TRUE</code>, all Neptune ML S3 artifacts should be deleted when the job is stopped. The default is <code>FALSE</code>.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.delete_ml_endpoint_input.DeleteMLEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.delete_ml_endpoint_output.DeleteMLEndpointOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.delete_ml_endpoint

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.delete_ml_endpoint.async_delete_ml_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.delete_ml_endpoint_input.DeleteMLEndpointInput = {
            "id": id
        }
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn
        if clean is not None:
            input_["clean"] = clean

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_propertygraph_statistics(
        self, *, config_overrides: Optional[AsyncneptunedataClientConfig] = None
    ) -> "capo_neptunedata.types.delete_propertygraph_statistics_output.DeletePropertygraphStatisticsOutput":
        """<p>Deletes statistics for Gremlin and openCypher (property graph) data.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletestatistics">neptune-db:DeleteStatistics</a> IAM action in that cluster.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.statistics_not_available_exception.StatisticsNotAvailableException: <p>Raised when statistics needed to satisfy a request are not available.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.delete_propertygraph_statistics_output.DeletePropertygraphStatisticsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.delete_propertygraph_statistics

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.delete_propertygraph_statistics.async_delete_propertygraph_statistics(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_sparql_statistics(
        self, *, config_overrides: Optional[AsyncneptunedataClientConfig] = None
    ) -> "capo_neptunedata.types.delete_sparql_statistics_output.DeleteSparqlStatisticsOutput":
        """<p>Deletes SPARQL statistics</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletestatistics">neptune-db:DeleteStatistics</a> IAM action in that cluster.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.statistics_not_available_exception.StatisticsNotAvailableException: <p>Raised when statistics needed to satisfy a request are not available.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.delete_sparql_statistics_output.DeleteSparqlStatisticsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.delete_sparql_statistics

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.delete_sparql_statistics.async_delete_sparql_statistics(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_fast_reset(
        self,
        action: "capo_neptunedata.types.action.Action",
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        token: Optional[str] = None,
    ) -> "capo_neptunedata.types.execute_fast_reset_output.ExecuteFastResetOutput":
        """<p>The fast reset REST API lets you reset a Neptune graph quicky and easily, removing all of its data.</p> <p>Neptune fast reset is a two-step process. First you call <code>ExecuteFastReset</code> with <code>action</code> set to <code>initiateDatabaseReset</code>. This returns a UUID token which you then include when calling <code>ExecuteFastReset</code> again with <code>action</code> set to <code>performDatabaseReset</code>. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-fast-reset.html">Empty an Amazon Neptune DB cluster using the fast reset API</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#resetdatabase">neptune-db:ResetDatabase</a> IAM action in that cluster.</p>

        Args:
            action: <p>The fast reset action. One of the following values:</p> <ul> <li> <p> <b> <code>initiateDatabaseReset</code> </b> - This action generates a unique token needed to actually perform the fast reset.</p> </li> <li> <p> <b> <code>performDatabaseReset</code> </b> - This action uses the token generated by the <code>initiateDatabaseReset</code> action to actually perform the fast reset.</p> <p/> </li> </ul>
            token: <p>The fast-reset token to initiate the reset.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Raised when the HTTP method used by a request is not supported by the endpoint being used.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.server_shutdown_exception.ServerShutdownException: <p>Raised when the server shuts down while processing a request.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.execute_fast_reset_input.ExecuteFastResetInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.execute_fast_reset_output.ExecuteFastResetOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.execute_fast_reset

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.execute_fast_reset.async_execute_fast_reset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.execute_fast_reset_input.ExecuteFastResetInput = {
            "action": action
        }
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_gremlin_explain_query(
        self,
        gremlin_query: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
    ) -> "capo_neptunedata.types.execute_gremlin_explain_query_output.ExecuteGremlinExplainQueryOutput":
        """<p>Executes a Gremlin Explain query.</p> <p>Amazon Neptune has added a Gremlin feature named <code>explain</code> that provides is a self-service tool for understanding the execution approach being taken by the Neptune engine for the query. You invoke it by adding an <code>explain</code> parameter to an HTTP call that submits a Gremlin query.</p> <p>The explain feature provides information about the logical structure of query execution plans. You can use this information to identify potential evaluation and execution bottlenecks and to tune your query, as explained in <a href="https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-traversal-tuning.html">Tuning Gremlin queries</a>. You can also use query hints to improve query execution plans.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows one of the following IAM actions in that cluster, depending on the query:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery">neptune-db:ReadDataViaQuery</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#writedataviaquery">neptune-db:WriteDataViaQuery</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletedataviaquery">neptune-db:DeleteDataViaQuery</a> </p> </li> </ul> <p>Note that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:Gremlin</a> IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            gremlin_query: <p>The Gremlin explain query string.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.cancelled_by_user_exception.CancelledByUserException: <p>Raised when a user cancelled a request.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.malformed_query_exception.MalformedQueryException: <p>Raised when a query is submitted that is syntactically incorrect or does not pass additional validation.</p>
            capo_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException: <p>Raised when a request fails because of insufficient memory resources. The request can be retried.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.query_limit_exceeded_exception.QueryLimitExceededException: <p>Raised when the number of active queries exceeds what the server can process. The query in question can be retried when the system is less busy.</p>
            capo_neptunedata.errors.query_limit_exception.QueryLimitException: <p>Raised when the size of a query exceeds the system limit.</p>
            capo_neptunedata.errors.query_too_large_exception.QueryTooLargeException: <p>Raised when the body of a query is too large.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.execute_gremlin_explain_query_input.ExecuteGremlinExplainQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.execute_gremlin_explain_query_output.ExecuteGremlinExplainQueryOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.execute_gremlin_explain_query

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.execute_gremlin_explain_query.async_execute_gremlin_explain_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.execute_gremlin_explain_query_input.ExecuteGremlinExplainQueryInput = {
            "gremlin_query": gremlin_query
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_gremlin_profile_query(
        self,
        gremlin_query: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        results: Optional[bool] = None,
        chop: Optional[int] = None,
        serializer: Optional[str] = None,
        index_ops: Optional[bool] = None,
    ) -> "capo_neptunedata.types.execute_gremlin_profile_query_output.ExecuteGremlinProfileQueryOutput":
        """<p>Executes a Gremlin Profile query, which runs a specified traversal, collects various metrics about the run, and produces a profile report as output. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html">Gremlin profile API in Neptune</a> for details.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery">neptune-db:ReadDataViaQuery</a> IAM action in that cluster.</p> <p>Note that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:Gremlin</a> IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            gremlin_query: <p>The Gremlin query string to profile.</p>
            results: <p>If this flag is set to <code>TRUE</code>, the query results are gathered and displayed as part of the profile report. If <code>FALSE</code>, only the result count is displayed.</p>
            chop: <p>If non-zero, causes the results string to be truncated at that number of characters. If set to zero, the string contains all the results.</p>
            serializer: <p>If non-null, the gathered results are returned in a serialized response message in the format specified by this parameter. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html">Gremlin profile API in Neptune</a> for more information.</p>
            index_ops: <p>If this flag is set to <code>TRUE</code>, the results include a detailed report of all index operations that took place during query execution and serialization.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.cancelled_by_user_exception.CancelledByUserException: <p>Raised when a user cancelled a request.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.malformed_query_exception.MalformedQueryException: <p>Raised when a query is submitted that is syntactically incorrect or does not pass additional validation.</p>
            capo_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException: <p>Raised when a request fails because of insufficient memory resources. The request can be retried.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.query_limit_exceeded_exception.QueryLimitExceededException: <p>Raised when the number of active queries exceeds what the server can process. The query in question can be retried when the system is less busy.</p>
            capo_neptunedata.errors.query_limit_exception.QueryLimitException: <p>Raised when the size of a query exceeds the system limit.</p>
            capo_neptunedata.errors.query_too_large_exception.QueryTooLargeException: <p>Raised when the body of a query is too large.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.execute_gremlin_profile_query_input.ExecuteGremlinProfileQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.execute_gremlin_profile_query_output.ExecuteGremlinProfileQueryOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.execute_gremlin_profile_query

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.execute_gremlin_profile_query.async_execute_gremlin_profile_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.execute_gremlin_profile_query_input.ExecuteGremlinProfileQueryInput = {
            "gremlin_query": gremlin_query
        }
        if results is not None:
            input_["results"] = results
        if chop is not None:
            input_["chop"] = chop
        if serializer is not None:
            input_["serializer"] = serializer
        if index_ops is not None:
            input_["index_ops"] = index_ops

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_gremlin_query(
        self,
        gremlin_query: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        serializer: Optional[str] = None,
    ) -> (
        "capo_neptunedata.types.execute_gremlin_query_output.ExecuteGremlinQueryOutput"
    ):
        """<p>This commands executes a Gremlin query. Amazon Neptune is compatible with Apache TinkerPop3 and Gremlin, so you can use the Gremlin traversal language to query the graph, as described under <a href="https://tinkerpop.apache.org/docs/current/reference/#graph">The Graph</a> in the Apache TinkerPop3 documentation. More details can also be found in <a href="https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin.html">Accessing a Neptune graph with Gremlin</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that enables one of the following IAM actions in that cluster, depending on the query:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery">neptune-db:ReadDataViaQuery</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#writedataviaquery">neptune-db:WriteDataViaQuery</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletedataviaquery">neptune-db:DeleteDataViaQuery</a> </p> </li> </ul> <p>Note that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:Gremlin</a> IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            gremlin_query: <p>Using this API, you can run Gremlin queries in string format much as you can using the HTTP endpoint. The interface is compatible with whatever Gremlin version your DB cluster is using (see the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-client.html#best-practices-gremlin-java-latest">Tinkerpop client section</a> to determine which Gremlin releases your engine version supports).</p>
            serializer: <p>If non-null, the query results are returned in a serialized response message in the format specified by this parameter. See the <a href="https://tinkerpop.apache.org/docs/current/reference/#_graphson">GraphSON</a> section in the TinkerPop documentation for a list of the formats that are currently supported.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.cancelled_by_user_exception.CancelledByUserException: <p>Raised when a user cancelled a request.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.malformed_query_exception.MalformedQueryException: <p>Raised when a query is submitted that is syntactically incorrect or does not pass additional validation.</p>
            capo_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException: <p>Raised when a request fails because of insufficient memory resources. The request can be retried.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.query_limit_exceeded_exception.QueryLimitExceededException: <p>Raised when the number of active queries exceeds what the server can process. The query in question can be retried when the system is less busy.</p>
            capo_neptunedata.errors.query_limit_exception.QueryLimitException: <p>Raised when the size of a query exceeds the system limit.</p>
            capo_neptunedata.errors.query_too_large_exception.QueryTooLargeException: <p>Raised when the body of a query is too large.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.execute_gremlin_query_input.ExecuteGremlinQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.execute_gremlin_query_output.ExecuteGremlinQueryOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.execute_gremlin_query

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.execute_gremlin_query.async_execute_gremlin_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.execute_gremlin_query_input.ExecuteGremlinQueryInput = {
            "gremlin_query": gremlin_query
        }
        if serializer is not None:
            input_["serializer"] = serializer

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_open_cypher_explain_query(
        self,
        open_cypher_query: str,
        explain_mode: "capo_neptunedata.types.open_cypher_explain_mode.OpenCypherExplainMode",
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        parameters: Optional[str] = None,
    ) -> "capo_neptunedata.types.execute_open_cypher_explain_query_output.ExecuteOpenCypherExplainQueryOutput":
        """<p>Executes an openCypher <code>explain</code> request. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain.html">The openCypher explain feature</a> for more information.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery">neptune-db:ReadDataViaQuery</a> IAM action in that cluster.</p> <p>Note that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:OpenCypher</a> IAM condition key can be used in the policy document to restrict the use of openCypher queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            open_cypher_query: <p>The openCypher query string.</p>
            parameters: <p>The openCypher query parameters.</p>
            explain_mode: <p>The openCypher <code>explain</code> mode. Can be one of: <code>static</code>, <code>dynamic</code>, or <code>details</code>.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.cancelled_by_user_exception.CancelledByUserException: <p>Raised when a user cancelled a request.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_numeric_data_exception.InvalidNumericDataException: <p>Raised when invalid numerical data is encountered when servicing a request.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.malformed_query_exception.MalformedQueryException: <p>Raised when a query is submitted that is syntactically incorrect or does not pass additional validation.</p>
            capo_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException: <p>Raised when a request fails because of insufficient memory resources. The request can be retried.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.query_limit_exceeded_exception.QueryLimitExceededException: <p>Raised when the number of active queries exceeds what the server can process. The query in question can be retried when the system is less busy.</p>
            capo_neptunedata.errors.query_limit_exception.QueryLimitException: <p>Raised when the size of a query exceeds the system limit.</p>
            capo_neptunedata.errors.query_too_large_exception.QueryTooLargeException: <p>Raised when the body of a query is too large.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.execute_open_cypher_explain_query_input.ExecuteOpenCypherExplainQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.execute_open_cypher_explain_query_output.ExecuteOpenCypherExplainQueryOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.execute_open_cypher_explain_query

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.execute_open_cypher_explain_query.async_execute_open_cypher_explain_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.execute_open_cypher_explain_query_input.ExecuteOpenCypherExplainQueryInput = {
            "open_cypher_query": open_cypher_query,
            "explain_mode": explain_mode,
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_open_cypher_query(
        self,
        open_cypher_query: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        parameters: Optional[str] = None,
    ) -> "capo_neptunedata.types.execute_open_cypher_query_output.ExecuteOpenCypherQueryOutput":
        """<p>Executes an openCypher query. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html">Accessing the Neptune Graph with openCypher</a> for more information.</p> <p>Neptune supports building graph applications using openCypher, which is currently one of the most popular query languages among developers working with graph databases. Developers, business analysts, and data scientists like openCypher's declarative, SQL-inspired syntax because it provides a familiar structure in which to querying property graphs.</p> <p>The openCypher language was originally developed by Neo4j, then open-sourced in 2015 and contributed to the <a href="https://opencypher.org/">openCypher project</a> under an Apache 2 open-source license.</p> <p>Note that when invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows one of the following IAM actions in that cluster, depending on the query:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery">neptune-db:ReadDataViaQuery</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#writedataviaquery">neptune-db:WriteDataViaQuery</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletedataviaquery">neptune-db:DeleteDataViaQuery</a> </p> </li> </ul> <p>Note also that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:OpenCypher</a> IAM condition key can be used in the policy document to restrict the use of openCypher queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            open_cypher_query: <p>The openCypher query string to be executed.</p>
            parameters: <p>The openCypher query parameters for query execution. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-parameterized-queries.html">Examples of openCypher parameterized queries</a> for more information.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.cancelled_by_user_exception.CancelledByUserException: <p>Raised when a user cancelled a request.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_numeric_data_exception.InvalidNumericDataException: <p>Raised when invalid numerical data is encountered when servicing a request.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.malformed_query_exception.MalformedQueryException: <p>Raised when a query is submitted that is syntactically incorrect or does not pass additional validation.</p>
            capo_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException: <p>Raised when a request fails because of insufficient memory resources. The request can be retried.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.query_limit_exceeded_exception.QueryLimitExceededException: <p>Raised when the number of active queries exceeds what the server can process. The query in question can be retried when the system is less busy.</p>
            capo_neptunedata.errors.query_limit_exception.QueryLimitException: <p>Raised when the size of a query exceeds the system limit.</p>
            capo_neptunedata.errors.query_too_large_exception.QueryTooLargeException: <p>Raised when the body of a query is too large.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.execute_open_cypher_query_input.ExecuteOpenCypherQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.execute_open_cypher_query_output.ExecuteOpenCypherQueryOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.execute_open_cypher_query

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.execute_open_cypher_query.async_execute_open_cypher_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.execute_open_cypher_query_input.ExecuteOpenCypherQueryInput = {
            "open_cypher_query": open_cypher_query
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_engine_status(
        self, *, config_overrides: Optional[AsyncneptunedataClientConfig] = None
    ) -> "capo_neptunedata.types.get_engine_status_output.GetEngineStatusOutput":
        """<p>Retrieves the status of the graph database on the host.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getenginestatus">neptune-db:GetEngineStatus</a> IAM action in that cluster.</p>

        Raises:
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.internal_failure_exception.InternalFailureException: <p>Raised when the processing of the request failed unexpectedly.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_engine_status_output.GetEngineStatusOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_engine_status

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_engine_status.async_get_engine_status(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_gremlin_query_status(
        self,
        query_id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
    ) -> "capo_neptunedata.types.get_gremlin_query_status_output.GetGremlinQueryStatusOutput":
        """<p>Gets the status of a specified Gremlin query.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus">neptune-db:GetQueryStatus</a> IAM action in that cluster.</p> <p>Note that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:Gremlin</a> IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            query_id: <p>The unique identifier that identifies the Gremlin query.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_gremlin_query_status_input.GetGremlinQueryStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_gremlin_query_status_output.GetGremlinQueryStatusOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_gremlin_query_status

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_gremlin_query_status.async_get_gremlin_query_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_gremlin_query_status_input.GetGremlinQueryStatusInput = {
            "query_id": query_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_loader_job_status(
        self,
        load_id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        details: Optional[bool] = None,
        errors: Optional[bool] = None,
        page: Optional[
            "capo_neptunedata.types.positive_integer.PositiveInteger"
        ] = None,
        errors_per_page: Optional[
            "capo_neptunedata.types.positive_integer.PositiveInteger"
        ] = None,
    ) -> "capo_neptunedata.types.get_loader_job_status_output.GetLoaderJobStatusOutput":
        """<p>Gets status information about a specified load job. Neptune keeps track of the most recent 1,024 bulk load jobs, and stores the last 10,000 error details per job.</p> <p>See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-status.htm">Neptune Loader Get-Status API</a> for more information.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getloaderjobstatus">neptune-db:GetLoaderJobStatus</a> IAM action in that cluster..</p>

        Args:
            load_id: <p>The load ID of the load job to get the status of.</p>
            details: <p>Flag indicating whether or not to include details beyond the overall status (<code>TRUE</code> or <code>FALSE</code>; the default is <code>FALSE</code>).</p>
            errors: <p>Flag indicating whether or not to include a list of errors encountered (<code>TRUE</code> or <code>FALSE</code>; the default is <code>FALSE</code>).</p> <p>The list of errors is paged. The <code>page</code> and <code>errorsPerPage</code> parameters allow you to page through all the errors.</p>
            page: <p>The error page number (a positive integer; the default is <code>1</code>). Only valid when the <code>errors</code> parameter is set to <code>TRUE</code>.</p>
            errors_per_page: <p>The number of errors returned in each page (a positive integer; the default is <code>10</code>). Only valid when the <code>errors</code> parameter set to <code>TRUE</code>.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.bulk_load_id_not_found_exception.BulkLoadIdNotFoundException: <p>Raised when a specified bulk-load job ID cannot be found.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.internal_failure_exception.InternalFailureException: <p>Raised when the processing of the request failed unexpectedly.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.load_url_access_denied_exception.LoadUrlAccessDeniedException: <p>Raised when access is denied to a specified load URL.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_loader_job_status_input.GetLoaderJobStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_loader_job_status_output.GetLoaderJobStatusOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_loader_job_status

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_loader_job_status.async_get_loader_job_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_loader_job_status_input.GetLoaderJobStatusInput = {
            "load_id": load_id
        }
        if details is not None:
            input_["details"] = details
        if errors is not None:
            input_["errors"] = errors
        if page is not None:
            input_["page"] = page
        if errors_per_page is not None:
            input_["errors_per_page"] = errors_per_page

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ml_data_processing_job(
        self,
        id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        neptune_iam_role_arn: Optional[str] = None,
    ) -> "capo_neptunedata.types.get_ml_data_processing_job_output.GetMLDataProcessingJobOutput":
        """<p>Retrieves information about a specified data processing job. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-dataprocessing.html">The <code>dataprocessing</code> command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getmldataprocessingjobstatus">neptune-db:neptune-db:GetMLDataProcessingJobStatus</a> IAM action in that cluster.</p>

        Args:
            id: <p>The unique identifier of the data-processing job to be retrieved.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_ml_data_processing_job_input.GetMLDataProcessingJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_ml_data_processing_job_output.GetMLDataProcessingJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_ml_data_processing_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_ml_data_processing_job.async_get_ml_data_processing_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_ml_data_processing_job_input.GetMLDataProcessingJobInput = {
            "id": id
        }
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ml_endpoint(
        self,
        id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        neptune_iam_role_arn: Optional[str] = None,
    ) -> "capo_neptunedata.types.get_ml_endpoint_output.GetMLEndpointOutput":
        """<p>Retrieves details about an inference endpoint. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-endpoints.html">Managing inference endpoints using the endpoints command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getmlendpointstatus">neptune-db:GetMLEndpointStatus</a> IAM action in that cluster.</p>

        Args:
            id: <p>The unique identifier of the inference endpoint.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_ml_endpoint_input.GetMLEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_ml_endpoint_output.GetMLEndpointOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_ml_endpoint

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_ml_endpoint.async_get_ml_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_ml_endpoint_input.GetMLEndpointInput = {
            "id": id
        }
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ml_model_training_job(
        self,
        id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        neptune_iam_role_arn: Optional[str] = None,
    ) -> "capo_neptunedata.types.get_ml_model_training_job_output.GetMLModelTrainingJobOutput":
        """<p>Retrieves information about a Neptune ML model training job. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-modeltraining.html">Model training using the <code>modeltraining</code> command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getmlmodeltrainingjobstatus">neptune-db:GetMLModelTrainingJobStatus</a> IAM action in that cluster.</p>

        Args:
            id: <p>The unique identifier of the model-training job to retrieve.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_ml_model_training_job_input.GetMLModelTrainingJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_ml_model_training_job_output.GetMLModelTrainingJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_ml_model_training_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_ml_model_training_job.async_get_ml_model_training_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_ml_model_training_job_input.GetMLModelTrainingJobInput = {
            "id": id
        }
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ml_model_transform_job(
        self,
        id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        neptune_iam_role_arn: Optional[str] = None,
    ) -> "capo_neptunedata.types.get_ml_model_transform_job_output.GetMLModelTransformJobOutput":
        """<p>Gets information about a specified model transform job. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-model-transform.html">Use a trained model to generate new model artifacts</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getmlmodeltransformjobstatus">neptune-db:GetMLModelTransformJobStatus</a> IAM action in that cluster.</p>

        Args:
            id: <p>The unique identifier of the model-transform job to be reetrieved.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_ml_model_transform_job_input.GetMLModelTransformJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_ml_model_transform_job_output.GetMLModelTransformJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_ml_model_transform_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_ml_model_transform_job.async_get_ml_model_transform_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_ml_model_transform_job_input.GetMLModelTransformJobInput = {
            "id": id
        }
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_open_cypher_query_status(
        self,
        query_id: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
    ) -> "capo_neptunedata.types.get_open_cypher_query_status_output.GetOpenCypherQueryStatusOutput":
        """<p>Retrieves the status of a specified openCypher query.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus">neptune-db:GetQueryStatus</a> IAM action in that cluster.</p> <p>Note that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:OpenCypher</a> IAM condition key can be used in the policy document to restrict the use of openCypher queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            query_id: <p>The unique ID of the openCypher query for which to retrieve the query status.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_numeric_data_exception.InvalidNumericDataException: <p>Raised when invalid numerical data is encountered when servicing a request.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_open_cypher_query_status_input.GetOpenCypherQueryStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_open_cypher_query_status_output.GetOpenCypherQueryStatusOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_open_cypher_query_status

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_open_cypher_query_status.async_get_open_cypher_query_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_open_cypher_query_status_input.GetOpenCypherQueryStatusInput = {
            "query_id": query_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_propertygraph_statistics(
        self, *, config_overrides: Optional[AsyncneptunedataClientConfig] = None
    ) -> "capo_neptunedata.types.get_propertygraph_statistics_output.GetPropertygraphStatisticsOutput":
        """<p>Gets property graph statistics (Gremlin and openCypher).</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstatisticsstatus">neptune-db:GetStatisticsStatus</a> IAM action in that cluster.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.statistics_not_available_exception.StatisticsNotAvailableException: <p>Raised when statistics needed to satisfy a request are not available.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_propertygraph_statistics_output.GetPropertygraphStatisticsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_propertygraph_statistics

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_propertygraph_statistics.async_get_propertygraph_statistics(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_propertygraph_stream(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        limit: Optional[int] = None,
        iterator_type: Optional[
            "capo_neptunedata.types.iterator_type.IteratorType"
        ] = None,
        commit_num: Optional[int] = None,
        op_num: Optional[int] = None,
        encoding: Optional["capo_neptunedata.types.encoding.Encoding"] = None,
    ) -> "capo_neptunedata.types.get_propertygraph_stream_output.GetPropertygraphStreamOutput":
        """<p>Gets a stream for a property graph.</p> <p>With the Neptune Streams feature, you can generate a complete sequence of change-log entries that record every change made to your graph data as it happens. <code>GetPropertygraphStream</code> lets you collect these change-log entries for a property graph.</p> <p>The Neptune streams feature needs to be enabled on your Neptune DBcluster. To enable streams, set the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html#parameters-db-cluster-parameters-neptune_streams">neptune_streams</a> DB cluster parameter to <code>1</code>.</p> <p>See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/streams.html">Capturing graph changes in real time using Neptune streams</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstreamrecords">neptune-db:GetStreamRecords</a> IAM action in that cluster.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that enables one of the following IAM actions, depending on the query:</p> <p>Note that you can restrict property-graph queries using the following IAM context keys:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:Gremlin</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:OpenCypher</a> </p> </li> </ul> <p>See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            limit: <p>Specifies the maximum number of records to return. There is also a size limit of 10 MB on the response that can't be modified and that takes precedence over the number of records specified in the <code>limit</code> parameter. The response does include a threshold-breaching record if the 10 MB limit was reached.</p> <p>The range for <code>limit</code> is 1 to 100,000, with a default of 10.</p>
            iterator_type: <p>Can be one of:</p> <ul> <li> <p> <code>AT_SEQUENCE_NUMBER</code> - Indicates that reading should start from the event sequence number specified jointly by the <code>commitNum</code> and <code>opNum</code> parameters.</p> </li> <li> <p> <code>AFTER_SEQUENCE_NUMBER</code> - Indicates that reading should start right after the event sequence number specified jointly by the <code>commitNum</code> and <code>opNum</code> parameters.</p> </li> <li> <p> <code>TRIM_HORIZON</code> - Indicates that reading should start at the last untrimmed record in the system, which is the oldest unexpired (not yet deleted) record in the change-log stream.</p> </li> <li> <p> <code>LATEST</code> - Indicates that reading should start at the most recent record in the system, which is the latest unexpired (not yet deleted) record in the change-log stream.</p> </li> </ul>
            commit_num: <p>The commit number of the starting record to read from the change-log stream. This parameter is required when <code>iteratorType</code> is<code>AT_SEQUENCE_NUMBER</code> or <code>AFTER_SEQUENCE_NUMBER</code>, and ignored when <code>iteratorType</code> is <code>TRIM_HORIZON</code> or <code>LATEST</code>.</p>
            op_num: <p>The operation sequence number within the specified commit to start reading from in the change-log stream data. The default is <code>1</code>.</p>
            encoding: <p>If set to TRUE, Neptune compresses the response using gzip encoding.</p>

        Raises:
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.expired_stream_exception.ExpiredStreamException: <p>Raised when a request attempts to access an stream that has expired.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException: <p>Raised when a request fails because of insufficient memory resources. The request can be retried.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.stream_records_not_found_exception.StreamRecordsNotFoundException: <p>Raised when stream records requested by a query cannot be found.</p>
            capo_neptunedata.errors.throttling_exception.ThrottlingException: <p>Raised when the rate of requests exceeds the maximum throughput. Requests can be retried after encountering this exception.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_propertygraph_stream_input.GetPropertygraphStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_propertygraph_stream_output.GetPropertygraphStreamOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_propertygraph_stream

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_propertygraph_stream.async_get_propertygraph_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_propertygraph_stream_input.GetPropertygraphStreamInput = {}
        if limit is not None:
            input_["limit"] = limit
        if iterator_type is not None:
            input_["iterator_type"] = iterator_type
        if commit_num is not None:
            input_["commit_num"] = commit_num
        if op_num is not None:
            input_["op_num"] = op_num
        if encoding is not None:
            input_["encoding"] = encoding

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_propertygraph_summary(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        mode: Optional[
            "capo_neptunedata.types.graph_summary_type.GraphSummaryType"
        ] = None,
    ) -> "capo_neptunedata.types.get_propertygraph_summary_output.GetPropertygraphSummaryOutput":
        """<p>Gets a graph summary for a property graph.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getgraphsummary">neptune-db:GetGraphSummary</a> IAM action in that cluster.</p>

        Args:
            mode: <p>Mode can take one of two values: <code>BASIC</code> (the default), and <code>DETAILED</code>.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.statistics_not_available_exception.StatisticsNotAvailableException: <p>Raised when statistics needed to satisfy a request are not available.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_propertygraph_summary_input.GetPropertygraphSummaryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_propertygraph_summary_output.GetPropertygraphSummaryOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_propertygraph_summary

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_propertygraph_summary.async_get_propertygraph_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_propertygraph_summary_input.GetPropertygraphSummaryInput = {}
        if mode is not None:
            input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_rdf_graph_summary(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        mode: Optional[
            "capo_neptunedata.types.graph_summary_type.GraphSummaryType"
        ] = None,
    ) -> "capo_neptunedata.types.get_rdf_graph_summary_output.GetRDFGraphSummaryOutput":
        """<p>Gets a graph summary for an RDF graph.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getgraphsummary">neptune-db:GetGraphSummary</a> IAM action in that cluster.</p>

        Args:
            mode: <p>Mode can take one of two values: <code>BASIC</code> (the default), and <code>DETAILED</code>.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.statistics_not_available_exception.StatisticsNotAvailableException: <p>Raised when statistics needed to satisfy a request are not available.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_rdf_graph_summary_input.GetRDFGraphSummaryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_rdf_graph_summary_output.GetRDFGraphSummaryOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_rdf_graph_summary

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_rdf_graph_summary.async_get_rdf_graph_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_rdf_graph_summary_input.GetRDFGraphSummaryInput = {}
        if mode is not None:
            input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_sparql_statistics(
        self, *, config_overrides: Optional[AsyncneptunedataClientConfig] = None
    ) -> (
        "capo_neptunedata.types.get_sparql_statistics_output.GetSparqlStatisticsOutput"
    ):
        """<p>Gets RDF statistics (SPARQL).</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.statistics_not_available_exception.StatisticsNotAvailableException: <p>Raised when statistics needed to satisfy a request are not available.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_sparql_statistics_output.GetSparqlStatisticsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_sparql_statistics

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_sparql_statistics.async_get_sparql_statistics(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_sparql_stream(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        limit: Optional[int] = None,
        iterator_type: Optional[
            "capo_neptunedata.types.iterator_type.IteratorType"
        ] = None,
        commit_num: Optional[int] = None,
        op_num: Optional[int] = None,
        encoding: Optional["capo_neptunedata.types.encoding.Encoding"] = None,
    ) -> "capo_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput":
        """<p>Gets a stream for an RDF graph.</p> <p>With the Neptune Streams feature, you can generate a complete sequence of change-log entries that record every change made to your graph data as it happens. <code>GetSparqlStream</code> lets you collect these change-log entries for an RDF graph.</p> <p>The Neptune streams feature needs to be enabled on your Neptune DBcluster. To enable streams, set the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html#parameters-db-cluster-parameters-neptune_streams">neptune_streams</a> DB cluster parameter to <code>1</code>.</p> <p>See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/streams.html">Capturing graph changes in real time using Neptune streams</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstreamrecords">neptune-db:GetStreamRecords</a> IAM action in that cluster.</p> <p>Note that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:Sparql</a> IAM condition key can be used in the policy document to restrict the use of SPARQL queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            limit: <p>Specifies the maximum number of records to return. There is also a size limit of 10 MB on the response that can't be modified and that takes precedence over the number of records specified in the <code>limit</code> parameter. The response does include a threshold-breaching record if the 10 MB limit was reached.</p> <p>The range for <code>limit</code> is 1 to 100,000, with a default of 10.</p>
            iterator_type: <p>Can be one of:</p> <ul> <li> <p> <code>AT_SEQUENCE_NUMBER</code> - Indicates that reading should start from the event sequence number specified jointly by the <code>commitNum</code> and <code>opNum</code> parameters.</p> </li> <li> <p> <code>AFTER_SEQUENCE_NUMBER</code> - Indicates that reading should start right after the event sequence number specified jointly by the <code>commitNum</code> and <code>opNum</code> parameters.</p> </li> <li> <p> <code>TRIM_HORIZON</code> - Indicates that reading should start at the last untrimmed record in the system, which is the oldest unexpired (not yet deleted) record in the change-log stream.</p> </li> <li> <p> <code>LATEST</code> - Indicates that reading should start at the most recent record in the system, which is the latest unexpired (not yet deleted) record in the change-log stream.</p> </li> </ul>
            commit_num: <p>The commit number of the starting record to read from the change-log stream. This parameter is required when <code>iteratorType</code> is<code>AT_SEQUENCE_NUMBER</code> or <code>AFTER_SEQUENCE_NUMBER</code>, and ignored when <code>iteratorType</code> is <code>TRIM_HORIZON</code> or <code>LATEST</code>.</p>
            op_num: <p>The operation sequence number within the specified commit to start reading from in the change-log stream data. The default is <code>1</code>.</p>
            encoding: <p>If set to TRUE, Neptune compresses the response using gzip encoding.</p>

        Raises:
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.expired_stream_exception.ExpiredStreamException: <p>Raised when a request attempts to access an stream that has expired.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException: <p>Raised when a request fails because of insufficient memory resources. The request can be retried.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.stream_records_not_found_exception.StreamRecordsNotFoundException: <p>Raised when stream records requested by a query cannot be found.</p>
            capo_neptunedata.errors.throttling_exception.ThrottlingException: <p>Raised when the rate of requests exceeds the maximum throughput. Requests can be retried after encountering this exception.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.get_sparql_stream_input.GetSparqlStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.get_sparql_stream

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.get_sparql_stream.async_get_sparql_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.get_sparql_stream_input.GetSparqlStreamInput = {}
        if limit is not None:
            input_["limit"] = limit
        if iterator_type is not None:
            input_["iterator_type"] = iterator_type
        if commit_num is not None:
            input_["commit_num"] = commit_num
        if op_num is not None:
            input_["op_num"] = op_num
        if encoding is not None:
            input_["encoding"] = encoding

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_gremlin_queries(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        include_waiting: Optional[bool] = None,
    ) -> "capo_neptunedata.types.list_gremlin_queries_output.ListGremlinQueriesOutput":
        """<p>Lists active Gremlin queries. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status.html">Gremlin query status API</a> for details about the output.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus">neptune-db:GetQueryStatus</a> IAM action in that cluster.</p> <p>Note that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:Gremlin</a> IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            include_waiting: <p>If set to <code>TRUE</code>, the list returned includes waiting queries. The default is <code>FALSE</code>;</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.list_gremlin_queries_input.ListGremlinQueriesInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.list_gremlin_queries_output.ListGremlinQueriesOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.list_gremlin_queries

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.list_gremlin_queries.async_list_gremlin_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.list_gremlin_queries_input.ListGremlinQueriesInput = {}
        if include_waiting is not None:
            input_["include_waiting"] = include_waiting

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_loader_jobs(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        limit: Optional[
            "capo_neptunedata.types.positive_integer.PositiveInteger"
        ] = None,
        include_queued_loads: Optional[bool] = None,
    ) -> "capo_neptunedata.types.list_loader_jobs_output.ListLoaderJobsOutput":
        """<p>Retrieves a list of the <code>loadIds</code> for all active loader jobs.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listloaderjobs">neptune-db:ListLoaderJobs</a> IAM action in that cluster..</p>

        Args:
            limit: <p>The number of load IDs to list. Must be a positive integer greater than zero and not more than <code>100</code> (which is the default).</p>
            include_queued_loads: <p>An optional parameter that can be used to exclude the load IDs of queued load requests when requesting a list of load IDs by setting the parameter to <code>FALSE</code>. The default value is <code>TRUE</code>.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.bulk_load_id_not_found_exception.BulkLoadIdNotFoundException: <p>Raised when a specified bulk-load job ID cannot be found.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.internal_failure_exception.InternalFailureException: <p>Raised when the processing of the request failed unexpectedly.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.load_url_access_denied_exception.LoadUrlAccessDeniedException: <p>Raised when access is denied to a specified load URL.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.list_loader_jobs_input.ListLoaderJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.list_loader_jobs_output.ListLoaderJobsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.list_loader_jobs

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.list_loader_jobs.async_list_loader_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.list_loader_jobs_input.ListLoaderJobsInput = {}
        if limit is not None:
            input_["limit"] = limit
        if include_queued_loads is not None:
            input_["include_queued_loads"] = include_queued_loads

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ml_data_processing_jobs(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        max_items: Optional[
            "capo_neptunedata.types.positive_integer.PositiveInteger"
        ] = None,
        neptune_iam_role_arn: Optional[str] = None,
    ) -> "capo_neptunedata.types.list_ml_data_processing_jobs_output.ListMLDataProcessingJobsOutput":
        """<p>Returns a list of Neptune ML data processing jobs. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-dataprocessing.html#machine-learning-api-dataprocessing-list-jobs">Listing active data-processing jobs using the Neptune ML dataprocessing command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listmldataprocessingjobs">neptune-db:ListMLDataProcessingJobs</a> IAM action in that cluster.</p>

        Args:
            max_items: <p>The maximum number of items to return (from 1 to 1024; the default is 10).</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.list_ml_data_processing_jobs_input.ListMLDataProcessingJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.list_ml_data_processing_jobs_output.ListMLDataProcessingJobsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.list_ml_data_processing_jobs

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.list_ml_data_processing_jobs.async_list_ml_data_processing_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.list_ml_data_processing_jobs_input.ListMLDataProcessingJobsInput = {}
        if max_items is not None:
            input_["max_items"] = max_items
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ml_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        max_items: Optional[
            "capo_neptunedata.types.positive_integer.PositiveInteger"
        ] = None,
        neptune_iam_role_arn: Optional[str] = None,
    ) -> "capo_neptunedata.types.list_ml_endpoints_output.ListMLEndpointsOutput":
        """<p>Lists existing inference endpoints. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-endpoints.html">Managing inference endpoints using the endpoints command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listmlendpoints">neptune-db:ListMLEndpoints</a> IAM action in that cluster.</p>

        Args:
            max_items: <p>The maximum number of items to return (from 1 to 1024; the default is 10.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.list_ml_endpoints_input.ListMLEndpointsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.list_ml_endpoints_output.ListMLEndpointsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.list_ml_endpoints

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.list_ml_endpoints.async_list_ml_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.list_ml_endpoints_input.ListMLEndpointsInput = {}
        if max_items is not None:
            input_["max_items"] = max_items
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ml_model_training_jobs(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        max_items: Optional[
            "capo_neptunedata.types.positive_integer.PositiveInteger"
        ] = None,
        neptune_iam_role_arn: Optional[str] = None,
    ) -> "capo_neptunedata.types.list_ml_model_training_jobs_output.ListMLModelTrainingJobsOutput":
        """<p>Lists Neptune ML model-training jobs. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-modeltraining.html">Model training using the <code>modeltraining</code> command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#neptune-db:listmlmodeltrainingjobs">neptune-db:neptune-db:ListMLModelTrainingJobs</a> IAM action in that cluster.</p>

        Args:
            max_items: <p>The maximum number of items to return (from 1 to 1024; the default is 10).</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.list_ml_model_training_jobs_input.ListMLModelTrainingJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.list_ml_model_training_jobs_output.ListMLModelTrainingJobsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.list_ml_model_training_jobs

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.list_ml_model_training_jobs.async_list_ml_model_training_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.list_ml_model_training_jobs_input.ListMLModelTrainingJobsInput = {}
        if max_items is not None:
            input_["max_items"] = max_items
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ml_model_transform_jobs(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        max_items: Optional[
            "capo_neptunedata.types.positive_integer.PositiveInteger"
        ] = None,
        neptune_iam_role_arn: Optional[str] = None,
    ) -> "capo_neptunedata.types.list_ml_model_transform_jobs_output.ListMLModelTransformJobsOutput":
        """<p>Returns a list of model transform job IDs. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-model-transform.html">Use a trained model to generate new model artifacts</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listmlmodeltransformjobs">neptune-db:ListMLModelTransformJobs</a> IAM action in that cluster.</p>

        Args:
            max_items: <p>The maximum number of items to return (from 1 to 1024; the default is 10).</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.list_ml_model_transform_jobs_input.ListMLModelTransformJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.list_ml_model_transform_jobs_output.ListMLModelTransformJobsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.list_ml_model_transform_jobs

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.list_ml_model_transform_jobs.async_list_ml_model_transform_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.list_ml_model_transform_jobs_input.ListMLModelTransformJobsInput = {}
        if max_items is not None:
            input_["max_items"] = max_items
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_open_cypher_queries(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        include_waiting: Optional[bool] = None,
    ) -> "capo_neptunedata.types.list_open_cypher_queries_output.ListOpenCypherQueriesOutput":
        """<p>Lists active openCypher queries. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-status.html">Neptune openCypher status endpoint</a> for more information.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus">neptune-db:GetQueryStatus</a> IAM action in that cluster.</p> <p>Note that the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys">neptune-db:QueryLanguage:OpenCypher</a> IAM condition key can be used in the policy document to restrict the use of openCypher queries (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html">Condition keys available in Neptune IAM data-access policy statements</a>).</p>

        Args:
            include_waiting: <p> When set to <code>TRUE</code> and other parameters are not present, causes status information to be returned for waiting queries as well as for running queries.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Raised when a request attempts to modify data that is concurrently being modified by another process.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException: <p>Raised when a request fails.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_numeric_data_exception.InvalidNumericDataException: <p>Raised when invalid numerical data is encountered when servicing a request.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.parsing_exception.ParsingException: <p>Raised when a parsing issue is encountered.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException: <p>Raised when the an operation exceeds the time limit allowed for it.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.list_open_cypher_queries_input.ListOpenCypherQueriesInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.list_open_cypher_queries_output.ListOpenCypherQueriesOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.list_open_cypher_queries

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.list_open_cypher_queries.async_list_open_cypher_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.list_open_cypher_queries_input.ListOpenCypherQueriesInput = {}
        if include_waiting is not None:
            input_["include_waiting"] = include_waiting

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def manage_propertygraph_statistics(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        mode: Optional[
            "capo_neptunedata.types.statistics_auto_generation_mode.StatisticsAutoGenerationMode"
        ] = None,
    ) -> "capo_neptunedata.types.manage_propertygraph_statistics_output.ManagePropertygraphStatisticsOutput":
        """<p>Manages the generation and use of property graph statistics.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#managestatistics">neptune-db:ManageStatistics</a> IAM action in that cluster.</p>

        Args:
            mode: <p>The statistics generation mode. One of: <code>DISABLE_AUTOCOMPUTE</code>, <code>ENABLE_AUTOCOMPUTE</code>, or <code>REFRESH</code>, the last of which manually triggers DFE statistics generation.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.statistics_not_available_exception.StatisticsNotAvailableException: <p>Raised when statistics needed to satisfy a request are not available.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.manage_propertygraph_statistics_input.ManagePropertygraphStatisticsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.manage_propertygraph_statistics_output.ManagePropertygraphStatisticsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.manage_propertygraph_statistics

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.manage_propertygraph_statistics.async_manage_propertygraph_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.manage_propertygraph_statistics_input.ManagePropertygraphStatisticsInput = {}
        if mode is not None:
            input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def manage_sparql_statistics(
        self,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        mode: Optional[
            "capo_neptunedata.types.statistics_auto_generation_mode.StatisticsAutoGenerationMode"
        ] = None,
    ) -> "capo_neptunedata.types.manage_sparql_statistics_output.ManageSparqlStatisticsOutput":
        """<p>Manages the generation and use of RDF graph statistics.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#managestatistics">neptune-db:ManageStatistics</a> IAM action in that cluster.</p>

        Args:
            mode: <p>The statistics generation mode. One of: <code>DISABLE_AUTOCOMPUTE</code>, <code>ENABLE_AUTOCOMPUTE</code>, or <code>REFRESH</code>, the last of which manually triggers DFE statistics generation.</p>

        Raises:
            capo_neptunedata.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException: <p>Raised when a request attempts to write to a read-only resource.</p>
            capo_neptunedata.errors.statistics_not_available_exception.StatisticsNotAvailableException: <p>Raised when statistics needed to satisfy a request are not available.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.manage_sparql_statistics_input.ManageSparqlStatisticsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.manage_sparql_statistics_output.ManageSparqlStatisticsOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.manage_sparql_statistics

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.manage_sparql_statistics.async_manage_sparql_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.manage_sparql_statistics_input.ManageSparqlStatisticsInput = {}
        if mode is not None:
            input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_loader_job(
        self,
        source: str,
        format: "capo_neptunedata.types.format.Format",
        s3_bucket_region: "capo_neptunedata.types.s3_bucket_region.S3BucketRegion",
        iam_role_arn: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        mode: Optional["capo_neptunedata.types.mode.Mode"] = None,
        fail_on_error: Optional[bool] = None,
        parallelism: Optional["capo_neptunedata.types.parallelism.Parallelism"] = None,
        parser_configuration: Optional[
            "capo_neptunedata.types.string_valued_map.StringValuedMap"
        ] = None,
        update_single_cardinality_properties: Optional[bool] = None,
        queue_request: Optional[bool] = None,
        dependencies: Optional["capo_neptunedata.types.string_list.StringList"] = None,
        user_provided_edge_ids: Optional[bool] = None,
        edge_only_load: Optional[bool] = None,
    ) -> "capo_neptunedata.types.start_loader_job_output.StartLoaderJobOutput":
        r"""<p>Starts a Neptune bulk loader job to load data from an Amazon S3 bucket into a Neptune DB instance. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html">Using the Amazon Neptune Bulk Loader to Ingest Data</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startloaderjob">neptune-db:StartLoaderJob</a> IAM action in that cluster.</p>

        Args:
            source: <p>The <code>source</code> parameter accepts an S3 URI that identifies a single file, multiple files, a folder, or multiple folders. Neptune loads every data file in any folder that is specified.</p> <p>The URI can be in any of the following formats.</p> <ul> <li> <p> <code>s3://(bucket_name)/(object-key-name)</code> </p> </li> <li> <p> <code>https://s3.amazonaws.com/(bucket_name)/(object-key-name)</code> </p> </li> <li> <p> <code>https://s3.us-east-1.amazonaws.com/(bucket_name)/(object-key-name)</code> </p> </li> </ul> <p>The <code>object-key-name</code> element of the URI is equivalent to the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html#API_ListObjects_RequestParameters">prefix</a> parameter in an S3 <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html">ListObjects</a> API call. It identifies all the objects in the specified S3 bucket whose names begin with that prefix. That can be a single file or folder, or multiple files and/or folders.</p> <p>The specified folder or folders can contain multiple vertex files and multiple edge files.</p>
            format: <p>The format of the data. For more information about data formats for the Neptune <code>Loader</code> command, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format.html">Load Data Formats</a>.</p> <p class="title"> <b>Allowed values</b> </p> <ul> <li> <p> <b> <code>csv</code> </b> for the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV data format</a>.</p> </li> <li> <p> <b> <code>opencypher</code> </b> for the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher CSV data format</a>.</p> </li> <li> <p> <b> <code>ntriples</code> </b> for the <a href="https://www.w3.org/TR/n-triples/">N-Triples RDF data format</a>.</p> </li> <li> <p> <b> <code>nquads</code> </b> for the <a href="https://www.w3.org/TR/n-quads/">N-Quads RDF data format</a>.</p> </li> <li> <p> <b> <code>rdfxml</code> </b> for the <a href="https://www.w3.org/TR/rdf-syntax-grammar/">RDF\XML RDF data format</a>.</p> </li> <li> <p> <b> <code>turtle</code> </b> for the <a href="https://www.w3.org/TR/turtle/">Turtle RDF data format</a>.</p> </li> </ul>
            s3_bucket_region: <p>The Amazon region of the S3 bucket. This must match the Amazon Region of the DB cluster.</p>
            iam_role_arn: <p>The Amazon Resource Name (ARN) for an IAM role to be assumed by the Neptune DB instance for access to the S3 bucket. The IAM role ARN provided here should be attached to the DB cluster (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM-add-role-cluster.html">Adding the IAM Role to an Amazon Neptune Cluster</a>.</p>
            mode: <p>The load job mode.</p> <p> <i>Allowed values</i>: <code>RESUME</code>, <code>NEW</code>, <code>AUTO</code>.</p> <p> <i>Default value</i>: <code>AUTO</code>.</p> <p class="title"> <b/> </p> <ul> <li> <p> <code>RESUME</code> - In RESUME mode, the loader looks for a previous load from this source, and if it finds one, resumes that load job. If no previous load job is found, the loader stops.</p> <p>The loader avoids reloading files that were successfully loaded in a previous job. It only tries to process failed files. If you dropped previously loaded data from your Neptune cluster, that data is not reloaded in this mode. If a previous load job loaded all files from the same source successfully, nothing is reloaded, and the loader returns success.</p> </li> <li> <p> <code>NEW</code> - In NEW mode, the creates a new load request regardless of any previous loads. You can use this mode to reload all the data from a source after dropping previously loaded data from your Neptune cluster, or to load new data available at the same source.</p> </li> <li> <p> <code>AUTO</code> - In AUTO mode, the loader looks for a previous load job from the same source, and if it finds one, resumes that job, just as in <code>RESUME</code> mode.</p> <p>If the loader doesn't find a previous load job from the same source, it loads all data from the source, just as in <code>NEW</code> mode.</p> </li> </ul>
            fail_on_error: <p> <b> <code>failOnError</code> </b> - A flag to toggle a complete stop on an error.</p> <p> <i>Allowed values</i>: <code>"TRUE"</code>, <code>"FALSE"</code>.</p> <p> <i>Default value</i>: <code>"TRUE"</code>.</p> <p>When this parameter is set to <code>"FALSE"</code>, the loader tries to load all the data in the location specified, skipping any entries with errors.</p> <p>When this parameter is set to <code>"TRUE"</code>, the loader stops as soon as it encounters an error. Data loaded up to that point persists.</p>
            parallelism: <p>The optional <code>parallelism</code> parameter can be set to reduce the number of threads used by the bulk load process.</p> <p> <i>Allowed values</i>:</p> <ul> <li> <p> <code>LOW</code> – The number of threads used is the number of available vCPUs divided by 8.</p> </li> <li> <p> <code>MEDIUM</code> – The number of threads used is the number of available vCPUs divided by 2.</p> </li> <li> <p> <code>HIGH</code> – The number of threads used is the same as the number of available vCPUs.</p> </li> <li> <p> <code>OVERSUBSCRIBE</code> – The number of threads used is the number of available vCPUs multiplied by 2. If this value is used, the bulk loader takes up all available resources.</p> <p>This does not mean, however, that the <code>OVERSUBSCRIBE</code> setting results in 100% CPU utilization. Because the load operation is I/O bound, the highest CPU utilization to expect is in the 60% to 70% range.</p> </li> </ul> <p> <i>Default value</i>: <code>HIGH</code> </p> <p>The <code>parallelism</code> setting can sometimes result in a deadlock between threads when loading openCypher data. When this happens, Neptune returns the <code>LOAD_DATA_DEADLOCK</code> error. You can generally fix the issue by setting <code>parallelism</code> to a lower setting and retrying the load command.</p>
            parser_configuration: <p> <b> <code>parserConfiguration</code> </b> – An optional object with additional parser configuration values. Each of the child parameters is also optional:</p> <p class="title"> <b/> </p> <ul> <li> <p> <b> <code>namedGraphUri</code> </b> - The default graph for all RDF formats when no graph is specified (for non-quads formats and NQUAD entries with no graph).</p> <p>The default is <code>https://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph</code>.</p> </li> <li> <p> <b> <code>baseUri</code> </b> - The base URI for RDF/XML and Turtle formats.</p> <p>The default is <code>https://aws.amazon.com/neptune/default</code>.</p> </li> <li> <p> <b> <code>allowEmptyStrings</code> </b> - Gremlin users need to be able to pass empty string values("") as node and edge properties when loading CSV data. If <code>allowEmptyStrings</code> is set to <code>false</code> (the default), such empty strings are treated as nulls and are not loaded.</p> <p>If <code>allowEmptyStrings</code> is set to <code>true</code>, the loader treats empty strings as valid property values and loads them accordingly.</p> </li> </ul>
            update_single_cardinality_properties: <p> <code>updateSingleCardinalityProperties</code> is an optional parameter that controls how the bulk loader treats a new value for single-cardinality vertex or edge properties. This is not supported for loading openCypher data.</p> <p> <i>Allowed values</i>: <code>"TRUE"</code>, <code>"FALSE"</code>.</p> <p> <i>Default value</i>: <code>"FALSE"</code>.</p> <p>By default, or when <code>updateSingleCardinalityProperties</code> is explicitly set to <code>"FALSE"</code>, the loader treats a new value as an error, because it violates single cardinality.</p> <p>When <code>updateSingleCardinalityProperties</code> is set to <code>"TRUE"</code>, on the other hand, the bulk loader replaces the existing value with the new one. If multiple edge or single-cardinality vertex property values are provided in the source file(s) being loaded, the final value at the end of the bulk load could be any one of those new values. The loader only guarantees that the existing value has been replaced by one of the new ones.</p>
            queue_request: <p>This is an optional flag parameter that indicates whether the load request can be queued up or not. </p> <p>You don't have to wait for one load job to complete before issuing the next one, because Neptune can queue up as many as 64 jobs at a time, provided that their <code>queueRequest</code> parameters are all set to <code>"TRUE"</code>. The queue order of the jobs will be first-in-first-out (FIFO).</p> <p>If the <code>queueRequest</code> parameter is omitted or set to <code>"FALSE"</code>, the load request will fail if another load job is already running.</p> <p> <i>Allowed values</i>: <code>"TRUE"</code>, <code>"FALSE"</code>.</p> <p> <i>Default value</i>: <code>"FALSE"</code>.</p>
            dependencies: <p>This is an optional parameter that can make a queued load request contingent on the successful completion of one or more previous jobs in the queue.</p> <p>Neptune can queue up as many as 64 load requests at a time, if their <code>queueRequest</code> parameters are set to <code>"TRUE"</code>. The <code>dependencies</code> parameter lets you make execution of such a queued request dependent on the successful completion of one or more specified previous requests in the queue.</p> <p>For example, if load <code>Job-A</code> and <code>Job-B</code> are independent of each other, but load <code>Job-C</code> needs <code>Job-A</code> and <code>Job-B</code> to be finished before it begins, proceed as follows:</p> <ol> <li> <p>Submit <code>load-job-A</code> and <code>load-job-B</code> one after another in any order, and save their load-ids.</p> </li> <li> <p>Submit <code>load-job-C</code> with the load-ids of the two jobs in its <code>dependencies</code> field:</p> </li> </ol> <p>Because of the <code>dependencies</code> parameter, the bulk loader will not start <code>Job-C</code> until <code>Job-A</code> and <code>Job-B</code> have completed successfully. If either one of them fails, Job-C will not be executed, and its status will be set to <code>LOAD_FAILED_BECAUSE_DEPENDENCY_NOT_SATISFIED</code>.</p> <p>You can set up multiple levels of dependency in this way, so that the failure of one job will cause all requests that are directly or indirectly dependent on it to be cancelled.</p>
            user_provided_edge_ids: <p>This parameter is required only when loading openCypher data that contains relationship IDs. It must be included and set to <code>True</code> when openCypher relationship IDs are explicitly provided in the load data (recommended).</p> <p>When <code>userProvidedEdgeIds</code> is absent or set to <code>True</code>, an <code>:ID</code> column must be present in every relationship file in the load.</p> <p>When <code>userProvidedEdgeIds</code> is present and set to <code>False</code>, relationship files in the load <b>must not</b> contain an <code>:ID</code> column. Instead, the Neptune loader automatically generates an ID for each relationship.</p> <p>It's useful to provide relationship IDs explicitly so that the loader can resume loading after error in the CSV data have been fixed, without having to reload any relationships that have already been loaded. If relationship IDs have not been explicitly assigned, the loader cannot resume a failed load if any relationship file has had to be corrected, and must instead reload all the relationships.</p>
            edge_only_load: <p> <b> <code>edgeOnlyLoad</code> </b> - A flag that controls file processing order during bulk loading.</p> <p> <i>Allowed values</i>: <code>"TRUE"</code>, <code>"FALSE"</code>.</p> <p> <i>Default value</i>: <code>"FALSE"</code>.</p> <p>When this parameter is set to "FALSE", the loader automatically loads vertex files first, then edge files afterwards. It does this by first scanning all files to determine their contents (vertices or edges). When this parameter is set to "TRUE", the loader skips the initial scanning phase and immediately loads all files in the order they appear.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.bulk_load_id_not_found_exception.BulkLoadIdNotFoundException: <p>Raised when a specified bulk-load job ID cannot be found.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.internal_failure_exception.InternalFailureException: <p>Raised when the processing of the request failed unexpectedly.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.load_url_access_denied_exception.LoadUrlAccessDeniedException: <p>Raised when access is denied to a specified load URL.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.s3_exception.S3Exception: <p>Raised when there is a problem accessing Amazon S3.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.start_loader_job_input.StartLoaderJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.start_loader_job_output.StartLoaderJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.start_loader_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.start_loader_job.async_start_loader_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.start_loader_job_input.StartLoaderJobInput = {
            "source": source,
            "format": format,
            "s3_bucket_region": s3_bucket_region,
            "iam_role_arn": iam_role_arn,
        }
        if mode is not None:
            input_["mode"] = mode
        if fail_on_error is not None:
            input_["fail_on_error"] = fail_on_error
        if parallelism is not None:
            input_["parallelism"] = parallelism
        if parser_configuration is not None:
            input_["parser_configuration"] = parser_configuration
        if update_single_cardinality_properties is not None:
            input_["update_single_cardinality_properties"] = (
                update_single_cardinality_properties
            )
        if queue_request is not None:
            input_["queue_request"] = queue_request
        if dependencies is not None:
            input_["dependencies"] = dependencies
        if user_provided_edge_ids is not None:
            input_["user_provided_edge_ids"] = user_provided_edge_ids
        if edge_only_load is not None:
            input_["edge_only_load"] = edge_only_load

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_ml_data_processing_job(
        self,
        input_data_s3_location: str,
        processed_data_s3_location: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        id: Optional[str] = None,
        previous_data_processing_job_id: Optional[str] = None,
        sagemaker_iam_role_arn: Optional[str] = None,
        neptune_iam_role_arn: Optional[str] = None,
        processing_instance_type: Optional[str] = None,
        processing_instance_volume_size_in_gb: Optional[int] = None,
        processing_time_out_in_seconds: Optional[int] = None,
        model_type: Optional[str] = None,
        config_file_name: Optional[str] = None,
        subnets: Optional["capo_neptunedata.types.string_list.StringList"] = None,
        security_group_ids: Optional[
            "capo_neptunedata.types.string_list.StringList"
        ] = None,
        volume_encryption_kms_key: Optional[str] = None,
        s3_output_encryption_kms_key: Optional[str] = None,
    ) -> "capo_neptunedata.types.start_ml_data_processing_job_output.StartMLDataProcessingJobOutput":
        """<p>Creates a new Neptune ML data processing job for processing the graph data exported from Neptune for training. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-dataprocessing.html">The <code>dataprocessing</code> command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startmlmodeldataprocessingjob">neptune-db:StartMLModelDataProcessingJob</a> IAM action in that cluster.</p>

        Args:
            id: <p>A unique identifier for the new job. The default is an autogenerated UUID.</p>
            previous_data_processing_job_id: <p>The job ID of a completed data processing job run on an earlier version of the data.</p>
            input_data_s3_location: <p>The URI of the Amazon S3 location where you want SageMaker to download the data needed to run the data processing job.</p>
            processed_data_s3_location: <p>The URI of the Amazon S3 location where you want SageMaker to save the results of a data processing job.</p>
            sagemaker_iam_role_arn: <p>The ARN of an IAM role for SageMaker execution. This must be listed in your DB cluster parameter group or an error will occur.</p>
            neptune_iam_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that SageMaker can assume to perform tasks on your behalf. This must be listed in your DB cluster parameter group or an error will occur.</p>
            processing_instance_type: <p>The type of ML instance used during data processing. Its memory should be large enough to hold the processed dataset. The default is the smallest ml.r5 type whose memory is ten times larger than the size of the exported graph data on disk.</p>
            processing_instance_volume_size_in_gb: <p>The disk volume size of the processing instance. Both input data and processed data are stored on disk, so the volume size must be large enough to hold both data sets. The default is 0. If not specified or 0, Neptune ML chooses the volume size automatically based on the data size.</p>
            processing_time_out_in_seconds: <p>Timeout in seconds for the data processing job. The default is 86,400 (1 day).</p>
            model_type: <p>One of the two model types that Neptune ML currently supports: heterogeneous graph models (<code>heterogeneous</code>), and knowledge graph (<code>kge</code>). The default is none. If not specified, Neptune ML chooses the model type automatically based on the data.</p>
            config_file_name: <p>A data specification file that describes how to load the exported graph data for training. The file is automatically generated by the Neptune export toolkit. The default is <code>training-data-configuration.json</code>.</p>
            subnets: <p>The IDs of the subnets in the Neptune VPC. The default is None.</p>
            security_group_ids: <p>The VPC security group IDs. The default is None.</p>
            volume_encryption_kms_key: <p>The Amazon Key Management Service (Amazon KMS) key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instances that run the training job. The default is None.</p>
            s3_output_encryption_kms_key: <p>The Amazon Key Management Service (Amazon KMS) key that SageMaker uses to encrypt the output of the processing job. The default is none.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.start_ml_data_processing_job_input.StartMLDataProcessingJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.start_ml_data_processing_job_output.StartMLDataProcessingJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.start_ml_data_processing_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.start_ml_data_processing_job.async_start_ml_data_processing_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.start_ml_data_processing_job_input.StartMLDataProcessingJobInput = {
            "input_data_s3_location": input_data_s3_location,
            "processed_data_s3_location": processed_data_s3_location,
        }
        if id is not None:
            input_["id"] = id
        if previous_data_processing_job_id is not None:
            input_["previous_data_processing_job_id"] = previous_data_processing_job_id
        if sagemaker_iam_role_arn is not None:
            input_["sagemaker_iam_role_arn"] = sagemaker_iam_role_arn
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn
        if processing_instance_type is not None:
            input_["processing_instance_type"] = processing_instance_type
        if processing_instance_volume_size_in_gb is not None:
            input_["processing_instance_volume_size_in_gb"] = (
                processing_instance_volume_size_in_gb
            )
        if processing_time_out_in_seconds is not None:
            input_["processing_time_out_in_seconds"] = processing_time_out_in_seconds
        if model_type is not None:
            input_["model_type"] = model_type
        if config_file_name is not None:
            input_["config_file_name"] = config_file_name
        if subnets is not None:
            input_["subnets"] = subnets
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if volume_encryption_kms_key is not None:
            input_["volume_encryption_kms_key"] = volume_encryption_kms_key
        if s3_output_encryption_kms_key is not None:
            input_["s3_output_encryption_kms_key"] = s3_output_encryption_kms_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_ml_model_training_job(
        self,
        data_processing_job_id: str,
        train_model_s3_location: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        id: Optional[str] = None,
        previous_model_training_job_id: Optional[str] = None,
        sagemaker_iam_role_arn: Optional[str] = None,
        neptune_iam_role_arn: Optional[str] = None,
        base_processing_instance_type: Optional[str] = None,
        training_instance_type: Optional[str] = None,
        training_instance_volume_size_in_gb: Optional[int] = None,
        training_time_out_in_seconds: Optional[int] = None,
        max_hpo_number_of_training_jobs: Optional[int] = None,
        max_hpo_parallel_training_jobs: Optional[int] = None,
        subnets: Optional["capo_neptunedata.types.string_list.StringList"] = None,
        security_group_ids: Optional[
            "capo_neptunedata.types.string_list.StringList"
        ] = None,
        volume_encryption_kms_key: Optional[str] = None,
        s3_output_encryption_kms_key: Optional[str] = None,
        enable_managed_spot_training: Optional[bool] = None,
        custom_model_training_parameters: Optional[
            "capo_neptunedata.types.custom_model_training_parameters.CustomModelTrainingParameters"
        ] = None,
    ) -> "capo_neptunedata.types.start_ml_model_training_job_output.StartMLModelTrainingJobOutput":
        """<p>Creates a new Neptune ML model training job. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-modeltraining.html">Model training using the <code>modeltraining</code> command</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startmlmodeltrainingjob">neptune-db:StartMLModelTrainingJob</a> IAM action in that cluster.</p>

        Args:
            id: <p>A unique identifier for the new job. The default is An autogenerated UUID.</p>
            previous_model_training_job_id: <p>The job ID of a completed model-training job that you want to update incrementally based on updated data.</p>
            data_processing_job_id: <p>The job ID of the completed data-processing job that has created the data that the training will work with.</p>
            train_model_s3_location: <p>The location in Amazon S3 where the model artifacts are to be stored.</p>
            sagemaker_iam_role_arn: <p>The ARN of an IAM role for SageMaker execution.This must be listed in your DB cluster parameter group or an error will occur.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>
            base_processing_instance_type: <p>The type of ML instance used in preparing and managing training of ML models. This is a CPU instance chosen based on memory requirements for processing the training data and model.</p>
            training_instance_type: <p>The type of ML instance used for model training. All Neptune ML models support CPU, GPU, and multiGPU training. The default is <code>ml.p3.2xlarge</code>. Choosing the right instance type for training depends on the task type, graph size, and your budget.</p>
            training_instance_volume_size_in_gb: <p>The disk volume size of the training instance. Both input data and the output model are stored on disk, so the volume size must be large enough to hold both data sets. The default is 0. If not specified or 0, Neptune ML selects a disk volume size based on the recommendation generated in the data processing step.</p>
            training_time_out_in_seconds: <p>Timeout in seconds for the training job. The default is 86,400 (1 day).</p>
            max_hpo_number_of_training_jobs: <p>Maximum total number of training jobs to start for the hyperparameter tuning job. The default is 2. Neptune ML automatically tunes the hyperparameters of the machine learning model. To obtain a model that performs well, use at least 10 jobs (in other words, set <code>maxHPONumberOfTrainingJobs</code> to 10). In general, the more tuning runs, the better the results.</p>
            max_hpo_parallel_training_jobs: <p>Maximum number of parallel training jobs to start for the hyperparameter tuning job. The default is 2. The number of parallel jobs you can run is limited by the available resources on your training instance.</p>
            subnets: <p>The IDs of the subnets in the Neptune VPC. The default is None.</p>
            security_group_ids: <p>The VPC security group IDs. The default is None.</p>
            volume_encryption_kms_key: <p>The Amazon Key Management Service (KMS) key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instances that run the training job. The default is None.</p>
            s3_output_encryption_kms_key: <p>The Amazon Key Management Service (KMS) key that SageMaker uses to encrypt the output of the processing job. The default is none.</p>
            enable_managed_spot_training: <p>Optimizes the cost of training machine-learning models by using Amazon Elastic Compute Cloud spot instances. The default is <code>False</code>.</p>
            custom_model_training_parameters: <p>The configuration for custom model training. This is a JSON object.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.start_ml_model_training_job_input.StartMLModelTrainingJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.start_ml_model_training_job_output.StartMLModelTrainingJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.start_ml_model_training_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.start_ml_model_training_job.async_start_ml_model_training_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.start_ml_model_training_job_input.StartMLModelTrainingJobInput = {
            "data_processing_job_id": data_processing_job_id,
            "train_model_s3_location": train_model_s3_location,
        }
        if id is not None:
            input_["id"] = id
        if previous_model_training_job_id is not None:
            input_["previous_model_training_job_id"] = previous_model_training_job_id
        if sagemaker_iam_role_arn is not None:
            input_["sagemaker_iam_role_arn"] = sagemaker_iam_role_arn
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn
        if base_processing_instance_type is not None:
            input_["base_processing_instance_type"] = base_processing_instance_type
        if training_instance_type is not None:
            input_["training_instance_type"] = training_instance_type
        if training_instance_volume_size_in_gb is not None:
            input_["training_instance_volume_size_in_gb"] = (
                training_instance_volume_size_in_gb
            )
        if training_time_out_in_seconds is not None:
            input_["training_time_out_in_seconds"] = training_time_out_in_seconds
        if max_hpo_number_of_training_jobs is not None:
            input_["max_hpo_number_of_training_jobs"] = max_hpo_number_of_training_jobs
        if max_hpo_parallel_training_jobs is not None:
            input_["max_hpo_parallel_training_jobs"] = max_hpo_parallel_training_jobs
        if subnets is not None:
            input_["subnets"] = subnets
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if volume_encryption_kms_key is not None:
            input_["volume_encryption_kms_key"] = volume_encryption_kms_key
        if s3_output_encryption_kms_key is not None:
            input_["s3_output_encryption_kms_key"] = s3_output_encryption_kms_key
        if enable_managed_spot_training is not None:
            input_["enable_managed_spot_training"] = enable_managed_spot_training
        if custom_model_training_parameters is not None:
            input_["custom_model_training_parameters"] = (
                custom_model_training_parameters
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_ml_model_transform_job(
        self,
        model_transform_output_s3_location: str,
        *,
        config_overrides: Optional[AsyncneptunedataClientConfig] = None,
        id: Optional[str] = None,
        data_processing_job_id: Optional[str] = None,
        ml_model_training_job_id: Optional[str] = None,
        training_job_name: Optional[str] = None,
        sagemaker_iam_role_arn: Optional[str] = None,
        neptune_iam_role_arn: Optional[str] = None,
        custom_model_transform_parameters: Optional[
            "capo_neptunedata.types.custom_model_transform_parameters.CustomModelTransformParameters"
        ] = None,
        base_processing_instance_type: Optional[str] = None,
        base_processing_instance_volume_size_in_gb: Optional[int] = None,
        subnets: Optional["capo_neptunedata.types.string_list.StringList"] = None,
        security_group_ids: Optional[
            "capo_neptunedata.types.string_list.StringList"
        ] = None,
        volume_encryption_kms_key: Optional[str] = None,
        s3_output_encryption_kms_key: Optional[str] = None,
    ) -> "capo_neptunedata.types.start_ml_model_transform_job_output.StartMLModelTransformJobOutput":
        """<p>Creates a new model transform job. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-model-transform.html">Use a trained model to generate new model artifacts</a>.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startmlmodeltransformjob">neptune-db:StartMLModelTransformJob</a> IAM action in that cluster.</p>

        Args:
            id: <p>A unique identifier for the new job. The default is an autogenerated UUID.</p>
            data_processing_job_id: <p>The job ID of a completed data-processing job. You must include either <code>dataProcessingJobId</code> and a <code>mlModelTrainingJobId</code>, or a <code>trainingJobName</code>.</p>
            ml_model_training_job_id: <p>The job ID of a completed model-training job. You must include either <code>dataProcessingJobId</code> and a <code>mlModelTrainingJobId</code>, or a <code>trainingJobName</code>.</p>
            training_job_name: <p>The name of a completed SageMaker training job. You must include either <code>dataProcessingJobId</code> and a <code>mlModelTrainingJobId</code>, or a <code>trainingJobName</code>.</p>
            model_transform_output_s3_location: <p>The location in Amazon S3 where the model artifacts are to be stored.</p>
            sagemaker_iam_role_arn: <p>The ARN of an IAM role for SageMaker execution. This must be listed in your DB cluster parameter group or an error will occur.</p>
            neptune_iam_role_arn: <p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>
            custom_model_transform_parameters: <p>Configuration information for a model transform using a custom model. The <code>customModelTransformParameters</code> object contains the following fields, which must have values compatible with the saved model parameters from the training job:</p>
            base_processing_instance_type: <p>The type of ML instance used in preparing and managing training of ML models. This is an ML compute instance chosen based on memory requirements for processing the training data and model.</p>
            base_processing_instance_volume_size_in_gb: <p>The disk volume size of the training instance in gigabytes. The default is 0. Both input data and the output model are stored on disk, so the volume size must be large enough to hold both data sets. If not specified or 0, Neptune ML selects a disk volume size based on the recommendation generated in the data processing step.</p>
            subnets: <p>The IDs of the subnets in the Neptune VPC. The default is None.</p>
            security_group_ids: <p>The VPC security group IDs. The default is None.</p>
            volume_encryption_kms_key: <p>The Amazon Key Management Service (KMS) key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instances that run the training job. The default is None.</p>
            s3_output_encryption_kms_key: <p>The Amazon Key Management Service (KMS) key that SageMaker uses to encrypt the output of the processing job. The default is none.</p>

        Raises:
            capo_neptunedata.errors.bad_request_exception.BadRequestException: <p>Raised when a request is submitted that cannot be processed.</p>
            capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException: <p>Raised when a request timed out in the client.</p>
            capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException: <p>Raised when a value in a request field did not satisfy required constraints.</p>
            capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException: <p>Raised when an argument in a request is not supported.</p>
            capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException: <p>Raised when an argument in a request has an invalid value.</p>
            capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException: <p>Raised when a parameter value is not valid.</p>
            capo_neptunedata.errors.missing_parameter_exception.MissingParameterException: <p>Raised when a required parameter is missing.</p>
            capo_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException: <p>Raised when a specified machine-learning resource could not be found.</p>
            capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException: <p>Raised when a precondition for processing a request is not satisfied.</p>
            capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException: <p>Raised when the number of requests being processed exceeds the limit.</p>
            capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException: <p>Raised when a request attempts to initiate an operation that is not supported.</p>
            capo_neptunedata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptunedata.types.start_ml_model_transform_job_input.StartMLModelTransformJobInput]",
        ) -> AsyncOperationResponse[
            "capo_neptunedata.types.start_ml_model_transform_job_output.StartMLModelTransformJobOutput"
        ]:
            import capo_neptunedata._operations.amazon_neptune_dataplane.start_ml_model_transform_job

            (
                output,
                http_response,
            ) = await capo_neptunedata._operations.amazon_neptune_dataplane.start_ml_model_transform_job.async_start_ml_model_transform_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptunedata.types.start_ml_model_transform_job_input.StartMLModelTransformJobInput = {
            "model_transform_output_s3_location": model_transform_output_s3_location
        }
        if id is not None:
            input_["id"] = id
        if data_processing_job_id is not None:
            input_["data_processing_job_id"] = data_processing_job_id
        if ml_model_training_job_id is not None:
            input_["ml_model_training_job_id"] = ml_model_training_job_id
        if training_job_name is not None:
            input_["training_job_name"] = training_job_name
        if sagemaker_iam_role_arn is not None:
            input_["sagemaker_iam_role_arn"] = sagemaker_iam_role_arn
        if neptune_iam_role_arn is not None:
            input_["neptune_iam_role_arn"] = neptune_iam_role_arn
        if custom_model_transform_parameters is not None:
            input_["custom_model_transform_parameters"] = (
                custom_model_transform_parameters
            )
        if base_processing_instance_type is not None:
            input_["base_processing_instance_type"] = base_processing_instance_type
        if base_processing_instance_volume_size_in_gb is not None:
            input_["base_processing_instance_volume_size_in_gb"] = (
                base_processing_instance_volume_size_in_gb
            )
        if subnets is not None:
            input_["subnets"] = subnets
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if volume_encryption_kms_key is not None:
            input_["volume_encryption_kms_key"] = volume_encryption_kms_key
        if s3_output_encryption_kms_key is not None:
            input_["s3_output_encryption_kms_key"] = s3_output_encryption_kms_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
