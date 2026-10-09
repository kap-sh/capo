"""Generated from Smithy shape ``com.amazonaws.detective#AmazonDetective``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_detective._auth._signers
import capo_detective._auth._sigv4
from capo_detective._auth._identity import Credentials
from capo_detective._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_detective._auth._zapros_handler import AuthMiddleware
from capo_detective._pagination import resolve_path as _resolve_path
from capo_detective._services._aws_config import aaws_config
from capo_detective._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_detective.types.accept_invitation_request
    import capo_detective.types.account_id
    import capo_detective.types.account_id_extended_list
    import capo_detective.types.account_id_list
    import capo_detective.types.account_list
    import capo_detective.types.ai_pagination_token
    import capo_detective.types.batch_get_graph_member_datasources_request
    import capo_detective.types.batch_get_graph_member_datasources_response
    import capo_detective.types.batch_get_membership_datasources_request
    import capo_detective.types.batch_get_membership_datasources_response
    import capo_detective.types.boolean
    import capo_detective.types.create_graph_request
    import capo_detective.types.create_graph_response
    import capo_detective.types.create_members_request
    import capo_detective.types.create_members_response
    import capo_detective.types.datasource_package_list
    import capo_detective.types.delete_graph_request
    import capo_detective.types.delete_members_request
    import capo_detective.types.delete_members_response
    import capo_detective.types.describe_organization_configuration_request
    import capo_detective.types.describe_organization_configuration_response
    import capo_detective.types.disassociate_membership_request
    import capo_detective.types.email_message
    import capo_detective.types.enable_organization_admin_account_request
    import capo_detective.types.entity_arn
    import capo_detective.types.filter_criteria
    import capo_detective.types.get_investigation_request
    import capo_detective.types.get_investigation_response
    import capo_detective.types.get_members_request
    import capo_detective.types.get_members_response
    import capo_detective.types.graph_arn
    import capo_detective.types.graph_arn_list
    import capo_detective.types.indicator_type
    import capo_detective.types.investigation_id
    import capo_detective.types.list_datasource_packages_request
    import capo_detective.types.list_datasource_packages_response
    import capo_detective.types.list_graphs_request
    import capo_detective.types.list_graphs_response
    import capo_detective.types.list_indicators_request
    import capo_detective.types.list_indicators_response
    import capo_detective.types.list_investigations_request
    import capo_detective.types.list_investigations_response
    import capo_detective.types.list_invitations_request
    import capo_detective.types.list_invitations_response
    import capo_detective.types.list_members_request
    import capo_detective.types.list_members_response
    import capo_detective.types.list_organization_admin_accounts_request
    import capo_detective.types.list_organization_admin_accounts_response
    import capo_detective.types.list_tags_for_resource_request
    import capo_detective.types.list_tags_for_resource_response
    import capo_detective.types.max_results
    import capo_detective.types.member_results_limit
    import capo_detective.types.pagination_token
    import capo_detective.types.reject_invitation_request
    import capo_detective.types.sort_criteria
    import capo_detective.types.start_investigation_request
    import capo_detective.types.start_investigation_response
    import capo_detective.types.start_monitoring_member_request
    import capo_detective.types.state
    import capo_detective.types.tag_key_list
    import capo_detective.types.tag_map
    import capo_detective.types.tag_resource_request
    import capo_detective.types.tag_resource_response
    import capo_detective.types.timestamp
    import capo_detective.types.untag_resource_request
    import capo_detective.types.untag_resource_response
    import capo_detective.types.update_datasource_packages_request
    import capo_detective.types.update_investigation_state_request
    import capo_detective.types.update_organization_configuration_request


class AsyncDetectiveClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncDetectiveClient:
    """A client for the ``Detective`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncDetectiveClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncDetectiveClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDetectiveClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def accept_invitation(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> None:
        """<p>Accepts an invitation for the member account to contribute data to a behavior graph. This operation can only be called by an invited member account. </p> <p>The request provides the ARN of behavior graph.</p> <p>The member account status in the graph must be <code>INVITED</code>.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph that the member account is accepting the invitation for.</p> <p>The member account status in the behavior graph must be <code>INVITED</code>.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.conflict_exception.ConflictException: <p>The request attempted an invalid action.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.accept_invitation_request.AcceptInvitationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.accept_invitation

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.accept_invitation.async_accept_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.accept_invitation_request.AcceptInvitationRequest = {
            "graph_arn": graph_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_graph_member_datasources(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        account_ids: "capo_detective.types.account_id_extended_list.AccountIdExtendedList",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.batch_get_graph_member_datasources_response.BatchGetGraphMemberDatasourcesResponse":
        """<p>Gets data source package information for the behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            account_ids: <p>The list of Amazon Web Services accounts to get data source package information on.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.batch_get_graph_member_datasources_request.BatchGetGraphMemberDatasourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.batch_get_graph_member_datasources_response.BatchGetGraphMemberDatasourcesResponse"
        ]:
            import capo_detective._operations.amazon_detective.batch_get_graph_member_datasources

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.batch_get_graph_member_datasources.async_batch_get_graph_member_datasources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.batch_get_graph_member_datasources_request.BatchGetGraphMemberDatasourcesRequest = {
            "graph_arn": graph_arn,
            "account_ids": account_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_membership_datasources(
        self,
        graph_arns: "capo_detective.types.graph_arn_list.GraphArnList",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.batch_get_membership_datasources_response.BatchGetMembershipDatasourcesResponse":
        """<p>Gets information on the data source package history for an account.</p>

        Args:
            graph_arns: <p>The ARN of the behavior graph.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.batch_get_membership_datasources_request.BatchGetMembershipDatasourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.batch_get_membership_datasources_response.BatchGetMembershipDatasourcesResponse"
        ]:
            import capo_detective._operations.amazon_detective.batch_get_membership_datasources

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.batch_get_membership_datasources.async_batch_get_membership_datasources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.batch_get_membership_datasources_request.BatchGetMembershipDatasourcesRequest = {
            "graph_arns": graph_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_graph(
        self,
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        tags: Optional["capo_detective.types.tag_map.TagMap"] = None,
    ) -> "capo_detective.types.create_graph_response.CreateGraphResponse":
        """<p>Creates a new behavior graph for the calling account, and sets that account as the administrator account. This operation is called by the account that is enabling Detective.</p> <p>The operation also enables Detective for the calling account in the currently selected Region. It returns the ARN of the new behavior graph.</p> <p> <code>CreateGraph</code> triggers a process to create the corresponding data tables for the new behavior graph.</p> <p>An account can only be the administrator account for one behavior graph within a Region. If the same account calls <code>CreateGraph</code> with the same administrator account, it always returns the same behavior graph ARN. It does not create a new behavior graph.</p>

        Args:
            tags: <p>The tags to assign to the new behavior graph. You can add up to 50 tags. For each tag, you provide the tag key and the tag value. Each tag key can contain up to 128 characters. Each tag value can contain up to 256 characters.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.conflict_exception.ConflictException: <p>The request attempted an invalid action.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request cannot be completed for one of the following reasons.</p> <ul> <li> <p>This request cannot be completed if it would cause the number of member accounts in the behavior graph to exceed the maximum allowed. A behavior graph cannot have more than 1,200 member accounts.</p> </li> <li> <p>This request cannot be completed if the current volume ingested is above the limit of 10 TB per day. Detective will not allow you to add additional member accounts.</p> </li> </ul>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.create_graph_request.CreateGraphRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.create_graph_response.CreateGraphResponse"
        ]:
            import capo_detective._operations.amazon_detective.create_graph

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.create_graph.async_create_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.create_graph_request.CreateGraphRequest = {}
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_members(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        accounts: "capo_detective.types.account_list.AccountList",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        message: Optional["capo_detective.types.email_message.EmailMessage"] = None,
        disable_email_notification: Optional[
            "capo_detective.types.boolean.Boolean"
        ] = None,
    ) -> "capo_detective.types.create_members_response.CreateMembersResponse":
        """<p> <code>CreateMembers</code> is used to send invitations to accounts. For the organization behavior graph, the Detective administrator account uses <code>CreateMembers</code> to enable organization accounts as member accounts.</p> <p>For invited accounts, <code>CreateMembers</code> sends a request to invite the specified Amazon Web Services accounts to be member accounts in the behavior graph. This operation can only be called by the administrator account for a behavior graph. </p> <p> <code>CreateMembers</code> verifies the accounts and then invites the verified accounts. The administrator can optionally specify to not send invitation emails to the member accounts. This would be used when the administrator manages their member accounts centrally.</p> <p>For organization accounts in the organization behavior graph, <code>CreateMembers</code> attempts to enable the accounts. The organization accounts do not receive invitations.</p> <p>The request provides the behavior graph ARN and the list of accounts to invite or to enable.</p> <p>The response separates the requested accounts into two lists:</p> <ul> <li> <p>The accounts that <code>CreateMembers</code> was able to process. For invited accounts, includes member accounts that are being verified, that have passed verification and are to be invited, and that have failed verification. For organization accounts in the organization behavior graph, includes accounts that can be enabled and that cannot be enabled.</p> </li> <li> <p>The accounts that <code>CreateMembers</code> was unable to process. This list includes accounts that were already invited to be member accounts in the behavior graph.</p> </li> </ul>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            message: <p>Customized message text to include in the invitation email message to the invited member accounts.</p>
            disable_email_notification: <p>if set to <code>true</code>, then the invited accounts do not receive email notifications. By default, this is set to <code>false</code>, and the invited accounts receive email notifications.</p> <p>Organization accounts in the organization behavior graph do not receive email notifications.</p>
            accounts: <p>The list of Amazon Web Services accounts to invite or to enable. You can invite or enable up to 50 accounts at a time. For each invited account, the account list contains the account identifier and the Amazon Web Services account root user email address. For organization accounts in the organization behavior graph, the email address is not required.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request cannot be completed for one of the following reasons.</p> <ul> <li> <p>This request cannot be completed if it would cause the number of member accounts in the behavior graph to exceed the maximum allowed. A behavior graph cannot have more than 1,200 member accounts.</p> </li> <li> <p>This request cannot be completed if the current volume ingested is above the limit of 10 TB per day. Detective will not allow you to add additional member accounts.</p> </li> </ul>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.create_members_request.CreateMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.create_members_response.CreateMembersResponse"
        ]:
            import capo_detective._operations.amazon_detective.create_members

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.create_members.async_create_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.create_members_request.CreateMembersRequest = {
            "graph_arn": graph_arn,
            "accounts": accounts,
        }
        if message is not None:
            input_["message"] = message
        if disable_email_notification is not None:
            input_["disable_email_notification"] = disable_email_notification

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_graph(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> None:
        """<p>Disables the specified behavior graph and queues it to be deleted. This operation removes the behavior graph from each member account's list of behavior graphs.</p> <p> <code>DeleteGraph</code> can only be called by the administrator account for a behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph to disable.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.delete_graph_request.DeleteGraphRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.delete_graph

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.delete_graph.async_delete_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.delete_graph_request.DeleteGraphRequest = {
            "graph_arn": graph_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_members(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        account_ids: "capo_detective.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.delete_members_response.DeleteMembersResponse":
        """<p>Removes the specified member accounts from the behavior graph. The removed accounts no longer contribute data to the behavior graph. This operation can only be called by the administrator account for the behavior graph.</p> <p>For invited accounts, the removed accounts are deleted from the list of accounts in the behavior graph. To restore the account, the administrator account must send another invitation.</p> <p>For organization accounts in the organization behavior graph, the Detective administrator account can always enable the organization account again. Organization accounts that are not enabled as member accounts are not included in the <code>ListMembers</code> results for the organization behavior graph.</p> <p>An administrator account cannot use <code>DeleteMembers</code> to remove their own account from the behavior graph. To disable a behavior graph, the administrator account uses the <code>DeleteGraph</code> API method.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph to remove members from.</p>
            account_ids: <p>The list of Amazon Web Services account identifiers for the member accounts to remove from the behavior graph. You can remove up to 50 member accounts at a time.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.conflict_exception.ConflictException: <p>The request attempted an invalid action.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.delete_members_request.DeleteMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.delete_members_response.DeleteMembersResponse"
        ]:
            import capo_detective._operations.amazon_detective.delete_members

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.delete_members.async_delete_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.delete_members_request.DeleteMembersRequest = {
            "graph_arn": graph_arn,
            "account_ids": account_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_organization_configuration(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse":
        """<p>Returns information about the configuration for the organization behavior graph. Currently indicates whether to automatically enable new organization accounts as member accounts.</p> <p>Can only be called by the Detective administrator account for the organization. </p>

        Args:
            graph_arn: <p>The ARN of the organization behavior graph.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse"
        ]:
            import capo_detective._operations.amazon_detective.describe_organization_configuration

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.describe_organization_configuration.async_describe_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest = {
            "graph_arn": graph_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_organization_admin_account(
        self, *, config_overrides: Optional[AsyncDetectiveClientConfig] = None
    ) -> None:
        """<p>Removes the Detective administrator account in the current Region. Deletes the organization behavior graph.</p> <p>Can only be called by the organization management account.</p> <p>Removing the Detective administrator account does not affect the delegated administrator account for Detective in Organizations.</p> <p>To remove the delegated administrator account in Organizations, use the Organizations API. Removing the delegated administrator account also removes the Detective administrator account in all Regions, except for Regions where the Detective administrator account is the organization management account.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.disable_organization_admin_account

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.disable_organization_admin_account.async_disable_organization_admin_account(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_membership(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> None:
        """<p>Removes the member account from the specified behavior graph. This operation can only be called by an invited member account that has the <code>ENABLED</code> status.</p> <p> <code>DisassociateMembership</code> cannot be called by an organization account in the organization behavior graph. For the organization behavior graph, the Detective administrator account determines which organization accounts to enable or disable as member accounts.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph to remove the member account from.</p> <p>The member account's member status in the behavior graph must be <code>ENABLED</code>.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.conflict_exception.ConflictException: <p>The request attempted an invalid action.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.disassociate_membership_request.DisassociateMembershipRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.disassociate_membership

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.disassociate_membership.async_disassociate_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.disassociate_membership_request.DisassociateMembershipRequest = {
            "graph_arn": graph_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_organization_admin_account(
        self,
        account_id: "capo_detective.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> None:
        """<p>Designates the Detective administrator account for the organization in the current Region.</p> <p>If the account does not have Detective enabled, then enables Detective for that account and creates a new behavior graph.</p> <p>Can only be called by the organization management account.</p> <p>If the organization has a delegated administrator account in Organizations, then the Detective administrator account must be either the delegated administrator account or the organization management account.</p> <p>If the organization does not have a delegated administrator account in Organizations, then you can choose any account in the organization. If you choose an account other than the organization management account, Detective calls Organizations to make that account the delegated administrator account for Detective. The organization management account cannot be the delegated administrator account.</p>

        Args:
            account_id: <p>The Amazon Web Services account identifier of the account to designate as the Detective administrator account for the organization.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.enable_organization_admin_account

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.enable_organization_admin_account.async_enable_organization_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_investigation(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        investigation_id: "capo_detective.types.investigation_id.InvestigationId",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.get_investigation_response.GetInvestigationResponse":
        """<p>Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. <code>GetInvestigation</code> returns the investigation results of an investigation for a behavior graph. </p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            investigation_id: <p>The investigation ID of the investigation report.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.get_investigation_request.GetInvestigationRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.get_investigation_response.GetInvestigationResponse"
        ]:
            import capo_detective._operations.amazon_detective.get_investigation

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.get_investigation.async_get_investigation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.get_investigation_request.GetInvestigationRequest = {
            "graph_arn": graph_arn,
            "investigation_id": investigation_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_members(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        account_ids: "capo_detective.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.get_members_response.GetMembersResponse":
        """<p>Returns the membership details for specified member accounts for a behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph for which to request the member details.</p>
            account_ids: <p>The list of Amazon Web Services account identifiers for the member account for which to return member details. You can request details for up to 50 member accounts at a time.</p> <p>You cannot use <code>GetMembers</code> to retrieve information about member accounts that were removed from the behavior graph.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.get_members_request.GetMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.get_members_response.GetMembersResponse"
        ]:
            import capo_detective._operations.amazon_detective.get_members

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.get_members.async_get_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.get_members_request.GetMembersRequest = {
            "graph_arn": graph_arn,
            "account_ids": account_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_datasource_packages(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "capo_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse":
        """<p>Lists data source packages in the behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            next_token: <p>For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.list_datasource_packages_request.ListDatasourcePackagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse"
        ]:
            import capo_detective._operations.amazon_detective.list_datasource_packages

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.list_datasource_packages.async_list_datasource_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.list_datasource_packages_request.ListDatasourcePackagesRequest = {
            "graph_arn": graph_arn
        }
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

    async def iter_list_datasource_packages(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "AsyncIterator[capo_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse]":
        _token = next_token
        while True:
            _response = await self.list_datasource_packages(
                graph_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_graphs(
        self,
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "capo_detective.types.list_graphs_response.ListGraphsResponse":
        """<p>Returns the list of behavior graphs that the calling account is an administrator account of. This operation can only be called by an administrator account.</p> <p>Because an account can currently only be the administrator of one behavior graph within a Region, the results always contain a single behavior graph.</p>

        Args:
            next_token: <p>For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of graphs to return at a time. The total must be less than the overall limit on the number of results to return, which is currently 200.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.list_graphs_request.ListGraphsRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.list_graphs_response.ListGraphsResponse"
        ]:
            import capo_detective._operations.amazon_detective.list_graphs

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.list_graphs.async_list_graphs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.list_graphs_request.ListGraphsRequest = {}
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

    async def iter_list_graphs(
        self,
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "AsyncIterator[capo_detective.types.list_graphs_response.ListGraphsResponse]":
        _token = next_token
        while True:
            _response = await self.list_graphs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_indicators(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        investigation_id: "capo_detective.types.investigation_id.InvestigationId",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        indicator_type: Optional[
            "capo_detective.types.indicator_type.IndicatorType"
        ] = None,
        next_token: Optional[
            "capo_detective.types.ai_pagination_token.AiPaginationToken"
        ] = None,
        max_results: Optional["capo_detective.types.max_results.MaxResults"] = None,
    ) -> "capo_detective.types.list_indicators_response.ListIndicatorsResponse":
        """<p>Gets the indicators from an investigation. You can use the information from the indicators to determine if an IAM user and/or IAM role is involved in an unusual activity that could indicate malicious behavior and its impact.</p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            investigation_id: <p>The investigation ID of the investigation report.</p>
            indicator_type: <p>For the list of indicators of compromise that are generated by Detective investigations, see <a href="https://docs.aws.amazon.com/detective/latest/userguide/detective-investigation-about.html">Detective investigations</a>.</p>
            next_token: <p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.</p>
            max_results: <p>Lists the maximum number of indicators in a page.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.list_indicators_request.ListIndicatorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.list_indicators_response.ListIndicatorsResponse"
        ]:
            import capo_detective._operations.amazon_detective.list_indicators

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.list_indicators.async_list_indicators(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.list_indicators_request.ListIndicatorsRequest = {
            "graph_arn": graph_arn,
            "investigation_id": investigation_id,
        }
        if indicator_type is not None:
            input_["indicator_type"] = indicator_type
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

    async def list_investigations(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.ai_pagination_token.AiPaginationToken"
        ] = None,
        max_results: Optional["capo_detective.types.max_results.MaxResults"] = None,
        filter_criteria: Optional[
            "capo_detective.types.filter_criteria.FilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "capo_detective.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "capo_detective.types.list_investigations_response.ListInvestigationsResponse":
        """<p>Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. <code>ListInvestigations</code> lists all active Detective investigations.</p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            next_token: <p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.</p>
            max_results: <p>Lists the maximum number of investigations in a page.</p>
            filter_criteria: <p>Filters the investigation results based on a criteria.</p>
            sort_criteria: <p>Sorts the investigation results based on a criteria.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.list_investigations_request.ListInvestigationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.list_investigations_response.ListInvestigationsResponse"
        ]:
            import capo_detective._operations.amazon_detective.list_investigations

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.list_investigations.async_list_investigations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.list_investigations_request.ListInvestigationsRequest = {
            "graph_arn": graph_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_invitations(
        self,
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "capo_detective.types.list_invitations_response.ListInvitationsResponse":
        """<p>Retrieves the list of open and accepted behavior graph invitations for the member account. This operation can only be called by an invited member account.</p> <p>Open invitations are invitations that the member account has not responded to.</p> <p>The results do not include behavior graphs for which the member account declined the invitation. The results also do not include behavior graphs that the member account resigned from or was removed from.</p>

        Args:
            next_token: <p>For requests to retrieve the next page of results, the pagination token that was returned with the previous page of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of behavior graph invitations to return in the response. The total must be less than the overall limit on the number of results to return, which is currently 200.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.list_invitations_request.ListInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.list_invitations_response.ListInvitationsResponse"
        ]:
            import capo_detective._operations.amazon_detective.list_invitations

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.list_invitations.async_list_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.list_invitations_request.ListInvitationsRequest = {}
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

    async def iter_list_invitations(
        self,
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "AsyncIterator[capo_detective.types.list_invitations_response.ListInvitationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_invitations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_members(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "capo_detective.types.list_members_response.ListMembersResponse":
        """<p>Retrieves the list of member accounts for a behavior graph.</p> <p>For invited accounts, the results do not include member accounts that were removed from the behavior graph.</p> <p>For the organization behavior graph, the results do not include organization accounts that the Detective administrator account has not enabled as member accounts.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph for which to retrieve the list of member accounts.</p>
            next_token: <p>For requests to retrieve the next page of member account results, the pagination token that was returned with the previous page of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of member accounts to include in the response. The total must be less than the overall limit on the number of results to return, which is currently 200.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.list_members_request.ListMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.list_members_response.ListMembersResponse"
        ]:
            import capo_detective._operations.amazon_detective.list_members

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.list_members.async_list_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.list_members_request.ListMembersRequest = {
            "graph_arn": graph_arn
        }
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

    async def iter_list_members(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> (
        "AsyncIterator[capo_detective.types.list_members_response.ListMembersResponse]"
    ):
        _token = next_token
        while True:
            _response = await self.list_members(
                graph_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "capo_detective.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse":
        """<p>Returns information about the Detective administrator account for an organization. Can only be called by the organization management account.</p>

        Args:
            next_token: <p>For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse"
        ]:
            import capo_detective._operations.amazon_detective.list_organization_admin_accounts

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.list_organization_admin_accounts.async_list_organization_admin_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest = {}
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

    async def iter_list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        next_token: Optional[
            "capo_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "AsyncIterator[capo_detective.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse]":
        _token = next_token
        while True:
            _response = await self.list_organization_admin_accounts(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns the tag values that are assigned to a behavior graph.</p>

        Args:
            resource_arn: <p>The ARN of the behavior graph for which to retrieve the tag values.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_detective._operations.amazon_detective.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_invitation(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> None:
        """<p>Rejects an invitation to contribute the account data to a behavior graph. This operation must be called by an invited member account that has the <code>INVITED</code> status.</p> <p> <code>RejectInvitation</code> cannot be called by an organization account in the organization behavior graph. In the organization behavior graph, organization accounts do not receive an invitation.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph to reject the invitation to.</p> <p>The member account's current member status in the behavior graph must be <code>INVITED</code>.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.conflict_exception.ConflictException: <p>The request attempted an invalid action.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.reject_invitation_request.RejectInvitationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.reject_invitation

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.reject_invitation.async_reject_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.reject_invitation_request.RejectInvitationRequest = {
            "graph_arn": graph_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_investigation(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        entity_arn: "capo_detective.types.entity_arn.EntityArn",
        scope_start_time: "capo_detective.types.timestamp.Timestamp",
        scope_end_time: "capo_detective.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.start_investigation_response.StartInvestigationResponse":
        """<p>Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. <code>StartInvestigation</code> initiates an investigation on an entity in a behavior graph. </p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            entity_arn: <p>The unique Amazon Resource Name (ARN) of the IAM user and IAM role.</p>
            scope_start_time: <p>The data and time when the investigation began. The value is an UTC ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>
            scope_end_time: <p>The data and time when the investigation ended. The value is an UTC ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.start_investigation_request.StartInvestigationRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.start_investigation_response.StartInvestigationResponse"
        ]:
            import capo_detective._operations.amazon_detective.start_investigation

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.start_investigation.async_start_investigation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.start_investigation_request.StartInvestigationRequest = {
            "graph_arn": graph_arn,
            "entity_arn": entity_arn,
            "scope_start_time": scope_start_time,
            "scope_end_time": scope_end_time,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_monitoring_member(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        account_id: "capo_detective.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> None:
        """<p>Sends a request to enable data ingest for a member account that has a status of <code>ACCEPTED_BUT_DISABLED</code>.</p> <p>For valid member accounts, the status is updated as follows.</p> <ul> <li> <p>If Detective enabled the member account, then the new status is <code>ENABLED</code>.</p> </li> <li> <p>If Detective cannot enable the member account, the status remains <code>ACCEPTED_BUT_DISABLED</code>. </p> </li> </ul>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            account_id: <p>The account ID of the member account to try to enable.</p> <p>The account must be an invited member account with a status of <code>ACCEPTED_BUT_DISABLED</code>. </p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.conflict_exception.ConflictException: <p>The request attempted an invalid action.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request cannot be completed for one of the following reasons.</p> <ul> <li> <p>This request cannot be completed if it would cause the number of member accounts in the behavior graph to exceed the maximum allowed. A behavior graph cannot have more than 1,200 member accounts.</p> </li> <li> <p>This request cannot be completed if the current volume ingested is above the limit of 10 TB per day. Detective will not allow you to add additional member accounts.</p> </li> </ul>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.start_monitoring_member_request.StartMonitoringMemberRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.start_monitoring_member

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.start_monitoring_member.async_start_monitoring_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.start_monitoring_member_request.StartMonitoringMemberRequest = {
            "graph_arn": graph_arn,
            "account_id": account_id,
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
        resource_arn: "capo_detective.types.graph_arn.GraphArn",
        tags: "capo_detective.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.tag_resource_response.TagResourceResponse":
        """<p>Applies tag values to a behavior graph.</p>

        Args:
            resource_arn: <p>The ARN of the behavior graph to assign the tags to.</p>
            tags: <p>The tags to assign to the behavior graph. You can add up to 50 tags. For each tag, you provide the tag key and the tag value. Each tag key can contain up to 128 characters. Each tag value can contain up to 256 characters.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_detective._operations.amazon_detective.tag_resource

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_detective.types.graph_arn.GraphArn",
        tag_keys: "capo_detective.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> "capo_detective.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a behavior graph.</p>

        Args:
            resource_arn: <p>The ARN of the behavior graph to remove the tags from.</p>
            tag_keys: <p>The tag keys of the tags to remove from the behavior graph. You can remove up to 50 tags at a time.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_detective.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_detective._operations.amazon_detective.untag_resource

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_datasource_packages(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        datasource_packages: "capo_detective.types.datasource_package_list.DatasourcePackageList",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> None:
        """<p>Starts a data source package for the Detective behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            datasource_packages: <p>The data source package to start for the behavior graph.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request cannot be completed for one of the following reasons.</p> <ul> <li> <p>This request cannot be completed if it would cause the number of member accounts in the behavior graph to exceed the maximum allowed. A behavior graph cannot have more than 1,200 member accounts.</p> </li> <li> <p>This request cannot be completed if the current volume ingested is above the limit of 10 TB per day. Detective will not allow you to add additional member accounts.</p> </li> </ul>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.update_datasource_packages_request.UpdateDatasourcePackagesRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.update_datasource_packages

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.update_datasource_packages.async_update_datasource_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.update_datasource_packages_request.UpdateDatasourcePackagesRequest = {
            "graph_arn": graph_arn,
            "datasource_packages": datasource_packages,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_investigation_state(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        investigation_id: "capo_detective.types.investigation_id.InvestigationId",
        state: "capo_detective.types.state.State",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
    ) -> None:
        """<p>Updates the state of an investigation.</p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            investigation_id: <p>The investigation ID of the investigation report.</p>
            state: <p>The current state of the investigation. An archived investigation indicates you have completed reviewing the investigation.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request refers to a nonexistent resource.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.update_investigation_state_request.UpdateInvestigationStateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.update_investigation_state

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.update_investigation_state.async_update_investigation_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.update_investigation_state_request.UpdateInvestigationStateRequest = {
            "graph_arn": graph_arn,
            "investigation_id": investigation_id,
            "state": state,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_organization_configuration(
        self,
        graph_arn: "capo_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[AsyncDetectiveClientConfig] = None,
        auto_enable: Optional["capo_detective.types.boolean.Boolean"] = None,
    ) -> None:
        """<p>Updates the configuration for the Organizations integration in the current Region. Can only be called by the Detective administrator account for the organization.</p>

        Args:
            graph_arn: <p>The ARN of the organization behavior graph.</p>
            auto_enable: <p>Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.</p>

        Raises:
            capo_detective.errors.access_denied_exception.AccessDeniedException: <p>The request issuer does not have permission to access this resource or perform this operation.</p>
            capo_detective.errors.internal_server_exception.InternalServerException: <p>The request was valid but failed because of a problem with the service.</p>
            capo_detective.errors.too_many_requests_exception.TooManyRequestsException: <p>The request cannot be completed because too many other requests are occurring at the same time.</p>
            capo_detective.errors.validation_exception.ValidationException: <p>The request parameters are invalid.</p>
            capo_detective.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_detective.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_detective._operations.amazon_detective.update_organization_configuration

            (
                output,
                http_response,
            ) = await capo_detective._operations.amazon_detective.update_organization_configuration.async_update_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_detective.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest = {
            "graph_arn": graph_arn
        }
        if auto_enable is not None:
            input_["auto_enable"] = auto_enable

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
