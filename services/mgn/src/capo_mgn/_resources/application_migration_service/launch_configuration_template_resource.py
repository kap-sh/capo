from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_mgn._auth._signers
import capo_mgn._auth._sigv4
from capo_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mgn.types.action_category
    import capo_mgn.types.action_description
    import capo_mgn.types.action_id
    import capo_mgn.types.arn
    import capo_mgn.types.boot_mode
    import capo_mgn.types.bounded_string
    import capo_mgn.types.create_launch_configuration_template_request
    import capo_mgn.types.delete_launch_configuration_template_request
    import capo_mgn.types.delete_launch_configuration_template_response
    import capo_mgn.types.describe_launch_configuration_templates_request
    import capo_mgn.types.describe_launch_configuration_templates_response
    import capo_mgn.types.document_version
    import capo_mgn.types.kms_key_arn
    import capo_mgn.types.launch_configuration_template
    import capo_mgn.types.launch_configuration_template_i_ds
    import capo_mgn.types.launch_configuration_template_id
    import capo_mgn.types.launch_disposition
    import capo_mgn.types.launch_template_disk_conf
    import capo_mgn.types.licensing
    import capo_mgn.types.list_template_actions_request
    import capo_mgn.types.list_template_actions_response
    import capo_mgn.types.max_results_type
    import capo_mgn.types.operating_system_string
    import capo_mgn.types.order_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.positive_integer
    import capo_mgn.types.post_launch_actions
    import capo_mgn.types.put_template_action_request
    import capo_mgn.types.remove_template_action_request
    import capo_mgn.types.remove_template_action_response
    import capo_mgn.types.ssm_document_external_parameters
    import capo_mgn.types.ssm_document_parameters
    import capo_mgn.types.strictly_positive_integer
    import capo_mgn.types.tag_value
    import capo_mgn.types.tags_map
    import capo_mgn.types.target_instance_type_right_sizing_method
    import capo_mgn.types.template_action_document
    import capo_mgn.types.template_actions_request_filters
    import capo_mgn.types.update_launch_configuration_template_request
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class LaunchConfigurationTemplateResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        post_launch_actions: Optional[
            "capo_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional["capo_mgn.types.tag_value.TagValue"] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        launch_disposition: Optional[
            "capo_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["capo_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "capo_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional[
            "capo_mgn.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            post_launch_actions: <p>Launch configuration template post launch actions.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.create_launch_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_launch_configuration_template.create_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_launch_configuration_template_request

            return capo_mgn.types.create_launch_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_mgn.types.launch_configuration_template

            return capo_mgn.types.launch_configuration_template.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateLaunchConfigurationTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
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
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        post_launch_actions: Optional[
            "capo_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional["capo_mgn.types.tag_value.TagValue"] = None,
        launch_disposition: Optional[
            "capo_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["capo_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "capo_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional["capo_mgn.types.arn.ARN"] = None,
    ) -> "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            post_launch_actions: <p>Post Launch Action to execute on the Test or Cutover instance.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.update_launch_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_launch_configuration_template.update_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_mgn.types.launch_configuration_template

            return capo_mgn.types.launch_configuration_template.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateLaunchConfigurationTemplate", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>ID of resource to be deleted.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_launch_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_launch_configuration_template.delete_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteLaunchConfigurationTemplate")
        )
        input_: capo_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {
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
        config_overrides: Optional[mgnClientConfig] = None,
        launch_configuration_template_i_ds: Optional[
            "capo_mgn.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>Next pagination token returned from DescribeLaunchConfigurationTemplates.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_launch_configuration_templates

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_launch_configuration_templates.describe_launch_configuration_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_launch_configuration_templates_response

            return capo_mgn.types.describe_launch_configuration_templates_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeLaunchConfigurationTemplates", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}
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

    def list_template_actions(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.template_actions_request_filters.TemplateActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_template_actions_response.ListTemplateActionsResponse":
        """<p>List template post migration custom actions.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            filters: <p>Filters to apply when listing template post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing template post migration custom actions.</p>
            next_token: <p>Next token to use when listing template post migration custom actions.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_template_actions_request.ListTemplateActionsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_template_actions_response.ListTemplateActionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_template_actions

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_template_actions.list_template_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTemplateActions")
        )
        input_: capo_mgn.types.list_template_actions_request.ListTemplateActionsRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    def put_template_action(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_name: "capo_mgn.types.bounded_string.BoundedString",
        document_identifier: "capo_mgn.types.bounded_string.BoundedString",
        order: "capo_mgn.types.order_type.OrderType",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        document_version: Optional[
            "capo_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "capo_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        operating_system: Optional[
            "capo_mgn.types.operating_system_string.OperatingSystemString"
        ] = None,
        external_parameters: Optional[
            "capo_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "capo_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["capo_mgn.types.action_category.ActionCategory"] = None,
    ) -> "capo_mgn.types.template_action_document.TemplateActionDocument":
        """<p>Put template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            action_name: <p>Template post migration custom action name.</p>
            document_identifier: <p>Template post migration custom action document identifier.</p>
            order: <p>Template post migration custom action order.</p>
            action_id: <p>Template post migration custom action ID.</p>
            document_version: <p>Template post migration custom action document version.</p>
            active: <p>Template post migration custom action active status.</p>
            timeout_seconds: <p>Template post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Template post migration custom action must succeed for cutover.</p>
            parameters: <p>Template post migration custom action parameters.</p>
            operating_system: <p>Operating system eligible for this template post migration custom action.</p>
            external_parameters: <p>Template post migration custom action external parameters.</p>
            description: <p>Template post migration custom action description.</p>
            category: <p>Template post migration custom action category.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.put_template_action_request.PutTemplateActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.template_action_document.TemplateActionDocument"
        ]:
            import capo_mgn._operations.application_migration_service.put_template_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.put_template_action.put_template_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTemplateAction")
        )
        input_: capo_mgn.types.put_template_action_request.PutTemplateActionRequest = {
            "launch_configuration_template_id": launch_configuration_template_id,
            "action_name": action_name,
            "document_identifier": document_identifier,
            "order": order,
            "action_id": action_id,
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if active is not None:
            input_["active"] = active
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input_["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input_["parameters"] = parameters
        if operating_system is not None:
            input_["operating_system"] = operating_system
        if external_parameters is not None:
            input_["external_parameters"] = external_parameters
        if description is not None:
            input_["description"] = description
        if category is not None:
            input_["category"] = category

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_template_action(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.remove_template_action_response.RemoveTemplateActionResponse":
        """<p>Remove template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID of the post migration custom action to remove.</p>
            action_id: <p>Template post migration custom action ID to remove.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.remove_template_action_request.RemoveTemplateActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.remove_template_action_response.RemoveTemplateActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.remove_template_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.remove_template_action.remove_template_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RemoveTemplateAction")
        )
        input_: capo_mgn.types.remove_template_action_request.RemoveTemplateActionRequest = {
            "launch_configuration_template_id": launch_configuration_template_id,
            "action_id": action_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncLaunchConfigurationTemplateResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        post_launch_actions: Optional[
            "capo_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional["capo_mgn.types.tag_value.TagValue"] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        launch_disposition: Optional[
            "capo_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["capo_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "capo_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional[
            "capo_mgn.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            post_launch_actions: <p>Launch configuration template post launch actions.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.create_launch_configuration_template

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.create_launch_configuration_template.async_create_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_launch_configuration_template_request

            return capo_mgn.types.create_launch_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_mgn.types.launch_configuration_template

            return capo_mgn.types.launch_configuration_template.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateLaunchConfigurationTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
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
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        post_launch_actions: Optional[
            "capo_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional["capo_mgn.types.tag_value.TagValue"] = None,
        launch_disposition: Optional[
            "capo_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["capo_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "capo_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional["capo_mgn.types.arn.ARN"] = None,
    ) -> "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            post_launch_actions: <p>Post Launch Action to execute on the Test or Cutover instance.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.update_launch_configuration_template

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_launch_configuration_template.async_update_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_mgn.types.launch_configuration_template

            return capo_mgn.types.launch_configuration_template.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateLaunchConfigurationTemplate", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> "capo_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>ID of resource to be deleted.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_launch_configuration_template

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.delete_launch_configuration_template.async_delete_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteLaunchConfigurationTemplate")
        )
        input_: capo_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {
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
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        launch_configuration_template_i_ds: Optional[
            "capo_mgn.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>Next pagination token returned from DescribeLaunchConfigurationTemplates.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_launch_configuration_templates

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.describe_launch_configuration_templates.async_describe_launch_configuration_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_launch_configuration_templates_response

            return capo_mgn.types.describe_launch_configuration_templates_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeLaunchConfigurationTemplates", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}
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

    async def list_template_actions(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.template_actions_request_filters.TemplateActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_template_actions_response.ListTemplateActionsResponse":
        """<p>List template post migration custom actions.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            filters: <p>Filters to apply when listing template post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing template post migration custom actions.</p>
            next_token: <p>Next token to use when listing template post migration custom actions.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_template_actions_request.ListTemplateActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_template_actions_response.ListTemplateActionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_template_actions

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_template_actions.async_list_template_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTemplateActions")
        )
        input_: capo_mgn.types.list_template_actions_request.ListTemplateActionsRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def put_template_action(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_name: "capo_mgn.types.bounded_string.BoundedString",
        document_identifier: "capo_mgn.types.bounded_string.BoundedString",
        order: "capo_mgn.types.order_type.OrderType",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        document_version: Optional[
            "capo_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "capo_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        operating_system: Optional[
            "capo_mgn.types.operating_system_string.OperatingSystemString"
        ] = None,
        external_parameters: Optional[
            "capo_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "capo_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["capo_mgn.types.action_category.ActionCategory"] = None,
    ) -> "capo_mgn.types.template_action_document.TemplateActionDocument":
        """<p>Put template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            action_name: <p>Template post migration custom action name.</p>
            document_identifier: <p>Template post migration custom action document identifier.</p>
            order: <p>Template post migration custom action order.</p>
            action_id: <p>Template post migration custom action ID.</p>
            document_version: <p>Template post migration custom action document version.</p>
            active: <p>Template post migration custom action active status.</p>
            timeout_seconds: <p>Template post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Template post migration custom action must succeed for cutover.</p>
            parameters: <p>Template post migration custom action parameters.</p>
            operating_system: <p>Operating system eligible for this template post migration custom action.</p>
            external_parameters: <p>Template post migration custom action external parameters.</p>
            description: <p>Template post migration custom action description.</p>
            category: <p>Template post migration custom action category.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.put_template_action_request.PutTemplateActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.template_action_document.TemplateActionDocument"
        ]:
            import capo_mgn._operations.application_migration_service.put_template_action

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.put_template_action.async_put_template_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTemplateAction")
        )
        input_: capo_mgn.types.put_template_action_request.PutTemplateActionRequest = {
            "launch_configuration_template_id": launch_configuration_template_id,
            "action_name": action_name,
            "document_identifier": document_identifier,
            "order": order,
            "action_id": action_id,
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if active is not None:
            input_["active"] = active
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input_["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input_["parameters"] = parameters
        if operating_system is not None:
            input_["operating_system"] = operating_system
        if external_parameters is not None:
            input_["external_parameters"] = external_parameters
        if description is not None:
            input_["description"] = description
        if category is not None:
            input_["category"] = category

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_template_action(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> "capo_mgn.types.remove_template_action_response.RemoveTemplateActionResponse":
        """<p>Remove template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID of the post migration custom action to remove.</p>
            action_id: <p>Template post migration custom action ID to remove.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.remove_template_action_request.RemoveTemplateActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.remove_template_action_response.RemoveTemplateActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.remove_template_action

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.remove_template_action.async_remove_template_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RemoveTemplateAction")
        )
        input_: capo_mgn.types.remove_template_action_request.RemoveTemplateActionRequest = {
            "launch_configuration_template_id": launch_configuration_template_id,
            "action_id": action_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
