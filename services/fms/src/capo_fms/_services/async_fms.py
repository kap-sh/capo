"""Generated from Smithy shape ``com.amazonaws.fms#AWSFMS_20180101``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_fms._auth._signers
import capo_fms._auth._sigv4
from capo_fms._auth._identity import Credentials
from capo_fms._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_fms._auth._zapros_handler import AuthMiddleware
from capo_fms._pagination import resolve_path as _resolve_path
from capo_fms._services._aws_config import aaws_config
from capo_fms._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_fms.types.admin_account_summary
    import capo_fms.types.admin_scope
    import capo_fms.types.apps_list_data
    import capo_fms.types.apps_list_data_summary
    import capo_fms.types.associate_admin_account_request
    import capo_fms.types.associate_third_party_firewall_request
    import capo_fms.types.associate_third_party_firewall_response
    import capo_fms.types.aws_account_id
    import capo_fms.types.aws_account_id_list
    import capo_fms.types.base62_id
    import capo_fms.types.batch_associate_resource_request
    import capo_fms.types.batch_associate_resource_response
    import capo_fms.types.batch_disassociate_resource_request
    import capo_fms.types.batch_disassociate_resource_response
    import capo_fms.types.boolean
    import capo_fms.types.delete_apps_list_request
    import capo_fms.types.delete_notification_channel_request
    import capo_fms.types.delete_policy_request
    import capo_fms.types.delete_protocols_list_request
    import capo_fms.types.delete_resource_set_request
    import capo_fms.types.disassociate_admin_account_request
    import capo_fms.types.disassociate_third_party_firewall_request
    import capo_fms.types.disassociate_third_party_firewall_response
    import capo_fms.types.get_admin_account_request
    import capo_fms.types.get_admin_account_response
    import capo_fms.types.get_admin_scope_request
    import capo_fms.types.get_admin_scope_response
    import capo_fms.types.get_apps_list_request
    import capo_fms.types.get_apps_list_response
    import capo_fms.types.get_compliance_detail_request
    import capo_fms.types.get_compliance_detail_response
    import capo_fms.types.get_notification_channel_request
    import capo_fms.types.get_notification_channel_response
    import capo_fms.types.get_policy_request
    import capo_fms.types.get_policy_response
    import capo_fms.types.get_protection_status_request
    import capo_fms.types.get_protection_status_response
    import capo_fms.types.get_protocols_list_request
    import capo_fms.types.get_protocols_list_response
    import capo_fms.types.get_resource_set_request
    import capo_fms.types.get_resource_set_response
    import capo_fms.types.get_third_party_firewall_association_status_request
    import capo_fms.types.get_third_party_firewall_association_status_response
    import capo_fms.types.get_violation_details_request
    import capo_fms.types.get_violation_details_response
    import capo_fms.types.identifier
    import capo_fms.types.identifier_list
    import capo_fms.types.list_admin_accounts_for_organization_request
    import capo_fms.types.list_admin_accounts_for_organization_response
    import capo_fms.types.list_admins_managing_account_request
    import capo_fms.types.list_admins_managing_account_response
    import capo_fms.types.list_apps_lists_request
    import capo_fms.types.list_apps_lists_response
    import capo_fms.types.list_compliance_status_request
    import capo_fms.types.list_compliance_status_response
    import capo_fms.types.list_discovered_resources_request
    import capo_fms.types.list_discovered_resources_response
    import capo_fms.types.list_id
    import capo_fms.types.list_member_accounts_request
    import capo_fms.types.list_member_accounts_response
    import capo_fms.types.list_policies_request
    import capo_fms.types.list_policies_response
    import capo_fms.types.list_protocols_lists_request
    import capo_fms.types.list_protocols_lists_response
    import capo_fms.types.list_resource_set_resources_request
    import capo_fms.types.list_resource_set_resources_response
    import capo_fms.types.list_resource_sets_request
    import capo_fms.types.list_resource_sets_response
    import capo_fms.types.list_tags_for_resource_request
    import capo_fms.types.list_tags_for_resource_response
    import capo_fms.types.list_third_party_firewall_firewall_policies_request
    import capo_fms.types.list_third_party_firewall_firewall_policies_response
    import capo_fms.types.pagination_max_results
    import capo_fms.types.pagination_token
    import capo_fms.types.policy
    import capo_fms.types.policy_compliance_status
    import capo_fms.types.policy_id
    import capo_fms.types.policy_summary
    import capo_fms.types.protocols_list_data
    import capo_fms.types.protocols_list_data_summary
    import capo_fms.types.put_admin_account_request
    import capo_fms.types.put_apps_list_request
    import capo_fms.types.put_apps_list_response
    import capo_fms.types.put_notification_channel_request
    import capo_fms.types.put_policy_request
    import capo_fms.types.put_policy_response
    import capo_fms.types.put_protocols_list_request
    import capo_fms.types.put_protocols_list_response
    import capo_fms.types.put_resource_set_request
    import capo_fms.types.put_resource_set_response
    import capo_fms.types.resource_arn
    import capo_fms.types.resource_id
    import capo_fms.types.resource_set
    import capo_fms.types.resource_type
    import capo_fms.types.tag_key_list
    import capo_fms.types.tag_list
    import capo_fms.types.tag_resource_request
    import capo_fms.types.tag_resource_response
    import capo_fms.types.third_party_firewall
    import capo_fms.types.third_party_firewall_firewall_policy
    import capo_fms.types.time_stamp
    import capo_fms.types.untag_resource_request
    import capo_fms.types.untag_resource_response


class AsyncFMSClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncFMSClient:
    """A client for the ``FMS`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AsyncFMSClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncFMSClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncFMSClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def associate_admin_account(
        self,
        admin_account: "capo_fms.types.aws_account_id.AWSAccountId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> None:
        """<p>Sets a Firewall Manager default administrator account. The Firewall Manager default administrator account can manage third-party firewalls and has full administrative scope that allows administration of all policy types, accounts, organizational units, and Regions. This account must be a member account of the organization in Organizations whose resources you want to protect.</p> <p>For information about working with Firewall Manager administrator accounts, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/fms-administrators.html">Managing Firewall Manager administrators</a> in the <i>Firewall Manager Developer Guide</i>.</p>

        Args:
            admin_account: <p>The Amazon Web Services account ID to associate with Firewall Manager as the Firewall Manager default administrator account. This account must be a member account of the organization in Organizations whose resources you want to protect. For more information about Organizations, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html">Managing the Amazon Web Services Accounts in Your Organization</a>. </p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.associate_admin_account_request.AssociateAdminAccountRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_fms._operations.awsfms_20180101.associate_admin_account

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.associate_admin_account.async_associate_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.associate_admin_account_request.AssociateAdminAccountRequest = {
            "admin_account": admin_account
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_third_party_firewall(
        self,
        third_party_firewall: "capo_fms.types.third_party_firewall.ThirdPartyFirewall",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.associate_third_party_firewall_response.AssociateThirdPartyFirewallResponse":
        """<p>Sets the Firewall Manager policy administrator as a tenant administrator of a third-party firewall service. A tenant is an instance of the third-party firewall service that's associated with your Amazon Web Services customer account.</p>

        Args:
            third_party_firewall: <p>The name of the third-party firewall vendor.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.associate_third_party_firewall_request.AssociateThirdPartyFirewallRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.associate_third_party_firewall_response.AssociateThirdPartyFirewallResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.associate_third_party_firewall

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.associate_third_party_firewall.async_associate_third_party_firewall(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.associate_third_party_firewall_request.AssociateThirdPartyFirewallRequest = {
            "third_party_firewall": third_party_firewall
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_associate_resource(
        self,
        resource_set_identifier: "capo_fms.types.identifier.Identifier",
        items: "capo_fms.types.identifier_list.IdentifierList",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.batch_associate_resource_response.BatchAssociateResourceResponse":
        """<p>Associate resources to a Firewall Manager resource set.</p>

        Args:
            resource_set_identifier: <p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>
            items: <p>The uniform resource identifiers (URIs) of resources that should be associated to the resource set. The URIs must be Amazon Resource Names (ARNs).</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.batch_associate_resource_request.BatchAssociateResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.batch_associate_resource_response.BatchAssociateResourceResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.batch_associate_resource

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.batch_associate_resource.async_batch_associate_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.batch_associate_resource_request.BatchAssociateResourceRequest = {
            "resource_set_identifier": resource_set_identifier,
            "items": items,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_disassociate_resource(
        self,
        resource_set_identifier: "capo_fms.types.identifier.Identifier",
        items: "capo_fms.types.identifier_list.IdentifierList",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.batch_disassociate_resource_response.BatchDisassociateResourceResponse":
        """<p>Disassociates resources from a Firewall Manager resource set.</p>

        Args:
            resource_set_identifier: <p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>
            items: <p>The uniform resource identifiers (URI) of resources that should be disassociated from the resource set. The URIs must be Amazon Resource Names (ARNs).</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.batch_disassociate_resource_request.BatchDisassociateResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.batch_disassociate_resource_response.BatchDisassociateResourceResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.batch_disassociate_resource

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.batch_disassociate_resource.async_batch_disassociate_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.batch_disassociate_resource_request.BatchDisassociateResourceRequest = {
            "resource_set_identifier": resource_set_identifier,
            "items": items,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_apps_list(
        self,
        list_id: "capo_fms.types.list_id.ListId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> None:
        """<p>Permanently deletes an Firewall Manager applications list.</p>

        Args:
            list_id: <p>The ID of the applications list that you want to delete. You can retrieve this ID from <code>PutAppsList</code>, <code>ListAppsLists</code>, and <code>GetAppsList</code>.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.delete_apps_list_request.DeleteAppsListRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_fms._operations.awsfms_20180101.delete_apps_list

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.delete_apps_list.async_delete_apps_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.delete_apps_list_request.DeleteAppsListRequest = {
            "list_id": list_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_notification_channel(
        self, *, config_overrides: Optional[AsyncFMSClientConfig] = None
    ) -> None:
        """<p>Deletes an Firewall Manager association with the IAM role and the Amazon Simple Notification Service (SNS) topic that is used to record Firewall Manager SNS logs.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.delete_notification_channel_request.DeleteNotificationChannelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_fms._operations.awsfms_20180101.delete_notification_channel

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.delete_notification_channel.async_delete_notification_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.delete_notification_channel_request.DeleteNotificationChannelRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_policy(
        self,
        policy_id: "capo_fms.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        delete_all_policy_resources: Optional["capo_fms.types.boolean.Boolean"] = None,
    ) -> None:
        """<p>Permanently deletes an Firewall Manager policy. </p>

        Args:
            policy_id: <p>The ID of the policy that you want to delete. You can retrieve this ID from <code>PutPolicy</code> and <code>ListPolicies</code>.</p>
            delete_all_policy_resources: <p>If <code>True</code>, the request performs cleanup according to the policy type. </p> <p>For WAF and Shield Advanced policies, the cleanup does the following:</p> <ul> <li> <p>Deletes rule groups created by Firewall Manager</p> </li> <li> <p>Removes web ACLs from in-scope resources</p> </li> <li> <p>Deletes web ACLs that contain no rules or rule groups</p> </li> </ul> <p>For security group policies, the cleanup does the following for each security group in the policy:</p> <ul> <li> <p>Disassociates the security group from in-scope resources </p> </li> <li> <p>Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy</p> </li> </ul> <note> <p>For security group common policies, even if set to <code>False</code>, Firewall Manager deletes all security groups created by Firewall Manager that aren't associated with any other resources through another policy.</p> </note> <p>After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope. </p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.delete_policy_request.DeletePolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_fms._operations.awsfms_20180101.delete_policy

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.delete_policy.async_delete_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.delete_policy_request.DeletePolicyRequest = {
            "policy_id": policy_id
        }
        if delete_all_policy_resources is not None:
            input_["delete_all_policy_resources"] = delete_all_policy_resources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_protocols_list(
        self,
        list_id: "capo_fms.types.list_id.ListId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> None:
        """<p>Permanently deletes an Firewall Manager protocols list.</p>

        Args:
            list_id: <p>The ID of the protocols list that you want to delete. You can retrieve this ID from <code>PutProtocolsList</code>, <code>ListProtocolsLists</code>, and <code>GetProtocolsLost</code>.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.delete_protocols_list_request.DeleteProtocolsListRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_fms._operations.awsfms_20180101.delete_protocols_list

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.delete_protocols_list.async_delete_protocols_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.delete_protocols_list_request.DeleteProtocolsListRequest = {
            "list_id": list_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_set(
        self,
        identifier: "capo_fms.types.base62_id.Base62Id",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <a>ResourceSet</a>.</p>

        Args:
            identifier: <p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.delete_resource_set_request.DeleteResourceSetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_fms._operations.awsfms_20180101.delete_resource_set

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.delete_resource_set.async_delete_resource_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.delete_resource_set_request.DeleteResourceSetRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_admin_account(
        self, *, config_overrides: Optional[AsyncFMSClientConfig] = None
    ) -> None:
        """<p>Disassociates an Firewall Manager administrator account. To set a different account as an Firewall Manager administrator, submit a <a>PutAdminAccount</a> request. To set an account as a default administrator account, you must submit an <a>AssociateAdminAccount</a> request.</p> <p>Disassociation of the default administrator account follows the first in, last out principle. If you are the default administrator, all Firewall Manager administrators within the organization must first disassociate their accounts before you can disassociate your account.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.disassociate_admin_account_request.DisassociateAdminAccountRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_fms._operations.awsfms_20180101.disassociate_admin_account

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.disassociate_admin_account.async_disassociate_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.disassociate_admin_account_request.DisassociateAdminAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_third_party_firewall(
        self,
        third_party_firewall: "capo_fms.types.third_party_firewall.ThirdPartyFirewall",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.disassociate_third_party_firewall_response.DisassociateThirdPartyFirewallResponse":
        """<p>Disassociates a Firewall Manager policy administrator from a third-party firewall tenant. When you call <code>DisassociateThirdPartyFirewall</code>, the third-party firewall vendor deletes all of the firewalls that are associated with the account.</p>

        Args:
            third_party_firewall: <p>The name of the third-party firewall vendor.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.disassociate_third_party_firewall_request.DisassociateThirdPartyFirewallRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.disassociate_third_party_firewall_response.DisassociateThirdPartyFirewallResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.disassociate_third_party_firewall

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.disassociate_third_party_firewall.async_disassociate_third_party_firewall(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.disassociate_third_party_firewall_request.DisassociateThirdPartyFirewallRequest = {
            "third_party_firewall": third_party_firewall
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_admin_account(
        self, *, config_overrides: Optional[AsyncFMSClientConfig] = None
    ) -> "capo_fms.types.get_admin_account_response.GetAdminAccountResponse":
        """<p>Returns the Organizations account that is associated with Firewall Manager as the Firewall Manager default administrator.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_admin_account_request.GetAdminAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_admin_account_response.GetAdminAccountResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_admin_account

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_admin_account.async_get_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_admin_account_request.GetAdminAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_admin_scope(
        self,
        admin_account: "capo_fms.types.aws_account_id.AWSAccountId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.get_admin_scope_response.GetAdminScopeResponse":
        """<p>Returns information about the specified account's administrative scope. The administrative scope defines the resources that an Firewall Manager administrator can manage.</p>

        Args:
            admin_account: <p>The administrator account that you want to get the details for.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_admin_scope_request.GetAdminScopeRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_admin_scope_response.GetAdminScopeResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_admin_scope

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_admin_scope.async_get_admin_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_admin_scope_request.GetAdminScopeRequest = {
            "admin_account": admin_account
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_apps_list(
        self,
        list_id: "capo_fms.types.list_id.ListId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        default_list: Optional["capo_fms.types.boolean.Boolean"] = None,
    ) -> "capo_fms.types.get_apps_list_response.GetAppsListResponse":
        """<p>Returns information about the specified Firewall Manager applications list.</p>

        Args:
            list_id: <p>The ID of the Firewall Manager applications list that you want the details for.</p>
            default_list: <p>Specifies whether the list to retrieve is a default list owned by Firewall Manager.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_apps_list_request.GetAppsListRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_apps_list_response.GetAppsListResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_apps_list

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_apps_list.async_get_apps_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_apps_list_request.GetAppsListRequest = {
            "list_id": list_id
        }
        if default_list is not None:
            input_["default_list"] = default_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_compliance_detail(
        self,
        policy_id: "capo_fms.types.policy_id.PolicyId",
        member_account: "capo_fms.types.aws_account_id.AWSAccountId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.get_compliance_detail_response.GetComplianceDetailResponse":
        """<p>Returns detailed compliance information about the specified member account. Details include resources that are in and out of compliance with the specified policy. </p> <p>The reasons for resources being considered compliant depend on the Firewall Manager policy type. </p>

        Args:
            policy_id: <p>The ID of the policy that you want to get the details for. <code>PolicyId</code> is returned by <code>PutPolicy</code> and by <code>ListPolicies</code>.</p>
            member_account: <p>The Amazon Web Services account that owns the resources that you want to get the details for.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_compliance_detail_request.GetComplianceDetailRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_compliance_detail_response.GetComplianceDetailResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_compliance_detail

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_compliance_detail.async_get_compliance_detail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_compliance_detail_request.GetComplianceDetailRequest = {
            "policy_id": policy_id,
            "member_account": member_account,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_notification_channel(
        self, *, config_overrides: Optional[AsyncFMSClientConfig] = None
    ) -> "capo_fms.types.get_notification_channel_response.GetNotificationChannelResponse":
        """<p>Information about the Amazon Simple Notification Service (SNS) topic that is used to record Firewall Manager SNS logs.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_notification_channel_request.GetNotificationChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_notification_channel_response.GetNotificationChannelResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_notification_channel

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_notification_channel.async_get_notification_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_notification_channel_request.GetNotificationChannelRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_policy(
        self,
        policy_id: "capo_fms.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.get_policy_response.GetPolicyResponse":
        """<p>Returns information about the specified Firewall Manager policy.</p>

        Args:
            policy_id: <p>The ID of the Firewall Manager policy that you want the details for.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.invalid_type_exception.InvalidTypeException: <p>The value of the <code>Type</code> parameter is invalid.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_policy_request.GetPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_policy

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_policy.async_get_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_policy_request.GetPolicyRequest = {
            "policy_id": policy_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_protection_status(
        self,
        policy_id: "capo_fms.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        member_account_id: Optional[
            "capo_fms.types.aws_account_id.AWSAccountId"
        ] = None,
        start_time: Optional["capo_fms.types.time_stamp.TimeStamp"] = None,
        end_time: Optional["capo_fms.types.time_stamp.TimeStamp"] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_fms.types.get_protection_status_response.GetProtectionStatusResponse":
        """<p>If you created a Shield Advanced policy, returns policy-level attack summary information in the event of a potential DDoS attack. Other policy types are currently unsupported.</p>

        Args:
            policy_id: <p>The ID of the policy for which you want to get the attack information.</p>
            member_account_id: <p>The Amazon Web Services account that is in scope of the policy that you want to get the details for.</p>
            start_time: <p>The start of the time period to query for the attacks. This is a <code>timestamp</code> type. The request syntax listing indicates a <code>number</code> type because the default used by Firewall Manager is Unix time in seconds. However, any valid <code>timestamp</code> format is allowed.</p>
            end_time: <p>The end of the time period to query for the attacks. This is a <code>timestamp</code> type. The request syntax listing indicates a <code>number</code> type because the default used by Firewall Manager is Unix time in seconds. However, any valid <code>timestamp</code> format is allowed.</p>
            next_token: <p>If you specify a value for <code>MaxResults</code> and you have more objects than the number that you specify for <code>MaxResults</code>, Firewall Manager returns a <code>NextToken</code> value in the response, which you can use to retrieve another group of objects. For the second and subsequent <code>GetProtectionStatus</code> requests, specify the value of <code>NextToken</code> from the previous response to get information about another batch of objects.</p>
            max_results: <p>Specifies the number of objects that you want Firewall Manager to return for this request. If you have more objects than the number that you specify for <code>MaxResults</code>, the response includes a <code>NextToken</code> value that you can use to get another batch of objects.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_protection_status_request.GetProtectionStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_protection_status_response.GetProtectionStatusResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_protection_status

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_protection_status.async_get_protection_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_protection_status_request.GetProtectionStatusRequest = {
            "policy_id": policy_id
        }
        if member_account_id is not None:
            input_["member_account_id"] = member_account_id
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
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

    async def get_protocols_list(
        self,
        list_id: "capo_fms.types.list_id.ListId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        default_list: Optional["capo_fms.types.boolean.Boolean"] = None,
    ) -> "capo_fms.types.get_protocols_list_response.GetProtocolsListResponse":
        """<p>Returns information about the specified Firewall Manager protocols list.</p>

        Args:
            list_id: <p>The ID of the Firewall Manager protocols list that you want the details for.</p>
            default_list: <p>Specifies whether the list to retrieve is a default list owned by Firewall Manager.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_protocols_list_request.GetProtocolsListRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_protocols_list_response.GetProtocolsListResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_protocols_list

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_protocols_list.async_get_protocols_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_protocols_list_request.GetProtocolsListRequest = {
            "list_id": list_id
        }
        if default_list is not None:
            input_["default_list"] = default_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_set(
        self,
        identifier: "capo_fms.types.base62_id.Base62Id",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.get_resource_set_response.GetResourceSetResponse":
        """<p>Gets information about a specific resource set.</p>

        Args:
            identifier: <p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_resource_set_request.GetResourceSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_resource_set_response.GetResourceSetResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_resource_set

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_resource_set.async_get_resource_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_resource_set_request.GetResourceSetRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_third_party_firewall_association_status(
        self,
        third_party_firewall: "capo_fms.types.third_party_firewall.ThirdPartyFirewall",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.get_third_party_firewall_association_status_response.GetThirdPartyFirewallAssociationStatusResponse":
        """<p>The onboarding status of a Firewall Manager admin account to third-party firewall vendor tenant.</p>

        Args:
            third_party_firewall: <p>The name of the third-party firewall vendor.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_third_party_firewall_association_status_request.GetThirdPartyFirewallAssociationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_third_party_firewall_association_status_response.GetThirdPartyFirewallAssociationStatusResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_third_party_firewall_association_status

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_third_party_firewall_association_status.async_get_third_party_firewall_association_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_third_party_firewall_association_status_request.GetThirdPartyFirewallAssociationStatusRequest = {
            "third_party_firewall": third_party_firewall
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_violation_details(
        self,
        policy_id: "capo_fms.types.policy_id.PolicyId",
        member_account: "capo_fms.types.aws_account_id.AWSAccountId",
        resource_id: "capo_fms.types.resource_id.ResourceId",
        resource_type: "capo_fms.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.get_violation_details_response.GetViolationDetailsResponse":
        """<p>Retrieves violations for a resource based on the specified Firewall Manager policy and Amazon Web Services account.</p>

        Args:
            policy_id: <p>The ID of the Firewall Manager policy that you want the details for. You can get violation details for the following policy types:</p> <ul> <li> <p>WAF</p> </li> <li> <p>DNS Firewall</p> </li> <li> <p>Imported Network Firewall</p> </li> <li> <p>Network Firewall</p> </li> <li> <p>Security group content audit</p> </li> <li> <p>Network ACL</p> </li> <li> <p>Third-party firewall</p> </li> </ul>
            member_account: <p>The Amazon Web Services account ID that you want the details for.</p>
            resource_id: <p>The ID of the resource that has violations.</p>
            resource_type: <p>The resource type. This is in the format shown in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services Resource Types Reference</a>. Supported resource types are: <code>AWS::WAFv2::WebACL</code>, <code>AWS::EC2::Instance</code>, <code>AWS::EC2::NetworkInterface</code>, <code>AWS::EC2::SecurityGroup</code>, <code>AWS::NetworkFirewall::FirewallPolicy</code>, and <code>AWS::EC2::Subnet</code>. </p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.get_violation_details_request.GetViolationDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.get_violation_details_response.GetViolationDetailsResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.get_violation_details

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.get_violation_details.async_get_violation_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.get_violation_details_request.GetViolationDetailsRequest = {
            "policy_id": policy_id,
            "member_account": member_account,
            "resource_id": resource_id,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_admin_accounts_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_fms.types.list_admin_accounts_for_organization_response.ListAdminAccountsForOrganizationResponse":
        """<p>Returns a <code>AdminAccounts</code> object that lists the Firewall Manager administrators within the organization that are onboarded to Firewall Manager by <a>AssociateAdminAccount</a>.</p> <p>This operation can be called only from the organization's management account.</p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_admin_accounts_for_organization_request.ListAdminAccountsForOrganizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_admin_accounts_for_organization_response.ListAdminAccountsForOrganizationResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_admin_accounts_for_organization

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_admin_accounts_for_organization.async_list_admin_accounts_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_admin_accounts_for_organization_request.ListAdminAccountsForOrganizationRequest = {}
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

    async def iter_list_admin_accounts_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_fms.types.admin_account_summary.AdminAccountSummary]":
        _token = next_token
        while True:
            _response = await self.list_admin_accounts_for_organization(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("admin_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_admins_managing_account(
        self,
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_fms.types.list_admins_managing_account_response.ListAdminsManagingAccountResponse":
        """<p>Lists the accounts that are managing the specified Organizations member account. This is useful for any member account so that they can view the accounts who are managing their account. This operation only returns the managing administrators that have the requested account within their <a>AdminScope</a>.</p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_admins_managing_account_request.ListAdminsManagingAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_admins_managing_account_response.ListAdminsManagingAccountResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_admins_managing_account

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_admins_managing_account.async_list_admins_managing_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_admins_managing_account_request.ListAdminsManagingAccountRequest = {}
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

    async def iter_list_admins_managing_account(
        self,
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_fms.types.aws_account_id.AWSAccountId]":
        _token = next_token
        while True:
            _response = await self.list_admins_managing_account(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("admin_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_apps_lists(
        self,
        max_results: "capo_fms.types.pagination_max_results.PaginationMaxResults",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        default_lists: Optional["capo_fms.types.boolean.Boolean"] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_fms.types.list_apps_lists_response.ListAppsListsResponse":
        """<p>Returns an array of <code>AppsListDataSummary</code> objects.</p>

        Args:
            default_lists: <p>Specifies whether the lists to retrieve are default lists owned by Firewall Manager.</p>
            next_token: <p>If you specify a value for <code>MaxResults</code> in your list request, and you have more objects than the maximum, Firewall Manager returns this token in the response. For all but the first request, you provide the token returned by the prior request in the request parameters, to retrieve the next batch of objects.</p>
            max_results: <p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify this, Firewall Manager returns all available objects.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_apps_lists_request.ListAppsListsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_apps_lists_response.ListAppsListsResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_apps_lists

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_apps_lists.async_list_apps_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_apps_lists_request.ListAppsListsRequest = {
            "max_results": max_results
        }
        if default_lists is not None:
            input_["default_lists"] = default_lists
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_apps_lists(
        self,
        max_results: "capo_fms.types.pagination_max_results.PaginationMaxResults",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        default_lists: Optional["capo_fms.types.boolean.Boolean"] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_fms.types.apps_list_data_summary.AppsListDataSummary]":
        _token = next_token
        while True:
            _response = await self.list_apps_lists(
                max_results,
                config_overrides=config_overrides,
                default_lists=default_lists,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("apps_lists",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_compliance_status(
        self,
        policy_id: "capo_fms.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_fms.types.list_compliance_status_response.ListComplianceStatusResponse":
        """<p>Returns an array of <code>PolicyComplianceStatus</code> objects. Use <code>PolicyComplianceStatus</code> to get a summary of which member accounts are protected by the specified policy. </p>

        Args:
            policy_id: <p>The ID of the Firewall Manager policy that you want the details for.</p>
            next_token: <p>If you specify a value for <code>MaxResults</code> and you have more <code>PolicyComplianceStatus</code> objects than the number that you specify for <code>MaxResults</code>, Firewall Manager returns a <code>NextToken</code> value in the response that allows you to list another group of <code>PolicyComplianceStatus</code> objects. For the second and subsequent <code>ListComplianceStatus</code> requests, specify the value of <code>NextToken</code> from the previous response to get information about another batch of <code>PolicyComplianceStatus</code> objects.</p>
            max_results: <p>Specifies the number of <code>PolicyComplianceStatus</code> objects that you want Firewall Manager to return for this request. If you have more <code>PolicyComplianceStatus</code> objects than the number that you specify for <code>MaxResults</code>, the response includes a <code>NextToken</code> value that you can use to get another batch of <code>PolicyComplianceStatus</code> objects.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_compliance_status_request.ListComplianceStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_compliance_status_response.ListComplianceStatusResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_compliance_status

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_compliance_status.async_list_compliance_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_compliance_status_request.ListComplianceStatusRequest = {
            "policy_id": policy_id
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

    async def iter_list_compliance_status(
        self,
        policy_id: "capo_fms.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> (
        "AsyncIterator[capo_fms.types.policy_compliance_status.PolicyComplianceStatus]"
    ):
        _token = next_token
        while True:
            _response = await self.list_compliance_status(
                policy_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_compliance_status_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_discovered_resources(
        self,
        member_account_ids: "capo_fms.types.aws_account_id_list.AWSAccountIdList",
        resource_type: "capo_fms.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_fms.types.list_discovered_resources_response.ListDiscoveredResourcesResponse":
        """<p>Returns an array of resources in the organization's accounts that are available to be associated with a resource set.</p>

        Args:
            member_account_ids: <p>The Amazon Web Services account IDs to discover resources in. Only one account is supported per request. The account must be a member of your organization.</p>
            resource_type: <p>The type of resources to discover.</p>
            max_results: <p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_discovered_resources_request.ListDiscoveredResourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_discovered_resources_response.ListDiscoveredResourcesResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_discovered_resources

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_discovered_resources.async_list_discovered_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_discovered_resources_request.ListDiscoveredResourcesRequest = {
            "member_account_ids": member_account_ids,
            "resource_type": resource_type,
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

    async def list_member_accounts(
        self,
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_fms.types.list_member_accounts_response.ListMemberAccountsResponse":
        """<p>Returns a <code>MemberAccounts</code> object that lists the member accounts in the administrator's Amazon Web Services organization.</p> <p>Either an Firewall Manager administrator or the organization's management account can make this request.</p>

        Args:
            next_token: <p>If you specify a value for <code>MaxResults</code> and you have more account IDs than the number that you specify for <code>MaxResults</code>, Firewall Manager returns a <code>NextToken</code> value in the response that allows you to list another group of IDs. For the second and subsequent <code>ListMemberAccountsRequest</code> requests, specify the value of <code>NextToken</code> from the previous response to get information about another batch of member account IDs.</p>
            max_results: <p>Specifies the number of member account IDs that you want Firewall Manager to return for this request. If you have more IDs than the number that you specify for <code>MaxResults</code>, the response includes a <code>NextToken</code> value that you can use to get another batch of member account IDs.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_member_accounts_request.ListMemberAccountsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_member_accounts_response.ListMemberAccountsResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_member_accounts

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_member_accounts.async_list_member_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_member_accounts_request.ListMemberAccountsRequest = {}
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

    async def iter_list_member_accounts(
        self,
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_fms.types.aws_account_id.AWSAccountId]":
        _token = next_token
        while True:
            _response = await self.list_member_accounts(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("member_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_policies(
        self,
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_fms.types.list_policies_response.ListPoliciesResponse":
        """<p>Returns an array of <code>PolicySummary</code> objects.</p>

        Args:
            next_token: <p>If you specify a value for <code>MaxResults</code> and you have more <code>PolicySummary</code> objects than the number that you specify for <code>MaxResults</code>, Firewall Manager returns a <code>NextToken</code> value in the response that allows you to list another group of <code>PolicySummary</code> objects. For the second and subsequent <code>ListPolicies</code> requests, specify the value of <code>NextToken</code> from the previous response to get information about another batch of <code>PolicySummary</code> objects.</p>
            max_results: <p>Specifies the number of <code>PolicySummary</code> objects that you want Firewall Manager to return for this request. If you have more <code>PolicySummary</code> objects than the number that you specify for <code>MaxResults</code>, the response includes a <code>NextToken</code> value that you can use to get another batch of <code>PolicySummary</code> objects.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_policies_request.ListPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_policies_response.ListPoliciesResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_policies

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_policies.async_list_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_policies_request.ListPoliciesRequest = {}
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

    async def iter_list_policies(
        self,
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_fms.types.policy_summary.PolicySummary]":
        _token = next_token
        while True:
            _response = await self.list_policies(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_protocols_lists(
        self,
        max_results: "capo_fms.types.pagination_max_results.PaginationMaxResults",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        default_lists: Optional["capo_fms.types.boolean.Boolean"] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_fms.types.list_protocols_lists_response.ListProtocolsListsResponse":
        """<p>Returns an array of <code>ProtocolsListDataSummary</code> objects.</p>

        Args:
            default_lists: <p>Specifies whether the lists to retrieve are default lists owned by Firewall Manager.</p>
            next_token: <p>If you specify a value for <code>MaxResults</code> in your list request, and you have more objects than the maximum, Firewall Manager returns this token in the response. For all but the first request, you provide the token returned by the prior request in the request parameters, to retrieve the next batch of objects.</p>
            max_results: <p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify this, Firewall Manager returns all available objects.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_protocols_lists_request.ListProtocolsListsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_protocols_lists_response.ListProtocolsListsResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_protocols_lists

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_protocols_lists.async_list_protocols_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_protocols_lists_request.ListProtocolsListsRequest = {
            "max_results": max_results
        }
        if default_lists is not None:
            input_["default_lists"] = default_lists
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_protocols_lists(
        self,
        max_results: "capo_fms.types.pagination_max_results.PaginationMaxResults",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        default_lists: Optional["capo_fms.types.boolean.Boolean"] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_fms.types.protocols_list_data_summary.ProtocolsListDataSummary]":
        _token = next_token
        while True:
            _response = await self.list_protocols_lists(
                max_results,
                config_overrides=config_overrides,
                default_lists=default_lists,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("protocols_lists",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_set_resources(
        self,
        identifier: "capo_fms.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_fms.types.list_resource_set_resources_response.ListResourceSetResourcesResponse":
        """<p>Returns an array of resources that are currently associated to a resource set.</p>

        Args:
            identifier: <p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>
            max_results: <p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_resource_set_resources_request.ListResourceSetResourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_resource_set_resources_response.ListResourceSetResourcesResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_resource_set_resources

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_resource_set_resources.async_list_resource_set_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_resource_set_resources_request.ListResourceSetResourcesRequest = {
            "identifier": identifier
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

    async def list_resource_sets(
        self,
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_fms.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_fms.types.list_resource_sets_response.ListResourceSetsResponse":
        """<p>Returns an array of <code>ResourceSetSummary</code> objects.</p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_resource_sets_request.ListResourceSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_resource_sets_response.ListResourceSetsResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_resource_sets

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_resource_sets.async_list_resource_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_resource_sets_request.ListResourceSetsRequest = {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_fms.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the list of tags for the specified Amazon Web Services resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to return tags for. The Firewall Manager resources that support tagging are policies, applications lists, and protocols lists. </p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_third_party_firewall_firewall_policies(
        self,
        third_party_firewall: "capo_fms.types.third_party_firewall.ThirdPartyFirewall",
        max_results: "capo_fms.types.pagination_max_results.PaginationMaxResults",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_fms.types.list_third_party_firewall_firewall_policies_response.ListThirdPartyFirewallFirewallPoliciesResponse":
        """<p>Retrieves a list of all of the third-party firewall policies that are associated with the third-party firewall administrator's account.</p>

        Args:
            third_party_firewall: <p>The name of the third-party firewall vendor.</p>
            next_token: <p>If the previous response included a <code>NextToken</code> element, the specified third-party firewall vendor is associated with more third-party firewall policies. To get more third-party firewall policies, submit another <code>ListThirdPartyFirewallFirewallPoliciesRequest</code> request.</p> <p> For the value of <code>NextToken</code>, specify the value of <code>NextToken</code> from the previous response. If the previous response didn't include a <code>NextToken</code> element, there are no more third-party firewall policies to get. </p>
            max_results: <p>The maximum number of third-party firewall policies that you want Firewall Manager to return. If the specified third-party firewall vendor is associated with more than <code>MaxResults</code> firewall policies, the response includes a <code>NextToken</code> element. <code>NextToken</code> contains an encrypted token that identifies the first third-party firewall policies that Firewall Manager will return if you submit another request.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.list_third_party_firewall_firewall_policies_request.ListThirdPartyFirewallFirewallPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.list_third_party_firewall_firewall_policies_response.ListThirdPartyFirewallFirewallPoliciesResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.list_third_party_firewall_firewall_policies

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.list_third_party_firewall_firewall_policies.async_list_third_party_firewall_firewall_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.list_third_party_firewall_firewall_policies_request.ListThirdPartyFirewallFirewallPoliciesRequest = {
            "third_party_firewall": third_party_firewall,
            "max_results": max_results,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_third_party_firewall_firewall_policies(
        self,
        third_party_firewall: "capo_fms.types.third_party_firewall.ThirdPartyFirewall",
        max_results: "capo_fms.types.pagination_max_results.PaginationMaxResults",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        next_token: Optional["capo_fms.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_fms.types.third_party_firewall_firewall_policy.ThirdPartyFirewallFirewallPolicy]":
        _token = next_token
        while True:
            _response = await self.list_third_party_firewall_firewall_policies(
                third_party_firewall,
                max_results,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("third_party_firewall_firewall_policies",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_admin_account(
        self,
        admin_account: "capo_fms.types.aws_account_id.AWSAccountId",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        admin_scope: Optional["capo_fms.types.admin_scope.AdminScope"] = None,
    ) -> None:
        """<p>Creates or updates an Firewall Manager administrator account. The account must be a member of the organization that was onboarded to Firewall Manager by <a>AssociateAdminAccount</a>. Only the organization's management account can create an Firewall Manager administrator account. When you create an Firewall Manager administrator account, the service checks to see if the account is already a delegated administrator within Organizations. If the account isn't a delegated administrator, Firewall Manager calls Organizations to delegate the account within Organizations. For more information about administrator accounts within Organizations, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html">Managing the Amazon Web Services Accounts in Your Organization</a>.</p>

        Args:
            admin_account: <p>The Amazon Web Services account ID to add as an Firewall Manager administrator account. The account must be a member of the organization that was onboarded to Firewall Manager by <a>AssociateAdminAccount</a>. For more information about Organizations, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html">Managing the Amazon Web Services Accounts in Your Organization</a>.</p>
            admin_scope: <p>Configures the resources that the specified Firewall Manager administrator can manage. As a best practice, set the administrative scope according to the principles of least privilege. Only grant the administrator the specific resources or permissions that they need to perform the duties of their role.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.put_admin_account_request.PutAdminAccountRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_fms._operations.awsfms_20180101.put_admin_account

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.put_admin_account.async_put_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.put_admin_account_request.PutAdminAccountRequest = {
            "admin_account": admin_account
        }
        if admin_scope is not None:
            input_["admin_scope"] = admin_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_apps_list(
        self,
        apps_list: "capo_fms.types.apps_list_data.AppsListData",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        tag_list: Optional["capo_fms.types.tag_list.TagList"] = None,
    ) -> "capo_fms.types.put_apps_list_response.PutAppsListResponse":
        """<p>Creates an Firewall Manager applications list.</p>

        Args:
            apps_list: <p>The details of the Firewall Manager applications list to be created.</p>
            tag_list: <p>The tags associated with the resource.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.put_apps_list_request.PutAppsListRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.put_apps_list_response.PutAppsListResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.put_apps_list

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.put_apps_list.async_put_apps_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.put_apps_list_request.PutAppsListRequest = {
            "apps_list": apps_list
        }
        if tag_list is not None:
            input_["tag_list"] = tag_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_notification_channel(
        self,
        sns_topic_arn: "capo_fms.types.resource_arn.ResourceArn",
        sns_role_name: "capo_fms.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> None:
        """<p>Designates the IAM role and Amazon Simple Notification Service (SNS) topic that Firewall Manager uses to record SNS logs.</p> <p>To perform this action outside of the console, you must first configure the SNS topic's access policy to allow the <code>SnsRoleName</code> to publish SNS logs. If the <code>SnsRoleName</code> provided is a role other than the <code>AWSServiceRoleForFMS</code> service-linked role, this role must have a trust relationship configured to allow the Firewall Manager service principal <code>fms.amazonaws.com</code> to assume this role. For information about configuring an SNS access policy, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-security_iam_service-with-iam.html#fms-security_iam_service-with-iam-roles-service">Service roles for Firewall Manager</a> in the <i>Firewall Manager Developer Guide</i>.</p>

        Args:
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the SNS topic that collects notifications from Firewall Manager.</p>
            sns_role_name: <p>The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record Firewall Manager activity. </p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.put_notification_channel_request.PutNotificationChannelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_fms._operations.awsfms_20180101.put_notification_channel

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.put_notification_channel.async_put_notification_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.put_notification_channel_request.PutNotificationChannelRequest = {
            "sns_topic_arn": sns_topic_arn,
            "sns_role_name": sns_role_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_policy(
        self,
        policy: "capo_fms.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        tag_list: Optional["capo_fms.types.tag_list.TagList"] = None,
    ) -> "capo_fms.types.put_policy_response.PutPolicyResponse":
        """<p>Creates an Firewall Manager policy.</p> <p>A Firewall Manager policy is specific to the individual policy type. If you want to enforce multiple policy types across accounts, you can create multiple policies. You can create more than one policy for each type. </p> <p>If you add a new account to an organization that you created with Organizations, Firewall Manager automatically applies the policy to the resources in that account that are within scope of the policy. </p> <p>Firewall Manager provides the following types of policies: </p> <ul> <li> <p> <b>WAF policy</b> - This policy applies WAF web ACL protections to specified accounts and resources. </p> </li> <li> <p> <b>Shield Advanced policy</b> - This policy applies Shield Advanced protection to specified accounts and resources. </p> </li> <li> <p> <b>Security Groups policy</b> - This type of policy gives you control over security groups that are in use throughout your organization in Organizations and lets you enforce a baseline set of rules across your organization. </p> </li> <li> <p> <b>Network ACL policy</b> - This type of policy gives you control over the network ACLs that are in use throughout your organization in Organizations and lets you enforce a baseline set of first and last network ACL rules across your organization. </p> </li> <li> <p> <b>Network Firewall policy</b> - This policy applies Network Firewall protection to your organization's VPCs. </p> </li> <li> <p> <b>DNS Firewall policy</b> - This policy applies Amazon Route 53 Resolver DNS Firewall protections to your organization's VPCs. </p> </li> <li> <p> <b>Third-party firewall policy</b> - This policy applies third-party firewall protections. Third-party firewalls are available by subscription through the Amazon Web Services Marketplace console at <a href="http://aws.amazon.com/marketplace">Amazon Web Services Marketplace</a>.</p> <ul> <li> <p> <b>Palo Alto Networks Cloud NGFW policy</b> - This policy applies Palo Alto Networks Cloud Next Generation Firewall (NGFW) protections and Palo Alto Networks Cloud NGFW rulestacks to your organization's VPCs.</p> </li> <li> <p> <b>Fortigate CNF policy</b> - This policy applies Fortigate Cloud Native Firewall (CNF) protections. Fortigate CNF is a cloud-centered solution that blocks Zero-Day threats and secures cloud infrastructures with industry-leading advanced threat prevention, smart web application firewalls (WAF), and API protection.</p> </li> </ul> </li> </ul>

        Args:
            policy: <p>The details of the Firewall Manager policy to be created.</p>
            tag_list: <p>The tags to add to the Amazon Web Services resource.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.invalid_type_exception.InvalidTypeException: <p>The value of the <code>Type</code> parameter is invalid.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.put_policy_request.PutPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.put_policy_response.PutPolicyResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.put_policy

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.put_policy.async_put_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.put_policy_request.PutPolicyRequest = {"policy": policy}
        if tag_list is not None:
            input_["tag_list"] = tag_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_protocols_list(
        self,
        protocols_list: "capo_fms.types.protocols_list_data.ProtocolsListData",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        tag_list: Optional["capo_fms.types.tag_list.TagList"] = None,
    ) -> "capo_fms.types.put_protocols_list_response.PutProtocolsListResponse":
        """<p>Creates an Firewall Manager protocols list.</p>

        Args:
            protocols_list: <p>The details of the Firewall Manager protocols list to be created.</p>
            tag_list: <p>The tags associated with the resource.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.put_protocols_list_request.PutProtocolsListRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.put_protocols_list_response.PutProtocolsListResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.put_protocols_list

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.put_protocols_list.async_put_protocols_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.put_protocols_list_request.PutProtocolsListRequest = {
            "protocols_list": protocols_list
        }
        if tag_list is not None:
            input_["tag_list"] = tag_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_set(
        self,
        resource_set: "capo_fms.types.resource_set.ResourceSet",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
        tag_list: Optional["capo_fms.types.tag_list.TagList"] = None,
    ) -> "capo_fms.types.put_resource_set_response.PutResourceSetResponse":
        """<p>Creates the resource set.</p> <p>An Firewall Manager resource set defines the resources to import into an Firewall Manager policy from another Amazon Web Services service.</p>

        Args:
            resource_set: <p>Details about the resource set to be created or updated.></p>
            tag_list: <p>Retrieves the tags associated with the specified resource set. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.put_resource_set_request.PutResourceSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.put_resource_set_response.PutResourceSetResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.put_resource_set

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.put_resource_set.async_put_resource_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.put_resource_set_request.PutResourceSetRequest = {
            "resource_set": resource_set
        }
        if tag_list is not None:
            input_["tag_list"] = tag_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_fms.types.resource_arn.ResourceArn",
        tag_list: "capo_fms.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to an Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to return tags for. The Firewall Manager resources that support tagging are policies, applications lists, and protocols lists. </p>
            tag_list: <p>The tags to add to the resource.</p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.limit_exceeded_exception.LimitExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>policy</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html">Firewall Manager Limits</a> in the <i>WAF Developer Guide</i>.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.tag_resource

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_list": tag_list,
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
        resource_arn: "capo_fms.types.resource_arn.ResourceArn",
        tag_keys: "capo_fms.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncFMSClientConfig] = None,
    ) -> "capo_fms.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from an Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to return tags for. The Firewall Manager resources that support tagging are policies, applications lists, and protocols lists. </p>
            tag_keys: <p>The keys of the tags to remove from the resource. </p>

        Raises:
            capo_fms.errors.internal_error_exception.InternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_fms.errors.invalid_input_exception.InvalidInputException: <p>The parameters of the request were invalid.</p>
            capo_fms.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an <code>AssociateAdminAccount</code> request for an account ID that was already set as the Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for Organizations before you can access it.</p>
            capo_fms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_fms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fms.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_fms.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_fms._operations.awsfms_20180101.untag_resource

            (
                output,
                http_response,
            ) = await capo_fms._operations.awsfms_20180101.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fms.types.untag_resource_request.UntagResourceRequest = {
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
