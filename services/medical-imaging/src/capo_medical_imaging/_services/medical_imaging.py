"""Generated from Smithy shape ``com.amazonaws.medicalimaging#AHIGatewayService``."""

import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_medical_imaging._auth._signers
import capo_medical_imaging._auth._sigv4
from capo_medical_imaging._auth._identity import Credentials
from capo_medical_imaging._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_medical_imaging._auth._zapros_handler import AuthMiddleware
from capo_medical_imaging._pagination import resolve_path as _resolve_path
from capo_medical_imaging._resources.ahi_gateway_service.datastore_resource import (
    DatastoreResource,
)
from capo_medical_imaging._resources.ahi_gateway_service.image_set_resource import (
    ImageSetResource,
)
from capo_medical_imaging._services._aws_config import aws_config
from capo_medical_imaging._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_medical_imaging.types.arn
    import capo_medical_imaging.types.aws_account_id
    import capo_medical_imaging.types.client_token
    import capo_medical_imaging.types.copy_image_set_information
    import capo_medical_imaging.types.copy_image_set_request
    import capo_medical_imaging.types.copy_image_set_response
    import capo_medical_imaging.types.create_datastore_request
    import capo_medical_imaging.types.create_datastore_response
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.datastore_name
    import capo_medical_imaging.types.datastore_status
    import capo_medical_imaging.types.datastore_summary
    import capo_medical_imaging.types.delete_datastore_request
    import capo_medical_imaging.types.delete_datastore_response
    import capo_medical_imaging.types.delete_image_set_request
    import capo_medical_imaging.types.delete_image_set_response
    import capo_medical_imaging.types.dicom_import_job_summary
    import capo_medical_imaging.types.get_datastore_request
    import capo_medical_imaging.types.get_datastore_response
    import capo_medical_imaging.types.get_dicom_import_job_request
    import capo_medical_imaging.types.get_dicom_import_job_response
    import capo_medical_imaging.types.get_image_frame_request
    import capo_medical_imaging.types.get_image_frame_response
    import capo_medical_imaging.types.get_image_set_metadata_request
    import capo_medical_imaging.types.get_image_set_metadata_response
    import capo_medical_imaging.types.get_image_set_request
    import capo_medical_imaging.types.get_image_set_response
    import capo_medical_imaging.types.image_frame_information
    import capo_medical_imaging.types.image_set_external_version_id
    import capo_medical_imaging.types.image_set_id
    import capo_medical_imaging.types.image_set_properties
    import capo_medical_imaging.types.image_sets_metadata_summary
    import capo_medical_imaging.types.import_configuration
    import capo_medical_imaging.types.job_id
    import capo_medical_imaging.types.job_name
    import capo_medical_imaging.types.job_status
    import capo_medical_imaging.types.kms_key_arn
    import capo_medical_imaging.types.lambda_arn
    import capo_medical_imaging.types.list_datastores_request
    import capo_medical_imaging.types.list_datastores_response
    import capo_medical_imaging.types.list_dicom_import_jobs_request
    import capo_medical_imaging.types.list_dicom_import_jobs_response
    import capo_medical_imaging.types.list_image_set_versions_request
    import capo_medical_imaging.types.list_image_set_versions_response
    import capo_medical_imaging.types.list_tags_for_resource_request
    import capo_medical_imaging.types.list_tags_for_resource_response
    import capo_medical_imaging.types.lossless_storage_format
    import capo_medical_imaging.types.metadata_updates
    import capo_medical_imaging.types.next_token
    import capo_medical_imaging.types.role_arn
    import capo_medical_imaging.types.s3_uri
    import capo_medical_imaging.types.search_criteria
    import capo_medical_imaging.types.search_image_sets_request
    import capo_medical_imaging.types.search_image_sets_response
    import capo_medical_imaging.types.start_dicom_import_job_request
    import capo_medical_imaging.types.start_dicom_import_job_response
    import capo_medical_imaging.types.tag_key_list
    import capo_medical_imaging.types.tag_map
    import capo_medical_imaging.types.tag_resource_request
    import capo_medical_imaging.types.tag_resource_response
    import capo_medical_imaging.types.untag_resource_request
    import capo_medical_imaging.types.untag_resource_response
    import capo_medical_imaging.types.update_image_set_metadata_request
    import capo_medical_imaging.types.update_image_set_metadata_response


class MedicalImagingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class MedicalImagingClient:
    """A client for the ``MedicalImaging`` service.

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
        self._config = MedicalImagingClientConfig(
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
        self.datastore_resource = DatastoreResource(self)
        self.image_set_resource = ImageSetResource(self)

    def operation_options(
        self, config_overrides: Optional[MedicalImagingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MedicalImagingClientConfig = config_overrides or {}
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

    def copy_image_set(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        source_image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId",
        copy_image_set_information: "capo_medical_imaging.types.copy_image_set_information.CopyImageSetInformation",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        force: Optional[bool] = None,
        promote_to_primary: Optional[bool] = None,
    ) -> "capo_medical_imaging.types.copy_image_set_response.CopyImageSetResponse":
        """<p>Copy an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            source_image_set_id: <p>The source image set identifier.</p>
            copy_image_set_information: <p>Copy image set information.</p>
            force: <p>Providing this parameter will force completion of the <code>CopyImageSet</code> operation, even if there are inconsistent Patient, Study, and/or Series level metadata elements between the <code>sourceImageSet</code> and <code>destinationImageSet</code>.</p>
            promote_to_primary: <p>Providing this parameter will configure the <code>CopyImageSet</code> operation to promote the given image set to the primary DICOM hierarchy. If successful, a new primary image set ID will be returned as the destination image set.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request caused a service quota to be exceeded.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.copy_image_set_request.CopyImageSetRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.copy_image_set_response.CopyImageSetResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.copy_image_set

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.copy_image_set.copy_image_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.copy_image_set_request.CopyImageSetRequest = {
            "datastore_id": datastore_id,
            "source_image_set_id": source_image_set_id,
            "copy_image_set_information": copy_image_set_information,
        }
        if force is not None:
            input_["force"] = force
        if promote_to_primary is not None:
            input_["promote_to_primary"] = promote_to_primary

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_image_set(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.delete_image_set_response.DeleteImageSetResponse":
        """<p>Delete an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.delete_image_set_request.DeleteImageSetRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.delete_image_set_response.DeleteImageSetResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.delete_image_set

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.delete_image_set.delete_image_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.delete_image_set_request.DeleteImageSetRequest = {
            "datastore_id": datastore_id,
            "image_set_id": image_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dicom_import_job(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        job_id: "capo_medical_imaging.types.job_id.JobId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.get_dicom_import_job_response.GetDICOMImportJobResponse":
        """<p>Get the import job properties to learn more about the job or job progress.</p> <note> <p>The <code>jobStatus</code> refers to the execution of the import job. Therefore, an import job can return a <code>jobStatus</code> as <code>COMPLETED</code> even if validation issues are discovered during the import process. If a <code>jobStatus</code> returns as <code>COMPLETED</code>, we still recommend you review the output manifests written to S3, as they provide details on the success or failure of individual P10 object imports.</p> </note>

        Args:
            datastore_id: <p>The data store identifier.</p>
            job_id: <p>The import job identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.get_dicom_import_job_request.GetDICOMImportJobRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.get_dicom_import_job_response.GetDICOMImportJobResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.get_dicom_import_job

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.get_dicom_import_job.get_dicom_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.get_dicom_import_job_request.GetDICOMImportJobRequest = {
            "datastore_id": datastore_id,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def get_image_frame(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId",
        image_frame_information: "capo_medical_imaging.types.image_frame_information.ImageFrameInformation",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "Generator[capo_medical_imaging.types.get_image_frame_response.GetImageFrameResponse]":
        """<p>Get an image frame (pixel data) for an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            image_frame_information: <p>Information about the image frame (pixel data) identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.not_acceptable_exception.NotAcceptableException: <p>The request content type or accept header is not supported.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.get_image_frame_request.GetImageFrameRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.get_image_frame_response.GetImageFrameResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.get_image_frame

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.get_image_frame.get_image_frame(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.get_image_frame_request.GetImageFrameRequest = {
            "datastore_id": datastore_id,
            "image_set_id": image_set_id,
            "image_frame_information": image_frame_information,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def get_image_set(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        version_id: Optional[
            "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
        ] = None,
    ) -> "capo_medical_imaging.types.get_image_set_response.GetImageSetResponse":
        """<p>Get image set properties.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            version_id: <p>The image set version identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.get_image_set_request.GetImageSetRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.get_image_set_response.GetImageSetResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.get_image_set

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.get_image_set.get_image_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.get_image_set_request.GetImageSetRequest = {
            "datastore_id": datastore_id,
            "image_set_id": image_set_id,
        }
        if version_id is not None:
            input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def get_image_set_metadata(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        version_id: Optional[
            "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
        ] = None,
    ) -> "Generator[capo_medical_imaging.types.get_image_set_metadata_response.GetImageSetMetadataResponse]":
        """<p>Get metadata attributes for an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            version_id: <p>The image set version identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.get_image_set_metadata_request.GetImageSetMetadataRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.get_image_set_metadata_response.GetImageSetMetadataResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.get_image_set_metadata

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.get_image_set_metadata.get_image_set_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.get_image_set_metadata_request.GetImageSetMetadataRequest = {
            "datastore_id": datastore_id,
            "image_set_id": image_set_id,
        }
        if version_id is not None:
            input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def list_dicom_import_jobs(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        job_status: Optional["capo_medical_imaging.types.job_status.JobStatus"] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_medical_imaging.types.list_dicom_import_jobs_response.ListDICOMImportJobsResponse":
        """<p>List import jobs created for a specific data store.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            job_status: <p>The filters for listing import jobs based on status.</p>
            next_token: <p>The pagination token used to request the list of import jobs on the next page.</p>
            max_results: <p>The max results count. The upper bound is determined by load testing.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.list_dicom_import_jobs_request.ListDICOMImportJobsRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.list_dicom_import_jobs_response.ListDICOMImportJobsResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.list_dicom_import_jobs

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.list_dicom_import_jobs.list_dicom_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.list_dicom_import_jobs_request.ListDICOMImportJobsRequest = {
            "datastore_id": datastore_id
        }
        if job_status is not None:
            input_["job_status"] = job_status
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

    def iter_list_dicom_import_jobs(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        job_status: Optional["capo_medical_imaging.types.job_status.JobStatus"] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_medical_imaging.types.dicom_import_job_summary.DICOMImportJobSummary]":
        _token = next_token
        while True:
            _response = self.list_dicom_import_jobs(
                datastore_id,
                config_overrides=config_overrides,
                job_status=job_status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_image_set_versions(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_medical_imaging.types.list_image_set_versions_response.ListImageSetVersionsResponse":
        """<p>List image set versions.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            next_token: <p>The pagination token used to request the list of image set versions on the next page.</p>
            max_results: <p>The max results count.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.list_image_set_versions_request.ListImageSetVersionsRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.list_image_set_versions_response.ListImageSetVersionsResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.list_image_set_versions

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.list_image_set_versions.list_image_set_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.list_image_set_versions_request.ListImageSetVersionsRequest = {
            "datastore_id": datastore_id,
            "image_set_id": image_set_id,
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

    def iter_list_image_set_versions(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_medical_imaging.types.image_set_properties.ImageSetProperties]":
        _token = next_token
        while True:
            _response = self.list_image_set_versions(
                datastore_id,
                image_set_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("image_set_properties_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_medical_imaging.types.arn.Arn",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a medical imaging resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the medical imaging resource to list tags for.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.list_tags_for_resource

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_image_sets(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        search_criteria: Optional[
            "capo_medical_imaging.types.search_criteria.SearchCriteria"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
    ) -> (
        "capo_medical_imaging.types.search_image_sets_response.SearchImageSetsResponse"
    ):
        """<p>Search image sets based on defined input attributes.</p> <note> <p> <code>SearchImageSets</code> accepts a single search query parameter and returns a paginated response of all image sets that have the matching criteria. All date range queries must be input as <code>(lowerBound, upperBound)</code>.</p> <p>By default, <code>SearchImageSets</code> uses the <code>updatedAt</code> field for sorting in descending order from newest to oldest.</p> </note>

        Args:
            datastore_id: <p>The identifier of the data store where the image sets reside.</p>
            search_criteria: <p>The search criteria that filters by applying a maximum of 1 item to <code>SearchByAttribute</code>.</p>
            max_results: <p>The maximum number of results that can be returned in a search.</p>
            next_token: <p>The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.search_image_sets_request.SearchImageSetsRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.search_image_sets_response.SearchImageSetsResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.search_image_sets

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.search_image_sets.search_image_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.search_image_sets_request.SearchImageSetsRequest = {
            "datastore_id": datastore_id
        }
        if search_criteria is not None:
            input_["search_criteria"] = search_criteria
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

    def iter_search_image_sets(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        search_criteria: Optional[
            "capo_medical_imaging.types.search_criteria.SearchCriteria"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_medical_imaging.types.image_sets_metadata_summary.ImageSetsMetadataSummary]":
        _token = next_token
        while True:
            _response = self.search_image_sets(
                datastore_id,
                config_overrides=config_overrides,
                search_criteria=search_criteria,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_sets_metadata_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_dicom_import_job(
        self,
        data_access_role_arn: "capo_medical_imaging.types.role_arn.RoleArn",
        client_token: "capo_medical_imaging.types.client_token.ClientToken",
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        input_s3_uri: "capo_medical_imaging.types.s3_uri.S3Uri",
        output_s3_uri: "capo_medical_imaging.types.s3_uri.S3Uri",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        job_name: Optional["capo_medical_imaging.types.job_name.JobName"] = None,
        input_owner_account_id: Optional[
            "capo_medical_imaging.types.aws_account_id.AwsAccountId"
        ] = None,
        import_configuration: Optional[
            "capo_medical_imaging.types.import_configuration.ImportConfiguration"
        ] = None,
    ) -> "capo_medical_imaging.types.start_dicom_import_job_response.StartDICOMImportJobResponse":
        """<p>Start importing bulk data into an <code>ACTIVE</code> data store. The import job imports DICOM P10 files or enhances existing DICOM files with JSON metadata. The <code>importConfiguration</code> parameter specifies the import type. The data is found in the S3 prefix specified by the <code>inputS3Uri</code> parameter. The import job stores processing results in the file specified by the <code>outputS3Uri</code> parameter.</p>

        Args:
            job_name: <p>The import job name.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants permission to access medical imaging resources.</p>
            client_token: <p>A unique identifier for API idempotency.</p>
            datastore_id: <p>The data store identifier.</p>
            input_s3_uri: <p>The input prefix path for the S3 bucket that contains the DICOM files to be imported.</p>
            output_s3_uri: <p>The output prefix of the S3 bucket to upload the results of the DICOM import job.</p>
            input_owner_account_id: <p>The account ID of the source S3 bucket owner.</p>
            import_configuration: <p>The import configuration for the import job.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request caused a service quota to be exceeded.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.start_dicom_import_job_request.StartDICOMImportJobRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.start_dicom_import_job_response.StartDICOMImportJobResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.start_dicom_import_job

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.start_dicom_import_job.start_dicom_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.start_dicom_import_job_request.StartDICOMImportJobRequest = {
            "data_access_role_arn": data_access_role_arn,
            "client_token": client_token,
            "datastore_id": datastore_id,
            "input_s3_uri": input_s3_uri,
            "output_s3_uri": output_s3_uri,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if input_owner_account_id is not None:
            input_["input_owner_account_id"] = input_owner_account_id
        if import_configuration is not None:
            input_["import_configuration"] = import_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_medical_imaging.types.arn.Arn",
        tags: "capo_medical_imaging.types.tag_map.TagMap",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a user-specifed key and value tag to a medical imaging resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to.</p>
            tags: <p>The user-specified key and value tag pairs added to a medical imaging resource.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.tag_resource

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_medical_imaging.types.arn.Arn",
        tag_keys: "capo_medical_imaging.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a medical imaging resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from.</p>
            tag_keys: <p>The keys for the tags to be removed from the medical imaging resource.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.untag_resource

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.untag_resource_request.UntagResourceRequest = {
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

    def update_image_set_metadata(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId",
        latest_version_id: "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId",
        update_image_set_metadata_updates: "capo_medical_imaging.types.metadata_updates.MetadataUpdates",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        force: Optional[bool] = None,
        include_study_image_sets: Optional[bool] = None,
    ) -> "capo_medical_imaging.types.update_image_set_metadata_response.UpdateImageSetMetadataResponse":
        """<p>Update image set metadata attributes.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            latest_version_id: <p>The latest image set version identifier.</p>
            force: <p>Setting this flag will force the <code>UpdateImageSetMetadata</code> operation for the following attributes:</p> <ul> <li> <p> <code>Tag.StudyInstanceUID</code>, <code>Tag.SeriesInstanceUID</code>, <code>Tag.SOPInstanceUID</code>, and <code>Tag.StudyID</code> </p> </li> <li> <p>Adding, removing, or updating private tags for an individual SOP Instance</p> </li> </ul>
            include_study_image_sets: <p>Flag to apply the metadata updates to all image sets in the same Study as the requested image set ID.</p>
            update_image_set_metadata_updates: <p>Update image set metadata updates.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request caused a service quota to be exceeded.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.update_image_set_metadata_request.UpdateImageSetMetadataRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.update_image_set_metadata_response.UpdateImageSetMetadataResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.update_image_set_metadata

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.update_image_set_metadata.update_image_set_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.update_image_set_metadata_request.UpdateImageSetMetadataRequest = {
            "datastore_id": datastore_id,
            "image_set_id": image_set_id,
            "latest_version_id": latest_version_id,
            "update_image_set_metadata_updates": update_image_set_metadata_updates,
        }
        if force is not None:
            input_["force"] = force
        if include_study_image_sets is not None:
            input_["include_study_image_sets"] = include_study_image_sets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_datastore(
        self,
        client_token: "capo_medical_imaging.types.client_token.ClientToken",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        datastore_name: Optional[
            "capo_medical_imaging.types.datastore_name.DatastoreName"
        ] = None,
        tags: Optional["capo_medical_imaging.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional[
            "capo_medical_imaging.types.kms_key_arn.KmsKeyArn"
        ] = None,
        lambda_authorizer_arn: Optional[
            "capo_medical_imaging.types.lambda_arn.LambdaArn"
        ] = None,
        lossless_storage_format: Optional[
            "capo_medical_imaging.types.lossless_storage_format.LosslessStorageFormat"
        ] = None,
    ) -> "capo_medical_imaging.types.create_datastore_response.CreateDatastoreResponse":
        """<p>Create a data store.</p>

        Args:
            datastore_name: <p>The data store name.</p>
            client_token: <p>A unique identifier for API idempotency.</p>
            tags: <p>The tags provided when creating a data store.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.</p>
            lambda_authorizer_arn: <p>The ARN of the authorizer's Lambda function.</p>
            lossless_storage_format: <p>The lossless storage format for the datastore.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request caused a service quota to be exceeded.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.create_datastore_request.CreateDatastoreRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.create_datastore_response.CreateDatastoreResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.create_datastore

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.create_datastore.create_datastore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.create_datastore_request.CreateDatastoreRequest = {
            "client_token": client_token
        }
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if lambda_authorizer_arn is not None:
            input_["lambda_authorizer_arn"] = lambda_authorizer_arn
        if lossless_storage_format is not None:
            input_["lossless_storage_format"] = lossless_storage_format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_datastore(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.get_datastore_response.GetDatastoreResponse":
        """<p>Get data store properties.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.get_datastore_request.GetDatastoreRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.get_datastore_response.GetDatastoreResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.get_datastore

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.get_datastore.get_datastore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.get_datastore_request.GetDatastoreRequest = {
            "datastore_id": datastore_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_datastore(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse":
        """<p>Delete a data store.</p> <note> <p>Before a data store can be deleted, you must first delete all image sets within it.</p> </note>

        Args:
            datastore_id: <p>The data store identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.delete_datastore

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.delete_datastore.delete_datastore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest = {
            "datastore_id": datastore_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_datastores(
        self,
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        datastore_status: Optional[
            "capo_medical_imaging.types.datastore_status.DatastoreStatus"
        ] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_medical_imaging.types.list_datastores_response.ListDatastoresResponse":
        """<p>List data stores.</p>

        Args:
            datastore_status: <p>The data store status.</p>
            next_token: <p>The pagination token used to request the list of data stores on the next page.</p>
            max_results: <p>Valid Range: Minimum value of 1. Maximum value of 50.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.list_datastores_request.ListDatastoresRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.list_datastores_response.ListDatastoresResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.list_datastores

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.list_datastores.list_datastores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medical_imaging.types.list_datastores_request.ListDatastoresRequest = {}
        if datastore_status is not None:
            input_["datastore_status"] = datastore_status
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

    def iter_list_datastores(
        self,
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        datastore_status: Optional[
            "capo_medical_imaging.types.datastore_status.DatastoreStatus"
        ] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_medical_imaging.types.datastore_summary.DatastoreSummary]":
        _token = next_token
        while True:
            _response = self.list_datastores(
                config_overrides=config_overrides,
                datastore_status=datastore_status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("datastore_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
