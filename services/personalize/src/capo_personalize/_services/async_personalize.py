"""Generated from Smithy shape ``com.amazonaws.personalize#AmazonPersonalize``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_personalize._auth._signers
import capo_personalize._auth._sigv4
from capo_personalize._auth._identity import Credentials
from capo_personalize._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_personalize._auth._zapros_handler import AuthMiddleware
from capo_personalize._pagination import resolve_path as _resolve_path
from capo_personalize._services._aws_config import aaws_config
from capo_personalize._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.avro_schema
    import capo_personalize.types.batch_inference_job_config
    import capo_personalize.types.batch_inference_job_input
    import capo_personalize.types.batch_inference_job_mode
    import capo_personalize.types.batch_inference_job_output
    import capo_personalize.types.batch_inference_job_summary
    import capo_personalize.types.batch_segment_job_input
    import capo_personalize.types.batch_segment_job_output
    import capo_personalize.types.batch_segment_job_summary
    import capo_personalize.types.boolean
    import capo_personalize.types.campaign_config
    import capo_personalize.types.campaign_summary
    import capo_personalize.types.create_batch_inference_job_request
    import capo_personalize.types.create_batch_inference_job_response
    import capo_personalize.types.create_batch_segment_job_request
    import capo_personalize.types.create_batch_segment_job_response
    import capo_personalize.types.create_campaign_request
    import capo_personalize.types.create_campaign_response
    import capo_personalize.types.create_data_deletion_job_request
    import capo_personalize.types.create_data_deletion_job_response
    import capo_personalize.types.create_dataset_export_job_request
    import capo_personalize.types.create_dataset_export_job_response
    import capo_personalize.types.create_dataset_group_request
    import capo_personalize.types.create_dataset_group_response
    import capo_personalize.types.create_dataset_import_job_request
    import capo_personalize.types.create_dataset_import_job_response
    import capo_personalize.types.create_dataset_request
    import capo_personalize.types.create_dataset_response
    import capo_personalize.types.create_event_tracker_request
    import capo_personalize.types.create_event_tracker_response
    import capo_personalize.types.create_filter_request
    import capo_personalize.types.create_filter_response
    import capo_personalize.types.create_metric_attribution_request
    import capo_personalize.types.create_metric_attribution_response
    import capo_personalize.types.create_recommender_request
    import capo_personalize.types.create_recommender_response
    import capo_personalize.types.create_schema_request
    import capo_personalize.types.create_schema_response
    import capo_personalize.types.create_solution_request
    import capo_personalize.types.create_solution_response
    import capo_personalize.types.create_solution_version_request
    import capo_personalize.types.create_solution_version_response
    import capo_personalize.types.data_source
    import capo_personalize.types.dataset_export_job_output
    import capo_personalize.types.dataset_export_job_summary
    import capo_personalize.types.dataset_group_summary
    import capo_personalize.types.dataset_import_job_summary
    import capo_personalize.types.dataset_schema_summary
    import capo_personalize.types.dataset_summary
    import capo_personalize.types.dataset_type
    import capo_personalize.types.delete_campaign_request
    import capo_personalize.types.delete_dataset_group_request
    import capo_personalize.types.delete_dataset_request
    import capo_personalize.types.delete_event_tracker_request
    import capo_personalize.types.delete_filter_request
    import capo_personalize.types.delete_metric_attribution_request
    import capo_personalize.types.delete_recommender_request
    import capo_personalize.types.delete_schema_request
    import capo_personalize.types.delete_solution_request
    import capo_personalize.types.describe_algorithm_request
    import capo_personalize.types.describe_algorithm_response
    import capo_personalize.types.describe_batch_inference_job_request
    import capo_personalize.types.describe_batch_inference_job_response
    import capo_personalize.types.describe_batch_segment_job_request
    import capo_personalize.types.describe_batch_segment_job_response
    import capo_personalize.types.describe_campaign_request
    import capo_personalize.types.describe_campaign_response
    import capo_personalize.types.describe_data_deletion_job_request
    import capo_personalize.types.describe_data_deletion_job_response
    import capo_personalize.types.describe_dataset_export_job_request
    import capo_personalize.types.describe_dataset_export_job_response
    import capo_personalize.types.describe_dataset_group_request
    import capo_personalize.types.describe_dataset_group_response
    import capo_personalize.types.describe_dataset_import_job_request
    import capo_personalize.types.describe_dataset_import_job_response
    import capo_personalize.types.describe_dataset_request
    import capo_personalize.types.describe_dataset_response
    import capo_personalize.types.describe_event_tracker_request
    import capo_personalize.types.describe_event_tracker_response
    import capo_personalize.types.describe_feature_transformation_request
    import capo_personalize.types.describe_feature_transformation_response
    import capo_personalize.types.describe_filter_request
    import capo_personalize.types.describe_filter_response
    import capo_personalize.types.describe_metric_attribution_request
    import capo_personalize.types.describe_metric_attribution_response
    import capo_personalize.types.describe_recipe_request
    import capo_personalize.types.describe_recipe_response
    import capo_personalize.types.describe_recommender_request
    import capo_personalize.types.describe_recommender_response
    import capo_personalize.types.describe_schema_request
    import capo_personalize.types.describe_schema_response
    import capo_personalize.types.describe_solution_request
    import capo_personalize.types.describe_solution_response
    import capo_personalize.types.describe_solution_version_request
    import capo_personalize.types.describe_solution_version_response
    import capo_personalize.types.domain
    import capo_personalize.types.event_tracker_summary
    import capo_personalize.types.event_type
    import capo_personalize.types.filter_expression
    import capo_personalize.types.filter_summary
    import capo_personalize.types.get_solution_metrics_request
    import capo_personalize.types.get_solution_metrics_response
    import capo_personalize.types.import_mode
    import capo_personalize.types.ingestion_mode
    import capo_personalize.types.kms_key_arn
    import capo_personalize.types.list_batch_inference_jobs_request
    import capo_personalize.types.list_batch_inference_jobs_response
    import capo_personalize.types.list_batch_segment_jobs_request
    import capo_personalize.types.list_batch_segment_jobs_response
    import capo_personalize.types.list_campaigns_request
    import capo_personalize.types.list_campaigns_response
    import capo_personalize.types.list_data_deletion_jobs_request
    import capo_personalize.types.list_data_deletion_jobs_response
    import capo_personalize.types.list_dataset_export_jobs_request
    import capo_personalize.types.list_dataset_export_jobs_response
    import capo_personalize.types.list_dataset_groups_request
    import capo_personalize.types.list_dataset_groups_response
    import capo_personalize.types.list_dataset_import_jobs_request
    import capo_personalize.types.list_dataset_import_jobs_response
    import capo_personalize.types.list_datasets_request
    import capo_personalize.types.list_datasets_response
    import capo_personalize.types.list_event_trackers_request
    import capo_personalize.types.list_event_trackers_response
    import capo_personalize.types.list_filters_request
    import capo_personalize.types.list_filters_response
    import capo_personalize.types.list_metric_attribution_metrics_request
    import capo_personalize.types.list_metric_attribution_metrics_response
    import capo_personalize.types.list_metric_attributions_request
    import capo_personalize.types.list_metric_attributions_response
    import capo_personalize.types.list_recipes_request
    import capo_personalize.types.list_recipes_response
    import capo_personalize.types.list_recommenders_request
    import capo_personalize.types.list_recommenders_response
    import capo_personalize.types.list_schemas_request
    import capo_personalize.types.list_schemas_response
    import capo_personalize.types.list_solution_versions_request
    import capo_personalize.types.list_solution_versions_response
    import capo_personalize.types.list_solutions_request
    import capo_personalize.types.list_solutions_response
    import capo_personalize.types.list_tags_for_resource_request
    import capo_personalize.types.list_tags_for_resource_response
    import capo_personalize.types.max_results
    import capo_personalize.types.metric_attribute
    import capo_personalize.types.metric_attributes
    import capo_personalize.types.metric_attributes_names_list
    import capo_personalize.types.metric_attribution_output
    import capo_personalize.types.metric_attribution_summary
    import capo_personalize.types.name
    import capo_personalize.types.next_token
    import capo_personalize.types.num_batch_results
    import capo_personalize.types.perform_auto_ml
    import capo_personalize.types.perform_auto_training
    import capo_personalize.types.perform_incremental_update
    import capo_personalize.types.recipe_provider
    import capo_personalize.types.recipe_summary
    import capo_personalize.types.recommender_config
    import capo_personalize.types.recommender_summary
    import capo_personalize.types.role_arn
    import capo_personalize.types.solution_config
    import capo_personalize.types.solution_summary
    import capo_personalize.types.solution_update_config
    import capo_personalize.types.solution_version_summary
    import capo_personalize.types.start_recommender_request
    import capo_personalize.types.start_recommender_response
    import capo_personalize.types.stop_recommender_request
    import capo_personalize.types.stop_recommender_response
    import capo_personalize.types.stop_solution_version_creation_request
    import capo_personalize.types.tag_keys
    import capo_personalize.types.tag_resource_request
    import capo_personalize.types.tag_resource_response
    import capo_personalize.types.tags
    import capo_personalize.types.theme_generation_config
    import capo_personalize.types.training_mode
    import capo_personalize.types.transactions_per_second
    import capo_personalize.types.untag_resource_request
    import capo_personalize.types.untag_resource_response
    import capo_personalize.types.update_campaign_request
    import capo_personalize.types.update_campaign_response
    import capo_personalize.types.update_dataset_request
    import capo_personalize.types.update_dataset_response
    import capo_personalize.types.update_metric_attribution_request
    import capo_personalize.types.update_metric_attribution_response
    import capo_personalize.types.update_recommender_request
    import capo_personalize.types.update_recommender_response
    import capo_personalize.types.update_solution_request
    import capo_personalize.types.update_solution_response


class AsyncPersonalizeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncPersonalizeClient:
    """A client for the ``Personalize`` service.

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
        self._config = AsyncPersonalizeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncPersonalizeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPersonalizeClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def create_batch_inference_job(
        self,
        job_name: "capo_personalize.types.name.Name",
        solution_version_arn: "capo_personalize.types.arn.Arn",
        job_input: "capo_personalize.types.batch_inference_job_input.BatchInferenceJobInput",
        job_output: "capo_personalize.types.batch_inference_job_output.BatchInferenceJobOutput",
        role_arn: "capo_personalize.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        filter_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        num_results: Optional[
            "capo_personalize.types.num_batch_results.NumBatchResults"
        ] = None,
        batch_inference_job_config: Optional[
            "capo_personalize.types.batch_inference_job_config.BatchInferenceJobConfig"
        ] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
        batch_inference_job_mode: Optional[
            "capo_personalize.types.batch_inference_job_mode.BatchInferenceJobMode"
        ] = None,
        theme_generation_config: Optional[
            "capo_personalize.types.theme_generation_config.ThemeGenerationConfig"
        ] = None,
    ) -> "capo_personalize.types.create_batch_inference_job_response.CreateBatchInferenceJobResponse":
        """<p>Generates batch recommendations based on a list of items or users stored in Amazon S3 and exports the recommendations to an Amazon S3 bucket.</p> <p>To generate batch recommendations, specify the ARN of a solution version and an Amazon S3 URI for the input and output data. For user personalization, popular items, and personalized ranking solutions, the batch inference job generates a list of recommended items for each user ID in the input file. For related items solutions, the job generates a list of recommended items for each item ID in the input file.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/getting-batch-recommendations.html">Creating a batch inference job </a>.</p> <p> If you use the Similar-Items recipe, Amazon Personalize can add descriptive themes to batch recommendations. To generate themes, set the job's mode to <code>THEME_GENERATION</code> and specify the name of the field that contains item names in the input data.</p> <p> For more information about generating themes, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/themed-batch-recommendations.html">Batch recommendations with themes from Content Generator </a>. </p> <p>You can't get batch recommendations with the Trending-Now or Next-Best-Action recipes.</p>

        Args:
            job_name: <p>The name of the batch inference job to create.</p>
            solution_version_arn: <p>The Amazon Resource Name (ARN) of the solution version that will be used to generate the batch inference recommendations.</p>
            filter_arn: <p>The ARN of the filter to apply to the batch inference job. For more information on using filters, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter-batch.html">Filtering batch recommendations</a>.</p>
            num_results: <p>The number of recommendations to retrieve.</p>
            job_input: <p>The Amazon S3 path that leads to the input file to base your recommendations on. The input material must be in JSON format.</p>
            job_output: <p>The path to the Amazon S3 bucket where the job's output will be stored.</p>
            role_arn: <p>The ARN of the Amazon Identity and Access Management role that has permissions to read and write to your input and output Amazon S3 buckets respectively.</p>
            batch_inference_job_config: <p>The configuration details of a batch inference job.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the batch inference job.</p>
            batch_inference_job_mode: <p>The mode of the batch inference job. To generate descriptive themes for groups of similar items, set the job mode to <code>THEME_GENERATION</code>. If you don't want to generate themes, use the default <code>BATCH_INFERENCE</code>.</p> <p> When you get batch recommendations with themes, you will incur additional costs. For more information, see <a href="https://aws.amazon.com/personalize/pricing/">Amazon Personalize pricing</a>. </p>
            theme_generation_config: <p>For theme generation jobs, specify the name of the column in your Items dataset that contains each item's name.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_batch_inference_job_request.CreateBatchInferenceJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_batch_inference_job_response.CreateBatchInferenceJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_batch_inference_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_batch_inference_job.async_create_batch_inference_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_batch_inference_job_request.CreateBatchInferenceJobRequest = {
            "job_name": job_name,
            "solution_version_arn": solution_version_arn,
            "job_input": job_input,
            "job_output": job_output,
            "role_arn": role_arn,
        }
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
        if num_results is not None:
            input_["num_results"] = num_results
        if batch_inference_job_config is not None:
            input_["batch_inference_job_config"] = batch_inference_job_config
        if tags is not None:
            input_["tags"] = tags
        if batch_inference_job_mode is not None:
            input_["batch_inference_job_mode"] = batch_inference_job_mode
        if theme_generation_config is not None:
            input_["theme_generation_config"] = theme_generation_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_batch_segment_job(
        self,
        job_name: "capo_personalize.types.name.Name",
        solution_version_arn: "capo_personalize.types.arn.Arn",
        job_input: "capo_personalize.types.batch_segment_job_input.BatchSegmentJobInput",
        job_output: "capo_personalize.types.batch_segment_job_output.BatchSegmentJobOutput",
        role_arn: "capo_personalize.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        filter_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        num_results: Optional[
            "capo_personalize.types.num_batch_results.NumBatchResults"
        ] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_batch_segment_job_response.CreateBatchSegmentJobResponse":
        """<p>Creates a batch segment job. The operation can handle up to 50 million records and the input file must be in JSON format. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/recommendations-batch.html">Getting batch recommendations and user segments</a>.</p>

        Args:
            job_name: <p>The name of the batch segment job to create.</p>
            solution_version_arn: <p>The Amazon Resource Name (ARN) of the solution version you want the batch segment job to use to generate batch segments.</p>
            filter_arn: <p>The ARN of the filter to apply to the batch segment job. For more information on using filters, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter-batch.html">Filtering batch recommendations</a>.</p>
            num_results: <p>The number of predicted users generated by the batch segment job for each line of input data. The maximum number of users per segment is 5 million.</p>
            job_input: <p>The Amazon S3 path for the input data used to generate the batch segment job.</p>
            job_output: <p>The Amazon S3 path for the bucket where the job's output will be stored.</p>
            role_arn: <p>The ARN of the Amazon Identity and Access Management role that has permissions to read and write to your input and output Amazon S3 buckets respectively.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the batch segment job.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_batch_segment_job_request.CreateBatchSegmentJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_batch_segment_job_response.CreateBatchSegmentJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_batch_segment_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_batch_segment_job.async_create_batch_segment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_batch_segment_job_request.CreateBatchSegmentJobRequest = {
            "job_name": job_name,
            "solution_version_arn": solution_version_arn,
            "job_input": job_input,
            "job_output": job_output,
            "role_arn": role_arn,
        }
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
        if num_results is not None:
            input_["num_results"] = num_results
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_campaign(
        self,
        name: "capo_personalize.types.name.Name",
        solution_version_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        min_provisioned_tps: Optional[
            "capo_personalize.types.transactions_per_second.TransactionsPerSecond"
        ] = None,
        campaign_config: Optional[
            "capo_personalize.types.campaign_config.CampaignConfig"
        ] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_campaign_response.CreateCampaignResponse":
        """<important> <p> You incur campaign costs while it is active. To avoid unnecessary costs, make sure to delete the campaign when you are finished. For information about campaign costs, see <a href="https://aws.amazon.com/personalize/pricing/">Amazon Personalize pricing</a>.</p> </important> <p>Creates a campaign that deploys a solution version. When a client calls the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html">GetRecommendations</a> and <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetPersonalizedRanking.html">GetPersonalizedRanking</a> APIs, a campaign is specified in the request.</p> <p> <b>Minimum Provisioned TPS and Auto-Scaling</b> </p> <important> <p> A high <code>minProvisionedTPS</code> will increase your cost. We recommend starting with 1 for <code>minProvisionedTPS</code> (the default). Track your usage using Amazon CloudWatch metrics, and increase the <code>minProvisionedTPS</code> as necessary.</p> </important> <p> When you create an Amazon Personalize campaign, you can specify the minimum provisioned transactions per second (<code>minProvisionedTPS</code>) for the campaign. This is the baseline transaction throughput for the campaign provisioned by Amazon Personalize. It sets the minimum billing charge for the campaign while it is active. A transaction is a single <code>GetRecommendations</code> or <code>GetPersonalizedRanking</code> request. The default <code>minProvisionedTPS</code> is 1.</p> <p> If your TPS increases beyond the <code>minProvisionedTPS</code>, Amazon Personalize auto-scales the provisioned capacity up and down, but never below <code>minProvisionedTPS</code>. There's a short time delay while the capacity is increased that might cause loss of transactions. When your traffic reduces, capacity returns to the <code>minProvisionedTPS</code>. </p> <p>You are charged for the the minimum provisioned TPS or, if your requests exceed the <code>minProvisionedTPS</code>, the actual TPS. The actual TPS is the total number of recommendation requests you make. We recommend starting with a low <code>minProvisionedTPS</code>, track your usage using Amazon CloudWatch metrics, and then increase the <code>minProvisionedTPS</code> as necessary.</p> <p>For more information about campaign costs, see <a href="https://aws.amazon.com/personalize/pricing/">Amazon Personalize pricing</a>.</p> <p> <b>Status</b> </p> <p>A campaign can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul> <p>To get the campaign status, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html">DescribeCampaign</a>.</p> <note> <p>Wait until the <code>status</code> of the campaign is <code>ACTIVE</code> before asking the campaign for recommendations.</p> </note> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListCampaigns.html">ListCampaigns</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html">DescribeCampaign</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateCampaign.html">UpdateCampaign</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteCampaign.html">DeleteCampaign</a> </p> </li> </ul>

        Args:
            name: <p>A name for the new campaign. The campaign name must be unique within your account.</p>
            solution_version_arn: <p>The Amazon Resource Name (ARN) of the trained model to deploy with the campaign. To specify the latest solution version of your solution, specify the ARN of your <i>solution</i> in <code>SolutionArn/$LATEST</code> format. You must use this format if you set <code>syncWithLatestSolutionVersion</code> to <code>True</code> in the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CampaignConfig.html">CampaignConfig</a>. </p> <p> To deploy a model that isn't the latest solution version of your solution, specify the ARN of the solution version. </p> <p> For more information about automatic campaign updates, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update">Enabling automatic campaign updates</a>. </p>
            min_provisioned_tps: <p>Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support. A high <code>minProvisionedTPS</code> will increase your bill. We recommend starting with 1 for <code>minProvisionedTPS</code> (the default). Track your usage using Amazon CloudWatch metrics, and increase the <code>minProvisionedTPS</code> as necessary.</p>
            campaign_config: <p>The configuration details of a campaign.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the campaign.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_campaign_request.CreateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_campaign

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_campaign.async_create_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_campaign_request.CreateCampaignRequest = {
            "name": name,
            "solution_version_arn": solution_version_arn,
        }
        if min_provisioned_tps is not None:
            input_["min_provisioned_tps"] = min_provisioned_tps
        if campaign_config is not None:
            input_["campaign_config"] = campaign_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_deletion_job(
        self,
        job_name: "capo_personalize.types.name.Name",
        dataset_group_arn: "capo_personalize.types.arn.Arn",
        data_source: "capo_personalize.types.data_source.DataSource",
        role_arn: "capo_personalize.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_data_deletion_job_response.CreateDataDeletionJobResponse":
        """<p>Creates a batch job that deletes all references to specific users from an Amazon Personalize dataset group in batches. You specify the users to delete in a CSV file of userIds in an Amazon S3 bucket. After a job completes, Amazon Personalize no longer trains on the users’ data and no longer considers the users when generating user segments. For more information about creating a data deletion job, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/delete-records.html">Deleting users</a>.</p> <ul> <li> <p>Your input file must be a CSV file with a single USER_ID column that lists the users IDs. For more information about preparing the CSV file, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/prepare-deletion-input-file.html">Preparing your data deletion file and uploading it to Amazon S3</a>.</p> </li> <li> <p>To give Amazon Personalize permission to access your input CSV file of userIds, you must specify an IAM service role that has permission to read from the data source. This role needs <code>GetObject</code> and <code>ListBucket</code> permissions for the bucket and its content. These permissions are the same as importing data. For information on granting access to your Amazon S3 bucket, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/granting-personalize-s3-access.html">Giving Amazon Personalize Access to Amazon S3 Resources</a>. </p> </li> </ul> <p> After you create a job, it can take up to a day to delete all references to the users from datasets and models. Until the job completes, Amazon Personalize continues to use the data when training. And if you use a User Segmentation recipe, the users might appear in user segments. </p> <p> <b>Status</b> </p> <p>A data deletion job can have one of the following statuses:</p> <ul> <li> <p>PENDING > IN_PROGRESS > COMPLETED -or- FAILED</p> </li> </ul> <p>To get the status of the data deletion job, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataDeletionJob.html">DescribeDataDeletionJob</a> API operation and specify the Amazon Resource Name (ARN) of the job. If the status is FAILED, the response includes a <code>failureReason</code> key, which describes why the job failed.</p> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListDataDeletionJobs.html">ListDataDeletionJobs</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataDeletionJob.html">DescribeDataDeletionJob</a> </p> </li> </ul>

        Args:
            job_name: <p>The name for the data deletion job.</p>
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group that has the datasets you want to delete records from.</p>
            data_source: <p>The Amazon S3 bucket that contains the list of userIds of the users to delete.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that has permissions to read from the Amazon S3 data source.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the data deletion job.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_data_deletion_job_request.CreateDataDeletionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_data_deletion_job_response.CreateDataDeletionJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_data_deletion_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_data_deletion_job.async_create_data_deletion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_data_deletion_job_request.CreateDataDeletionJobRequest = {
            "job_name": job_name,
            "dataset_group_arn": dataset_group_arn,
            "data_source": data_source,
            "role_arn": role_arn,
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

    async def create_dataset(
        self,
        name: "capo_personalize.types.name.Name",
        schema_arn: "capo_personalize.types.arn.Arn",
        dataset_group_arn: "capo_personalize.types.arn.Arn",
        dataset_type: "capo_personalize.types.dataset_type.DatasetType",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates an empty dataset and adds it to the specified dataset group. Use <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a> to import your training data to a dataset.</p> <p>There are 5 types of datasets:</p> <ul> <li> <p>Item interactions</p> </li> <li> <p>Items</p> </li> <li> <p>Users</p> </li> <li> <p>Action interactions</p> </li> <li> <p>Actions</p> </li> </ul> <p>Each dataset type has an associated schema with required field types. Only the <code>Item interactions</code> dataset is required in order to train a model (also referred to as creating a solution).</p> <p>A dataset can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul> <p>To get the status of the dataset, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html">DescribeDataset</a>.</p> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasets.html">ListDatasets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html">DescribeDataset</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteDataset.html">DeleteDataset</a> </p> </li> </ul>

        Args:
            name: <p>The name for the dataset.</p>
            schema_arn: <p>The ARN of the schema to associate with the dataset. The schema defines the dataset fields.</p>
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group to add the dataset to.</p>
            dataset_type: <p>The type of dataset.</p> <p>One of the following (case insensitive) values:</p> <ul> <li> <p>Interactions</p> </li> <li> <p>Items</p> </li> <li> <p>Users</p> </li> <li> <p>Actions</p> </li> <li> <p>Action_Interactions</p> </li> </ul>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the dataset.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_dataset_request.CreateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_dataset

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_dataset_request.CreateDatasetRequest = {
            "name": name,
            "schema_arn": schema_arn,
            "dataset_group_arn": dataset_group_arn,
            "dataset_type": dataset_type,
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

    async def create_dataset_export_job(
        self,
        job_name: "capo_personalize.types.name.Name",
        dataset_arn: "capo_personalize.types.arn.Arn",
        role_arn: "capo_personalize.types.role_arn.RoleArn",
        job_output: "capo_personalize.types.dataset_export_job_output.DatasetExportJobOutput",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        ingestion_mode: Optional[
            "capo_personalize.types.ingestion_mode.IngestionMode"
        ] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_dataset_export_job_response.CreateDatasetExportJobResponse":
        """<p> Creates a job that exports data from your dataset to an Amazon S3 bucket. To allow Amazon Personalize to export the training data, you must specify an service-linked IAM role that gives Amazon Personalize <code>PutObject</code> permissions for your Amazon S3 bucket. For information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/export-data.html">Exporting a dataset</a> in the Amazon Personalize developer guide. </p> <p> <b>Status</b> </p> <p>A dataset export job can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> </ul> <p> To get the status of the export job, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetExportJob.html">DescribeDatasetExportJob</a>, and specify the Amazon Resource Name (ARN) of the dataset export job. The dataset export is complete when the status shows as ACTIVE. If the status shows as CREATE FAILED, the response includes a <code>failureReason</code> key, which describes why the job failed. </p>

        Args:
            job_name: <p>The name for the dataset export job.</p>
            dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset that contains the data to export.</p>
            ingestion_mode: <p>The data to export, based on how you imported the data. You can choose to export only <code>BULK</code> data that you imported using a dataset import job, only <code>PUT</code> data that you imported incrementally (using the console, PutEvents, PutUsers and PutItems operations), or <code>ALL</code> for both types. The default value is <code>PUT</code>. </p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that has permissions to add data to your output Amazon S3 bucket.</p>
            job_output: <p>The path to the Amazon S3 bucket where the job's output is stored.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the dataset export job.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_dataset_export_job_request.CreateDatasetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_dataset_export_job_response.CreateDatasetExportJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_dataset_export_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_dataset_export_job.async_create_dataset_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_dataset_export_job_request.CreateDatasetExportJobRequest = {
            "job_name": job_name,
            "dataset_arn": dataset_arn,
            "role_arn": role_arn,
            "job_output": job_output,
        }
        if ingestion_mode is not None:
            input_["ingestion_mode"] = ingestion_mode
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dataset_group(
        self,
        name: "capo_personalize.types.name.Name",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        role_arn: Optional["capo_personalize.types.role_arn.RoleArn"] = None,
        kms_key_arn: Optional["capo_personalize.types.kms_key_arn.KmsKeyArn"] = None,
        domain: Optional["capo_personalize.types.domain.Domain"] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_dataset_group_response.CreateDatasetGroupResponse":
        """<p>Creates an empty dataset group. A dataset group is a container for Amazon Personalize resources. A dataset group can contain at most three datasets, one for each type of dataset:</p> <ul> <li> <p>Item interactions</p> </li> <li> <p>Items</p> </li> <li> <p>Users</p> </li> <li> <p>Actions</p> </li> <li> <p>Action interactions</p> </li> </ul> <p> A dataset group can be a Domain dataset group, where you specify a domain and use pre-configured resources like recommenders, or a Custom dataset group, where you use custom resources, such as a solution with a solution version, that you deploy with a campaign. If you start with a Domain dataset group, you can still add custom resources such as solutions and solution versions trained with recipes for custom use cases and deployed with campaigns. </p> <p>A dataset group can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING</p> </li> </ul> <p>To get the status of the dataset group, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetGroup.html">DescribeDatasetGroup</a>. If the status shows as CREATE FAILED, the response includes a <code>failureReason</code> key, which describes why the creation failed.</p> <note> <p>You must wait until the <code>status</code> of the dataset group is <code>ACTIVE</code> before adding a dataset to the group.</p> </note> <p>You can specify an Key Management Service (KMS) key to encrypt the datasets in the group. If you specify a KMS key, you must also include an Identity and Access Management (IAM) role that has permission to access the key.</p> <p class="title"> <b>APIs that require a dataset group ARN in the request</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html">CreateDataset</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateEventTracker.html">CreateEventTracker</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html">CreateSolution</a> </p> </li> </ul> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasetGroups.html">ListDatasetGroups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetGroup.html">DescribeDatasetGroup</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteDatasetGroup.html">DeleteDatasetGroup</a> </p> </li> </ul>

        Args:
            name: <p>The name for the new dataset group.</p>
            role_arn: <p>The ARN of the Identity and Access Management (IAM) role that has permissions to access the Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of a Key Management Service (KMS) key used to encrypt the datasets.</p>
            domain: <p>The domain of the dataset group. Specify a domain to create a Domain dataset group. The domain you specify determines the default schemas for datasets and the use cases available for recommenders. If you don't specify a domain, you create a Custom dataset group with solution versions that you deploy with a campaign. </p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the dataset group.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_dataset_group_request.CreateDatasetGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_dataset_group_response.CreateDatasetGroupResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_dataset_group

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_dataset_group.async_create_dataset_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_dataset_group_request.CreateDatasetGroupRequest = {
            "name": name
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if domain is not None:
            input_["domain"] = domain
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dataset_import_job(
        self,
        job_name: "capo_personalize.types.name.Name",
        dataset_arn: "capo_personalize.types.arn.Arn",
        data_source: "capo_personalize.types.data_source.DataSource",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        role_arn: Optional["capo_personalize.types.role_arn.RoleArn"] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
        import_mode: Optional["capo_personalize.types.import_mode.ImportMode"] = None,
        publish_attribution_metrics_to_s3: Optional[
            "capo_personalize.types.boolean.Boolean"
        ] = None,
    ) -> "capo_personalize.types.create_dataset_import_job_response.CreateDatasetImportJobResponse":
        """<p>Creates a job that imports training data from your data source (an Amazon S3 bucket) to an Amazon Personalize dataset. To allow Amazon Personalize to import the training data, you must specify an IAM service role that has permission to read from the data source, as Amazon Personalize makes a copy of your data and processes it internally. For information on granting access to your Amazon S3 bucket, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/granting-personalize-s3-access.html">Giving Amazon Personalize Access to Amazon S3 Resources</a>. </p> <p>If you already created a recommender or deployed a custom solution version with a campaign, how new bulk records influence recommendations depends on the domain use case or recipe that you use. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/how-new-data-influences-recommendations.html">How new data influences real-time recommendations</a>.</p> <important> <p>By default, a dataset import job replaces any existing data in the dataset that you imported in bulk. To add new records without replacing existing data, specify INCREMENTAL for the import mode in the CreateDatasetImportJob operation.</p> </important> <p> <b>Status</b> </p> <p>A dataset import job can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> </ul> <p>To get the status of the import job, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetImportJob.html">DescribeDatasetImportJob</a>, providing the Amazon Resource Name (ARN) of the dataset import job. The dataset import is complete when the status shows as ACTIVE. If the status shows as CREATE FAILED, the response includes a <code>failureReason</code> key, which describes why the job failed.</p> <note> <p>Importing takes time. You must wait until the status shows as ACTIVE before training a model using the dataset.</p> </note> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasetImportJobs.html">ListDatasetImportJobs</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetImportJob.html">DescribeDatasetImportJob</a> </p> </li> </ul>

        Args:
            job_name: <p>The name for the dataset import job.</p>
            dataset_arn: <p>The ARN of the dataset that receives the imported data.</p>
            data_source: <p>The Amazon S3 bucket that contains the training data to import.</p>
            role_arn: <p>The ARN of the IAM role that has permissions to read from the Amazon S3 data source.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the dataset import job.</p>
            import_mode: <p>Specify how to add the new records to an existing dataset. The default import mode is <code>FULL</code>. If you haven't imported bulk records into the dataset previously, you can only specify <code>FULL</code>.</p> <ul> <li> <p>Specify <code>FULL</code> to overwrite all existing bulk data in your dataset. Data you imported individually is not replaced.</p> </li> <li> <p>Specify <code>INCREMENTAL</code> to append the new records to the existing data in your dataset. Amazon Personalize replaces any record with the same ID with the new one.</p> </li> </ul>
            publish_attribution_metrics_to_s3: <p>If you created a metric attribution, specify whether to publish metrics for this import job to Amazon S3</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_dataset_import_job_request.CreateDatasetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_dataset_import_job_response.CreateDatasetImportJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_dataset_import_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_dataset_import_job.async_create_dataset_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_dataset_import_job_request.CreateDatasetImportJobRequest = {
            "job_name": job_name,
            "dataset_arn": dataset_arn,
            "data_source": data_source,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if import_mode is not None:
            input_["import_mode"] = import_mode
        if publish_attribution_metrics_to_s3 is not None:
            input_["publish_attribution_metrics_to_s3"] = (
                publish_attribution_metrics_to_s3
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_event_tracker(
        self,
        name: "capo_personalize.types.name.Name",
        dataset_group_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_event_tracker_response.CreateEventTrackerResponse":
        """<p>Creates an event tracker that you use when adding event data to a specified dataset group using the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html">PutEvents</a> API.</p> <note> <p>Only one event tracker can be associated with a dataset group. You will get an error if you call <code>CreateEventTracker</code> using the same dataset group as an existing event tracker.</p> </note> <p>When you create an event tracker, the response includes a tracking ID, which you pass as a parameter when you use the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html">PutEvents</a> operation. Amazon Personalize then appends the event data to the Item interactions dataset of the dataset group you specify in your event tracker. </p> <p>The event tracker can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul> <p>To get the status of the event tracker, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeEventTracker.html">DescribeEventTracker</a>.</p> <note> <p>The event tracker must be in the ACTIVE state before using the tracking ID.</p> </note> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListEventTrackers.html">ListEventTrackers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeEventTracker.html">DescribeEventTracker</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteEventTracker.html">DeleteEventTracker</a> </p> </li> </ul>

        Args:
            name: <p>The name for the event tracker.</p>
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group that receives the event data.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the event tracker.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_event_tracker_request.CreateEventTrackerRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_event_tracker_response.CreateEventTrackerResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_event_tracker

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_event_tracker.async_create_event_tracker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_event_tracker_request.CreateEventTrackerRequest = {
            "name": name,
            "dataset_group_arn": dataset_group_arn,
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

    async def create_filter(
        self,
        name: "capo_personalize.types.name.Name",
        dataset_group_arn: "capo_personalize.types.arn.Arn",
        filter_expression: "capo_personalize.types.filter_expression.FilterExpression",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_filter_response.CreateFilterResponse":
        """<p>Creates a recommendation filter. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering recommendations and user segments</a>.</p>

        Args:
            name: <p>The name of the filter to create.</p>
            dataset_group_arn: <p>The ARN of the dataset group that the filter will belong to.</p>
            filter_expression: <p>The filter expression defines which items are included or excluded from recommendations. Filter expression must follow specific format rules. For information about filter expression structure and syntax, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter-expressions.html">Filter expressions</a>.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the filter.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_filter_request.CreateFilterRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_filter_response.CreateFilterResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_filter

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_filter.async_create_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_filter_request.CreateFilterRequest = {
            "name": name,
            "dataset_group_arn": dataset_group_arn,
            "filter_expression": filter_expression,
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

    async def create_metric_attribution(
        self,
        name: "capo_personalize.types.name.Name",
        dataset_group_arn: "capo_personalize.types.arn.Arn",
        metrics: "capo_personalize.types.metric_attributes.MetricAttributes",
        metrics_output_config: "capo_personalize.types.metric_attribution_output.MetricAttributionOutput",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.create_metric_attribution_response.CreateMetricAttributionResponse":
        """<p>Creates a metric attribution. A metric attribution creates reports on the data that you import into Amazon Personalize. Depending on how you imported the data, you can view reports in Amazon CloudWatch or Amazon S3. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/measuring-recommendation-impact.html">Measuring impact of recommendations</a>.</p>

        Args:
            name: <p>A name for the metric attribution.</p>
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the destination dataset group for the metric attribution.</p>
            metrics: <p>A list of metric attributes for the metric attribution. Each metric attribute specifies an event type to track and a function. Available functions are <code>SUM()</code> or <code>SAMPLECOUNT()</code>. For SUM() functions, provide the dataset type (either Interactions or Items) and column to sum as a parameter. For example SUM(Items.PRICE).</p>
            metrics_output_config: <p>The output configuration details for the metric attribution.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_metric_attribution_request.CreateMetricAttributionRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_metric_attribution_response.CreateMetricAttributionResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_metric_attribution

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_metric_attribution.async_create_metric_attribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_metric_attribution_request.CreateMetricAttributionRequest = {
            "name": name,
            "dataset_group_arn": dataset_group_arn,
            "metrics": metrics,
            "metrics_output_config": metrics_output_config,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_recommender(
        self,
        name: "capo_personalize.types.name.Name",
        dataset_group_arn: "capo_personalize.types.arn.Arn",
        recipe_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        recommender_config: Optional[
            "capo_personalize.types.recommender_config.RecommenderConfig"
        ] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_recommender_response.CreateRecommenderResponse":
        """<p>Creates a recommender with the recipe (a Domain dataset group use case) you specify. You create recommenders for a Domain dataset group and specify the recommender's Amazon Resource Name (ARN) when you make a <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html">GetRecommendations</a> request. </p> <p> <b>Minimum recommendation requests per second</b> </p> <important> <p>A high <code>minRecommendationRequestsPerSecond</code> will increase your bill. We recommend starting with 1 for <code>minRecommendationRequestsPerSecond</code> (the default). Track your usage using Amazon CloudWatch metrics, and increase the <code>minRecommendationRequestsPerSecond</code> as necessary.</p> </important> <p>When you create a recommender, you can configure the recommender's minimum recommendation requests per second. The minimum recommendation requests per second (<code>minRecommendationRequestsPerSecond</code>) specifies the baseline recommendation request throughput provisioned by Amazon Personalize. The default minRecommendationRequestsPerSecond is <code>1</code>. A recommendation request is a single <code>GetRecommendations</code> operation. Request throughput is measured in requests per second and Amazon Personalize uses your requests per second to derive your requests per hour and the price of your recommender usage. </p> <p> If your requests per second increases beyond <code>minRecommendationRequestsPerSecond</code>, Amazon Personalize auto-scales the provisioned capacity up and down, but never below <code>minRecommendationRequestsPerSecond</code>. There's a short time delay while the capacity is increased that might cause loss of requests.</p> <p> Your bill is the greater of either the minimum requests per hour (based on minRecommendationRequestsPerSecond) or the actual number of requests. The actual request throughput used is calculated as the average requests/second within a one-hour window. We recommend starting with the default <code>minRecommendationRequestsPerSecond</code>, track your usage using Amazon CloudWatch metrics, and then increase the <code>minRecommendationRequestsPerSecond</code> as necessary. </p> <p> <b>Status</b> </p> <p>A recommender can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>STOP PENDING > STOP IN_PROGRESS > INACTIVE > START PENDING > START IN_PROGRESS > ACTIVE</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul> <p>To get the recommender status, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeRecommender.html">DescribeRecommender</a>.</p> <note> <p>Wait until the <code>status</code> of the recommender is <code>ACTIVE</code> before asking the recommender for recommendations.</p> </note> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListRecommenders.html">ListRecommenders</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeRecommender.html">DescribeRecommender</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateRecommender.html">UpdateRecommender</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteRecommender.html">DeleteRecommender</a> </p> </li> </ul>

        Args:
            name: <p>The name of the recommender.</p>
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the destination domain dataset group for the recommender.</p>
            recipe_arn: <p>The Amazon Resource Name (ARN) of the recipe that the recommender will use. For a recommender, a recipe is a Domain dataset group use case. Only Domain dataset group use cases can be used to create a recommender. For information about use cases see <a href="https://docs.aws.amazon.com/personalize/latest/dg/domain-use-cases.html">Choosing recommender use cases</a>. </p>
            recommender_config: <p>The configuration details of the recommender.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the recommender.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_recommender_request.CreateRecommenderRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_recommender_response.CreateRecommenderResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_recommender

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_recommender.async_create_recommender(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_recommender_request.CreateRecommenderRequest = {
            "name": name,
            "dataset_group_arn": dataset_group_arn,
            "recipe_arn": recipe_arn,
        }
        if recommender_config is not None:
            input_["recommender_config"] = recommender_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_schema(
        self,
        name: "capo_personalize.types.name.Name",
        schema: "capo_personalize.types.avro_schema.AvroSchema",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        domain: Optional["capo_personalize.types.domain.Domain"] = None,
    ) -> "capo_personalize.types.create_schema_response.CreateSchemaResponse":
        """<p>Creates an Amazon Personalize schema from the specified schema string. The schema you create must be in Avro JSON format.</p> <p>Amazon Personalize recognizes three schema variants. Each schema is associated with a dataset type and has a set of required field and keywords. If you are creating a schema for a dataset in a Domain dataset group, you provide the domain of the Domain dataset group. You specify a schema when you call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html">CreateDataset</a>.</p> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSchemas.html">ListSchemas</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSchema.html">DescribeSchema</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSchema.html">DeleteSchema</a> </p> </li> </ul>

        Args:
            name: <p>The name for the schema.</p>
            schema: <p>A schema in Avro JSON format.</p>
            domain: <p>The domain for the schema. If you are creating a schema for a dataset in a Domain dataset group, specify the domain you chose when you created the Domain dataset group.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_schema_request.CreateSchemaRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_schema_response.CreateSchemaResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_schema

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_schema.async_create_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_schema_request.CreateSchemaRequest = {
            "name": name,
            "schema": schema,
        }
        if domain is not None:
            input_["domain"] = domain

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_solution(
        self,
        name: "capo_personalize.types.name.Name",
        dataset_group_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        perform_hpo: Optional["capo_personalize.types.boolean.Boolean"] = None,
        perform_auto_ml: Optional[
            "capo_personalize.types.perform_auto_ml.PerformAutoML"
        ] = None,
        perform_auto_training: Optional[
            "capo_personalize.types.perform_auto_training.PerformAutoTraining"
        ] = None,
        perform_incremental_update: Optional[
            "capo_personalize.types.perform_incremental_update.PerformIncrementalUpdate"
        ] = None,
        recipe_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        event_type: Optional["capo_personalize.types.event_type.EventType"] = None,
        solution_config: Optional[
            "capo_personalize.types.solution_config.SolutionConfig"
        ] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_solution_response.CreateSolutionResponse":
        """<important> <p>By default, all new solutions use automatic training. With automatic training, you incur training costs while your solution is active. To avoid unnecessary costs, when you are finished you can <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateSolution.html">update the solution</a> to turn off automatic training. For information about training costs, see <a href="https://aws.amazon.com/personalize/pricing/">Amazon Personalize pricing</a>.</p> </important> <p>Creates the configuration for training a model (creating a solution version). This configuration includes the recipe to use for model training and optional training configuration, such as columns to use in training and feature transformation parameters. For more information about configuring a solution, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html">Creating and configuring a solution</a>. </p> <p> By default, new solutions use automatic training to create solution versions every 7 days. You can change the training frequency. Automatic solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within the hour, the solution skips the first automatic training. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html">Configuring automatic training</a>.</p> <p> To turn off automatic training, set <code>performAutoTraining</code> to false. If you turn off automatic training, you must manually create a solution version by calling the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolutionVersion.html">CreateSolutionVersion</a> operation.</p> <p>After training starts, you can get the solution version's Amazon Resource Name (ARN) with the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html">ListSolutionVersions</a> API operation. To get its status, use the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html">DescribeSolutionVersion</a>. </p> <p>After training completes you can evaluate model accuracy by calling <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_GetSolutionMetrics.html">GetSolutionMetrics</a>. When you are satisfied with the solution version, you deploy it using <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html">CreateCampaign</a>. The campaign provides recommendations to a client through the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html">GetRecommendations</a> API.</p> <note> <p>Amazon Personalize doesn't support configuring the <code>hpoObjective</code> for solution hyperparameter optimization at this time.</p> </note> <p> <b>Status</b> </p> <p>A solution can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul> <p>To get the status of the solution, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html">DescribeSolution</a>. If you use manual training, the status must be ACTIVE before you call <code>CreateSolutionVersion</code>.</p> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateSolution.html">UpdateSolution</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutions.html">ListSolutions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolutionVersion.html">CreateSolutionVersion</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html">DescribeSolution</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSolution.html">DeleteSolution</a> </p> </li> </ul> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html">ListSolutionVersions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html">DescribeSolutionVersion</a> </p> </li> </ul>

        Args:
            name: <p>The name for the solution.</p>
            perform_hpo: <p>Whether to perform hyperparameter optimization (HPO) on the specified or selected recipe. The default is <code>false</code>.</p> <p>When performing AutoML, this parameter is always <code>true</code> and you should not set it to <code>false</code>.</p>
            perform_auto_ml: <important> <p>We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize recipes. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html">Choosing a recipe</a>.</p> </important> <p>Whether to perform automated machine learning (AutoML). The default is <code>false</code>. For this case, you must specify <code>recipeArn</code>.</p> <p>When set to <code>true</code>, Amazon Personalize analyzes your training data and selects the optimal USER_PERSONALIZATION recipe and hyperparameters. In this case, you must omit <code>recipeArn</code>. Amazon Personalize determines the optimal recipe by running tests with different values for the hyperparameters. AutoML lengthens the training process as compared to selecting a specific recipe.</p>
            perform_auto_training: <p>Whether the solution uses automatic training to create new solution versions (trained models). The default is <code>True</code> and the solution automatically creates new solution versions every 7 days. You can change the training frequency by specifying a <code>schedulingExpression</code> in the <code>AutoTrainingConfig</code> as part of solution configuration. For more information about automatic training, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html">Configuring automatic training</a>.</p> <p> Automatic solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within the hour, the solution skips the first automatic training. </p> <p> After training starts, you can get the solution version's Amazon Resource Name (ARN) with the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html">ListSolutionVersions</a> API operation. To get its status, use the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html">DescribeSolutionVersion</a>. </p>
            perform_incremental_update: <p>Whether to perform incremental training updates on your model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe.</p>
            recipe_arn: <p>The Amazon Resource Name (ARN) of the recipe to use for model training. This is required when <code>performAutoML</code> is false. For information about different Amazon Personalize recipes and their ARNs, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html">Choosing a recipe</a>. </p>
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group that provides the training data.</p>
            event_type: <p>When your have multiple event types (using an <code>EVENT_TYPE</code> schema field), this parameter specifies which event type (for example, 'click' or 'like') is used for training the model.</p> <p>If you do not provide an <code>eventType</code>, Amazon Personalize will use all interactions for training with equal weight regardless of type.</p>
            solution_config: <p>The configuration properties for the solution. When <code>performAutoML</code> is set to true, Amazon Personalize only evaluates the <code>autoMLConfig</code> section of the solution configuration.</p> <note> <p>Amazon Personalize doesn't support configuring the <code>hpoObjective</code> at this time.</p> </note>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the solution.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_solution_request.CreateSolutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_solution_response.CreateSolutionResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_solution

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_solution.async_create_solution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_solution_request.CreateSolutionRequest = {
            "name": name,
            "dataset_group_arn": dataset_group_arn,
        }
        if perform_hpo is not None:
            input_["perform_hpo"] = perform_hpo
        if perform_auto_ml is not None:
            input_["perform_auto_ml"] = perform_auto_ml
        if perform_auto_training is not None:
            input_["perform_auto_training"] = perform_auto_training
        if perform_incremental_update is not None:
            input_["perform_incremental_update"] = perform_incremental_update
        if recipe_arn is not None:
            input_["recipe_arn"] = recipe_arn
        if event_type is not None:
            input_["event_type"] = event_type
        if solution_config is not None:
            input_["solution_config"] = solution_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_solution_version(
        self,
        solution_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        name: Optional["capo_personalize.types.name.Name"] = None,
        training_mode: Optional[
            "capo_personalize.types.training_mode.TrainingMode"
        ] = None,
        tags: Optional["capo_personalize.types.tags.Tags"] = None,
    ) -> "capo_personalize.types.create_solution_version_response.CreateSolutionVersionResponse":
        """<p>Trains or retrains an active solution in a Custom dataset group. A solution is created using the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html">CreateSolution</a> operation and must be in the ACTIVE state before calling <code>CreateSolutionVersion</code>. A new version of the solution is created every time you call this operation.</p> <p> <b>Status</b> </p> <p>A solution version can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING</p> </li> <li> <p>CREATE IN_PROGRESS</p> </li> <li> <p>ACTIVE</p> </li> <li> <p>CREATE FAILED</p> </li> <li> <p>CREATE STOPPING</p> </li> <li> <p>CREATE STOPPED</p> </li> </ul> <p>To get the status of the version, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html">DescribeSolutionVersion</a>. Wait until the status shows as ACTIVE before calling <code>CreateCampaign</code>.</p> <p>If the status shows as CREATE FAILED, the response includes a <code>failureReason</code> key, which describes why the job failed.</p> <p class="title"> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html">ListSolutionVersions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html">DescribeSolutionVersion</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutions.html">ListSolutions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html">CreateSolution</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html">DescribeSolution</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSolution.html">DeleteSolution</a> </p> </li> </ul>

        Args:
            name: <p>The name of the solution version.</p>
            solution_arn: <p>The Amazon Resource Name (ARN) of the solution containing the training configuration information.</p>
            training_mode: <p>The scope of training to be performed when creating the solution version. The default is <code>FULL</code>. This creates a completely new model based on the entirety of the training data from the datasets in your dataset group. </p> <p>If you use <a href="https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html">User-Personalization</a>, you can specify a training mode of <code>UPDATE</code>. This updates the model to consider new items for recommendations. It is not a full retraining. You should still complete a full retraining weekly. If you specify <code>UPDATE</code>, Amazon Personalize will stop automatic updates for the solution version. To resume updates, create a new solution with training mode set to <code>FULL</code> and deploy it in a campaign. For more information about automatic updates, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/use-case-recipe-features.html#maintaining-with-automatic-updates">Automatic updates</a>. </p> <p>The <code>UPDATE</code> option can only be used when you already have an active solution version created from the input solution using the <code>FULL</code> option and the input solution was trained with the <a href="https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html">User-Personalization</a> recipe or the legacy <a href="https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-hrnn-coldstart.html">HRNN-Coldstart</a> recipe.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the solution version.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.create_solution_version_request.CreateSolutionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.create_solution_version_response.CreateSolutionVersionResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.create_solution_version

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.create_solution_version.async_create_solution_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.create_solution_version_request.CreateSolutionVersionRequest = {
            "solution_arn": solution_arn
        }
        if name is not None:
            input_["name"] = name
        if training_mode is not None:
            input_["training_mode"] = training_mode
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_campaign(
        self,
        campaign_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Removes a campaign by deleting the solution deployment. The solution that the campaign is based on is not deleted and can be redeployed when needed. A deleted campaign can no longer be specified in a <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html">GetRecommendations</a> request. For information on creating campaigns, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html">CreateCampaign</a>.</p>

        Args:
            campaign_arn: <p>The Amazon Resource Name (ARN) of the campaign to delete.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.delete_campaign

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.delete_campaign.async_delete_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.delete_campaign_request.DeleteCampaignRequest = {
            "campaign_arn": campaign_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataset(
        self,
        dataset_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Deletes a dataset. You can't delete a dataset if an associated <code>DatasetImportJob</code> or <code>SolutionVersion</code> is in the CREATE PENDING or IN PROGRESS state. For more information about deleting datasets, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/delete-dataset.html">Deleting a dataset</a>. </p>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset to delete.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.delete_dataset

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.delete_dataset.async_delete_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.delete_dataset_request.DeleteDatasetRequest = {
            "dataset_arn": dataset_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataset_group(
        self,
        dataset_group_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Deletes a dataset group. Before you delete a dataset group, you must delete the following:</p> <ul> <li> <p>All associated event trackers.</p> </li> <li> <p>All associated solutions.</p> </li> <li> <p>All datasets in the dataset group.</p> </li> </ul>

        Args:
            dataset_group_arn: <p>The ARN of the dataset group to delete.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.delete_dataset_group_request.DeleteDatasetGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.delete_dataset_group

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.delete_dataset_group.async_delete_dataset_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.delete_dataset_group_request.DeleteDatasetGroupRequest = {
            "dataset_group_arn": dataset_group_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_event_tracker(
        self,
        event_tracker_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Deletes the event tracker. Does not delete the dataset from the dataset group. For more information on event trackers, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateEventTracker.html">CreateEventTracker</a>.</p>

        Args:
            event_tracker_arn: <p>The Amazon Resource Name (ARN) of the event tracker to delete.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.delete_event_tracker_request.DeleteEventTrackerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.delete_event_tracker

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.delete_event_tracker.async_delete_event_tracker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.delete_event_tracker_request.DeleteEventTrackerRequest = {
            "event_tracker_arn": event_tracker_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_filter(
        self,
        filter_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Deletes a filter.</p>

        Args:
            filter_arn: <p>The ARN of the filter to delete.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.delete_filter_request.DeleteFilterRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.delete_filter

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.delete_filter.async_delete_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.delete_filter_request.DeleteFilterRequest = {
            "filter_arn": filter_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_metric_attribution(
        self,
        metric_attribution_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Deletes a metric attribution.</p>

        Args:
            metric_attribution_arn: <p>The metric attribution's Amazon Resource Name (ARN).</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.delete_metric_attribution_request.DeleteMetricAttributionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.delete_metric_attribution

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.delete_metric_attribution.async_delete_metric_attribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.delete_metric_attribution_request.DeleteMetricAttributionRequest = {
            "metric_attribution_arn": metric_attribution_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_recommender(
        self,
        recommender_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Deactivates and removes a recommender. A deleted recommender can no longer be specified in a <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html">GetRecommendations</a> request.</p>

        Args:
            recommender_arn: <p>The Amazon Resource Name (ARN) of the recommender to delete.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.delete_recommender_request.DeleteRecommenderRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.delete_recommender

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.delete_recommender.async_delete_recommender(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.delete_recommender_request.DeleteRecommenderRequest = {
            "recommender_arn": recommender_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_schema(
        self,
        schema_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Deletes a schema. Before deleting a schema, you must delete all datasets referencing the schema. For more information on schemas, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSchema.html">CreateSchema</a>.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) of the schema to delete.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.delete_schema_request.DeleteSchemaRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.delete_schema

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.delete_schema.async_delete_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.delete_schema_request.DeleteSchemaRequest = {
            "schema_arn": schema_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_solution(
        self,
        solution_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Deletes all versions of a solution and the <code>Solution</code> object itself. Before deleting a solution, you must delete all campaigns based on the solution. To determine what campaigns are using the solution, call <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListCampaigns.html">ListCampaigns</a> and supply the Amazon Resource Name (ARN) of the solution. You can't delete a solution if an associated <code>SolutionVersion</code> is in the CREATE PENDING or IN PROGRESS state. For more information on solutions, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html">CreateSolution</a>.</p>

        Args:
            solution_arn: <p>The ARN of the solution to delete.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.delete_solution_request.DeleteSolutionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.delete_solution

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.delete_solution.async_delete_solution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.delete_solution_request.DeleteSolutionRequest = {
            "solution_arn": solution_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_algorithm(
        self,
        algorithm_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_algorithm_response.DescribeAlgorithmResponse":
        """<p>Describes the given algorithm.</p>

        Args:
            algorithm_arn: <p>The Amazon Resource Name (ARN) of the algorithm to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_algorithm_request.DescribeAlgorithmRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_algorithm_response.DescribeAlgorithmResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_algorithm

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_algorithm.async_describe_algorithm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_algorithm_request.DescribeAlgorithmRequest = {
            "algorithm_arn": algorithm_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_batch_inference_job(
        self,
        batch_inference_job_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_batch_inference_job_response.DescribeBatchInferenceJobResponse":
        """<p>Gets the properties of a batch inference job including name, Amazon Resource Name (ARN), status, input and output configurations, and the ARN of the solution version used to generate the recommendations.</p>

        Args:
            batch_inference_job_arn: <p>The ARN of the batch inference job to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_batch_inference_job_request.DescribeBatchInferenceJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_batch_inference_job_response.DescribeBatchInferenceJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_batch_inference_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_batch_inference_job.async_describe_batch_inference_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_batch_inference_job_request.DescribeBatchInferenceJobRequest = {
            "batch_inference_job_arn": batch_inference_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_batch_segment_job(
        self,
        batch_segment_job_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_batch_segment_job_response.DescribeBatchSegmentJobResponse":
        """<p>Gets the properties of a batch segment job including name, Amazon Resource Name (ARN), status, input and output configurations, and the ARN of the solution version used to generate segments.</p>

        Args:
            batch_segment_job_arn: <p>The ARN of the batch segment job to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_batch_segment_job_request.DescribeBatchSegmentJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_batch_segment_job_response.DescribeBatchSegmentJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_batch_segment_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_batch_segment_job.async_describe_batch_segment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_batch_segment_job_request.DescribeBatchSegmentJobRequest = {
            "batch_segment_job_arn": batch_segment_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_campaign(
        self,
        campaign_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_campaign_response.DescribeCampaignResponse":
        """<p>Describes the given campaign, including its status.</p> <p>A campaign can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul> <p>When the <code>status</code> is <code>CREATE FAILED</code>, the response includes the <code>failureReason</code> key, which describes why.</p> <p>For more information on campaigns, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html">CreateCampaign</a>.</p>

        Args:
            campaign_arn: <p>The Amazon Resource Name (ARN) of the campaign.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_campaign_request.DescribeCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_campaign_response.DescribeCampaignResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_campaign

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_campaign.async_describe_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_campaign_request.DescribeCampaignRequest = {
            "campaign_arn": campaign_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_data_deletion_job(
        self,
        data_deletion_job_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_data_deletion_job_response.DescribeDataDeletionJobResponse":
        """<p>Describes the data deletion job created by <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataDeletionJob.html">CreateDataDeletionJob</a>, including the job status.</p>

        Args:
            data_deletion_job_arn: <p>The Amazon Resource Name (ARN) of the data deletion job.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_data_deletion_job_request.DescribeDataDeletionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_data_deletion_job_response.DescribeDataDeletionJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_data_deletion_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_data_deletion_job.async_describe_data_deletion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_data_deletion_job_request.DescribeDataDeletionJobRequest = {
            "data_deletion_job_arn": data_deletion_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset(
        self,
        dataset_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_dataset_response.DescribeDatasetResponse":
        """<p>Describes the given dataset. For more information on datasets, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html">CreateDataset</a>.</p>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_dataset

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_dataset.async_describe_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_dataset_request.DescribeDatasetRequest = {
            "dataset_arn": dataset_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset_export_job(
        self,
        dataset_export_job_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_dataset_export_job_response.DescribeDatasetExportJobResponse":
        """<p>Describes the dataset export job created by <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetExportJob.html">CreateDatasetExportJob</a>, including the export job status.</p>

        Args:
            dataset_export_job_arn: <p>The Amazon Resource Name (ARN) of the dataset export job to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_dataset_export_job_request.DescribeDatasetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_dataset_export_job_response.DescribeDatasetExportJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_dataset_export_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_dataset_export_job.async_describe_dataset_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_dataset_export_job_request.DescribeDatasetExportJobRequest = {
            "dataset_export_job_arn": dataset_export_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset_group(
        self,
        dataset_group_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_dataset_group_response.DescribeDatasetGroupResponse":
        """<p>Describes the given dataset group. For more information on dataset groups, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a>.</p>

        Args:
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_dataset_group_request.DescribeDatasetGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_dataset_group_response.DescribeDatasetGroupResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_dataset_group

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_dataset_group.async_describe_dataset_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_dataset_group_request.DescribeDatasetGroupRequest = {
            "dataset_group_arn": dataset_group_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset_import_job(
        self,
        dataset_import_job_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_dataset_import_job_response.DescribeDatasetImportJobResponse":
        """<p>Describes the dataset import job created by <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a>, including the import job status.</p>

        Args:
            dataset_import_job_arn: <p>The Amazon Resource Name (ARN) of the dataset import job to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_dataset_import_job_request.DescribeDatasetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_dataset_import_job_response.DescribeDatasetImportJobResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_dataset_import_job

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_dataset_import_job.async_describe_dataset_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_dataset_import_job_request.DescribeDatasetImportJobRequest = {
            "dataset_import_job_arn": dataset_import_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_event_tracker(
        self,
        event_tracker_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_event_tracker_response.DescribeEventTrackerResponse":
        """<p>Describes an event tracker. The response includes the <code>trackingId</code> and <code>status</code> of the event tracker. For more information on event trackers, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateEventTracker.html">CreateEventTracker</a>.</p>

        Args:
            event_tracker_arn: <p>The Amazon Resource Name (ARN) of the event tracker to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_event_tracker_request.DescribeEventTrackerRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_event_tracker_response.DescribeEventTrackerResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_event_tracker

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_event_tracker.async_describe_event_tracker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_event_tracker_request.DescribeEventTrackerRequest = {
            "event_tracker_arn": event_tracker_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_feature_transformation(
        self,
        feature_transformation_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_feature_transformation_response.DescribeFeatureTransformationResponse":
        """<p>Describes the given feature transformation.</p>

        Args:
            feature_transformation_arn: <p>The Amazon Resource Name (ARN) of the feature transformation to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_feature_transformation_request.DescribeFeatureTransformationRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_feature_transformation_response.DescribeFeatureTransformationResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_feature_transformation

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_feature_transformation.async_describe_feature_transformation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_feature_transformation_request.DescribeFeatureTransformationRequest = {
            "feature_transformation_arn": feature_transformation_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_filter(
        self,
        filter_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_filter_response.DescribeFilterResponse":
        """<p>Describes a filter's properties.</p>

        Args:
            filter_arn: <p>The ARN of the filter to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_filter_request.DescribeFilterRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_filter_response.DescribeFilterResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_filter

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_filter.async_describe_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_filter_request.DescribeFilterRequest = {
            "filter_arn": filter_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_metric_attribution(
        self,
        metric_attribution_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_metric_attribution_response.DescribeMetricAttributionResponse":
        """<p>Describes a metric attribution.</p>

        Args:
            metric_attribution_arn: <p>The metric attribution's Amazon Resource Name (ARN).</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_metric_attribution_request.DescribeMetricAttributionRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_metric_attribution_response.DescribeMetricAttributionResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_metric_attribution

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_metric_attribution.async_describe_metric_attribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_metric_attribution_request.DescribeMetricAttributionRequest = {
            "metric_attribution_arn": metric_attribution_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_recipe(
        self,
        recipe_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_recipe_response.DescribeRecipeResponse":
        """<p>Describes a recipe.</p> <p>A recipe contains three items:</p> <ul> <li> <p>An algorithm that trains a model.</p> </li> <li> <p>Hyperparameters that govern the training.</p> </li> <li> <p>Feature transformation information for modifying the input data before training.</p> </li> </ul> <p>Amazon Personalize provides a set of predefined recipes. You specify a recipe when you create a solution with the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html">CreateSolution</a> API. <code>CreateSolution</code> trains a model by using the algorithm in the specified recipe and a training dataset. The solution, when deployed as a campaign, can provide recommendations using the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html">GetRecommendations</a> API.</p>

        Args:
            recipe_arn: <p>The Amazon Resource Name (ARN) of the recipe to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_recipe_request.DescribeRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_recipe_response.DescribeRecipeResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_recipe

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_recipe.async_describe_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_recipe_request.DescribeRecipeRequest = {
            "recipe_arn": recipe_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_recommender(
        self,
        recommender_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_recommender_response.DescribeRecommenderResponse":
        """<p>Describes the given recommender, including its status.</p> <p>A recommender can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>STOP PENDING > STOP IN_PROGRESS > INACTIVE > START PENDING > START IN_PROGRESS > ACTIVE</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul> <p>When the <code>status</code> is <code>CREATE FAILED</code>, the response includes the <code>failureReason</code> key, which describes why.</p> <p>The <code>modelMetrics</code> key is null when the recommender is being created or deleted.</p> <p>For more information on recommenders, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateRecommender.html">CreateRecommender</a>.</p>

        Args:
            recommender_arn: <p>The Amazon Resource Name (ARN) of the recommender to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_recommender_request.DescribeRecommenderRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_recommender_response.DescribeRecommenderResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_recommender

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_recommender.async_describe_recommender(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_recommender_request.DescribeRecommenderRequest = {
            "recommender_arn": recommender_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_schema(
        self,
        schema_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_schema_response.DescribeSchemaResponse":
        """<p>Describes a schema. For more information on schemas, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSchema.html">CreateSchema</a>.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) of the schema to retrieve.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_schema_request.DescribeSchemaRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_schema_response.DescribeSchemaResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_schema

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_schema.async_describe_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_schema_request.DescribeSchemaRequest = {
            "schema_arn": schema_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_solution(
        self,
        solution_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_solution_response.DescribeSolutionResponse":
        """<p>Describes a solution. For more information on solutions, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html">CreateSolution</a>.</p>

        Args:
            solution_arn: <p>The Amazon Resource Name (ARN) of the solution to describe.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_solution_request.DescribeSolutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_solution_response.DescribeSolutionResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_solution

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_solution.async_describe_solution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_solution_request.DescribeSolutionRequest = {
            "solution_arn": solution_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_solution_version(
        self,
        solution_version_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.describe_solution_version_response.DescribeSolutionVersionResponse":
        """<p>Describes a specific version of a solution. For more information on solutions, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html">CreateSolution</a> </p>

        Args:
            solution_version_arn: <p>The Amazon Resource Name (ARN) of the solution version.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.describe_solution_version_request.DescribeSolutionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.describe_solution_version_response.DescribeSolutionVersionResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.describe_solution_version

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.describe_solution_version.async_describe_solution_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.describe_solution_version_request.DescribeSolutionVersionRequest = {
            "solution_version_arn": solution_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_solution_metrics(
        self,
        solution_version_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.get_solution_metrics_response.GetSolutionMetricsResponse":
        """<p>Gets the metrics for the specified solution version.</p>

        Args:
            solution_version_arn: <p>The Amazon Resource Name (ARN) of the solution version for which to get metrics.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.get_solution_metrics_request.GetSolutionMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.get_solution_metrics_response.GetSolutionMetricsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.get_solution_metrics

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.get_solution_metrics.async_get_solution_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.get_solution_metrics_request.GetSolutionMetricsRequest = {
            "solution_version_arn": solution_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_batch_inference_jobs(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        solution_version_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_batch_inference_jobs_response.ListBatchInferenceJobsResponse":
        """<p>Gets a list of the batch inference jobs that have been performed off of a solution version.</p>

        Args:
            solution_version_arn: <p>The Amazon Resource Name (ARN) of the solution version from which the batch inference jobs were created.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of batch inference job results to return in each page. The default value is 100.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_batch_inference_jobs_request.ListBatchInferenceJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_batch_inference_jobs_response.ListBatchInferenceJobsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_batch_inference_jobs

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_batch_inference_jobs.async_list_batch_inference_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_batch_inference_jobs_request.ListBatchInferenceJobsRequest = {}
        if solution_version_arn is not None:
            input_["solution_version_arn"] = solution_version_arn
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

    async def iter_list_batch_inference_jobs(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        solution_version_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.batch_inference_job_summary.BatchInferenceJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_batch_inference_jobs(
                config_overrides=config_overrides,
                solution_version_arn=solution_version_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("batch_inference_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_batch_segment_jobs(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        solution_version_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_batch_segment_jobs_response.ListBatchSegmentJobsResponse":
        """<p>Gets a list of the batch segment jobs that have been performed off of a solution version that you specify.</p>

        Args:
            solution_version_arn: <p>The Amazon Resource Name (ARN) of the solution version that the batch segment jobs used to generate batch segments.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of batch segment job results to return in each page. The default value is 100.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_batch_segment_jobs_request.ListBatchSegmentJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_batch_segment_jobs_response.ListBatchSegmentJobsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_batch_segment_jobs

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_batch_segment_jobs.async_list_batch_segment_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_batch_segment_jobs_request.ListBatchSegmentJobsRequest = {}
        if solution_version_arn is not None:
            input_["solution_version_arn"] = solution_version_arn
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

    async def iter_list_batch_segment_jobs(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        solution_version_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.batch_segment_job_summary.BatchSegmentJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_batch_segment_jobs(
                config_overrides=config_overrides,
                solution_version_arn=solution_version_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("batch_segment_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_campaigns(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        solution_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_campaigns_response.ListCampaignsResponse":
        """<p>Returns a list of campaigns that use the given solution. When a solution is not specified, all the campaigns associated with the account are listed. The response provides the properties for each campaign, including the Amazon Resource Name (ARN). For more information on campaigns, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html">CreateCampaign</a>.</p>

        Args:
            solution_arn: <p>The Amazon Resource Name (ARN) of the solution to list the campaigns for. When a solution is not specified, all the campaigns associated with the account are listed.</p>
            next_token: <p>A token returned from the previous call to <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListCampaigns.html">ListCampaigns</a> for getting the next set of campaigns (if they exist).</p>
            max_results: <p>The maximum number of campaigns to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_campaigns_request.ListCampaignsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_campaigns_response.ListCampaignsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_campaigns

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_campaigns.async_list_campaigns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_campaigns_request.ListCampaignsRequest = {}
        if solution_arn is not None:
            input_["solution_arn"] = solution_arn
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

    async def iter_list_campaigns(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        solution_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.campaign_summary.CampaignSummary]":
        _token = next_token
        while True:
            _response = await self.list_campaigns(
                config_overrides=config_overrides,
                solution_arn=solution_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("campaigns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_deletion_jobs(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_data_deletion_jobs_response.ListDataDeletionJobsResponse":
        """<p>Returns a list of data deletion jobs for a dataset group ordered by creation time, with the most recent first. When a dataset group is not specified, all the data deletion jobs associated with the account are listed. The response provides the properties for each job, including the Amazon Resource Name (ARN). For more information on data deletion jobs, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/delete-records.html">Deleting users</a>.</p>

        Args:
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group to list data deletion jobs for.</p>
            next_token: <p>A token returned from the previous call to <code>ListDataDeletionJobs</code> for getting the next set of jobs (if they exist).</p>
            max_results: <p>The maximum number of data deletion jobs to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_data_deletion_jobs_request.ListDataDeletionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_data_deletion_jobs_response.ListDataDeletionJobsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_data_deletion_jobs

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_data_deletion_jobs.async_list_data_deletion_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_data_deletion_jobs_request.ListDataDeletionJobsRequest = {}
        if dataset_group_arn is not None:
            input_["dataset_group_arn"] = dataset_group_arn
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

    async def list_dataset_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_dataset_export_jobs_response.ListDatasetExportJobsResponse":
        """<p>Returns a list of dataset export jobs that use the given dataset. When a dataset is not specified, all the dataset export jobs associated with the account are listed. The response provides the properties for each dataset export job, including the Amazon Resource Name (ARN). For more information on dataset export jobs, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetExportJob.html">CreateDatasetExportJob</a>. For more information on datasets, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html">CreateDataset</a>.</p>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset to list the dataset export jobs for.</p>
            next_token: <p>A token returned from the previous call to <code>ListDatasetExportJobs</code> for getting the next set of dataset export jobs (if they exist).</p>
            max_results: <p>The maximum number of dataset export jobs to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_dataset_export_jobs_request.ListDatasetExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_dataset_export_jobs_response.ListDatasetExportJobsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_dataset_export_jobs

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_dataset_export_jobs.async_list_dataset_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_dataset_export_jobs_request.ListDatasetExportJobsRequest = {}
        if dataset_arn is not None:
            input_["dataset_arn"] = dataset_arn
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

    async def iter_list_dataset_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.dataset_export_job_summary.DatasetExportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_dataset_export_jobs(
                config_overrides=config_overrides,
                dataset_arn=dataset_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dataset_export_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dataset_groups(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_personalize.types.list_dataset_groups_response.ListDatasetGroupsResponse"
    ):
        """<p>Returns a list of dataset groups. The response provides the properties for each dataset group, including the Amazon Resource Name (ARN). For more information on dataset groups, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a>.</p>

        Args:
            next_token: <p>A token returned from the previous call to <code>ListDatasetGroups</code> for getting the next set of dataset groups (if they exist).</p>
            max_results: <p>The maximum number of dataset groups to return.</p>

        Raises:
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_dataset_groups_request.ListDatasetGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_dataset_groups_response.ListDatasetGroupsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_dataset_groups

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_dataset_groups.async_list_dataset_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_dataset_groups_request.ListDatasetGroupsRequest = {}
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

    async def iter_list_dataset_groups(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.dataset_group_summary.DatasetGroupSummary]":
        _token = next_token
        while True:
            _response = await self.list_dataset_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dataset_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dataset_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_dataset_import_jobs_response.ListDatasetImportJobsResponse":
        """<p>Returns a list of dataset import jobs that use the given dataset. When a dataset is not specified, all the dataset import jobs associated with the account are listed. The response provides the properties for each dataset import job, including the Amazon Resource Name (ARN). For more information on dataset import jobs, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a>. For more information on datasets, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html">CreateDataset</a>.</p>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset to list the dataset import jobs for.</p>
            next_token: <p>A token returned from the previous call to <code>ListDatasetImportJobs</code> for getting the next set of dataset import jobs (if they exist).</p>
            max_results: <p>The maximum number of dataset import jobs to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_dataset_import_jobs_request.ListDatasetImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_dataset_import_jobs_response.ListDatasetImportJobsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_dataset_import_jobs

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_dataset_import_jobs.async_list_dataset_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_dataset_import_jobs_request.ListDatasetImportJobsRequest = {}
        if dataset_arn is not None:
            input_["dataset_arn"] = dataset_arn
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

    async def iter_list_dataset_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.dataset_import_job_summary.DatasetImportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_dataset_import_jobs(
                config_overrides=config_overrides,
                dataset_arn=dataset_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dataset_import_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_datasets_response.ListDatasetsResponse":
        """<p>Returns the list of datasets contained in the given dataset group. The response provides the properties for each dataset, including the Amazon Resource Name (ARN). For more information on datasets, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html">CreateDataset</a>.</p>

        Args:
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group that contains the datasets to list.</p>
            next_token: <p>A token returned from the previous call to <code>ListDatasets</code> for getting the next set of dataset import jobs (if they exist).</p>
            max_results: <p>The maximum number of datasets to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_datasets_request.ListDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_datasets

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_datasets_request.ListDatasetsRequest = {}
        if dataset_group_arn is not None:
            input_["dataset_group_arn"] = dataset_group_arn
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

    async def iter_list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.dataset_summary.DatasetSummary]":
        _token = next_token
        while True:
            _response = await self.list_datasets(
                config_overrides=config_overrides,
                dataset_group_arn=dataset_group_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("datasets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_event_trackers(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_personalize.types.list_event_trackers_response.ListEventTrackersResponse"
    ):
        """<p>Returns the list of event trackers associated with the account. The response provides the properties for each event tracker, including the Amazon Resource Name (ARN) and tracking ID. For more information on event trackers, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateEventTracker.html">CreateEventTracker</a>.</p>

        Args:
            dataset_group_arn: <p>The ARN of a dataset group used to filter the response.</p>
            next_token: <p>A token returned from the previous call to <code>ListEventTrackers</code> for getting the next set of event trackers (if they exist).</p>
            max_results: <p>The maximum number of event trackers to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_event_trackers_request.ListEventTrackersRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_event_trackers_response.ListEventTrackersResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_event_trackers

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_event_trackers.async_list_event_trackers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_event_trackers_request.ListEventTrackersRequest = {}
        if dataset_group_arn is not None:
            input_["dataset_group_arn"] = dataset_group_arn
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

    async def iter_list_event_trackers(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.event_tracker_summary.EventTrackerSummary]":
        _token = next_token
        while True:
            _response = await self.list_event_trackers(
                config_overrides=config_overrides,
                dataset_group_arn=dataset_group_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_trackers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_filters(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_filters_response.ListFiltersResponse":
        """<p>Lists all filters that belong to a given dataset group.</p>

        Args:
            dataset_group_arn: <p>The ARN of the dataset group that contains the filters.</p>
            next_token: <p>A token returned from the previous call to <code>ListFilters</code> for getting the next set of filters (if they exist).</p>
            max_results: <p>The maximum number of filters to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_filters_request.ListFiltersRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_filters_response.ListFiltersResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_filters

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_filters.async_list_filters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_filters_request.ListFiltersRequest = {}
        if dataset_group_arn is not None:
            input_["dataset_group_arn"] = dataset_group_arn
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

    async def iter_list_filters(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.filter_summary.FilterSummary]":
        _token = next_token
        while True:
            _response = await self.list_filters(
                config_overrides=config_overrides,
                dataset_group_arn=dataset_group_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("filters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_metric_attribution_metrics(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        metric_attribution_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_metric_attribution_metrics_response.ListMetricAttributionMetricsResponse":
        """<p>Lists the metrics for the metric attribution.</p>

        Args:
            metric_attribution_arn: <p>The Amazon Resource Name (ARN) of the metric attribution to retrieve attributes for.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of metrics to return in one page of results.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_metric_attribution_metrics_request.ListMetricAttributionMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_metric_attribution_metrics_response.ListMetricAttributionMetricsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_metric_attribution_metrics

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_metric_attribution_metrics.async_list_metric_attribution_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_metric_attribution_metrics_request.ListMetricAttributionMetricsRequest = {}
        if metric_attribution_arn is not None:
            input_["metric_attribution_arn"] = metric_attribution_arn
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

    async def iter_list_metric_attribution_metrics(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        metric_attribution_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.metric_attribute.MetricAttribute]":
        _token = next_token
        while True:
            _response = await self.list_metric_attribution_metrics(
                config_overrides=config_overrides,
                metric_attribution_arn=metric_attribution_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("metrics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_metric_attributions(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_metric_attributions_response.ListMetricAttributionsResponse":
        """<p>Lists metric attributions.</p>

        Args:
            dataset_group_arn: <p>The metric attributions' dataset group Amazon Resource Name (ARN).</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of metric attributions to return in one page of results.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_metric_attributions_request.ListMetricAttributionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_metric_attributions_response.ListMetricAttributionsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_metric_attributions

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_metric_attributions.async_list_metric_attributions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_metric_attributions_request.ListMetricAttributionsRequest = {}
        if dataset_group_arn is not None:
            input_["dataset_group_arn"] = dataset_group_arn
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

    async def iter_list_metric_attributions(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.metric_attribution_summary.MetricAttributionSummary]":
        _token = next_token
        while True:
            _response = await self.list_metric_attributions(
                config_overrides=config_overrides,
                dataset_group_arn=dataset_group_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("metric_attributions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recipes(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        recipe_provider: Optional[
            "capo_personalize.types.recipe_provider.RecipeProvider"
        ] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
        domain: Optional["capo_personalize.types.domain.Domain"] = None,
    ) -> "capo_personalize.types.list_recipes_response.ListRecipesResponse":
        """<p>Returns a list of available recipes. The response provides the properties for each recipe, including the recipe's Amazon Resource Name (ARN).</p>

        Args:
            recipe_provider: <p>The default is <code>SERVICE</code>.</p>
            next_token: <p>A token returned from the previous call to <code>ListRecipes</code> for getting the next set of recipes (if they exist).</p>
            max_results: <p>The maximum number of recipes to return.</p>
            domain: <p> Filters returned recipes by domain for a Domain dataset group. Only recipes (Domain dataset group use cases) for this domain are included in the response. If you don't specify a domain, all recipes are returned. </p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_recipes_request.ListRecipesRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_recipes_response.ListRecipesResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_recipes

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_recipes.async_list_recipes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_recipes_request.ListRecipesRequest = {}
        if recipe_provider is not None:
            input_["recipe_provider"] = recipe_provider
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if domain is not None:
            input_["domain"] = domain

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_recipes(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        recipe_provider: Optional[
            "capo_personalize.types.recipe_provider.RecipeProvider"
        ] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
        domain: Optional["capo_personalize.types.domain.Domain"] = None,
    ) -> "AsyncIterator[capo_personalize.types.recipe_summary.RecipeSummary]":
        _token = next_token
        while True:
            _response = await self.list_recipes(
                config_overrides=config_overrides,
                recipe_provider=recipe_provider,
                next_token=_token,
                max_results=max_results,
                domain=domain,
            )
            _page = _resolve_path(_response, ("recipes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommenders(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_recommenders_response.ListRecommendersResponse":
        """<p>Returns a list of recommenders in a given Domain dataset group. When a Domain dataset group is not specified, all the recommenders associated with the account are listed. The response provides the properties for each recommender, including the Amazon Resource Name (ARN). For more information on recommenders, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateRecommender.html">CreateRecommender</a>.</p>

        Args:
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the Domain dataset group to list the recommenders for. When a Domain dataset group is not specified, all the recommenders associated with the account are listed.</p>
            next_token: <p>A token returned from the previous call to <code>ListRecommenders</code> for getting the next set of recommenders (if they exist).</p>
            max_results: <p>The maximum number of recommenders to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_recommenders_request.ListRecommendersRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_recommenders_response.ListRecommendersResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_recommenders

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_recommenders.async_list_recommenders(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_recommenders_request.ListRecommendersRequest = {}
        if dataset_group_arn is not None:
            input_["dataset_group_arn"] = dataset_group_arn
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

    async def iter_list_recommenders(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.recommender_summary.RecommenderSummary]":
        _token = next_token
        while True:
            _response = await self.list_recommenders(
                config_overrides=config_overrides,
                dataset_group_arn=dataset_group_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("recommenders",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_schemas(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_schemas_response.ListSchemasResponse":
        """<p>Returns the list of schemas associated with the account. The response provides the properties for each schema, including the Amazon Resource Name (ARN). For more information on schemas, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSchema.html">CreateSchema</a>.</p>

        Args:
            next_token: <p>A token returned from the previous call to <code>ListSchemas</code> for getting the next set of schemas (if they exist).</p>
            max_results: <p>The maximum number of schemas to return.</p>

        Raises:
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_schemas_request.ListSchemasRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_schemas_response.ListSchemasResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_schemas

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_schemas.async_list_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_schemas_request.ListSchemasRequest = {}
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

    async def iter_list_schemas(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.dataset_schema_summary.DatasetSchemaSummary]":
        _token = next_token
        while True:
            _response = await self.list_schemas(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_solutions(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_solutions_response.ListSolutionsResponse":
        """<p>Returns a list of solutions in a given dataset group. When a dataset group is not specified, all the solutions associated with the account are listed. The response provides the properties for each solution, including the Amazon Resource Name (ARN). For more information on solutions, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html">CreateSolution</a>.</p>

        Args:
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group.</p>
            next_token: <p>A token returned from the previous call to <code>ListSolutions</code> for getting the next set of solutions (if they exist).</p>
            max_results: <p>The maximum number of solutions to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_solutions_request.ListSolutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_solutions_response.ListSolutionsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_solutions

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_solutions.async_list_solutions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_solutions_request.ListSolutionsRequest = {}
        if dataset_group_arn is not None:
            input_["dataset_group_arn"] = dataset_group_arn
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

    async def iter_list_solutions(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        dataset_group_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.solution_summary.SolutionSummary]":
        _token = next_token
        while True:
            _response = await self.list_solutions(
                config_overrides=config_overrides,
                dataset_group_arn=dataset_group_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("solutions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_solution_versions(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        solution_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "capo_personalize.types.list_solution_versions_response.ListSolutionVersionsResponse":
        """<p>Returns a list of solution versions for the given solution. When a solution is not specified, all the solution versions associated with the account are listed. The response provides the properties for each solution version, including the Amazon Resource Name (ARN).</p>

        Args:
            solution_arn: <p>The Amazon Resource Name (ARN) of the solution.</p>
            next_token: <p>A token returned from the previous call to <code>ListSolutionVersions</code> for getting the next set of solution versions (if they exist).</p>
            max_results: <p>The maximum number of solution versions to return.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_solution_versions_request.ListSolutionVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_solution_versions_response.ListSolutionVersionsResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_solution_versions

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_solution_versions.async_list_solution_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_solution_versions_request.ListSolutionVersionsRequest = {}
        if solution_arn is not None:
            input_["solution_arn"] = solution_arn
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

    async def iter_list_solution_versions(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        solution_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        next_token: Optional["capo_personalize.types.next_token.NextToken"] = None,
        max_results: Optional["capo_personalize.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_personalize.types.solution_version_summary.SolutionVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_solution_versions(
                config_overrides=config_overrides,
                solution_arn=solution_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("solution_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Get a list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> attached to a resource.</p>

        Args:
            resource_arn: <p>The resource's Amazon Resource Name (ARN).</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_recommender(
        self,
        recommender_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.start_recommender_response.StartRecommenderResponse":
        """<p>Starts a recommender that is INACTIVE. Starting a recommender does not create any new models, but resumes billing and automatic retraining for the recommender.</p>

        Args:
            recommender_arn: <p>The Amazon Resource Name (ARN) of the recommender to start.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.start_recommender_request.StartRecommenderRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.start_recommender_response.StartRecommenderResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.start_recommender

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.start_recommender.async_start_recommender(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.start_recommender_request.StartRecommenderRequest = {
            "recommender_arn": recommender_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_recommender(
        self,
        recommender_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.stop_recommender_response.StopRecommenderResponse":
        """<p>Stops a recommender that is ACTIVE. Stopping a recommender halts billing and automatic retraining for the recommender.</p>

        Args:
            recommender_arn: <p>The Amazon Resource Name (ARN) of the recommender to stop.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.stop_recommender_request.StopRecommenderRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.stop_recommender_response.StopRecommenderResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.stop_recommender

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.stop_recommender.async_stop_recommender(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.stop_recommender_request.StopRecommenderRequest = {
            "recommender_arn": recommender_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_solution_version_creation(
        self,
        solution_version_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> None:
        """<p>Stops creating a solution version that is in a state of CREATE_PENDING or CREATE IN_PROGRESS. </p> <p>Depending on the current state of the solution version, the solution version state changes as follows:</p> <ul> <li> <p>CREATE_PENDING > CREATE_STOPPED</p> <p>or</p> </li> <li> <p>CREATE_IN_PROGRESS > CREATE_STOPPING > CREATE_STOPPED</p> </li> </ul> <p>You are billed for all of the training completed up until you stop the solution version creation. You cannot resume creating a solution version once it has been stopped.</p>

        Args:
            solution_version_arn: <p>The Amazon Resource Name (ARN) of the solution version you want to stop creating.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.stop_solution_version_creation_request.StopSolutionVersionCreationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_personalize._operations.amazon_personalize.stop_solution_version_creation

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.stop_solution_version_creation.async_stop_solution_version_creation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.stop_solution_version_creation_request.StopSolutionVersionCreationRequest = {
            "solution_version_arn": solution_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_personalize.types.arn.Arn",
        tags: "capo_personalize.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.tag_resource_response.TagResourceResponse":
        """<p>Add a list of tags to a resource.</p>

        Args:
            resource_arn: <p>The resource's Amazon Resource Name (ARN).</p>
            tags: <p>Tags to apply to the resource. For more information see <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">Tagging Amazon Personalize resources</a>.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource. </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.tag_resource

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_personalize.types.arn.Arn",
        tag_keys: "capo_personalize.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags that are attached to a resource. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/tags-remove.html">Removing tags from Amazon Personalize resources</a>.</p>

        Args:
            resource_arn: <p>The resource's Amazon Resource Name (ARN).</p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.too_many_tag_keys_exception.TooManyTagKeysException: <p>The request contains more tag keys than can be associated with a resource (50 tag keys per resource). </p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.untag_resource

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_campaign(
        self,
        campaign_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        solution_version_arn: Optional["capo_personalize.types.arn.Arn"] = None,
        min_provisioned_tps: Optional[
            "capo_personalize.types.transactions_per_second.TransactionsPerSecond"
        ] = None,
        campaign_config: Optional[
            "capo_personalize.types.campaign_config.CampaignConfig"
        ] = None,
    ) -> "capo_personalize.types.update_campaign_response.UpdateCampaignResponse":
        """<p> Updates a campaign to deploy a retrained solution version with an existing campaign, change your campaign's <code>minProvisionedTPS</code>, or modify your campaign's configuration. For example, you can set <code>enableMetadataWithRecommendations</code> to true for an existing campaign.</p> <p> To update a campaign to start automatically using the latest solution version, specify the following:</p> <ul> <li> <p>For the <code>SolutionVersionArn</code> parameter, specify the Amazon Resource Name (ARN) of your solution in <code>SolutionArn/$LATEST</code> format. </p> </li> <li> <p> In the <code>campaignConfig</code>, set <code>syncWithLatestSolutionVersion</code> to <code>true</code>. </p> </li> </ul> <p>To update a campaign, the campaign status must be ACTIVE or CREATE FAILED. Check the campaign status using the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html">DescribeCampaign</a> operation.</p> <note> <p>You can still get recommendations from a campaign while an update is in progress. The campaign will use the previous solution version and campaign configuration to generate recommendations until the latest campaign update status is <code>Active</code>. </p> </note> <p>For more information about updating a campaign, including code samples, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/update-campaigns.html">Updating a campaign</a>. For more information about campaigns, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html">Creating a campaign</a>.</p>

        Args:
            campaign_arn: <p>The Amazon Resource Name (ARN) of the campaign.</p>
            solution_version_arn: <p>The Amazon Resource Name (ARN) of a new model to deploy. To specify the latest solution version of your solution, specify the ARN of your <i>solution</i> in <code>SolutionArn/$LATEST</code> format. You must use this format if you set <code>syncWithLatestSolutionVersion</code> to <code>True</code> in the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CampaignConfig.html">CampaignConfig</a>. </p> <p> To deploy a model that isn't the latest solution version of your solution, specify the ARN of the solution version. </p> <p> For more information about automatic campaign updates, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update">Enabling automatic campaign updates</a>. </p>
            min_provisioned_tps: <p>Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support. A high <code>minProvisionedTPS</code> will increase your bill. We recommend starting with 1 for <code>minProvisionedTPS</code> (the default). Track your usage using Amazon CloudWatch metrics, and increase the <code>minProvisionedTPS</code> as necessary.</p>
            campaign_config: <p>The configuration details of a campaign.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.update_campaign_request.UpdateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.update_campaign_response.UpdateCampaignResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.update_campaign

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.update_campaign.async_update_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.update_campaign_request.UpdateCampaignRequest = {
            "campaign_arn": campaign_arn
        }
        if solution_version_arn is not None:
            input_["solution_version_arn"] = solution_version_arn
        if min_provisioned_tps is not None:
            input_["min_provisioned_tps"] = min_provisioned_tps
        if campaign_config is not None:
            input_["campaign_config"] = campaign_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_dataset(
        self,
        dataset_arn: "capo_personalize.types.arn.Arn",
        schema_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.update_dataset_response.UpdateDatasetResponse":
        """<p>Update a dataset to replace its schema with a new or existing one. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/updating-dataset-schema.html">Replacing a dataset's schema</a>. </p>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset that you want to update.</p>
            schema_arn: <p>The Amazon Resource Name (ARN) of the new schema you want use.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.update_dataset_request.UpdateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.update_dataset_response.UpdateDatasetResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.update_dataset

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.update_dataset.async_update_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.update_dataset_request.UpdateDatasetRequest = {
            "dataset_arn": dataset_arn,
            "schema_arn": schema_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_metric_attribution(
        self,
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        add_metrics: Optional[
            "capo_personalize.types.metric_attributes.MetricAttributes"
        ] = None,
        remove_metrics: Optional[
            "capo_personalize.types.metric_attributes_names_list.MetricAttributesNamesList"
        ] = None,
        metrics_output_config: Optional[
            "capo_personalize.types.metric_attribution_output.MetricAttributionOutput"
        ] = None,
        metric_attribution_arn: Optional["capo_personalize.types.arn.Arn"] = None,
    ) -> "capo_personalize.types.update_metric_attribution_response.UpdateMetricAttributionResponse":
        """<p>Updates a metric attribution.</p>

        Args:
            add_metrics: <p>Add new metric attributes to the metric attribution.</p>
            remove_metrics: <p>Remove metric attributes from the metric attribution.</p>
            metrics_output_config: <p>An output config for the metric attribution.</p>
            metric_attribution_arn: <p>The Amazon Resource Name (ARN) for the metric attribution to update.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.update_metric_attribution_request.UpdateMetricAttributionRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.update_metric_attribution_response.UpdateMetricAttributionResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.update_metric_attribution

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.update_metric_attribution.async_update_metric_attribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.update_metric_attribution_request.UpdateMetricAttributionRequest = {}
        if add_metrics is not None:
            input_["add_metrics"] = add_metrics
        if remove_metrics is not None:
            input_["remove_metrics"] = remove_metrics
        if metrics_output_config is not None:
            input_["metrics_output_config"] = metrics_output_config
        if metric_attribution_arn is not None:
            input_["metric_attribution_arn"] = metric_attribution_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_recommender(
        self,
        recommender_arn: "capo_personalize.types.arn.Arn",
        recommender_config: "capo_personalize.types.recommender_config.RecommenderConfig",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
    ) -> "capo_personalize.types.update_recommender_response.UpdateRecommenderResponse":
        """<p>Updates the recommender to modify the recommender configuration. If you update the recommender to modify the columns used in training, Amazon Personalize automatically starts a full retraining of the models backing your recommender. While the update completes, you can still get recommendations from the recommender. The recommender uses the previous configuration until the update completes. To track the status of this update, use the <code>latestRecommenderUpdate</code> returned in the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeRecommender.html">DescribeRecommender</a> operation. </p>

        Args:
            recommender_arn: <p>The Amazon Resource Name (ARN) of the recommender to modify.</p>
            recommender_config: <p>The configuration details of the recommender.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.update_recommender_request.UpdateRecommenderRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.update_recommender_response.UpdateRecommenderResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.update_recommender

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.update_recommender.async_update_recommender(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.update_recommender_request.UpdateRecommenderRequest = {
            "recommender_arn": recommender_arn,
            "recommender_config": recommender_config,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_solution(
        self,
        solution_arn: "capo_personalize.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncPersonalizeClientConfig] = None,
        perform_auto_training: Optional[
            "capo_personalize.types.perform_auto_training.PerformAutoTraining"
        ] = None,
        perform_incremental_update: Optional[
            "capo_personalize.types.perform_incremental_update.PerformIncrementalUpdate"
        ] = None,
        solution_update_config: Optional[
            "capo_personalize.types.solution_update_config.SolutionUpdateConfig"
        ] = None,
    ) -> "capo_personalize.types.update_solution_response.UpdateSolutionResponse":
        """<p>Updates an Amazon Personalize solution to use a different automatic training configuration. When you update a solution, you can change whether the solution uses automatic training, and you can change the training frequency. For more information about updating a solution, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/updating-solution.html">Updating a solution</a>.</p> <p>A solution update can be in one of the following states:</p> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> <p>To get the status of a solution update, call the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html">DescribeSolution</a> API operation and find the status in the <code>latestSolutionUpdate</code>. </p>

        Args:
            solution_arn: <p>The Amazon Resource Name (ARN) of the solution to update.</p>
            perform_auto_training: <p>Whether the solution uses automatic training to create new solution versions (trained models). You can change the training frequency by specifying a <code>schedulingExpression</code> in the <code>AutoTrainingConfig</code> as part of solution configuration. </p> <p> If you turn on automatic training, the first automatic training starts within one hour after the solution update completes. If you manually create a solution version within the hour, the solution skips the first automatic training. For more information about automatic training, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html">Configuring automatic training</a>. </p> <p> After training starts, you can get the solution version's Amazon Resource Name (ARN) with the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html">ListSolutionVersions</a> API operation. To get its status, use the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html">DescribeSolutionVersion</a>. </p>
            perform_incremental_update: <p>Whether to perform incremental training updates on your model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe.</p>
            solution_update_config: <p>The new configuration details of the solution.</p>

        Raises:
            capo_personalize.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_personalize.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_personalize.types.update_solution_request.UpdateSolutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_personalize.types.update_solution_response.UpdateSolutionResponse"
        ]:
            import capo_personalize._operations.amazon_personalize.update_solution

            (
                output,
                http_response,
            ) = await capo_personalize._operations.amazon_personalize.update_solution.async_update_solution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize.types.update_solution_request.UpdateSolutionRequest = {
            "solution_arn": solution_arn
        }
        if perform_auto_training is not None:
            input_["perform_auto_training"] = perform_auto_training
        if perform_incremental_update is not None:
            input_["perform_incremental_update"] = perform_incremental_update
        if solution_update_config is not None:
            input_["solution_update_config"] = solution_update_config

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
