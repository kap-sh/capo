"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#AWSLookoutEquipmentFrontendService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_lookoutequipment._auth._signers
import capo_lookoutequipment._auth._sigv4
from capo_lookoutequipment._auth._identity import Credentials
from capo_lookoutequipment._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lookoutequipment._auth._zapros_handler import AuthMiddleware
from capo_lookoutequipment._pagination import resolve_path as _resolve_path
from capo_lookoutequipment._services._aws_config import aaws_config
from capo_lookoutequipment._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_lookoutequipment.types.amazon_resource_arn
    import capo_lookoutequipment.types.comments
    import capo_lookoutequipment.types.create_dataset_request
    import capo_lookoutequipment.types.create_dataset_response
    import capo_lookoutequipment.types.create_inference_scheduler_request
    import capo_lookoutequipment.types.create_inference_scheduler_response
    import capo_lookoutequipment.types.create_label_group_request
    import capo_lookoutequipment.types.create_label_group_response
    import capo_lookoutequipment.types.create_label_request
    import capo_lookoutequipment.types.create_label_response
    import capo_lookoutequipment.types.create_model_request
    import capo_lookoutequipment.types.create_model_response
    import capo_lookoutequipment.types.create_retraining_scheduler_request
    import capo_lookoutequipment.types.create_retraining_scheduler_response
    import capo_lookoutequipment.types.data_delay_offset_in_minutes
    import capo_lookoutequipment.types.data_pre_processing_configuration
    import capo_lookoutequipment.types.data_upload_frequency
    import capo_lookoutequipment.types.dataset_arn
    import capo_lookoutequipment.types.dataset_identifier
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.dataset_schema
    import capo_lookoutequipment.types.delete_dataset_request
    import capo_lookoutequipment.types.delete_inference_scheduler_request
    import capo_lookoutequipment.types.delete_label_group_request
    import capo_lookoutequipment.types.delete_label_request
    import capo_lookoutequipment.types.delete_model_request
    import capo_lookoutequipment.types.delete_resource_policy_request
    import capo_lookoutequipment.types.delete_retraining_scheduler_request
    import capo_lookoutequipment.types.describe_data_ingestion_job_request
    import capo_lookoutequipment.types.describe_data_ingestion_job_response
    import capo_lookoutequipment.types.describe_dataset_request
    import capo_lookoutequipment.types.describe_dataset_response
    import capo_lookoutequipment.types.describe_inference_scheduler_request
    import capo_lookoutequipment.types.describe_inference_scheduler_response
    import capo_lookoutequipment.types.describe_label_group_request
    import capo_lookoutequipment.types.describe_label_group_response
    import capo_lookoutequipment.types.describe_label_request
    import capo_lookoutequipment.types.describe_label_response
    import capo_lookoutequipment.types.describe_model_request
    import capo_lookoutequipment.types.describe_model_response
    import capo_lookoutequipment.types.describe_model_version_request
    import capo_lookoutequipment.types.describe_model_version_response
    import capo_lookoutequipment.types.describe_resource_policy_request
    import capo_lookoutequipment.types.describe_resource_policy_response
    import capo_lookoutequipment.types.describe_retraining_scheduler_request
    import capo_lookoutequipment.types.describe_retraining_scheduler_response
    import capo_lookoutequipment.types.equipment
    import capo_lookoutequipment.types.fault_code
    import capo_lookoutequipment.types.fault_codes
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.import_dataset_request
    import capo_lookoutequipment.types.import_dataset_response
    import capo_lookoutequipment.types.import_model_version_request
    import capo_lookoutequipment.types.import_model_version_response
    import capo_lookoutequipment.types.inference_data_import_strategy
    import capo_lookoutequipment.types.inference_execution_status
    import capo_lookoutequipment.types.inference_input_configuration
    import capo_lookoutequipment.types.inference_output_configuration
    import capo_lookoutequipment.types.inference_scheduler_identifier
    import capo_lookoutequipment.types.inference_scheduler_name
    import capo_lookoutequipment.types.inference_scheduler_status
    import capo_lookoutequipment.types.ingestion_input_configuration
    import capo_lookoutequipment.types.ingestion_job_id
    import capo_lookoutequipment.types.ingestion_job_status
    import capo_lookoutequipment.types.label_group_name
    import capo_lookoutequipment.types.label_id
    import capo_lookoutequipment.types.label_rating
    import capo_lookoutequipment.types.labels_input_configuration
    import capo_lookoutequipment.types.list_data_ingestion_jobs_request
    import capo_lookoutequipment.types.list_data_ingestion_jobs_response
    import capo_lookoutequipment.types.list_datasets_request
    import capo_lookoutequipment.types.list_datasets_response
    import capo_lookoutequipment.types.list_inference_events_request
    import capo_lookoutequipment.types.list_inference_events_response
    import capo_lookoutequipment.types.list_inference_executions_request
    import capo_lookoutequipment.types.list_inference_executions_response
    import capo_lookoutequipment.types.list_inference_schedulers_request
    import capo_lookoutequipment.types.list_inference_schedulers_response
    import capo_lookoutequipment.types.list_label_groups_request
    import capo_lookoutequipment.types.list_label_groups_response
    import capo_lookoutequipment.types.list_labels_request
    import capo_lookoutequipment.types.list_labels_response
    import capo_lookoutequipment.types.list_model_versions_request
    import capo_lookoutequipment.types.list_model_versions_response
    import capo_lookoutequipment.types.list_models_request
    import capo_lookoutequipment.types.list_models_response
    import capo_lookoutequipment.types.list_retraining_schedulers_request
    import capo_lookoutequipment.types.list_retraining_schedulers_response
    import capo_lookoutequipment.types.list_sensor_statistics_request
    import capo_lookoutequipment.types.list_sensor_statistics_response
    import capo_lookoutequipment.types.list_tags_for_resource_request
    import capo_lookoutequipment.types.list_tags_for_resource_response
    import capo_lookoutequipment.types.lookback_window
    import capo_lookoutequipment.types.max_results
    import capo_lookoutequipment.types.model_diagnostics_output_configuration
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.model_promote_mode
    import capo_lookoutequipment.types.model_status
    import capo_lookoutequipment.types.model_version
    import capo_lookoutequipment.types.model_version_arn
    import capo_lookoutequipment.types.model_version_source_type
    import capo_lookoutequipment.types.model_version_status
    import capo_lookoutequipment.types.name_or_arn
    import capo_lookoutequipment.types.next_token
    import capo_lookoutequipment.types.off_condition
    import capo_lookoutequipment.types.policy
    import capo_lookoutequipment.types.policy_revision_id
    import capo_lookoutequipment.types.put_resource_policy_request
    import capo_lookoutequipment.types.put_resource_policy_response
    import capo_lookoutequipment.types.resource_arn
    import capo_lookoutequipment.types.retraining_frequency
    import capo_lookoutequipment.types.retraining_scheduler_status
    import capo_lookoutequipment.types.start_data_ingestion_job_request
    import capo_lookoutequipment.types.start_data_ingestion_job_response
    import capo_lookoutequipment.types.start_inference_scheduler_request
    import capo_lookoutequipment.types.start_inference_scheduler_response
    import capo_lookoutequipment.types.start_retraining_scheduler_request
    import capo_lookoutequipment.types.start_retraining_scheduler_response
    import capo_lookoutequipment.types.stop_inference_scheduler_request
    import capo_lookoutequipment.types.stop_inference_scheduler_response
    import capo_lookoutequipment.types.stop_retraining_scheduler_request
    import capo_lookoutequipment.types.stop_retraining_scheduler_response
    import capo_lookoutequipment.types.tag_key_list
    import capo_lookoutequipment.types.tag_list
    import capo_lookoutequipment.types.tag_resource_request
    import capo_lookoutequipment.types.tag_resource_response
    import capo_lookoutequipment.types.timestamp
    import capo_lookoutequipment.types.untag_resource_request
    import capo_lookoutequipment.types.untag_resource_response
    import capo_lookoutequipment.types.update_active_model_version_request
    import capo_lookoutequipment.types.update_active_model_version_response
    import capo_lookoutequipment.types.update_inference_scheduler_request
    import capo_lookoutequipment.types.update_label_group_request
    import capo_lookoutequipment.types.update_model_request
    import capo_lookoutequipment.types.update_retraining_scheduler_request


class AsyncLookoutEquipmentClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncLookoutEquipmentClient:
    """A client for the ``LookoutEquipment`` service.

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
        self._config = AsyncLookoutEquipmentClientConfig(
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
        self, config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLookoutEquipmentClientConfig = config_overrides or {}
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

    async def create_dataset(
        self,
        dataset_name: "capo_lookoutequipment.types.dataset_name.DatasetName",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        dataset_schema: Optional[
            "capo_lookoutequipment.types.dataset_schema.DatasetSchema"
        ] = None,
        server_side_kms_key_id: Optional[
            "capo_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["capo_lookoutequipment.types.tag_list.TagList"] = None,
    ) -> "capo_lookoutequipment.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates a container for a collection of data being ingested for analysis. The dataset contains the metadata describing where the data is and what the data actually looks like. For example, it contains the location of the data source, the data schema, and other information. A dataset also contains any tags associated with the ingested data. </p>

        Args:
            dataset_name: <p>The name of the dataset being created. </p>
            dataset_schema: <p>A JSON description of the data that is in each time series dataset, including names, column names, and data types. </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key used to encrypt dataset data by Amazon Lookout for Equipment. </p>
            client_token: <p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            tags: <p>Any tags associated with the ingested data described in the dataset. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.create_dataset_request.CreateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_dataset

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.create_dataset_request.CreateDatasetRequest = {
            "dataset_name": dataset_name,
            "client_token": client_token,
        }
        if dataset_schema is not None:
            input_["dataset_schema"] = dataset_schema
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_inference_scheduler(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_name.InferenceSchedulerName",
        data_upload_frequency: "capo_lookoutequipment.types.data_upload_frequency.DataUploadFrequency",
        data_input_configuration: "capo_lookoutequipment.types.inference_input_configuration.InferenceInputConfiguration",
        data_output_configuration: "capo_lookoutequipment.types.inference_output_configuration.InferenceOutputConfiguration",
        role_arn: "capo_lookoutequipment.types.iam_role_arn.IamRoleArn",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        data_delay_offset_in_minutes: Optional[
            "capo_lookoutequipment.types.data_delay_offset_in_minutes.DataDelayOffsetInMinutes"
        ] = None,
        server_side_kms_key_id: Optional[
            "capo_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["capo_lookoutequipment.types.tag_list.TagList"] = None,
    ) -> "capo_lookoutequipment.types.create_inference_scheduler_response.CreateInferenceSchedulerResponse":
        """<p> Creates a scheduled inference. Scheduling an inference is setting up a continuous real-time inference plan to analyze new measurement data. When setting up the schedule, you provide an S3 bucket location for the input data, assign it a delimiter between separate entries in the data, set an offset delay if desired, and set the frequency of inferencing. You must also provide an S3 bucket location for the output data. </p>

        Args:
            model_name: <p>The name of the previously trained machine learning model being used to create the inference scheduler. </p>
            inference_scheduler_name: <p>The name of the inference scheduler being created. </p>
            data_delay_offset_in_minutes: <p>The interval (in minutes) of planned delay at the start of each inference segment. For example, if inference is set to run every ten minutes, the delay is set to five minutes and the time is 09:08. The inference scheduler will wake up at the configured interval (which, without a delay configured, would be 09:10) plus the additional five minute delay time (so 09:15) to check your Amazon S3 bucket. The delay provides a buffer for you to upload data at the same frequency, so that you don't have to stop and restart the scheduler when uploading new data.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-inference-process.html">Understanding the inference process</a>.</p>
            data_upload_frequency: <p> How often data is uploaded to the source Amazon S3 bucket for the input data. The value chosen is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment runs inference on your data.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-inference-process.html">Understanding the inference process</a>.</p>
            data_input_configuration: <p>Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location. </p>
            data_output_configuration: <p>Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output. </p>
            role_arn: <p>The Amazon Resource Name (ARN) of a role with permission to access the data source being used for the inference. </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key used to encrypt inference scheduler data by Amazon Lookout for Equipment. </p>
            client_token: <p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            tags: <p>Any tags associated with the inference scheduler. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.create_inference_scheduler_request.CreateInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.create_inference_scheduler_response.CreateInferenceSchedulerResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_inference_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_inference_scheduler.async_create_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.create_inference_scheduler_request.CreateInferenceSchedulerRequest = {
            "model_name": model_name,
            "inference_scheduler_name": inference_scheduler_name,
            "data_upload_frequency": data_upload_frequency,
            "data_input_configuration": data_input_configuration,
            "data_output_configuration": data_output_configuration,
            "role_arn": role_arn,
            "client_token": client_token,
        }
        if data_delay_offset_in_minutes is not None:
            input_["data_delay_offset_in_minutes"] = data_delay_offset_in_minutes
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_label(
        self,
        label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName",
        start_time: "capo_lookoutequipment.types.timestamp.Timestamp",
        end_time: "capo_lookoutequipment.types.timestamp.Timestamp",
        rating: "capo_lookoutequipment.types.label_rating.LabelRating",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        fault_code: Optional["capo_lookoutequipment.types.fault_code.FaultCode"] = None,
        notes: Optional["capo_lookoutequipment.types.comments.Comments"] = None,
        equipment: Optional["capo_lookoutequipment.types.equipment.Equipment"] = None,
    ) -> "capo_lookoutequipment.types.create_label_response.CreateLabelResponse":
        """<p> Creates a label for an event. </p>

        Args:
            label_group_name: <p> The name of a group of labels. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>
            start_time: <p> The start time of the labeled event. </p>
            end_time: <p> The end time of the labeled event. </p>
            rating: <p> Indicates whether a labeled event represents an anomaly. </p>
            fault_code: <p> Provides additional information about the label. The fault code must be defined in the FaultCodes attribute of the label group.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>
            notes: <p> Metadata providing additional information about the label. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>
            equipment: <p> Indicates that a label pertains to a particular piece of equipment. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>
            client_token: <p> A unique identifier for the request to create a label. If you do not set the client request token, Lookout for Equipment generates one. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.create_label_request.CreateLabelRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.create_label_response.CreateLabelResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_label

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_label.async_create_label(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.create_label_request.CreateLabelRequest = {
            "label_group_name": label_group_name,
            "start_time": start_time,
            "end_time": end_time,
            "rating": rating,
            "client_token": client_token,
        }
        if fault_code is not None:
            input_["fault_code"] = fault_code
        if notes is not None:
            input_["notes"] = notes
        if equipment is not None:
            input_["equipment"] = equipment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_label_group(
        self,
        label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        fault_codes: Optional[
            "capo_lookoutequipment.types.fault_codes.FaultCodes"
        ] = None,
        tags: Optional["capo_lookoutequipment.types.tag_list.TagList"] = None,
    ) -> "capo_lookoutequipment.types.create_label_group_response.CreateLabelGroupResponse":
        """<p> Creates a group of labels. </p>

        Args:
            label_group_name: <p> Names a group of labels.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>
            fault_codes: <p> The acceptable fault codes (indicating the type of anomaly associated with the label) that can be used with this label group.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>
            client_token: <p> A unique identifier for the request to create a label group. If you do not set the client request token, Lookout for Equipment generates one. </p>
            tags: <p> Tags that provide metadata about the label group you are creating. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.create_label_group_request.CreateLabelGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.create_label_group_response.CreateLabelGroupResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_label_group

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_label_group.async_create_label_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.create_label_group_request.CreateLabelGroupRequest = {
            "label_group_name": label_group_name,
            "client_token": client_token,
        }
        if fault_codes is not None:
            input_["fault_codes"] = fault_codes
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_model(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        dataset_name: "capo_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        dataset_schema: Optional[
            "capo_lookoutequipment.types.dataset_schema.DatasetSchema"
        ] = None,
        labels_input_configuration: Optional[
            "capo_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
        ] = None,
        training_data_start_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        training_data_end_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        evaluation_data_start_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        evaluation_data_end_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        role_arn: Optional[
            "capo_lookoutequipment.types.iam_role_arn.IamRoleArn"
        ] = None,
        data_pre_processing_configuration: Optional[
            "capo_lookoutequipment.types.data_pre_processing_configuration.DataPreProcessingConfiguration"
        ] = None,
        server_side_kms_key_id: Optional[
            "capo_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["capo_lookoutequipment.types.tag_list.TagList"] = None,
        off_condition: Optional[
            "capo_lookoutequipment.types.off_condition.OffCondition"
        ] = None,
        model_diagnostics_output_configuration: Optional[
            "capo_lookoutequipment.types.model_diagnostics_output_configuration.ModelDiagnosticsOutputConfiguration"
        ] = None,
    ) -> "capo_lookoutequipment.types.create_model_response.CreateModelResponse":
        """<p>Creates a machine learning model for data inference. </p> <p>A machine-learning (ML) model is a mathematical model that finds patterns in your data. In Amazon Lookout for Equipment, the model learns the patterns of normal behavior and detects abnormal behavior that could be potential equipment failure (or maintenance events). The models are made by analyzing normal data and abnormalities in machine behavior that have already occurred.</p> <p>Your model is trained using a portion of the data from your dataset and uses that data to learn patterns of normal behavior and abnormal patterns that lead to equipment failure. Another portion of the data is used to evaluate the model's accuracy. </p>

        Args:
            model_name: <p>The name for the machine learning model to be created.</p>
            dataset_name: <p>The name of the dataset for the machine learning model being created. </p>
            dataset_schema: <p>The data schema for the machine learning model being created. </p>
            labels_input_configuration: <p>The input configuration for the labels being used for the machine learning model that's being created. </p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            training_data_start_time: <p>Indicates the time reference in the dataset that should be used to begin the subset of training data for the machine learning model. </p>
            training_data_end_time: <p>Indicates the time reference in the dataset that should be used to end the subset of training data for the machine learning model. </p>
            evaluation_data_start_time: <p>Indicates the time reference in the dataset that should be used to begin the subset of evaluation data for the machine learning model. </p>
            evaluation_data_end_time: <p> Indicates the time reference in the dataset that should be used to end the subset of evaluation data for the machine learning model. </p>
            role_arn: <p> The Amazon Resource Name (ARN) of a role with permission to access the data source being used to create the machine learning model. </p>
            data_pre_processing_configuration: <p>The configuration is the <code>TargetSamplingRate</code>, which is the sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the <code>TargetSamplingRate</code> is 1 minute.</p> <p>When providing a value for the <code>TargetSamplingRate</code>, you must attach the prefix "PT" to the rate you want. The value for a 1 second rate is therefore <i>PT1S</i>, the value for a 15 minute rate is <i>PT15M</i>, and the value for a 1 hour rate is <i>PT1H</i> </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key used to encrypt model data by Amazon Lookout for Equipment. </p>
            tags: <p> Any tags associated with the machine learning model being created. </p>
            off_condition: <p>Indicates that the asset associated with this sensor has been shut off. As long as this condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or inference.</p>
            model_diagnostics_output_configuration: <p>The Amazon S3 location where you want Amazon Lookout for Equipment to save the pointwise model diagnostics. You must also specify the <code>RoleArn</code> request parameter.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.create_model_request.CreateModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.create_model_response.CreateModelResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_model

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_model.async_create_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.create_model_request.CreateModelRequest = {
            "model_name": model_name,
            "dataset_name": dataset_name,
            "client_token": client_token,
        }
        if dataset_schema is not None:
            input_["dataset_schema"] = dataset_schema
        if labels_input_configuration is not None:
            input_["labels_input_configuration"] = labels_input_configuration
        if training_data_start_time is not None:
            input_["training_data_start_time"] = training_data_start_time
        if training_data_end_time is not None:
            input_["training_data_end_time"] = training_data_end_time
        if evaluation_data_start_time is not None:
            input_["evaluation_data_start_time"] = evaluation_data_start_time
        if evaluation_data_end_time is not None:
            input_["evaluation_data_end_time"] = evaluation_data_end_time
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if data_pre_processing_configuration is not None:
            input_["data_pre_processing_configuration"] = (
                data_pre_processing_configuration
            )
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if off_condition is not None:
            input_["off_condition"] = off_condition
        if model_diagnostics_output_configuration is not None:
            input_["model_diagnostics_output_configuration"] = (
                model_diagnostics_output_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_retraining_scheduler(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        retraining_frequency: "capo_lookoutequipment.types.retraining_frequency.RetrainingFrequency",
        lookback_window: "capo_lookoutequipment.types.lookback_window.LookbackWindow",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        retraining_start_date: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        promote_mode: Optional[
            "capo_lookoutequipment.types.model_promote_mode.ModelPromoteMode"
        ] = None,
    ) -> "capo_lookoutequipment.types.create_retraining_scheduler_response.CreateRetrainingSchedulerResponse":
        """<p>Creates a retraining scheduler on the specified model. </p>

        Args:
            model_name: <p>The name of the model to add the retraining scheduler to. </p>
            retraining_start_date: <p>The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the nearest UTC day.</p>
            retraining_frequency: <p>This parameter uses the <a href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601</a> standard to set the frequency at which you want retraining to occur in terms of Years, Months, and/or Days (note: other parameters like Time are not currently supported). The minimum value is 30 days (P30D) and the maximum value is 1 year (P1Y). For example, the following values are valid:</p> <ul> <li> <p>P3M15D – Every 3 months and 15 days</p> </li> <li> <p>P2M – Every 2 months</p> </li> <li> <p>P150D – Every 150 days</p> </li> </ul>
            lookback_window: <p>The number of past days of data that will be used for retraining.</p>
            promote_mode: <p>Indicates how the service will use new models. In <code>MANAGED</code> mode, new models will automatically be used for inference if they have better performance than the current model. In <code>MANUAL</code> mode, the new models will not be used <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/versioning-model.html#model-activation">until they are manually activated</a>.</p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creates a retraining scheduler with a specific start date

            >>> await client.create_retraining_scheduler(model_name='sample-model', retraining_start_date='2024-01-01T00:00:00Z', retraining_frequency='P1M', lookback_window='P360D', client_token='sample-client-token')
            Creates a retraining scheduler with manual promote mode

            >>> await client.create_retraining_scheduler(model_name='sample-model', retraining_frequency='P1M', lookback_window='P360D', promote_mode='MANUAL', client_token='sample-client-token')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.create_retraining_scheduler_request.CreateRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.create_retraining_scheduler_response.CreateRetrainingSchedulerResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_retraining_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_retraining_scheduler.async_create_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.create_retraining_scheduler_request.CreateRetrainingSchedulerRequest = {
            "model_name": model_name,
            "retraining_frequency": retraining_frequency,
            "lookback_window": lookback_window,
            "client_token": client_token,
        }
        if retraining_start_date is not None:
            input_["retraining_start_date"] = retraining_start_date
        if promote_mode is not None:
            input_["promote_mode"] = promote_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataset(
        self,
        dataset_name: "capo_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p> Deletes a dataset and associated artifacts. The operation will check to see if any inference scheduler or data ingestion job is currently using the dataset, and if there isn't, the dataset, its metadata, and any associated data stored in S3 will be deleted. This does not affect any models that used this dataset for training and evaluation, but does prevent it from being used in the future. </p>

        Args:
            dataset_name: <p>The name of the dataset to be deleted. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_dataset

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_dataset.async_delete_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.delete_dataset_request.DeleteDatasetRequest = {
            "dataset_name": dataset_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_inference_scheduler(
        self,
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p>Deletes an inference scheduler that has been set up. Prior inference results will not be deleted.</p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler to be deleted. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.delete_inference_scheduler_request.DeleteInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_inference_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_inference_scheduler.async_delete_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.delete_inference_scheduler_request.DeleteInferenceSchedulerRequest = {
            "inference_scheduler_name": inference_scheduler_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_label(
        self,
        label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName",
        label_id: "capo_lookoutequipment.types.label_id.LabelId",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p> Deletes a label. </p>

        Args:
            label_group_name: <p> The name of the label group that contains the label that you want to delete. Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>
            label_id: <p> The ID of the label that you want to delete. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.delete_label_request.DeleteLabelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_label

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_label.async_delete_label(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.delete_label_request.DeleteLabelRequest = {
            "label_group_name": label_group_name,
            "label_id": label_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_label_group(
        self,
        label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p> Deletes a group of labels. </p>

        Args:
            label_group_name: <p> The name of the label group that you want to delete. Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.delete_label_group_request.DeleteLabelGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_label_group

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_label_group.async_delete_label_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.delete_label_group_request.DeleteLabelGroupRequest = {
            "label_group_name": label_group_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_model(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p>Deletes a machine learning model currently available for Amazon Lookout for Equipment. This will prevent it from being used with an inference scheduler, even one that is already set up. </p>

        Args:
            model_name: <p>The name of the machine learning model to be deleted. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.delete_model_request.DeleteModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_model

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_model.async_delete_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.delete_model_request.DeleteModelRequest = {
            "model_name": model_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_lookoutequipment.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource policy attached to the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which the resource policy should be deleted.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_retraining_scheduler(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p>Deletes a retraining scheduler from a model. The retraining scheduler must be in the <code>STOPPED</code> status. </p>

        Args:
            model_name: <p>The name of the model whose retraining scheduler you want to delete. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Deletes a retraining scheduler

            >>> await client.delete_retraining_scheduler(model_name='sample-model')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.delete_retraining_scheduler_request.DeleteRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_retraining_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_retraining_scheduler.async_delete_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.delete_retraining_scheduler_request.DeleteRetrainingSchedulerRequest = {
            "model_name": model_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_data_ingestion_job(
        self,
        job_id: "capo_lookoutequipment.types.ingestion_job_id.IngestionJobId",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.describe_data_ingestion_job_response.DescribeDataIngestionJobResponse":
        """<p>Provides information on a specific data ingestion job such as creation time, dataset ARN, and status.</p>

        Args:
            job_id: <p>The job ID of the data ingestion job. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.describe_data_ingestion_job_request.DescribeDataIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.describe_data_ingestion_job_response.DescribeDataIngestionJobResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_data_ingestion_job

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_data_ingestion_job.async_describe_data_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.describe_data_ingestion_job_request.DescribeDataIngestionJobRequest = {
            "job_id": job_id
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
        dataset_name: "capo_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> (
        "capo_lookoutequipment.types.describe_dataset_response.DescribeDatasetResponse"
    ):
        """<p>Provides a JSON description of the data in each time series dataset, including names, column names, and data types.</p>

        Args:
            dataset_name: <p>The name of the dataset to be described. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_dataset

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_dataset.async_describe_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.describe_dataset_request.DescribeDatasetRequest = {
            "dataset_name": dataset_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_inference_scheduler(
        self,
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.describe_inference_scheduler_response.DescribeInferenceSchedulerResponse":
        """<p> Specifies information about the inference scheduler being used, including name, model, status, and associated metadata </p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler being described. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.describe_inference_scheduler_request.DescribeInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.describe_inference_scheduler_response.DescribeInferenceSchedulerResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_inference_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_inference_scheduler.async_describe_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.describe_inference_scheduler_request.DescribeInferenceSchedulerRequest = {
            "inference_scheduler_name": inference_scheduler_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_label(
        self,
        label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName",
        label_id: "capo_lookoutequipment.types.label_id.LabelId",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.describe_label_response.DescribeLabelResponse":
        """<p> Returns the name of the label. </p>

        Args:
            label_group_name: <p> Returns the name of the group containing the label. </p>
            label_id: <p> Returns the ID of the label. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.describe_label_request.DescribeLabelRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.describe_label_response.DescribeLabelResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_label

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_label.async_describe_label(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.describe_label_request.DescribeLabelRequest = {
            "label_group_name": label_group_name,
            "label_id": label_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_label_group(
        self,
        label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.describe_label_group_response.DescribeLabelGroupResponse":
        """<p> Returns information about the label group. </p>

        Args:
            label_group_name: <p> Returns the name of the label group. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.describe_label_group_request.DescribeLabelGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.describe_label_group_response.DescribeLabelGroupResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_label_group

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_label_group.async_describe_label_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.describe_label_group_request.DescribeLabelGroupRequest = {
            "label_group_name": label_group_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_model(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.describe_model_response.DescribeModelResponse":
        """<p>Provides a JSON containing the overall information about a specific machine learning model, including model name and ARN, dataset, training and evaluation information, status, and so on. </p>

        Args:
            model_name: <p>The name of the machine learning model to be described. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.describe_model_request.DescribeModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.describe_model_response.DescribeModelResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_model

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_model.async_describe_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.describe_model_request.DescribeModelRequest = {
            "model_name": model_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_model_version(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        model_version: "capo_lookoutequipment.types.model_version.ModelVersion",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.describe_model_version_response.DescribeModelVersionResponse":
        """<p>Retrieves information about a specific machine learning model version.</p>

        Args:
            model_name: <p>The name of the machine learning model that this version belongs to.</p>
            model_version: <p>The version of the machine learning model.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.describe_model_version_request.DescribeModelVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.describe_model_version_response.DescribeModelVersionResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_model_version

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_model_version.async_describe_model_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.describe_model_version_request.DescribeModelVersionRequest = {
            "model_name": model_name,
            "model_version": model_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_resource_policy(
        self,
        resource_arn: "capo_lookoutequipment.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.describe_resource_policy_response.DescribeResourcePolicyResponse":
        """<p>Provides the details of a resource policy attached to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that is associated with the resource policy.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.describe_resource_policy_request.DescribeResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.describe_resource_policy_response.DescribeResourcePolicyResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_resource_policy

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_resource_policy.async_describe_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.describe_resource_policy_request.DescribeResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_retraining_scheduler(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.describe_retraining_scheduler_response.DescribeRetrainingSchedulerResponse":
        """<p>Provides a description of the retraining scheduler, including information such as the model name and retraining parameters. </p>

        Args:
            model_name: <p>The name of the model that the retraining scheduler is attached to. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describes a retraining scheduler

            >>> await client.describe_retraining_scheduler(model_name='sample-model')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.describe_retraining_scheduler_request.DescribeRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.describe_retraining_scheduler_response.DescribeRetrainingSchedulerResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_retraining_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_retraining_scheduler.async_describe_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.describe_retraining_scheduler_request.DescribeRetrainingSchedulerRequest = {
            "model_name": model_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_dataset(
        self,
        source_dataset_arn: "capo_lookoutequipment.types.dataset_arn.DatasetArn",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        dataset_name: Optional[
            "capo_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
        server_side_kms_key_id: Optional[
            "capo_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["capo_lookoutequipment.types.tag_list.TagList"] = None,
    ) -> "capo_lookoutequipment.types.import_dataset_response.ImportDatasetResponse":
        """<p>Imports a dataset.</p>

        Args:
            source_dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset to import.</p>
            dataset_name: <p>The name of the machine learning dataset to be created. If the dataset already exists, Amazon Lookout for Equipment overwrites the existing dataset. If you don't specify this field, it is filled with the name of the source dataset.</p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key key used to encrypt model data by Amazon Lookout for Equipment. </p>
            tags: <p>Any tags associated with the dataset to be created.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.import_dataset_request.ImportDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.import_dataset_response.ImportDatasetResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.import_dataset

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.import_dataset.async_import_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.import_dataset_request.ImportDatasetRequest = {
            "source_dataset_arn": source_dataset_arn,
            "client_token": client_token,
        }
        if dataset_name is not None:
            input_["dataset_name"] = dataset_name
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_model_version(
        self,
        source_model_version_arn: "capo_lookoutequipment.types.model_version_arn.ModelVersionArn",
        dataset_name: "capo_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        model_name: Optional["capo_lookoutequipment.types.model_name.ModelName"] = None,
        labels_input_configuration: Optional[
            "capo_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
        ] = None,
        role_arn: Optional[
            "capo_lookoutequipment.types.iam_role_arn.IamRoleArn"
        ] = None,
        server_side_kms_key_id: Optional[
            "capo_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["capo_lookoutequipment.types.tag_list.TagList"] = None,
        inference_data_import_strategy: Optional[
            "capo_lookoutequipment.types.inference_data_import_strategy.InferenceDataImportStrategy"
        ] = None,
    ) -> "capo_lookoutequipment.types.import_model_version_response.ImportModelVersionResponse":
        """<p>Imports a model that has been trained successfully.</p>

        Args:
            source_model_version_arn: <p>The Amazon Resource Name (ARN) of the model version to import.</p>
            model_name: <p>The name for the machine learning model to be created. If the model already exists, Amazon Lookout for Equipment creates a new version. If you do not specify this field, it is filled with the name of the source model.</p>
            dataset_name: <p>The name of the dataset for the machine learning model being imported. </p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            role_arn: <p>The Amazon Resource Name (ARN) of a role with permission to access the data source being used to create the machine learning model. </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key key used to encrypt model data by Amazon Lookout for Equipment. </p>
            tags: <p>The tags associated with the machine learning model to be created. </p>
            inference_data_import_strategy: <p>Indicates how to import the accumulated inference data when a model version is imported. The possible values are as follows:</p> <ul> <li> <p>NO_IMPORT – Don't import the data.</p> </li> <li> <p>ADD_WHEN_EMPTY – Only import the data from the source model if there is no existing data in the target model.</p> </li> <li> <p>OVERWRITE – Import the data from the source model and overwrite the existing data in the target model.</p> </li> </ul>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.import_model_version_request.ImportModelVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.import_model_version_response.ImportModelVersionResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.import_model_version

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.import_model_version.async_import_model_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.import_model_version_request.ImportModelVersionRequest = {
            "source_model_version_arn": source_model_version_arn,
            "dataset_name": dataset_name,
            "client_token": client_token,
        }
        if model_name is not None:
            input_["model_name"] = model_name
        if labels_input_configuration is not None:
            input_["labels_input_configuration"] = labels_input_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if inference_data_import_strategy is not None:
            input_["inference_data_import_strategy"] = inference_data_import_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_ingestion_jobs(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        dataset_name: Optional[
            "capo_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        status: Optional[
            "capo_lookoutequipment.types.ingestion_job_status.IngestionJobStatus"
        ] = None,
    ) -> "capo_lookoutequipment.types.list_data_ingestion_jobs_response.ListDataIngestionJobsResponse":
        """<p>Provides a list of all data ingestion jobs, including dataset name and ARN, S3 location of the input data, status, and so on. </p>

        Args:
            dataset_name: <p>The name of the dataset being used for the data ingestion job. </p>
            next_token: <p>An opaque pagination token indicating where to continue the listing of data ingestion jobs. </p>
            max_results: <p> Specifies the maximum number of data ingestion jobs to list. </p>
            status: <p>Indicates the status of the data ingestion job. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_data_ingestion_jobs_request.ListDataIngestionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_data_ingestion_jobs_response.ListDataIngestionJobsResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_data_ingestion_jobs

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_data_ingestion_jobs.async_list_data_ingestion_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_data_ingestion_jobs_request.ListDataIngestionJobsRequest = {}
        if dataset_name is not None:
            input_["dataset_name"] = dataset_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_data_ingestion_jobs(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        dataset_name: Optional[
            "capo_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        status: Optional[
            "capo_lookoutequipment.types.ingestion_job_status.IngestionJobStatus"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_data_ingestion_jobs_response.ListDataIngestionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_data_ingestion_jobs(
                config_overrides=config_overrides,
                dataset_name=dataset_name,
                next_token=_token,
                max_results=max_results,
                status=status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        dataset_name_begins_with: Optional[
            "capo_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
    ) -> "capo_lookoutequipment.types.list_datasets_response.ListDatasetsResponse":
        """<p>Lists all datasets currently available in your account, filtering on the dataset name. </p>

        Args:
            next_token: <p> An opaque pagination token indicating where to continue the listing of datasets. </p>
            max_results: <p> Specifies the maximum number of datasets to list. </p>
            dataset_name_begins_with: <p>The beginning of the name of the datasets to be listed. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_datasets_request.ListDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_datasets

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_datasets_request.ListDatasetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if dataset_name_begins_with is not None:
            input_["dataset_name_begins_with"] = dataset_name_begins_with

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
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        dataset_name_begins_with: Optional[
            "capo_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_datasets_response.ListDatasetsResponse]":
        _token = next_token
        while True:
            _response = await self.list_datasets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                dataset_name_begins_with=dataset_name_begins_with,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_inference_events(
        self,
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        interval_start_time: "capo_lookoutequipment.types.timestamp.Timestamp",
        interval_end_time: "capo_lookoutequipment.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_lookoutequipment.types.list_inference_events_response.ListInferenceEventsResponse":
        """<p> Lists all inference events that have been found for the specified inference scheduler. </p>

        Args:
            next_token: <p>An opaque pagination token indicating where to continue the listing of inference events.</p>
            max_results: <p>Specifies the maximum number of inference events to list. </p>
            inference_scheduler_name: <p>The name of the inference scheduler for the inference events listed. </p>
            interval_start_time: <p> Lookout for Equipment will return all the inference events with an end time equal to or greater than the start time given.</p>
            interval_end_time: <p>Returns all the inference events with an end start time equal to or greater than less than the end time given.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_inference_events_request.ListInferenceEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_inference_events_response.ListInferenceEventsResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_events

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_events.async_list_inference_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_inference_events_request.ListInferenceEventsRequest = {
            "inference_scheduler_name": inference_scheduler_name,
            "interval_start_time": interval_start_time,
            "interval_end_time": interval_end_time,
        }
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

    async def iter_list_inference_events(
        self,
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        interval_start_time: "capo_lookoutequipment.types.timestamp.Timestamp",
        interval_end_time: "capo_lookoutequipment.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_inference_events_response.ListInferenceEventsResponse]":
        _token = next_token
        while True:
            _response = await self.list_inference_events(
                inference_scheduler_name,
                interval_start_time,
                interval_end_time,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_inference_executions(
        self,
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        data_start_time_after: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        data_end_time_before: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        status: Optional[
            "capo_lookoutequipment.types.inference_execution_status.InferenceExecutionStatus"
        ] = None,
    ) -> "capo_lookoutequipment.types.list_inference_executions_response.ListInferenceExecutionsResponse":
        """<p> Lists all inference executions that have been performed by the specified inference scheduler. </p>

        Args:
            next_token: <p>An opaque pagination token indicating where to continue the listing of inference executions.</p>
            max_results: <p>Specifies the maximum number of inference executions to list. </p>
            inference_scheduler_name: <p>The name of the inference scheduler for the inference execution listed. </p>
            data_start_time_after: <p>The time reference in the inferenced dataset after which Amazon Lookout for Equipment started the inference execution. </p>
            data_end_time_before: <p>The time reference in the inferenced dataset before which Amazon Lookout for Equipment stopped the inference execution. </p>
            status: <p>The status of the inference execution. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_inference_executions_request.ListInferenceExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_inference_executions_response.ListInferenceExecutionsResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_executions

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_executions.async_list_inference_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_inference_executions_request.ListInferenceExecutionsRequest = {
            "inference_scheduler_name": inference_scheduler_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if data_start_time_after is not None:
            input_["data_start_time_after"] = data_start_time_after
        if data_end_time_before is not None:
            input_["data_end_time_before"] = data_end_time_before
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_inference_executions(
        self,
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        data_start_time_after: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        data_end_time_before: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        status: Optional[
            "capo_lookoutequipment.types.inference_execution_status.InferenceExecutionStatus"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_inference_executions_response.ListInferenceExecutionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_inference_executions(
                inference_scheduler_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                data_start_time_after=data_start_time_after,
                data_end_time_before=data_end_time_before,
                status=status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_inference_schedulers(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        inference_scheduler_name_begins_with: Optional[
            "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
        ] = None,
        model_name: Optional["capo_lookoutequipment.types.model_name.ModelName"] = None,
        status: Optional[
            "capo_lookoutequipment.types.inference_scheduler_status.InferenceSchedulerStatus"
        ] = None,
    ) -> "capo_lookoutequipment.types.list_inference_schedulers_response.ListInferenceSchedulersResponse":
        """<p>Retrieves a list of all inference schedulers currently available for your account. </p>

        Args:
            next_token: <p> An opaque pagination token indicating where to continue the listing of inference schedulers. </p>
            max_results: <p> Specifies the maximum number of inference schedulers to list. </p>
            inference_scheduler_name_begins_with: <p>The beginning of the name of the inference schedulers to be listed. </p>
            model_name: <p>The name of the machine learning model used by the inference scheduler to be listed. </p>
            status: <p>Specifies the current status of the inference schedulers.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_inference_schedulers_request.ListInferenceSchedulersRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_inference_schedulers_response.ListInferenceSchedulersResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_schedulers

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_schedulers.async_list_inference_schedulers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_inference_schedulers_request.ListInferenceSchedulersRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if inference_scheduler_name_begins_with is not None:
            input_["inference_scheduler_name_begins_with"] = (
                inference_scheduler_name_begins_with
            )
        if model_name is not None:
            input_["model_name"] = model_name
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_inference_schedulers(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        inference_scheduler_name_begins_with: Optional[
            "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
        ] = None,
        model_name: Optional["capo_lookoutequipment.types.model_name.ModelName"] = None,
        status: Optional[
            "capo_lookoutequipment.types.inference_scheduler_status.InferenceSchedulerStatus"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_inference_schedulers_response.ListInferenceSchedulersResponse]":
        _token = next_token
        while True:
            _response = await self.list_inference_schedulers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                inference_scheduler_name_begins_with=inference_scheduler_name_begins_with,
                model_name=model_name,
                status=status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_label_groups(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        label_group_name_begins_with: Optional[
            "capo_lookoutequipment.types.label_group_name.LabelGroupName"
        ] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "capo_lookoutequipment.types.list_label_groups_response.ListLabelGroupsResponse"
    ):
        """<p> Returns a list of the label groups. </p>

        Args:
            label_group_name_begins_with: <p> The beginning of the name of the label groups to be listed. </p>
            next_token: <p> An opaque pagination token indicating where to continue the listing of label groups. </p>
            max_results: <p> Specifies the maximum number of label groups to list. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_label_groups_request.ListLabelGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_label_groups_response.ListLabelGroupsResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_label_groups

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_label_groups.async_list_label_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_label_groups_request.ListLabelGroupsRequest = {}
        if label_group_name_begins_with is not None:
            input_["label_group_name_begins_with"] = label_group_name_begins_with
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

    async def iter_list_label_groups(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        label_group_name_begins_with: Optional[
            "capo_lookoutequipment.types.label_group_name.LabelGroupName"
        ] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_label_groups_response.ListLabelGroupsResponse]":
        _token = next_token
        while True:
            _response = await self.list_label_groups(
                config_overrides=config_overrides,
                label_group_name_begins_with=label_group_name_begins_with,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_labels(
        self,
        label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        interval_start_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        interval_end_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        fault_code: Optional["capo_lookoutequipment.types.fault_code.FaultCode"] = None,
        equipment: Optional["capo_lookoutequipment.types.equipment.Equipment"] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_lookoutequipment.types.list_labels_response.ListLabelsResponse":
        """<p> Provides a list of labels. </p>

        Args:
            label_group_name: <p> Returns the name of the label group. </p>
            interval_start_time: <p> Returns all the labels with a end time equal to or later than the start time given. </p>
            interval_end_time: <p> Returns all labels with a start time earlier than the end time given. </p>
            fault_code: <p> Returns labels with a particular fault code. </p>
            equipment: <p> Lists the labels that pertain to a particular piece of equipment. </p>
            next_token: <p> An opaque pagination token indicating where to continue the listing of label groups. </p>
            max_results: <p> Specifies the maximum number of labels to list. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_labels_request.ListLabelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_labels_response.ListLabelsResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_labels

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_labels.async_list_labels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_labels_request.ListLabelsRequest = {
            "label_group_name": label_group_name
        }
        if interval_start_time is not None:
            input_["interval_start_time"] = interval_start_time
        if interval_end_time is not None:
            input_["interval_end_time"] = interval_end_time
        if fault_code is not None:
            input_["fault_code"] = fault_code
        if equipment is not None:
            input_["equipment"] = equipment
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

    async def iter_list_labels(
        self,
        label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        interval_start_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        interval_end_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        fault_code: Optional["capo_lookoutequipment.types.fault_code.FaultCode"] = None,
        equipment: Optional["capo_lookoutequipment.types.equipment.Equipment"] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_labels_response.ListLabelsResponse]":
        _token = next_token
        while True:
            _response = await self.list_labels(
                label_group_name,
                config_overrides=config_overrides,
                interval_start_time=interval_start_time,
                interval_end_time=interval_end_time,
                fault_code=fault_code,
                equipment=equipment,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_models(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_lookoutequipment.types.model_status.ModelStatus"] = None,
        model_name_begins_with: Optional[
            "capo_lookoutequipment.types.model_name.ModelName"
        ] = None,
        dataset_name_begins_with: Optional[
            "capo_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
    ) -> "capo_lookoutequipment.types.list_models_response.ListModelsResponse":
        """<p>Generates a list of all models in the account, including model name and ARN, dataset, and status. </p>

        Args:
            next_token: <p> An opaque pagination token indicating where to continue the listing of machine learning models. </p>
            max_results: <p> Specifies the maximum number of machine learning models to list. </p>
            status: <p>The status of the machine learning model. </p>
            model_name_begins_with: <p>The beginning of the name of the machine learning models being listed. </p>
            dataset_name_begins_with: <p>The beginning of the name of the dataset of the machine learning models to be listed. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_models_request.ListModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_models_response.ListModelsResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_models

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_models.async_list_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_models_request.ListModelsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if model_name_begins_with is not None:
            input_["model_name_begins_with"] = model_name_begins_with
        if dataset_name_begins_with is not None:
            input_["dataset_name_begins_with"] = dataset_name_begins_with

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_models(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_lookoutequipment.types.model_status.ModelStatus"] = None,
        model_name_begins_with: Optional[
            "capo_lookoutequipment.types.model_name.ModelName"
        ] = None,
        dataset_name_begins_with: Optional[
            "capo_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_models_response.ListModelsResponse]":
        _token = next_token
        while True:
            _response = await self.list_models(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
                model_name_begins_with=model_name_begins_with,
                dataset_name_begins_with=dataset_name_begins_with,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_model_versions(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        status: Optional[
            "capo_lookoutequipment.types.model_version_status.ModelVersionStatus"
        ] = None,
        source_type: Optional[
            "capo_lookoutequipment.types.model_version_source_type.ModelVersionSourceType"
        ] = None,
        created_at_end_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        created_at_start_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        max_model_version: Optional[
            "capo_lookoutequipment.types.model_version.ModelVersion"
        ] = None,
        min_model_version: Optional[
            "capo_lookoutequipment.types.model_version.ModelVersion"
        ] = None,
    ) -> "capo_lookoutequipment.types.list_model_versions_response.ListModelVersionsResponse":
        """<p>Generates a list of all model versions for a given model, including the model version, model version ARN, and status. To list a subset of versions, use the <code>MaxModelVersion</code> and <code>MinModelVersion</code> fields.</p>

        Args:
            model_name: <p>Then name of the machine learning model for which the model versions are to be listed.</p>
            next_token: <p>If the total number of results exceeds the limit that the response can display, the response returns an opaque pagination token indicating where to continue the listing of machine learning model versions. Use this token in the <code>NextToken</code> field in the request to list the next page of results.</p>
            max_results: <p>Specifies the maximum number of machine learning model versions to list.</p>
            status: <p>Filter the results based on the current status of the model version.</p>
            source_type: <p>Filter the results based on the way the model version was generated.</p>
            created_at_end_time: <p>Filter results to return all the model versions created before this time.</p>
            created_at_start_time: <p>Filter results to return all the model versions created after this time.</p>
            max_model_version: <p>Specifies the highest version of the model to return in the list.</p>
            min_model_version: <p>Specifies the lowest version of the model to return in the list.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_model_versions_request.ListModelVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_model_versions_response.ListModelVersionsResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_model_versions

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_model_versions.async_list_model_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_model_versions_request.ListModelVersionsRequest = {
            "model_name": model_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if source_type is not None:
            input_["source_type"] = source_type
        if created_at_end_time is not None:
            input_["created_at_end_time"] = created_at_end_time
        if created_at_start_time is not None:
            input_["created_at_start_time"] = created_at_start_time
        if max_model_version is not None:
            input_["max_model_version"] = max_model_version
        if min_model_version is not None:
            input_["min_model_version"] = min_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_model_versions(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        status: Optional[
            "capo_lookoutequipment.types.model_version_status.ModelVersionStatus"
        ] = None,
        source_type: Optional[
            "capo_lookoutequipment.types.model_version_source_type.ModelVersionSourceType"
        ] = None,
        created_at_end_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        created_at_start_time: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        max_model_version: Optional[
            "capo_lookoutequipment.types.model_version.ModelVersion"
        ] = None,
        min_model_version: Optional[
            "capo_lookoutequipment.types.model_version.ModelVersion"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_model_versions_response.ListModelVersionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_model_versions(
                model_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
                source_type=source_type,
                created_at_end_time=created_at_end_time,
                created_at_start_time=created_at_start_time,
                max_model_version=max_model_version,
                min_model_version=min_model_version,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_retraining_schedulers(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        model_name_begins_with: Optional[
            "capo_lookoutequipment.types.model_name.ModelName"
        ] = None,
        status: Optional[
            "capo_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
        ] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_lookoutequipment.types.list_retraining_schedulers_response.ListRetrainingSchedulersResponse":
        """<p>Lists all retraining schedulers in your account, filtering by model name prefix and status. </p>

        Args:
            model_name_begins_with: <p>Specify this field to only list retraining schedulers whose machine learning models begin with the value you specify. </p>
            status: <p>Specify this field to only list retraining schedulers whose status matches the value you specify. </p>
            next_token: <p>If the number of results exceeds the maximum, a pagination token is returned. Use the token in the request to show the next page of retraining schedulers.</p>
            max_results: <p>Specifies the maximum number of retraining schedulers to list. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Listing retraining schedulers

            >>> await client.list_retraining_schedulers(max_results=50)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_retraining_schedulers_request.ListRetrainingSchedulersRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_retraining_schedulers_response.ListRetrainingSchedulersResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_retraining_schedulers

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_retraining_schedulers.async_list_retraining_schedulers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_retraining_schedulers_request.ListRetrainingSchedulersRequest = {}
        if model_name_begins_with is not None:
            input_["model_name_begins_with"] = model_name_begins_with
        if status is not None:
            input_["status"] = status
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

    async def iter_list_retraining_schedulers(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        model_name_begins_with: Optional[
            "capo_lookoutequipment.types.model_name.ModelName"
        ] = None,
        status: Optional[
            "capo_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
        ] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_retraining_schedulers_response.ListRetrainingSchedulersResponse]":
        _token = next_token
        while True:
            _response = await self.list_retraining_schedulers(
                config_overrides=config_overrides,
                model_name_begins_with=model_name_begins_with,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sensor_statistics(
        self,
        dataset_name: "capo_lookoutequipment.types.dataset_name.DatasetName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        ingestion_job_id: Optional[
            "capo_lookoutequipment.types.ingestion_job_id.IngestionJobId"
        ] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
    ) -> "capo_lookoutequipment.types.list_sensor_statistics_response.ListSensorStatisticsResponse":
        """<p> Lists statistics about the data collected for each of the sensors that have been successfully ingested in the particular dataset. Can also be used to retreive Sensor Statistics for a previous ingestion job. </p>

        Args:
            dataset_name: <p> The name of the dataset associated with the list of Sensor Statistics. </p>
            ingestion_job_id: <p> The ingestion job id associated with the list of Sensor Statistics. To get sensor statistics for a particular ingestion job id, both dataset name and ingestion job id must be submitted as inputs. </p>
            max_results: <p>Specifies the maximum number of sensors for which to retrieve statistics. </p>
            next_token: <p>An opaque pagination token indicating where to continue the listing of sensor statistics. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_sensor_statistics_request.ListSensorStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_sensor_statistics_response.ListSensorStatisticsResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_sensor_statistics

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_sensor_statistics.async_list_sensor_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_sensor_statistics_request.ListSensorStatisticsRequest = {
            "dataset_name": dataset_name
        }
        if ingestion_job_id is not None:
            input_["ingestion_job_id"] = ingestion_job_id
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

    async def iter_list_sensor_statistics(
        self,
        dataset_name: "capo_lookoutequipment.types.dataset_name.DatasetName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        ingestion_job_id: Optional[
            "capo_lookoutequipment.types.ingestion_job_id.IngestionJobId"
        ] = None,
        max_results: Optional[
            "capo_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_lookoutequipment.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lookoutequipment.types.list_sensor_statistics_response.ListSensorStatisticsResponse]":
        _token = next_token
        while True:
            _response = await self.list_sensor_statistics(
                dataset_name,
                config_overrides=config_overrides,
                ingestion_job_id=ingestion_job_id,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all the tags for a specified resource, including key and value. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource (such as the dataset or model) that is the focus of the <code>ListTagsForResource</code> operation. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "capo_lookoutequipment.types.resource_arn.ResourceArn",
        resource_policy: "capo_lookoutequipment.types.policy.Policy",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        policy_revision_id: Optional[
            "capo_lookoutequipment.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_lookoutequipment.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates a resource control policy for a given resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which the policy is being created.</p>
            resource_policy: <p>The JSON-formatted resource policy to create.</p>
            policy_revision_id: <p>A unique identifier for a revision of the resource policy.</p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "resource_policy": resource_policy,
            "client_token": client_token,
        }
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_data_ingestion_job(
        self,
        dataset_name: "capo_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        ingestion_input_configuration: "capo_lookoutequipment.types.ingestion_input_configuration.IngestionInputConfiguration",
        role_arn: "capo_lookoutequipment.types.iam_role_arn.IamRoleArn",
        client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.start_data_ingestion_job_response.StartDataIngestionJobResponse":
        """<p>Starts a data ingestion job. Amazon Lookout for Equipment returns the job status. </p>

        Args:
            dataset_name: <p>The name of the dataset being used by the data ingestion job. </p>
            ingestion_input_configuration: <p> Specifies information for the input data for the data ingestion job, including dataset S3 location. </p>
            role_arn: <p> The Amazon Resource Name (ARN) of a role with permission to access the data source for the data ingestion job. </p>
            client_token: <p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.start_data_ingestion_job_request.StartDataIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.start_data_ingestion_job_response.StartDataIngestionJobResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_data_ingestion_job

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_data_ingestion_job.async_start_data_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.start_data_ingestion_job_request.StartDataIngestionJobRequest = {
            "dataset_name": dataset_name,
            "ingestion_input_configuration": ingestion_input_configuration,
            "role_arn": role_arn,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_inference_scheduler(
        self,
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.start_inference_scheduler_response.StartInferenceSchedulerResponse":
        """<p>Starts an inference scheduler. </p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler to be started. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.start_inference_scheduler_request.StartInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.start_inference_scheduler_response.StartInferenceSchedulerResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_inference_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_inference_scheduler.async_start_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.start_inference_scheduler_request.StartInferenceSchedulerRequest = {
            "inference_scheduler_name": inference_scheduler_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_retraining_scheduler(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.start_retraining_scheduler_response.StartRetrainingSchedulerResponse":
        """<p>Starts a retraining scheduler. </p>

        Args:
            model_name: <p>The name of the model whose retraining scheduler you want to start.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Starts a retraining scheduler

            >>> await client.start_retraining_scheduler(model_name='sample-model')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.start_retraining_scheduler_request.StartRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.start_retraining_scheduler_response.StartRetrainingSchedulerResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_retraining_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_retraining_scheduler.async_start_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.start_retraining_scheduler_request.StartRetrainingSchedulerRequest = {
            "model_name": model_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_inference_scheduler(
        self,
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.stop_inference_scheduler_response.StopInferenceSchedulerResponse":
        """<p>Stops an inference scheduler. </p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler to be stopped. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.stop_inference_scheduler_request.StopInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.stop_inference_scheduler_response.StopInferenceSchedulerResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.stop_inference_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.stop_inference_scheduler.async_stop_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.stop_inference_scheduler_request.StopInferenceSchedulerRequest = {
            "inference_scheduler_name": inference_scheduler_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_retraining_scheduler(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.stop_retraining_scheduler_response.StopRetrainingSchedulerResponse":
        """<p>Stops a retraining scheduler. </p>

        Args:
            model_name: <p>The name of the model whose retraining scheduler you want to stop.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Stops a retraining scheduler

            >>> await client.stop_retraining_scheduler(model_name='sample-model')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.stop_retraining_scheduler_request.StopRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.stop_retraining_scheduler_response.StopRetrainingSchedulerResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.stop_retraining_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.stop_retraining_scheduler.async_stop_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.stop_retraining_scheduler_request.StopRetrainingSchedulerRequest = {
            "model_name": model_name
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
        resource_arn: "capo_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn",
        tags: "capo_lookoutequipment.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.tag_resource_response.TagResourceResponse":
        """<p>Associates a given tag to a resource in your account. A tag is a key-value pair which can be added to an Amazon Lookout for Equipment resource as metadata. Tags can be used for organizing your resources as well as helping you to search and filter by tag. Multiple tags can be added to a resource, either when you create it, or later. Up to 50 tags can be associated with each resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the specific resource to which the tag should be associated. </p>
            tags: <p>The tag or tags to be associated with a specific resource. Both the tag key and value are specified. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Resource limitations have been exceeded. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn",
        tag_keys: "capo_lookoutequipment.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a specific tag from a given resource. The tag is specified by its key. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which the tag is currently associated. </p>
            tag_keys: <p>Specifies the key of the tag to be removed from a specified resource. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_active_model_version(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        model_version: "capo_lookoutequipment.types.model_version.ModelVersion",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "capo_lookoutequipment.types.update_active_model_version_response.UpdateActiveModelVersionResponse":
        """<p>Sets the active model version for a given machine learning model.</p>

        Args:
            model_name: <p>The name of the machine learning model for which the active model version is being set.</p>
            model_version: <p>The version of the machine learning model for which the active model version is being set.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.update_active_model_version_request.UpdateActiveModelVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lookoutequipment.types.update_active_model_version_response.UpdateActiveModelVersionResponse"
        ]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_active_model_version

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_active_model_version.async_update_active_model_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.update_active_model_version_request.UpdateActiveModelVersionRequest = {
            "model_name": model_name,
            "model_version": model_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_inference_scheduler(
        self,
        inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        data_delay_offset_in_minutes: Optional[
            "capo_lookoutequipment.types.data_delay_offset_in_minutes.DataDelayOffsetInMinutes"
        ] = None,
        data_upload_frequency: Optional[
            "capo_lookoutequipment.types.data_upload_frequency.DataUploadFrequency"
        ] = None,
        data_input_configuration: Optional[
            "capo_lookoutequipment.types.inference_input_configuration.InferenceInputConfiguration"
        ] = None,
        data_output_configuration: Optional[
            "capo_lookoutequipment.types.inference_output_configuration.InferenceOutputConfiguration"
        ] = None,
        role_arn: Optional[
            "capo_lookoutequipment.types.iam_role_arn.IamRoleArn"
        ] = None,
    ) -> None:
        """<p>Updates an inference scheduler. </p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler to be updated. </p>
            data_delay_offset_in_minutes: <p> A period of time (in minutes) by which inference on the data is delayed after the data starts. For instance, if you select an offset delay time of five minutes, inference will not begin on the data until the first data measurement after the five minute mark. For example, if five minutes is selected, the inference scheduler will wake up at the configured frequency with the additional five minute delay time to check the customer S3 bucket. The customer can upload data at the same frequency and they don't need to stop and restart the scheduler when uploading new data.</p>
            data_upload_frequency: <p>How often data is uploaded to the source S3 bucket for the input data. The value chosen is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on your data. In this example, it starts once every 5 minutes. </p>
            data_input_configuration: <p> Specifies information for the input data for the inference scheduler, including delimiter, format, and dataset location. </p>
            data_output_configuration: <p> Specifies information for the output results from the inference scheduler, including the output S3 location. </p>
            role_arn: <p> The Amazon Resource Name (ARN) of a role with permission to access the data source for the inference scheduler. </p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.update_inference_scheduler_request.UpdateInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_inference_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_inference_scheduler.async_update_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.update_inference_scheduler_request.UpdateInferenceSchedulerRequest = {
            "inference_scheduler_name": inference_scheduler_name
        }
        if data_delay_offset_in_minutes is not None:
            input_["data_delay_offset_in_minutes"] = data_delay_offset_in_minutes
        if data_upload_frequency is not None:
            input_["data_upload_frequency"] = data_upload_frequency
        if data_input_configuration is not None:
            input_["data_input_configuration"] = data_input_configuration
        if data_output_configuration is not None:
            input_["data_output_configuration"] = data_output_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_label_group(
        self,
        label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        fault_codes: Optional[
            "capo_lookoutequipment.types.fault_codes.FaultCodes"
        ] = None,
    ) -> None:
        """<p> Updates the label group. </p>

        Args:
            label_group_name: <p> The name of the label group to be updated. </p>
            fault_codes: <p> Updates the code indicating the type of anomaly associated with the label. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.update_label_group_request.UpdateLabelGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_label_group

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_label_group.async_update_label_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.update_label_group_request.UpdateLabelGroupRequest = {
            "label_group_name": label_group_name
        }
        if fault_codes is not None:
            input_["fault_codes"] = fault_codes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_model(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        labels_input_configuration: Optional[
            "capo_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
        ] = None,
        role_arn: Optional[
            "capo_lookoutequipment.types.iam_role_arn.IamRoleArn"
        ] = None,
        model_diagnostics_output_configuration: Optional[
            "capo_lookoutequipment.types.model_diagnostics_output_configuration.ModelDiagnosticsOutputConfiguration"
        ] = None,
    ) -> None:
        """<p>Updates a model in the account.</p>

        Args:
            model_name: <p>The name of the model to update.</p>
            role_arn: <p>The ARN of the model to update.</p>
            model_diagnostics_output_configuration: <p>The Amazon S3 location where you want Amazon Lookout for Equipment to save the pointwise model diagnostics for the model. You must also specify the <code>RoleArn</code> request parameter.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updates a model

            >>> await client.update_model(model_name='sample-model', labels_input_configuration={'LabelGroupName': 'sample-label-group'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.update_model_request.UpdateModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_model

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_model.async_update_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.update_model_request.UpdateModelRequest = {
            "model_name": model_name
        }
        if labels_input_configuration is not None:
            input_["labels_input_configuration"] = labels_input_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if model_diagnostics_output_configuration is not None:
            input_["model_diagnostics_output_configuration"] = (
                model_diagnostics_output_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_retraining_scheduler(
        self,
        model_name: "capo_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        retraining_start_date: Optional[
            "capo_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        retraining_frequency: Optional[
            "capo_lookoutequipment.types.retraining_frequency.RetrainingFrequency"
        ] = None,
        lookback_window: Optional[
            "capo_lookoutequipment.types.lookback_window.LookbackWindow"
        ] = None,
        promote_mode: Optional[
            "capo_lookoutequipment.types.model_promote_mode.ModelPromoteMode"
        ] = None,
    ) -> None:
        """<p>Updates a retraining scheduler. </p>

        Args:
            model_name: <p>The name of the model whose retraining scheduler you want to update. </p>
            retraining_start_date: <p>The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the nearest UTC day.</p>
            retraining_frequency: <p>This parameter uses the <a href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601</a> standard to set the frequency at which you want retraining to occur in terms of Years, Months, and/or Days (note: other parameters like Time are not currently supported). The minimum value is 30 days (P30D) and the maximum value is 1 year (P1Y). For example, the following values are valid:</p> <ul> <li> <p>P3M15D – Every 3 months and 15 days</p> </li> <li> <p>P2M – Every 2 months</p> </li> <li> <p>P150D – Every 150 days</p> </li> </ul>
            lookback_window: <p>The number of past days of data that will be used for retraining.</p>
            promote_mode: <p>Indicates how the service will use new models. In <code>MANAGED</code> mode, new models will automatically be used for inference if they have better performance than the current model. In <code>MANUAL</code> mode, the new models will not be used <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/versioning-model.html#model-activation">until they are manually activated</a>.</p>

        Raises:
            capo_lookoutequipment.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have access to the resource. </p>
            capo_lookoutequipment.errors.conflict_exception.ConflictException: <p> The request could not be completed due to a conflict with the current state of the target resource. </p>
            capo_lookoutequipment.errors.internal_server_exception.InternalServerException: <p> Processing of the request has failed because of an unknown error, exception or failure. </p>
            capo_lookoutequipment.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource requested could not be found. Verify the resource ID and retry your request. </p>
            capo_lookoutequipment.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_lookoutequipment.errors.validation_exception.ValidationException: <p> The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related Amazon Web Services service that's being utilized. </p>
            capo_lookoutequipment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updates a retraining scheduler

            >>> await client.update_retraining_scheduler(model_name='sample-model', retraining_start_date='2024-01-01T00:00:00Z', retraining_frequency='P1Y')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lookoutequipment.types.update_retraining_scheduler_request.UpdateRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_retraining_scheduler

            (
                output,
                http_response,
            ) = await capo_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_retraining_scheduler.async_update_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lookoutequipment.types.update_retraining_scheduler_request.UpdateRetrainingSchedulerRequest = {
            "model_name": model_name
        }
        if retraining_start_date is not None:
            input_["retraining_start_date"] = retraining_start_date
        if retraining_frequency is not None:
            input_["retraining_frequency"] = retraining_frequency
        if lookback_window is not None:
            input_["lookback_window"] = lookback_window
        if promote_mode is not None:
            input_["promote_mode"] = promote_mode

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
