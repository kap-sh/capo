"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#SageMakerGeospatial``."""

import uuid
import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_sagemaker_geospatial._auth._signers
import capo_sagemaker_geospatial._auth._sigv4
from capo_sagemaker_geospatial._auth._identity import Credentials
from capo_sagemaker_geospatial._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemaker_geospatial._auth._zapros_handler import AuthMiddleware
from capo_sagemaker_geospatial._pagination import resolve_path as _resolve_path
from capo_sagemaker_geospatial._resources.sage_maker_geospatial.earth_observation_job import (
    EarthObservationJob,
)
from capo_sagemaker_geospatial._resources.sage_maker_geospatial.raster_data_collection import (
    RasterDataCollection,
)
from capo_sagemaker_geospatial._resources.sage_maker_geospatial.vector_enrichment_job import (
    VectorEnrichmentJob,
)
from capo_sagemaker_geospatial._services._aws_config import aws_config
from capo_sagemaker_geospatial._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.arn
    import capo_sagemaker_geospatial.types.data_collection_arn
    import capo_sagemaker_geospatial.types.delete_earth_observation_job_input
    import capo_sagemaker_geospatial.types.delete_earth_observation_job_output
    import capo_sagemaker_geospatial.types.delete_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.delete_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.earth_observation_job_arn
    import capo_sagemaker_geospatial.types.earth_observation_job_status
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.export_earth_observation_job_input
    import capo_sagemaker_geospatial.types.export_earth_observation_job_output
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config
    import capo_sagemaker_geospatial.types.get_earth_observation_job_input
    import capo_sagemaker_geospatial.types.get_earth_observation_job_output
    import capo_sagemaker_geospatial.types.get_raster_data_collection_input
    import capo_sagemaker_geospatial.types.get_raster_data_collection_output
    import capo_sagemaker_geospatial.types.get_tile_input
    import capo_sagemaker_geospatial.types.get_tile_output
    import capo_sagemaker_geospatial.types.get_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.get_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.input_config_input
    import capo_sagemaker_geospatial.types.job_config_input
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.list_earth_observation_job_input
    import capo_sagemaker_geospatial.types.list_earth_observation_job_output
    import capo_sagemaker_geospatial.types.list_earth_observation_job_output_config
    import capo_sagemaker_geospatial.types.list_raster_data_collections_input
    import capo_sagemaker_geospatial.types.list_raster_data_collections_output
    import capo_sagemaker_geospatial.types.list_tags_for_resource_request
    import capo_sagemaker_geospatial.types.list_tags_for_resource_response
    import capo_sagemaker_geospatial.types.list_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.list_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.list_vector_enrichment_job_output_config
    import capo_sagemaker_geospatial.types.next_token
    import capo_sagemaker_geospatial.types.output_config_input
    import capo_sagemaker_geospatial.types.output_type
    import capo_sagemaker_geospatial.types.raster_data_collection_metadata
    import capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input
    import capo_sagemaker_geospatial.types.search_raster_data_collection_input
    import capo_sagemaker_geospatial.types.search_raster_data_collection_output
    import capo_sagemaker_geospatial.types.sort_order
    import capo_sagemaker_geospatial.types.start_earth_observation_job_input
    import capo_sagemaker_geospatial.types.start_earth_observation_job_output
    import capo_sagemaker_geospatial.types.start_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.start_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.stop_earth_observation_job_input
    import capo_sagemaker_geospatial.types.stop_earth_observation_job_output
    import capo_sagemaker_geospatial.types.stop_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.stop_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.string_list_input
    import capo_sagemaker_geospatial.types.tag_key_list
    import capo_sagemaker_geospatial.types.tag_resource_request
    import capo_sagemaker_geospatial.types.tag_resource_response
    import capo_sagemaker_geospatial.types.tags
    import capo_sagemaker_geospatial.types.target_options
    import capo_sagemaker_geospatial.types.untag_resource_request
    import capo_sagemaker_geospatial.types.untag_resource_response
    import capo_sagemaker_geospatial.types.vector_enrichment_job_arn
    import capo_sagemaker_geospatial.types.vector_enrichment_job_config
    import capo_sagemaker_geospatial.types.vector_enrichment_job_input_config


class SageMakerGeospatialClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class SageMakerGeospatialClient:
    """A client for the ``SageMakerGeospatial`` service.

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
        self._config = SageMakerGeospatialClientConfig(
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

        # resources
        self.earth_observation_job = EarthObservationJob(self)
        self.raster_data_collection = RasterDataCollection(self)
        self.vector_enrichment_job = VectorEnrichmentJob(self)

    def operation_options(
        self, config_overrides: Optional[SageMakerGeospatialClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SageMakerGeospatialClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_sagemaker_geospatial.types.arn.Arn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags attached to the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to tag.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_tags_for_resource

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_sagemaker_geospatial.types.arn.Arn",
        tags: "capo_sagemaker_geospatial.types.tags.Tags",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.tag_resource_response.TagResourceResponse":
        """<p>The resource you want to tag.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to tag.</p>
            tags: <p>Each tag consists of a key and a value.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.tag_resource

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_sagemaker_geospatial.types.arn.Arn",
        tag_keys: "capo_sagemaker_geospatial.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> (
        "capo_sagemaker_geospatial.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>The resource you want to untag.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to untag.</p>
            tag_keys: <p>Keys of the tags you want to remove.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.untag_resource

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.untag_resource_request.UntagResourceRequest = {
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

    def start_earth_observation_job(
        self,
        name: str,
        input_config: "capo_sagemaker_geospatial.types.input_config_input.InputConfigInput",
        job_config: "capo_sagemaker_geospatial.types.job_config_input.JobConfigInput",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional["capo_sagemaker_geospatial.types.kms_key.KmsKey"] = None,
        tags: Optional["capo_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "capo_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput":
        """<p>Use this operation to create an Earth observation job.</p>

        Args:
            name: <p>The name of the Earth Observation job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Earth Observation job.</p>
            job_config: <p>An object containing information about the job configuration.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            tags: <p>Each tag consists of a key and a value.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job.start_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput = {
            "name": name,
            "input_config": input_config,
            "job_config": job_config,
            "execution_role_arn": execution_role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_earth_observation_job(
        self,
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput":
        """<p>Get the details for a previously initiated Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job.get_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_earth_observation_job(
        self,
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput":
        """<p>Use this operation to delete an Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being deleted.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job.delete_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_earth_observation_jobs(
        self,
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        status_equals: Optional[
            "capo_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
        ] = None,
        sort_order: Optional[
            "capo_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput":
        """<p>Use this operation to get a list of the Earth Observation jobs associated with the calling Amazon Web Services account.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs.list_earth_observation_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput = {}
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    def iter_list_earth_observation_jobs(
        self,
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        status_equals: Optional[
            "capo_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
        ] = None,
        sort_order: Optional[
            "capo_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_sagemaker_geospatial.types.list_earth_observation_job_output_config.ListEarthObservationJobOutputConfig]":
        _token = next_token
        while True:
            _response = self.list_earth_observation_jobs(
                config_overrides=config_overrides,
                status_equals=status_equals,
                sort_order=sort_order,
                sort_by=sort_by,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("earth_observation_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def export_earth_observation_job(
        self,
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "capo_sagemaker_geospatial.types.output_config_input.OutputConfigInput",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        export_source_images: Optional[bool] = None,
    ) -> "capo_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput":
        """<p>Use this operation to export results of an Earth Observation job and optionally source images used as input to the EOJ to an Amazon S3 location.</p>

        Args:
            arn: <p>The input Amazon Resource Name (ARN) of the Earth Observation job being exported.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            output_config: <p>An object containing information about the output file.</p>
            export_source_images: <p>The source images provided to the Earth Observation job being exported.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job.export_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput = {
            "arn": arn,
            "execution_role_arn": execution_role_arn,
            "output_config": output_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if export_source_images is not None:
            input_["export_source_images"] = export_source_images

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def get_tile(
        self,
        x: int,
        y: int,
        z: int,
        image_assets: "capo_sagemaker_geospatial.types.string_list_input.StringListInput",
        target: "capo_sagemaker_geospatial.types.target_options.TargetOptions",
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        image_mask: Optional[bool] = None,
        output_format: Optional[str] = None,
        time_range_filter: Optional[str] = None,
        property_filters: Optional[str] = None,
        output_data_type: Optional[
            "capo_sagemaker_geospatial.types.output_type.OutputType"
        ] = None,
        execution_role_arn: Optional[
            "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
        ] = None,
    ) -> "Generator[capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput]":
        """<p>Gets a web mercator tile for the given Earth Observation job.</p>

        Args:
            x: <p>The x coordinate of the tile input.</p>
            y: <p>The y coordinate of the tile input.</p>
            z: <p>The z coordinate of the tile input.</p>
            image_assets: <p>The particular assets or bands to tile.</p>
            target: <p>Determines what part of the Earth Observation job to tile. 'INPUT' or 'OUTPUT' are the valid options.</p>
            arn: <p>The Amazon Resource Name (ARN) of the tile operation.</p>
            image_mask: <p>Determines whether or not to return a valid data mask.</p>
            output_format: <p>The data format of the output tile. The formats include .npy, .png and .jpg.</p>
            time_range_filter: <p>Time range filter applied to imagery to find the images to tile.</p>
            property_filters: <p>Property filters for the imagery to tile.</p>
            output_data_type: <p>The output data type of the tile operation.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specify.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.get_tile_input.GetTileInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile.get_tile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.get_tile_input.GetTileInput = {
            "x": x,
            "y": y,
            "z": z,
            "image_assets": image_assets,
            "target": target,
            "arn": arn,
        }
        if image_mask is not None:
            input_["image_mask"] = image_mask
        if output_format is not None:
            input_["output_format"] = output_format
        if time_range_filter is not None:
            input_["time_range_filter"] = time_range_filter
        if property_filters is not None:
            input_["property_filters"] = property_filters
        if output_data_type is not None:
            input_["output_data_type"] = output_data_type
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def stop_earth_observation_job(
        self,
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput":
        """<p>Use this operation to stop an existing earth observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being stopped.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job.stop_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_raster_data_collection(
        self,
        arn: "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput":
        """<p>Use this operation to get details of a specific raster data collection.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection.get_raster_data_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_raster_data_collections(
        self,
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput":
        """<p>Use this operation to get raster data collections.</p>

        Args:
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections.list_raster_data_collections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput = {}
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

    def iter_list_raster_data_collections(
        self,
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_sagemaker_geospatial.types.raster_data_collection_metadata.RasterDataCollectionMetadata]":
        _token = next_token
        while True:
            _response = self.list_raster_data_collections(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("raster_data_collection_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_raster_data_collection(
        self,
        arn: "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        raster_data_collection_query: "capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input.RasterDataCollectionQueryWithBandFilterInput",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
    ) -> "capo_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput":
        """<p>Allows you run image query on a specific raster data collection to get a list of the satellite imagery matching the selected filters.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>
            raster_data_collection_query: <p>RasterDataCollectionQuery consisting of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterest.html">AreaOfInterest(AOI)</a>, <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_PropertyFilter.html">PropertyFilters</a> and <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TimeRangeFilterInput.html">TimeRangeFilterInput</a> used in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html">SearchRasterDataCollection</a>.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection.search_raster_data_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput = {
            "arn": arn,
            "raster_data_collection_query": raster_data_collection_query,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_search_raster_data_collection(
        self,
        arn: "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        raster_data_collection_query: "capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input.RasterDataCollectionQueryWithBandFilterInput",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput]":
        _token = next_token
        while True:
            _response = self.search_raster_data_collection(
                arn,
                raster_data_collection_query,
                config_overrides=config_overrides,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_vector_enrichment_job(
        self,
        name: str,
        input_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_input_config.VectorEnrichmentJobInputConfig",
        job_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_config.VectorEnrichmentJobConfig",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional["capo_sagemaker_geospatial.types.kms_key.KmsKey"] = None,
        tags: Optional["capo_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "capo_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput":
        """<p>Creates a Vector Enrichment job for the supplied job type. Currently, there are two supported job types: reverse geocoding and map matching.</p>

        Args:
            name: <p>The name of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Vector Enrichment job.</p>
            job_config: <p>An object containing information about the job configuration.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            tags: <p>Each tag consists of a key and a value.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job.start_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput = {
            "name": name,
            "input_config": input_config,
            "job_config": job_config,
            "execution_role_arn": execution_role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vector_enrichment_job(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput":
        """<p>Retrieves details of a Vector Enrichment Job for a given job Amazon Resource Name (ARN).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job.get_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vector_enrichment_job(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput":
        """<p>Use this operation to delete a Vector Enrichment job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job being deleted.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job.delete_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vector_enrichment_jobs(
        self,
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        status_equals: Optional[str] = None,
        sort_order: Optional[
            "capo_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput":
        """<p>Retrieves a list of vector enrichment jobs.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The maximum number of items to return.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs.list_vector_enrichment_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput = {}
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    def iter_list_vector_enrichment_jobs(
        self,
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        status_equals: Optional[str] = None,
        sort_order: Optional[
            "capo_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_sagemaker_geospatial.types.list_vector_enrichment_job_output_config.ListVectorEnrichmentJobOutputConfig]":
        _token = next_token
        while True:
            _response = self.list_vector_enrichment_jobs(
                config_overrides=config_overrides,
                status_equals=status_equals,
                sort_order=sort_order,
                sort_by=sort_by,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("vector_enrichment_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def export_vector_enrichment_job(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.ExportVectorEnrichmentJobOutputConfig",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput":
        """<p>Use this operation to copy results of a Vector Enrichment job to an Amazon S3 location.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM rolewith permission to upload to the location in OutputConfig.</p>
            output_config: <p>Output location information for exporting Vector Enrichment Job results. </p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job.export_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput = {
            "arn": arn,
            "execution_role_arn": execution_role_arn,
            "output_config": output_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_vector_enrichment_job(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput":
        """<p>Stops the Vector Enrichment job for a given job ARN.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job.stop_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput = {
            "arn": arn
        }

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
