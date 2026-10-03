"""Generated from Smithy shape ``com.amazonaws.aiops#AIOps``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_aiops._auth._signers
import capo_aiops._auth._sigv4
from capo_aiops._auth._identity import Credentials
from capo_aiops._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_aiops._auth._zapros_handler import AuthMiddleware
from capo_aiops._pagination import resolve_path as _resolve_path
from capo_aiops._resources.ai_ops.investigation_group import InvestigationGroup
from capo_aiops._resources.ai_ops.investigation_group_policy import (
    InvestigationGroupPolicy,
)
from capo_aiops._services._aws_config import aws_config
from capo_aiops._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_aiops.types.chatbot_notification_channel
    import capo_aiops.types.create_investigation_group_input
    import capo_aiops.types.create_investigation_group_output
    import capo_aiops.types.cross_account_configurations
    import capo_aiops.types.delete_investigation_group_policy_output
    import capo_aiops.types.delete_investigation_group_policy_request
    import capo_aiops.types.delete_investigation_group_request
    import capo_aiops.types.encryption_configuration
    import capo_aiops.types.get_investigation_group_policy_request
    import capo_aiops.types.get_investigation_group_policy_response
    import capo_aiops.types.get_investigation_group_request
    import capo_aiops.types.get_investigation_group_response
    import capo_aiops.types.investigation_group_identifier
    import capo_aiops.types.investigation_group_policy_document
    import capo_aiops.types.list_investigation_groups_input
    import capo_aiops.types.list_investigation_groups_model
    import capo_aiops.types.list_investigation_groups_output
    import capo_aiops.types.list_tags_for_resource_output
    import capo_aiops.types.list_tags_for_resource_request
    import capo_aiops.types.put_investigation_group_policy_request
    import capo_aiops.types.put_investigation_group_policy_response
    import capo_aiops.types.retention
    import capo_aiops.types.role_arn
    import capo_aiops.types.sensitive_string_with_length_limits
    import capo_aiops.types.string_with_pattern_and_length_limits
    import capo_aiops.types.tag_key_boundaries
    import capo_aiops.types.tag_keys
    import capo_aiops.types.tag_resource_request
    import capo_aiops.types.tag_resource_response
    import capo_aiops.types.tags
    import capo_aiops.types.untag_resource_request
    import capo_aiops.types.untag_resource_response
    import capo_aiops.types.update_investigation_group_output
    import capo_aiops.types.update_investigation_group_request


class AIOpsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AIOpsClient:
    """A client for the ``AIOps`` service.

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
        self._config = AIOpsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.investigation_group = InvestigationGroup(self)
        self.investigation_group_policy = InvestigationGroupPolicy(self)

    def operation_options(
        self, config_overrides: Optional[AIOpsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AIOpsClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self, resource_arn: str, *, config_overrides: Optional[AIOpsClientConfig] = None
    ) -> "capo_aiops.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Displays the tags associated with a CloudWatch investigations resource. Currently, investigation groups support tagging.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch investigations resource that you want to view tags for. You can use the <code>ListInvestigationGroups</code> operation to find the ARNs of investigation groups.</p> <p>The ARN format for an investigation group is <code>arn:aws:aiops:<i>Region</i>:<i>account-id</i>:investigation-group:<i>investigation-group-id</i> </code>.</p>

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
            req: "OperationRequest[capo_aiops.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_aiops._operations.ai_ops.list_tags_for_resource

            output, http_response = (
                capo_aiops._operations.ai_ops.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_aiops.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: str,
        tags: "capo_aiops.types.tags.Tags",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "capo_aiops.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can associate as many as 50 tags with a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to apply the tags to. You can use the <code>ListInvestigationGroups</code> operation to find the ARNs of investigation groups.</p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>

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
            req: "OperationRequest[capo_aiops.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_aiops._operations.ai_ops.tag_resource

            output, http_response = (
                capo_aiops._operations.ai_ops.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_aiops.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: str,
        tag_keys: "capo_aiops.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "capo_aiops.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove the tags from. You can use the<code>ListInvestigationGroups</code> operation to find the ARNs of investigation groups.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

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
            req: "OperationRequest[capo_aiops.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_aiops._operations.ai_ops.untag_resource

            output, http_response = (
                capo_aiops._operations.ai_ops.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_aiops.types.untag_resource_request.UntagResourceRequest = {
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

    def create_investigation_group(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def get_investigation_group(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def update_investigation_group(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_investigation_group(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_investigation_groups(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_investigation_groups(
        self,
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
        next_token: Optional[
            "capo_aiops.types.sensitive_string_with_length_limits.SensitiveStringWithLengthLimits"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_aiops.types.list_investigation_groups_model.ListInvestigationGroupsModel]":
        _token = next_token
        while True:
            _response = self.list_investigation_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("investigation_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_investigation_group_policy(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        policy: "capo_aiops.types.investigation_group_policy_document.InvestigationGroupPolicyDocument",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "capo_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse":
        """<p>Creates an IAM resource policy and assigns it to the specified investigation group.</p> <p>If you create your investigation group with <code>CreateInvestigationGroup</code> and you want to enable CloudWatch alarms to create investigations and add events to investigations, you must use this operation to create a policy similar to this example.</p> <p> <code> { "Version": "2008-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "aiops.alarms.cloudwatch.amazonaws.com" }, "Action": [ "aiops:CreateInvestigation", "aiops:CreateInvestigationEvent" ], "Resource": "*", "Condition": { "StringEquals": { "aws:SourceAccount": "account-id" }, "ArnLike": { "aws:SourceArn": "arn:aws:cloudwatch:region:account-id:alarm:*" } } } ] } </code> </p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to assign the policy to.</p>
            policy: <p>The policy, in JSON format.</p>

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
            req: "OperationRequest[capo_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse"
        ]:
            import capo_aiops._operations.ai_ops.put_investigation_group_policy

            output, http_response = (
                capo_aiops._operations.ai_ops.put_investigation_group_policy.put_investigation_group_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest = {
            "identifier": identifier,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_investigation_group_policy(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "capo_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse":
        r"""<p>Returns the JSON of the IAM resource policy associated with the specified investigation group in a string. For example, <code>{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"aiops.alarms.cloudwatch.amazonaws.com\"},\"Action\":[\"aiops:CreateInvestigation\",\"aiops:CreateInvestigationEvent\"],\"Resource\":\"*\",\"Condition\":{\"StringEquals\":{\"aws:SourceAccount\":\"111122223333\"},\"ArnLike\":{\"aws:SourceArn\":\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\"}}}]}</code>.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to view the policy of.</p>

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
            req: "OperationRequest[capo_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse"
        ]:
            import capo_aiops._operations.ai_ops.get_investigation_group_policy

            output, http_response = (
                capo_aiops._operations.ai_ops.get_investigation_group_policy.get_investigation_group_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_investigation_group_policy(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "capo_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput":
        """<p>Removes the IAM resource policy from being associated with the investigation group that you specify.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to remove the policy from.</p>

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
            req: "OperationRequest[capo_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput"
        ]:
            import capo_aiops._operations.ai_ops.delete_investigation_group_policy

            output, http_response = (
                capo_aiops._operations.ai_ops.delete_investigation_group_policy.delete_investigation_group_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest = {
            "identifier": identifier
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
