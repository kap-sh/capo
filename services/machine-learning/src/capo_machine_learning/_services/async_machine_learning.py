"""Generated from Smithy shape ``com.amazonaws.machinelearning#AmazonML_20141212``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_machine_learning._auth._signers
import capo_machine_learning._auth._sigv4
from capo_machine_learning._auth._identity import Credentials
from capo_machine_learning._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_machine_learning._auth._zapros_handler import AuthMiddleware
from capo_machine_learning._pagination import resolve_path as _resolve_path
from capo_machine_learning._services._aws_config import aaws_config
from capo_machine_learning._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_machine_learning.types.add_tags_input
    import capo_machine_learning.types.add_tags_output
    import capo_machine_learning.types.batch_prediction
    import capo_machine_learning.types.batch_prediction_filter_variable
    import capo_machine_learning.types.comparator_value
    import capo_machine_learning.types.compute_statistics
    import capo_machine_learning.types.create_batch_prediction_input
    import capo_machine_learning.types.create_batch_prediction_output
    import capo_machine_learning.types.create_data_source_from_rds_input
    import capo_machine_learning.types.create_data_source_from_rds_output
    import capo_machine_learning.types.create_data_source_from_redshift_input
    import capo_machine_learning.types.create_data_source_from_redshift_output
    import capo_machine_learning.types.create_data_source_from_s3_input
    import capo_machine_learning.types.create_data_source_from_s3_output
    import capo_machine_learning.types.create_evaluation_input
    import capo_machine_learning.types.create_evaluation_output
    import capo_machine_learning.types.create_ml_model_input
    import capo_machine_learning.types.create_ml_model_output
    import capo_machine_learning.types.create_realtime_endpoint_input
    import capo_machine_learning.types.create_realtime_endpoint_output
    import capo_machine_learning.types.data_source
    import capo_machine_learning.types.data_source_filter_variable
    import capo_machine_learning.types.delete_batch_prediction_input
    import capo_machine_learning.types.delete_batch_prediction_output
    import capo_machine_learning.types.delete_data_source_input
    import capo_machine_learning.types.delete_data_source_output
    import capo_machine_learning.types.delete_evaluation_input
    import capo_machine_learning.types.delete_evaluation_output
    import capo_machine_learning.types.delete_ml_model_input
    import capo_machine_learning.types.delete_ml_model_output
    import capo_machine_learning.types.delete_realtime_endpoint_input
    import capo_machine_learning.types.delete_realtime_endpoint_output
    import capo_machine_learning.types.delete_tags_input
    import capo_machine_learning.types.delete_tags_output
    import capo_machine_learning.types.describe_batch_predictions_input
    import capo_machine_learning.types.describe_batch_predictions_output
    import capo_machine_learning.types.describe_data_sources_input
    import capo_machine_learning.types.describe_data_sources_output
    import capo_machine_learning.types.describe_evaluations_input
    import capo_machine_learning.types.describe_evaluations_output
    import capo_machine_learning.types.describe_ml_models_input
    import capo_machine_learning.types.describe_ml_models_output
    import capo_machine_learning.types.describe_tags_input
    import capo_machine_learning.types.describe_tags_output
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name
    import capo_machine_learning.types.evaluation
    import capo_machine_learning.types.evaluation_filter_variable
    import capo_machine_learning.types.get_batch_prediction_input
    import capo_machine_learning.types.get_batch_prediction_output
    import capo_machine_learning.types.get_data_source_input
    import capo_machine_learning.types.get_data_source_output
    import capo_machine_learning.types.get_evaluation_input
    import capo_machine_learning.types.get_evaluation_output
    import capo_machine_learning.types.get_ml_model_input
    import capo_machine_learning.types.get_ml_model_output
    import capo_machine_learning.types.ml_model
    import capo_machine_learning.types.ml_model_filter_variable
    import capo_machine_learning.types.ml_model_type
    import capo_machine_learning.types.page_limit
    import capo_machine_learning.types.predict_input
    import capo_machine_learning.types.predict_output
    import capo_machine_learning.types.rds_data_spec
    import capo_machine_learning.types.recipe
    import capo_machine_learning.types.record
    import capo_machine_learning.types.redshift_data_spec
    import capo_machine_learning.types.role_arn
    import capo_machine_learning.types.s3_data_spec
    import capo_machine_learning.types.s3_url
    import capo_machine_learning.types.score_threshold
    import capo_machine_learning.types.sort_order
    import capo_machine_learning.types.string_type
    import capo_machine_learning.types.tag_key_list
    import capo_machine_learning.types.tag_list
    import capo_machine_learning.types.taggable_resource_type
    import capo_machine_learning.types.training_parameters
    import capo_machine_learning.types.update_batch_prediction_input
    import capo_machine_learning.types.update_batch_prediction_output
    import capo_machine_learning.types.update_data_source_input
    import capo_machine_learning.types.update_data_source_output
    import capo_machine_learning.types.update_evaluation_input
    import capo_machine_learning.types.update_evaluation_output
    import capo_machine_learning.types.update_ml_model_input
    import capo_machine_learning.types.update_ml_model_output
    import capo_machine_learning.types.verbose
    import capo_machine_learning.types.vip_url


class AsyncMachineLearningClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMachineLearningClient:
    """A client for the ``MachineLearning`` service.

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
        self._config = AsyncMachineLearningClientConfig(
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
        self, config_overrides: Optional[AsyncMachineLearningClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMachineLearningClientConfig = config_overrides or {}
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

    async def add_tags(
        self,
        tags: "capo_machine_learning.types.tag_list.TagList",
        resource_id: "capo_machine_learning.types.entity_id.EntityId",
        resource_type: "capo_machine_learning.types.taggable_resource_type.TaggableResourceType",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.add_tags_output.AddTagsOutput":
        """<p>Adds one or more tags to an object, up to a limit of 10. Each tag consists of a key and an optional value. If you add a tag using a key that is already associated with the ML object, <code>AddTags</code> updates the tag's value.</p>

        Args:
            tags: <p>The key-value pairs to use to create tags. If you specify a key without specifying a value, Amazon ML creates a tag with the specified key and a value of null.</p>
            resource_id: <p>The ID of the ML object to tag. For example, <code>exampleModelId</code>.</p>
            resource_type: <p>The type of the ML object to tag.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.invalid_tag_exception.InvalidTagException
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.tag_limit_exceeded_exception.TagLimitExceededException
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.add_tags_input.AddTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.add_tags_output.AddTagsOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.add_tags

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.add_tags.async_add_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.add_tags_input.AddTagsInput = {
            "tags": tags,
            "resource_id": resource_id,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_batch_prediction(
        self,
        batch_prediction_id: "capo_machine_learning.types.entity_id.EntityId",
        ml_model_id: "capo_machine_learning.types.entity_id.EntityId",
        batch_prediction_data_source_id: "capo_machine_learning.types.entity_id.EntityId",
        output_uri: "capo_machine_learning.types.s3_url.S3Url",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        batch_prediction_name: Optional[
            "capo_machine_learning.types.entity_name.EntityName"
        ] = None,
    ) -> "capo_machine_learning.types.create_batch_prediction_output.CreateBatchPredictionOutput":
        """<p>Generates predictions for a group of observations. The observations to process exist in one or more data files referenced by a <code>DataSource</code>. This operation creates a new <code>BatchPrediction</code>, and uses an <code>MLModel</code> and the data files referenced by the <code>DataSource</code> as information sources. </p> <p> <code>CreateBatchPrediction</code> is an asynchronous operation. In response to <code>CreateBatchPrediction</code>, Amazon Machine Learning (Amazon ML) immediately returns and sets the <code>BatchPrediction</code> status to <code>PENDING</code>. After the <code>BatchPrediction</code> completes, Amazon ML sets the status to <code>COMPLETED</code>. </p> <p>You can poll for status updates by using the <a>GetBatchPrediction</a> operation and checking the <code>Status</code> parameter of the result. After the <code>COMPLETED</code> status appears, the results are available in the location specified by the <code>OutputUri</code> parameter.</p>

        Args:
            batch_prediction_id: <p>A user-supplied ID that uniquely identifies the <code>BatchPrediction</code>.</p>
            batch_prediction_name: <p>A user-supplied name or description of the <code>BatchPrediction</code>. <code>BatchPredictionName</code> can only use the UTF-8 character set.</p>
            ml_model_id: <p>The ID of the <code>MLModel</code> that will generate predictions for the group of observations. </p>
            batch_prediction_data_source_id: <p>The ID of the <code>DataSource</code> that points to the group of observations to predict.</p>
            output_uri: <p>The location of an Amazon Simple Storage Service (Amazon S3) bucket or directory to store the batch prediction results. The following substrings are not allowed in the <code>s3 key</code> portion of the <code>outputURI</code> field: ':', '//', '/./', '/../'.</p> <p>Amazon ML needs permissions to store and retrieve the logs on your behalf. For information about how to set permissions, see the <a href="https://docs.aws.amazon.com/machine-learning/latest/dg">Amazon Machine Learning Developer Guide</a>.</p>

        Raises:
            capo_machine_learning.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A second request to use or change an object was not allowed. This can result from retrying a request using a parameter that was not present in the original request.</p>
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.create_batch_prediction_input.CreateBatchPredictionInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.create_batch_prediction_output.CreateBatchPredictionOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.create_batch_prediction

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.create_batch_prediction.async_create_batch_prediction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.create_batch_prediction_input.CreateBatchPredictionInput = {
            "batch_prediction_id": batch_prediction_id,
            "ml_model_id": ml_model_id,
            "batch_prediction_data_source_id": batch_prediction_data_source_id,
            "output_uri": output_uri,
        }
        if batch_prediction_name is not None:
            input_["batch_prediction_name"] = batch_prediction_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_source_from_rds(
        self,
        data_source_id: "capo_machine_learning.types.entity_id.EntityId",
        rds_data: "capo_machine_learning.types.rds_data_spec.RDSDataSpec",
        role_arn: "capo_machine_learning.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        data_source_name: Optional[
            "capo_machine_learning.types.entity_name.EntityName"
        ] = None,
        compute_statistics: Optional[
            "capo_machine_learning.types.compute_statistics.ComputeStatistics"
        ] = None,
    ) -> "capo_machine_learning.types.create_data_source_from_rds_output.CreateDataSourceFromRDSOutput":
        r"""<p>Creates a <code>DataSource</code> object from an <a href="http://aws.amazon.com/rds/"> Amazon Relational Database Service</a> (Amazon RDS). A <code>DataSource</code> references data that can be used to perform <code>CreateMLModel</code>, <code>CreateEvaluation</code>, or <code>CreateBatchPrediction</code> operations.</p> <p> <code>CreateDataSourceFromRDS</code> is an asynchronous operation. In response to <code>CreateDataSourceFromRDS</code>, Amazon Machine Learning (Amazon ML) immediately returns and sets the <code>DataSource</code> status to <code>PENDING</code>. After the <code>DataSource</code> is created and ready for use, Amazon ML sets the <code>Status</code> parameter to <code>COMPLETED</code>. <code>DataSource</code> in the <code>COMPLETED</code> or <code>PENDING</code> state can be used only to perform <code>>CreateMLModel</code>>, <code>CreateEvaluation</code>, or <code>CreateBatchPrediction</code> operations. </p> <p> If Amazon ML cannot accept the input source, it sets the <code>Status</code> parameter to <code>FAILED</code> and includes an error message in the <code>Message</code> attribute of the <code>GetDataSource</code> operation response. </p>

        Args:
            data_source_id: <p>A user-supplied ID that uniquely identifies the <code>DataSource</code>. Typically, an Amazon Resource Number (ARN) becomes the ID for a <code>DataSource</code>.</p>
            data_source_name: <p>A user-supplied name or description of the <code>DataSource</code>.</p>
            rds_data: <p>The data specification of an Amazon RDS <code>DataSource</code>:</p> <ul> <li> <p>DatabaseInformation -</p> <ul> <li> <p> <code>DatabaseName</code> - The name of the Amazon RDS database.</p> </li> <li> <p> <code>InstanceIdentifier </code> - A unique identifier for the Amazon RDS database instance.</p> </li> </ul> </li> <li> <p>DatabaseCredentials - AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon RDS database.</p> </li> <li> <p>ResourceRole - A role (DataPipelineDefaultResourceRole) assumed by an EC2 instance to carry out the copy task from Amazon RDS to Amazon Simple Storage Service (Amazon S3). For more information, see <a href="https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html">Role templates</a> for data pipelines.</p> </li> <li> <p>ServiceRole - A role (DataPipelineDefaultRole) assumed by the AWS Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see <a href="https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html">Role templates</a> for data pipelines.</p> </li> <li> <p>SecurityInfo - The security information to use to access an RDS DB instance. You need to set up appropriate ingress rules for the security entity IDs provided to allow access to the Amazon RDS instance. Specify a [<code>SubnetId</code>, <code>SecurityGroupIds</code>] pair for a VPC-based RDS DB instance.</p> </li> <li> <p>SelectSqlQuery - A query that is used to retrieve the observation data for the <code>Datasource</code>.</p> </li> <li> <p>S3StagingLocation - The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using <code>SelectSqlQuery</code> is stored in this location.</p> </li> <li> <p>DataSchemaUri - The Amazon S3 location of the <code>DataSchema</code>.</p> </li> <li> <p>DataSchema - A JSON string representing the schema. This is not required if <code>DataSchemaUri</code> is specified. </p> </li> <li> <p>DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the <code>Datasource</code>. </p> <p> Sample - <code> "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"</code> </p> </li> </ul>
            role_arn: <p>The role that Amazon ML assumes on behalf of the user to create and activate a data pipeline in the user's account and copy data using the <code>SelectSqlQuery</code> query from Amazon RDS to Amazon S3.</p> <p></p>
            compute_statistics: <p>The compute statistics for a <code>DataSource</code>. The statistics are generated from the observation data referenced by a <code>DataSource</code>. Amazon ML uses the statistics internally during <code>MLModel</code> training. This parameter must be set to <code>true</code> if the <code></code>DataSource<code></code> needs to be used for <code>MLModel</code> training. </p>

        Raises:
            capo_machine_learning.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A second request to use or change an object was not allowed. This can result from retrying a request using a parameter that was not present in the original request.</p>
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.create_data_source_from_rds_input.CreateDataSourceFromRDSInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.create_data_source_from_rds_output.CreateDataSourceFromRDSOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.create_data_source_from_rds

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.create_data_source_from_rds.async_create_data_source_from_rds(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.create_data_source_from_rds_input.CreateDataSourceFromRDSInput = {
            "data_source_id": data_source_id,
            "rds_data": rds_data,
            "role_arn": role_arn,
        }
        if data_source_name is not None:
            input_["data_source_name"] = data_source_name
        if compute_statistics is not None:
            input_["compute_statistics"] = compute_statistics

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_source_from_redshift(
        self,
        data_source_id: "capo_machine_learning.types.entity_id.EntityId",
        data_spec: "capo_machine_learning.types.redshift_data_spec.RedshiftDataSpec",
        role_arn: "capo_machine_learning.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        data_source_name: Optional[
            "capo_machine_learning.types.entity_name.EntityName"
        ] = None,
        compute_statistics: Optional[
            "capo_machine_learning.types.compute_statistics.ComputeStatistics"
        ] = None,
    ) -> "capo_machine_learning.types.create_data_source_from_redshift_output.CreateDataSourceFromRedshiftOutput":
        r"""<p>Creates a <code>DataSource</code> from a database hosted on an Amazon Redshift cluster. A <code>DataSource</code> references data that can be used to perform either <code>CreateMLModel</code>, <code>CreateEvaluation</code>, or <code>CreateBatchPrediction</code> operations.</p> <p> <code>CreateDataSourceFromRedshift</code> is an asynchronous operation. In response to <code>CreateDataSourceFromRedshift</code>, Amazon Machine Learning (Amazon ML) immediately returns and sets the <code>DataSource</code> status to <code>PENDING</code>. After the <code>DataSource</code> is created and ready for use, Amazon ML sets the <code>Status</code> parameter to <code>COMPLETED</code>. <code>DataSource</code> in <code>COMPLETED</code> or <code>PENDING</code> states can be used to perform only <code>CreateMLModel</code>, <code>CreateEvaluation</code>, or <code>CreateBatchPrediction</code> operations. </p> <p> If Amazon ML can't accept the input source, it sets the <code>Status</code> parameter to <code>FAILED</code> and includes an error message in the <code>Message</code> attribute of the <code>GetDataSource</code> operation response. </p> <p>The observations should be contained in the database hosted on an Amazon Redshift cluster and should be specified by a <code>SelectSqlQuery</code> query. Amazon ML executes an <code>Unload</code> command in Amazon Redshift to transfer the result set of the <code>SelectSqlQuery</code> query to <code>S3StagingLocation</code>.</p> <p>After the <code>DataSource</code> has been created, it's ready for use in evaluations and batch predictions. If you plan to use the <code>DataSource</code> to train an <code>MLModel</code>, the <code>DataSource</code> also requires a recipe. A recipe describes how each input variable will be used in training an <code>MLModel</code>. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.</p> <p>You can't change an existing datasource, but you can copy and modify the settings from an existing Amazon Redshift datasource to create a new datasource. To do so, call <code>GetDataSource</code> for an existing datasource and copy the values to a <code>CreateDataSource</code> call. Change the settings that you want to change and make sure that all required fields have the appropriate values.</p>

        Args:
            data_source_id: <p>A user-supplied ID that uniquely identifies the <code>DataSource</code>.</p>
            data_source_name: <p>A user-supplied name or description of the <code>DataSource</code>. </p>
            data_spec: <p>The data specification of an Amazon Redshift <code>DataSource</code>:</p> <ul> <li> <p>DatabaseInformation -</p> <ul> <li> <p> <code>DatabaseName</code> - The name of the Amazon Redshift database.</p> </li> <li> <p> <code> ClusterIdentifier</code> - The unique ID for the Amazon Redshift cluster.</p> </li> </ul> </li> <li> <p>DatabaseCredentials - The AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon Redshift database.</p> </li> <li> <p>SelectSqlQuery - The query that is used to retrieve the observation data for the <code>Datasource</code>.</p> </li> <li> <p>S3StagingLocation - The Amazon Simple Storage Service (Amazon S3) location for staging Amazon Redshift data. The data retrieved from Amazon Redshift using the <code>SelectSqlQuery</code> query is stored in this location.</p> </li> <li> <p>DataSchemaUri - The Amazon S3 location of the <code>DataSchema</code>.</p> </li> <li> <p>DataSchema - A JSON string representing the schema. This is not required if <code>DataSchemaUri</code> is specified. </p> </li> <li> <p>DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the <code>DataSource</code>.</p> <p> Sample - <code> "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"</code> </p> </li> </ul>
            role_arn: <p>A fully specified role Amazon Resource Name (ARN). Amazon ML assumes the role on behalf of the user to create the following:</p> <ul> <li> <p>A security group to allow Amazon ML to execute the <code>SelectSqlQuery</code> query on an Amazon Redshift cluster</p> </li> <li> <p>An Amazon S3 bucket policy to grant Amazon ML read/write permissions on the <code>S3StagingLocation</code> </p> </li> </ul>
            compute_statistics: <p>The compute statistics for a <code>DataSource</code>. The statistics are generated from the observation data referenced by a <code>DataSource</code>. Amazon ML uses the statistics internally during <code>MLModel</code> training. This parameter must be set to <code>true</code> if the <code>DataSource</code> needs to be used for <code>MLModel</code> training.</p>

        Raises:
            capo_machine_learning.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A second request to use or change an object was not allowed. This can result from retrying a request using a parameter that was not present in the original request.</p>
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.create_data_source_from_redshift_input.CreateDataSourceFromRedshiftInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.create_data_source_from_redshift_output.CreateDataSourceFromRedshiftOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.create_data_source_from_redshift

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.create_data_source_from_redshift.async_create_data_source_from_redshift(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.create_data_source_from_redshift_input.CreateDataSourceFromRedshiftInput = {
            "data_source_id": data_source_id,
            "data_spec": data_spec,
            "role_arn": role_arn,
        }
        if data_source_name is not None:
            input_["data_source_name"] = data_source_name
        if compute_statistics is not None:
            input_["compute_statistics"] = compute_statistics

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_source_from_s3(
        self,
        data_source_id: "capo_machine_learning.types.entity_id.EntityId",
        data_spec: "capo_machine_learning.types.s3_data_spec.S3DataSpec",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        data_source_name: Optional[
            "capo_machine_learning.types.entity_name.EntityName"
        ] = None,
        compute_statistics: Optional[
            "capo_machine_learning.types.compute_statistics.ComputeStatistics"
        ] = None,
    ) -> "capo_machine_learning.types.create_data_source_from_s3_output.CreateDataSourceFromS3Output":
        r"""<p>Creates a <code>DataSource</code> object. A <code>DataSource</code> references data that can be used to perform <code>CreateMLModel</code>, <code>CreateEvaluation</code>, or <code>CreateBatchPrediction</code> operations.</p> <p> <code>CreateDataSourceFromS3</code> is an asynchronous operation. In response to <code>CreateDataSourceFromS3</code>, Amazon Machine Learning (Amazon ML) immediately returns and sets the <code>DataSource</code> status to <code>PENDING</code>. After the <code>DataSource</code> has been created and is ready for use, Amazon ML sets the <code>Status</code> parameter to <code>COMPLETED</code>. <code>DataSource</code> in the <code>COMPLETED</code> or <code>PENDING</code> state can be used to perform only <code>CreateMLModel</code>, <code>CreateEvaluation</code> or <code>CreateBatchPrediction</code> operations. </p> <p> If Amazon ML can't accept the input source, it sets the <code>Status</code> parameter to <code>FAILED</code> and includes an error message in the <code>Message</code> attribute of the <code>GetDataSource</code> operation response. </p> <p>The observation data used in a <code>DataSource</code> should be ready to use; that is, it should have a consistent structure, and missing data values should be kept to a minimum. The observation data must reside in one or more .csv files in an Amazon Simple Storage Service (Amazon S3) location, along with a schema that describes the data items by name and type. The same schema must be used for all of the data files referenced by the <code>DataSource</code>. </p> <p>After the <code>DataSource</code> has been created, it's ready to use in evaluations and batch predictions. If you plan to use the <code>DataSource</code> to train an <code>MLModel</code>, the <code>DataSource</code> also needs a recipe. A recipe describes how each input variable will be used in training an <code>MLModel</code>. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.</p>

        Args:
            data_source_id: <p>A user-supplied identifier that uniquely identifies the <code>DataSource</code>. </p>
            data_source_name: <p>A user-supplied name or description of the <code>DataSource</code>. </p>
            data_spec: <p>The data specification of a <code>DataSource</code>:</p> <ul> <li> <p>DataLocationS3 - The Amazon S3 location of the observation data.</p> </li> <li> <p>DataSchemaLocationS3 - The Amazon S3 location of the <code>DataSchema</code>.</p> </li> <li> <p>DataSchema - A JSON string representing the schema. This is not required if <code>DataSchemaUri</code> is specified. </p> </li> <li> <p>DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the <code>Datasource</code>. </p> <p> Sample - <code> "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"</code> </p> </li> </ul>
            compute_statistics: <p>The compute statistics for a <code>DataSource</code>. The statistics are generated from the observation data referenced by a <code>DataSource</code>. Amazon ML uses the statistics internally during <code>MLModel</code> training. This parameter must be set to <code>true</code> if the <code></code>DataSource<code></code> needs to be used for <code>MLModel</code> training.</p>

        Raises:
            capo_machine_learning.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A second request to use or change an object was not allowed. This can result from retrying a request using a parameter that was not present in the original request.</p>
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.create_data_source_from_s3_input.CreateDataSourceFromS3Input]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.create_data_source_from_s3_output.CreateDataSourceFromS3Output"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.create_data_source_from_s3

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.create_data_source_from_s3.async_create_data_source_from_s3(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.create_data_source_from_s3_input.CreateDataSourceFromS3Input = {
            "data_source_id": data_source_id,
            "data_spec": data_spec,
        }
        if data_source_name is not None:
            input_["data_source_name"] = data_source_name
        if compute_statistics is not None:
            input_["compute_statistics"] = compute_statistics

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_evaluation(
        self,
        evaluation_id: "capo_machine_learning.types.entity_id.EntityId",
        ml_model_id: "capo_machine_learning.types.entity_id.EntityId",
        evaluation_data_source_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        evaluation_name: Optional[
            "capo_machine_learning.types.entity_name.EntityName"
        ] = None,
    ) -> "capo_machine_learning.types.create_evaluation_output.CreateEvaluationOutput":
        """<p>Creates a new <code>Evaluation</code> of an <code>MLModel</code>. An <code>MLModel</code> is evaluated on a set of observations associated to a <code>DataSource</code>. Like a <code>DataSource</code> for an <code>MLModel</code>, the <code>DataSource</code> for an <code>Evaluation</code> contains values for the <code>Target Variable</code>. The <code>Evaluation</code> compares the predicted result for each observation to the actual outcome and provides a summary so that you know how effective the <code>MLModel</code> functions on the test data. Evaluation generates a relevant performance metric, such as BinaryAUC, RegressionRMSE or MulticlassAvgFScore based on the corresponding <code>MLModelType</code>: <code>BINARY</code>, <code>REGRESSION</code> or <code>MULTICLASS</code>. </p> <p> <code>CreateEvaluation</code> is an asynchronous operation. In response to <code>CreateEvaluation</code>, Amazon Machine Learning (Amazon ML) immediately returns and sets the evaluation status to <code>PENDING</code>. After the <code>Evaluation</code> is created and ready for use, Amazon ML sets the status to <code>COMPLETED</code>. </p> <p>You can use the <code>GetEvaluation</code> operation to check progress of the evaluation during the creation operation.</p>

        Args:
            evaluation_id: <p>A user-supplied ID that uniquely identifies the <code>Evaluation</code>.</p>
            evaluation_name: <p>A user-supplied name or description of the <code>Evaluation</code>.</p>
            ml_model_id: <p>The ID of the <code>MLModel</code> to evaluate.</p> <p>The schema used in creating the <code>MLModel</code> must match the schema of the <code>DataSource</code> used in the <code>Evaluation</code>.</p>
            evaluation_data_source_id: <p>The ID of the <code>DataSource</code> for the evaluation. The schema of the <code>DataSource</code> must match the schema used to create the <code>MLModel</code>.</p>

        Raises:
            capo_machine_learning.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A second request to use or change an object was not allowed. This can result from retrying a request using a parameter that was not present in the original request.</p>
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.create_evaluation_input.CreateEvaluationInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.create_evaluation_output.CreateEvaluationOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.create_evaluation

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.create_evaluation.async_create_evaluation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.create_evaluation_input.CreateEvaluationInput = {
            "evaluation_id": evaluation_id,
            "ml_model_id": ml_model_id,
            "evaluation_data_source_id": evaluation_data_source_id,
        }
        if evaluation_name is not None:
            input_["evaluation_name"] = evaluation_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ml_model(
        self,
        ml_model_id: "capo_machine_learning.types.entity_id.EntityId",
        ml_model_type: "capo_machine_learning.types.ml_model_type.MLModelType",
        training_data_source_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        ml_model_name: Optional[
            "capo_machine_learning.types.entity_name.EntityName"
        ] = None,
        parameters: Optional[
            "capo_machine_learning.types.training_parameters.TrainingParameters"
        ] = None,
        recipe: Optional["capo_machine_learning.types.recipe.Recipe"] = None,
        recipe_uri: Optional["capo_machine_learning.types.s3_url.S3Url"] = None,
    ) -> "capo_machine_learning.types.create_ml_model_output.CreateMLModelOutput":
        """<p>Creates a new <code>MLModel</code> using the <code>DataSource</code> and the recipe as information sources. </p> <p>An <code>MLModel</code> is nearly immutable. Users can update only the <code>MLModelName</code> and the <code>ScoreThreshold</code> in an <code>MLModel</code> without creating a new <code>MLModel</code>. </p> <p> <code>CreateMLModel</code> is an asynchronous operation. In response to <code>CreateMLModel</code>, Amazon Machine Learning (Amazon ML) immediately returns and sets the <code>MLModel</code> status to <code>PENDING</code>. After the <code>MLModel</code> has been created and ready is for use, Amazon ML sets the status to <code>COMPLETED</code>. </p> <p>You can use the <code>GetMLModel</code> operation to check the progress of the <code>MLModel</code> during the creation operation.</p> <p> <code>CreateMLModel</code> requires a <code>DataSource</code> with computed statistics, which can be created by setting <code>ComputeStatistics</code> to <code>true</code> in <code>CreateDataSourceFromRDS</code>, <code>CreateDataSourceFromS3</code>, or <code>CreateDataSourceFromRedshift</code> operations. </p>

        Args:
            ml_model_id: <p>A user-supplied ID that uniquely identifies the <code>MLModel</code>.</p>
            ml_model_name: <p>A user-supplied name or description of the <code>MLModel</code>.</p>
            ml_model_type: <p>The category of supervised learning that this <code>MLModel</code> will address. Choose from the following types:</p> <ul> <li> <p>Choose <code>REGRESSION</code> if the <code>MLModel</code> will be used to predict a numeric value.</p> </li> <li> <p>Choose <code>BINARY</code> if the <code>MLModel</code> result has two possible values.</p> </li> <li> <p>Choose <code>MULTICLASS</code> if the <code>MLModel</code> result has a limited number of values.</p> </li> </ul> <p> For more information, see the <a href="https://docs.aws.amazon.com/machine-learning/latest/dg">Amazon Machine Learning Developer Guide</a>.</p>
            parameters: <p>A list of the training parameters in the <code>MLModel</code>. The list is implemented as a map of key-value pairs.</p> <p>The following is the current set of training parameters:</p> <ul> <li> <p> <code>sgd.maxMLModelSizeInBytes</code> - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance.</p> <p> The value is an integer that ranges from <code>100000</code> to <code>2147483648</code>. The default value is <code>33554432</code>.</p> </li> <li> <p> <code>sgd.maxPasses</code> - The number of times that the training process traverses the observations to build the <code>MLModel</code>. The value is an integer that ranges from <code>1</code> to <code>10000</code>. The default value is <code>10</code>.</p> </li> <li> <p> <code>sgd.shuffleType</code> - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are <code>auto</code> and <code>none</code>. The default value is <code>none</code>. We strongly recommend that you shuffle your data.</p> </li> <li> <p> <code>sgd.l1RegularizationAmount</code> - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as <code>1.0E-08</code>.</p> <p>The value is a double that ranges from <code>0</code> to <code>MAX_DOUBLE</code>. The default is to not use L1 normalization. This parameter can't be used when <code>L2</code> is specified. Use this parameter sparingly.</p> </li> <li> <p> <code>sgd.l2RegularizationAmount</code> - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as <code>1.0E-08</code>.</p> <p>The value is a double that ranges from <code>0</code> to <code>MAX_DOUBLE</code>. The default is to not use L2 normalization. This parameter can't be used when <code>L1</code> is specified. Use this parameter sparingly.</p> </li> </ul>
            training_data_source_id: <p>The <code>DataSource</code> that points to the training data.</p>
            recipe: <p>The data recipe for creating the <code>MLModel</code>. You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.</p>
            recipe_uri: <p>The Amazon Simple Storage Service (Amazon S3) location and file name that contains the <code>MLModel</code> recipe. You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.</p>

        Raises:
            capo_machine_learning.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A second request to use or change an object was not allowed. This can result from retrying a request using a parameter that was not present in the original request.</p>
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.create_ml_model_input.CreateMLModelInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.create_ml_model_output.CreateMLModelOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.create_ml_model

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.create_ml_model.async_create_ml_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.create_ml_model_input.CreateMLModelInput = {
            "ml_model_id": ml_model_id,
            "ml_model_type": ml_model_type,
            "training_data_source_id": training_data_source_id,
        }
        if ml_model_name is not None:
            input_["ml_model_name"] = ml_model_name
        if parameters is not None:
            input_["parameters"] = parameters
        if recipe is not None:
            input_["recipe"] = recipe
        if recipe_uri is not None:
            input_["recipe_uri"] = recipe_uri

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_realtime_endpoint(
        self,
        ml_model_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.create_realtime_endpoint_output.CreateRealtimeEndpointOutput":
        """<p>Creates a real-time endpoint for the <code>MLModel</code>. The endpoint contains the URI of the <code>MLModel</code>; that is, the location to send real-time prediction requests for the specified <code>MLModel</code>.</p>

        Args:
            ml_model_id: <p>The ID assigned to the <code>MLModel</code> during creation.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.create_realtime_endpoint_input.CreateRealtimeEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.create_realtime_endpoint_output.CreateRealtimeEndpointOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.create_realtime_endpoint

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.create_realtime_endpoint.async_create_realtime_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.create_realtime_endpoint_input.CreateRealtimeEndpointInput = {
            "ml_model_id": ml_model_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_batch_prediction(
        self,
        batch_prediction_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.delete_batch_prediction_output.DeleteBatchPredictionOutput":
        """<p>Assigns the DELETED status to a <code>BatchPrediction</code>, rendering it unusable.</p> <p>After using the <code>DeleteBatchPrediction</code> operation, you can use the <a>GetBatchPrediction</a> operation to verify that the status of the <code>BatchPrediction</code> changed to DELETED.</p> <p> <b>Caution:</b> The result of the <code>DeleteBatchPrediction</code> operation is irreversible.</p>

        Args:
            batch_prediction_id: <p>A user-supplied ID that uniquely identifies the <code>BatchPrediction</code>.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.delete_batch_prediction_input.DeleteBatchPredictionInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.delete_batch_prediction_output.DeleteBatchPredictionOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.delete_batch_prediction

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.delete_batch_prediction.async_delete_batch_prediction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.delete_batch_prediction_input.DeleteBatchPredictionInput = {
            "batch_prediction_id": batch_prediction_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_source(
        self,
        data_source_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.delete_data_source_output.DeleteDataSourceOutput":
        """<p>Assigns the DELETED status to a <code>DataSource</code>, rendering it unusable.</p> <p>After using the <code>DeleteDataSource</code> operation, you can use the <a>GetDataSource</a> operation to verify that the status of the <code>DataSource</code> changed to DELETED.</p> <p> <b>Caution:</b> The results of the <code>DeleteDataSource</code> operation are irreversible.</p>

        Args:
            data_source_id: <p>A user-supplied ID that uniquely identifies the <code>DataSource</code>.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.delete_data_source_input.DeleteDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.delete_data_source_output.DeleteDataSourceOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.delete_data_source

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.delete_data_source.async_delete_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.delete_data_source_input.DeleteDataSourceInput = {
            "data_source_id": data_source_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_evaluation(
        self,
        evaluation_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.delete_evaluation_output.DeleteEvaluationOutput":
        """<p>Assigns the <code>DELETED</code> status to an <code>Evaluation</code>, rendering it unusable.</p> <p>After invoking the <code>DeleteEvaluation</code> operation, you can use the <code>GetEvaluation</code> operation to verify that the status of the <code>Evaluation</code> changed to <code>DELETED</code>.</p> <p> <b>Caution:</b> The results of the <code>DeleteEvaluation</code> operation are irreversible.</p>

        Args:
            evaluation_id: <p>A user-supplied ID that uniquely identifies the <code>Evaluation</code> to delete.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.delete_evaluation_input.DeleteEvaluationInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.delete_evaluation_output.DeleteEvaluationOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.delete_evaluation

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.delete_evaluation.async_delete_evaluation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.delete_evaluation_input.DeleteEvaluationInput = {
            "evaluation_id": evaluation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ml_model(
        self,
        ml_model_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.delete_ml_model_output.DeleteMLModelOutput":
        """<p>Assigns the <code>DELETED</code> status to an <code>MLModel</code>, rendering it unusable.</p> <p>After using the <code>DeleteMLModel</code> operation, you can use the <code>GetMLModel</code> operation to verify that the status of the <code>MLModel</code> changed to DELETED.</p> <p> <b>Caution:</b> The result of the <code>DeleteMLModel</code> operation is irreversible.</p>

        Args:
            ml_model_id: <p>A user-supplied ID that uniquely identifies the <code>MLModel</code>.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.delete_ml_model_input.DeleteMLModelInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.delete_ml_model_output.DeleteMLModelOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.delete_ml_model

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.delete_ml_model.async_delete_ml_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.delete_ml_model_input.DeleteMLModelInput = {
            "ml_model_id": ml_model_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_realtime_endpoint(
        self,
        ml_model_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.delete_realtime_endpoint_output.DeleteRealtimeEndpointOutput":
        """<p>Deletes a real time endpoint of an <code>MLModel</code>.</p>

        Args:
            ml_model_id: <p>The ID assigned to the <code>MLModel</code> during creation.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.delete_realtime_endpoint_input.DeleteRealtimeEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.delete_realtime_endpoint_output.DeleteRealtimeEndpointOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.delete_realtime_endpoint

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.delete_realtime_endpoint.async_delete_realtime_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.delete_realtime_endpoint_input.DeleteRealtimeEndpointInput = {
            "ml_model_id": ml_model_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_tags(
        self,
        tag_keys: "capo_machine_learning.types.tag_key_list.TagKeyList",
        resource_id: "capo_machine_learning.types.entity_id.EntityId",
        resource_type: "capo_machine_learning.types.taggable_resource_type.TaggableResourceType",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.delete_tags_output.DeleteTagsOutput":
        """<p>Deletes the specified tags associated with an ML object. After this operation is complete, you can't recover deleted tags.</p> <p>If you specify a tag that doesn't exist, Amazon ML ignores it.</p>

        Args:
            tag_keys: <p>One or more tags to delete.</p>
            resource_id: <p>The ID of the tagged ML object. For example, <code>exampleModelId</code>.</p>
            resource_type: <p>The type of the tagged ML object.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.invalid_tag_exception.InvalidTagException
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.delete_tags_input.DeleteTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.delete_tags_output.DeleteTagsOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.delete_tags

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.delete_tags.async_delete_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.delete_tags_input.DeleteTagsInput = {
            "tag_keys": tag_keys,
            "resource_id": resource_id,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_batch_predictions(
        self,
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        filter_variable: Optional[
            "capo_machine_learning.types.batch_prediction_filter_variable.BatchPredictionFilterVariable"
        ] = None,
        eq: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        gt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        lt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ge: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        le: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ne: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        prefix: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        sort_order: Optional["capo_machine_learning.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_machine_learning.types.string_type.StringType"
        ] = None,
        limit: Optional["capo_machine_learning.types.page_limit.PageLimit"] = None,
    ) -> "capo_machine_learning.types.describe_batch_predictions_output.DescribeBatchPredictionsOutput":
        """<p>Returns a list of <code>BatchPrediction</code> operations that match the search criteria in the request.</p>

        Args:
            filter_variable: <p>Use one of the following variables to filter a list of <code>BatchPrediction</code>:</p> <ul> <li> <p> <code>CreatedAt</code> - Sets the search criteria to the <code>BatchPrediction</code> creation date.</p> </li> <li> <p> <code>Status</code> - Sets the search criteria to the <code>BatchPrediction</code> status.</p> </li> <li> <p> <code>Name</code> - Sets the search criteria to the contents of the <code>BatchPrediction</code> <b> </b> <code>Name</code>.</p> </li> <li> <p> <code>IAMUser</code> - Sets the search criteria to the user account that invoked the <code>BatchPrediction</code> creation.</p> </li> <li> <p> <code>MLModelId</code> - Sets the search criteria to the <code>MLModel</code> used in the <code>BatchPrediction</code>.</p> </li> <li> <p> <code>DataSourceId</code> - Sets the search criteria to the <code>DataSource</code> used in the <code>BatchPrediction</code>.</p> </li> <li> <p> <code>DataURI</code> - Sets the search criteria to the data file(s) used in the <code>BatchPrediction</code>. The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.</p> </li> </ul>
            eq: <p>The equal to operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that exactly match the value specified with <code>EQ</code>.</p>
            gt: <p>The greater than operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that are greater than the value specified with <code>GT</code>.</p>
            lt: <p>The less than operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that are less than the value specified with <code>LT</code>.</p>
            ge: <p>The greater than or equal to operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that are greater than or equal to the value specified with <code>GE</code>. </p>
            le: <p>The less than or equal to operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that are less than or equal to the value specified with <code>LE</code>.</p>
            ne: <p>The not equal to operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values not equal to the value specified with <code>NE</code>.</p>
            prefix: <p>A string that is found at the beginning of a variable, such as <code>Name</code> or <code>Id</code>.</p> <p>For example, a <code>Batch Prediction</code> operation could have the <code>Name</code> <code>2014-09-09-HolidayGiftMailer</code>. To search for this <code>BatchPrediction</code>, select <code>Name</code> for the <code>FilterVariable</code> and any of the following strings for the <code>Prefix</code>: </p> <ul> <li> <p>2014-09</p> </li> <li> <p>2014-09-09</p> </li> <li> <p>2014-09-09-Holiday</p> </li> </ul>
            sort_order: <p>A two-value parameter that determines the sequence of the resulting list of <code>MLModel</code>s.</p> <ul> <li> <p> <code>asc</code> - Arranges the list in ascending order (A-Z, 0-9).</p> </li> <li> <p> <code>dsc</code> - Arranges the list in descending order (Z-A, 9-0).</p> </li> </ul> <p>Results are sorted by <code>FilterVariable</code>.</p>
            next_token: <p>An ID of the page in the paginated results.</p>
            limit: <p>The number of pages of information to include in the result. The range of acceptable values is <code>1</code> through <code>100</code>. The default value is <code>100</code>.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.describe_batch_predictions_input.DescribeBatchPredictionsInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.describe_batch_predictions_output.DescribeBatchPredictionsOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.describe_batch_predictions

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.describe_batch_predictions.async_describe_batch_predictions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.describe_batch_predictions_input.DescribeBatchPredictionsInput = {}
        if filter_variable is not None:
            input_["filter_variable"] = filter_variable
        if eq is not None:
            input_["eq"] = eq
        if gt is not None:
            input_["gt"] = gt
        if lt is not None:
            input_["lt"] = lt
        if ge is not None:
            input_["ge"] = ge
        if le is not None:
            input_["le"] = le
        if ne is not None:
            input_["ne"] = ne
        if prefix is not None:
            input_["prefix"] = prefix
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_batch_predictions(
        self,
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        filter_variable: Optional[
            "capo_machine_learning.types.batch_prediction_filter_variable.BatchPredictionFilterVariable"
        ] = None,
        eq: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        gt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        lt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ge: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        le: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ne: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        prefix: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        sort_order: Optional["capo_machine_learning.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_machine_learning.types.string_type.StringType"
        ] = None,
        limit: Optional["capo_machine_learning.types.page_limit.PageLimit"] = None,
    ) -> "AsyncIterator[capo_machine_learning.types.batch_prediction.BatchPrediction]":
        _token = next_token
        while True:
            _response = await self.describe_batch_predictions(
                config_overrides=config_overrides,
                filter_variable=filter_variable,
                eq=eq,
                gt=gt,
                lt=lt,
                ge=ge,
                le=le,
                ne=ne,
                prefix=prefix,
                sort_order=sort_order,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_data_sources(
        self,
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        filter_variable: Optional[
            "capo_machine_learning.types.data_source_filter_variable.DataSourceFilterVariable"
        ] = None,
        eq: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        gt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        lt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ge: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        le: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ne: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        prefix: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        sort_order: Optional["capo_machine_learning.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_machine_learning.types.string_type.StringType"
        ] = None,
        limit: Optional["capo_machine_learning.types.page_limit.PageLimit"] = None,
    ) -> "capo_machine_learning.types.describe_data_sources_output.DescribeDataSourcesOutput":
        """<p>Returns a list of <code>DataSource</code> that match the search criteria in the request.</p>

        Args:
            filter_variable: <p>Use one of the following variables to filter a list of <code>DataSource</code>:</p> <ul> <li> <p> <code>CreatedAt</code> - Sets the search criteria to <code>DataSource</code> creation dates.</p> </li> <li> <p> <code>Status</code> - Sets the search criteria to <code>DataSource</code> statuses.</p> </li> <li> <p> <code>Name</code> - Sets the search criteria to the contents of <code>DataSource</code> <code>Name</code>.</p> </li> <li> <p> <code>DataUri</code> - Sets the search criteria to the URI of data files used to create the <code>DataSource</code>. The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.</p> </li> <li> <p> <code>IAMUser</code> - Sets the search criteria to the user account that invoked the <code>DataSource</code> creation.</p> </li> </ul>
            eq: <p>The equal to operator. The <code>DataSource</code> results will have <code>FilterVariable</code> values that exactly match the value specified with <code>EQ</code>.</p>
            gt: <p>The greater than operator. The <code>DataSource</code> results will have <code>FilterVariable</code> values that are greater than the value specified with <code>GT</code>.</p>
            lt: <p>The less than operator. The <code>DataSource</code> results will have <code>FilterVariable</code> values that are less than the value specified with <code>LT</code>.</p>
            ge: <p>The greater than or equal to operator. The <code>DataSource</code> results will have <code>FilterVariable</code> values that are greater than or equal to the value specified with <code>GE</code>. </p>
            le: <p>The less than or equal to operator. The <code>DataSource</code> results will have <code>FilterVariable</code> values that are less than or equal to the value specified with <code>LE</code>.</p>
            ne: <p>The not equal to operator. The <code>DataSource</code> results will have <code>FilterVariable</code> values not equal to the value specified with <code>NE</code>.</p>
            prefix: <p>A string that is found at the beginning of a variable, such as <code>Name</code> or <code>Id</code>.</p> <p>For example, a <code>DataSource</code> could have the <code>Name</code> <code>2014-09-09-HolidayGiftMailer</code>. To search for this <code>DataSource</code>, select <code>Name</code> for the <code>FilterVariable</code> and any of the following strings for the <code>Prefix</code>: </p> <ul> <li> <p>2014-09</p> </li> <li> <p>2014-09-09</p> </li> <li> <p>2014-09-09-Holiday</p> </li> </ul>
            sort_order: <p>A two-value parameter that determines the sequence of the resulting list of <code>DataSource</code>.</p> <ul> <li> <p> <code>asc</code> - Arranges the list in ascending order (A-Z, 0-9).</p> </li> <li> <p> <code>dsc</code> - Arranges the list in descending order (Z-A, 9-0).</p> </li> </ul> <p>Results are sorted by <code>FilterVariable</code>.</p>
            next_token: <p>The ID of the page in the paginated results.</p>
            limit: <p> The maximum number of <code>DataSource</code> to include in the result.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.describe_data_sources_input.DescribeDataSourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.describe_data_sources_output.DescribeDataSourcesOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.describe_data_sources

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.describe_data_sources.async_describe_data_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.describe_data_sources_input.DescribeDataSourcesInput = {}
        if filter_variable is not None:
            input_["filter_variable"] = filter_variable
        if eq is not None:
            input_["eq"] = eq
        if gt is not None:
            input_["gt"] = gt
        if lt is not None:
            input_["lt"] = lt
        if ge is not None:
            input_["ge"] = ge
        if le is not None:
            input_["le"] = le
        if ne is not None:
            input_["ne"] = ne
        if prefix is not None:
            input_["prefix"] = prefix
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_data_sources(
        self,
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        filter_variable: Optional[
            "capo_machine_learning.types.data_source_filter_variable.DataSourceFilterVariable"
        ] = None,
        eq: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        gt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        lt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ge: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        le: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ne: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        prefix: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        sort_order: Optional["capo_machine_learning.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_machine_learning.types.string_type.StringType"
        ] = None,
        limit: Optional["capo_machine_learning.types.page_limit.PageLimit"] = None,
    ) -> "AsyncIterator[capo_machine_learning.types.data_source.DataSource]":
        _token = next_token
        while True:
            _response = await self.describe_data_sources(
                config_overrides=config_overrides,
                filter_variable=filter_variable,
                eq=eq,
                gt=gt,
                lt=lt,
                ge=ge,
                le=le,
                ne=ne,
                prefix=prefix,
                sort_order=sort_order,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_evaluations(
        self,
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        filter_variable: Optional[
            "capo_machine_learning.types.evaluation_filter_variable.EvaluationFilterVariable"
        ] = None,
        eq: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        gt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        lt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ge: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        le: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ne: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        prefix: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        sort_order: Optional["capo_machine_learning.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_machine_learning.types.string_type.StringType"
        ] = None,
        limit: Optional["capo_machine_learning.types.page_limit.PageLimit"] = None,
    ) -> "capo_machine_learning.types.describe_evaluations_output.DescribeEvaluationsOutput":
        """<p>Returns a list of <code>DescribeEvaluations</code> that match the search criteria in the request.</p>

        Args:
            filter_variable: <p>Use one of the following variable to filter a list of <code>Evaluation</code> objects:</p> <ul> <li> <p> <code>CreatedAt</code> - Sets the search criteria to the <code>Evaluation</code> creation date.</p> </li> <li> <p> <code>Status</code> - Sets the search criteria to the <code>Evaluation</code> status.</p> </li> <li> <p> <code>Name</code> - Sets the search criteria to the contents of <code>Evaluation</code> <b> </b> <code>Name</code>.</p> </li> <li> <p> <code>IAMUser</code> - Sets the search criteria to the user account that invoked an <code>Evaluation</code>.</p> </li> <li> <p> <code>MLModelId</code> - Sets the search criteria to the <code>MLModel</code> that was evaluated.</p> </li> <li> <p> <code>DataSourceId</code> - Sets the search criteria to the <code>DataSource</code> used in <code>Evaluation</code>.</p> </li> <li> <p> <code>DataUri</code> - Sets the search criteria to the data file(s) used in <code>Evaluation</code>. The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.</p> </li> </ul>
            eq: <p>The equal to operator. The <code>Evaluation</code> results will have <code>FilterVariable</code> values that exactly match the value specified with <code>EQ</code>.</p>
            gt: <p>The greater than operator. The <code>Evaluation</code> results will have <code>FilterVariable</code> values that are greater than the value specified with <code>GT</code>.</p>
            lt: <p>The less than operator. The <code>Evaluation</code> results will have <code>FilterVariable</code> values that are less than the value specified with <code>LT</code>.</p>
            ge: <p>The greater than or equal to operator. The <code>Evaluation</code> results will have <code>FilterVariable</code> values that are greater than or equal to the value specified with <code>GE</code>. </p>
            le: <p>The less than or equal to operator. The <code>Evaluation</code> results will have <code>FilterVariable</code> values that are less than or equal to the value specified with <code>LE</code>.</p>
            ne: <p>The not equal to operator. The <code>Evaluation</code> results will have <code>FilterVariable</code> values not equal to the value specified with <code>NE</code>.</p>
            prefix: <p>A string that is found at the beginning of a variable, such as <code>Name</code> or <code>Id</code>.</p> <p>For example, an <code>Evaluation</code> could have the <code>Name</code> <code>2014-09-09-HolidayGiftMailer</code>. To search for this <code>Evaluation</code>, select <code>Name</code> for the <code>FilterVariable</code> and any of the following strings for the <code>Prefix</code>: </p> <ul> <li> <p>2014-09</p> </li> <li> <p>2014-09-09</p> </li> <li> <p>2014-09-09-Holiday</p> </li> </ul>
            sort_order: <p>A two-value parameter that determines the sequence of the resulting list of <code>Evaluation</code>.</p> <ul> <li> <p> <code>asc</code> - Arranges the list in ascending order (A-Z, 0-9).</p> </li> <li> <p> <code>dsc</code> - Arranges the list in descending order (Z-A, 9-0).</p> </li> </ul> <p>Results are sorted by <code>FilterVariable</code>.</p>
            next_token: <p>The ID of the page in the paginated results.</p>
            limit: <p> The maximum number of <code>Evaluation</code> to include in the result.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.describe_evaluations_input.DescribeEvaluationsInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.describe_evaluations_output.DescribeEvaluationsOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.describe_evaluations

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.describe_evaluations.async_describe_evaluations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.describe_evaluations_input.DescribeEvaluationsInput = {}
        if filter_variable is not None:
            input_["filter_variable"] = filter_variable
        if eq is not None:
            input_["eq"] = eq
        if gt is not None:
            input_["gt"] = gt
        if lt is not None:
            input_["lt"] = lt
        if ge is not None:
            input_["ge"] = ge
        if le is not None:
            input_["le"] = le
        if ne is not None:
            input_["ne"] = ne
        if prefix is not None:
            input_["prefix"] = prefix
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_evaluations(
        self,
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        filter_variable: Optional[
            "capo_machine_learning.types.evaluation_filter_variable.EvaluationFilterVariable"
        ] = None,
        eq: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        gt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        lt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ge: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        le: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ne: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        prefix: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        sort_order: Optional["capo_machine_learning.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_machine_learning.types.string_type.StringType"
        ] = None,
        limit: Optional["capo_machine_learning.types.page_limit.PageLimit"] = None,
    ) -> "AsyncIterator[capo_machine_learning.types.evaluation.Evaluation]":
        _token = next_token
        while True:
            _response = await self.describe_evaluations(
                config_overrides=config_overrides,
                filter_variable=filter_variable,
                eq=eq,
                gt=gt,
                lt=lt,
                ge=ge,
                le=le,
                ne=ne,
                prefix=prefix,
                sort_order=sort_order,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_ml_models(
        self,
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        filter_variable: Optional[
            "capo_machine_learning.types.ml_model_filter_variable.MLModelFilterVariable"
        ] = None,
        eq: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        gt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        lt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ge: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        le: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ne: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        prefix: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        sort_order: Optional["capo_machine_learning.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_machine_learning.types.string_type.StringType"
        ] = None,
        limit: Optional["capo_machine_learning.types.page_limit.PageLimit"] = None,
    ) -> "capo_machine_learning.types.describe_ml_models_output.DescribeMLModelsOutput":
        """<p>Returns a list of <code>MLModel</code> that match the search criteria in the request.</p>

        Args:
            filter_variable: <p>Use one of the following variables to filter a list of <code>MLModel</code>:</p> <ul> <li> <p> <code>CreatedAt</code> - Sets the search criteria to <code>MLModel</code> creation date.</p> </li> <li> <p> <code>Status</code> - Sets the search criteria to <code>MLModel</code> status.</p> </li> <li> <p> <code>Name</code> - Sets the search criteria to the contents of <code>MLModel</code> <b> </b> <code>Name</code>.</p> </li> <li> <p> <code>IAMUser</code> - Sets the search criteria to the user account that invoked the <code>MLModel</code> creation.</p> </li> <li> <p> <code>TrainingDataSourceId</code> - Sets the search criteria to the <code>DataSource</code> used to train one or more <code>MLModel</code>.</p> </li> <li> <p> <code>RealtimeEndpointStatus</code> - Sets the search criteria to the <code>MLModel</code> real-time endpoint status.</p> </li> <li> <p> <code>MLModelType</code> - Sets the search criteria to <code>MLModel</code> type: binary, regression, or multi-class.</p> </li> <li> <p> <code>Algorithm</code> - Sets the search criteria to the algorithm that the <code>MLModel</code> uses.</p> </li> <li> <p> <code>TrainingDataURI</code> - Sets the search criteria to the data file(s) used in training a <code>MLModel</code>. The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.</p> </li> </ul>
            eq: <p>The equal to operator. The <code>MLModel</code> results will have <code>FilterVariable</code> values that exactly match the value specified with <code>EQ</code>.</p>
            gt: <p>The greater than operator. The <code>MLModel</code> results will have <code>FilterVariable</code> values that are greater than the value specified with <code>GT</code>.</p>
            lt: <p>The less than operator. The <code>MLModel</code> results will have <code>FilterVariable</code> values that are less than the value specified with <code>LT</code>.</p>
            ge: <p>The greater than or equal to operator. The <code>MLModel</code> results will have <code>FilterVariable</code> values that are greater than or equal to the value specified with <code>GE</code>. </p>
            le: <p>The less than or equal to operator. The <code>MLModel</code> results will have <code>FilterVariable</code> values that are less than or equal to the value specified with <code>LE</code>.</p>
            ne: <p>The not equal to operator. The <code>MLModel</code> results will have <code>FilterVariable</code> values not equal to the value specified with <code>NE</code>.</p>
            prefix: <p>A string that is found at the beginning of a variable, such as <code>Name</code> or <code>Id</code>.</p> <p>For example, an <code>MLModel</code> could have the <code>Name</code> <code>2014-09-09-HolidayGiftMailer</code>. To search for this <code>MLModel</code>, select <code>Name</code> for the <code>FilterVariable</code> and any of the following strings for the <code>Prefix</code>: </p> <ul> <li> <p>2014-09</p> </li> <li> <p>2014-09-09</p> </li> <li> <p>2014-09-09-Holiday</p> </li> </ul>
            sort_order: <p>A two-value parameter that determines the sequence of the resulting list of <code>MLModel</code>.</p> <ul> <li> <p> <code>asc</code> - Arranges the list in ascending order (A-Z, 0-9).</p> </li> <li> <p> <code>dsc</code> - Arranges the list in descending order (Z-A, 9-0).</p> </li> </ul> <p>Results are sorted by <code>FilterVariable</code>.</p>
            next_token: <p>The ID of the page in the paginated results.</p>
            limit: <p>The number of pages of information to include in the result. The range of acceptable values is <code>1</code> through <code>100</code>. The default value is <code>100</code>.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.describe_ml_models_input.DescribeMLModelsInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.describe_ml_models_output.DescribeMLModelsOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.describe_ml_models

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.describe_ml_models.async_describe_ml_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.describe_ml_models_input.DescribeMLModelsInput = {}
        if filter_variable is not None:
            input_["filter_variable"] = filter_variable
        if eq is not None:
            input_["eq"] = eq
        if gt is not None:
            input_["gt"] = gt
        if lt is not None:
            input_["lt"] = lt
        if ge is not None:
            input_["ge"] = ge
        if le is not None:
            input_["le"] = le
        if ne is not None:
            input_["ne"] = ne
        if prefix is not None:
            input_["prefix"] = prefix
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_ml_models(
        self,
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        filter_variable: Optional[
            "capo_machine_learning.types.ml_model_filter_variable.MLModelFilterVariable"
        ] = None,
        eq: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        gt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        lt: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ge: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        le: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        ne: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        prefix: Optional[
            "capo_machine_learning.types.comparator_value.ComparatorValue"
        ] = None,
        sort_order: Optional["capo_machine_learning.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_machine_learning.types.string_type.StringType"
        ] = None,
        limit: Optional["capo_machine_learning.types.page_limit.PageLimit"] = None,
    ) -> "AsyncIterator[capo_machine_learning.types.ml_model.MLModel]":
        _token = next_token
        while True:
            _response = await self.describe_ml_models(
                config_overrides=config_overrides,
                filter_variable=filter_variable,
                eq=eq,
                gt=gt,
                lt=lt,
                ge=ge,
                le=le,
                ne=ne,
                prefix=prefix,
                sort_order=sort_order,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_tags(
        self,
        resource_id: "capo_machine_learning.types.entity_id.EntityId",
        resource_type: "capo_machine_learning.types.taggable_resource_type.TaggableResourceType",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.describe_tags_output.DescribeTagsOutput":
        """<p>Describes one or more of the tags for your Amazon ML object.</p>

        Args:
            resource_id: <p>The ID of the ML object. For example, <code>exampleModelId</code>. </p>
            resource_type: <p>The type of the ML object.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.describe_tags_input.DescribeTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.describe_tags_output.DescribeTagsOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.describe_tags

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.describe_tags.async_describe_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.describe_tags_input.DescribeTagsInput = {
            "resource_id": resource_id,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_batch_prediction(
        self,
        batch_prediction_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.get_batch_prediction_output.GetBatchPredictionOutput":
        """<p>Returns a <code>BatchPrediction</code> that includes detailed metadata, status, and data file information for a <code>Batch Prediction</code> request.</p>

        Args:
            batch_prediction_id: <p>An ID assigned to the <code>BatchPrediction</code> at creation.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.get_batch_prediction_input.GetBatchPredictionInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.get_batch_prediction_output.GetBatchPredictionOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.get_batch_prediction

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.get_batch_prediction.async_get_batch_prediction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.get_batch_prediction_input.GetBatchPredictionInput = {
            "batch_prediction_id": batch_prediction_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_source(
        self,
        data_source_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        verbose: Optional["capo_machine_learning.types.verbose.Verbose"] = None,
    ) -> "capo_machine_learning.types.get_data_source_output.GetDataSourceOutput":
        """<p>Returns a <code>DataSource</code> that includes metadata and data file information, as well as the current status of the <code>DataSource</code>.</p> <p> <code>GetDataSource</code> provides results in normal or verbose format. The verbose format adds the schema description and the list of files pointed to by the DataSource to the normal format.</p>

        Args:
            data_source_id: <p>The ID assigned to the <code>DataSource</code> at creation.</p>
            verbose: <p>Specifies whether the <code>GetDataSource</code> operation should return <code>DataSourceSchema</code>.</p> <p>If true, <code>DataSourceSchema</code> is returned.</p> <p>If false, <code>DataSourceSchema</code> is not returned.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.get_data_source_input.GetDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.get_data_source_output.GetDataSourceOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.get_data_source

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.get_data_source.async_get_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.get_data_source_input.GetDataSourceInput = {
            "data_source_id": data_source_id
        }
        if verbose is not None:
            input_["verbose"] = verbose

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_evaluation(
        self,
        evaluation_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.get_evaluation_output.GetEvaluationOutput":
        """<p>Returns an <code>Evaluation</code> that includes metadata as well as the current status of the <code>Evaluation</code>.</p>

        Args:
            evaluation_id: <p>The ID of the <code>Evaluation</code> to retrieve. The evaluation of each <code>MLModel</code> is recorded and cataloged. The ID provides the means to access the information. </p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.get_evaluation_input.GetEvaluationInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.get_evaluation_output.GetEvaluationOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.get_evaluation

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.get_evaluation.async_get_evaluation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.get_evaluation_input.GetEvaluationInput = {
            "evaluation_id": evaluation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ml_model(
        self,
        ml_model_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        verbose: Optional["capo_machine_learning.types.verbose.Verbose"] = None,
    ) -> "capo_machine_learning.types.get_ml_model_output.GetMLModelOutput":
        """<p>Returns an <code>MLModel</code> that includes detailed metadata, data source information, and the current status of the <code>MLModel</code>.</p> <p> <code>GetMLModel</code> provides results in normal or verbose format. </p>

        Args:
            ml_model_id: <p>The ID assigned to the <code>MLModel</code> at creation.</p>
            verbose: <p>Specifies whether the <code>GetMLModel</code> operation should return <code>Recipe</code>.</p> <p>If true, <code>Recipe</code> is returned.</p> <p>If false, <code>Recipe</code> is not returned.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.get_ml_model_input.GetMLModelInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.get_ml_model_output.GetMLModelOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.get_ml_model

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.get_ml_model.async_get_ml_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.get_ml_model_input.GetMLModelInput = {
            "ml_model_id": ml_model_id
        }
        if verbose is not None:
            input_["verbose"] = verbose

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def predict(
        self,
        ml_model_id: "capo_machine_learning.types.entity_id.EntityId",
        record: "capo_machine_learning.types.record.Record",
        predict_endpoint: "capo_machine_learning.types.vip_url.VipURL",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.predict_output.PredictOutput":
        """<p>Generates a prediction for the observation using the specified <code>ML Model</code>.</p> <p> <b>Note:</b> Not all response parameters will be populated. Whether a response parameter is populated depends on the type of model requested.</p>

        Args:
            ml_model_id: <p>A unique identifier of the <code>MLModel</code>.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.limit_exceeded_exception.LimitExceededException: <p>The subscriber exceeded the maximum number of operations. This exception can occur when listing objects such as <code>DataSource</code>.</p>
            capo_machine_learning.errors.predictor_not_mounted_exception.PredictorNotMountedException: <p>The exception is thrown when a predict request is made to an unmounted <code>MLModel</code>.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.predict_input.PredictInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.predict_output.PredictOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.predict

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.predict.async_predict(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.predict_input.PredictInput = {
            "ml_model_id": ml_model_id,
            "record": record,
            "predict_endpoint": predict_endpoint,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_batch_prediction(
        self,
        batch_prediction_id: "capo_machine_learning.types.entity_id.EntityId",
        batch_prediction_name: "capo_machine_learning.types.entity_name.EntityName",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.update_batch_prediction_output.UpdateBatchPredictionOutput":
        """<p>Updates the <code>BatchPredictionName</code> of a <code>BatchPrediction</code>.</p> <p>You can use the <code>GetBatchPrediction</code> operation to view the contents of the updated data element.</p>

        Args:
            batch_prediction_id: <p>The ID assigned to the <code>BatchPrediction</code> during creation.</p>
            batch_prediction_name: <p>A new user-supplied name or description of the <code>BatchPrediction</code>.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.update_batch_prediction_input.UpdateBatchPredictionInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.update_batch_prediction_output.UpdateBatchPredictionOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.update_batch_prediction

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.update_batch_prediction.async_update_batch_prediction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.update_batch_prediction_input.UpdateBatchPredictionInput = {
            "batch_prediction_id": batch_prediction_id,
            "batch_prediction_name": batch_prediction_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_source(
        self,
        data_source_id: "capo_machine_learning.types.entity_id.EntityId",
        data_source_name: "capo_machine_learning.types.entity_name.EntityName",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.update_data_source_output.UpdateDataSourceOutput":
        """<p>Updates the <code>DataSourceName</code> of a <code>DataSource</code>.</p> <p>You can use the <code>GetDataSource</code> operation to view the contents of the updated data element.</p>

        Args:
            data_source_id: <p>The ID assigned to the <code>DataSource</code> during creation.</p>
            data_source_name: <p>A new user-supplied name or description of the <code>DataSource</code> that will replace the current description. </p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.update_data_source_input.UpdateDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.update_data_source_output.UpdateDataSourceOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.update_data_source

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.update_data_source.async_update_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.update_data_source_input.UpdateDataSourceInput = {
            "data_source_id": data_source_id,
            "data_source_name": data_source_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_evaluation(
        self,
        evaluation_id: "capo_machine_learning.types.entity_id.EntityId",
        evaluation_name: "capo_machine_learning.types.entity_name.EntityName",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
    ) -> "capo_machine_learning.types.update_evaluation_output.UpdateEvaluationOutput":
        """<p>Updates the <code>EvaluationName</code> of an <code>Evaluation</code>.</p> <p>You can use the <code>GetEvaluation</code> operation to view the contents of the updated data element.</p>

        Args:
            evaluation_id: <p>The ID assigned to the <code>Evaluation</code> during creation.</p>
            evaluation_name: <p>A new user-supplied name or description of the <code>Evaluation</code> that will replace the current content. </p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.update_evaluation_input.UpdateEvaluationInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.update_evaluation_output.UpdateEvaluationOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.update_evaluation

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.update_evaluation.async_update_evaluation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.update_evaluation_input.UpdateEvaluationInput = {
            "evaluation_id": evaluation_id,
            "evaluation_name": evaluation_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ml_model(
        self,
        ml_model_id: "capo_machine_learning.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncMachineLearningClientConfig] = None,
        ml_model_name: Optional[
            "capo_machine_learning.types.entity_name.EntityName"
        ] = None,
        score_threshold: Optional[
            "capo_machine_learning.types.score_threshold.ScoreThreshold"
        ] = None,
    ) -> "capo_machine_learning.types.update_ml_model_output.UpdateMLModelOutput":
        """<p>Updates the <code>MLModelName</code> and the <code>ScoreThreshold</code> of an <code>MLModel</code>.</p> <p>You can use the <code>GetMLModel</code> operation to view the contents of the updated data element.</p>

        Args:
            ml_model_id: <p>The ID assigned to the <code>MLModel</code> during creation.</p>
            ml_model_name: <p>A user-supplied name or description of the <code>MLModel</code>.</p>
            score_threshold: <p>The <code>ScoreThreshold</code> used in binary classification <code>MLModel</code> that marks the boundary between a positive prediction and a negative prediction.</p> <p>Output values greater than or equal to the <code>ScoreThreshold</code> receive a positive result from the <code>MLModel</code>, such as <code>true</code>. Output values less than the <code>ScoreThreshold</code> receive a negative response from the <code>MLModel</code>, such as <code>false</code>.</p>

        Raises:
            capo_machine_learning.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred when trying to process a request.</p>
            capo_machine_learning.errors.invalid_input_exception.InvalidInputException: <p>An error on the client occurred. Typically, the cause is an invalid input value.</p>
            capo_machine_learning.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource cannot be located.</p>
            capo_machine_learning.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_machine_learning.types.update_ml_model_input.UpdateMLModelInput]",
        ) -> AsyncOperationResponse[
            "capo_machine_learning.types.update_ml_model_output.UpdateMLModelOutput"
        ]:
            import capo_machine_learning._operations.amazon_ml_20141212.update_ml_model

            (
                output,
                http_response,
            ) = await capo_machine_learning._operations.amazon_ml_20141212.update_ml_model.async_update_ml_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_machine_learning.types.update_ml_model_input.UpdateMLModelInput = {
            "ml_model_id": ml_model_id
        }
        if ml_model_name is not None:
            input_["ml_model_name"] = ml_model_name
        if score_threshold is not None:
            input_["score_threshold"] = score_threshold

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
