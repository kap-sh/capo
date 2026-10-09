"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#AmazonSageMakerFeatureStoreRuntime``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_sagemaker_featurestore_runtime._auth._signers
import capo_sagemaker_featurestore_runtime._auth._sigv4
from capo_sagemaker_featurestore_runtime._auth._identity import Credentials
from capo_sagemaker_featurestore_runtime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemaker_featurestore_runtime._auth._zapros_handler import AuthMiddleware
from capo_sagemaker_featurestore_runtime._pagination import (
    resolve_path as _resolve_path,
)
from capo_sagemaker_featurestore_runtime._services._aws_config import aws_config
from capo_sagemaker_featurestore_runtime._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_identifiers
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_request
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_response
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_entries
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_request
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_response
    import capo_sagemaker_featurestore_runtime.types.boolean
    import capo_sagemaker_featurestore_runtime.types.delete_record_request
    import capo_sagemaker_featurestore_runtime.types.deletion_mode
    import capo_sagemaker_featurestore_runtime.types.expiration_time_response
    import capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn
    import capo_sagemaker_featurestore_runtime.types.feature_names
    import capo_sagemaker_featurestore_runtime.types.get_record_request
    import capo_sagemaker_featurestore_runtime.types.get_record_response
    import capo_sagemaker_featurestore_runtime.types.list_records_max_results
    import capo_sagemaker_featurestore_runtime.types.list_records_next_token
    import capo_sagemaker_featurestore_runtime.types.list_records_request
    import capo_sagemaker_featurestore_runtime.types.list_records_response
    import capo_sagemaker_featurestore_runtime.types.put_record_request
    import capo_sagemaker_featurestore_runtime.types.record
    import capo_sagemaker_featurestore_runtime.types.target_stores
    import capo_sagemaker_featurestore_runtime.types.ttl_duration
    import capo_sagemaker_featurestore_runtime.types.update_record_request
    import capo_sagemaker_featurestore_runtime.types.value_as_string


class SageMakerFeatureStoreRuntimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class SageMakerFeatureStoreRuntimeClient:
    """A client for the ``SageMakerFeatureStoreRuntime`` service.

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
        self._config = SageMakerFeatureStoreRuntimeClientConfig(
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
        self,
        config_overrides: Optional[SageMakerFeatureStoreRuntimeClientConfig] = None,
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SageMakerFeatureStoreRuntimeClientConfig = config_overrides or {}
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

    def batch_get_record(
        self,
        *,
        config_overrides: Optional[SageMakerFeatureStoreRuntimeClientConfig] = None,
        identifiers: Optional[
            "capo_sagemaker_featurestore_runtime.types.batch_get_record_identifiers.BatchGetRecordIdentifiers"
        ] = None,
        expiration_time_response: Optional[
            "capo_sagemaker_featurestore_runtime.types.expiration_time_response.ExpirationTimeResponse"
        ] = None,
    ) -> "capo_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse":
        """<p>Retrieves a batch of <code>Records</code> from a <code>FeatureGroup</code>.</p>

        Args:
            identifiers: <p>A list containing the name or Amazon Resource Name (ARN) of the <code>FeatureGroup</code>, the list of names of <code>Feature</code>s to be retrieved, and the corresponding <code>RecordIdentifier</code> values as strings.</p>
            expiration_time_response: <p>Parameter to request <code>ExpiresAt</code> in response. If <code>Enabled</code>, <code>BatchGetRecord</code> will return the value of <code>ExpiresAt</code>, if it is not null. If <code>Disabled</code> and null, <code>BatchGetRecord</code> will return null.</p>

        Raises:
            capo_sagemaker_featurestore_runtime.errors.access_forbidden.AccessForbidden: <p>You do not have permission to perform an action.</p>
            capo_sagemaker_featurestore_runtime.errors.internal_failure.InternalFailure: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_featurestore_runtime.errors.service_unavailable.ServiceUnavailable: <p>The service is currently unavailable.</p>
            capo_sagemaker_featurestore_runtime.errors.validation_error.ValidationError: <p>There was an error validating your request.</p>
            capo_sagemaker_featurestore_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_featurestore_runtime.types.batch_get_record_request.BatchGetRecordRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse"
        ]:
            import capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.batch_get_record

            output, http_response = (
                capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.batch_get_record.batch_get_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_featurestore_runtime.types.batch_get_record_request.BatchGetRecordRequest = {}
        if identifiers is not None:
            input_["identifiers"] = identifiers
        if expiration_time_response is not None:
            input_["expiration_time_response"] = expiration_time_response

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_write_record(
        self,
        *,
        config_overrides: Optional[SageMakerFeatureStoreRuntimeClientConfig] = None,
        entries: Optional[
            "capo_sagemaker_featurestore_runtime.types.batch_write_record_entries.BatchWriteRecordEntries"
        ] = None,
        ttl_duration: Optional[
            "capo_sagemaker_featurestore_runtime.types.ttl_duration.TtlDuration"
        ] = None,
    ) -> "capo_sagemaker_featurestore_runtime.types.batch_write_record_response.BatchWriteRecordResponse":
        """<p>Writes a batch of <code>Records</code> to one or more <code>FeatureGroup</code>s. Use this API for bulk ingestion of records into the <code>OnlineStore</code> and <code>OfflineStore</code>.</p> <p>You can set the ingested records to expire at a given time to live (TTL) duration after the record's event time by specifying the <code>TtlDuration</code> parameter. A request level <code>TtlDuration</code> applies to all entries that do not specify their own <code>TtlDuration</code>.</p>

        Args:
            entries: <p>A list of records to write. Each entry specifies the <code>FeatureGroup</code>, the record data, and optionally target stores and a TTL duration.</p>
            ttl_duration: <p>Time to live duration applied to all entries in the batch that do not specify their own <code>TtlDuration</code>; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. For information on HardDelete, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html">DeleteRecord</a> API in the Amazon SageMaker API Reference guide.</p>

        Raises:
            capo_sagemaker_featurestore_runtime.errors.access_forbidden.AccessForbidden: <p>You do not have permission to perform an action.</p>
            capo_sagemaker_featurestore_runtime.errors.internal_failure.InternalFailure: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_featurestore_runtime.errors.resource_not_found.ResourceNotFound: <p>A resource that is required to perform an action was not found.</p>
            capo_sagemaker_featurestore_runtime.errors.service_unavailable.ServiceUnavailable: <p>The service is currently unavailable.</p>
            capo_sagemaker_featurestore_runtime.errors.validation_error.ValidationError: <p>There was an error validating your request.</p>
            capo_sagemaker_featurestore_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Write records to multiple feature groups

            >>> client.batch_write_record(entries=[{'FeatureGroupName': 'my-feature-group', 'Record': [{'FeatureName': 'customer_id', 'ValueAsString': 'cust-001'}, {'FeatureName': 'age', 'ValueAsString': '25'}]}])
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_featurestore_runtime.types.batch_write_record_request.BatchWriteRecordRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_featurestore_runtime.types.batch_write_record_response.BatchWriteRecordResponse"
        ]:
            import capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.batch_write_record

            output, http_response = (
                capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.batch_write_record.batch_write_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_featurestore_runtime.types.batch_write_record_request.BatchWriteRecordRequest = {}
        if entries is not None:
            input_["entries"] = entries
        if ttl_duration is not None:
            input_["ttl_duration"] = ttl_duration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_record(
        self,
        feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn",
        *,
        config_overrides: Optional[SageMakerFeatureStoreRuntimeClientConfig] = None,
        record_identifier_value_as_string: Optional[
            "capo_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
        ] = None,
        event_time: Optional[
            "capo_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
        ] = None,
        target_stores: Optional[
            "capo_sagemaker_featurestore_runtime.types.target_stores.TargetStores"
        ] = None,
        deletion_mode: Optional[
            "capo_sagemaker_featurestore_runtime.types.deletion_mode.DeletionMode"
        ] = None,
    ) -> None:
        """<p>Deletes a <code>Record</code> from a <code>FeatureGroup</code> in the <code>OnlineStore</code>. Feature Store supports both <code>SoftDelete</code> and <code>HardDelete</code>. For <code>SoftDelete</code> (default), feature columns are set to <code>null</code> and the record is no longer retrievable by <code>GetRecord</code> or <code>BatchGetRecord</code>. For <code>HardDelete</code>, the complete <code>Record</code> is removed from the <code>OnlineStore</code>. In both cases, Feature Store appends the deleted record marker to the <code>OfflineStore</code>. The deleted record marker is a record with the same <code>RecordIdentifer</code> as the original, but with <code>is_deleted</code> value set to <code>True</code>, <code>EventTime</code> set to the delete input <code>EventTime</code>, and other feature values set to <code>null</code>.</p> <p>Note that the <code>EventTime</code> specified in <code>DeleteRecord</code> should be set later than the <code>EventTime</code> of the existing record in the <code>OnlineStore</code> for that <code>RecordIdentifer</code>. If it is not, the deletion does not occur:</p> <ul> <li> <p>For <code>SoftDelete</code>, the existing (not deleted) record remains in the <code>OnlineStore</code>, though the delete record marker is still written to the <code>OfflineStore</code>.</p> </li> <li> <p> <code>HardDelete</code> returns <code>EventTime</code>: <code>400 ValidationException</code> to indicate that the delete operation failed. No delete record marker is written to the <code>OfflineStore</code>.</p> </li> </ul> <p>When a record is deleted from the <code>OnlineStore</code>, the deleted record marker is appended to the <code>OfflineStore</code>. If you have the Iceberg table format enabled for your <code>OfflineStore</code>, you can remove all history of a record from the <code>OfflineStore</code> using Amazon Athena or Apache Spark. For information on how to hard delete a record from the <code>OfflineStore</code> with the Iceberg table format enabled, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-delete-records.html#feature-store-delete-records-offline-store">Delete records from the offline store</a>.</p>

        Args:
            feature_group_name: <p>The name or Amazon Resource Name (ARN) of the feature group to delete the record from. </p>
            record_identifier_value_as_string: <p>The value for the <code>RecordIdentifier</code> that uniquely identifies the record, in string format. </p>
            event_time: <p>Timestamp indicating when the deletion event occurred. <code>EventTime</code> can be used to query data at a certain point in time.</p>
            target_stores: <p>A list of stores from which you're deleting the record. By default, Feature Store deletes the record from all of the stores that you're using for the <code>FeatureGroup</code>.</p>
            deletion_mode: <p>The name of the deletion mode for deleting the record. By default, the deletion mode is set to <code>SoftDelete</code>.</p>

        Raises:
            capo_sagemaker_featurestore_runtime.errors.access_forbidden.AccessForbidden: <p>You do not have permission to perform an action.</p>
            capo_sagemaker_featurestore_runtime.errors.internal_failure.InternalFailure: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_featurestore_runtime.errors.service_unavailable.ServiceUnavailable: <p>The service is currently unavailable.</p>
            capo_sagemaker_featurestore_runtime.errors.validation_error.ValidationError: <p>There was an error validating your request.</p>
            capo_sagemaker_featurestore_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_featurestore_runtime.types.delete_record_request.DeleteRecordRequest]",
        ) -> OperationResponse[None]:
            import capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.delete_record

            output, http_response = (
                capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.delete_record.delete_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_featurestore_runtime.types.delete_record_request.DeleteRecordRequest = {
            "feature_group_name": feature_group_name
        }
        if record_identifier_value_as_string is not None:
            input_["record_identifier_value_as_string"] = (
                record_identifier_value_as_string
            )
        if event_time is not None:
            input_["event_time"] = event_time
        if target_stores is not None:
            input_["target_stores"] = target_stores
        if deletion_mode is not None:
            input_["deletion_mode"] = deletion_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_record(
        self,
        feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn",
        *,
        config_overrides: Optional[SageMakerFeatureStoreRuntimeClientConfig] = None,
        record_identifier_value_as_string: Optional[
            "capo_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
        ] = None,
        feature_names: Optional[
            "capo_sagemaker_featurestore_runtime.types.feature_names.FeatureNames"
        ] = None,
        expiration_time_response: Optional[
            "capo_sagemaker_featurestore_runtime.types.expiration_time_response.ExpirationTimeResponse"
        ] = None,
    ) -> "capo_sagemaker_featurestore_runtime.types.get_record_response.GetRecordResponse":
        """<p>Use for <code>OnlineStore</code> serving from a <code>FeatureStore</code>. Only the latest records stored in the <code>OnlineStore</code> can be retrieved. If no Record with <code>RecordIdentifierValue</code> is found, then an empty result is returned. </p>

        Args:
            feature_group_name: <p>The name or Amazon Resource Name (ARN) of the feature group from which you want to retrieve a record.</p>
            record_identifier_value_as_string: <p>The value that corresponds to <code>RecordIdentifier</code> type and uniquely identifies the record in the <code>FeatureGroup</code>. </p>
            feature_names: <p>List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.</p>
            expiration_time_response: <p>Parameter to request <code>ExpiresAt</code> in response. If <code>Enabled</code>, <code>GetRecord</code> will return the value of <code>ExpiresAt</code>, if it is not null. If <code>Disabled</code> and null, <code>GetRecord</code> will return null.</p>

        Raises:
            capo_sagemaker_featurestore_runtime.errors.access_forbidden.AccessForbidden: <p>You do not have permission to perform an action.</p>
            capo_sagemaker_featurestore_runtime.errors.internal_failure.InternalFailure: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_featurestore_runtime.errors.resource_not_found.ResourceNotFound: <p>A resource that is required to perform an action was not found.</p>
            capo_sagemaker_featurestore_runtime.errors.service_unavailable.ServiceUnavailable: <p>The service is currently unavailable.</p>
            capo_sagemaker_featurestore_runtime.errors.validation_error.ValidationError: <p>There was an error validating your request.</p>
            capo_sagemaker_featurestore_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_featurestore_runtime.types.get_record_request.GetRecordRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_featurestore_runtime.types.get_record_response.GetRecordResponse"
        ]:
            import capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.get_record

            output, http_response = (
                capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.get_record.get_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_featurestore_runtime.types.get_record_request.GetRecordRequest = {
            "feature_group_name": feature_group_name
        }
        if record_identifier_value_as_string is not None:
            input_["record_identifier_value_as_string"] = (
                record_identifier_value_as_string
            )
        if feature_names is not None:
            input_["feature_names"] = feature_names
        if expiration_time_response is not None:
            input_["expiration_time_response"] = expiration_time_response

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_records(
        self,
        feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn",
        *,
        config_overrides: Optional[SageMakerFeatureStoreRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_sagemaker_featurestore_runtime.types.list_records_max_results.ListRecordsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_sagemaker_featurestore_runtime.types.list_records_next_token.ListRecordsNextToken"
        ] = None,
        include_soft_deleted_records: Optional[
            "capo_sagemaker_featurestore_runtime.types.boolean.Boolean"
        ] = None,
    ) -> "capo_sagemaker_featurestore_runtime.types.list_records_response.ListRecordsResponse":
        """<p>Lists the <code>RecordIdentifier</code> values of all records stored in a <code>FeatureGroup</code>'s <code>OnlineStore</code>. This enables you to discover which records exist without retrieving the full record data.</p>

        Args:
            feature_group_name: <p>The name or Amazon Resource Name (ARN) of the feature group to list records from.</p>
            max_results: <p>The maximum number of record identifiers to return in a single page of results. For the <code>InMemory</code> tier, this value is a hint and not a strict requirement. The response may contain more or fewer results than the specified <code>MaxResults</code>.</p>
            next_token: <p>A token to resume pagination of <code>ListRecords</code> results.</p>
            include_soft_deleted_records: <p>If set to <code>true</code>, the result includes records that have been soft deleted.</p>

        Raises:
            capo_sagemaker_featurestore_runtime.errors.access_forbidden.AccessForbidden: <p>You do not have permission to perform an action.</p>
            capo_sagemaker_featurestore_runtime.errors.internal_failure.InternalFailure: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_featurestore_runtime.errors.resource_not_found.ResourceNotFound: <p>A resource that is required to perform an action was not found.</p>
            capo_sagemaker_featurestore_runtime.errors.service_unavailable.ServiceUnavailable: <p>The service is currently unavailable.</p>
            capo_sagemaker_featurestore_runtime.errors.validation_error.ValidationError: <p>There was an error validating your request.</p>
            capo_sagemaker_featurestore_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List record identifiers from a feature group

            >>> client.list_records(feature_group_name='my-feature-group', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_featurestore_runtime.types.list_records_request.ListRecordsRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_featurestore_runtime.types.list_records_response.ListRecordsResponse"
        ]:
            import capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.list_records

            output, http_response = (
                capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.list_records.list_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_featurestore_runtime.types.list_records_request.ListRecordsRequest = {
            "feature_group_name": feature_group_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_soft_deleted_records is not None:
            input_["include_soft_deleted_records"] = include_soft_deleted_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_records(
        self,
        feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn",
        *,
        config_overrides: Optional[SageMakerFeatureStoreRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_sagemaker_featurestore_runtime.types.list_records_max_results.ListRecordsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_sagemaker_featurestore_runtime.types.list_records_next_token.ListRecordsNextToken"
        ] = None,
        include_soft_deleted_records: Optional[
            "capo_sagemaker_featurestore_runtime.types.boolean.Boolean"
        ] = None,
    ) -> "Iterator[capo_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString]":
        _token = next_token
        while True:
            _response = self.list_records(
                feature_group_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                include_soft_deleted_records=include_soft_deleted_records,
            )
            _page = _resolve_path(_response, ("record_identifiers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_record(
        self,
        feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn",
        *,
        config_overrides: Optional[SageMakerFeatureStoreRuntimeClientConfig] = None,
        record: Optional[
            "capo_sagemaker_featurestore_runtime.types.record.Record"
        ] = None,
        target_stores: Optional[
            "capo_sagemaker_featurestore_runtime.types.target_stores.TargetStores"
        ] = None,
        ttl_duration: Optional[
            "capo_sagemaker_featurestore_runtime.types.ttl_duration.TtlDuration"
        ] = None,
    ) -> None:
        """<p>The <code>PutRecord</code> API is used to ingest a list of <code>Records</code> into your feature group. </p> <p>If a new record’s <code>EventTime</code> is greater, the new record is written to both the <code>OnlineStore</code> and <code>OfflineStore</code>. Otherwise, the record is a historic record and it is written only to the <code>OfflineStore</code>. </p> <p>You can specify the ingestion to be applied to the <code>OnlineStore</code>, <code>OfflineStore</code>, or both by using the <code>TargetStores</code> request parameter. </p> <p>You can set the ingested record to expire at a given time to live (TTL) duration after the record’s event time, <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>, by specifying the <code>TtlDuration</code> parameter. A record level <code>TtlDuration</code> is set when specifying the <code>TtlDuration</code> parameter using the <code>PutRecord</code> API call. If the input <code>TtlDuration</code> is <code>null</code> or unspecified, <code>TtlDuration</code> is set to the default feature group level <code>TtlDuration</code>. A record level <code>TtlDuration</code> supersedes the group level <code>TtlDuration</code>.</p>

        Args:
            feature_group_name: <p>The name or Amazon Resource Name (ARN) of the feature group that you want to insert the record into.</p>
            record: <p>List of FeatureValues to be inserted. This will be a full over-write. If you only want to update few of the feature values, do the following:</p> <ul> <li> <p>Use <code>GetRecord</code> to retrieve the latest record.</p> </li> <li> <p>Update the record returned from <code>GetRecord</code>. </p> </li> <li> <p>Use <code>PutRecord</code> to update feature values.</p> </li> </ul>
            target_stores: <p>A list of stores to which you're adding the record. By default, Feature Store adds the record to all of the stores that you're using for the <code>FeatureGroup</code>.</p>
            ttl_duration: <p>Time to live duration, where the record is hard deleted after the expiration time is reached; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. For information on HardDelete, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html">DeleteRecord</a> API in the Amazon SageMaker API Reference guide.</p>

        Raises:
            capo_sagemaker_featurestore_runtime.errors.access_forbidden.AccessForbidden: <p>You do not have permission to perform an action.</p>
            capo_sagemaker_featurestore_runtime.errors.internal_failure.InternalFailure: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_featurestore_runtime.errors.service_unavailable.ServiceUnavailable: <p>The service is currently unavailable.</p>
            capo_sagemaker_featurestore_runtime.errors.validation_error.ValidationError: <p>There was an error validating your request.</p>
            capo_sagemaker_featurestore_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_featurestore_runtime.types.put_record_request.PutRecordRequest]",
        ) -> OperationResponse[None]:
            import capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.put_record

            output, http_response = (
                capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.put_record.put_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_featurestore_runtime.types.put_record_request.PutRecordRequest = {
            "feature_group_name": feature_group_name
        }
        if record is not None:
            input_["record"] = record
        if target_stores is not None:
            input_["target_stores"] = target_stores
        if ttl_duration is not None:
            input_["ttl_duration"] = ttl_duration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_record(
        self,
        feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn",
        *,
        config_overrides: Optional[SageMakerFeatureStoreRuntimeClientConfig] = None,
        record_identifier_value_as_string: Optional[
            "capo_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
        ] = None,
        features: Optional[
            "capo_sagemaker_featurestore_runtime.types.record.Record"
        ] = None,
        target_stores: Optional[
            "capo_sagemaker_featurestore_runtime.types.target_stores.TargetStores"
        ] = None,
        ttl_duration: Optional[
            "capo_sagemaker_featurestore_runtime.types.ttl_duration.TtlDuration"
        ] = None,
    ) -> None:
        """<p>Updates one or more feature values for an existing record in the specified feature group. Features that you do not include in the request remain unchanged. You can update up to 100 features per call.</p> <important> <p>This operation is available only for feature groups that use the <code>Standard_V2</code> or <code>InMemory</code> online store type.</p> </important> <p>The record must already exist. If the record does not exist or has been soft-deleted, the operation returns a <code>ResourceNotFound</code> error. To create a record, use <code>PutRecord</code>.</p> <p>If you provide an <code>EventTime</code> that is older than the record's current <code>EventTime</code>, the service rejects the update with a <code>ConflictException</code>. If the <code>EventTime</code> is equal to or newer than the current value, the service applies the update. If you omit <code>EventTime</code>, the service keeps the record's existing <code>EventTime</code> and applies the update.</p> <p>If you specify a <code>TtlDuration</code>, you must also provide an <code>EventTime</code> in the request. Otherwise, the operation returns a <code>ValidationError</code>.</p>

        Args:
            feature_group_name: <p>The identifier for the feature group that contains the record to update. You can specify one of the following:</p> <ul> <li> <p>The feature group name.</p> </li> <li> <p>The feature group Amazon Resource Name (ARN).</p> </li> </ul>
            record_identifier_value_as_string: <p>The value that uniquely identifies the record in the feature group. This must match the value defined by the feature group's record identifier feature.</p>
            features: <p>The feature values to write to the record.</p>
            target_stores: <p>The target stores for the record update. By default, Amazon SageMaker Feature Store updates the record in all stores associated with the <code>FeatureGroup</code>.</p>
            ttl_duration: <p>The time-to-live (TTL) duration for the record. Amazon SageMaker Feature Store deletes the record when <code>EventTime</code> + <code>TtlDuration</code> elapses. If you omit this parameter, the record's existing TTL setting remains unchanged. For information about <code>HardDelete</code>, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html">DeleteRecord</a> operation in the Amazon SageMaker API Reference.</p>

        Raises:
            capo_sagemaker_featurestore_runtime.errors.access_forbidden.AccessForbidden: <p>You do not have permission to perform an action.</p>
            capo_sagemaker_featurestore_runtime.errors.conflict_exception.ConflictException: <p>The service rejected the update because the provided <code>EventTime</code> is older than the record's current <code>EventTime</code>. To persist the update, retrieve the record's latest <code>EventTime</code> and resubmit the request with an <code>EventTime</code> that is equal to or newer than the current value.</p>
            capo_sagemaker_featurestore_runtime.errors.internal_failure.InternalFailure: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_featurestore_runtime.errors.resource_not_found.ResourceNotFound: <p>A resource that is required to perform an action was not found.</p>
            capo_sagemaker_featurestore_runtime.errors.service_unavailable.ServiceUnavailable: <p>The service is currently unavailable.</p>
            capo_sagemaker_featurestore_runtime.errors.validation_error.ValidationError: <p>There was an error validating your request.</p>
            capo_sagemaker_featurestore_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update specific features in a record

            >>> client.update_record(feature_group_name='my-feature-group', record_identifier_value_as_string='cust-001', features=[{'FeatureName': 'age', 'ValueAsString': '26'}, {'FeatureName': 'membership_tier', 'ValueAsString': 'gold'}, {'FeatureName': 'event_time', 'ValueAsString': '2026-07-26T12:00:00Z'}])
            Update features and set a time-to-live (TTL) duration

            >>> client.update_record(feature_group_name='my-feature-group', record_identifier_value_as_string='cust-001', features=[{'FeatureName': 'age', 'ValueAsString': '26'}, {'FeatureName': 'event_time', 'ValueAsString': '2026-07-26T12:00:00Z'}], ttl_duration={'Unit': 'Weeks', 'Value': 4})
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_featurestore_runtime.types.update_record_request.UpdateRecordRequest]",
        ) -> OperationResponse[None]:
            import capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.update_record

            output, http_response = (
                capo_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.update_record.update_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_featurestore_runtime.types.update_record_request.UpdateRecordRequest = {
            "feature_group_name": feature_group_name
        }
        if record_identifier_value_as_string is not None:
            input_["record_identifier_value_as_string"] = (
                record_identifier_value_as_string
            )
        if features is not None:
            input_["features"] = features
        if target_stores is not None:
            input_["target_stores"] = target_stores
        if ttl_duration is not None:
            input_["ttl_duration"] = ttl_duration

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
