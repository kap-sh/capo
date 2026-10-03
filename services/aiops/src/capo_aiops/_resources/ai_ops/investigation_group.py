from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_aiops._auth._signers
import capo_aiops._auth._sigv4
from capo_aiops._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_aiops.types.chatbot_notification_channel
    import capo_aiops.types.create_investigation_group_input
    import capo_aiops.types.create_investigation_group_output
    import capo_aiops.types.cross_account_configurations
    import capo_aiops.types.delete_investigation_group_request
    import capo_aiops.types.encryption_configuration
    import capo_aiops.types.get_investigation_group_request
    import capo_aiops.types.get_investigation_group_response
    import capo_aiops.types.investigation_group_identifier
    import capo_aiops.types.list_investigation_groups_input
    import capo_aiops.types.list_investigation_groups_model
    import capo_aiops.types.list_investigation_groups_output
    import capo_aiops.types.retention
    import capo_aiops.types.role_arn
    import capo_aiops.types.sensitive_string_with_length_limits
    import capo_aiops.types.string_with_pattern_and_length_limits
    import capo_aiops.types.tag_key_boundaries
    import capo_aiops.types.tags
    import capo_aiops.types.update_investigation_group_output
    import capo_aiops.types.update_investigation_group_request
    from capo_aiops._services.ai_ops import AIOpsClient, AIOpsClientConfig
    from capo_aiops._services.async_ai_ops import (
        AsyncAIOpsClient,
        AsyncAIOpsClientConfig,
    )


