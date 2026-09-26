from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_lambda_microvms._auth._signers
import capo_lambda_microvms._auth._sigv4
from capo_lambda_microvms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda_microvms.types.architecture
    import capo_lambda_microvms.types.capability_list
    import capo_lambda_microvms.types.chipset
    import capo_lambda_microvms.types.code_artifact
    import capo_lambda_microvms.types.cpu_configuration_list
    import capo_lambda_microvms.types.delete_microvm_image_input
    import capo_lambda_microvms.types.delete_microvm_image_output
    import capo_lambda_microvms.types.delete_microvm_image_version_input
    import capo_lambda_microvms.types.delete_microvm_image_version_output
    import capo_lambda_microvms.types.environment_variable_map
    import capo_lambda_microvms.types.get_microvm_image_build_input
    import capo_lambda_microvms.types.get_microvm_image_build_output
    import capo_lambda_microvms.types.get_microvm_image_input
    import capo_lambda_microvms.types.get_microvm_image_output
    import capo_lambda_microvms.types.get_microvm_image_version_input
    import capo_lambda_microvms.types.get_microvm_image_version_output
    import capo_lambda_microvms.types.hooks
    import capo_lambda_microvms.types.list_managed_microvm_image_versions_input
    import capo_lambda_microvms.types.list_managed_microvm_image_versions_output
    import capo_lambda_microvms.types.list_microvm_image_builds_input
    import capo_lambda_microvms.types.list_microvm_image_builds_output
    import capo_lambda_microvms.types.list_microvm_image_versions_input
    import capo_lambda_microvms.types.list_microvm_image_versions_output
    import capo_lambda_microvms.types.list_microvm_images_request
    import capo_lambda_microvms.types.list_microvm_images_response
    import capo_lambda_microvms.types.logging
    import capo_lambda_microvms.types.managed_microvm_image_version
    import capo_lambda_microvms.types.microvm_image_build_summary
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.microvm_image_summary
    import capo_lambda_microvms.types.microvm_image_version_status
    import capo_lambda_microvms.types.microvm_image_version_summary
    import capo_lambda_microvms.types.network_connector_list
    import capo_lambda_microvms.types.non_blank_string
    import capo_lambda_microvms.types.resources_list
    import capo_lambda_microvms.types.role_arn
    import capo_lambda_microvms.types.string
    import capo_lambda_microvms.types.update_microvm_image_request
    import capo_lambda_microvms.types.update_microvm_image_response
    import capo_lambda_microvms.types.update_microvm_image_version_request
    import capo_lambda_microvms.types.update_microvm_image_version_response
    import capo_lambda_microvms.types.version
    from capo_lambda_microvms._services.async_lambda_microvms import (
        AsyncLambdaMicrovmsClient,
        AsyncLambdaMicrovmsClientConfig,
    )
    from capo_lambda_microvms._services.lambda_microvms import (
        LambdaMicrovmsClient,
        LambdaMicrovmsClientConfig,
    )


