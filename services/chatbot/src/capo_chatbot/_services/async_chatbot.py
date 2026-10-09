"""Generated from Smithy shape ``com.amazonaws.chatbot#WheatleyOrchestration_20171011``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_chatbot._auth._signers
import capo_chatbot._auth._sigv4
from capo_chatbot._auth._identity import Credentials
from capo_chatbot._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_chatbot._auth._zapros_handler import AuthMiddleware
from capo_chatbot._pagination import resolve_path as _resolve_path
from capo_chatbot._resources.wheatley_orchestration_20171011.custom_action_resource import (
    AsyncCustomActionResource,
)
from capo_chatbot._services._aws_config import aaws_config
from capo_chatbot._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_chatbot.types.amazon_resource_name
    import capo_chatbot.types.arn
    import capo_chatbot.types.associate_to_configuration_request
    import capo_chatbot.types.associate_to_configuration_result
    import capo_chatbot.types.association_listing
    import capo_chatbot.types.boolean_account_preference
    import capo_chatbot.types.chat_configuration_arn
    import capo_chatbot.types.chime_webhook_configuration
    import capo_chatbot.types.chime_webhook_description
    import capo_chatbot.types.chime_webhook_url
    import capo_chatbot.types.client_token
    import capo_chatbot.types.configuration_name
    import capo_chatbot.types.configured_team
    import capo_chatbot.types.create_chime_webhook_configuration_request
    import capo_chatbot.types.create_chime_webhook_configuration_result
    import capo_chatbot.types.create_custom_action_request
    import capo_chatbot.types.create_custom_action_result
    import capo_chatbot.types.create_slack_channel_configuration_request
    import capo_chatbot.types.create_slack_channel_configuration_result
    import capo_chatbot.types.create_teams_channel_configuration_request
    import capo_chatbot.types.create_teams_channel_configuration_result
    import capo_chatbot.types.custom_action_alias_name
    import capo_chatbot.types.custom_action_arn
    import capo_chatbot.types.custom_action_attachment_list
    import capo_chatbot.types.custom_action_definition
    import capo_chatbot.types.custom_action_name
    import capo_chatbot.types.customer_cw_log_level
    import capo_chatbot.types.delete_chime_webhook_configuration_request
    import capo_chatbot.types.delete_chime_webhook_configuration_result
    import capo_chatbot.types.delete_custom_action_request
    import capo_chatbot.types.delete_custom_action_result
    import capo_chatbot.types.delete_microsoft_teams_user_identity_request
    import capo_chatbot.types.delete_microsoft_teams_user_identity_result
    import capo_chatbot.types.delete_slack_channel_configuration_request
    import capo_chatbot.types.delete_slack_channel_configuration_result
    import capo_chatbot.types.delete_slack_user_identity_request
    import capo_chatbot.types.delete_slack_user_identity_result
    import capo_chatbot.types.delete_slack_workspace_authorization_request
    import capo_chatbot.types.delete_slack_workspace_authorization_result
    import capo_chatbot.types.delete_teams_channel_configuration_request
    import capo_chatbot.types.delete_teams_channel_configuration_result
    import capo_chatbot.types.delete_teams_configured_team_request
    import capo_chatbot.types.delete_teams_configured_team_result
    import capo_chatbot.types.describe_chime_webhook_configurations_request
    import capo_chatbot.types.describe_chime_webhook_configurations_result
    import capo_chatbot.types.describe_slack_channel_configurations_request
    import capo_chatbot.types.describe_slack_channel_configurations_result
    import capo_chatbot.types.describe_slack_user_identities_request
    import capo_chatbot.types.describe_slack_user_identities_result
    import capo_chatbot.types.describe_slack_workspaces_request
    import capo_chatbot.types.describe_slack_workspaces_result
    import capo_chatbot.types.disassociate_from_configuration_request
    import capo_chatbot.types.disassociate_from_configuration_result
    import capo_chatbot.types.get_account_preferences_request
    import capo_chatbot.types.get_account_preferences_result
    import capo_chatbot.types.get_custom_action_request
    import capo_chatbot.types.get_custom_action_result
    import capo_chatbot.types.get_teams_channel_configuration_request
    import capo_chatbot.types.get_teams_channel_configuration_result
    import capo_chatbot.types.guardrail_policy_arn_list
    import capo_chatbot.types.list_associations_request
    import capo_chatbot.types.list_associations_result
    import capo_chatbot.types.list_custom_actions_request
    import capo_chatbot.types.list_custom_actions_result
    import capo_chatbot.types.list_microsoft_teams_configured_teams_request
    import capo_chatbot.types.list_microsoft_teams_configured_teams_result
    import capo_chatbot.types.list_microsoft_teams_user_identities_request
    import capo_chatbot.types.list_microsoft_teams_user_identities_result
    import capo_chatbot.types.list_tags_for_resource_request
    import capo_chatbot.types.list_tags_for_resource_response
    import capo_chatbot.types.list_teams_channel_configurations_request
    import capo_chatbot.types.list_teams_channel_configurations_result
    import capo_chatbot.types.max_results
    import capo_chatbot.types.pagination_token
    import capo_chatbot.types.resource_identifier
    import capo_chatbot.types.slack_channel_configuration
    import capo_chatbot.types.slack_channel_display_name
    import capo_chatbot.types.slack_channel_id
    import capo_chatbot.types.slack_team_id
    import capo_chatbot.types.slack_user_id
    import capo_chatbot.types.slack_user_identity
    import capo_chatbot.types.slack_workspace
    import capo_chatbot.types.sns_topic_arn_list
    import capo_chatbot.types.string
    import capo_chatbot.types.tag_key_list
    import capo_chatbot.types.tag_list
    import capo_chatbot.types.tag_resource_request
    import capo_chatbot.types.tag_resource_response
    import capo_chatbot.types.tags
    import capo_chatbot.types.team_name
    import capo_chatbot.types.teams_channel_configuration
    import capo_chatbot.types.teams_channel_id
    import capo_chatbot.types.teams_channel_name
    import capo_chatbot.types.teams_user_identity
    import capo_chatbot.types.untag_resource_request
    import capo_chatbot.types.untag_resource_response
    import capo_chatbot.types.update_account_preferences_request
    import capo_chatbot.types.update_account_preferences_result
    import capo_chatbot.types.update_chime_webhook_configuration_request
    import capo_chatbot.types.update_chime_webhook_configuration_result
    import capo_chatbot.types.update_custom_action_request
    import capo_chatbot.types.update_custom_action_result
    import capo_chatbot.types.update_slack_channel_configuration_request
    import capo_chatbot.types.update_slack_channel_configuration_result
    import capo_chatbot.types.update_teams_channel_configuration_request
    import capo_chatbot.types.update_teams_channel_configuration_result
    import capo_chatbot.types.uuid


class AsyncchatbotClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncchatbotClient:
    """A client for the ``chatbot`` service.

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
        self._config = AsyncchatbotClientConfig(
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
        self.custom_action_resource = AsyncCustomActionResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncchatbotClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncchatbotClientConfig = config_overrides or {}
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

    async def associate_to_configuration(
        self,
        resource: "capo_chatbot.types.resource_identifier.ResourceIdentifier",
        chat_configuration: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.associate_to_configuration_result.AssociateToConfigurationResult":
        """<p>Links a resource (for example, a custom action) to a channel configuration.</p>

        Args:
            resource: <p>The resource Amazon Resource Name (ARN) to link.</p>
            chat_configuration: <p>The channel configuration to associate with the resource.</p>

        Raises:
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Associate a custom action to a configuration
            Associate a custom action to a channel configuration, allowing it to be used in that channel

            >>> await client.associate_to_configuration(resource='arn:aws:chatbot::1234567890:custom-action/my-custom-action', chat_configuration='arn:aws:chatbot::1234567890:chat-configuration/slack-channel/my-channel')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.associate_to_configuration_request.AssociateToConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.associate_to_configuration_result.AssociateToConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.associate_to_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.associate_to_configuration.async_associate_to_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.associate_to_configuration_request.AssociateToConfigurationRequest = {
            "resource": resource,
            "chat_configuration": chat_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_chime_webhook_configuration(
        self,
        webhook_description: "capo_chatbot.types.chime_webhook_description.ChimeWebhookDescription",
        webhook_url: "capo_chatbot.types.chime_webhook_url.ChimeWebhookUrl",
        sns_topic_arns: "capo_chatbot.types.sns_topic_arn_list.SnsTopicArnList",
        iam_role_arn: "capo_chatbot.types.arn.Arn",
        configuration_name: "capo_chatbot.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        logging_level: Optional[
            "capo_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        tags: Optional["capo_chatbot.types.tags.Tags"] = None,
    ) -> "capo_chatbot.types.create_chime_webhook_configuration_result.CreateChimeWebhookConfigurationResult":
        """<p>Creates an AWS Chatbot configuration for Amazon Chime.</p>

        Args:
            webhook_description: <p>A description of the webhook. We recommend using the convention <code>RoomName/WebhookName</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html">Tutorial: Get started with Amazon Chime</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            webhook_url: <p>The URL for the Amazon Chime webhook.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            configuration_name: <p>The name of the configuration.</p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>

        Raises:
            capo_chatbot.errors.conflict_exception.ConflictException: <p>There was an issue processing your request.</p>
            capo_chatbot.errors.create_chime_webhook_configuration_exception.CreateChimeWebhookConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.create_chime_webhook_configuration_request.CreateChimeWebhookConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.create_chime_webhook_configuration_result.CreateChimeWebhookConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.create_chime_webhook_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.create_chime_webhook_configuration.async_create_chime_webhook_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.create_chime_webhook_configuration_request.CreateChimeWebhookConfigurationRequest = {
            "webhook_description": webhook_description,
            "webhook_url": webhook_url,
            "sns_topic_arns": sns_topic_arns,
            "iam_role_arn": iam_role_arn,
            "configuration_name": configuration_name,
        }
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_microsoft_teams_channel_configuration(
        self,
        channel_id: "capo_chatbot.types.teams_channel_id.TeamsChannelId",
        team_id: "capo_chatbot.types.uuid.UUID",
        tenant_id: "capo_chatbot.types.uuid.UUID",
        iam_role_arn: "capo_chatbot.types.arn.Arn",
        configuration_name: "capo_chatbot.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        channel_name: Optional[
            "capo_chatbot.types.teams_channel_name.TeamsChannelName"
        ] = None,
        team_name: Optional["capo_chatbot.types.team_name.TeamName"] = None,
        sns_topic_arns: Optional[
            "capo_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        logging_level: Optional[
            "capo_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        guardrail_policy_arns: Optional[
            "capo_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
        ] = None,
        user_authorization_required: Optional[
            "capo_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
        tags: Optional["capo_chatbot.types.tags.Tags"] = None,
    ) -> "capo_chatbot.types.create_teams_channel_configuration_result.CreateTeamsChannelConfigurationResult":
        """<p>Creates an AWS Chatbot configuration for Microsoft Teams.</p>

        Args:
            channel_id: <p>The ID of the Microsoft Teams channel.</p>
            channel_name: <p>The name of the Microsoft Teams channel.</p>
            team_id: <p> The ID of the Microsoft Teams authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            team_name: <p>The name of the Microsoft Teams Team.</p>
            tenant_id: <p>The ID of the Microsoft Teams tenant.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            configuration_name: <p>The name of the configuration.</p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            guardrail_policy_arns: <p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>

        Raises:
            capo_chatbot.errors.conflict_exception.ConflictException: <p>There was an issue processing your request.</p>
            capo_chatbot.errors.create_teams_channel_configuration_exception.CreateTeamsChannelConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.create_teams_channel_configuration_request.CreateTeamsChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.create_teams_channel_configuration_result.CreateTeamsChannelConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.create_microsoft_teams_channel_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.create_microsoft_teams_channel_configuration.async_create_microsoft_teams_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.create_teams_channel_configuration_request.CreateTeamsChannelConfigurationRequest = {
            "channel_id": channel_id,
            "team_id": team_id,
            "tenant_id": tenant_id,
            "iam_role_arn": iam_role_arn,
            "configuration_name": configuration_name,
        }
        if channel_name is not None:
            input_["channel_name"] = channel_name
        if team_name is not None:
            input_["team_name"] = team_name
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if guardrail_policy_arns is not None:
            input_["guardrail_policy_arns"] = guardrail_policy_arns
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_slack_channel_configuration(
        self,
        slack_team_id: "capo_chatbot.types.slack_team_id.SlackTeamId",
        slack_channel_id: "capo_chatbot.types.slack_channel_id.SlackChannelId",
        iam_role_arn: "capo_chatbot.types.arn.Arn",
        configuration_name: "capo_chatbot.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        slack_channel_name: Optional[
            "capo_chatbot.types.slack_channel_display_name.SlackChannelDisplayName"
        ] = None,
        sns_topic_arns: Optional[
            "capo_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        logging_level: Optional[
            "capo_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        guardrail_policy_arns: Optional[
            "capo_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
        ] = None,
        user_authorization_required: Optional[
            "capo_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
        tags: Optional["capo_chatbot.types.tags.Tags"] = None,
    ) -> "capo_chatbot.types.create_slack_channel_configuration_result.CreateSlackChannelConfigurationResult":
        """<p>Creates an AWS Chatbot confugration for Slack.</p>

        Args:
            slack_team_id: <p>The ID of the Slack workspace authorized with AWS Chatbot.</p>
            slack_channel_id: <p>The ID of the Slack channel.</p> <p>To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ. </p>
            slack_channel_name: <p>The name of the Slack channel.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            configuration_name: <p>The name of the configuration.</p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            guardrail_policy_arns: <p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>

        Raises:
            capo_chatbot.errors.conflict_exception.ConflictException: <p>There was an issue processing your request.</p>
            capo_chatbot.errors.create_slack_channel_configuration_exception.CreateSlackChannelConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.create_slack_channel_configuration_request.CreateSlackChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.create_slack_channel_configuration_result.CreateSlackChannelConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.create_slack_channel_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.create_slack_channel_configuration.async_create_slack_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.create_slack_channel_configuration_request.CreateSlackChannelConfigurationRequest = {
            "slack_team_id": slack_team_id,
            "slack_channel_id": slack_channel_id,
            "iam_role_arn": iam_role_arn,
            "configuration_name": configuration_name,
        }
        if slack_channel_name is not None:
            input_["slack_channel_name"] = slack_channel_name
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if guardrail_policy_arns is not None:
            input_["guardrail_policy_arns"] = guardrail_policy_arns
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_chime_webhook_configuration(
        self,
        chat_configuration_arn: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.delete_chime_webhook_configuration_result.DeleteChimeWebhookConfigurationResult":
        """<p>Deletes a Amazon Chime webhook configuration for AWS Chatbot.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the ChimeWebhookConfiguration to delete.</p>

        Raises:
            capo_chatbot.errors.delete_chime_webhook_configuration_exception.DeleteChimeWebhookConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.delete_chime_webhook_configuration_request.DeleteChimeWebhookConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.delete_chime_webhook_configuration_result.DeleteChimeWebhookConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.delete_chime_webhook_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.delete_chime_webhook_configuration.async_delete_chime_webhook_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.delete_chime_webhook_configuration_request.DeleteChimeWebhookConfigurationRequest = {
            "chat_configuration_arn": chat_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_microsoft_teams_channel_configuration(
        self,
        chat_configuration_arn: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.delete_teams_channel_configuration_result.DeleteTeamsChannelConfigurationResult":
        """<p>Deletes a Microsoft Teams channel configuration for AWS Chatbot</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>

        Raises:
            capo_chatbot.errors.delete_teams_channel_configuration_exception.DeleteTeamsChannelConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.delete_teams_channel_configuration_request.DeleteTeamsChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.delete_teams_channel_configuration_result.DeleteTeamsChannelConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_channel_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_channel_configuration.async_delete_microsoft_teams_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.delete_teams_channel_configuration_request.DeleteTeamsChannelConfigurationRequest = {
            "chat_configuration_arn": chat_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_microsoft_teams_configured_team(
        self,
        team_id: "capo_chatbot.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.delete_teams_configured_team_result.DeleteTeamsConfiguredTeamResult":
        """<p>Deletes the Microsoft Teams team authorization allowing for channels to be configured in that Microsoft Teams team. Note that the Microsoft Teams team must have no channels configured to remove it. </p>

        Args:
            team_id: <p>The ID of the Microsoft Teams team authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>

        Raises:
            capo_chatbot.errors.delete_teams_configured_team_exception.DeleteTeamsConfiguredTeamException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.delete_teams_configured_team_request.DeleteTeamsConfiguredTeamRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.delete_teams_configured_team_result.DeleteTeamsConfiguredTeamResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_configured_team

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_configured_team.async_delete_microsoft_teams_configured_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.delete_teams_configured_team_request.DeleteTeamsConfiguredTeamRequest = {
            "team_id": team_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_microsoft_teams_user_identity(
        self,
        chat_configuration_arn: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        user_id: "capo_chatbot.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.delete_microsoft_teams_user_identity_result.DeleteMicrosoftTeamsUserIdentityResult":
        """<p>Identifes a user level permission for a channel configuration.</p>

        Args:
            chat_configuration_arn: <p>The ARN of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>
            user_id: <p>The Microsoft Teams user ID.</p>

        Raises:
            capo_chatbot.errors.delete_microsoft_teams_user_identity_exception.DeleteMicrosoftTeamsUserIdentityException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.delete_microsoft_teams_user_identity_request.DeleteMicrosoftTeamsUserIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.delete_microsoft_teams_user_identity_result.DeleteMicrosoftTeamsUserIdentityResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_user_identity

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_user_identity.async_delete_microsoft_teams_user_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.delete_microsoft_teams_user_identity_request.DeleteMicrosoftTeamsUserIdentityRequest = {
            "chat_configuration_arn": chat_configuration_arn,
            "user_id": user_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_slack_channel_configuration(
        self,
        chat_configuration_arn: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.delete_slack_channel_configuration_result.DeleteSlackChannelConfigurationResult":
        """<p>Deletes a Slack channel configuration for AWS Chatbot</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the SlackChannelConfiguration to delete.</p>

        Raises:
            capo_chatbot.errors.delete_slack_channel_configuration_exception.DeleteSlackChannelConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.delete_slack_channel_configuration_request.DeleteSlackChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.delete_slack_channel_configuration_result.DeleteSlackChannelConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.delete_slack_channel_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.delete_slack_channel_configuration.async_delete_slack_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.delete_slack_channel_configuration_request.DeleteSlackChannelConfigurationRequest = {
            "chat_configuration_arn": chat_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_slack_user_identity(
        self,
        chat_configuration_arn: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        slack_team_id: "capo_chatbot.types.slack_team_id.SlackTeamId",
        slack_user_id: "capo_chatbot.types.slack_user_id.SlackUserId",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.delete_slack_user_identity_result.DeleteSlackUserIdentityResult":
        """<p>Deletes a user level permission for a Slack channel configuration.</p>

        Args:
            chat_configuration_arn: <p>The ARN of the SlackChannelConfiguration associated with the user identity to delete.</p>
            slack_team_id: <p>The ID of the Slack workspace authorized with AWS Chatbot.</p>
            slack_user_id: <p>The ID of the user in Slack</p>

        Raises:
            capo_chatbot.errors.delete_slack_user_identity_exception.DeleteSlackUserIdentityException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.delete_slack_user_identity_request.DeleteSlackUserIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.delete_slack_user_identity_result.DeleteSlackUserIdentityResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.delete_slack_user_identity

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.delete_slack_user_identity.async_delete_slack_user_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.delete_slack_user_identity_request.DeleteSlackUserIdentityRequest = {
            "chat_configuration_arn": chat_configuration_arn,
            "slack_team_id": slack_team_id,
            "slack_user_id": slack_user_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_slack_workspace_authorization(
        self,
        slack_team_id: "capo_chatbot.types.slack_team_id.SlackTeamId",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.delete_slack_workspace_authorization_result.DeleteSlackWorkspaceAuthorizationResult":
        """<p>Deletes the Slack workspace authorization that allows channels to be configured in that workspace. This requires all configured channels in the workspace to be deleted. </p>

        Args:
            slack_team_id: <p>The ID of the Slack workspace authorized with AWS Chatbot.</p>

        Raises:
            capo_chatbot.errors.delete_slack_workspace_authorization_fault.DeleteSlackWorkspaceAuthorizationFault: <p>There was an issue deleting your Slack workspace.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.delete_slack_workspace_authorization_request.DeleteSlackWorkspaceAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.delete_slack_workspace_authorization_result.DeleteSlackWorkspaceAuthorizationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.delete_slack_workspace_authorization

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.delete_slack_workspace_authorization.async_delete_slack_workspace_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.delete_slack_workspace_authorization_request.DeleteSlackWorkspaceAuthorizationRequest = {
            "slack_team_id": slack_team_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_chime_webhook_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        chat_configuration_arn: Optional[
            "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
    ) -> "capo_chatbot.types.describe_chime_webhook_configurations_result.DescribeChimeWebhookConfigurationsResult":
        """<p>Lists Amazon Chime webhook configurations optionally filtered by ChatConfigurationArn</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>
            chat_configuration_arn: <p>An optional Amazon Resource Name (ARN) of a ChimeWebhookConfiguration to describe.</p>

        Raises:
            capo_chatbot.errors.describe_chime_webhook_configurations_exception.DescribeChimeWebhookConfigurationsException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.describe_chime_webhook_configurations_request.DescribeChimeWebhookConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.describe_chime_webhook_configurations_result.DescribeChimeWebhookConfigurationsResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.describe_chime_webhook_configurations

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.describe_chime_webhook_configurations.async_describe_chime_webhook_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.describe_chime_webhook_configurations_request.DescribeChimeWebhookConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if chat_configuration_arn is not None:
            input_["chat_configuration_arn"] = chat_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_chime_webhook_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        chat_configuration_arn: Optional[
            "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
    ) -> "AsyncIterator[capo_chatbot.types.chime_webhook_configuration.ChimeWebhookConfiguration]":
        _token = next_token
        while True:
            _response = await self.describe_chime_webhook_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                chat_configuration_arn=chat_configuration_arn,
            )
            _page = _resolve_path(_response, ("webhook_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_slack_channel_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        chat_configuration_arn: Optional[
            "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
    ) -> "capo_chatbot.types.describe_slack_channel_configurations_result.DescribeSlackChannelConfigurationsResult":
        """<p>Lists Slack channel configurations optionally filtered by ChatConfigurationArn</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>
            next_token: <p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>
            chat_configuration_arn: <p>An optional Amazon Resource Name (ARN) of a SlackChannelConfiguration to describe.</p>

        Raises:
            capo_chatbot.errors.describe_slack_channel_configurations_exception.DescribeSlackChannelConfigurationsException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.describe_slack_channel_configurations_request.DescribeSlackChannelConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.describe_slack_channel_configurations_result.DescribeSlackChannelConfigurationsResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.describe_slack_channel_configurations

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.describe_slack_channel_configurations.async_describe_slack_channel_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.describe_slack_channel_configurations_request.DescribeSlackChannelConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if chat_configuration_arn is not None:
            input_["chat_configuration_arn"] = chat_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_slack_channel_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        chat_configuration_arn: Optional[
            "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
    ) -> "AsyncIterator[capo_chatbot.types.slack_channel_configuration.SlackChannelConfiguration]":
        _token = next_token
        while True:
            _response = await self.describe_slack_channel_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                chat_configuration_arn=chat_configuration_arn,
            )
            _page = _resolve_path(_response, ("slack_channel_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_slack_user_identities(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        chat_configuration_arn: Optional[
            "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
    ) -> "capo_chatbot.types.describe_slack_user_identities_result.DescribeSlackUserIdentitiesResult":
        """<p>Lists all Slack user identities with a mapped role.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the SlackChannelConfiguration associated with the user identities to describe.</p>
            next_token: <p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>

        Raises:
            capo_chatbot.errors.describe_slack_user_identities_exception.DescribeSlackUserIdentitiesException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.describe_slack_user_identities_request.DescribeSlackUserIdentitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.describe_slack_user_identities_result.DescribeSlackUserIdentitiesResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.describe_slack_user_identities

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.describe_slack_user_identities.async_describe_slack_user_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.describe_slack_user_identities_request.DescribeSlackUserIdentitiesRequest = {}
        if chat_configuration_arn is not None:
            input_["chat_configuration_arn"] = chat_configuration_arn
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

    async def iter_describe_slack_user_identities(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        chat_configuration_arn: Optional[
            "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_chatbot.types.slack_user_identity.SlackUserIdentity]":
        _token = next_token
        while True:
            _response = await self.describe_slack_user_identities(
                config_overrides=config_overrides,
                chat_configuration_arn=chat_configuration_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("slack_user_identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_slack_workspaces(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_chatbot.types.describe_slack_workspaces_result.DescribeSlackWorkspacesResult":
        """<p>List all authorized Slack workspaces connected to the AWS Account onboarded with AWS Chatbot.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>
            next_token: <p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>

        Raises:
            capo_chatbot.errors.describe_slack_workspaces_exception.DescribeSlackWorkspacesException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.describe_slack_workspaces_request.DescribeSlackWorkspacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.describe_slack_workspaces_result.DescribeSlackWorkspacesResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.describe_slack_workspaces

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.describe_slack_workspaces.async_describe_slack_workspaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.describe_slack_workspaces_request.DescribeSlackWorkspacesRequest = {}
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

    async def iter_describe_slack_workspaces(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_chatbot.types.slack_workspace.SlackWorkspace]":
        _token = next_token
        while True:
            _response = await self.describe_slack_workspaces(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("slack_workspaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disassociate_from_configuration(
        self,
        resource: "capo_chatbot.types.resource_identifier.ResourceIdentifier",
        chat_configuration: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.disassociate_from_configuration_result.DisassociateFromConfigurationResult":
        """<p>Unlink a resource, for example a custom action, from a channel configuration.</p>

        Args:
            resource: <p>The resource (for example, a custom action) Amazon Resource Name (ARN) to unlink.</p>
            chat_configuration: <p>The channel configuration the resource is being disassociated from.</p>

        Raises:
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Disassociate a custom action from a configuration

            >>> await client.disassociate_from_configuration(resource='arn:aws:chatbot::1234567890:custom-action/my-custom-action', chat_configuration='arn:aws:chatbot::1234567890:chat-configuration/slack-channel/my-channel')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.disassociate_from_configuration_request.DisassociateFromConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.disassociate_from_configuration_result.DisassociateFromConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.disassociate_from_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.disassociate_from_configuration.async_disassociate_from_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.disassociate_from_configuration_request.DisassociateFromConfigurationRequest = {
            "resource": resource,
            "chat_configuration": chat_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account_preferences(
        self, *, config_overrides: Optional[AsyncchatbotClientConfig] = None
    ) -> (
        "capo_chatbot.types.get_account_preferences_result.GetAccountPreferencesResult"
    ):
        """<p>Returns AWS Chatbot account preferences.</p>

        Raises:
            capo_chatbot.errors.get_account_preferences_exception.GetAccountPreferencesException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.get_account_preferences_request.GetAccountPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.get_account_preferences_result.GetAccountPreferencesResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.get_account_preferences

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.get_account_preferences.async_get_account_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.get_account_preferences_request.GetAccountPreferencesRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_microsoft_teams_channel_configuration(
        self,
        chat_configuration_arn: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.get_teams_channel_configuration_result.GetTeamsChannelConfigurationResult":
        """<p>Returns a Microsoft Teams channel configuration in an AWS account.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration to retrieve.</p>

        Raises:
            capo_chatbot.errors.get_teams_channel_configuration_exception.GetTeamsChannelConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.get_teams_channel_configuration_request.GetTeamsChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.get_teams_channel_configuration_result.GetTeamsChannelConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.get_microsoft_teams_channel_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.get_microsoft_teams_channel_configuration.async_get_microsoft_teams_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.get_teams_channel_configuration_request.GetTeamsChannelConfigurationRequest = {
            "chat_configuration_arn": chat_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_associations(
        self,
        chat_configuration: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_chatbot.types.string.String"] = None,
    ) -> "capo_chatbot.types.list_associations_result.ListAssociationsResult":
        """<p>Lists resources associated with a channel configuration.</p>

        Args:
            chat_configuration: <p>The channel configuration to list associations for.</p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>

        Raises:
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List custom actions associated with a configuration

            >>> await client.list_associations(chat_configuration='arn:aws:chatbot::1234567890:chat-configuration/slack-channel/my-channel')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.list_associations_request.ListAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.list_associations_result.ListAssociationsResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.list_associations

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.list_associations.async_list_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.list_associations_request.ListAssociationsRequest = {
            "chat_configuration": chat_configuration
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

    async def iter_list_associations(
        self,
        chat_configuration: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_chatbot.types.string.String"] = None,
    ) -> "AsyncIterator[capo_chatbot.types.association_listing.AssociationListing]":
        _token = next_token
        while True:
            _response = await self.list_associations(
                chat_configuration,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_microsoft_teams_channel_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        team_id: Optional["capo_chatbot.types.uuid.UUID"] = None,
    ) -> "capo_chatbot.types.list_teams_channel_configurations_result.ListTeamsChannelConfigurationsResult":
        """<p>Lists all AWS Chatbot Microsoft Teams channel configurations in an AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>
            team_id: <p> The ID of the Microsoft Teams authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>

        Raises:
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.list_teams_channel_configurations_exception.ListTeamsChannelConfigurationsException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.list_teams_channel_configurations_request.ListTeamsChannelConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.list_teams_channel_configurations_result.ListTeamsChannelConfigurationsResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_channel_configurations

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_channel_configurations.async_list_microsoft_teams_channel_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.list_teams_channel_configurations_request.ListTeamsChannelConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if team_id is not None:
            input_["team_id"] = team_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_microsoft_teams_channel_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        team_id: Optional["capo_chatbot.types.uuid.UUID"] = None,
    ) -> "AsyncIterator[capo_chatbot.types.teams_channel_configuration.TeamsChannelConfiguration]":
        _token = next_token
        while True:
            _response = await self.list_microsoft_teams_channel_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                team_id=team_id,
            )
            _page = _resolve_path(_response, ("team_channel_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_microsoft_teams_configured_teams(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_chatbot.types.list_microsoft_teams_configured_teams_result.ListMicrosoftTeamsConfiguredTeamsResult":
        """<p>Lists all authorized Microsoft Teams for an AWS Account</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>

        Raises:
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.list_microsoft_teams_configured_teams_exception.ListMicrosoftTeamsConfiguredTeamsException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.list_microsoft_teams_configured_teams_request.ListMicrosoftTeamsConfiguredTeamsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.list_microsoft_teams_configured_teams_result.ListMicrosoftTeamsConfiguredTeamsResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_configured_teams

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_configured_teams.async_list_microsoft_teams_configured_teams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.list_microsoft_teams_configured_teams_request.ListMicrosoftTeamsConfiguredTeamsRequest = {}
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

    async def iter_list_microsoft_teams_configured_teams(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_chatbot.types.configured_team.ConfiguredTeam]":
        _token = next_token
        while True:
            _response = await self.list_microsoft_teams_configured_teams(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("configured_teams",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_microsoft_teams_user_identities(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        chat_configuration_arn: Optional[
            "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
    ) -> "capo_chatbot.types.list_microsoft_teams_user_identities_result.ListMicrosoftTeamsUserIdentitiesResult":
        """<p>A list all Microsoft Teams user identities with a mapped role.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identities to list.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>

        Raises:
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.list_microsoft_teams_user_identities_exception.ListMicrosoftTeamsUserIdentitiesException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.list_microsoft_teams_user_identities_request.ListMicrosoftTeamsUserIdentitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.list_microsoft_teams_user_identities_result.ListMicrosoftTeamsUserIdentitiesResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_user_identities

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_user_identities.async_list_microsoft_teams_user_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.list_microsoft_teams_user_identities_request.ListMicrosoftTeamsUserIdentitiesRequest = {}
        if chat_configuration_arn is not None:
            input_["chat_configuration_arn"] = chat_configuration_arn
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

    async def iter_list_microsoft_teams_user_identities(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        chat_configuration_arn: Optional[
            "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
        next_token: Optional[
            "capo_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_chatbot.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_chatbot.types.teams_user_identity.TeamsUserIdentity]":
        _token = next_token
        while True:
            _response = await self.list_microsoft_teams_user_identities(
                config_overrides=config_overrides,
                chat_configuration_arn=chat_configuration_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("teams_user_identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_chatbot.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> (
        "capo_chatbot.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a user, server, or role.</p>

        Args:
            resource_arn: <p>The ARN of the resource to list tags for.</p>

        Raises:
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.service_unavailable_exception.ServiceUnavailableException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_chatbot.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_chatbot.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.tag_resource_response.TagResourceResponse":
        """<p>Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.</p>

        Args:
            resource_arn: <p>The ARN of the configuration.</p>
            tags: <p>A list of tags to apply to the configuration.</p>

        Raises:
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.service_unavailable_exception.ServiceUnavailableException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.too_many_tags_exception.TooManyTagsException: <p>The supplied list of tags contains too many tags.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.tag_resource

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_chatbot.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_chatbot.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.untag_resource_response.UntagResourceResponse":
        """<p>Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.</p>

        Args:
            resource_arn: <p>The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific AWS resource, such as a server, user, or role.</p>
            tag_keys: <p>TagKeys are key-value pairs assigned to ARNs that can be used to group and search for resources by type. This metadata can be attached to resources for any purpose.</p>

        Raises:
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.service_unavailable_exception.ServiceUnavailableException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.untag_resource

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_account_preferences(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        user_authorization_required: Optional[
            "capo_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
        training_data_collection_enabled: Optional[
            "capo_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
    ) -> "capo_chatbot.types.update_account_preferences_result.UpdateAccountPreferencesResult":
        """<p>Updates AWS Chatbot account preferences.</p>

        Args:
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>
            training_data_collection_enabled: <p>Turns on training data collection.</p> <p>This helps improve the AWS Chatbot experience by allowing AWS Chatbot to store and use your customer information, such as AWS Chatbot configurations, notifications, user inputs, AWS Chatbot generated responses, and interaction data. This data helps us to continuously improve and develop Artificial Intelligence (AI) technologies. Your data is not shared with any third parties and is protected using sophisticated controls to prevent unauthorized access and misuse. AWS Chatbot does not store or use interactions in chat channels with Amazon Q for training AI technologies for AWS Chatbot. </p>

        Raises:
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.update_account_preferences_exception.UpdateAccountPreferencesException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.update_account_preferences_request.UpdateAccountPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.update_account_preferences_result.UpdateAccountPreferencesResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.update_account_preferences

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.update_account_preferences.async_update_account_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.update_account_preferences_request.UpdateAccountPreferencesRequest = {}
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required
        if training_data_collection_enabled is not None:
            input_["training_data_collection_enabled"] = (
                training_data_collection_enabled
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_chime_webhook_configuration(
        self,
        chat_configuration_arn: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        webhook_description: Optional[
            "capo_chatbot.types.chime_webhook_description.ChimeWebhookDescription"
        ] = None,
        webhook_url: Optional[
            "capo_chatbot.types.chime_webhook_url.ChimeWebhookUrl"
        ] = None,
        sns_topic_arns: Optional[
            "capo_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        iam_role_arn: Optional["capo_chatbot.types.arn.Arn"] = None,
        logging_level: Optional[
            "capo_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
    ) -> "capo_chatbot.types.update_chime_webhook_configuration_result.UpdateChimeWebhookConfigurationResult":
        """<p>Updates a Amazon Chime webhook configuration.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the ChimeWebhookConfiguration to update.</p>
            webhook_description: <p>A description of the webhook. We recommend using the convention <code>RoomName/WebhookName</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html">Tutorial: Get started with Amazon Chime</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            webhook_url: <p>The URL for the Amazon Chime webhook.</p>
            sns_topic_arns: <p>The ARNs of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>

        Raises:
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.update_chime_webhook_configuration_exception.UpdateChimeWebhookConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.update_chime_webhook_configuration_request.UpdateChimeWebhookConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.update_chime_webhook_configuration_result.UpdateChimeWebhookConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.update_chime_webhook_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.update_chime_webhook_configuration.async_update_chime_webhook_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.update_chime_webhook_configuration_request.UpdateChimeWebhookConfigurationRequest = {
            "chat_configuration_arn": chat_configuration_arn
        }
        if webhook_description is not None:
            input_["webhook_description"] = webhook_description
        if webhook_url is not None:
            input_["webhook_url"] = webhook_url
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if logging_level is not None:
            input_["logging_level"] = logging_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_microsoft_teams_channel_configuration(
        self,
        chat_configuration_arn: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        channel_id: "capo_chatbot.types.teams_channel_id.TeamsChannelId",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        channel_name: Optional[
            "capo_chatbot.types.teams_channel_name.TeamsChannelName"
        ] = None,
        sns_topic_arns: Optional[
            "capo_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        iam_role_arn: Optional["capo_chatbot.types.arn.Arn"] = None,
        logging_level: Optional[
            "capo_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        guardrail_policy_arns: Optional[
            "capo_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
        ] = None,
        user_authorization_required: Optional[
            "capo_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
    ) -> "capo_chatbot.types.update_teams_channel_configuration_result.UpdateTeamsChannelConfigurationResult":
        """<p>Updates an Microsoft Teams channel configuration.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the TeamsChannelConfiguration to update.</p>
            channel_id: <p>The ID of the Microsoft Teams channel.</p>
            channel_name: <p>The name of the Microsoft Teams channel.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            guardrail_policy_arns: <p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>

        Raises:
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.update_teams_channel_configuration_exception.UpdateTeamsChannelConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.update_teams_channel_configuration_request.UpdateTeamsChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.update_teams_channel_configuration_result.UpdateTeamsChannelConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.update_microsoft_teams_channel_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.update_microsoft_teams_channel_configuration.async_update_microsoft_teams_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.update_teams_channel_configuration_request.UpdateTeamsChannelConfigurationRequest = {
            "chat_configuration_arn": chat_configuration_arn,
            "channel_id": channel_id,
        }
        if channel_name is not None:
            input_["channel_name"] = channel_name
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if guardrail_policy_arns is not None:
            input_["guardrail_policy_arns"] = guardrail_policy_arns
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_slack_channel_configuration(
        self,
        chat_configuration_arn: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        slack_channel_id: "capo_chatbot.types.slack_channel_id.SlackChannelId",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        slack_channel_name: Optional[
            "capo_chatbot.types.slack_channel_display_name.SlackChannelDisplayName"
        ] = None,
        sns_topic_arns: Optional[
            "capo_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        iam_role_arn: Optional["capo_chatbot.types.arn.Arn"] = None,
        logging_level: Optional[
            "capo_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        guardrail_policy_arns: Optional[
            "capo_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
        ] = None,
        user_authorization_required: Optional[
            "capo_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
    ) -> "capo_chatbot.types.update_slack_channel_configuration_result.UpdateSlackChannelConfigurationResult":
        """<p>Updates a Slack channel configuration.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the SlackChannelConfiguration to update.</p>
            slack_channel_id: <p>The ID of the Slack channel.</p> <p>To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ. </p>
            slack_channel_name: <p>The name of the Slack channel.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            guardrail_policy_arns: <p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>

        Raises:
            capo_chatbot.errors.invalid_parameter_exception.InvalidParameterException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.update_slack_channel_configuration_exception.UpdateSlackChannelConfigurationException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.update_slack_channel_configuration_request.UpdateSlackChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.update_slack_channel_configuration_result.UpdateSlackChannelConfigurationResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.update_slack_channel_configuration

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.update_slack_channel_configuration.async_update_slack_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.update_slack_channel_configuration_request.UpdateSlackChannelConfigurationRequest = {
            "chat_configuration_arn": chat_configuration_arn,
            "slack_channel_id": slack_channel_id,
        }
        if slack_channel_name is not None:
            input_["slack_channel_name"] = slack_channel_name
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if guardrail_policy_arns is not None:
            input_["guardrail_policy_arns"] = guardrail_policy_arns
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_action(
        self,
        definition: "capo_chatbot.types.custom_action_definition.CustomActionDefinition",
        action_name: "capo_chatbot.types.custom_action_name.CustomActionName",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        alias_name: Optional[
            "capo_chatbot.types.custom_action_alias_name.CustomActionAliasName"
        ] = None,
        attachments: Optional[
            "capo_chatbot.types.custom_action_attachment_list.CustomActionAttachmentList"
        ] = None,
        tags: Optional["capo_chatbot.types.tag_list.TagList"] = None,
        client_token: Optional["capo_chatbot.types.client_token.ClientToken"] = None,
    ) -> "capo_chatbot.types.create_custom_action_result.CreateCustomActionResult":
        """<p>Creates a custom action that can be invoked as an alias or as a button on a notification.</p>

        Args:
            definition: <p>The definition of the command to run when invoked as an alias or as an action button.</p>
            alias_name: <p>The name used to invoke this action in a chat channel. For example, <code>@aws run my-alias</code>.</p>
            attachments: <p>Defines when this custom action button should be attached to a notification.</p>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request.</p> <p>If you do not specify a client token, one is automatically generated by the SDK.</p>
            action_name: <p>The name of the custom action. This name is included in the Amazon Resource Name (ARN).</p>

        Raises:
            capo_chatbot.errors.conflict_exception.ConflictException: <p>There was an issue processing your request.</p>
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for AWS Chatbot.</p>
            capo_chatbot.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an alias that invokes a Lambda function
            Creates an alias that invokes a Lambda function from chat channels. You can use this alias by entering 'run invoke', after which you're prompted for the function name.

            >>> await client.create_custom_action(action_name='my-custom-action', definition={'CommandText': 'lambda invoke $functionName'}, alias_name='invoke')
            Create a custom action to list alarms
            Creates a button on all Cloudwatch notifications that lists alarms in the ‘ALARM’ state.

            >>> await client.create_custom_action(action_name='describe-alarms', definition={'CommandText': 'cloudwatch describe-alarms --state-value ALARM'}, attachments=[{'NotificationType': 'CloudWatch', 'ButtonText': 'List alarms'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.create_custom_action_request.CreateCustomActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.create_custom_action_result.CreateCustomActionResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.create_custom_action

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.create_custom_action.async_create_custom_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.create_custom_action_request.CreateCustomActionRequest = {
            "definition": definition,
            "action_name": action_name,
        }
        if alias_name is not None:
            input_["alias_name"] = alias_name
        if attachments is not None:
            input_["attachments"] = attachments
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

    async def get_custom_action(
        self,
        custom_action_arn: "capo_chatbot.types.custom_action_arn.CustomActionArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.get_custom_action_result.GetCustomActionResult":
        """<p>Returns a custom action.</p>

        Args:
            custom_action_arn: <p>Returns the fully defined Amazon Resource Name (ARN) of the custom action.</p>

        Raises:
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a custom action

            >>> await client.get_custom_action(custom_action_arn='arn:aws:chatbot::1234567890:custom-action/my-custom-action')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.get_custom_action_request.GetCustomActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.get_custom_action_result.GetCustomActionResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.get_custom_action

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.get_custom_action.async_get_custom_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.get_custom_action_request.GetCustomActionRequest = {
            "custom_action_arn": custom_action_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_custom_action(
        self,
        custom_action_arn: "capo_chatbot.types.custom_action_arn.CustomActionArn",
        definition: "capo_chatbot.types.custom_action_definition.CustomActionDefinition",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        alias_name: Optional[
            "capo_chatbot.types.custom_action_alias_name.CustomActionAliasName"
        ] = None,
        attachments: Optional[
            "capo_chatbot.types.custom_action_attachment_list.CustomActionAttachmentList"
        ] = None,
    ) -> "capo_chatbot.types.update_custom_action_result.UpdateCustomActionResult":
        """<p>Updates a custom action.</p>

        Args:
            custom_action_arn: <p>The fully defined Amazon Resource Name (ARN) of the custom action.</p>
            definition: <p>The definition of the command to run when invoked as an alias or as an action button.</p>
            alias_name: <p>The name used to invoke this action in the chat channel. For example, <code>@aws run my-alias</code>.</p>
            attachments: <p>Defines when this custom action button should be attached to a notification.</p>

        Raises:
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update the command definition of an existing action
            Updates the command text of a custom action without altering the existing alias name or attachment criteria

            >>> await client.update_custom_action(custom_action_arn='arn:aws:chatbot::1234567890:custom-action/my-custom-action', definition={'CommandText': 'lambda invoke MyNewFunction'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.update_custom_action_request.UpdateCustomActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.update_custom_action_result.UpdateCustomActionResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.update_custom_action

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.update_custom_action.async_update_custom_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.update_custom_action_request.UpdateCustomActionRequest = {
            "custom_action_arn": custom_action_arn,
            "definition": definition,
        }
        if alias_name is not None:
            input_["alias_name"] = alias_name
        if attachments is not None:
            input_["attachments"] = attachments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_action(
        self,
        custom_action_arn: "capo_chatbot.types.custom_action_arn.CustomActionArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "capo_chatbot.types.delete_custom_action_result.DeleteCustomActionResult":
        """<p>Deletes a custom action.</p>

        Args:
            custom_action_arn: <p>The fully defined ARN of the custom action.</p>

        Raises:
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.resource_not_found_exception.ResourceNotFoundException: <p>We were unable to find the resource for your request</p>
            capo_chatbot.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a custom action

            >>> await client.delete_custom_action(custom_action_arn='arn:aws:chatbot::1234567890:custom-action/my-custom-action')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.delete_custom_action_request.DeleteCustomActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.delete_custom_action_result.DeleteCustomActionResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.delete_custom_action

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.delete_custom_action.async_delete_custom_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.delete_custom_action_request.DeleteCustomActionRequest = {
            "custom_action_arn": custom_action_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_custom_actions(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_chatbot.types.list_custom_actions_result.ListCustomActionsResult":
        """<p>Lists custom actions defined in this account.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>

        Raises:
            capo_chatbot.errors.internal_service_error.InternalServiceError: <p>Unexpected error during processing of request.</p>
            capo_chatbot.errors.invalid_request_exception.InvalidRequestException: <p>Your request input doesn't meet the constraints required by AWS Chatbot.</p>
            capo_chatbot.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_chatbot.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List custom actions

            >>> await client.list_custom_actions()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chatbot.types.list_custom_actions_request.ListCustomActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chatbot.types.list_custom_actions_result.ListCustomActionsResult"
        ]:
            import capo_chatbot._operations.wheatley_orchestration_20171011.list_custom_actions

            (
                output,
                http_response,
            ) = await capo_chatbot._operations.wheatley_orchestration_20171011.list_custom_actions.async_list_custom_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chatbot.types.list_custom_actions_request.ListCustomActionsRequest = {}
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

    async def iter_list_custom_actions(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_chatbot.types.custom_action_arn.CustomActionArn]":
        _token = next_token
        while True:
            _response = await self.list_custom_actions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("custom_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
