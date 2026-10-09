"""Generated from Smithy shape ``com.amazonaws.frauddetector#AWSHawksNestServiceFacade``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_frauddetector._auth._signers
import capo_frauddetector._auth._sigv4
from capo_frauddetector._auth._identity import Credentials
from capo_frauddetector._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_frauddetector._auth._zapros_handler import AuthMiddleware
from capo_frauddetector._pagination import resolve_path as _resolve_path
from capo_frauddetector._services._aws_config import aws_config
from capo_frauddetector._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_frauddetector.types.batch_create_variable_request
    import capo_frauddetector.types.batch_create_variable_result
    import capo_frauddetector.types.batch_get_variable_request
    import capo_frauddetector.types.batch_get_variable_result
    import capo_frauddetector.types.batch_imports_max_page_size
    import capo_frauddetector.types.batch_predictions_max_page_size
    import capo_frauddetector.types.cancel_batch_import_job_request
    import capo_frauddetector.types.cancel_batch_import_job_result
    import capo_frauddetector.types.cancel_batch_prediction_job_request
    import capo_frauddetector.types.cancel_batch_prediction_job_result
    import capo_frauddetector.types.create_batch_import_job_request
    import capo_frauddetector.types.create_batch_import_job_result
    import capo_frauddetector.types.create_batch_prediction_job_request
    import capo_frauddetector.types.create_batch_prediction_job_result
    import capo_frauddetector.types.create_detector_version_request
    import capo_frauddetector.types.create_detector_version_result
    import capo_frauddetector.types.create_list_request
    import capo_frauddetector.types.create_list_result
    import capo_frauddetector.types.create_model_request
    import capo_frauddetector.types.create_model_result
    import capo_frauddetector.types.create_model_version_request
    import capo_frauddetector.types.create_model_version_result
    import capo_frauddetector.types.create_rule_request
    import capo_frauddetector.types.create_rule_result
    import capo_frauddetector.types.create_variable_request
    import capo_frauddetector.types.create_variable_result
    import capo_frauddetector.types.data_source
    import capo_frauddetector.types.data_type
    import capo_frauddetector.types.delete_audit_history
    import capo_frauddetector.types.delete_batch_import_job_request
    import capo_frauddetector.types.delete_batch_import_job_result
    import capo_frauddetector.types.delete_batch_prediction_job_request
    import capo_frauddetector.types.delete_batch_prediction_job_result
    import capo_frauddetector.types.delete_detector_request
    import capo_frauddetector.types.delete_detector_result
    import capo_frauddetector.types.delete_detector_version_request
    import capo_frauddetector.types.delete_detector_version_result
    import capo_frauddetector.types.delete_entity_type_request
    import capo_frauddetector.types.delete_entity_type_result
    import capo_frauddetector.types.delete_event_request
    import capo_frauddetector.types.delete_event_result
    import capo_frauddetector.types.delete_event_type_request
    import capo_frauddetector.types.delete_event_type_result
    import capo_frauddetector.types.delete_events_by_event_type_request
    import capo_frauddetector.types.delete_events_by_event_type_result
    import capo_frauddetector.types.delete_external_model_request
    import capo_frauddetector.types.delete_external_model_result
    import capo_frauddetector.types.delete_label_request
    import capo_frauddetector.types.delete_label_result
    import capo_frauddetector.types.delete_list_request
    import capo_frauddetector.types.delete_list_result
    import capo_frauddetector.types.delete_model_request
    import capo_frauddetector.types.delete_model_result
    import capo_frauddetector.types.delete_model_version_request
    import capo_frauddetector.types.delete_model_version_result
    import capo_frauddetector.types.delete_outcome_request
    import capo_frauddetector.types.delete_outcome_result
    import capo_frauddetector.types.delete_rule_request
    import capo_frauddetector.types.delete_rule_result
    import capo_frauddetector.types.delete_variable_request
    import capo_frauddetector.types.delete_variable_result
    import capo_frauddetector.types.describe_detector_request
    import capo_frauddetector.types.describe_detector_result
    import capo_frauddetector.types.describe_model_versions_request
    import capo_frauddetector.types.describe_model_versions_result
    import capo_frauddetector.types.description
    import capo_frauddetector.types.detector_version_max_results
    import capo_frauddetector.types.detector_version_status
    import capo_frauddetector.types.detectors_max_results
    import capo_frauddetector.types.elements_list
    import capo_frauddetector.types.entity_types_max_results
    import capo_frauddetector.types.event_ingestion
    import capo_frauddetector.types.event_orchestration
    import capo_frauddetector.types.event_predictions_max_results
    import capo_frauddetector.types.event_types_max_results
    import capo_frauddetector.types.event_variable_map
    import capo_frauddetector.types.external_events_detail
    import capo_frauddetector.types.external_model_endpoint_data_blob_map
    import capo_frauddetector.types.external_models_max_results
    import capo_frauddetector.types.filter_condition
    import capo_frauddetector.types.float_version_string
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.get_batch_import_jobs_request
    import capo_frauddetector.types.get_batch_import_jobs_result
    import capo_frauddetector.types.get_batch_prediction_jobs_request
    import capo_frauddetector.types.get_batch_prediction_jobs_result
    import capo_frauddetector.types.get_delete_events_by_event_type_status_request
    import capo_frauddetector.types.get_delete_events_by_event_type_status_result
    import capo_frauddetector.types.get_detector_version_request
    import capo_frauddetector.types.get_detector_version_result
    import capo_frauddetector.types.get_detectors_request
    import capo_frauddetector.types.get_detectors_result
    import capo_frauddetector.types.get_entity_types_request
    import capo_frauddetector.types.get_entity_types_result
    import capo_frauddetector.types.get_event_prediction_metadata_request
    import capo_frauddetector.types.get_event_prediction_metadata_result
    import capo_frauddetector.types.get_event_prediction_request
    import capo_frauddetector.types.get_event_prediction_result
    import capo_frauddetector.types.get_event_request
    import capo_frauddetector.types.get_event_result
    import capo_frauddetector.types.get_event_types_request
    import capo_frauddetector.types.get_event_types_result
    import capo_frauddetector.types.get_external_models_request
    import capo_frauddetector.types.get_external_models_result
    import capo_frauddetector.types.get_kms_encryption_key_result
    import capo_frauddetector.types.get_labels_request
    import capo_frauddetector.types.get_labels_result
    import capo_frauddetector.types.get_list_elements_request
    import capo_frauddetector.types.get_list_elements_result
    import capo_frauddetector.types.get_lists_metadata_request
    import capo_frauddetector.types.get_lists_metadata_result
    import capo_frauddetector.types.get_model_version_request
    import capo_frauddetector.types.get_model_version_result
    import capo_frauddetector.types.get_models_request
    import capo_frauddetector.types.get_models_result
    import capo_frauddetector.types.get_outcomes_request
    import capo_frauddetector.types.get_outcomes_result
    import capo_frauddetector.types.get_rules_request
    import capo_frauddetector.types.get_rules_result
    import capo_frauddetector.types.get_variables_request
    import capo_frauddetector.types.get_variables_result
    import capo_frauddetector.types.iam_role_arn
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.ingested_events_detail
    import capo_frauddetector.types.kms_encryption_key_arn
    import capo_frauddetector.types.labels_max_results
    import capo_frauddetector.types.language
    import capo_frauddetector.types.list_event_predictions_request
    import capo_frauddetector.types.list_event_predictions_result
    import capo_frauddetector.types.list_of_entities
    import capo_frauddetector.types.list_of_model_versions
    import capo_frauddetector.types.list_of_strings
    import capo_frauddetector.types.list_tags_for_resource_request
    import capo_frauddetector.types.list_tags_for_resource_result
    import capo_frauddetector.types.list_update_mode
    import capo_frauddetector.types.lists_elements_max_results
    import capo_frauddetector.types.lists_metadata_max_results
    import capo_frauddetector.types.model_endpoint_status
    import capo_frauddetector.types.model_identifier
    import capo_frauddetector.types.model_input_configuration
    import capo_frauddetector.types.model_output_configuration
    import capo_frauddetector.types.model_source
    import capo_frauddetector.types.model_type_enum
    import capo_frauddetector.types.model_version_status
    import capo_frauddetector.types.models_max_page_size
    import capo_frauddetector.types.name_list
    import capo_frauddetector.types.next_token
    import capo_frauddetector.types.no_dash_identifier
    import capo_frauddetector.types.non_empty_list_of_strings
    import capo_frauddetector.types.outcomes_max_results
    import capo_frauddetector.types.prediction_time_range
    import capo_frauddetector.types.put_detector_request
    import capo_frauddetector.types.put_detector_result
    import capo_frauddetector.types.put_entity_type_request
    import capo_frauddetector.types.put_entity_type_result
    import capo_frauddetector.types.put_event_type_request
    import capo_frauddetector.types.put_event_type_result
    import capo_frauddetector.types.put_external_model_request
    import capo_frauddetector.types.put_external_model_result
    import capo_frauddetector.types.put_kms_encryption_key_request
    import capo_frauddetector.types.put_kms_encryption_key_result
    import capo_frauddetector.types.put_label_request
    import capo_frauddetector.types.put_label_result
    import capo_frauddetector.types.put_outcome_request
    import capo_frauddetector.types.put_outcome_result
    import capo_frauddetector.types.rule
    import capo_frauddetector.types.rule_execution_mode
    import capo_frauddetector.types.rule_expression
    import capo_frauddetector.types.rule_list
    import capo_frauddetector.types.rules_max_results
    import capo_frauddetector.types.s3_bucket_location
    import capo_frauddetector.types.sage_maker_endpoint_identifier
    import capo_frauddetector.types.send_event_request
    import capo_frauddetector.types.send_event_result
    import capo_frauddetector.types.string
    import capo_frauddetector.types.tag_key_list
    import capo_frauddetector.types.tag_list
    import capo_frauddetector.types.tag_resource_request
    import capo_frauddetector.types.tag_resource_result
    import capo_frauddetector.types.tags_max_results
    import capo_frauddetector.types.time
    import capo_frauddetector.types.training_data_schema
    import capo_frauddetector.types.training_data_source_enum
    import capo_frauddetector.types.untag_resource_request
    import capo_frauddetector.types.untag_resource_result
    import capo_frauddetector.types.update_detector_version_metadata_request
    import capo_frauddetector.types.update_detector_version_metadata_result
    import capo_frauddetector.types.update_detector_version_request
    import capo_frauddetector.types.update_detector_version_result
    import capo_frauddetector.types.update_detector_version_status_request
    import capo_frauddetector.types.update_detector_version_status_result
    import capo_frauddetector.types.update_event_label_request
    import capo_frauddetector.types.update_event_label_result
    import capo_frauddetector.types.update_list_request
    import capo_frauddetector.types.update_list_result
    import capo_frauddetector.types.update_model_request
    import capo_frauddetector.types.update_model_result
    import capo_frauddetector.types.update_model_version_request
    import capo_frauddetector.types.update_model_version_result
    import capo_frauddetector.types.update_model_version_status_request
    import capo_frauddetector.types.update_model_version_status_result
    import capo_frauddetector.types.update_rule_metadata_request
    import capo_frauddetector.types.update_rule_metadata_result
    import capo_frauddetector.types.update_rule_version_request
    import capo_frauddetector.types.update_rule_version_result
    import capo_frauddetector.types.update_variable_request
    import capo_frauddetector.types.update_variable_result
    import capo_frauddetector.types.utc_timestamp_iso8601
    import capo_frauddetector.types.variable_entry_list
    import capo_frauddetector.types.variable_type
    import capo_frauddetector.types.variables_max_results
    import capo_frauddetector.types.whole_number_version_string


class FraudDetectorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class FraudDetectorClient:
    """A client for the ``FraudDetector`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = FraudDetectorClientConfig(
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
        self, config_overrides: Optional[FraudDetectorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: FraudDetectorClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def batch_create_variable(
        self,
        variable_entries: "capo_frauddetector.types.variable_entry_list.VariableEntryList",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.batch_create_variable_result.BatchCreateVariableResult":
        """<p>Creates a batch of variables.</p>

        Args:
            variable_entries: <p>The list of variables for the batch create variable request.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.batch_create_variable_request.BatchCreateVariableRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.batch_create_variable_result.BatchCreateVariableResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.batch_create_variable

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.batch_create_variable.batch_create_variable(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.batch_create_variable_request.BatchCreateVariableRequest = {
            "variable_entries": variable_entries
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

    def batch_get_variable(
        self,
        names: "capo_frauddetector.types.name_list.NameList",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.batch_get_variable_result.BatchGetVariableResult":
        """<p>Gets a batch of variables.</p>

        Args:
            names: <p>The list of variable names to get.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.batch_get_variable_request.BatchGetVariableRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.batch_get_variable_result.BatchGetVariableResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.batch_get_variable

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.batch_get_variable.batch_get_variable(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.batch_get_variable_request.BatchGetVariableRequest = {
            "names": names
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_batch_import_job(
        self,
        job_id: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.cancel_batch_import_job_result.CancelBatchImportJobResult":
        """<p> Cancels an in-progress batch import job.</p>

        Args:
            job_id: <p> The ID of an in-progress batch import job to cancel. </p> <p>Amazon Fraud Detector will throw an error if the batch import job is in <code>FAILED</code>, <code>CANCELED</code>, or <code>COMPLETED</code> state.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.cancel_batch_import_job_request.CancelBatchImportJobRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.cancel_batch_import_job_result.CancelBatchImportJobResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.cancel_batch_import_job

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.cancel_batch_import_job.cancel_batch_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.cancel_batch_import_job_request.CancelBatchImportJobRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_batch_prediction_job(
        self,
        job_id: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.cancel_batch_prediction_job_result.CancelBatchPredictionJobResult":
        """<p>Cancels the specified batch prediction job.</p>

        Args:
            job_id: <p>The ID of the batch prediction job to cancel.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.cancel_batch_prediction_job_request.CancelBatchPredictionJobRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.cancel_batch_prediction_job_result.CancelBatchPredictionJobResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.cancel_batch_prediction_job

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.cancel_batch_prediction_job.cancel_batch_prediction_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.cancel_batch_prediction_job_request.CancelBatchPredictionJobRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_batch_import_job(
        self,
        job_id: "capo_frauddetector.types.identifier.identifier",
        input_path: "capo_frauddetector.types.s3_bucket_location.s3BucketLocation",
        output_path: "capo_frauddetector.types.s3_bucket_location.s3BucketLocation",
        event_type_name: "capo_frauddetector.types.identifier.identifier",
        iam_role_arn: "capo_frauddetector.types.iam_role_arn.iamRoleArn",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.create_batch_import_job_result.CreateBatchImportJobResult":
        """<p>Creates a batch import job. </p>

        Args:
            job_id: <p>The ID of the batch import job. The ID cannot be of a past job, unless the job exists in <code>CREATE_FAILED</code> state.</p>
            input_path: <p>The URI that points to the Amazon S3 location of your data file.</p>
            output_path: <p>The URI that points to the Amazon S3 location for storing your results. </p>
            event_type_name: <p>The name of the event type.</p>
            iam_role_arn: <p>The ARN of the IAM role created for Amazon S3 bucket that holds your data file.</p> <p>The IAM role must have read permissions to your input S3 bucket and write permissions to your output S3 bucket. For more information about bucket permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html">User policy examples</a> in the <i>Amazon S3 User Guide</i>.</p>
            tags: <p>A collection of key-value pairs associated with this request. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.create_batch_import_job_request.CreateBatchImportJobRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.create_batch_import_job_result.CreateBatchImportJobResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.create_batch_import_job

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.create_batch_import_job.create_batch_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.create_batch_import_job_request.CreateBatchImportJobRequest = {
            "job_id": job_id,
            "input_path": input_path,
            "output_path": output_path,
            "event_type_name": event_type_name,
            "iam_role_arn": iam_role_arn,
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

    def create_batch_prediction_job(
        self,
        job_id: "capo_frauddetector.types.identifier.identifier",
        input_path: "capo_frauddetector.types.s3_bucket_location.s3BucketLocation",
        output_path: "capo_frauddetector.types.s3_bucket_location.s3BucketLocation",
        event_type_name: "capo_frauddetector.types.identifier.identifier",
        detector_name: "capo_frauddetector.types.identifier.identifier",
        iam_role_arn: "capo_frauddetector.types.iam_role_arn.iamRoleArn",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        detector_version: Optional[
            "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.create_batch_prediction_job_result.CreateBatchPredictionJobResult":
        """<p>Creates a batch prediction job.</p>

        Args:
            job_id: <p>The ID of the batch prediction job.</p>
            input_path: <p>The Amazon S3 location of your training file.</p>
            output_path: <p>The Amazon S3 location of your output file.</p>
            event_type_name: <p>The name of the event type.</p>
            detector_name: <p>The name of the detector.</p>
            detector_version: <p>The detector version.</p>
            iam_role_arn: <p>The ARN of the IAM role to use for this job request.</p> <p>The IAM Role must have read permissions to your input S3 bucket and write permissions to your output S3 bucket. For more information about bucket permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html">User policy examples</a> in the <i>Amazon S3 User Guide</i>.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.create_batch_prediction_job_request.CreateBatchPredictionJobRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.create_batch_prediction_job_result.CreateBatchPredictionJobResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.create_batch_prediction_job

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.create_batch_prediction_job.create_batch_prediction_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.create_batch_prediction_job_request.CreateBatchPredictionJobRequest = {
            "job_id": job_id,
            "input_path": input_path,
            "output_path": output_path,
            "event_type_name": event_type_name,
            "detector_name": detector_name,
            "iam_role_arn": iam_role_arn,
        }
        if detector_version is not None:
            input_["detector_version"] = detector_version
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_detector_version(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        rules: "capo_frauddetector.types.rule_list.RuleList",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        external_model_endpoints: Optional[
            "capo_frauddetector.types.list_of_strings.ListOfStrings"
        ] = None,
        model_versions: Optional[
            "capo_frauddetector.types.list_of_model_versions.ListOfModelVersions"
        ] = None,
        rule_execution_mode: Optional[
            "capo_frauddetector.types.rule_execution_mode.RuleExecutionMode"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.create_detector_version_result.CreateDetectorVersionResult":
        """<p>Creates a detector version. The detector version starts in a <code>DRAFT</code> status.</p>

        Args:
            detector_id: <p>The ID of the detector under which you want to create a new version.</p>
            description: <p>The description of the detector version.</p>
            external_model_endpoints: <p>The Amazon Sagemaker model endpoints to include in the detector version.</p>
            rules: <p>The rules to include in the detector version.</p>
            model_versions: <p>The model versions to include in the detector version.</p>
            rule_execution_mode: <p>The rule execution mode for the rules included in the detector version.</p> <p>You can define and edit the rule mode at the detector version level, when it is in draft status.</p> <p>If you specify <code>FIRST_MATCHED</code>, Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.</p> <p>If you specifiy <code>ALL_MATCHED</code>, Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules. </p> <p>The default behavior is <code>FIRST_MATCHED</code>.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.create_detector_version_request.CreateDetectorVersionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.create_detector_version_result.CreateDetectorVersionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.create_detector_version

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.create_detector_version.create_detector_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.create_detector_version_request.CreateDetectorVersionRequest = {
            "detector_id": detector_id,
            "rules": rules,
        }
        if description is not None:
            input_["description"] = description
        if external_model_endpoints is not None:
            input_["external_model_endpoints"] = external_model_endpoints
        if model_versions is not None:
            input_["model_versions"] = model_versions
        if rule_execution_mode is not None:
            input_["rule_execution_mode"] = rule_execution_mode
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_list(
        self,
        name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        elements: Optional[
            "capo_frauddetector.types.elements_list.ElementsList"
        ] = None,
        variable_type: Optional[
            "capo_frauddetector.types.variable_type.variableType"
        ] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.create_list_result.CreateListResult":
        """<p> Creates a list. </p> <p>List is a set of input data for a variable in your event dataset. You use the input data in a rule that's associated with your detector. For more information, see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/lists.html">Lists</a>.</p>

        Args:
            name: <p> The name of the list. </p>
            elements: <p> The names of the elements, if providing. You can also create an empty list and add elements later using the <a href="https://docs.aws.amazon.com/frauddetector/latest/api/API_Updatelist.html">UpdateList</a> API. </p>
            variable_type: <p> The variable type of the list. You can only assign the variable type with String data type. For more information, see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types">Variable types</a>. </p>
            description: <p> The description of the list. </p>
            tags: <p> A collection of the key and value pairs. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.create_list_request.CreateListRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.create_list_result.CreateListResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.create_list

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.create_list.create_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.create_list_request.CreateListRequest = {
            "name": name
        }
        if elements is not None:
            input_["elements"] = elements
        if variable_type is not None:
            input_["variable_type"] = variable_type
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_model(
        self,
        model_id: "capo_frauddetector.types.model_identifier.modelIdentifier",
        model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum",
        event_type_name: "capo_frauddetector.types.string.string",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.create_model_result.CreateModelResult":
        """<p>Creates a model using the specified model type.</p>

        Args:
            model_id: <p>The model ID.</p>
            model_type: <p>The model type. </p>
            description: <p>The model description. </p>
            event_type_name: <p>The name of the event type.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.create_model_request.CreateModelRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.create_model_result.CreateModelResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.create_model

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.create_model.create_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.create_model_request.CreateModelRequest = {
            "model_id": model_id,
            "model_type": model_type,
            "event_type_name": event_type_name,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_model_version(
        self,
        model_id: "capo_frauddetector.types.model_identifier.modelIdentifier",
        model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum",
        training_data_source: "capo_frauddetector.types.training_data_source_enum.TrainingDataSourceEnum",
        training_data_schema: "capo_frauddetector.types.training_data_schema.TrainingDataSchema",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        external_events_detail: Optional[
            "capo_frauddetector.types.external_events_detail.ExternalEventsDetail"
        ] = None,
        ingested_events_detail: Optional[
            "capo_frauddetector.types.ingested_events_detail.IngestedEventsDetail"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> (
        "capo_frauddetector.types.create_model_version_result.CreateModelVersionResult"
    ):
        """<p>Creates a version of the model using the specified model type and model id. </p>

        Args:
            model_id: <p>The model ID. </p>
            model_type: <p>The model type.</p>
            training_data_source: <p>The training data source location in Amazon S3. </p>
            training_data_schema: <p>The training data schema.</p>
            external_events_detail: <p>Details of the external events data used for model version training. Required if <code>trainingDataSource</code> is <code>EXTERNAL_EVENTS</code>.</p>
            ingested_events_detail: <p>Details of the ingested events data used for model version training. Required if <code>trainingDataSource</code> is <code>INGESTED_EVENTS</code>.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.create_model_version_request.CreateModelVersionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.create_model_version_result.CreateModelVersionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.create_model_version

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.create_model_version.create_model_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.create_model_version_request.CreateModelVersionRequest = {
            "model_id": model_id,
            "model_type": model_type,
            "training_data_source": training_data_source,
            "training_data_schema": training_data_schema,
        }
        if external_events_detail is not None:
            input_["external_events_detail"] = external_events_detail
        if ingested_events_detail is not None:
            input_["ingested_events_detail"] = ingested_events_detail
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_rule(
        self,
        rule_id: "capo_frauddetector.types.identifier.identifier",
        detector_id: "capo_frauddetector.types.identifier.identifier",
        expression: "capo_frauddetector.types.rule_expression.ruleExpression",
        language: "capo_frauddetector.types.language.Language",
        outcomes: "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.create_rule_result.CreateRuleResult":
        """<p>Creates a rule for use with the specified detector. </p>

        Args:
            rule_id: <p>The rule ID.</p>
            detector_id: <p>The detector ID for the rule's parent detector.</p>
            description: <p>The rule description.</p>
            expression: <p>The rule expression.</p>
            language: <p>The language of the rule.</p>
            outcomes: <p>The outcome or outcomes returned when the rule expression matches.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.create_rule_request.CreateRuleRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.create_rule_result.CreateRuleResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.create_rule

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.create_rule.create_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.create_rule_request.CreateRuleRequest = {
            "rule_id": rule_id,
            "detector_id": detector_id,
            "expression": expression,
            "language": language,
            "outcomes": outcomes,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_variable(
        self,
        name: "capo_frauddetector.types.string.string",
        data_type: "capo_frauddetector.types.data_type.DataType",
        data_source: "capo_frauddetector.types.data_source.DataSource",
        default_value: "capo_frauddetector.types.string.string",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional["capo_frauddetector.types.string.string"] = None,
        variable_type: Optional["capo_frauddetector.types.string.string"] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.create_variable_result.CreateVariableResult":
        """<p>Creates a variable.</p>

        Args:
            name: <p>The name of the variable.</p>
            data_type: <p>The data type of the variable.</p>
            data_source: <p>The source of the data.</p>
            default_value: <p>The default value for the variable when no value is received.</p>
            description: <p>The description.</p>
            variable_type: <p>The variable type. For more information see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types">Variable types</a>. </p> <p>Valid Values: <code>AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT</code> </p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.create_variable_request.CreateVariableRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.create_variable_result.CreateVariableResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.create_variable

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.create_variable.create_variable(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.create_variable_request.CreateVariableRequest = {
            "name": name,
            "data_type": data_type,
            "data_source": data_source,
            "default_value": default_value,
        }
        if description is not None:
            input_["description"] = description
        if variable_type is not None:
            input_["variable_type"] = variable_type
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_batch_import_job(
        self,
        job_id: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_batch_import_job_result.DeleteBatchImportJobResult":
        """<p>Deletes the specified batch import job ID record. This action does not delete the data that was batch imported. </p>

        Args:
            job_id: <p>The ID of the batch import job to delete. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_batch_import_job_request.DeleteBatchImportJobRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_batch_import_job_result.DeleteBatchImportJobResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_batch_import_job

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_batch_import_job.delete_batch_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_batch_import_job_request.DeleteBatchImportJobRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_batch_prediction_job(
        self,
        job_id: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_batch_prediction_job_result.DeleteBatchPredictionJobResult":
        """<p>Deletes a batch prediction job.</p>

        Args:
            job_id: <p>The ID of the batch prediction job to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_batch_prediction_job_request.DeleteBatchPredictionJobRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_batch_prediction_job_result.DeleteBatchPredictionJobResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_batch_prediction_job

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_batch_prediction_job.delete_batch_prediction_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_batch_prediction_job_request.DeleteBatchPredictionJobRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_detector(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_detector_result.DeleteDetectorResult":
        """<p>Deletes the detector. Before deleting a detector, you must first delete all detector versions and rule versions associated with the detector.</p> <p>When you delete a detector, Amazon Fraud Detector permanently deletes the detector and the data is no longer stored in Amazon Fraud Detector.</p>

        Args:
            detector_id: <p>The ID of the detector to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_detector_request.DeleteDetectorRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_detector_result.DeleteDetectorResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_detector

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_detector.delete_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_detector_request.DeleteDetectorRequest = {
            "detector_id": detector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_detector_version(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        detector_version_id: "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_detector_version_result.DeleteDetectorVersionResult":
        """<p>Deletes the detector version. You cannot delete detector versions that are in <code>ACTIVE</code> status.</p> <p>When you delete a detector version, Amazon Fraud Detector permanently deletes the detector and the data is no longer stored in Amazon Fraud Detector.</p>

        Args:
            detector_id: <p>The ID of the parent detector for the detector version to delete.</p>
            detector_version_id: <p>The ID of the detector version to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_detector_version_request.DeleteDetectorVersionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_detector_version_result.DeleteDetectorVersionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_detector_version

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_detector_version.delete_detector_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_detector_version_request.DeleteDetectorVersionRequest = {
            "detector_id": detector_id,
            "detector_version_id": detector_version_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_entity_type(
        self,
        name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_entity_type_result.DeleteEntityTypeResult":
        """<p>Deletes an entity type.</p> <p>You cannot delete an entity type that is included in an event type.</p> <p>When you delete an entity type, Amazon Fraud Detector permanently deletes that entity type and the data is no longer stored in Amazon Fraud Detector.</p>

        Args:
            name: <p>The name of the entity type to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_entity_type_request.DeleteEntityTypeRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_entity_type_result.DeleteEntityTypeResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_entity_type

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_entity_type.delete_entity_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_entity_type_request.DeleteEntityTypeRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event(
        self,
        event_id: "capo_frauddetector.types.identifier.identifier",
        event_type_name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        delete_audit_history: Optional[
            "capo_frauddetector.types.delete_audit_history.DeleteAuditHistory"
        ] = None,
    ) -> "capo_frauddetector.types.delete_event_result.DeleteEventResult":
        """<p>Deletes the specified event.</p> <p>When you delete an event, Amazon Fraud Detector permanently deletes that event and the event data is no longer stored in Amazon Fraud Detector. If <code>deleteAuditHistory</code> is <code>True</code>, event data is available through search for up to 30 seconds after the delete operation is completed.</p>

        Args:
            event_id: <p>The ID of the event to delete.</p>
            event_type_name: <p>The name of the event type.</p>
            delete_audit_history: <p>Specifies whether or not to delete any predictions associated with the event. If set to <code>True</code>, </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_event_request.DeleteEventRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_event_result.DeleteEventResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_event

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_event.delete_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_event_request.DeleteEventRequest = {
            "event_id": event_id,
            "event_type_name": event_type_name,
        }
        if delete_audit_history is not None:
            input_["delete_audit_history"] = delete_audit_history

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_events_by_event_type(
        self,
        event_type_name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_events_by_event_type_result.DeleteEventsByEventTypeResult":
        """<p>Deletes all events of a particular event type.</p>

        Args:
            event_type_name: <p>The name of the event type.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_events_by_event_type_request.DeleteEventsByEventTypeRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_events_by_event_type_result.DeleteEventsByEventTypeResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_events_by_event_type

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_events_by_event_type.delete_events_by_event_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_events_by_event_type_request.DeleteEventsByEventTypeRequest = {
            "event_type_name": event_type_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_type(
        self,
        name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_event_type_result.DeleteEventTypeResult":
        """<p>Deletes an event type.</p> <p>You cannot delete an event type that is used in a detector or a model.</p> <p>When you delete an event type, Amazon Fraud Detector permanently deletes that event type and the data is no longer stored in Amazon Fraud Detector.</p>

        Args:
            name: <p>The name of the event type to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_event_type_request.DeleteEventTypeRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_event_type_result.DeleteEventTypeResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_event_type

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_event_type.delete_event_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_event_type_request.DeleteEventTypeRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_external_model(
        self,
        model_endpoint: "capo_frauddetector.types.sage_maker_endpoint_identifier.sageMakerEndpointIdentifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_external_model_result.DeleteExternalModelResult":
        """<p>Removes a SageMaker model from Amazon Fraud Detector.</p> <p>You can remove an Amazon SageMaker model if it is not associated with a detector version. Removing a SageMaker model disconnects it from Amazon Fraud Detector, but the model remains available in SageMaker.</p>

        Args:
            model_endpoint: <p>The endpoint of the Amazon Sagemaker model to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_external_model_request.DeleteExternalModelRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_external_model_result.DeleteExternalModelResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_external_model

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_external_model.delete_external_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_external_model_request.DeleteExternalModelRequest = {
            "model_endpoint": model_endpoint
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_label(
        self,
        name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_label_result.DeleteLabelResult":
        """<p>Deletes a label.</p> <p>You cannot delete labels that are included in an event type in Amazon Fraud Detector.</p> <p>You cannot delete a label assigned to an event ID. You must first delete the relevant event ID.</p> <p>When you delete a label, Amazon Fraud Detector permanently deletes that label and the data is no longer stored in Amazon Fraud Detector.</p>

        Args:
            name: <p>The name of the label to delete.</p>

        Raises:
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_label_request.DeleteLabelRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_label_result.DeleteLabelResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_label

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_label.delete_label(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_label_request.DeleteLabelRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_list(
        self,
        name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_list_result.DeleteListResult":
        """<p> Deletes the list, provided it is not used in a rule. </p> <p> When you delete a list, Amazon Fraud Detector permanently deletes that list and the elements in the list.</p>

        Args:
            name: <p> The name of the list to delete. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_list_request.DeleteListRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_list_result.DeleteListResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_list

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_list.delete_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_list_request.DeleteListRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_model(
        self,
        model_id: "capo_frauddetector.types.model_identifier.modelIdentifier",
        model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_model_result.DeleteModelResult":
        """<p>Deletes a model.</p> <p>You can delete models and model versions in Amazon Fraud Detector, provided that they are not associated with a detector version.</p> <p> When you delete a model, Amazon Fraud Detector permanently deletes that model and the data is no longer stored in Amazon Fraud Detector.</p>

        Args:
            model_id: <p>The model ID of the model to delete.</p>
            model_type: <p>The model type of the model to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_model_request.DeleteModelRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_model_result.DeleteModelResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_model

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_model.delete_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_model_request.DeleteModelRequest = {
            "model_id": model_id,
            "model_type": model_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_model_version(
        self,
        model_id: "capo_frauddetector.types.model_identifier.modelIdentifier",
        model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum",
        model_version_number: "capo_frauddetector.types.float_version_string.floatVersionString",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> (
        "capo_frauddetector.types.delete_model_version_result.DeleteModelVersionResult"
    ):
        """<p>Deletes a model version.</p> <p>You can delete models and model versions in Amazon Fraud Detector, provided that they are not associated with a detector version.</p> <p> When you delete a model version, Amazon Fraud Detector permanently deletes that model version and the data is no longer stored in Amazon Fraud Detector.</p>

        Args:
            model_id: <p>The model ID of the model version to delete.</p>
            model_type: <p>The model type of the model version to delete.</p>
            model_version_number: <p>The model version number of the model version to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_model_version_request.DeleteModelVersionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_model_version_result.DeleteModelVersionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_model_version

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_model_version.delete_model_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_model_version_request.DeleteModelVersionRequest = {
            "model_id": model_id,
            "model_type": model_type,
            "model_version_number": model_version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_outcome(
        self,
        name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_outcome_result.DeleteOutcomeResult":
        """<p>Deletes an outcome.</p> <p>You cannot delete an outcome that is used in a rule version.</p> <p>When you delete an outcome, Amazon Fraud Detector permanently deletes that outcome and the data is no longer stored in Amazon Fraud Detector.</p>

        Args:
            name: <p>The name of the outcome to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_outcome_request.DeleteOutcomeRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_outcome_result.DeleteOutcomeResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_outcome

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_outcome.delete_outcome(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_outcome_request.DeleteOutcomeRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_rule(
        self,
        rule: "capo_frauddetector.types.rule.Rule",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_rule_result.DeleteRuleResult":
        """<p>Deletes the rule. You cannot delete a rule if it is used by an <code>ACTIVE</code> or <code>INACTIVE</code> detector version.</p> <p>When you delete a rule, Amazon Fraud Detector permanently deletes that rule and the data is no longer stored in Amazon Fraud Detector.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_rule_request.DeleteRuleRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_rule_result.DeleteRuleResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_rule

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_rule.delete_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_rule_request.DeleteRuleRequest = {
            "rule": rule
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_variable(
        self,
        name: "capo_frauddetector.types.string.string",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.delete_variable_result.DeleteVariableResult":
        """<p>Deletes a variable.</p> <p>You can't delete variables that are included in an event type in Amazon Fraud Detector.</p> <p>Amazon Fraud Detector automatically deletes model output variables and SageMaker model output variables when you delete the model. You can't delete these variables manually.</p> <p>When you delete a variable, Amazon Fraud Detector permanently deletes that variable and the data is no longer stored in Amazon Fraud Detector.</p>

        Args:
            name: <p>The name of the variable to delete.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.delete_variable_request.DeleteVariableRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.delete_variable_result.DeleteVariableResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_variable

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.delete_variable.delete_variable(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.delete_variable_request.DeleteVariableRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_detector(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.detector_version_max_results.DetectorVersionMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.describe_detector_result.DescribeDetectorResult":
        """<p>Gets all versions for a specified detector.</p>

        Args:
            detector_id: <p>The detector ID.</p>
            next_token: <p>The next token from the previous response.</p>
            max_results: <p>The maximum number of results to return for the request.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.describe_detector_request.DescribeDetectorRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.describe_detector_result.DescribeDetectorResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.describe_detector

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.describe_detector.describe_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.describe_detector_request.DescribeDetectorRequest = {
            "detector_id": detector_id
        }
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

    def describe_model_versions(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        model_id: Optional[
            "capo_frauddetector.types.model_identifier.modelIdentifier"
        ] = None,
        model_version_number: Optional[
            "capo_frauddetector.types.float_version_string.floatVersionString"
        ] = None,
        model_type: Optional[
            "capo_frauddetector.types.model_type_enum.ModelTypeEnum"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.models_max_page_size.modelsMaxPageSize"
        ] = None,
    ) -> "capo_frauddetector.types.describe_model_versions_result.DescribeModelVersionsResult":
        """<p>Gets all of the model versions for the specified model type or for the specified model type and model ID. You can also get details for a single, specified model version. </p>

        Args:
            model_id: <p>The model ID.</p>
            model_version_number: <p>The model version number.</p>
            model_type: <p>The model type.</p>
            next_token: <p>The next token from the previous results.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.describe_model_versions_request.DescribeModelVersionsRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.describe_model_versions_result.DescribeModelVersionsResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.describe_model_versions

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.describe_model_versions.describe_model_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.describe_model_versions_request.DescribeModelVersionsRequest = {}
        if model_id is not None:
            input_["model_id"] = model_id
        if model_version_number is not None:
            input_["model_version_number"] = model_version_number
        if model_type is not None:
            input_["model_type"] = model_type
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

    def iter_describe_model_versions(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        model_id: Optional[
            "capo_frauddetector.types.model_identifier.modelIdentifier"
        ] = None,
        model_version_number: Optional[
            "capo_frauddetector.types.float_version_string.floatVersionString"
        ] = None,
        model_type: Optional[
            "capo_frauddetector.types.model_type_enum.ModelTypeEnum"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.models_max_page_size.modelsMaxPageSize"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.describe_model_versions_result.DescribeModelVersionsResult]":
        _token = next_token
        while True:
            _response = self.describe_model_versions(
                config_overrides=config_overrides,
                model_id=model_id,
                model_version_number=model_version_number,
                model_type=model_type,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_batch_import_jobs(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        job_id: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        max_results: Optional[
            "capo_frauddetector.types.batch_imports_max_page_size.batchImportsMaxPageSize"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
    ) -> (
        "capo_frauddetector.types.get_batch_import_jobs_result.GetBatchImportJobsResult"
    ):
        """<p>Gets all batch import jobs or a specific job of the specified ID. This is a paginated API. If you provide a null <code>maxResults</code>, this action retrieves a maximum of 50 records per page. If you provide a <code>maxResults</code>, the value must be between 1 and 50. To get the next page results, provide the pagination token from the <code>GetBatchImportJobsResponse</code> as part of your request. A null pagination token fetches the records from the beginning.</p>

        Args:
            job_id: <p>The ID of the batch import job to get.</p>
            max_results: <p>The maximum number of objects to return for request.</p>
            next_token: <p>The next token from the previous request.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_batch_import_jobs_request.GetBatchImportJobsRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_batch_import_jobs_result.GetBatchImportJobsResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_batch_import_jobs

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_batch_import_jobs.get_batch_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_batch_import_jobs_request.GetBatchImportJobsRequest = {}
        if job_id is not None:
            input_["job_id"] = job_id
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

    def iter_get_batch_import_jobs(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        job_id: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        max_results: Optional[
            "capo_frauddetector.types.batch_imports_max_page_size.batchImportsMaxPageSize"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
    ) -> "Iterator[capo_frauddetector.types.get_batch_import_jobs_result.GetBatchImportJobsResult]":
        _token = next_token
        while True:
            _response = self.get_batch_import_jobs(
                config_overrides=config_overrides,
                job_id=job_id,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_batch_prediction_jobs(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        job_id: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        max_results: Optional[
            "capo_frauddetector.types.batch_predictions_max_page_size.batchPredictionsMaxPageSize"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
    ) -> "capo_frauddetector.types.get_batch_prediction_jobs_result.GetBatchPredictionJobsResult":
        """<p>Gets all batch prediction jobs or a specific job if you specify a job ID. This is a paginated API. If you provide a null maxResults, this action retrieves a maximum of 50 records per page. If you provide a maxResults, the value must be between 1 and 50. To get the next page results, provide the pagination token from the GetBatchPredictionJobsResponse as part of your request. A null pagination token fetches the records from the beginning.</p>

        Args:
            job_id: <p>The batch prediction job for which to get the details.</p>
            max_results: <p>The maximum number of objects to return for the request.</p>
            next_token: <p>The next token from the previous request.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_batch_prediction_jobs_request.GetBatchPredictionJobsRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_batch_prediction_jobs_result.GetBatchPredictionJobsResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_batch_prediction_jobs

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_batch_prediction_jobs.get_batch_prediction_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_batch_prediction_jobs_request.GetBatchPredictionJobsRequest = {}
        if job_id is not None:
            input_["job_id"] = job_id
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

    def iter_get_batch_prediction_jobs(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        job_id: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        max_results: Optional[
            "capo_frauddetector.types.batch_predictions_max_page_size.batchPredictionsMaxPageSize"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
    ) -> "Iterator[capo_frauddetector.types.get_batch_prediction_jobs_result.GetBatchPredictionJobsResult]":
        _token = next_token
        while True:
            _response = self.get_batch_prediction_jobs(
                config_overrides=config_overrides,
                job_id=job_id,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_delete_events_by_event_type_status(
        self,
        event_type_name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.get_delete_events_by_event_type_status_result.GetDeleteEventsByEventTypeStatusResult":
        """<p>Retrieves the status of a <code>DeleteEventsByEventType</code> action.</p>

        Args:
            event_type_name: <p>Name of event type for which to get the deletion status.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_delete_events_by_event_type_status_request.GetDeleteEventsByEventTypeStatusRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_delete_events_by_event_type_status_result.GetDeleteEventsByEventTypeStatusResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_delete_events_by_event_type_status

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_delete_events_by_event_type_status.get_delete_events_by_event_type_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_delete_events_by_event_type_status_request.GetDeleteEventsByEventTypeStatusRequest = {
            "event_type_name": event_type_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_detectors(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        detector_id: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.detectors_max_results.DetectorsMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_detectors_result.GetDetectorsResult":
        """<p>Gets all detectors or a single detector if a <code>detectorId</code> is specified. This is a paginated API. If you provide a null <code>maxResults</code>, this action retrieves a maximum of 10 records per page. If you provide a <code>maxResults</code>, the value must be between 5 and 10. To get the next page results, provide the pagination token from the <code>GetDetectorsResponse</code> as part of your request. A null pagination token fetches the records from the beginning. </p>

        Args:
            detector_id: <p>The detector ID.</p>
            next_token: <p>The next token for the subsequent request.</p>
            max_results: <p>The maximum number of objects to return for the request.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_detectors_request.GetDetectorsRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_detectors_result.GetDetectorsResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_detectors

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_detectors.get_detectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_detectors_request.GetDetectorsRequest = {}
        if detector_id is not None:
            input_["detector_id"] = detector_id
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

    def iter_get_detectors(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        detector_id: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.detectors_max_results.DetectorsMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_detectors_result.GetDetectorsResult]":
        _token = next_token
        while True:
            _response = self.get_detectors(
                config_overrides=config_overrides,
                detector_id=detector_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_detector_version(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        detector_version_id: "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> (
        "capo_frauddetector.types.get_detector_version_result.GetDetectorVersionResult"
    ):
        """<p>Gets a particular detector version. </p>

        Args:
            detector_id: <p>The detector ID.</p>
            detector_version_id: <p>The detector version ID.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_detector_version_request.GetDetectorVersionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_detector_version_result.GetDetectorVersionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_detector_version

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_detector_version.get_detector_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_detector_version_request.GetDetectorVersionRequest = {
            "detector_id": detector_id,
            "detector_version_id": detector_version_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_entity_types(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.entity_types_max_results.entityTypesMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_entity_types_result.GetEntityTypesResult":
        """<p>Gets all entity types or a specific entity type if a name is specified. This is a paginated API. If you provide a null <code>maxResults</code>, this action retrieves a maximum of 10 records per page. If you provide a <code>maxResults</code>, the value must be between 5 and 10. To get the next page results, provide the pagination token from the <code>GetEntityTypesResponse</code> as part of your request. A null pagination token fetches the records from the beginning. </p>

        Args:
            name: <p>The name.</p>
            next_token: <p>The next token for the subsequent request.</p>
            max_results: <p>The maximum number of objects to return for the request.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_entity_types_request.GetEntityTypesRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_entity_types_result.GetEntityTypesResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_entity_types

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_entity_types.get_entity_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_entity_types_request.GetEntityTypesRequest = {}
        if name is not None:
            input_["name"] = name
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

    def iter_get_entity_types(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.entity_types_max_results.entityTypesMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_entity_types_result.GetEntityTypesResult]":
        _token = next_token
        while True:
            _response = self.get_entity_types(
                config_overrides=config_overrides,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_event(
        self,
        event_id: "capo_frauddetector.types.string.string",
        event_type_name: "capo_frauddetector.types.string.string",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.get_event_result.GetEventResult":
        """<p>Retrieves details of events stored with Amazon Fraud Detector. This action does not retrieve prediction results.</p>

        Args:
            event_id: <p>The ID of the event to retrieve.</p>
            event_type_name: <p>The event type of the event to retrieve.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_event_request.GetEventRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_event_result.GetEventResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_event

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_event.get_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_event_request.GetEventRequest = {
            "event_id": event_id,
            "event_type_name": event_type_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_prediction(
        self,
        detector_id: "capo_frauddetector.types.string.string",
        event_id: "capo_frauddetector.types.string.string",
        event_type_name: "capo_frauddetector.types.string.string",
        entities: "capo_frauddetector.types.list_of_entities.listOfEntities",
        event_timestamp: "capo_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601",
        event_variables: "capo_frauddetector.types.event_variable_map.EventVariableMap",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        detector_version_id: Optional[
            "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
        ] = None,
        external_model_endpoint_data_blobs: Optional[
            "capo_frauddetector.types.external_model_endpoint_data_blob_map.ExternalModelEndpointDataBlobMap"
        ] = None,
    ) -> (
        "capo_frauddetector.types.get_event_prediction_result.GetEventPredictionResult"
    ):
        """<p>Evaluates an event against a detector version. If a version ID is not provided, the detector’s (<code>ACTIVE</code>) version is used.</p>

        Args:
            detector_id: <p>The detector ID.</p>
            detector_version_id: <p>The detector version ID.</p>
            event_id: <p>The unique ID used to identify the event.</p>
            event_type_name: <p>The event type associated with the detector specified for the prediction.</p>
            entities: <p>The entity type (associated with the detector's event type) and specific entity ID representing who performed the event. If an entity id is not available, use "UNKNOWN."</p>
            event_timestamp: <p>Timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.</p>
            event_variables: <p>Names of the event type's variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.</p> <important> <p>You must provide at least one eventVariable</p> </important> <p>To ensure most accurate fraud prediction and to simplify your data preparation, Amazon Fraud Detector will replace all missing variables or values as follows:</p> <p> <b>For Amazon Fraud Detector trained models:</b> </p> <p>If a null value is provided explicitly for a variable or if a variable is missing, model will replace the null value or the missing variable (no variable name in the eventVariables map) with calculated default mean/medians for numeric variables and with special values for categorical variables.</p> <p> <b>For imported SageMaker models:</b> </p> <p>If a null value is provided explicitly for a variable, the model and rules will use “null” as the value. If a variable is not provided (no variable name in the eventVariables map), model and rules will use the default value that is provided for the variable. </p>
            external_model_endpoint_data_blobs: <p>The Amazon SageMaker model endpoint input data blobs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.resource_unavailable_exception.ResourceUnavailableException: <p>An exception indicating that the attached customer-owned (external) model threw an exception when Amazon Fraud Detector invoked the model.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_event_prediction_request.GetEventPredictionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_event_prediction_result.GetEventPredictionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_event_prediction

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_event_prediction.get_event_prediction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_event_prediction_request.GetEventPredictionRequest = {
            "detector_id": detector_id,
            "event_id": event_id,
            "event_type_name": event_type_name,
            "entities": entities,
            "event_timestamp": event_timestamp,
            "event_variables": event_variables,
        }
        if detector_version_id is not None:
            input_["detector_version_id"] = detector_version_id
        if external_model_endpoint_data_blobs is not None:
            input_["external_model_endpoint_data_blobs"] = (
                external_model_endpoint_data_blobs
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_prediction_metadata(
        self,
        event_id: "capo_frauddetector.types.identifier.identifier",
        event_type_name: "capo_frauddetector.types.identifier.identifier",
        detector_id: "capo_frauddetector.types.identifier.identifier",
        detector_version_id: "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString",
        prediction_timestamp: "capo_frauddetector.types.time.time",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.get_event_prediction_metadata_result.GetEventPredictionMetadataResult":
        """<p> Gets details of the past fraud predictions for the specified event ID, event type, detector ID, and detector version ID that was generated in the specified time period. </p>

        Args:
            event_id: <p> The event ID. </p>
            event_type_name: <p> The event type associated with the detector specified for the prediction. </p>
            detector_id: <p> The detector ID. </p>
            detector_version_id: <p> The detector version ID. </p>
            prediction_timestamp: <p> The timestamp that defines when the prediction was generated. The timestamp must be specified using ISO 8601 standard in UTC.</p> <p>We recommend calling <a href="https://docs.aws.amazon.com/frauddetector/latest/api/API_ListEventPredictions.html">ListEventPredictions</a> first, and using the <code>predictionTimestamp</code> value in the response to provide an accurate prediction timestamp value.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_event_prediction_metadata_request.GetEventPredictionMetadataRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_event_prediction_metadata_result.GetEventPredictionMetadataResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_event_prediction_metadata

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_event_prediction_metadata.get_event_prediction_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_event_prediction_metadata_request.GetEventPredictionMetadataRequest = {
            "event_id": event_id,
            "event_type_name": event_type_name,
            "detector_id": detector_id,
            "detector_version_id": detector_version_id,
            "prediction_timestamp": prediction_timestamp,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_types(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.event_types_max_results.eventTypesMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_event_types_result.GetEventTypesResult":
        """<p>Gets all event types or a specific event type if name is provided. This is a paginated API. If you provide a null <code>maxResults</code>, this action retrieves a maximum of 10 records per page. If you provide a <code>maxResults</code>, the value must be between 5 and 10. To get the next page results, provide the pagination token from the <code>GetEventTypesResponse</code> as part of your request. A null pagination token fetches the records from the beginning. </p>

        Args:
            name: <p>The name.</p>
            next_token: <p>The next token for the subsequent request.</p>
            max_results: <p>The maximum number of objects to return for the request.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_event_types_request.GetEventTypesRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_event_types_result.GetEventTypesResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_event_types

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_event_types.get_event_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_event_types_request.GetEventTypesRequest = {}
        if name is not None:
            input_["name"] = name
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

    def iter_get_event_types(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.event_types_max_results.eventTypesMaxResults"
        ] = None,
    ) -> (
        "Iterator[capo_frauddetector.types.get_event_types_result.GetEventTypesResult]"
    ):
        _token = next_token
        while True:
            _response = self.get_event_types(
                config_overrides=config_overrides,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_external_models(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        model_endpoint: Optional["capo_frauddetector.types.string.string"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.external_models_max_results.ExternalModelsMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_external_models_result.GetExternalModelsResult":
        """<p>Gets the details for one or more Amazon SageMaker models that have been imported into the service. This is a paginated API. If you provide a null <code>maxResults</code>, this actions retrieves a maximum of 10 records per page. If you provide a <code>maxResults</code>, the value must be between 5 and 10. To get the next page results, provide the pagination token from the <code>GetExternalModelsResult</code> as part of your request. A null pagination token fetches the records from the beginning. </p>

        Args:
            model_endpoint: <p>The Amazon SageMaker model endpoint.</p>
            next_token: <p>The next page token for the request.</p>
            max_results: <p>The maximum number of objects to return for the request.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_external_models_request.GetExternalModelsRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_external_models_result.GetExternalModelsResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_external_models

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_external_models.get_external_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_external_models_request.GetExternalModelsRequest = {}
        if model_endpoint is not None:
            input_["model_endpoint"] = model_endpoint
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

    def iter_get_external_models(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        model_endpoint: Optional["capo_frauddetector.types.string.string"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.external_models_max_results.ExternalModelsMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_external_models_result.GetExternalModelsResult]":
        _token = next_token
        while True:
            _response = self.get_external_models(
                config_overrides=config_overrides,
                model_endpoint=model_endpoint,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_kms_encryption_key(
        self, *, config_overrides: Optional[FraudDetectorClientConfig] = None
    ) -> "capo_frauddetector.types.get_kms_encryption_key_result.GetKMSEncryptionKeyResult":
        """<p>Gets the encryption key if a KMS key has been specified to be used to encrypt content in Amazon Fraud Detector.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_kms_encryption_key_result.GetKMSEncryptionKeyResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_kms_encryption_key

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_kms_encryption_key.get_kms_encryption_key(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_labels(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.labels_max_results.labelsMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_labels_result.GetLabelsResult":
        """<p>Gets all labels or a specific label if name is provided. This is a paginated API. If you provide a null <code>maxResults</code>, this action retrieves a maximum of 50 records per page. If you provide a <code>maxResults</code>, the value must be between 10 and 50. To get the next page results, provide the pagination token from the <code>GetGetLabelsResponse</code> as part of your request. A null pagination token fetches the records from the beginning. </p>

        Args:
            name: <p>The name of the label or labels to get.</p>
            next_token: <p>The next token for the subsequent request.</p>
            max_results: <p>The maximum number of objects to return for the request.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_labels_request.GetLabelsRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_labels_result.GetLabelsResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_labels

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_labels.get_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_labels_request.GetLabelsRequest = {}
        if name is not None:
            input_["name"] = name
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

    def iter_get_labels(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.labels_max_results.labelsMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_labels_result.GetLabelsResult]":
        _token = next_token
        while True:
            _response = self.get_labels(
                config_overrides=config_overrides,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_list_elements(
        self,
        name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        next_token: Optional["capo_frauddetector.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_frauddetector.types.lists_elements_max_results.ListsElementsMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_list_elements_result.GetListElementsResult":
        """<p> Gets all the elements in the specified list. </p>

        Args:
            name: <p> The name of the list. </p>
            next_token: <p> The next token for the subsequent request. </p>
            max_results: <p> The maximum number of objects to return for the request. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_list_elements_request.GetListElementsRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_list_elements_result.GetListElementsResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_list_elements

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_list_elements.get_list_elements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_list_elements_request.GetListElementsRequest = {
            "name": name
        }
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

    def iter_get_list_elements(
        self,
        name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        next_token: Optional["capo_frauddetector.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_frauddetector.types.lists_elements_max_results.ListsElementsMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_list_elements_result.GetListElementsResult]":
        _token = next_token
        while True:
            _response = self.get_list_elements(
                name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_lists_metadata(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional[
            "capo_frauddetector.types.no_dash_identifier.noDashIdentifier"
        ] = None,
        next_token: Optional["capo_frauddetector.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_frauddetector.types.lists_metadata_max_results.ListsMetadataMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_lists_metadata_result.GetListsMetadataResult":
        """<p> Gets the metadata of either all the lists under the account or the specified list. </p>

        Args:
            name: <p> The name of the list. </p>
            next_token: <p> The next token for the subsequent request. </p>
            max_results: <p> The maximum number of objects to return for the request. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_lists_metadata_request.GetListsMetadataRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_lists_metadata_result.GetListsMetadataResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_lists_metadata

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_lists_metadata.get_lists_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_lists_metadata_request.GetListsMetadataRequest = {}
        if name is not None:
            input_["name"] = name
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

    def iter_get_lists_metadata(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional[
            "capo_frauddetector.types.no_dash_identifier.noDashIdentifier"
        ] = None,
        next_token: Optional["capo_frauddetector.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_frauddetector.types.lists_metadata_max_results.ListsMetadataMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_lists_metadata_result.GetListsMetadataResult]":
        _token = next_token
        while True:
            _response = self.get_lists_metadata(
                config_overrides=config_overrides,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_models(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        model_id: Optional[
            "capo_frauddetector.types.model_identifier.modelIdentifier"
        ] = None,
        model_type: Optional[
            "capo_frauddetector.types.model_type_enum.ModelTypeEnum"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.models_max_page_size.modelsMaxPageSize"
        ] = None,
    ) -> "capo_frauddetector.types.get_models_result.GetModelsResult":
        """<p>Gets one or more models. Gets all models for the Amazon Web Services account if no model type and no model id provided. Gets all models for the Amazon Web Services account and model type, if the model type is specified but model id is not provided. Gets a specific model if (model type, model id) tuple is specified. </p> <p>This is a paginated API. If you provide a null <code>maxResults</code>, this action retrieves a maximum of 10 records per page. If you provide a <code>maxResults</code>, the value must be between 1 and 10. To get the next page results, provide the pagination token from the response as part of your request. A null pagination token fetches the records from the beginning.</p>

        Args:
            model_id: <p>The model ID.</p>
            model_type: <p>The model type.</p>
            next_token: <p>The next token for the subsequent request.</p>
            max_results: <p>The maximum number of objects to return for the request. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_models_request.GetModelsRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_models_result.GetModelsResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_models

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_models.get_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_models_request.GetModelsRequest = {}
        if model_id is not None:
            input_["model_id"] = model_id
        if model_type is not None:
            input_["model_type"] = model_type
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

    def iter_get_models(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        model_id: Optional[
            "capo_frauddetector.types.model_identifier.modelIdentifier"
        ] = None,
        model_type: Optional[
            "capo_frauddetector.types.model_type_enum.ModelTypeEnum"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.models_max_page_size.modelsMaxPageSize"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_models_result.GetModelsResult]":
        _token = next_token
        while True:
            _response = self.get_models(
                config_overrides=config_overrides,
                model_id=model_id,
                model_type=model_type,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_model_version(
        self,
        model_id: "capo_frauddetector.types.model_identifier.modelIdentifier",
        model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum",
        model_version_number: "capo_frauddetector.types.float_version_string.floatVersionString",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.get_model_version_result.GetModelVersionResult":
        """<p>Gets the details of the specified model version.</p>

        Args:
            model_id: <p>The model ID.</p>
            model_type: <p>The model type.</p>
            model_version_number: <p>The model version number.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_model_version_request.GetModelVersionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_model_version_result.GetModelVersionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_model_version

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_model_version.get_model_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_model_version_request.GetModelVersionRequest = {
            "model_id": model_id,
            "model_type": model_type,
            "model_version_number": model_version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_outcomes(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.outcomes_max_results.OutcomesMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_outcomes_result.GetOutcomesResult":
        """<p>Gets one or more outcomes. This is a paginated API. If you provide a null <code>maxResults</code>, this actions retrieves a maximum of 100 records per page. If you provide a <code>maxResults</code>, the value must be between 50 and 100. To get the next page results, provide the pagination token from the <code>GetOutcomesResult</code> as part of your request. A null pagination token fetches the records from the beginning. </p>

        Args:
            name: <p>The name of the outcome or outcomes to get.</p>
            next_token: <p>The next page token for the request. </p>
            max_results: <p>The maximum number of objects to return for the request. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_outcomes_request.GetOutcomesRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_outcomes_result.GetOutcomesResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_outcomes

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_outcomes.get_outcomes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_outcomes_request.GetOutcomesRequest = {}
        if name is not None:
            input_["name"] = name
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

    def iter_get_outcomes(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.outcomes_max_results.OutcomesMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_outcomes_result.GetOutcomesResult]":
        _token = next_token
        while True:
            _response = self.get_outcomes(
                config_overrides=config_overrides,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_rules(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        rule_id: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        rule_version: Optional[
            "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.rules_max_results.RulesMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_rules_result.GetRulesResult":
        """<p>Get all rules for a detector (paginated) if <code>ruleId</code> and <code>ruleVersion</code> are not specified. Gets all rules for the detector and the <code>ruleId</code> if present (paginated). Gets a specific rule if both the <code>ruleId</code> and the <code>ruleVersion</code> are specified.</p> <p>This is a paginated API. Providing null maxResults results in retrieving maximum of 100 records per page. If you provide maxResults the value must be between 50 and 100. To get the next page result, a provide a pagination token from GetRulesResult as part of your request. Null pagination token fetches the records from the beginning.</p>

        Args:
            rule_id: <p>The rule ID.</p>
            detector_id: <p>The detector ID.</p>
            rule_version: <p>The rule version.</p>
            next_token: <p>The next page token.</p>
            max_results: <p>The maximum number of rules to return for the request.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_rules_request.GetRulesRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_rules_result.GetRulesResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_rules

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_rules.get_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_rules_request.GetRulesRequest = {
            "detector_id": detector_id
        }
        if rule_id is not None:
            input_["rule_id"] = rule_id
        if rule_version is not None:
            input_["rule_version"] = rule_version
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

    def iter_get_rules(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        rule_id: Optional["capo_frauddetector.types.identifier.identifier"] = None,
        rule_version: Optional[
            "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.rules_max_results.RulesMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_rules_result.GetRulesResult]":
        _token = next_token
        while True:
            _response = self.get_rules(
                detector_id,
                config_overrides=config_overrides,
                rule_id=rule_id,
                rule_version=rule_version,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_variables(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.string.string"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.variables_max_results.VariablesMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.get_variables_result.GetVariablesResult":
        """<p>Gets all of the variables or the specific variable. This is a paginated API. Providing null <code>maxSizePerPage</code> results in retrieving maximum of 100 records per page. If you provide <code>maxSizePerPage</code> the value must be between 50 and 100. To get the next page result, a provide a pagination token from <code>GetVariablesResult</code> as part of your request. Null pagination token fetches the records from the beginning. </p>

        Args:
            name: <p>The name of the variable. </p>
            next_token: <p>The next page token of the get variable request. </p>
            max_results: <p>The max size per page determined for the get variable request. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.get_variables_request.GetVariablesRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.get_variables_result.GetVariablesResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.get_variables

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.get_variables.get_variables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.get_variables_request.GetVariablesRequest = {}
        if name is not None:
            input_["name"] = name
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

    def iter_get_variables(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        name: Optional["capo_frauddetector.types.string.string"] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.variables_max_results.VariablesMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.get_variables_result.GetVariablesResult]":
        _token = next_token
        while True:
            _response = self.get_variables(
                config_overrides=config_overrides,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_predictions(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        event_id: Optional[
            "capo_frauddetector.types.filter_condition.FilterCondition"
        ] = None,
        event_type: Optional[
            "capo_frauddetector.types.filter_condition.FilterCondition"
        ] = None,
        detector_id: Optional[
            "capo_frauddetector.types.filter_condition.FilterCondition"
        ] = None,
        detector_version_id: Optional[
            "capo_frauddetector.types.filter_condition.FilterCondition"
        ] = None,
        prediction_time_range: Optional[
            "capo_frauddetector.types.prediction_time_range.PredictionTimeRange"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.event_predictions_max_results.EventPredictionsMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.list_event_predictions_result.ListEventPredictionsResult":
        """<p>Gets a list of past predictions. The list can be filtered by detector ID, detector version ID, event ID, event type, or by specifying a time period. If filter is not specified, the most recent prediction is returned.</p> <p>For example, the following filter lists all past predictions for <code>xyz</code> event type - <code>{ "eventType":{ "value": "xyz" }” } </code> </p> <p>This is a paginated API. If you provide a null <code>maxResults</code>, this action will retrieve a maximum of 10 records per page. If you provide a <code>maxResults</code>, the value must be between 50 and 100. To get the next page results, provide the <code>nextToken</code> from the response as part of your request. A null <code>nextToken</code> fetches the records from the beginning. </p>

        Args:
            event_id: <p> The event ID. </p>
            event_type: <p> The event type associated with the detector. </p>
            detector_id: <p> The detector ID. </p>
            detector_version_id: <p> The detector version ID. </p>
            prediction_time_range: <p> The time period for when the predictions were generated. </p>
            next_token: <p> Identifies the next page of results to return. Use the token to make the call again to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>
            max_results: <p> The maximum number of predictions to return for the request. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.list_event_predictions_request.ListEventPredictionsRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.list_event_predictions_result.ListEventPredictionsResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.list_event_predictions

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.list_event_predictions.list_event_predictions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.list_event_predictions_request.ListEventPredictionsRequest = {}
        if event_id is not None:
            input_["event_id"] = event_id
        if event_type is not None:
            input_["event_type"] = event_type
        if detector_id is not None:
            input_["detector_id"] = detector_id
        if detector_version_id is not None:
            input_["detector_version_id"] = detector_version_id
        if prediction_time_range is not None:
            input_["prediction_time_range"] = prediction_time_range
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

    def iter_list_event_predictions(
        self,
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        event_id: Optional[
            "capo_frauddetector.types.filter_condition.FilterCondition"
        ] = None,
        event_type: Optional[
            "capo_frauddetector.types.filter_condition.FilterCondition"
        ] = None,
        detector_id: Optional[
            "capo_frauddetector.types.filter_condition.FilterCondition"
        ] = None,
        detector_version_id: Optional[
            "capo_frauddetector.types.filter_condition.FilterCondition"
        ] = None,
        prediction_time_range: Optional[
            "capo_frauddetector.types.prediction_time_range.PredictionTimeRange"
        ] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.event_predictions_max_results.EventPredictionsMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.list_event_predictions_result.ListEventPredictionsResult]":
        _token = next_token
        while True:
            _response = self.list_event_predictions(
                config_overrides=config_overrides,
                event_id=event_id,
                event_type=event_type,
                detector_id=detector_id,
                detector_version_id=detector_version_id,
                prediction_time_range=prediction_time_range,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.tags_max_results.TagsMaxResults"
        ] = None,
    ) -> "capo_frauddetector.types.list_tags_for_resource_result.ListTagsForResourceResult":
        """<p>Lists all tags associated with the resource. This is a paginated API. To get the next page results, provide the pagination token from the response as part of your request. A null pagination token fetches the records from the beginning. </p>

        Args:
            resource_arn: <p>The ARN that specifies the resource whose tags you want to list.</p>
            next_token: <p>The next token from the previous results.</p>
            max_results: <p>The maximum number of objects to return for the request. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.list_tags_for_resource

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }
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

    def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        next_token: Optional["capo_frauddetector.types.string.string"] = None,
        max_results: Optional[
            "capo_frauddetector.types.tags_max_results.TagsMaxResults"
        ] = None,
    ) -> "Iterator[capo_frauddetector.types.list_tags_for_resource_result.ListTagsForResourceResult]":
        _token = next_token
        while True:
            _response = self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_detector(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        event_type_name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.put_detector_result.PutDetectorResult":
        """<p>Creates or updates a detector. </p>

        Args:
            detector_id: <p>The detector ID. </p>
            description: <p>The description of the detector.</p>
            event_type_name: <p>The name of the event type.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.put_detector_request.PutDetectorRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.put_detector_result.PutDetectorResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.put_detector

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.put_detector.put_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.put_detector_request.PutDetectorRequest = {
            "detector_id": detector_id,
            "event_type_name": event_type_name,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_entity_type(
        self,
        name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.put_entity_type_result.PutEntityTypeResult":
        """<p>Creates or updates an entity type. An entity represents who is performing the event. As part of a fraud prediction, you pass the entity ID to indicate the specific entity who performed the event. An entity type classifies the entity. Example classifications include customer, merchant, or account.</p>

        Args:
            name: <p>The name of the entity type.</p>
            description: <p>The description.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.put_entity_type_request.PutEntityTypeRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.put_entity_type_result.PutEntityTypeResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.put_entity_type

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.put_entity_type.put_entity_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.put_entity_type_request.PutEntityTypeRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_event_type(
        self,
        name: "capo_frauddetector.types.identifier.identifier",
        event_variables: "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings",
        entity_types: "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        labels: Optional[
            "capo_frauddetector.types.list_of_strings.ListOfStrings"
        ] = None,
        event_ingestion: Optional[
            "capo_frauddetector.types.event_ingestion.EventIngestion"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
        event_orchestration: Optional[
            "capo_frauddetector.types.event_orchestration.EventOrchestration"
        ] = None,
    ) -> "capo_frauddetector.types.put_event_type_result.PutEventTypeResult":
        """<p>Creates or updates an event type. An event is a business activity that is evaluated for fraud risk. With Amazon Fraud Detector, you generate fraud predictions for events. An event type defines the structure for an event sent to Amazon Fraud Detector. This includes the variables sent as part of the event, the entity performing the event (such as a customer), and the labels that classify the event. Example event types include online payment transactions, account registrations, and authentications.</p>

        Args:
            name: <p>The name.</p>
            description: <p>The description of the event type.</p>
            event_variables: <p>The event type variables.</p>
            labels: <p>The event type labels.</p>
            entity_types: <p>The entity type for the event type. Example entity types: customer, merchant, account.</p>
            event_ingestion: <p>Specifies if ingestion is enabled or disabled.</p>
            tags: <p>A collection of key and value pairs.</p>
            event_orchestration: <p>Enables or disables event orchestration. If enabled, you can send event predictions to select AWS services for downstream processing of the events.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.put_event_type_request.PutEventTypeRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.put_event_type_result.PutEventTypeResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.put_event_type

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.put_event_type.put_event_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.put_event_type_request.PutEventTypeRequest = {
            "name": name,
            "event_variables": event_variables,
            "entity_types": entity_types,
        }
        if description is not None:
            input_["description"] = description
        if labels is not None:
            input_["labels"] = labels
        if event_ingestion is not None:
            input_["event_ingestion"] = event_ingestion
        if tags is not None:
            input_["tags"] = tags
        if event_orchestration is not None:
            input_["event_orchestration"] = event_orchestration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_external_model(
        self,
        model_endpoint: "capo_frauddetector.types.sage_maker_endpoint_identifier.sageMakerEndpointIdentifier",
        model_source: "capo_frauddetector.types.model_source.ModelSource",
        invoke_model_endpoint_role_arn: "capo_frauddetector.types.string.string",
        input_configuration: "capo_frauddetector.types.model_input_configuration.ModelInputConfiguration",
        output_configuration: "capo_frauddetector.types.model_output_configuration.ModelOutputConfiguration",
        model_endpoint_status: "capo_frauddetector.types.model_endpoint_status.ModelEndpointStatus",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.put_external_model_result.PutExternalModelResult":
        """<p>Creates or updates an Amazon SageMaker model endpoint. You can also use this action to update the configuration of the model endpoint, including the IAM role and/or the mapped variables. </p>

        Args:
            model_endpoint: <p>The model endpoints name.</p>
            model_source: <p>The source of the model.</p>
            invoke_model_endpoint_role_arn: <p>The IAM role used to invoke the model endpoint.</p>
            input_configuration: <p>The model endpoint input configuration.</p>
            output_configuration: <p>The model endpoint output configuration.</p>
            model_endpoint_status: <p>The model endpoint’s status in Amazon Fraud Detector.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.put_external_model_request.PutExternalModelRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.put_external_model_result.PutExternalModelResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.put_external_model

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.put_external_model.put_external_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.put_external_model_request.PutExternalModelRequest = {
            "model_endpoint": model_endpoint,
            "model_source": model_source,
            "invoke_model_endpoint_role_arn": invoke_model_endpoint_role_arn,
            "input_configuration": input_configuration,
            "output_configuration": output_configuration,
            "model_endpoint_status": model_endpoint_status,
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

    def put_kms_encryption_key(
        self,
        kms_encryption_key_arn: "capo_frauddetector.types.kms_encryption_key_arn.KmsEncryptionKeyArn",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.put_kms_encryption_key_result.PutKMSEncryptionKeyResult":
        """<p>Specifies the KMS key to be used to encrypt content in Amazon Fraud Detector.</p>

        Args:
            kms_encryption_key_arn: <p>The KMS encryption key ARN.</p> <p>The KMS key must be single-Region key. Amazon Fraud Detector does not support multi-Region KMS key.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.put_kms_encryption_key_request.PutKMSEncryptionKeyRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.put_kms_encryption_key_result.PutKMSEncryptionKeyResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.put_kms_encryption_key

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.put_kms_encryption_key.put_kms_encryption_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.put_kms_encryption_key_request.PutKMSEncryptionKeyRequest = {
            "kms_encryption_key_arn": kms_encryption_key_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_label(
        self,
        name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.put_label_result.PutLabelResult":
        """<p>Creates or updates label. A label classifies an event as fraudulent or legitimate. Labels are associated with event types and used to train supervised machine learning models in Amazon Fraud Detector. </p>

        Args:
            name: <p>The label name.</p>
            description: <p>The label description.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.put_label_request.PutLabelRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.put_label_result.PutLabelResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.put_label

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.put_label.put_label(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.put_label_request.PutLabelRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_outcome(
        self,
        name: "capo_frauddetector.types.identifier.identifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.put_outcome_result.PutOutcomeResult":
        """<p>Creates or updates an outcome. </p>

        Args:
            name: <p>The name of the outcome.</p>
            description: <p>The outcome description.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.put_outcome_request.PutOutcomeRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.put_outcome_result.PutOutcomeResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.put_outcome

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.put_outcome.put_outcome(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.put_outcome_request.PutOutcomeRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_event(
        self,
        event_id: "capo_frauddetector.types.identifier.identifier",
        event_type_name: "capo_frauddetector.types.identifier.identifier",
        event_timestamp: "capo_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601",
        event_variables: "capo_frauddetector.types.event_variable_map.EventVariableMap",
        entities: "capo_frauddetector.types.list_of_entities.listOfEntities",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        assigned_label: Optional[
            "capo_frauddetector.types.identifier.identifier"
        ] = None,
        label_timestamp: Optional[
            "capo_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601"
        ] = None,
    ) -> "capo_frauddetector.types.send_event_result.SendEventResult":
        """<p>Stores events in Amazon Fraud Detector without generating fraud predictions for those events. For example, you can use <code>SendEvent</code> to upload a historical dataset, which you can then later use to train a model.</p>

        Args:
            event_id: <p>The event ID to upload.</p>
            event_type_name: <p>The event type name of the event.</p>
            event_timestamp: <p>The timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.</p>
            event_variables: <p>Names of the event type's variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.</p>
            assigned_label: <p>The label to associate with the event. Required if specifying <code>labelTimestamp</code>.</p>
            label_timestamp: <p>The timestamp associated with the label. Required if specifying <code>assignedLabel</code>.</p>
            entities: <p>An array of entities.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.send_event_request.SendEventRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.send_event_result.SendEventResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.send_event

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.send_event.send_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.send_event_request.SendEventRequest = {
            "event_id": event_id,
            "event_type_name": event_type_name,
            "event_timestamp": event_timestamp,
            "event_variables": event_variables,
            "entities": entities,
        }
        if assigned_label is not None:
            input_["assigned_label"] = assigned_label
        if label_timestamp is not None:
            input_["label_timestamp"] = label_timestamp

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn",
        tags: "capo_frauddetector.types.tag_list.tagList",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.tag_resource_result.TagResourceResult":
        """<p>Assigns tags to a resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tags: <p>The tags to assign to the resource.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.tag_resource_result.TagResourceResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.tag_resource

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn",
        tag_keys: "capo_frauddetector.types.tag_key_list.tagKeyList",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.untag_resource_result.UntagResourceResult":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource from which to remove the tag.</p>
            tag_keys: <p>The resource ARN.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.untag_resource_result.UntagResourceResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.untag_resource

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_detector_version(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        detector_version_id: "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString",
        external_model_endpoints: "capo_frauddetector.types.list_of_strings.ListOfStrings",
        rules: "capo_frauddetector.types.rule_list.RuleList",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        model_versions: Optional[
            "capo_frauddetector.types.list_of_model_versions.ListOfModelVersions"
        ] = None,
        rule_execution_mode: Optional[
            "capo_frauddetector.types.rule_execution_mode.RuleExecutionMode"
        ] = None,
    ) -> "capo_frauddetector.types.update_detector_version_result.UpdateDetectorVersionResult":
        """<p> Updates a detector version. The detector version attributes that you can update include models, external model endpoints, rules, rule execution mode, and description. You can only update a <code>DRAFT</code> detector version.</p>

        Args:
            detector_id: <p>The parent detector ID for the detector version you want to update.</p>
            detector_version_id: <p>The detector version ID. </p>
            external_model_endpoints: <p>The Amazon SageMaker model endpoints to include in the detector version.</p>
            rules: <p>The rules to include in the detector version.</p>
            description: <p>The detector version description. </p>
            model_versions: <p>The model versions to include in the detector version.</p>
            rule_execution_mode: <p>The rule execution mode to add to the detector.</p> <p>If you specify <code>FIRST_MATCHED</code>, Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.</p> <p>If you specifiy <code>ALL_MATCHED</code>, Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules. You can define and edit the rule mode at the detector version level, when it is in draft status.</p> <p>The default behavior is <code>FIRST_MATCHED</code>.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_detector_version_request.UpdateDetectorVersionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_detector_version_result.UpdateDetectorVersionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_detector_version

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_detector_version.update_detector_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_detector_version_request.UpdateDetectorVersionRequest = {
            "detector_id": detector_id,
            "detector_version_id": detector_version_id,
            "external_model_endpoints": external_model_endpoints,
            "rules": rules,
        }
        if description is not None:
            input_["description"] = description
        if model_versions is not None:
            input_["model_versions"] = model_versions
        if rule_execution_mode is not None:
            input_["rule_execution_mode"] = rule_execution_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_detector_version_metadata(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        detector_version_id: "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString",
        description: "capo_frauddetector.types.description.description",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.update_detector_version_metadata_result.UpdateDetectorVersionMetadataResult":
        """<p>Updates the detector version's description. You can update the metadata for any detector version (<code>DRAFT, ACTIVE,</code> or <code>INACTIVE</code>). </p>

        Args:
            detector_id: <p>The detector ID.</p>
            detector_version_id: <p>The detector version ID. </p>
            description: <p>The description.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_detector_version_metadata_request.UpdateDetectorVersionMetadataRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_detector_version_metadata_result.UpdateDetectorVersionMetadataResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_detector_version_metadata

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_detector_version_metadata.update_detector_version_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_detector_version_metadata_request.UpdateDetectorVersionMetadataRequest = {
            "detector_id": detector_id,
            "detector_version_id": detector_version_id,
            "description": description,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_detector_version_status(
        self,
        detector_id: "capo_frauddetector.types.identifier.identifier",
        detector_version_id: "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString",
        status: "capo_frauddetector.types.detector_version_status.DetectorVersionStatus",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.update_detector_version_status_result.UpdateDetectorVersionStatusResult":
        """<p>Updates the detector version’s status. You can perform the following promotions or demotions using <code>UpdateDetectorVersionStatus</code>: <code>DRAFT</code> to <code>ACTIVE</code>, <code>ACTIVE</code> to <code>INACTIVE</code>, and <code>INACTIVE</code> to <code>ACTIVE</code>.</p>

        Args:
            detector_id: <p>The detector ID. </p>
            detector_version_id: <p>The detector version ID. </p>
            status: <p>The new status.</p> <p>The only supported values are <code>ACTIVE</code> and <code>INACTIVE</code> </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_detector_version_status_request.UpdateDetectorVersionStatusRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_detector_version_status_result.UpdateDetectorVersionStatusResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_detector_version_status

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_detector_version_status.update_detector_version_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_detector_version_status_request.UpdateDetectorVersionStatusRequest = {
            "detector_id": detector_id,
            "detector_version_id": detector_version_id,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_event_label(
        self,
        event_id: "capo_frauddetector.types.identifier.identifier",
        event_type_name: "capo_frauddetector.types.identifier.identifier",
        assigned_label: "capo_frauddetector.types.identifier.identifier",
        label_timestamp: "capo_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.update_event_label_result.UpdateEventLabelResult":
        """<p>Updates the specified event with a new label.</p>

        Args:
            event_id: <p>The ID of the event associated with the label to update.</p>
            event_type_name: <p>The event type of the event associated with the label to update.</p>
            assigned_label: <p>The new label to assign to the event.</p>
            label_timestamp: <p>The timestamp associated with the label. The timestamp must be specified using ISO 8601 standard in UTC. </p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_event_label_request.UpdateEventLabelRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_event_label_result.UpdateEventLabelResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_event_label

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_event_label.update_event_label(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_event_label_request.UpdateEventLabelRequest = {
            "event_id": event_id,
            "event_type_name": event_type_name,
            "assigned_label": assigned_label,
            "label_timestamp": label_timestamp,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_list(
        self,
        name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        elements: Optional[
            "capo_frauddetector.types.elements_list.ElementsList"
        ] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        update_mode: Optional[
            "capo_frauddetector.types.list_update_mode.ListUpdateMode"
        ] = None,
        variable_type: Optional[
            "capo_frauddetector.types.variable_type.variableType"
        ] = None,
    ) -> "capo_frauddetector.types.update_list_result.UpdateListResult":
        """<p> Updates a list. </p>

        Args:
            name: <p> The name of the list to update. </p>
            elements: <p> One or more list elements to add or replace. If you are providing the elements, make sure to specify the <code>updateMode</code> to use. </p> <p>If you are deleting all elements from the list, use <code>REPLACE</code> for the <code>updateMode</code> and provide an empty list (0 elements).</p>
            description: <p> The new description. </p>
            update_mode: <p> The update mode (type). </p> <ul> <li> <p>Use <code>APPEND</code> if you are adding elements to the list.</p> </li> <li> <p>Use <code>REPLACE</code> if you replacing existing elements in the list.</p> </li> <li> <p>Use <code>REMOVE</code> if you are removing elements from the list.</p> </li> </ul>
            variable_type: <p> The variable type you want to assign to the list. </p> <note> <p>You cannot update a variable type of a list that already has a variable type assigned to it. You can assign a variable type to a list only if the list does not already have a variable type.</p> </note>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_list_request.UpdateListRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_list_result.UpdateListResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_list

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_list.update_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_list_request.UpdateListRequest = {
            "name": name
        }
        if elements is not None:
            input_["elements"] = elements
        if description is not None:
            input_["description"] = description
        if update_mode is not None:
            input_["update_mode"] = update_mode
        if variable_type is not None:
            input_["variable_type"] = variable_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_model(
        self,
        model_id: "capo_frauddetector.types.model_identifier.modelIdentifier",
        model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
    ) -> "capo_frauddetector.types.update_model_result.UpdateModelResult":
        """<p>Updates model description.</p>

        Args:
            model_id: <p>The model ID.</p>
            model_type: <p>The model type.</p>
            description: <p>The new model description.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_model_request.UpdateModelRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_model_result.UpdateModelResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_model

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_model.update_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_model_request.UpdateModelRequest = {
            "model_id": model_id,
            "model_type": model_type,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_model_version(
        self,
        model_id: "capo_frauddetector.types.model_identifier.modelIdentifier",
        model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum",
        major_version_number: "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        external_events_detail: Optional[
            "capo_frauddetector.types.external_events_detail.ExternalEventsDetail"
        ] = None,
        ingested_events_detail: Optional[
            "capo_frauddetector.types.ingested_events_detail.IngestedEventsDetail"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> (
        "capo_frauddetector.types.update_model_version_result.UpdateModelVersionResult"
    ):
        """<p>Updates a model version. Updating a model version retrains an existing model version using updated training data and produces a new minor version of the model. You can update the training data set location and data access role attributes using this action. This action creates and trains a new minor version of the model, for example version 1.01, 1.02, 1.03.</p>

        Args:
            model_id: <p>The model ID.</p>
            model_type: <p>The model type.</p>
            major_version_number: <p>The major version number.</p>
            external_events_detail: <p>The details of the external events data used for training the model version. Required if <code>trainingDataSource</code> is <code>EXTERNAL_EVENTS</code>.</p>
            ingested_events_detail: <p>The details of the ingested event used for training the model version. Required if your <code>trainingDataSource</code> is <code>INGESTED_EVENTS</code>.</p>
            tags: <p>A collection of key and value pairs.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_model_version_request.UpdateModelVersionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_model_version_result.UpdateModelVersionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_model_version

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_model_version.update_model_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_model_version_request.UpdateModelVersionRequest = {
            "model_id": model_id,
            "model_type": model_type,
            "major_version_number": major_version_number,
        }
        if external_events_detail is not None:
            input_["external_events_detail"] = external_events_detail
        if ingested_events_detail is not None:
            input_["ingested_events_detail"] = ingested_events_detail
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_model_version_status(
        self,
        model_id: "capo_frauddetector.types.model_identifier.modelIdentifier",
        model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum",
        model_version_number: "capo_frauddetector.types.float_version_string.floatVersionString",
        status: "capo_frauddetector.types.model_version_status.ModelVersionStatus",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> "capo_frauddetector.types.update_model_version_status_result.UpdateModelVersionStatusResult":
        """<p>Updates the status of a model version.</p> <p>You can perform the following status updates:</p> <ol> <li> <p>Change the <code>TRAINING_IN_PROGRESS</code> status to <code>TRAINING_CANCELLED</code>.</p> </li> <li> <p>Change the <code>TRAINING_COMPLETE</code> status to <code>ACTIVE</code>.</p> </li> <li> <p>Change <code>ACTIVE</code> to <code>INACTIVE</code>.</p> </li> </ol>

        Args:
            model_id: <p>The model ID of the model version to update.</p>
            model_type: <p>The model type.</p>
            model_version_number: <p>The model version number.</p>
            status: <p>The model version status.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_model_version_status_request.UpdateModelVersionStatusRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_model_version_status_result.UpdateModelVersionStatusResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_model_version_status

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_model_version_status.update_model_version_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_model_version_status_request.UpdateModelVersionStatusRequest = {
            "model_id": model_id,
            "model_type": model_type,
            "model_version_number": model_version_number,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rule_metadata(
        self,
        rule: "capo_frauddetector.types.rule.Rule",
        description: "capo_frauddetector.types.description.description",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
    ) -> (
        "capo_frauddetector.types.update_rule_metadata_result.UpdateRuleMetadataResult"
    ):
        """<p>Updates a rule's metadata. The description attribute can be updated.</p>

        Args:
            rule: <p>The rule to update.</p>
            description: <p>The rule description.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_rule_metadata_request.UpdateRuleMetadataRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_rule_metadata_result.UpdateRuleMetadataResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_rule_metadata

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_rule_metadata.update_rule_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_rule_metadata_request.UpdateRuleMetadataRequest = {
            "rule": rule,
            "description": description,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rule_version(
        self,
        rule: "capo_frauddetector.types.rule.Rule",
        expression: "capo_frauddetector.types.rule_expression.ruleExpression",
        language: "capo_frauddetector.types.language.Language",
        outcomes: "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        description: Optional[
            "capo_frauddetector.types.description.description"
        ] = None,
        tags: Optional["capo_frauddetector.types.tag_list.tagList"] = None,
    ) -> "capo_frauddetector.types.update_rule_version_result.UpdateRuleVersionResult":
        """<p>Updates a rule version resulting in a new rule version. Updates a rule version resulting in a new rule version (version 1, 2, 3 ...). </p>

        Args:
            rule: <p>The rule to update.</p>
            description: <p>The description.</p>
            expression: <p>The rule expression.</p>
            language: <p>The language.</p>
            outcomes: <p>The outcomes.</p>
            tags: <p>The tags to assign to the rule version.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_rule_version_request.UpdateRuleVersionRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_rule_version_result.UpdateRuleVersionResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_rule_version

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_rule_version.update_rule_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_rule_version_request.UpdateRuleVersionRequest = {
            "rule": rule,
            "expression": expression,
            "language": language,
            "outcomes": outcomes,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_variable(
        self,
        name: "capo_frauddetector.types.string.string",
        *,
        config_overrides: Optional[FraudDetectorClientConfig] = None,
        default_value: Optional["capo_frauddetector.types.string.string"] = None,
        description: Optional["capo_frauddetector.types.string.string"] = None,
        variable_type: Optional["capo_frauddetector.types.string.string"] = None,
    ) -> "capo_frauddetector.types.update_variable_result.UpdateVariableResult":
        """<p>Updates a variable.</p>

        Args:
            name: <p>The name of the variable.</p>
            default_value: <p>The new default value of the variable.</p>
            description: <p>The new description.</p>
            variable_type: <p>The variable type. For more information see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types">Variable types</a>.</p>

        Raises:
            capo_frauddetector.errors.access_denied_exception.AccessDeniedException: <p>An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as <code>PutExternalModel</code>, that specifies a role that is not in your account.</p>
            capo_frauddetector.errors.conflict_exception.ConflictException: <p>An exception indicating there was a conflict during a delete operation.</p>
            capo_frauddetector.errors.internal_server_exception.InternalServerException: <p>An exception indicating an internal server error.</p>
            capo_frauddetector.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception indicating the specified resource was not found.</p>
            capo_frauddetector.errors.throttling_exception.ThrottlingException: <p>An exception indicating a throttling error.</p>
            capo_frauddetector.errors.validation_exception.ValidationException: <p>An exception indicating a specified value is not allowed.</p>
            capo_frauddetector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_frauddetector.types.update_variable_request.UpdateVariableRequest]",
        ) -> OperationResponse[
            "capo_frauddetector.types.update_variable_result.UpdateVariableResult"
        ]:
            import capo_frauddetector._operations.aws_hawks_nest_service_facade.update_variable

            output, http_response = (
                capo_frauddetector._operations.aws_hawks_nest_service_facade.update_variable.update_variable(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_frauddetector.types.update_variable_request.UpdateVariableRequest = {
            "name": name
        }
        if default_value is not None:
            input_["default_value"] = default_value
        if description is not None:
            input_["description"] = description
        if variable_type is not None:
            input_["variable_type"] = variable_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