class MicrovmImage:
    def __init__(self, service: LambdaMicrovmsClient) -> None:
        self._service = service

    def read(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_image_output.GetMicrovmImageOutput":
        """<p>Retrieves the details of a MicroVM image, including its state, versions, and configuration.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.get_microvm_image_input.GetMicrovmImageInput]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.get_microvm_image_output.GetMicrovmImageOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm_image

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.get_microvm_image.get_microvm_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_image_input.GetMicrovmImageInput = {
            "image_identifier": image_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.delete_microvm_image_output.DeleteMicrovmImageOutput":
        """<p>Deletes a MicroVM image. This operation is idempotent; deleting an image that has already been deleted succeeds without error.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to delete.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.delete_microvm_image_input.DeleteMicrovmImageInput]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.delete_microvm_image_output.DeleteMicrovmImageOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image.delete_microvm_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.delete_microvm_image_input.DeleteMicrovmImageInput = {
            "image_identifier": image_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        name_filter: Optional[
            "capo_lambda_microvms.types.non_blank_string.NonBlankString"
        ] = None,
    ) -> "capo_lambda_microvms.types.list_microvm_images_response.ListMicrovmImagesResponse":
        """<p>Lists MicroVM images in the account with optional name filtering. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            name_filter: <p>Filters images whose name contains the specified string.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.list_microvm_images_request.ListMicrovmImagesRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.list_microvm_images_response.ListMicrovmImagesResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvm_images

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.list_microvm_images.list_microvm_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvm_images_request.ListMicrovmImagesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name_filter is not None:
            input_["name_filter"] = name_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_microvm_image_version(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.delete_microvm_image_version_output.DeleteMicrovmImageVersionOutput":
        """<p>Deletes a specific version of a MicroVM image. This operation is idempotent; deleting a version that has already been deleted succeeds without error.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to delete.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.delete_microvm_image_version_input.DeleteMicrovmImageVersionInput]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.delete_microvm_image_version_output.DeleteMicrovmImageVersionOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image_version

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image_version.delete_microvm_image_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.delete_microvm_image_version_input.DeleteMicrovmImageVersionInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_microvm_image_build(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        build_id: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_image_build_output.GetMicrovmImageBuildOutput":
        """<p>Retrieves the details of a specific MicroVM image build, including its state, target architecture, and snapshot information.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image.</p>
            build_id: <p>The unique identifier of the build to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.get_microvm_image_build_input.GetMicrovmImageBuildInput]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.get_microvm_image_build_output.GetMicrovmImageBuildOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_build

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_build.get_microvm_image_build(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_image_build_input.GetMicrovmImageBuildInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
            "build_id": build_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_microvm_image_version(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_image_version_output.GetMicrovmImageVersionOutput":
        """<p>Retrieves the details of a specific version of a MicroVM image, including its configuration, state, and build information.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.get_microvm_image_version_input.GetMicrovmImageVersionInput]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.get_microvm_image_version_output.GetMicrovmImageVersionOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_version

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_version.get_microvm_image_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_image_version_input.GetMicrovmImageVersionInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_managed_microvm_image_versions(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "capo_lambda_microvms.types.list_managed_microvm_image_versions_output.ListManagedMicrovmImageVersionsOutput":
        """<p>Lists versions of a managed MicroVM image. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the managed MicroVM image to list versions for.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.list_managed_microvm_image_versions_input.ListManagedMicrovmImageVersionsInput]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.list_managed_microvm_image_versions_output.ListManagedMicrovmImageVersionsOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_managed_microvm_image_versions

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.list_managed_microvm_image_versions.list_managed_microvm_image_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_managed_microvm_image_versions_input.ListManagedMicrovmImageVersionsInput = {
            "image_identifier": image_identifier
        }
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

    def list_microvm_image_builds(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        architecture: Optional[
            "capo_lambda_microvms.types.architecture.Architecture"
        ] = None,
        chipset: Optional["capo_lambda_microvms.types.chipset.Chipset"] = None,
        chipset_generation: Optional[
            "capo_lambda_microvms.types.non_blank_string.NonBlankString"
        ] = None,
    ) -> "capo_lambda_microvms.types.list_microvm_image_builds_output.ListMicrovmImageBuildsOutput":
        """<p>Lists builds for a MicroVM image version with optional filtering by architecture and chipset. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to list builds for.</p>
            architecture: <p>Filters builds by target CPU architecture.</p>
            chipset: <p>Filters builds by target chipset.</p>
            chipset_generation: <p>Filters builds by target chipset generation.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.list_microvm_image_builds_input.ListMicrovmImageBuildsInput]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.list_microvm_image_builds_output.ListMicrovmImageBuildsOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_builds

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_builds.list_microvm_image_builds(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvm_image_builds_input.ListMicrovmImageBuildsInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if architecture is not None:
            input_["architecture"] = architecture
        if chipset is not None:
            input_["chipset"] = chipset
        if chipset_generation is not None:
            input_["chipset_generation"] = chipset_generation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_microvm_image_versions(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "capo_lambda_microvms.types.list_microvm_image_versions_output.ListMicrovmImageVersionsOutput":
        """<p>Lists versions of a MicroVM image. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to list versions for.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.list_microvm_image_versions_input.ListMicrovmImageVersionsInput]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.list_microvm_image_versions_output.ListMicrovmImageVersionsOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_versions

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_versions.list_microvm_image_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvm_image_versions_input.ListMicrovmImageVersionsInput = {
            "image_identifier": image_identifier
        }
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

    def update_microvm_image(
        self,
        base_image_arn: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        build_role_arn: "capo_lambda_microvms.types.role_arn.RoleArn",
        code_artifact: "capo_lambda_microvms.types.code_artifact.CodeArtifact",
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
        base_image_version: Optional[
            "capo_lambda_microvms.types.version.Version"
        ] = None,
        description: Optional[str] = None,
        logging: Optional["capo_lambda_microvms.types.logging.Logging"] = None,
        egress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        cpu_configurations: Optional[
            "capo_lambda_microvms.types.cpu_configuration_list.CpuConfigurationList"
        ] = None,
        resources: Optional[
            "capo_lambda_microvms.types.resources_list.ResourcesList"
        ] = None,
        additional_os_capabilities: Optional[
            "capo_lambda_microvms.types.capability_list.CapabilityList"
        ] = None,
        hooks: Optional["capo_lambda_microvms.types.hooks.Hooks"] = None,
        environment_variables: Optional[
            "capo_lambda_microvms.types.environment_variable_map.EnvironmentVariableMap"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.update_microvm_image_response.UpdateMicrovmImageResponse":
        r"""<p>Updates the configuration of a MicroVM image and triggers a new version build. This operation uses PUT semantics — all required fields (codeArtifact, baseImageArn, buildRoleArn) must be provided with every request.</p>

        Args:
            base_image_arn: <p>The ARN of the base MicroVM image.</p>
            base_image_version: <p>The specific version of the base MicroVM image to use.</p>
            build_role_arn: <p>The ARN of the IAM build role.</p>
            description: <p>The description of the MicroVM image.</p>
            code_artifact: <p>The code artifact containing the application code and metadata for the MicroVM image.</p>
            logging: <p>The logging configuration for build-time and runtime logs. Specify {\"cloudWatch\": {\"logGroup\": \"...\"}} to stream logs to a custom CloudWatch log group, or {\"disabled\": {}} to turn off logging.</p>
            egress_network_connectors: <p>The list of egress network connectors available to the MicroVM at runtime.</p>
            cpu_configurations: <p>The list of supported CPU configurations for the MicroVM.</p>
            resources: <p>The resource requirements for the MicroVM.</p>
            additional_os_capabilities: <p>Additional OS capabilities granted to the MicroVM runtime environment.</p>
            environment_variables: <p>Environment variables set in the MicroVM runtime environment.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to update.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota for Lambda MicroVMs.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.update_microvm_image_request.UpdateMicrovmImageRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.update_microvm_image_response.UpdateMicrovmImageResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.update_microvm_image

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.update_microvm_image.update_microvm_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.update_microvm_image_request.UpdateMicrovmImageRequest = {
            "base_image_arn": base_image_arn,
            "build_role_arn": build_role_arn,
            "code_artifact": code_artifact,
            "image_identifier": image_identifier,
        }
        if base_image_version is not None:
            input_["base_image_version"] = base_image_version
        if description is not None:
            input_["description"] = description
        if logging is not None:
            input_["logging"] = logging
        if egress_network_connectors is not None:
            input_["egress_network_connectors"] = egress_network_connectors
        if cpu_configurations is not None:
            input_["cpu_configurations"] = cpu_configurations
        if resources is not None:
            input_["resources"] = resources
        if additional_os_capabilities is not None:
            input_["additional_os_capabilities"] = additional_os_capabilities
        if hooks is not None:
            input_["hooks"] = hooks
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
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

    def update_microvm_image_version(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        status: "capo_lambda_microvms.types.microvm_image_version_status.MicrovmImageVersionStatus",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.update_microvm_image_version_response.UpdateMicrovmImageVersionResponse":
        """<p>Updates the status of a specific MicroVM image version.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to update.</p>
            status: <p>The new status to set for the MicroVM image version.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.update_microvm_image_version_request.UpdateMicrovmImageVersionRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.update_microvm_image_version_response.UpdateMicrovmImageVersionResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.update_microvm_image_version

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.update_microvm_image_version.update_microvm_image_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.update_microvm_image_version_request.UpdateMicrovmImageVersionRequest = {
            "image_identifier": image_identifier,
            "image_version": image_version,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMicrovmImage:
    def __init__(self, service: AsyncLambdaMicrovmsClient) -> None:
        self._service = service

    async def read(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_image_output.GetMicrovmImageOutput":
        """<p>Retrieves the details of a MicroVM image, including its state, versions, and configuration.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.get_microvm_image_input.GetMicrovmImageInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.get_microvm_image_output.GetMicrovmImageOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm_image

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.get_microvm_image.async_get_microvm_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_image_input.GetMicrovmImageInput = {
            "image_identifier": image_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.delete_microvm_image_output.DeleteMicrovmImageOutput":
        """<p>Deletes a MicroVM image. This operation is idempotent; deleting an image that has already been deleted succeeds without error.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to delete.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.delete_microvm_image_input.DeleteMicrovmImageInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.delete_microvm_image_output.DeleteMicrovmImageOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image.async_delete_microvm_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.delete_microvm_image_input.DeleteMicrovmImageInput = {
            "image_identifier": image_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        name_filter: Optional[
            "capo_lambda_microvms.types.non_blank_string.NonBlankString"
        ] = None,
    ) -> "capo_lambda_microvms.types.list_microvm_images_response.ListMicrovmImagesResponse":
        """<p>Lists MicroVM images in the account with optional name filtering. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            name_filter: <p>Filters images whose name contains the specified string.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_microvm_images_request.ListMicrovmImagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_microvm_images_response.ListMicrovmImagesResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvm_images

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_microvm_images.async_list_microvm_images(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvm_images_request.ListMicrovmImagesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name_filter is not None:
            input_["name_filter"] = name_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_microvm_image_version(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.delete_microvm_image_version_output.DeleteMicrovmImageVersionOutput":
        """<p>Deletes a specific version of a MicroVM image. This operation is idempotent; deleting a version that has already been deleted succeeds without error.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to delete.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.delete_microvm_image_version_input.DeleteMicrovmImageVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.delete_microvm_image_version_output.DeleteMicrovmImageVersionOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image_version

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image_version.async_delete_microvm_image_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.delete_microvm_image_version_input.DeleteMicrovmImageVersionInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_microvm_image_build(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        build_id: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_image_build_output.GetMicrovmImageBuildOutput":
        """<p>Retrieves the details of a specific MicroVM image build, including its state, target architecture, and snapshot information.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image.</p>
            build_id: <p>The unique identifier of the build to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.get_microvm_image_build_input.GetMicrovmImageBuildInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.get_microvm_image_build_output.GetMicrovmImageBuildOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_build

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_build.async_get_microvm_image_build(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_image_build_input.GetMicrovmImageBuildInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
            "build_id": build_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_microvm_image_version(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_image_version_output.GetMicrovmImageVersionOutput":
        """<p>Retrieves the details of a specific version of a MicroVM image, including its configuration, state, and build information.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.get_microvm_image_version_input.GetMicrovmImageVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.get_microvm_image_version_output.GetMicrovmImageVersionOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_version

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_version.async_get_microvm_image_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_image_version_input.GetMicrovmImageVersionInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_microvm_image_versions(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "capo_lambda_microvms.types.list_managed_microvm_image_versions_output.ListManagedMicrovmImageVersionsOutput":
        """<p>Lists versions of a managed MicroVM image. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the managed MicroVM image to list versions for.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_managed_microvm_image_versions_input.ListManagedMicrovmImageVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_managed_microvm_image_versions_output.ListManagedMicrovmImageVersionsOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_managed_microvm_image_versions

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_managed_microvm_image_versions.async_list_managed_microvm_image_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_managed_microvm_image_versions_input.ListManagedMicrovmImageVersionsInput = {
            "image_identifier": image_identifier
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

    async def list_microvm_image_builds(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        architecture: Optional[
            "capo_lambda_microvms.types.architecture.Architecture"
        ] = None,
        chipset: Optional["capo_lambda_microvms.types.chipset.Chipset"] = None,
        chipset_generation: Optional[
            "capo_lambda_microvms.types.non_blank_string.NonBlankString"
        ] = None,
    ) -> "capo_lambda_microvms.types.list_microvm_image_builds_output.ListMicrovmImageBuildsOutput":
        """<p>Lists builds for a MicroVM image version with optional filtering by architecture and chipset. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to list builds for.</p>
            architecture: <p>Filters builds by target CPU architecture.</p>
            chipset: <p>Filters builds by target chipset.</p>
            chipset_generation: <p>Filters builds by target chipset generation.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_microvm_image_builds_input.ListMicrovmImageBuildsInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_microvm_image_builds_output.ListMicrovmImageBuildsOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_builds

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_builds.async_list_microvm_image_builds(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvm_image_builds_input.ListMicrovmImageBuildsInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if architecture is not None:
            input_["architecture"] = architecture
        if chipset is not None:
            input_["chipset"] = chipset
        if chipset_generation is not None:
            input_["chipset_generation"] = chipset_generation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_microvm_image_versions(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "capo_lambda_microvms.types.list_microvm_image_versions_output.ListMicrovmImageVersionsOutput":
        """<p>Lists versions of a MicroVM image. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to list versions for.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_microvm_image_versions_input.ListMicrovmImageVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_microvm_image_versions_output.ListMicrovmImageVersionsOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_versions

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_versions.async_list_microvm_image_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvm_image_versions_input.ListMicrovmImageVersionsInput = {
            "image_identifier": image_identifier
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

    async def update_microvm_image(
        self,
        base_image_arn: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        build_role_arn: "capo_lambda_microvms.types.role_arn.RoleArn",
        code_artifact: "capo_lambda_microvms.types.code_artifact.CodeArtifact",
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        base_image_version: Optional[
            "capo_lambda_microvms.types.version.Version"
        ] = None,
        description: Optional[str] = None,
        logging: Optional["capo_lambda_microvms.types.logging.Logging"] = None,
        egress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        cpu_configurations: Optional[
            "capo_lambda_microvms.types.cpu_configuration_list.CpuConfigurationList"
        ] = None,
        resources: Optional[
            "capo_lambda_microvms.types.resources_list.ResourcesList"
        ] = None,
        additional_os_capabilities: Optional[
            "capo_lambda_microvms.types.capability_list.CapabilityList"
        ] = None,
        hooks: Optional["capo_lambda_microvms.types.hooks.Hooks"] = None,
        environment_variables: Optional[
            "capo_lambda_microvms.types.environment_variable_map.EnvironmentVariableMap"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.update_microvm_image_response.UpdateMicrovmImageResponse":
        r"""<p>Updates the configuration of a MicroVM image and triggers a new version build. This operation uses PUT semantics — all required fields (codeArtifact, baseImageArn, buildRoleArn) must be provided with every request.</p>

        Args:
            base_image_arn: <p>The ARN of the base MicroVM image.</p>
            base_image_version: <p>The specific version of the base MicroVM image to use.</p>
            build_role_arn: <p>The ARN of the IAM build role.</p>
            description: <p>The description of the MicroVM image.</p>
            code_artifact: <p>The code artifact containing the application code and metadata for the MicroVM image.</p>
            logging: <p>The logging configuration for build-time and runtime logs. Specify {\"cloudWatch\": {\"logGroup\": \"...\"}} to stream logs to a custom CloudWatch log group, or {\"disabled\": {}} to turn off logging.</p>
            egress_network_connectors: <p>The list of egress network connectors available to the MicroVM at runtime.</p>
            cpu_configurations: <p>The list of supported CPU configurations for the MicroVM.</p>
            resources: <p>The resource requirements for the MicroVM.</p>
            additional_os_capabilities: <p>Additional OS capabilities granted to the MicroVM runtime environment.</p>
            environment_variables: <p>Environment variables set in the MicroVM runtime environment.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to update.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota for Lambda MicroVMs.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.update_microvm_image_request.UpdateMicrovmImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.update_microvm_image_response.UpdateMicrovmImageResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.update_microvm_image

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.update_microvm_image.async_update_microvm_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.update_microvm_image_request.UpdateMicrovmImageRequest = {
            "base_image_arn": base_image_arn,
            "build_role_arn": build_role_arn,
            "code_artifact": code_artifact,
            "image_identifier": image_identifier,
        }
        if base_image_version is not None:
            input_["base_image_version"] = base_image_version
        if description is not None:
            input_["description"] = description
        if logging is not None:
            input_["logging"] = logging
        if egress_network_connectors is not None:
            input_["egress_network_connectors"] = egress_network_connectors
        if cpu_configurations is not None:
            input_["cpu_configurations"] = cpu_configurations
        if resources is not None:
            input_["resources"] = resources
        if additional_os_capabilities is not None:
            input_["additional_os_capabilities"] = additional_os_capabilities
        if hooks is not None:
            input_["hooks"] = hooks
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
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

    async def update_microvm_image_version(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        status: "capo_lambda_microvms.types.microvm_image_version_status.MicrovmImageVersionStatus",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.update_microvm_image_version_response.UpdateMicrovmImageVersionResponse":
        """<p>Updates the status of a specific MicroVM image version.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to update.</p>
            status: <p>The new status to set for the MicroVM image version.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.update_microvm_image_version_request.UpdateMicrovmImageVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.update_microvm_image_version_response.UpdateMicrovmImageVersionResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.update_microvm_image_version

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.update_microvm_image_version.async_update_microvm_image_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.update_microvm_image_version_request.UpdateMicrovmImageVersionRequest = {
            "image_identifier": image_identifier,
            "image_version": image_version,
            "status": status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
