"""Generated from Smithy shape ``com.amazonaws.supportapp#SupportApp``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_support_app._auth._signers
import capo_support_app._auth._sigv4
from capo_support_app._auth._identity import Credentials
from capo_support_app._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_support_app._auth._zapros_handler import AuthMiddleware
from capo_support_app._pagination import resolve_path as _resolve_path
from capo_support_app._services._aws_config import aws_config
from capo_support_app._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_support_app.types.aws_account_alias
    import capo_support_app.types.boolean_value
    import capo_support_app.types.channel_id
    import capo_support_app.types.channel_name
    import capo_support_app.types.create_slack_channel_configuration_request
    import capo_support_app.types.create_slack_channel_configuration_result
    import capo_support_app.types.delete_account_alias_request
    import capo_support_app.types.delete_account_alias_result
    import capo_support_app.types.delete_slack_channel_configuration_request
    import capo_support_app.types.delete_slack_channel_configuration_result
    import capo_support_app.types.delete_slack_workspace_configuration_request
    import capo_support_app.types.delete_slack_workspace_configuration_result
    import capo_support_app.types.get_account_alias_request
    import capo_support_app.types.get_account_alias_result
    import capo_support_app.types.list_slack_channel_configurations_request
    import capo_support_app.types.list_slack_channel_configurations_result
    import capo_support_app.types.list_slack_workspace_configurations_request
    import capo_support_app.types.list_slack_workspace_configurations_result
    import capo_support_app.types.notification_severity_level
    import capo_support_app.types.pagination_token
    import capo_support_app.types.put_account_alias_request
    import capo_support_app.types.put_account_alias_result
    import capo_support_app.types.register_slack_workspace_for_organization_request
    import capo_support_app.types.register_slack_workspace_for_organization_result
    import capo_support_app.types.role_arn
    import capo_support_app.types.team_id
    import capo_support_app.types.update_slack_channel_configuration_request
    import capo_support_app.types.update_slack_channel_configuration_result


class SupportAppClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class SupportAppClient:
    """A client for the ``SupportApp`` service.

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
        self._config = SupportAppClientConfig(
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
        self, config_overrides: Optional[SupportAppClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SupportAppClientConfig = config_overrides or {}
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

    def create_slack_channel_configuration(
        self,
        team_id: "capo_support_app.types.team_id.teamId",
        channel_id: "capo_support_app.types.channel_id.channelId",
        notify_on_case_severity: "capo_support_app.types.notification_severity_level.NotificationSeverityLevel",
        channel_role_arn: "capo_support_app.types.role_arn.roleArn",
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
        channel_name: Optional[
            "capo_support_app.types.channel_name.channelName"
        ] = None,
        notify_on_create_or_reopen_case: Optional[
            "capo_support_app.types.boolean_value.booleanValue"
        ] = None,
        notify_on_add_correspondence_to_case: Optional[
            "capo_support_app.types.boolean_value.booleanValue"
        ] = None,
        notify_on_resolve_case: Optional[
            "capo_support_app.types.boolean_value.booleanValue"
        ] = None,
    ) -> "capo_support_app.types.create_slack_channel_configuration_result.CreateSlackChannelConfigurationResult":
        """<p>Creates a Slack channel configuration for your Amazon Web Services account.</p> <note> <ul> <li> <p>You can add up to 5 Slack workspaces for your account.</p> </li> <li> <p>You can add up to 20 Slack channels for your account.</p> </li> </ul> </note> <p>A Slack channel can have up to 100 Amazon Web Services accounts. This means that only 100 accounts can add the same Slack channel to the Amazon Web Services Support App. We recommend that you only add the accounts that you need to manage support cases for your organization. This can reduce the notifications about case updates that you receive in the Slack channel.</p> <note> <p>We recommend that you choose a private Slack channel so that only members in that channel have read and write access to your support cases. Anyone in your Slack channel can create, update, or resolve support cases for your account. Users require an invitation to join private channels. </p> </note>

        Args:
            team_id: <p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>
            channel_id: <p>The channel ID in Slack. This ID identifies a channel within a Slack workspace.</p>
            channel_name: <p>The name of the Slack channel that you configure for the Amazon Web Services Support App.</p>
            notify_on_create_or_reopen_case: <p>Whether you want to get notified when a support case is created or reopened.</p>
            notify_on_add_correspondence_to_case: <p>Whether you want to get notified when a support case has a new correspondence.</p>
            notify_on_resolve_case: <p>Whether you want to get notified when a support case is resolved.</p>
            notify_on_case_severity: <p>The case severity for a support case that you want to receive notifications.</p> <p>If you specify <code>high</code> or <code>all</code>, you must specify <code>true</code> for at least one of the following parameters:</p> <ul> <li> <p> <code>notifyOnAddCorrespondenceToCase</code> </p> </li> <li> <p> <code>notifyOnCreateOrReopenCase</code> </p> </li> <li> <p> <code>notifyOnResolveCase</code> </p> </li> </ul> <p>If you specify <code>none</code>, the following parameters must be null or <code>false</code>:</p> <ul> <li> <p> <code>notifyOnAddCorrespondenceToCase</code> </p> </li> <li> <p> <code>notifyOnCreateOrReopenCase</code> </p> </li> <li> <p> <code>notifyOnResolveCase</code> </p> </li> </ul> <note> <p>If you don't specify these parameters in your request, they default to <code>false</code>.</p> </note>
            channel_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on Amazon Web Services. For more information, see <a href="https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html">Managing access to the Amazon Web Services Support App</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Raises:
            capo_support_app.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_support_app.errors.conflict_exception.ConflictException: <p>Your request has a conflict. For example, you might receive this error if you try the following:</p> <ul> <li> <p>Add, update, or delete a Slack channel configuration before you add a Slack workspace to your Amazon Web Services account.</p> </li> <li> <p>Add a Slack channel configuration that already exists in your Amazon Web Services account.</p> </li> <li> <p>Delete a Slack channel configuration for a live chat channel.</p> </li> <li> <p>Delete a Slack workspace from your Amazon Web Services account that has an active live chat channel.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from an Amazon Web Services account that doesn't belong to an organization.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from a member account, but the management account hasn't registered that workspace yet for the organization.</p> </li> </ul>
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your Service Quotas request exceeds the quota for the service. For example, your Service Quotas request to Amazon Web Services Support App might exceed the maximum number of workspaces or channels per account, or the maximum number of accounts per Slack channel.</p>
            capo_support_app.errors.validation_exception.ValidationException: <p>Your request input doesn't meet the constraints that the Amazon Web Services Support App specifies.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.create_slack_channel_configuration_request.CreateSlackChannelConfigurationRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.create_slack_channel_configuration_result.CreateSlackChannelConfigurationResult"
        ]:
            import capo_support_app._operations.support_app.create_slack_channel_configuration

            output, http_response = (
                capo_support_app._operations.support_app.create_slack_channel_configuration.create_slack_channel_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.create_slack_channel_configuration_request.CreateSlackChannelConfigurationRequest = {
            "team_id": team_id,
            "channel_id": channel_id,
            "notify_on_case_severity": notify_on_case_severity,
            "channel_role_arn": channel_role_arn,
        }
        if channel_name is not None:
            input_["channel_name"] = channel_name
        if notify_on_create_or_reopen_case is not None:
            input_["notify_on_create_or_reopen_case"] = notify_on_create_or_reopen_case
        if notify_on_add_correspondence_to_case is not None:
            input_["notify_on_add_correspondence_to_case"] = (
                notify_on_add_correspondence_to_case
            )
        if notify_on_resolve_case is not None:
            input_["notify_on_resolve_case"] = notify_on_resolve_case

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_account_alias(
        self, *, config_overrides: Optional[SupportAppClientConfig] = None
    ) -> "capo_support_app.types.delete_account_alias_result.DeleteAccountAliasResult":
        """<p>Deletes an alias for an Amazon Web Services account ID. The alias appears in the Amazon Web Services Support App page of the Amazon Web Services Support Center. The alias also appears in Slack messages from the Amazon Web Services Support App.</p>

        Raises:
            capo_support_app.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource is missing or doesn't exist, such as an account alias, Slack channel configuration, or Slack workspace configuration.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.delete_account_alias_request.DeleteAccountAliasRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.delete_account_alias_result.DeleteAccountAliasResult"
        ]:
            import capo_support_app._operations.support_app.delete_account_alias

            output, http_response = (
                capo_support_app._operations.support_app.delete_account_alias.delete_account_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.delete_account_alias_request.DeleteAccountAliasRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_slack_channel_configuration(
        self,
        team_id: "capo_support_app.types.team_id.teamId",
        channel_id: "capo_support_app.types.channel_id.channelId",
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
    ) -> "capo_support_app.types.delete_slack_channel_configuration_result.DeleteSlackChannelConfigurationResult":
        """<p>Deletes a Slack channel configuration from your Amazon Web Services account. This operation doesn't delete your Slack channel.</p>

        Args:
            team_id: <p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>
            channel_id: <p>The channel ID in Slack. This ID identifies a channel within a Slack workspace.</p>

        Raises:
            capo_support_app.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_support_app.errors.conflict_exception.ConflictException: <p>Your request has a conflict. For example, you might receive this error if you try the following:</p> <ul> <li> <p>Add, update, or delete a Slack channel configuration before you add a Slack workspace to your Amazon Web Services account.</p> </li> <li> <p>Add a Slack channel configuration that already exists in your Amazon Web Services account.</p> </li> <li> <p>Delete a Slack channel configuration for a live chat channel.</p> </li> <li> <p>Delete a Slack workspace from your Amazon Web Services account that has an active live chat channel.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from an Amazon Web Services account that doesn't belong to an organization.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from a member account, but the management account hasn't registered that workspace yet for the organization.</p> </li> </ul>
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource is missing or doesn't exist, such as an account alias, Slack channel configuration, or Slack workspace configuration.</p>
            capo_support_app.errors.validation_exception.ValidationException: <p>Your request input doesn't meet the constraints that the Amazon Web Services Support App specifies.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.delete_slack_channel_configuration_request.DeleteSlackChannelConfigurationRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.delete_slack_channel_configuration_result.DeleteSlackChannelConfigurationResult"
        ]:
            import capo_support_app._operations.support_app.delete_slack_channel_configuration

            output, http_response = (
                capo_support_app._operations.support_app.delete_slack_channel_configuration.delete_slack_channel_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.delete_slack_channel_configuration_request.DeleteSlackChannelConfigurationRequest = {
            "team_id": team_id,
            "channel_id": channel_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_slack_workspace_configuration(
        self,
        team_id: "capo_support_app.types.team_id.teamId",
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
    ) -> "capo_support_app.types.delete_slack_workspace_configuration_result.DeleteSlackWorkspaceConfigurationResult":
        """<p>Deletes a Slack workspace configuration from your Amazon Web Services account. This operation doesn't delete your Slack workspace.</p>

        Args:
            team_id: <p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>

        Raises:
            capo_support_app.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_support_app.errors.conflict_exception.ConflictException: <p>Your request has a conflict. For example, you might receive this error if you try the following:</p> <ul> <li> <p>Add, update, or delete a Slack channel configuration before you add a Slack workspace to your Amazon Web Services account.</p> </li> <li> <p>Add a Slack channel configuration that already exists in your Amazon Web Services account.</p> </li> <li> <p>Delete a Slack channel configuration for a live chat channel.</p> </li> <li> <p>Delete a Slack workspace from your Amazon Web Services account that has an active live chat channel.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from an Amazon Web Services account that doesn't belong to an organization.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from a member account, but the management account hasn't registered that workspace yet for the organization.</p> </li> </ul>
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource is missing or doesn't exist, such as an account alias, Slack channel configuration, or Slack workspace configuration.</p>
            capo_support_app.errors.validation_exception.ValidationException: <p>Your request input doesn't meet the constraints that the Amazon Web Services Support App specifies.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.delete_slack_workspace_configuration_request.DeleteSlackWorkspaceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.delete_slack_workspace_configuration_result.DeleteSlackWorkspaceConfigurationResult"
        ]:
            import capo_support_app._operations.support_app.delete_slack_workspace_configuration

            output, http_response = (
                capo_support_app._operations.support_app.delete_slack_workspace_configuration.delete_slack_workspace_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.delete_slack_workspace_configuration_request.DeleteSlackWorkspaceConfigurationRequest = {
            "team_id": team_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_alias(
        self, *, config_overrides: Optional[SupportAppClientConfig] = None
    ) -> "capo_support_app.types.get_account_alias_result.GetAccountAliasResult":
        """<p>Retrieves the alias from an Amazon Web Services account ID. The alias appears in the Amazon Web Services Support App page of the Amazon Web Services Support Center. The alias also appears in Slack messages from the Amazon Web Services Support App.</p>

        Raises:
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.get_account_alias_request.GetAccountAliasRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.get_account_alias_result.GetAccountAliasResult"
        ]:
            import capo_support_app._operations.support_app.get_account_alias

            output, http_response = (
                capo_support_app._operations.support_app.get_account_alias.get_account_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.get_account_alias_request.GetAccountAliasRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_slack_channel_configurations(
        self,
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
        next_token: Optional[
            "capo_support_app.types.pagination_token.paginationToken"
        ] = None,
    ) -> "capo_support_app.types.list_slack_channel_configurations_result.ListSlackChannelConfigurationsResult":
        """<p>Lists the Slack channel configurations for an Amazon Web Services account.</p>

        Args:
            next_token: <p>If the results of a search are large, the API only returns a portion of the results and includes a <code>nextToken</code> pagination token in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When the API returns the last set of results, the response doesn't include a pagination token value.</p>

        Raises:
            capo_support_app.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.list_slack_channel_configurations_request.ListSlackChannelConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.list_slack_channel_configurations_result.ListSlackChannelConfigurationsResult"
        ]:
            import capo_support_app._operations.support_app.list_slack_channel_configurations

            output, http_response = (
                capo_support_app._operations.support_app.list_slack_channel_configurations.list_slack_channel_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.list_slack_channel_configurations_request.ListSlackChannelConfigurationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_slack_channel_configurations(
        self,
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
        next_token: Optional[
            "capo_support_app.types.pagination_token.paginationToken"
        ] = None,
    ) -> "Iterator[capo_support_app.types.list_slack_channel_configurations_result.ListSlackChannelConfigurationsResult]":
        _token = next_token
        while True:
            _response = self.list_slack_channel_configurations(
                config_overrides=config_overrides,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_slack_workspace_configurations(
        self,
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
        next_token: Optional[
            "capo_support_app.types.pagination_token.paginationToken"
        ] = None,
    ) -> "capo_support_app.types.list_slack_workspace_configurations_result.ListSlackWorkspaceConfigurationsResult":
        """<p>Lists the Slack workspace configurations for an Amazon Web Services account.</p>

        Args:
            next_token: <p>If the results of a search are large, the API only returns a portion of the results and includes a <code>nextToken</code> pagination token in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When the API returns the last set of results, the response doesn't include a pagination token value.</p>

        Raises:
            capo_support_app.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.list_slack_workspace_configurations_request.ListSlackWorkspaceConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.list_slack_workspace_configurations_result.ListSlackWorkspaceConfigurationsResult"
        ]:
            import capo_support_app._operations.support_app.list_slack_workspace_configurations

            output, http_response = (
                capo_support_app._operations.support_app.list_slack_workspace_configurations.list_slack_workspace_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.list_slack_workspace_configurations_request.ListSlackWorkspaceConfigurationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_slack_workspace_configurations(
        self,
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
        next_token: Optional[
            "capo_support_app.types.pagination_token.paginationToken"
        ] = None,
    ) -> "Iterator[capo_support_app.types.list_slack_workspace_configurations_result.ListSlackWorkspaceConfigurationsResult]":
        _token = next_token
        while True:
            _response = self.list_slack_workspace_configurations(
                config_overrides=config_overrides,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_account_alias(
        self,
        account_alias: "capo_support_app.types.aws_account_alias.awsAccountAlias",
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
    ) -> "capo_support_app.types.put_account_alias_result.PutAccountAliasResult":
        """<p>Creates or updates an individual alias for each Amazon Web Services account ID. The alias appears in the Amazon Web Services Support App page of the Amazon Web Services Support Center. The alias also appears in Slack messages from the Amazon Web Services Support App.</p>

        Args:
            account_alias: <p>An alias or short name for an Amazon Web Services account.</p>

        Raises:
            capo_support_app.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.validation_exception.ValidationException: <p>Your request input doesn't meet the constraints that the Amazon Web Services Support App specifies.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.put_account_alias_request.PutAccountAliasRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.put_account_alias_result.PutAccountAliasResult"
        ]:
            import capo_support_app._operations.support_app.put_account_alias

            output, http_response = (
                capo_support_app._operations.support_app.put_account_alias.put_account_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.put_account_alias_request.PutAccountAliasRequest = {
            "account_alias": account_alias
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_slack_workspace_for_organization(
        self,
        team_id: "capo_support_app.types.team_id.teamId",
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
    ) -> "capo_support_app.types.register_slack_workspace_for_organization_result.RegisterSlackWorkspaceForOrganizationResult":
        """<p>Registers a Slack workspace for your Amazon Web Services account. To call this API, your account must be part of an organization in Organizations.</p> <p>If you're the <i>management account</i> and you want to register Slack workspaces for your organization, you must complete the following tasks:</p> <ol> <li> <p>Sign in to the <a href="https://console.aws.amazon.com/support/app">Amazon Web Services Support Center</a> and authorize the Slack workspaces where you want your organization to have access to. See <a href="https://docs.aws.amazon.com/awssupport/latest/user/authorize-slack-workspace.html">Authorize a Slack workspace</a> in the <i>Amazon Web Services Support User Guide</i>.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API to authorize each Slack workspace for the organization.</p> </li> </ol> <p>After the management account authorizes the Slack workspace, member accounts can call this API to authorize the same Slack workspace for their individual accounts. Member accounts don't need to authorize the Slack workspace manually through the <a href="https://console.aws.amazon.com/support/app">Amazon Web Services Support Center</a>.</p> <p>To use the Amazon Web Services Support App, each account must then complete the following tasks:</p> <ul> <li> <p>Create an Identity and Access Management (IAM) role with the required permission. For more information, see <a href="https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html">Managing access to the Amazon Web Services Support App</a>.</p> </li> <li> <p>Configure a Slack channel to use the Amazon Web Services Support App for support cases for that account. For more information, see <a href="https://docs.aws.amazon.com/awssupport/latest/user/add-your-slack-channel.html">Configuring a Slack channel</a>.</p> </li> </ul>

        Args:
            team_id: <p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>. Specify the Slack workspace that you want to use for your organization.</p>

        Raises:
            capo_support_app.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_support_app.errors.conflict_exception.ConflictException: <p>Your request has a conflict. For example, you might receive this error if you try the following:</p> <ul> <li> <p>Add, update, or delete a Slack channel configuration before you add a Slack workspace to your Amazon Web Services account.</p> </li> <li> <p>Add a Slack channel configuration that already exists in your Amazon Web Services account.</p> </li> <li> <p>Delete a Slack channel configuration for a live chat channel.</p> </li> <li> <p>Delete a Slack workspace from your Amazon Web Services account that has an active live chat channel.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from an Amazon Web Services account that doesn't belong to an organization.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from a member account, but the management account hasn't registered that workspace yet for the organization.</p> </li> </ul>
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource is missing or doesn't exist, such as an account alias, Slack channel configuration, or Slack workspace configuration.</p>
            capo_support_app.errors.validation_exception.ValidationException: <p>Your request input doesn't meet the constraints that the Amazon Web Services Support App specifies.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.register_slack_workspace_for_organization_request.RegisterSlackWorkspaceForOrganizationRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.register_slack_workspace_for_organization_result.RegisterSlackWorkspaceForOrganizationResult"
        ]:
            import capo_support_app._operations.support_app.register_slack_workspace_for_organization

            output, http_response = (
                capo_support_app._operations.support_app.register_slack_workspace_for_organization.register_slack_workspace_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.register_slack_workspace_for_organization_request.RegisterSlackWorkspaceForOrganizationRequest = {
            "team_id": team_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_slack_channel_configuration(
        self,
        team_id: "capo_support_app.types.team_id.teamId",
        channel_id: "capo_support_app.types.channel_id.channelId",
        *,
        config_overrides: Optional[SupportAppClientConfig] = None,
        channel_name: Optional[
            "capo_support_app.types.channel_name.channelName"
        ] = None,
        notify_on_create_or_reopen_case: Optional[
            "capo_support_app.types.boolean_value.booleanValue"
        ] = None,
        notify_on_add_correspondence_to_case: Optional[
            "capo_support_app.types.boolean_value.booleanValue"
        ] = None,
        notify_on_resolve_case: Optional[
            "capo_support_app.types.boolean_value.booleanValue"
        ] = None,
        notify_on_case_severity: Optional[
            "capo_support_app.types.notification_severity_level.NotificationSeverityLevel"
        ] = None,
        channel_role_arn: Optional["capo_support_app.types.role_arn.roleArn"] = None,
    ) -> "capo_support_app.types.update_slack_channel_configuration_result.UpdateSlackChannelConfigurationResult":
        """<p>Updates the configuration for a Slack channel, such as case update notifications.</p>

        Args:
            team_id: <p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>
            channel_id: <p>The channel ID in Slack. This ID identifies a channel within a Slack workspace.</p>
            channel_name: <p>The Slack channel name that you want to update.</p>
            notify_on_create_or_reopen_case: <p>Whether you want to get notified when a support case is created or reopened.</p>
            notify_on_add_correspondence_to_case: <p>Whether you want to get notified when a support case has a new correspondence.</p>
            notify_on_resolve_case: <p>Whether you want to get notified when a support case is resolved.</p>
            notify_on_case_severity: <p>The case severity for a support case that you want to receive notifications.</p> <p>If you specify <code>high</code> or <code>all</code>, at least one of the following parameters must be <code>true</code>:</p> <ul> <li> <p> <code>notifyOnAddCorrespondenceToCase</code> </p> </li> <li> <p> <code>notifyOnCreateOrReopenCase</code> </p> </li> <li> <p> <code>notifyOnResolveCase</code> </p> </li> </ul> <p>If you specify <code>none</code>, any of the following parameters that you specify in your request must be <code>false</code>:</p> <ul> <li> <p> <code>notifyOnAddCorrespondenceToCase</code> </p> </li> <li> <p> <code>notifyOnCreateOrReopenCase</code> </p> </li> <li> <p> <code>notifyOnResolveCase</code> </p> </li> </ul> <note> <p>If you don't specify these parameters in your request, the Amazon Web Services Support App uses the current values by default.</p> </note>
            channel_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on Amazon Web Services. For more information, see <a href="https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html">Managing access to the Amazon Web Services Support App</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Raises:
            capo_support_app.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_support_app.errors.conflict_exception.ConflictException: <p>Your request has a conflict. For example, you might receive this error if you try the following:</p> <ul> <li> <p>Add, update, or delete a Slack channel configuration before you add a Slack workspace to your Amazon Web Services account.</p> </li> <li> <p>Add a Slack channel configuration that already exists in your Amazon Web Services account.</p> </li> <li> <p>Delete a Slack channel configuration for a live chat channel.</p> </li> <li> <p>Delete a Slack workspace from your Amazon Web Services account that has an active live chat channel.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from an Amazon Web Services account that doesn't belong to an organization.</p> </li> <li> <p>Call the <code>RegisterSlackWorkspaceForOrganization</code> API from a member account, but the management account hasn't registered that workspace yet for the organization.</p> </li> </ul>
            capo_support_app.errors.internal_server_exception.InternalServerException: <p>We can’t process your request right now because of a server issue. Try again later.</p>
            capo_support_app.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource is missing or doesn't exist, such as an account alias, Slack channel configuration, or Slack workspace configuration.</p>
            capo_support_app.errors.validation_exception.ValidationException: <p>Your request input doesn't meet the constraints that the Amazon Web Services Support App specifies.</p>
            capo_support_app.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_support_app.types.update_slack_channel_configuration_request.UpdateSlackChannelConfigurationRequest]",
        ) -> OperationResponse[
            "capo_support_app.types.update_slack_channel_configuration_result.UpdateSlackChannelConfigurationResult"
        ]:
            import capo_support_app._operations.support_app.update_slack_channel_configuration

            output, http_response = (
                capo_support_app._operations.support_app.update_slack_channel_configuration.update_slack_channel_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support_app.types.update_slack_channel_configuration_request.UpdateSlackChannelConfigurationRequest = {
            "team_id": team_id,
            "channel_id": channel_id,
        }
        if channel_name is not None:
            input_["channel_name"] = channel_name
        if notify_on_create_or_reopen_case is not None:
            input_["notify_on_create_or_reopen_case"] = notify_on_create_or_reopen_case
        if notify_on_add_correspondence_to_case is not None:
            input_["notify_on_add_correspondence_to_case"] = (
                notify_on_add_correspondence_to_case
            )
        if notify_on_resolve_case is not None:
            input_["notify_on_resolve_case"] = notify_on_resolve_case
        if notify_on_case_severity is not None:
            input_["notify_on_case_severity"] = notify_on_case_severity
        if channel_role_arn is not None:
            input_["channel_role_arn"] = channel_role_arn

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
