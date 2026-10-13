from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_drs._auth._signers
import capo_drs._auth._sigv4
from capo_drs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_drs.types.arn
    import capo_drs.types.create_launch_configuration_template_request
    import capo_drs.types.create_launch_configuration_template_response
    import capo_drs.types.delete_launch_configuration_template_request
    import capo_drs.types.delete_launch_configuration_template_response
    import capo_drs.types.describe_launch_configuration_templates_request
    import capo_drs.types.describe_launch_configuration_templates_response
    import capo_drs.types.launch_configuration_template
    import capo_drs.types.launch_configuration_template_i_ds
    import capo_drs.types.launch_configuration_template_id
    import capo_drs.types.launch_disposition
    import capo_drs.types.licensing
    import capo_drs.types.max_results_type
    import capo_drs.types.pagination_token
    import capo_drs.types.recovery_mode
    import capo_drs.types.tags_map
    import capo_drs.types.target_instance_type_right_sizing_method
    import capo_drs.types.update_launch_configuration_template_request
    import capo_drs.types.update_launch_configuration_template_response
    from capo_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from capo_drs._services.drs import drsClient, drsClientConfig


class LaunchConfigurationTemplateResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[drsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        launch_disposition: Optional[
            "capo_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_drs.types.licensing.Licensing"] = None,
        export_bucket_arn: Optional["capo_drs.types.arn.ARN"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_source_instance: Optional[bool] = None,
        recovery_mode: Optional["capo_drs.types.recovery_mode.RecoveryMode"] = None,
    ) -> "capo_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>
            recovery_mode: <p>Recovery mode.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template.create_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.create_launch_configuration_template_request

            return capo_drs.types.create_launch_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.create_launch_configuration_template_response

            return capo_drs.types.create_launch_configuration_template_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateLaunchConfigurationTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}
        if tags is not None:
            input_["tags"] = tags
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if export_bucket_arn is not None:
            input_["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input_["launch_into_source_instance"] = launch_into_source_instance
        if recovery_mode is not None:
            input_["recovery_mode"] = recovery_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        launch_configuration_template_id: "capo_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        launch_disposition: Optional[
            "capo_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_drs.types.licensing.Licensing"] = None,
        export_bucket_arn: Optional["capo_drs.types.arn.ARN"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_source_instance: Optional[bool] = None,
        recovery_mode: Optional["capo_drs.types.recovery_mode.RecoveryMode"] = None,
    ) -> "capo_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>
            recovery_mode: <p>Recovery mode.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template.update_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.update_launch_configuration_template_response

            return capo_drs.types.update_launch_configuration_template_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateLaunchConfigurationTemplate", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if export_bucket_arn is not None:
            input_["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input_["launch_into_source_instance"] = launch_into_source_instance
        if recovery_mode is not None:
            input_["recovery_mode"] = recovery_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        launch_configuration_template_id: "capo_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>The ID of the Launch Configuration Template to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template.delete_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteLaunchConfigurationTemplate")
        )
        input_: capo_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
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
        config_overrides: Optional[drsClientConfig] = None,
        launch_configuration_template_i_ds: Optional[
            "capo_drs.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_drs.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>The token of the next Launch Configuration Template to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]",
        ) -> OperationResponse[
            "capo_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates.describe_launch_configuration_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_launch_configuration_templates_response

            return capo_drs.types.describe_launch_configuration_templates_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeLaunchConfigurationTemplates", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}
        if launch_configuration_template_i_ds is not None:
            input_["launch_configuration_template_i_ds"] = (
                launch_configuration_template_i_ds
            )
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


class AsyncLaunchConfigurationTemplateResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        launch_disposition: Optional[
            "capo_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_drs.types.licensing.Licensing"] = None,
        export_bucket_arn: Optional["capo_drs.types.arn.ARN"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_source_instance: Optional[bool] = None,
        recovery_mode: Optional["capo_drs.types.recovery_mode.RecoveryMode"] = None,
    ) -> "capo_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>
            recovery_mode: <p>Recovery mode.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template.async_create_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.create_launch_configuration_template_request

            return capo_drs.types.create_launch_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.create_launch_configuration_template_response

            return capo_drs.types.create_launch_configuration_template_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateLaunchConfigurationTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}
        if tags is not None:
            input_["tags"] = tags
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if export_bucket_arn is not None:
            input_["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input_["launch_into_source_instance"] = launch_into_source_instance
        if recovery_mode is not None:
            input_["recovery_mode"] = recovery_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        launch_configuration_template_id: "capo_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        launch_disposition: Optional[
            "capo_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_drs.types.licensing.Licensing"] = None,
        export_bucket_arn: Optional["capo_drs.types.arn.ARN"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_source_instance: Optional[bool] = None,
        recovery_mode: Optional["capo_drs.types.recovery_mode.RecoveryMode"] = None,
    ) -> "capo_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>
            recovery_mode: <p>Recovery mode.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template.async_update_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.update_launch_configuration_template_response

            return capo_drs.types.update_launch_configuration_template_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateLaunchConfigurationTemplate", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if export_bucket_arn is not None:
            input_["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input_["launch_into_source_instance"] = launch_into_source_instance
        if recovery_mode is not None:
            input_["recovery_mode"] = recovery_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        launch_configuration_template_id: "capo_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>The ID of the Launch Configuration Template to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template.async_delete_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteLaunchConfigurationTemplate")
        )
        input_: capo_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
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
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        launch_configuration_template_i_ds: Optional[
            "capo_drs.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_drs.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>The token of the next Launch Configuration Template to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates.async_describe_launch_configuration_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_launch_configuration_templates_response

            return capo_drs.types.describe_launch_configuration_templates_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeLaunchConfigurationTemplates", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}
        if launch_configuration_template_i_ds is not None:
            input_["launch_configuration_template_i_ds"] = (
                launch_configuration_template_i_ds
            )
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
