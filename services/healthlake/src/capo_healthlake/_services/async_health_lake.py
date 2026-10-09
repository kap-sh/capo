"""Generated from Smithy shape ``com.amazonaws.healthlake#HealthLake``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_healthlake._auth._signers
import capo_healthlake._auth._sigv4
from capo_healthlake._auth._identity import Credentials
from capo_healthlake._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_healthlake._auth._zapros_handler import AuthMiddleware
from capo_healthlake._pagination import resolve_path as _resolve_path
from capo_healthlake._services._aws_config import aaws_config
from capo_healthlake._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_healthlake.types.agent_input_message
    import capo_healthlake.types.amazon_resource_name
    import capo_healthlake.types.analytics_configuration
    import capo_healthlake.types.backup_configuration
    import capo_healthlake.types.bounded_length_string
    import capo_healthlake.types.change_description
    import capo_healthlake.types.client_token
    import capo_healthlake.types.client_token_string
    import capo_healthlake.types.conversation_id_string
    import capo_healthlake.types.create_data_transformation_profile_request
    import capo_healthlake.types.create_data_transformation_profile_response
    import capo_healthlake.types.create_data_transformation_profile_source
    import capo_healthlake.types.create_fhir_datastore_request
    import capo_healthlake.types.create_fhir_datastore_response
    import capo_healthlake.types.data_transformation_iam_role_arn
    import capo_healthlake.types.data_transformation_job_id
    import capo_healthlake.types.data_transformation_job_name
    import capo_healthlake.types.data_transformation_next_token
    import capo_healthlake.types.data_transformation_profile_summary
    import capo_healthlake.types.data_transformation_profile_version_summary
    import capo_healthlake.types.datastore_filter
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.datastore_name
    import capo_healthlake.types.date_time
    import capo_healthlake.types.default_enabled_boolean
    import capo_healthlake.types.delete_data_transformation_profile_request
    import capo_healthlake.types.delete_data_transformation_profile_response
    import capo_healthlake.types.delete_fhir_datastore_request
    import capo_healthlake.types.delete_fhir_datastore_response
    import capo_healthlake.types.describe_data_transformation_job_request
    import capo_healthlake.types.describe_data_transformation_job_response
    import capo_healthlake.types.describe_fhir_datastore_request
    import capo_healthlake.types.describe_fhir_datastore_response
    import capo_healthlake.types.describe_fhir_export_job_request
    import capo_healthlake.types.describe_fhir_export_job_response
    import capo_healthlake.types.describe_fhir_import_job_request
    import capo_healthlake.types.describe_fhir_import_job_response
    import capo_healthlake.types.fhir_version
    import capo_healthlake.types.get_data_transformation_profile_request
    import capo_healthlake.types.get_data_transformation_profile_response
    import capo_healthlake.types.health_lake_boolean
    import capo_healthlake.types.health_lake_timestamp
    import capo_healthlake.types.iam_role_arn
    import capo_healthlake.types.identity_provider_configuration
    import capo_healthlake.types.input_data_config
    import capo_healthlake.types.job_id
    import capo_healthlake.types.job_name
    import capo_healthlake.types.job_status
    import capo_healthlake.types.kms_key_id
    import capo_healthlake.types.list_data_transformation_jobs_request
    import capo_healthlake.types.list_data_transformation_jobs_response
    import capo_healthlake.types.list_data_transformation_profile_versions_request
    import capo_healthlake.types.list_data_transformation_profile_versions_response
    import capo_healthlake.types.list_data_transformation_profiles_request
    import capo_healthlake.types.list_data_transformation_profiles_response
    import capo_healthlake.types.list_fhir_datastores_request
    import capo_healthlake.types.list_fhir_datastores_response
    import capo_healthlake.types.list_fhir_export_jobs_request
    import capo_healthlake.types.list_fhir_export_jobs_response
    import capo_healthlake.types.list_fhir_import_jobs_request
    import capo_healthlake.types.list_fhir_import_jobs_response
    import capo_healthlake.types.list_tags_for_resource_request
    import capo_healthlake.types.list_tags_for_resource_response
    import capo_healthlake.types.max_results
    import capo_healthlake.types.max_results_integer
    import capo_healthlake.types.next_token
    import capo_healthlake.types.nlp_configuration
    import capo_healthlake.types.output_data_config
    import capo_healthlake.types.preload_data_config
    import capo_healthlake.types.profile_configuration
    import capo_healthlake.types.profile_description
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.profile_mapping
    import capo_healthlake.types.profile_name_string
    import capo_healthlake.types.profile_version
    import capo_healthlake.types.publish_data_transformation_profile_request
    import capo_healthlake.types.publish_data_transformation_profile_response
    import capo_healthlake.types.restore_configuration
    import capo_healthlake.types.restore_fhir_datastore_request
    import capo_healthlake.types.restore_fhir_datastore_response
    import capo_healthlake.types.source_format
    import capo_healthlake.types.sse_configuration
    import capo_healthlake.types.start_data_transformation_job_request
    import capo_healthlake.types.start_data_transformation_job_response
    import capo_healthlake.types.start_fhir_export_job_request
    import capo_healthlake.types.start_fhir_export_job_response
    import capo_healthlake.types.start_fhir_import_job_request
    import capo_healthlake.types.start_fhir_import_job_response
    import capo_healthlake.types.tag_key_list
    import capo_healthlake.types.tag_list
    import capo_healthlake.types.tag_map
    import capo_healthlake.types.tag_resource_request
    import capo_healthlake.types.tag_resource_response
    import capo_healthlake.types.transformation_input_data_config
    import capo_healthlake.types.transformation_job_status
    import capo_healthlake.types.transformation_job_summary
    import capo_healthlake.types.transformation_output_data_config
    import capo_healthlake.types.untag_resource_request
    import capo_healthlake.types.untag_resource_response
    import capo_healthlake.types.update_data_transformation_profile_request
    import capo_healthlake.types.update_data_transformation_profile_response
    import capo_healthlake.types.update_fhir_datastore_request
    import capo_healthlake.types.update_fhir_datastore_response
    import capo_healthlake.types.update_profile_with_agent_request
    import capo_healthlake.types.update_profile_with_agent_response
    import capo_healthlake.types.validation_level


class AsyncHealthLakeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncHealthLakeClient:
    """A client for the ``HealthLake`` service.

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
        self._config = AsyncHealthLakeClientConfig(
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
        self, config_overrides: Optional[AsyncHealthLakeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncHealthLakeClientConfig = config_overrides or {}
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

    async def create_data_transformation_profile(
        self,
        source_format: "capo_healthlake.types.source_format.SourceFormat",
        source: "capo_healthlake.types.create_data_transformation_profile_source.CreateDataTransformationProfileSource",
        profile_name: "capo_healthlake.types.profile_name_string.ProfileNameString",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        kms_key_id: Optional["capo_healthlake.types.kms_key_id.KmsKeyId"] = None,
        profile_description: Optional[
            "capo_healthlake.types.profile_description.ProfileDescription"
        ] = None,
        tags: Optional["capo_healthlake.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_healthlake.types.client_token.ClientToken"] = None,
    ) -> "capo_healthlake.types.create_data_transformation_profile_response.CreateDataTransformationProfileResponse":
        """<p>Creates a data transformation profile in DRAFT state. Specify a built-in starter profile, an existing profile version, raw profile content, or a sample data file as the source.</p>

        Args:
            source_format: <p>The source data format that this profile converts from (Consolidated Clinical Document Architecture (C-CDA) or Comma-separated values (CSV)).</p>
            source: <p>The source for the initial profile content. Specify a built-in starter profile, an existing profile version to clone, raw profile content for CI/CD workflows, or a sample data file in Amazon S3.</p>
            kms_key_id: <p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key identifier used to encrypt the profile content at rest.</p>
            profile_description: <p>A human-readable description of the profile's purpose.</p>
            profile_name: <p>A name for the data transformation profile.</p>
            tags: <p>The tags to associate with the profile at creation time.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.conflict_exception.ConflictException: <p>The data store is in a transition state and the user requested action cannot be performed.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.create_data_transformation_profile_request.CreateDataTransformationProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.create_data_transformation_profile_response.CreateDataTransformationProfileResponse"
        ]:
            import capo_healthlake._operations.health_lake.create_data_transformation_profile

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.create_data_transformation_profile.async_create_data_transformation_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.create_data_transformation_profile_request.CreateDataTransformationProfileRequest = {
            "source_format": source_format,
            "source": source,
            "profile_name": profile_name,
        }
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if profile_description is not None:
            input_["profile_description"] = profile_description
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_fhir_datastore(
        self,
        datastore_type_version: "capo_healthlake.types.fhir_version.FHIRVersion",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        datastore_name: Optional[
            "capo_healthlake.types.datastore_name.DatastoreName"
        ] = None,
        sse_configuration: Optional[
            "capo_healthlake.types.sse_configuration.SseConfiguration"
        ] = None,
        preload_data_config: Optional[
            "capo_healthlake.types.preload_data_config.PreloadDataConfig"
        ] = None,
        client_token: Optional[
            "capo_healthlake.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional["capo_healthlake.types.tag_list.TagList"] = None,
        identity_provider_configuration: Optional[
            "capo_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
        analytics_configuration: Optional[
            "capo_healthlake.types.analytics_configuration.AnalyticsConfiguration"
        ] = None,
        nlp_configuration: Optional[
            "capo_healthlake.types.nlp_configuration.NlpConfiguration"
        ] = None,
        profile_configuration: Optional[
            "capo_healthlake.types.profile_configuration.ProfileConfiguration"
        ] = None,
        backup_configuration: Optional[
            "capo_healthlake.types.backup_configuration.BackupConfiguration"
        ] = None,
    ) -> "capo_healthlake.types.create_fhir_datastore_response.CreateFHIRDatastoreResponse":
        """<p>Create a FHIR-enabled data store.</p>

        Args:
            datastore_name: <p>The data store name (user-generated).</p>
            datastore_type_version: <p>The FHIR release version supported by the data store. Current support is for version <code>R4</code>.</p>
            sse_configuration: <p>The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store. </p>
            preload_data_config: <p>An optional parameter to preload (import) open source Synthea FHIR data upon creation of the data store.</p>
            client_token: <p>An optional user-provided token to ensure API idempotency.</p>
            tags: <p>The resource tags applied to a data store when it is created.</p>
            identity_provider_configuration: <p>The identity provider configuration to use for the data store.</p>
            analytics_configuration: <p>The analytics configuration for the data store.</p>
            nlp_configuration: <p>The natural language processing (NLP) configuration for the data store.</p>
            profile_configuration: <p>The profile configuration for the data store.</p>
            backup_configuration: The backup configuration for the data store.

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.create_fhir_datastore_request.CreateFHIRDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.create_fhir_datastore_response.CreateFHIRDatastoreResponse"
        ]:
            import capo_healthlake._operations.health_lake.create_fhir_datastore

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.create_fhir_datastore.async_create_fhir_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.create_fhir_datastore_request.CreateFHIRDatastoreRequest = {
            "datastore_type_version": datastore_type_version
        }
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        if sse_configuration is not None:
            input_["sse_configuration"] = sse_configuration
        if preload_data_config is not None:
            input_["preload_data_config"] = preload_data_config
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration
        if analytics_configuration is not None:
            input_["analytics_configuration"] = analytics_configuration
        if nlp_configuration is not None:
            input_["nlp_configuration"] = nlp_configuration
        if profile_configuration is not None:
            input_["profile_configuration"] = profile_configuration
        if backup_configuration is not None:
            input_["backup_configuration"] = backup_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_transformation_profile(
        self,
        profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "capo_healthlake.types.delete_data_transformation_profile_response.DeleteDataTransformationProfileResponse":
        """<p>Deletes a data transformation profile and all its versions, including the DRAFT and all published versions.</p>

        Args:
            profile_id: <p>The unique identifier of the profile to delete.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.delete_data_transformation_profile_request.DeleteDataTransformationProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.delete_data_transformation_profile_response.DeleteDataTransformationProfileResponse"
        ]:
            import capo_healthlake._operations.health_lake.delete_data_transformation_profile

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.delete_data_transformation_profile.async_delete_data_transformation_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.delete_data_transformation_profile_request.DeleteDataTransformationProfileRequest = {
            "profile_id": profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_fhir_datastore(
        self,
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "capo_healthlake.types.delete_fhir_datastore_response.DeleteFHIRDatastoreResponse":
        """<p>Delete a FHIR-enabled data store.</p>

        Args:
            datastore_id: <p> The Amazon Web Services-generated identifier for the data store to be deleted.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.conflict_exception.ConflictException: <p>The data store is in a transition state and the user requested action cannot be performed.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.delete_fhir_datastore_request.DeleteFHIRDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.delete_fhir_datastore_response.DeleteFHIRDatastoreResponse"
        ]:
            import capo_healthlake._operations.health_lake.delete_fhir_datastore

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.delete_fhir_datastore.async_delete_fhir_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.delete_fhir_datastore_request.DeleteFHIRDatastoreRequest = {
            "datastore_id": datastore_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_data_transformation_job(
        self,
        job_id: "capo_healthlake.types.data_transformation_job_id.DataTransformationJobId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "capo_healthlake.types.describe_data_transformation_job_response.DescribeDataTransformationJobResponse":
        """<p>Describes a data transformation job, including its current status, configuration, and progress information.</p>

        Args:
            job_id: <p>The unique identifier of the data transformation job to describe.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.describe_data_transformation_job_request.DescribeDataTransformationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.describe_data_transformation_job_response.DescribeDataTransformationJobResponse"
        ]:
            import capo_healthlake._operations.health_lake.describe_data_transformation_job

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.describe_data_transformation_job.async_describe_data_transformation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.describe_data_transformation_job_request.DescribeDataTransformationJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_fhir_datastore(
        self,
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "capo_healthlake.types.describe_fhir_datastore_response.DescribeFHIRDatastoreResponse":
        """<p>Get properties for a FHIR-enabled data store.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>

        Raises:
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.describe_fhir_datastore_request.DescribeFHIRDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.describe_fhir_datastore_response.DescribeFHIRDatastoreResponse"
        ]:
            import capo_healthlake._operations.health_lake.describe_fhir_datastore

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.describe_fhir_datastore.async_describe_fhir_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.describe_fhir_datastore_request.DescribeFHIRDatastoreRequest = {
            "datastore_id": datastore_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_fhir_export_job(
        self,
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        job_id: "capo_healthlake.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "capo_healthlake.types.describe_fhir_export_job_response.DescribeFHIRExportJobResponse":
        """<p>Get FHIR export job properties.</p>

        Args:
            datastore_id: <p>The data store identifier from which FHIR data is being exported from.</p>
            job_id: <p>The export job identifier.</p>

        Raises:
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.describe_fhir_export_job_request.DescribeFHIRExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.describe_fhir_export_job_response.DescribeFHIRExportJobResponse"
        ]:
            import capo_healthlake._operations.health_lake.describe_fhir_export_job

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.describe_fhir_export_job.async_describe_fhir_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.describe_fhir_export_job_request.DescribeFHIRExportJobRequest = {
            "datastore_id": datastore_id,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_fhir_import_job(
        self,
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        job_id: "capo_healthlake.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "capo_healthlake.types.describe_fhir_import_job_response.DescribeFHIRImportJobResponse":
        """<p>Get the import job properties to learn more about the job or job progress.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            job_id: <p>The import job identifier.</p>

        Raises:
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.describe_fhir_import_job_request.DescribeFHIRImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.describe_fhir_import_job_response.DescribeFHIRImportJobResponse"
        ]:
            import capo_healthlake._operations.health_lake.describe_fhir_import_job

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.describe_fhir_import_job.async_describe_fhir_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.describe_fhir_import_job_request.DescribeFHIRImportJobRequest = {
            "datastore_id": datastore_id,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_transformation_profile(
        self,
        profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        profile_version: Optional[
            "capo_healthlake.types.profile_version.ProfileVersion"
        ] = None,
    ) -> "capo_healthlake.types.get_data_transformation_profile_response.GetDataTransformationProfileResponse":
        """<p>Retrieves a data transformation profile's metadata and profile content at a specific version. Specify version 0 to retrieve the DRAFT, a version number between 1 and 99 to retrieve a specific published version, or omit the version to retrieve the latest published version.</p>

        Args:
            profile_id: <p>The unique identifier of the profile to retrieve.</p>
            profile_version: <p>The version number to retrieve. Specify 0 to retrieve the DRAFT version. If you omit this parameter, the service returns the latest published version.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.get_data_transformation_profile_request.GetDataTransformationProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.get_data_transformation_profile_response.GetDataTransformationProfileResponse"
        ]:
            import capo_healthlake._operations.health_lake.get_data_transformation_profile

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.get_data_transformation_profile.async_get_data_transformation_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.get_data_transformation_profile_request.GetDataTransformationProfileRequest = {
            "profile_id": profile_id
        }
        if profile_version is not None:
            input_["profile_version"] = profile_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_transformation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        max_results: Optional["capo_healthlake.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
        ] = None,
        job_status: Optional[
            "capo_healthlake.types.transformation_job_status.TransformationJobStatus"
        ] = None,
        job_name: Optional[
            "capo_healthlake.types.data_transformation_job_name.DataTransformationJobName"
        ] = None,
        submitted_after: Optional["capo_healthlake.types.date_time.DateTime"] = None,
        submitted_before: Optional["capo_healthlake.types.date_time.DateTime"] = None,
    ) -> "capo_healthlake.types.list_data_transformation_jobs_response.ListDataTransformationJobsResponse":
        """<p>Lists data transformation jobs for your Amazon Web Services account. Results can be filtered by status, job name, and submit time window. Results are paginated. Use the <code>NextToken</code> parameter to retrieve additional results.</p>

        Args:
            max_results: <p>The maximum number of jobs to return per page. If you don't specify a value, the service returns up to 100 results.</p>
            next_token: <p>The pagination token from a previous response. Pass this value to retrieve the next page of results.</p>
            job_status: <p>Filters the results to include only jobs with the specified status.</p>
            job_name: <p>Filters the results to include only jobs with the specified name.</p>
            submitted_after: <p>Filters the results to include only jobs submitted at or after this timestamp.</p>
            submitted_before: <p>Filters the results to include only jobs submitted at or before this timestamp.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.list_data_transformation_jobs_request.ListDataTransformationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.list_data_transformation_jobs_response.ListDataTransformationJobsResponse"
        ]:
            import capo_healthlake._operations.health_lake.list_data_transformation_jobs

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.list_data_transformation_jobs.async_list_data_transformation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.list_data_transformation_jobs_request.ListDataTransformationJobsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if job_status is not None:
            input_["job_status"] = job_status
        if job_name is not None:
            input_["job_name"] = job_name
        if submitted_after is not None:
            input_["submitted_after"] = submitted_after
        if submitted_before is not None:
            input_["submitted_before"] = submitted_before

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_data_transformation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        max_results: Optional["capo_healthlake.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
        ] = None,
        job_status: Optional[
            "capo_healthlake.types.transformation_job_status.TransformationJobStatus"
        ] = None,
        job_name: Optional[
            "capo_healthlake.types.data_transformation_job_name.DataTransformationJobName"
        ] = None,
        submitted_after: Optional["capo_healthlake.types.date_time.DateTime"] = None,
        submitted_before: Optional["capo_healthlake.types.date_time.DateTime"] = None,
    ) -> "AsyncIterator[capo_healthlake.types.transformation_job_summary.TransformationJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_transformation_jobs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                job_status=job_status,
                job_name=job_name,
                submitted_after=submitted_after,
                submitted_before=submitted_before,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_transformation_profiles(
        self,
        source_format: "capo_healthlake.types.source_format.SourceFormat",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        max_results: Optional["capo_healthlake.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
        ] = None,
    ) -> "capo_healthlake.types.list_data_transformation_profiles_response.ListDataTransformationProfilesResponse":
        """<p>Lists all data transformation profiles in your account, returning the latest version summary for each. Use <code>GetDataTransformationProfile</code> to retrieve profile content. Results are paginated. Use the <code>NextToken</code> parameter to retrieve additional results.</p>

        Args:
            source_format: <p>Filters the results by source data format.</p>
            max_results: <p>The maximum number of profiles to return per page. If you don't specify a value, the service returns up to 100 results.</p>
            next_token: <p>The pagination token from a previous response. Pass this value to retrieve the next page of results.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.list_data_transformation_profiles_request.ListDataTransformationProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.list_data_transformation_profiles_response.ListDataTransformationProfilesResponse"
        ]:
            import capo_healthlake._operations.health_lake.list_data_transformation_profiles

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.list_data_transformation_profiles.async_list_data_transformation_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.list_data_transformation_profiles_request.ListDataTransformationProfilesRequest = {
            "source_format": source_format
        }
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

    async def iter_list_data_transformation_profiles(
        self,
        source_format: "capo_healthlake.types.source_format.SourceFormat",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        max_results: Optional["capo_healthlake.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_healthlake.types.data_transformation_profile_summary.DataTransformationProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_transformation_profiles(
                source_format,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_transformation_profile_versions(
        self,
        profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        max_results: Optional["capo_healthlake.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
        ] = None,
    ) -> "capo_healthlake.types.list_data_transformation_profile_versions_response.ListDataTransformationProfileVersionsResponse":
        """<p>Lists all versions of a specific data transformation profile (DRAFT and published), in reverse chronological order (newest first). Use <code>GetDataTransformationProfile</code> to retrieve profile content. Results are paginated. Use the <code>NextToken</code> parameter to retrieve additional results.</p>

        Args:
            profile_id: <p>The unique identifier of the profile whose versions to list.</p>
            max_results: <p>The maximum number of profile versions to return per page. If you don't specify a value, the service returns up to 100 results.</p>
            next_token: <p>The pagination token from a previous response. Pass this value to retrieve the next page of results.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.list_data_transformation_profile_versions_request.ListDataTransformationProfileVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.list_data_transformation_profile_versions_response.ListDataTransformationProfileVersionsResponse"
        ]:
            import capo_healthlake._operations.health_lake.list_data_transformation_profile_versions

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.list_data_transformation_profile_versions.async_list_data_transformation_profile_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.list_data_transformation_profile_versions_request.ListDataTransformationProfileVersionsRequest = {
            "profile_id": profile_id
        }
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

    async def iter_list_data_transformation_profile_versions(
        self,
        profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        max_results: Optional["capo_healthlake.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_healthlake.types.data_transformation_profile_version_summary.DataTransformationProfileVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_transformation_profile_versions(
                profile_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_fhir_datastores(
        self,
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        filter: Optional[
            "capo_healthlake.types.datastore_filter.DatastoreFilter"
        ] = None,
        next_token: Optional["capo_healthlake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_healthlake.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> (
        "capo_healthlake.types.list_fhir_datastores_response.ListFHIRDatastoresResponse"
    ):
        """<p>List all FHIR-enabled data stores in a user’s account, regardless of data store status.</p>

        Args:
            filter: <p>List all filters associated with a FHIR data store request.</p>
            next_token: <p>The token used to retrieve the next page of data stores when results are paginated.</p>
            max_results: <p>The maximum number of data stores returned on a page.</p>

        Raises:
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.list_fhir_datastores_request.ListFHIRDatastoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.list_fhir_datastores_response.ListFHIRDatastoresResponse"
        ]:
            import capo_healthlake._operations.health_lake.list_fhir_datastores

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.list_fhir_datastores.async_list_fhir_datastores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.list_fhir_datastores_request.ListFHIRDatastoresRequest = {}
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_list_fhir_datastores(
        self,
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        filter: Optional[
            "capo_healthlake.types.datastore_filter.DatastoreFilter"
        ] = None,
        next_token: Optional["capo_healthlake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_healthlake.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_healthlake.types.list_fhir_datastores_response.ListFHIRDatastoresResponse]":
        _token = next_token
        while True:
            _response = await self.list_fhir_datastores(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_fhir_export_jobs(
        self,
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        next_token: Optional["capo_healthlake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_healthlake.types.max_results_integer.MaxResultsInteger"
        ] = None,
        job_name: Optional["capo_healthlake.types.job_name.JobName"] = None,
        job_status: Optional["capo_healthlake.types.job_status.JobStatus"] = None,
        submitted_before: Optional[
            "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
        ] = None,
        submitted_after: Optional[
            "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
        ] = None,
    ) -> "capo_healthlake.types.list_fhir_export_jobs_response.ListFHIRExportJobsResponse":
        """<p>Lists all FHIR export jobs associated with an account and their statuses.</p>

        Args:
            datastore_id: <p>Limits the response to the export job with the specified data store ID. </p>
            next_token: <p>A pagination token used to identify the next page of results to return.</p>
            max_results: <p>Limits the number of results returned for a ListFHIRExportJobs to a maximum quantity specified by the user.</p>
            job_name: <p>Limits the response to the export job with the specified job name. </p>
            job_status: <p>Limits the response to export jobs with the specified job status. </p>
            submitted_before: <p>Limits the response to FHIR export jobs submitted before a user- specified date.</p>
            submitted_after: <p>Limits the response to FHIR export jobs submitted after a user-specified date.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.list_fhir_export_jobs_request.ListFHIRExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.list_fhir_export_jobs_response.ListFHIRExportJobsResponse"
        ]:
            import capo_healthlake._operations.health_lake.list_fhir_export_jobs

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.list_fhir_export_jobs.async_list_fhir_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.list_fhir_export_jobs_request.ListFHIRExportJobsRequest = {
            "datastore_id": datastore_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if job_name is not None:
            input_["job_name"] = job_name
        if job_status is not None:
            input_["job_status"] = job_status
        if submitted_before is not None:
            input_["submitted_before"] = submitted_before
        if submitted_after is not None:
            input_["submitted_after"] = submitted_after

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_fhir_export_jobs(
        self,
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        next_token: Optional["capo_healthlake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_healthlake.types.max_results_integer.MaxResultsInteger"
        ] = None,
        job_name: Optional["capo_healthlake.types.job_name.JobName"] = None,
        job_status: Optional["capo_healthlake.types.job_status.JobStatus"] = None,
        submitted_before: Optional[
            "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
        ] = None,
        submitted_after: Optional[
            "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
        ] = None,
    ) -> "AsyncIterator[capo_healthlake.types.list_fhir_export_jobs_response.ListFHIRExportJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_fhir_export_jobs(
                datastore_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                job_name=job_name,
                job_status=job_status,
                submitted_before=submitted_before,
                submitted_after=submitted_after,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_fhir_import_jobs(
        self,
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        next_token: Optional["capo_healthlake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_healthlake.types.max_results_integer.MaxResultsInteger"
        ] = None,
        job_name: Optional["capo_healthlake.types.job_name.JobName"] = None,
        job_status: Optional["capo_healthlake.types.job_status.JobStatus"] = None,
        submitted_before: Optional[
            "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
        ] = None,
        submitted_after: Optional[
            "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
        ] = None,
    ) -> "capo_healthlake.types.list_fhir_import_jobs_response.ListFHIRImportJobsResponse":
        """<p>List all FHIR import jobs associated with an account and their statuses.</p>

        Args:
            datastore_id: <p>Limits the response to the import job with the specified data store ID. </p>
            next_token: <p>The pagination token used to identify the next page of results to return.</p>
            max_results: <p>Limits the number of results returned for <code>ListFHIRImportJobs</code> to a maximum quantity specified by the user.</p>
            job_name: <p>Limits the response to the import job with the specified job name. </p>
            job_status: <p>Limits the response to the import job with the specified job status. </p>
            submitted_before: <p>Limits the response to FHIR import jobs submitted before a user- specified date. </p>
            submitted_after: <p>Limits the response to FHIR import jobs submitted after a user-specified date.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.list_fhir_import_jobs_request.ListFHIRImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.list_fhir_import_jobs_response.ListFHIRImportJobsResponse"
        ]:
            import capo_healthlake._operations.health_lake.list_fhir_import_jobs

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.list_fhir_import_jobs.async_list_fhir_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.list_fhir_import_jobs_request.ListFHIRImportJobsRequest = {
            "datastore_id": datastore_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if job_name is not None:
            input_["job_name"] = job_name
        if job_status is not None:
            input_["job_status"] = job_status
        if submitted_before is not None:
            input_["submitted_before"] = submitted_before
        if submitted_after is not None:
            input_["submitted_after"] = submitted_after

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_fhir_import_jobs(
        self,
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        next_token: Optional["capo_healthlake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_healthlake.types.max_results_integer.MaxResultsInteger"
        ] = None,
        job_name: Optional["capo_healthlake.types.job_name.JobName"] = None,
        job_status: Optional["capo_healthlake.types.job_status.JobStatus"] = None,
        submitted_before: Optional[
            "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
        ] = None,
        submitted_after: Optional[
            "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
        ] = None,
    ) -> "AsyncIterator[capo_healthlake.types.list_fhir_import_jobs_response.ListFHIRImportJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_fhir_import_jobs(
                datastore_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                job_name=job_name,
                job_status=job_status,
                submitted_before=submitted_before,
                submitted_after=submitted_after,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_healthlake.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "capo_healthlake.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of all existing tags associated with a data store.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the data store to which tags are being added.</p>

        Raises:
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_healthlake._operations.health_lake.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def publish_data_transformation_profile(
        self,
        profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString",
        source_format: "capo_healthlake.types.source_format.SourceFormat",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        from_existing_version: Optional[
            "capo_healthlake.types.profile_version.ProfileVersion"
        ] = None,
        change_description: Optional[
            "capo_healthlake.types.change_description.ChangeDescription"
        ] = None,
    ) -> "capo_healthlake.types.publish_data_transformation_profile_response.PublishDataTransformationProfileResponse":
        """<p>Promotes the current DRAFT version of a data transformation profile to a new immutable published version. Also supports rollback by publishing from a previously published version.</p>

        Args:
            profile_id: <p>The unique identifier of the profile to publish.</p>
            source_format: <p>The source data format of the profile.</p>
            from_existing_version: <p>The version number of a previously published version to republish as the new latest version. Use this parameter for rollback scenarios. If you omit this parameter, the service publishes the current DRAFT version.</p>
            change_description: <p>A description of what changed or why this version is being published.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.publish_data_transformation_profile_request.PublishDataTransformationProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.publish_data_transformation_profile_response.PublishDataTransformationProfileResponse"
        ]:
            import capo_healthlake._operations.health_lake.publish_data_transformation_profile

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.publish_data_transformation_profile.async_publish_data_transformation_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.publish_data_transformation_profile_request.PublishDataTransformationProfileRequest = {
            "profile_id": profile_id,
            "source_format": source_format,
        }
        if from_existing_version is not None:
            input_["from_existing_version"] = from_existing_version
        if change_description is not None:
            input_["change_description"] = change_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_fhir_datastore(
        self,
        source_datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        restore_configuration: "capo_healthlake.types.restore_configuration.RestoreConfiguration",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        datastore_name: Optional[
            "capo_healthlake.types.datastore_name.DatastoreName"
        ] = None,
        sse_configuration: Optional[
            "capo_healthlake.types.sse_configuration.SseConfiguration"
        ] = None,
        client_token: Optional[
            "capo_healthlake.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional["capo_healthlake.types.tag_list.TagList"] = None,
        identity_provider_configuration: Optional[
            "capo_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
        analytics_configuration: Optional[
            "capo_healthlake.types.analytics_configuration.AnalyticsConfiguration"
        ] = None,
        nlp_configuration: Optional[
            "capo_healthlake.types.nlp_configuration.NlpConfiguration"
        ] = None,
        profile_configuration: Optional[
            "capo_healthlake.types.profile_configuration.ProfileConfiguration"
        ] = None,
    ) -> "capo_healthlake.types.restore_fhir_datastore_response.RestoreFHIRDatastoreResponse":
        """Restore a backup-enabled data store to a point in time. Creates a new data store from the backup.

        Args:
            source_datastore_id: The identifier of the source data store to restore from.
            restore_configuration: The restore configuration specifying the type and parameters for the restore.
            datastore_name: The name for the restored data store.
            sse_configuration: The server-side encryption key configuration for the restored data store.
            client_token: An optional user-provided token to ensure API idempotency of the restore.
            tags: The resource tags applied to the restored data store.
            identity_provider_configuration: The identity provider configuration for the restored data store.
            analytics_configuration: The analytics configuration for the restored data store.
            nlp_configuration: The NLP configuration for the restored data store.
            profile_configuration: The profile configuration for the restored data store.

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.conflict_exception.ConflictException: <p>The data store is in a transition state and the user requested action cannot be performed.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Restore a data store to a point in time

            >>> await client.restore_fhir_datastore(source_datastore_id='source-datastore-id', restore_configuration={'ContinuousBackupRestoreConfiguration': {'RestorePointTime': '2026-08-01T00:00:00Z'}}, datastore_name='RestoredFhirDatastore')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.restore_fhir_datastore_request.RestoreFHIRDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.restore_fhir_datastore_response.RestoreFHIRDatastoreResponse"
        ]:
            import capo_healthlake._operations.health_lake.restore_fhir_datastore

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.restore_fhir_datastore.async_restore_fhir_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.restore_fhir_datastore_request.RestoreFHIRDatastoreRequest = {
            "source_datastore_id": source_datastore_id,
            "restore_configuration": restore_configuration,
        }
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        if sse_configuration is not None:
            input_["sse_configuration"] = sse_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration
        if analytics_configuration is not None:
            input_["analytics_configuration"] = analytics_configuration
        if nlp_configuration is not None:
            input_["nlp_configuration"] = nlp_configuration
        if profile_configuration is not None:
            input_["profile_configuration"] = profile_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_data_transformation_job(
        self,
        input_data_config: "capo_healthlake.types.transformation_input_data_config.TransformationInputDataConfig",
        output_data_config: "capo_healthlake.types.transformation_output_data_config.TransformationOutputDataConfig",
        data_access_role_arn: "capo_healthlake.types.data_transformation_iam_role_arn.DataTransformationIamRoleArn",
        client_token: "capo_healthlake.types.client_token.ClientToken",
        profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        job_name: Optional[
            "capo_healthlake.types.data_transformation_job_name.DataTransformationJobName"
        ] = None,
        drift_detection_enabled: Optional[bool] = None,
        provenance_enabled: Optional[bool] = None,
    ) -> "capo_healthlake.types.start_data_transformation_job_response.StartDataTransformationJobResponse":
        """<p>Starts an asynchronous data transformation job that converts source files from Amazon Simple Storage Service (Amazon S3) and writes the output to Amazon S3 or HealthLake.</p>

        Args:
            input_data_config: <p>The Amazon S3 location and format of the source files to transform.</p>
            output_data_config: <p>The Amazon S3 output location and Amazon Web Services Key Management Service (Amazon Web Services KMS) encryption configuration.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role that HealthLake assumes to read from and write to the specified Amazon S3 locations.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>
            job_name: <p>A descriptive name for the data transformation job.</p>
            profile_id: <p>The unique identifier of the data transformation profile to use for conversion.</p>
            drift_detection_enabled: <p>Specifies whether drift detection is enabled for this job. When enabled, HealthLake writes a drift report to the output Amazon S3 location alongside the converted files.</p>
            provenance_enabled: <p>Specifies whether FHIR R4 Provenance resource generation is enabled for this transformation job. When provenance is enabled, the service also generates related DocumentReference and Device resources. If you don't specify a value, the default is <code>true</code>. To disable provenance output, set this parameter to <code>false</code>.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.start_data_transformation_job_request.StartDataTransformationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.start_data_transformation_job_response.StartDataTransformationJobResponse"
        ]:
            import capo_healthlake._operations.health_lake.start_data_transformation_job

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.start_data_transformation_job.async_start_data_transformation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.start_data_transformation_job_request.StartDataTransformationJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "data_access_role_arn": data_access_role_arn,
            "client_token": client_token,
            "profile_id": profile_id,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if drift_detection_enabled is not None:
            input_["drift_detection_enabled"] = drift_detection_enabled
        if provenance_enabled is not None:
            input_["provenance_enabled"] = provenance_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_fhir_export_job(
        self,
        output_data_config: "capo_healthlake.types.output_data_config.OutputDataConfig",
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        data_access_role_arn: "capo_healthlake.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        job_name: Optional["capo_healthlake.types.job_name.JobName"] = None,
        client_token: Optional[
            "capo_healthlake.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_healthlake.types.start_fhir_export_job_response.StartFHIRExportJobResponse":
        """<p>Start a FHIR export job.</p>

        Args:
            job_name: <p>The export job name.</p>
            output_data_config: <p>The output data configuration supplied when the export job was started.</p>
            datastore_id: <p>The data store identifier from which files are being exported.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) used during initiation of the export job.</p>
            client_token: <p>An optional user provided token used for ensuring API idempotency.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.failed_dependency_exception.FailedDependencyException: <p>A dependent service failed to fulfill the request.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.start_fhir_export_job_request.StartFHIRExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.start_fhir_export_job_response.StartFHIRExportJobResponse"
        ]:
            import capo_healthlake._operations.health_lake.start_fhir_export_job

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.start_fhir_export_job.async_start_fhir_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.start_fhir_export_job_request.StartFHIRExportJobRequest = {
            "output_data_config": output_data_config,
            "datastore_id": datastore_id,
            "data_access_role_arn": data_access_role_arn,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_fhir_import_job(
        self,
        input_data_config: "capo_healthlake.types.input_data_config.InputDataConfig",
        job_output_data_config: "capo_healthlake.types.output_data_config.OutputDataConfig",
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        data_access_role_arn: "capo_healthlake.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        job_name: Optional["capo_healthlake.types.job_name.JobName"] = None,
        client_token: Optional[
            "capo_healthlake.types.client_token_string.ClientTokenString"
        ] = None,
        validation_level: Optional[
            "capo_healthlake.types.validation_level.ValidationLevel"
        ] = None,
        profile_id: Optional[
            "capo_healthlake.types.bounded_length_string.BoundedLengthString"
        ] = None,
        input_format: Optional[
            "capo_healthlake.types.bounded_length_string.BoundedLengthString"
        ] = None,
        drift_detection_enabled: Optional[
            "capo_healthlake.types.health_lake_boolean.HealthLakeBoolean"
        ] = None,
        provenance_enabled: Optional[
            "capo_healthlake.types.default_enabled_boolean.DefaultEnabledBoolean"
        ] = None,
    ) -> "capo_healthlake.types.start_fhir_import_job_response.StartFHIRImportJobResponse":
        """<p>Start importing bulk FHIR data into an ACTIVE data store. The import job imports FHIR data found in the <code>InputDataConfig</code> object and stores processing results in the <code>JobOutputDataConfig</code> object.</p>

        Args:
            job_name: <p>The import job name.</p>
            input_data_config: <p>The input properties for the import job request.</p>
            datastore_id: <p>The data store identifier.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) that grants access permission to HealthLake.</p>
            client_token: <p>The optional user-provided token used for ensuring API idempotency.</p>
            validation_level: <p>The validation level of the import job.</p>
            profile_id: <p>The data transformation profile identifier to use for the import job.</p>
            input_format: <p>The input format of the data to be imported.</p>
            drift_detection_enabled: <p>Specifies whether to enable drift detection for the import job.</p>
            provenance_enabled: <p>Specifies whether to enable provenance for the import job.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.failed_dependency_exception.FailedDependencyException: <p>A dependent service failed to fulfill the request.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.start_fhir_import_job_request.StartFHIRImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.start_fhir_import_job_response.StartFHIRImportJobResponse"
        ]:
            import capo_healthlake._operations.health_lake.start_fhir_import_job

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.start_fhir_import_job.async_start_fhir_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.start_fhir_import_job_request.StartFHIRImportJobRequest = {
            "input_data_config": input_data_config,
            "job_output_data_config": job_output_data_config,
            "datastore_id": datastore_id,
            "data_access_role_arn": data_access_role_arn,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if validation_level is not None:
            input_["validation_level"] = validation_level
        if profile_id is not None:
            input_["profile_id"] = profile_id
        if input_format is not None:
            input_["input_format"] = input_format
        if drift_detection_enabled is not None:
            input_["drift_detection_enabled"] = drift_detection_enabled
        if provenance_enabled is not None:
            input_["provenance_enabled"] = provenance_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_healthlake.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_healthlake.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "capo_healthlake.types.tag_resource_response.TagResourceResponse":
        """<p>Add a user-specifed key and value tag to a data store.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that grants access to the data store tags are being added to.</p>
            tags: <p>The user-specified key and value pair tags being added to a data store.</p>

        Raises:
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_healthlake._operations.health_lake.tag_resource

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_healthlake.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_healthlake.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "capo_healthlake.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove a user-specifed key and value tag from a data store.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the data store from which tags are being removed.</p>
            tag_keys: <p>The keys for the tags to be removed from the data store.</p>

        Raises:
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_healthlake._operations.health_lake.untag_resource

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_data_transformation_profile(
        self,
        profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString",
        profile_mapping: "capo_healthlake.types.profile_mapping.ProfileMapping",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        change_description: Optional[
            "capo_healthlake.types.change_description.ChangeDescription"
        ] = None,
    ) -> "capo_healthlake.types.update_data_transformation_profile_response.UpdateDataTransformationProfileResponse":
        """<p>Updates the DRAFT version (version 0) of a data transformation profile with new profile content. The update replaces all existing DRAFT content.</p>

        Args:
            profile_id: <p>The unique identifier of the profile to update.</p>
            profile_mapping: <p>The new profile content for the DRAFT version. This is a full replacement of all profile files.</p>
            change_description: <p>A description of what changed in this update.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.update_data_transformation_profile_request.UpdateDataTransformationProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.update_data_transformation_profile_response.UpdateDataTransformationProfileResponse"
        ]:
            import capo_healthlake._operations.health_lake.update_data_transformation_profile

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.update_data_transformation_profile.async_update_data_transformation_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.update_data_transformation_profile_request.UpdateDataTransformationProfileRequest = {
            "profile_id": profile_id,
            "profile_mapping": profile_mapping,
        }
        if change_description is not None:
            input_["change_description"] = change_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_fhir_datastore(
        self,
        datastore_id: "capo_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        datastore_name: Optional[
            "capo_healthlake.types.datastore_name.DatastoreName"
        ] = None,
        analytics_configuration: Optional[
            "capo_healthlake.types.analytics_configuration.AnalyticsConfiguration"
        ] = None,
        nlp_configuration: Optional[
            "capo_healthlake.types.nlp_configuration.NlpConfiguration"
        ] = None,
        profile_configuration: Optional[
            "capo_healthlake.types.profile_configuration.ProfileConfiguration"
        ] = None,
        identity_provider_configuration: Optional[
            "capo_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
        backup_configuration: Optional[
            "capo_healthlake.types.backup_configuration.BackupConfiguration"
        ] = None,
    ) -> "capo_healthlake.types.update_fhir_datastore_response.UpdateFHIRDatastoreResponse":
        """<p>Update the properties of a FHIR-enabled data store.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            datastore_name: <p>The data store name.</p>
            analytics_configuration: <p>The analytics configuration for the data store.</p>
            nlp_configuration: <p>The natural language processing (NLP) configuration for the data store.</p>
            profile_configuration: <p>The profile configuration for the data store.</p>
            identity_provider_configuration: <p>The identity provider configuration for the data store.</p>
            backup_configuration: The backup configuration for the data store.

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.conflict_exception.ConflictException: <p>The data store is in a transition state and the user requested action cannot be performed.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a data store's name and configuration

            >>> await client.update_fhir_datastore(datastore_id='datastore-id', datastore_name='RenamedFhirDatastore', nlp_configuration={'Status': 'ENABLED'}, analytics_configuration={'Status': 'DISABLED'}, profile_configuration={'DefaultProfiles': ['us-core-3.1.1', 'carin-bb-2.0.0']}, identity_provider_configuration={'AuthorizationStrategy': 'SMART_ON_FHIR_V1', 'FineGrainedAuthorizationEnabled': True})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.update_fhir_datastore_request.UpdateFHIRDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.update_fhir_datastore_response.UpdateFHIRDatastoreResponse"
        ]:
            import capo_healthlake._operations.health_lake.update_fhir_datastore

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.update_fhir_datastore.async_update_fhir_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.update_fhir_datastore_request.UpdateFHIRDatastoreRequest = {
            "datastore_id": datastore_id
        }
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        if analytics_configuration is not None:
            input_["analytics_configuration"] = analytics_configuration
        if nlp_configuration is not None:
            input_["nlp_configuration"] = nlp_configuration
        if profile_configuration is not None:
            input_["profile_configuration"] = profile_configuration
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration
        if backup_configuration is not None:
            input_["backup_configuration"] = backup_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_profile_with_agent(
        self,
        profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString",
        source_format: "capo_healthlake.types.source_format.SourceFormat",
        input_message: "capo_healthlake.types.agent_input_message.AgentInputMessage",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        conversation_id: Optional[
            "capo_healthlake.types.conversation_id_string.ConversationIdString"
        ] = None,
    ) -> "capo_healthlake.types.update_profile_with_agent_response.UpdateProfileWithAgentResponse":
        """<p>Updates a data transformation profile using chat-based interaction with an agent. Supports multi-turn conversations for iteratively customizing profiles.</p>

        Args:
            profile_id: <p>The unique identifier of the profile to update via the agent.</p>
            source_format: <p>The source data format for the transformation.</p>
            input_message: <p>The message to send to the agent.</p>
            conversation_id: <p>The conversation identifier for multi-turn interactions. Omit to start a new conversation.</p>

        Raises:
            capo_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            capo_healthlake.errors.agent_message_out_of_context_exception.AgentMessageOutOfContextException: <p>The agent message does not fit within the current conversation context. Start a new conversation or provide a message that relates to the current profile customization session.</p>
            capo_healthlake.errors.conversation_not_found_exception.ConversationNotFoundException: <p>The specified conversation identifier does not exist. Verify the conversation ID or omit it to start a new conversation.</p>
            capo_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            capo_healthlake.errors.not_implemented_operation_exception.NotImplementedOperationException: <p>The requested operation is not yet available. Check the service documentation for a list of supported operations.</p>
            capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            capo_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            capo_healthlake.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to make this request. Verify that your Amazon Web Services credentials are valid and that you have the required permissions.</p>
            capo_healthlake.errors.unsupported_mime_type_exception.UnsupportedMIMETypeException: <p>The content type in your request is not supported. Use a supported content type for this operation.</p>
            capo_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            capo_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_healthlake.types.update_profile_with_agent_request.UpdateProfileWithAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_healthlake.types.update_profile_with_agent_response.UpdateProfileWithAgentResponse"
        ]:
            import capo_healthlake._operations.health_lake.update_profile_with_agent

            (
                output,
                http_response,
            ) = await capo_healthlake._operations.health_lake.update_profile_with_agent.async_update_profile_with_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_healthlake.types.update_profile_with_agent_request.UpdateProfileWithAgentRequest = {
            "profile_id": profile_id,
            "source_format": source_format,
            "input_message": input_message,
        }
        if conversation_id is not None:
            input_["conversation_id"] = conversation_id

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