class InvestigationGroup:
    def __init__(self, service: AIOpsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_aiops.types.string_with_pattern_and_length_limits.StringWithPatternAndLengthLimits",
        role_arn: "capo_aiops.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
        encryption_configuration: Optional[
            "capo_aiops.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        retention_in_days: Optional["capo_aiops.types.retention.Retention"] = None,
        tags: Optional["capo_aiops.types.tags.Tags"] = None,
        tag_key_boundaries: Optional[
            "capo_aiops.types.tag_key_boundaries.TagKeyBoundaries"
        ] = None,
        chatbot_notification_channel: Optional[
            "capo_aiops.types.chatbot_notification_channel.ChatbotNotificationChannel"
        ] = None,
        is_cloud_trail_event_history_enabled: Optional[bool] = None,
        cross_account_configurations: Optional[
            "capo_aiops.types.cross_account_configurations.CrossAccountConfigurations"
        ] = None,
    ) -> "capo_aiops.types.create_investigation_group_output.CreateInvestigationGroupOutput":
        """<p>Creates an <i>investigation group</i> in your account. Creating an investigation group is a one-time setup task for each Region in your account. It is a necessary task to be able to perform investigations.</p> <p>Settings in the investigation group help you centrally manage the common properties of your investigations, such as the following:</p> <ul> <li> <p>Who can access the investigations</p> </li> <li> <p>Whether investigation data is encrypted with a customer managed Key Management Service key.</p> </li> <li> <p>How long investigations and their data are retained by default.</p> </li> </ul> <p>Currently, you can have one investigation group in each Region in your account. Each investigation in a Region is a part of the investigation group in that Region</p> <p>To create an investigation group and set up CloudWatch investigations, you must be signed in to an IAM principal that has either the <code>AIOpsConsoleAdminPolicy</code> or the <code>AdministratorAccess</code> IAM policy attached, or to an account that has similar permissions.</p> <important> <p>You can configure CloudWatch alarms to start investigations and add events to investigations. If you create your investigation group with <code>CreateInvestigationGroup</code> and you want to enable alarms to do this, you must use <code>PutInvestigationGroupPolicy</code> to create a resource policy that grants this permission to CloudWatch alarms. </p> <p>For more information about configuring CloudWatch alarms, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html">Using Amazon CloudWatch alarms</a> </p> </important>

        Args:
            name: <p>Provides a name for the investigation group.</p>
            role_arn: <p>Specify the ARN of the IAM role that CloudWatch investigations will use when it gathers investigation data. The permissions in this role determine which of your resources that CloudWatch investigations will have access to during investigations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-Security-Data">How to control what data CloudWatch investigations has access to during investigations</a>.</p>
            encryption_configuration: <p>Use this structure if you want to use a customer managed KMS key to encrypt your investigation data. If you omit this parameter, CloudWatch investigations will use an Amazon Web Services key to encrypt the data. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-KMS">Encryption of investigation data</a>.</p>
            retention_in_days: <p>Specify how long that investigation data is kept. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Retention.html">Operational investigation data retention</a>. </p> <p>If you omit this parameter, the default of 90 days is used.</p>
            tags: <p>A list of key-value pairs to associate with the investigation group. You can associate as many as 50 tags with an investigation group. To be able to associate tags when you create the investigation group, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p>
            tag_key_boundaries: <p>Enter the existing custom tag keys for custom applications in your system. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources. For example, to discover that an Amazon ECS service depends on an Amazon RDS database, CloudWatch investigations can discover this relationship using data sources such as X-Ray and CloudWatch Application Signals. However, if you haven't deployed these features, CloudWatch investigations will attempt to identify possible relationships. Tag boundaries can be used to narrow the resources that will be discovered by CloudWatch investigations in these cases.</p> <p>You don't need to enter tags created by myApplications or CloudFormation, because CloudWatch investigations can automatically detect those tags.</p>
            chatbot_notification_channel: <p>Use this structure to integrate CloudWatch investigations with chat applications. This structure is a string array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html">Getting started with Amazon Q in chat applications</a> and <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies">Resource type defined by Amazon Web Services Chatbot</a>.</p>
            is_cloud_trail_event_history_enabled: <p>Specify <code>true</code> to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is <code>true</code>.</p>
            cross_account_configurations: <p>List of <code>sourceRoleArn</code> values that have been configured for cross-account access.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_aiops.types.create_investigation_group_input.CreateInvestigationGroupInput]",
        ) -> OperationResponse[
            "capo_aiops.types.create_investigation_group_output.CreateInvestigationGroupOutput"
        ]:
            import capo_aiops._operations.ai_ops.create_investigation_group

            output, http_response = (
                capo_aiops._operations.ai_ops.create_investigation_group.create_investigation_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.create_investigation_group_input.CreateInvestigationGroupInput = {
            "name": name,
            "role_arn": role_arn,
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if retention_in_days is not None:
            input_["retention_in_days"] = retention_in_days
        if tags is not None:
            input_["tags"] = tags
        if tag_key_boundaries is not None:
            input_["tag_key_boundaries"] = tag_key_boundaries
        if chatbot_notification_channel is not None:
            input_["chatbot_notification_channel"] = chatbot_notification_channel
        if is_cloud_trail_event_history_enabled is not None:
            input_["is_cloud_trail_event_history_enabled"] = (
                is_cloud_trail_event_history_enabled
            )
        if cross_account_configurations is not None:
            input_["cross_account_configurations"] = cross_account_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "capo_aiops.types.get_investigation_group_response.GetInvestigationGroupResponse":
        """<p>Returns the configuration information for the specified investigation group.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to view. This is used to set the name of the investigation group.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_aiops.types.get_investigation_group_request.GetInvestigationGroupRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.get_investigation_group_response.GetInvestigationGroupResponse"
        ]:
            import capo_aiops._operations.ai_ops.get_investigation_group

            output, http_response = (
                capo_aiops._operations.ai_ops.get_investigation_group.get_investigation_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.get_investigation_group_request.GetInvestigationGroupRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
        role_arn: Optional["capo_aiops.types.role_arn.RoleArn"] = None,
        encryption_configuration: Optional[
            "capo_aiops.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tag_key_boundaries: Optional[
            "capo_aiops.types.tag_key_boundaries.TagKeyBoundaries"
        ] = None,
        chatbot_notification_channel: Optional[
            "capo_aiops.types.chatbot_notification_channel.ChatbotNotificationChannel"
        ] = None,
        is_cloud_trail_event_history_enabled: Optional[bool] = None,
        cross_account_configurations: Optional[
            "capo_aiops.types.cross_account_configurations.CrossAccountConfigurations"
        ] = None,
    ) -> "capo_aiops.types.update_investigation_group_output.UpdateInvestigationGroupOutput":
        """<p>Updates the configuration of the specified investigation group.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to modify.</p>
            role_arn: <p>Specify this field if you want to change the IAM role that CloudWatch investigations will use when it gathers investigation data. To do so, specify the ARN of the new role.</p> <p>The permissions in this role determine which of your resources that CloudWatch investigations will have access to during investigations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-Security-Data">How to control what data CloudWatch investigations has access to during investigations</a>.</p>
            encryption_configuration: <p>Use this structure if you want to use a customer managed KMS key to encrypt your investigation data. If you omit this parameter, CloudWatch investigations will use an Amazon Web Services key to encrypt the data. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-KMS">Encryption of investigation data</a>.</p>
            tag_key_boundaries: <p>Enter the existing custom tag keys for custom applications in your system. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources. For example, to discover that an Amazon ECS service depends on an Amazon RDS database, CloudWatch investigations can discover this relationship using data sources such as X-Ray and CloudWatch Application Signals. However, if you haven't deployed these features, CloudWatch investigations will attempt to identify possible relationships. Tag boundaries can be used to narrow the resources that will be discovered by CloudWatch investigations in these cases.</p> <p>You don't need to enter tags created by myApplications or CloudFormation, because CloudWatch investigations can automatically detect those tags.</p>
            chatbot_notification_channel: <p>Use this structure to integrate CloudWatch investigations with chat applications. This structure is a string array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html">Getting started with Amazon Q in chat applications</a> and <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies">Resource type defined by Amazon Web Services Chatbot</a>.</p>
            is_cloud_trail_event_history_enabled: <p>Specify <code>true</code> to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is <code>true</code>.</p>
            cross_account_configurations: <p>Used to configure cross-account access for an investigation group. It allows the investigation group to access resources in other accounts. </p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_aiops.types.update_investigation_group_request.UpdateInvestigationGroupRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.update_investigation_group_output.UpdateInvestigationGroupOutput"
        ]:
            import capo_aiops._operations.ai_ops.update_investigation_group

            output, http_response = (
                capo_aiops._operations.ai_ops.update_investigation_group.update_investigation_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.update_investigation_group_request.UpdateInvestigationGroupRequest = {
            "identifier": identifier
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tag_key_boundaries is not None:
            input_["tag_key_boundaries"] = tag_key_boundaries
        if chatbot_notification_channel is not None:
            input_["chatbot_notification_channel"] = chatbot_notification_channel
        if is_cloud_trail_event_history_enabled is not None:
            input_["is_cloud_trail_event_history_enabled"] = (
                is_cloud_trail_event_history_enabled
            )
        if cross_account_configurations is not None:
            input_["cross_account_configurations"] = cross_account_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified investigation group from your account. You can currently have one investigation group per Region in your account. After you delete an investigation group, you can later create a new investigation group in the same Region.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to delete.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_aiops.types.delete_investigation_group_request.DeleteInvestigationGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_aiops._operations.ai_ops.delete_investigation_group

            output, http_response = (
                capo_aiops._operations.ai_ops.delete_investigation_group.delete_investigation_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.delete_investigation_group_request.DeleteInvestigationGroupRequest = {
            "identifier": identifier
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
        config_overrides: Optional[AIOpsClientConfig] = None,
        next_token: Optional[
            "capo_aiops.types.sensitive_string_with_length_limits.SensitiveStringWithLengthLimits"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_aiops.types.list_investigation_groups_output.ListInvestigationGroupsOutput":
        """<p>Returns the ARN and name of each investigation group in the account.</p>

        Args:
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service operations.</p>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_aiops.types.list_investigation_groups_input.ListInvestigationGroupsInput]",
        ) -> OperationResponse[
            "capo_aiops.types.list_investigation_groups_output.ListInvestigationGroupsOutput"
        ]:
            import capo_aiops._operations.ai_ops.list_investigation_groups

            output, http_response = (
                capo_aiops._operations.ai_ops.list_investigation_groups.list_investigation_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.list_investigation_groups_input.ListInvestigationGroupsInput = {}
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


class AsyncInvestigationGroup:
    def __init__(self, service: AsyncAIOpsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_aiops.types.string_with_pattern_and_length_limits.StringWithPatternAndLengthLimits",
        role_arn: "capo_aiops.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
        encryption_configuration: Optional[
            "capo_aiops.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        retention_in_days: Optional["capo_aiops.types.retention.Retention"] = None,
        tags: Optional["capo_aiops.types.tags.Tags"] = None,
        tag_key_boundaries: Optional[
            "capo_aiops.types.tag_key_boundaries.TagKeyBoundaries"
        ] = None,
        chatbot_notification_channel: Optional[
            "capo_aiops.types.chatbot_notification_channel.ChatbotNotificationChannel"
        ] = None,
        is_cloud_trail_event_history_enabled: Optional[bool] = None,
        cross_account_configurations: Optional[
            "capo_aiops.types.cross_account_configurations.CrossAccountConfigurations"
        ] = None,
    ) -> "capo_aiops.types.create_investigation_group_output.CreateInvestigationGroupOutput":
        """<p>Creates an <i>investigation group</i> in your account. Creating an investigation group is a one-time setup task for each Region in your account. It is a necessary task to be able to perform investigations.</p> <p>Settings in the investigation group help you centrally manage the common properties of your investigations, such as the following:</p> <ul> <li> <p>Who can access the investigations</p> </li> <li> <p>Whether investigation data is encrypted with a customer managed Key Management Service key.</p> </li> <li> <p>How long investigations and their data are retained by default.</p> </li> </ul> <p>Currently, you can have one investigation group in each Region in your account. Each investigation in a Region is a part of the investigation group in that Region</p> <p>To create an investigation group and set up CloudWatch investigations, you must be signed in to an IAM principal that has either the <code>AIOpsConsoleAdminPolicy</code> or the <code>AdministratorAccess</code> IAM policy attached, or to an account that has similar permissions.</p> <important> <p>You can configure CloudWatch alarms to start investigations and add events to investigations. If you create your investigation group with <code>CreateInvestigationGroup</code> and you want to enable alarms to do this, you must use <code>PutInvestigationGroupPolicy</code> to create a resource policy that grants this permission to CloudWatch alarms. </p> <p>For more information about configuring CloudWatch alarms, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html">Using Amazon CloudWatch alarms</a> </p> </important>

        Args:
            name: <p>Provides a name for the investigation group.</p>
            role_arn: <p>Specify the ARN of the IAM role that CloudWatch investigations will use when it gathers investigation data. The permissions in this role determine which of your resources that CloudWatch investigations will have access to during investigations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-Security-Data">How to control what data CloudWatch investigations has access to during investigations</a>.</p>
            encryption_configuration: <p>Use this structure if you want to use a customer managed KMS key to encrypt your investigation data. If you omit this parameter, CloudWatch investigations will use an Amazon Web Services key to encrypt the data. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-KMS">Encryption of investigation data</a>.</p>
            retention_in_days: <p>Specify how long that investigation data is kept. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Retention.html">Operational investigation data retention</a>. </p> <p>If you omit this parameter, the default of 90 days is used.</p>
            tags: <p>A list of key-value pairs to associate with the investigation group. You can associate as many as 50 tags with an investigation group. To be able to associate tags when you create the investigation group, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p>
            tag_key_boundaries: <p>Enter the existing custom tag keys for custom applications in your system. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources. For example, to discover that an Amazon ECS service depends on an Amazon RDS database, CloudWatch investigations can discover this relationship using data sources such as X-Ray and CloudWatch Application Signals. However, if you haven't deployed these features, CloudWatch investigations will attempt to identify possible relationships. Tag boundaries can be used to narrow the resources that will be discovered by CloudWatch investigations in these cases.</p> <p>You don't need to enter tags created by myApplications or CloudFormation, because CloudWatch investigations can automatically detect those tags.</p>
            chatbot_notification_channel: <p>Use this structure to integrate CloudWatch investigations with chat applications. This structure is a string array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html">Getting started with Amazon Q in chat applications</a> and <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies">Resource type defined by Amazon Web Services Chatbot</a>.</p>
            is_cloud_trail_event_history_enabled: <p>Specify <code>true</code> to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is <code>true</code>.</p>
            cross_account_configurations: <p>List of <code>sourceRoleArn</code> values that have been configured for cross-account access.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_aiops.types.create_investigation_group_input.CreateInvestigationGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_aiops.types.create_investigation_group_output.CreateInvestigationGroupOutput"
        ]:
            import capo_aiops._operations.ai_ops.create_investigation_group

            (
                output,
                http_response,
            ) = await capo_aiops._operations.ai_ops.create_investigation_group.async_create_investigation_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.create_investigation_group_input.CreateInvestigationGroupInput = {
            "name": name,
            "role_arn": role_arn,
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if retention_in_days is not None:
            input_["retention_in_days"] = retention_in_days
        if tags is not None:
            input_["tags"] = tags
        if tag_key_boundaries is not None:
            input_["tag_key_boundaries"] = tag_key_boundaries
        if chatbot_notification_channel is not None:
            input_["chatbot_notification_channel"] = chatbot_notification_channel
        if is_cloud_trail_event_history_enabled is not None:
            input_["is_cloud_trail_event_history_enabled"] = (
                is_cloud_trail_event_history_enabled
            )
        if cross_account_configurations is not None:
            input_["cross_account_configurations"] = cross_account_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
    ) -> "capo_aiops.types.get_investigation_group_response.GetInvestigationGroupResponse":
        """<p>Returns the configuration information for the specified investigation group.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to view. This is used to set the name of the investigation group.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_aiops.types.get_investigation_group_request.GetInvestigationGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_aiops.types.get_investigation_group_response.GetInvestigationGroupResponse"
        ]:
            import capo_aiops._operations.ai_ops.get_investigation_group

            (
                output,
                http_response,
            ) = await capo_aiops._operations.ai_ops.get_investigation_group.async_get_investigation_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.get_investigation_group_request.GetInvestigationGroupRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
        role_arn: Optional["capo_aiops.types.role_arn.RoleArn"] = None,
        encryption_configuration: Optional[
            "capo_aiops.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tag_key_boundaries: Optional[
            "capo_aiops.types.tag_key_boundaries.TagKeyBoundaries"
        ] = None,
        chatbot_notification_channel: Optional[
            "capo_aiops.types.chatbot_notification_channel.ChatbotNotificationChannel"
        ] = None,
        is_cloud_trail_event_history_enabled: Optional[bool] = None,
        cross_account_configurations: Optional[
            "capo_aiops.types.cross_account_configurations.CrossAccountConfigurations"
        ] = None,
    ) -> "capo_aiops.types.update_investigation_group_output.UpdateInvestigationGroupOutput":
        """<p>Updates the configuration of the specified investigation group.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to modify.</p>
            role_arn: <p>Specify this field if you want to change the IAM role that CloudWatch investigations will use when it gathers investigation data. To do so, specify the ARN of the new role.</p> <p>The permissions in this role determine which of your resources that CloudWatch investigations will have access to during investigations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-Security-Data">How to control what data CloudWatch investigations has access to during investigations</a>.</p>
            encryption_configuration: <p>Use this structure if you want to use a customer managed KMS key to encrypt your investigation data. If you omit this parameter, CloudWatch investigations will use an Amazon Web Services key to encrypt the data. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-KMS">Encryption of investigation data</a>.</p>
            tag_key_boundaries: <p>Enter the existing custom tag keys for custom applications in your system. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources. For example, to discover that an Amazon ECS service depends on an Amazon RDS database, CloudWatch investigations can discover this relationship using data sources such as X-Ray and CloudWatch Application Signals. However, if you haven't deployed these features, CloudWatch investigations will attempt to identify possible relationships. Tag boundaries can be used to narrow the resources that will be discovered by CloudWatch investigations in these cases.</p> <p>You don't need to enter tags created by myApplications or CloudFormation, because CloudWatch investigations can automatically detect those tags.</p>
            chatbot_notification_channel: <p>Use this structure to integrate CloudWatch investigations with chat applications. This structure is a string array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html">Getting started with Amazon Q in chat applications</a> and <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies">Resource type defined by Amazon Web Services Chatbot</a>.</p>
            is_cloud_trail_event_history_enabled: <p>Specify <code>true</code> to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is <code>true</code>.</p>
            cross_account_configurations: <p>Used to configure cross-account access for an investigation group. It allows the investigation group to access resources in other accounts. </p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_aiops.types.update_investigation_group_request.UpdateInvestigationGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_aiops.types.update_investigation_group_output.UpdateInvestigationGroupOutput"
        ]:
            import capo_aiops._operations.ai_ops.update_investigation_group

            (
                output,
                http_response,
            ) = await capo_aiops._operations.ai_ops.update_investigation_group.async_update_investigation_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.update_investigation_group_request.UpdateInvestigationGroupRequest = {
            "identifier": identifier
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tag_key_boundaries is not None:
            input_["tag_key_boundaries"] = tag_key_boundaries
        if chatbot_notification_channel is not None:
            input_["chatbot_notification_channel"] = chatbot_notification_channel
        if is_cloud_trail_event_history_enabled is not None:
            input_["is_cloud_trail_event_history_enabled"] = (
                is_cloud_trail_event_history_enabled
            )
        if cross_account_configurations is not None:
            input_["cross_account_configurations"] = cross_account_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified investigation group from your account. You can currently have one investigation group per Region in your account. After you delete an investigation group, you can later create a new investigation group in the same Region.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to delete.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_aiops.types.delete_investigation_group_request.DeleteInvestigationGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_aiops._operations.ai_ops.delete_investigation_group

            (
                output,
                http_response,
            ) = await capo_aiops._operations.ai_ops.delete_investigation_group.async_delete_investigation_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.delete_investigation_group_request.DeleteInvestigationGroupRequest = {
            "identifier": identifier
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
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
        next_token: Optional[
            "capo_aiops.types.sensitive_string_with_length_limits.SensitiveStringWithLengthLimits"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_aiops.types.list_investigation_groups_output.ListInvestigationGroupsOutput":
        """<p>Returns the ARN and name of each investigation group in the account.</p>

        Args:
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service operations.</p>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_aiops.types.list_investigation_groups_input.ListInvestigationGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_aiops.types.list_investigation_groups_output.ListInvestigationGroupsOutput"
        ]:
            import capo_aiops._operations.ai_ops.list_investigation_groups

            (
                output,
                http_response,
            ) = await capo_aiops._operations.ai_ops.list_investigation_groups.async_list_investigation_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.list_investigation_groups_input.ListInvestigationGroupsInput = {}
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
