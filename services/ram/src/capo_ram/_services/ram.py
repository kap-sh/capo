"""Generated from Smithy shape ``com.amazonaws.ram#AmazonResourceSharing``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_ram._auth._signers
import capo_ram._auth._sigv4
from capo_ram._auth._identity import Credentials
from capo_ram._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ram._auth._zapros_handler import AuthMiddleware
from capo_ram._pagination import resolve_path as _resolve_path
from capo_ram._services._aws_config import aws_config
from capo_ram._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ram.types.accept_resource_share_invitation_request
    import capo_ram.types.accept_resource_share_invitation_response
    import capo_ram.types.associate_resource_share_permission_request
    import capo_ram.types.associate_resource_share_permission_response
    import capo_ram.types.associate_resource_share_request
    import capo_ram.types.associate_resource_share_response
    import capo_ram.types.associated_source
    import capo_ram.types.boolean
    import capo_ram.types.create_permission_request
    import capo_ram.types.create_permission_response
    import capo_ram.types.create_permission_version_request
    import capo_ram.types.create_permission_version_response
    import capo_ram.types.create_resource_share_request
    import capo_ram.types.create_resource_share_response
    import capo_ram.types.delete_permission_request
    import capo_ram.types.delete_permission_response
    import capo_ram.types.delete_permission_version_request
    import capo_ram.types.delete_permission_version_response
    import capo_ram.types.delete_resource_share_request
    import capo_ram.types.delete_resource_share_response
    import capo_ram.types.disassociate_resource_share_permission_request
    import capo_ram.types.disassociate_resource_share_permission_response
    import capo_ram.types.disassociate_resource_share_request
    import capo_ram.types.disassociate_resource_share_response
    import capo_ram.types.enable_sharing_with_aws_organization_request
    import capo_ram.types.enable_sharing_with_aws_organization_response
    import capo_ram.types.get_permission_request
    import capo_ram.types.get_permission_response
    import capo_ram.types.get_resource_policies_request
    import capo_ram.types.get_resource_policies_response
    import capo_ram.types.get_resource_share_associations_request
    import capo_ram.types.get_resource_share_associations_response
    import capo_ram.types.get_resource_share_invitations_request
    import capo_ram.types.get_resource_share_invitations_response
    import capo_ram.types.get_resource_shares_request
    import capo_ram.types.get_resource_shares_response
    import capo_ram.types.integer
    import capo_ram.types.list_pending_invitation_resources_request
    import capo_ram.types.list_pending_invitation_resources_response
    import capo_ram.types.list_permission_associations_request
    import capo_ram.types.list_permission_associations_response
    import capo_ram.types.list_permission_versions_request
    import capo_ram.types.list_permission_versions_response
    import capo_ram.types.list_permissions_request
    import capo_ram.types.list_permissions_response
    import capo_ram.types.list_principals_request
    import capo_ram.types.list_principals_response
    import capo_ram.types.list_replace_permission_associations_work_request
    import capo_ram.types.list_replace_permission_associations_work_response
    import capo_ram.types.list_resource_share_permissions_request
    import capo_ram.types.list_resource_share_permissions_response
    import capo_ram.types.list_resource_types_request
    import capo_ram.types.list_resource_types_response
    import capo_ram.types.list_resources_request
    import capo_ram.types.list_resources_response
    import capo_ram.types.list_source_associations_request
    import capo_ram.types.list_source_associations_response
    import capo_ram.types.max_results
    import capo_ram.types.permission_arn_list
    import capo_ram.types.permission_feature_set
    import capo_ram.types.permission_name
    import capo_ram.types.permission_type_filter
    import capo_ram.types.policy
    import capo_ram.types.principal_arn_or_id_list
    import capo_ram.types.promote_permission_created_from_policy_request
    import capo_ram.types.promote_permission_created_from_policy_response
    import capo_ram.types.promote_resource_share_created_from_policy_request
    import capo_ram.types.promote_resource_share_created_from_policy_response
    import capo_ram.types.reject_resource_share_invitation_request
    import capo_ram.types.reject_resource_share_invitation_response
    import capo_ram.types.replace_permission_associations_request
    import capo_ram.types.replace_permission_associations_response
    import capo_ram.types.replace_permission_associations_work_id_list
    import capo_ram.types.replace_permission_associations_work_status
    import capo_ram.types.resource_arn_list
    import capo_ram.types.resource_owner
    import capo_ram.types.resource_region_scope_filter
    import capo_ram.types.resource_share_arn_list
    import capo_ram.types.resource_share_association_status
    import capo_ram.types.resource_share_association_type
    import capo_ram.types.resource_share_configuration
    import capo_ram.types.resource_share_invitation_arn_list
    import capo_ram.types.resource_share_status
    import capo_ram.types.set_default_permission_version_request
    import capo_ram.types.set_default_permission_version_response
    import capo_ram.types.source_arn_or_account_list
    import capo_ram.types.string
    import capo_ram.types.tag_filters
    import capo_ram.types.tag_key_list
    import capo_ram.types.tag_list
    import capo_ram.types.tag_resource_request
    import capo_ram.types.tag_resource_response
    import capo_ram.types.untag_resource_request
    import capo_ram.types.untag_resource_response
    import capo_ram.types.update_resource_share_request
    import capo_ram.types.update_resource_share_response


class RAMClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class RAMClient:
    """A client for the ``RAM`` service.

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
        self._config = RAMClientConfig(
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
        self, config_overrides: Optional[RAMClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: RAMClientConfig = config_overrides or {}
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

    def accept_resource_share_invitation(
        self,
        resource_share_invitation_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.accept_resource_share_invitation_response.AcceptResourceShareInvitationResponse":
        """<p>Accepts an invitation to a resource share from another Amazon Web Services account. After you accept the invitation, the resources included in the resource share are available to interact with in the relevant Amazon Web Services Management Consoles and tools.</p>

        Args:
            resource_share_invitation_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the invitation that you want to accept.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.resource_share_invitation_already_accepted_exception.ResourceShareInvitationAlreadyAcceptedException: <p>The operation failed because the specified invitation was already accepted.</p>
            capo_ram.errors.resource_share_invitation_already_rejected_exception.ResourceShareInvitationAlreadyRejectedException: <p>The operation failed because the specified invitation was already rejected.</p>
            capo_ram.errors.resource_share_invitation_arn_not_found_exception.ResourceShareInvitationArnNotFoundException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> for an invitation was not found.</p>
            capo_ram.errors.resource_share_invitation_expired_exception.ResourceShareInvitationExpiredException: <p>The operation failed because the specified invitation is past its expiration date and time.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.accept_resource_share_invitation_request.AcceptResourceShareInvitationRequest]",
        ) -> OperationResponse[
            "capo_ram.types.accept_resource_share_invitation_response.AcceptResourceShareInvitationResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.accept_resource_share_invitation

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.accept_resource_share_invitation.accept_resource_share_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.accept_resource_share_invitation_request.AcceptResourceShareInvitationRequest = {
            "resource_share_invitation_arn": resource_share_invitation_arn
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_resource_share(
        self,
        resource_share_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_arns: Optional[
            "capo_ram.types.resource_arn_list.ResourceArnList"
        ] = None,
        principals: Optional[
            "capo_ram.types.principal_arn_or_id_list.PrincipalArnOrIdList"
        ] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
        sources: Optional[
            "capo_ram.types.source_arn_or_account_list.SourceArnOrAccountList"
        ] = None,
    ) -> "capo_ram.types.associate_resource_share_response.AssociateResourceShareResponse":
        """<p>Adds the specified list of principals, resources, and source constraints to a resource share. Principals that already have access to this resource share immediately receive access to the added resources. Newly added principals immediately receive access to the resources shared in this resource share. </p>

        Args:
            resource_share_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to add principals or resources to.</p>
            resource_arns: <p>Specifies a list of <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> of the resources that you want to share. This can be <code>null</code> if you want to add only principals.</p>
            principals: <p>Specifies a list of principals to whom you want to the resource share. This can be <code>null</code> if you want to add only resources.</p> <p>What the principals can do with the resources in the share is determined by the RAM permissions that you associate with the resource share. See <a>AssociateResourceSharePermission</a>.</p> <p>You can include the following values:</p> <ul> <li> <p>An Amazon Web Services account ID, for example: <code>123456789012</code> </p> </li> <li> <p>An <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an organization in Organizations, for example: <code>organizations::123456789012:organization/o-exampleorgid</code> </p> </li> <li> <p>An ARN of an organizational unit (OU) in Organizations, for example: <code>organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123</code> </p> </li> <li> <p>An ARN of an IAM role, for example: <code>iam::123456789012:role/rolename</code> </p> </li> <li> <p>An ARN of an IAM user, for example: <code>iam::123456789012user/username</code> </p> </li> <li> <p>A service principal name, for example: <code>service-id.amazonaws.com</code> </p> </li> </ul> <note> <p>Not all resource types can be shared with IAM roles and users. For more information, see <a href="https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types">Sharing with IAM roles and users</a> in the <i>Resource Access Manager User Guide</i>.</p> </note>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            sources: <p>Specifies source constraints (accounts, ARNs, organization IDs, or organization paths) that limit when service principals can access resources in this resource share. When a service principal attempts to access a shared resource, validation is performed to ensure the request originates from one of the specified sources. This helps prevent confused deputy attacks by applying constraints on where service principals can access resources from.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_state_transition_exception.InvalidStateTransitionException: <p>The operation failed because the requested operation isn't valid for the resource share in its current state.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.resource_share_limit_exceeded_exception.ResourceShareLimitExceededException: <p>The operation failed because it would exceed the limit for resource shares for your account. You can associate up to 100 resources per call. To view the limits for your Amazon Web Services account, see the <a href="https://console.aws.amazon.com/servicequotas/home/services/ram/quotas">RAM page in the Service Quotas console</a>.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.throttling_exception.ThrottlingException: <p>The operation failed because it exceeded the rate at which you are allowed to perform this operation. Please try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.associate_resource_share_request.AssociateResourceShareRequest]",
        ) -> OperationResponse[
            "capo_ram.types.associate_resource_share_response.AssociateResourceShareResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.associate_resource_share

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.associate_resource_share.associate_resource_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.associate_resource_share_request.AssociateResourceShareRequest = {
            "resource_share_arn": resource_share_arn
        }
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if principals is not None:
            input_["principals"] = principals
        if client_token is not None:
            input_["client_token"] = client_token
        if sources is not None:
            input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_resource_share_permission(
        self,
        resource_share_arn: "capo_ram.types.string.String",
        permission_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        replace: Optional["capo_ram.types.boolean.Boolean"] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
        permission_version: Optional["capo_ram.types.integer.Integer"] = None,
    ) -> "capo_ram.types.associate_resource_share_permission_response.AssociateResourceSharePermissionResponse":
        """<p>Adds or replaces the RAM permission for a resource type included in a resource share. You can have exactly one permission associated with each resource type in the resource share. You can add a new RAM permission only if there are currently no resources of that resource type currently in the resource share.</p>

        Args:
            resource_share_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share to which you want to add or replace permissions.</p>
            permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the RAM permission to associate with the resource share. To find the ARN for a permission, use either the <a>ListPermissions</a> operation or go to the <a href="https://console.aws.amazon.com/ram/home#Permissions:">Permissions library</a> page in the RAM console and then choose the name of the permission. The ARN is displayed on the detail page.</p>
            replace: <p>Specifies whether the specified permission should replace the existing permission associated with the resource share. Use <code>true</code> to replace the current permissions. Use <code>false</code> to add the permission to a resource share that currently doesn't have a permission. The default value is <code>false</code>.</p> <note> <p>A resource share can have only one permission per resource type. If a resource share already has a permission for the specified resource type and you don't set <code>replace</code> to <code>true</code> then the operation returns an error. This helps prevent accidental overwriting of a permission.</p> </note>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            permission_version: <p>Specifies the version of the RAM permission to associate with the resource share. You can specify <i>only</i> the version that is currently set as the default version for the permission. If you also set the <code>replace</code> pararameter to <code>true</code>, then this operation updates an outdated version of the permission to the current default version.</p> <note> <p>You don't need to specify this parameter because the default behavior is to use the version that is currently set as the default version for the permission. This parameter is supported for backwards compatibility.</p> </note>

        Raises:
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.associate_resource_share_permission_request.AssociateResourceSharePermissionRequest]",
        ) -> OperationResponse[
            "capo_ram.types.associate_resource_share_permission_response.AssociateResourceSharePermissionResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.associate_resource_share_permission

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.associate_resource_share_permission.associate_resource_share_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.associate_resource_share_permission_request.AssociateResourceSharePermissionRequest = {
            "resource_share_arn": resource_share_arn,
            "permission_arn": permission_arn,
        }
        if replace is not None:
            input_["replace"] = replace
        if client_token is not None:
            input_["client_token"] = client_token
        if permission_version is not None:
            input_["permission_version"] = permission_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_permission(
        self,
        name: "capo_ram.types.permission_name.PermissionName",
        resource_type: "capo_ram.types.string.String",
        policy_template: "capo_ram.types.policy.Policy",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
        tags: Optional["capo_ram.types.tag_list.TagList"] = None,
    ) -> "capo_ram.types.create_permission_response.CreatePermissionResponse":
        """<p>Creates a customer managed permission for a specified resource type that you can attach to resource shares. It is created in the Amazon Web Services Region in which you call the operation.</p>

        Args:
            name: <p>Specifies the name of the customer managed permission. The name must be unique within the Amazon Web Services Region.</p>
            resource_type: <p>Specifies the name of the resource type that this customer managed permission applies to.</p> <p>The format is <code> <i><service-code></i>:<i><resource-type></i> </code> and is case sensitive. For example, to specify an Amazon EC2 Subnet, you can use the string <code>ec2:Subnet</code>. To see the list of valid values for this parameter, query the <a>ListResourceTypes</a> operation. This value must match the display name of the resource (available in <code>ListResourceTypes</code>).</p>
            policy_template: <p>A string in JSON format string that contains the following elements of a resource-based policy:</p> <ul> <li> <p> <b>Effect</b>: must be set to <code>ALLOW</code>.</p> </li> <li> <p> <b>Action</b>: specifies the actions that are allowed by this customer managed permission. The list must contain only actions that are supported by the specified resource type. For a list of all actions supported by each resource type, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html">Actions, resources, and condition keys for Amazon Web Services services</a> in the <i>Identity and Access Management User Guide</i>.</p> </li> <li> <p> <b>Condition</b>: (optional) specifies conditional parameters that must evaluate to true when a user attempts an action for that action to be allowed. For more information about the Condition element, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html">IAM policies: Condition element</a> in the <i>Identity and Access Management User Guide</i>.</p> </li> </ul> <p>This template can't include either the <code>Resource</code> or <code>Principal</code> elements. Those are both filled in by RAM when it instantiates the resource-based policy on each resource shared using this managed permission. The <code>Resource</code> comes from the ARN of the specific resource that you are sharing. The <code>Principal</code> comes from the list of identities added to the resource share.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            tags: <p>Specifies a list of one or more tag key and value pairs to attach to the permission.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_policy_exception.InvalidPolicyException: <p>The operation failed because a policy you specified isn't valid.</p>
            capo_ram.errors.malformed_policy_template_exception.MalformedPolicyTemplateException: <p>The operation failed because the policy template that you provided isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.permission_already_exists_exception.PermissionAlreadyExistsException: <p>The operation failed because a permission with the specified name already exists in the requested Amazon Web Services Region. Choose a different name.</p>
            capo_ram.errors.permission_limit_exceeded_exception.PermissionLimitExceededException: <p>The operation failed because it would exceed the maximum number of permissions you can create in each Amazon Web Services Region. To view the limits for your Amazon Web Services account, see the <a href="https://console.aws.amazon.com/servicequotas/home/services/ram/quotas">RAM page in the Service Quotas console</a>.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.create_permission_request.CreatePermissionRequest]",
        ) -> OperationResponse[
            "capo_ram.types.create_permission_response.CreatePermissionResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.create_permission

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.create_permission.create_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.create_permission_request.CreatePermissionRequest = {
            "name": name,
            "resource_type": resource_type,
            "policy_template": policy_template,
        }
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_permission_version(
        self,
        permission_arn: "capo_ram.types.string.String",
        policy_template: "capo_ram.types.policy.Policy",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.create_permission_version_response.CreatePermissionVersionResponse":
        """<p>Creates a new version of the specified customer managed permission. The new version is automatically set as the default version of the customer managed permission. New resource shares automatically use the default permission. Existing resource shares continue to use their original permission versions, but you can use <a>ReplacePermissionAssociations</a> to update them.</p> <p>If the specified customer managed permission already has the maximum of 5 versions, then you must delete one of the existing versions before you can create a new one.</p>

        Args:
            permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the customer managed permission you're creating a new version for.</p>
            policy_template: <p>A string in JSON format string that contains the following elements of a resource-based policy:</p> <ul> <li> <p> <b>Effect</b>: must be set to <code>ALLOW</code>.</p> </li> <li> <p> <b>Action</b>: specifies the actions that are allowed by this customer managed permission. The list must contain only actions that are supported by the specified resource type. For a list of all actions supported by each resource type, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html">Actions, resources, and condition keys for Amazon Web Services services</a> in the <i>Identity and Access Management User Guide</i>.</p> </li> <li> <p> <b>Condition</b>: (optional) specifies conditional parameters that must evaluate to true when a user attempts an action for that action to be allowed. For more information about the Condition element, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html">IAM policies: Condition element</a> in the <i>Identity and Access Management User Guide</i>.</p> </li> </ul> <p>This template can't include either the <code>Resource</code> or <code>Principal</code> elements. Those are both filled in by RAM when it instantiates the resource-based policy on each resource shared using this managed permission. The <code>Resource</code> comes from the ARN of the specific resource that you are sharing. The <code>Principal</code> comes from the list of identities added to the resource share.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_policy_exception.InvalidPolicyException: <p>The operation failed because a policy you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.malformed_policy_template_exception.MalformedPolicyTemplateException: <p>The operation failed because the policy template that you provided isn't valid.</p>
            capo_ram.errors.permission_versions_limit_exceeded_exception.PermissionVersionsLimitExceededException: <p>The operation failed because it would exceed the limit for the number of versions you can have for a permission. To view the limits for your Amazon Web Services account, see the <a href="https://console.aws.amazon.com/servicequotas/home/services/ram/quotas">RAM page in the Service Quotas console</a>.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.create_permission_version_request.CreatePermissionVersionRequest]",
        ) -> OperationResponse[
            "capo_ram.types.create_permission_version_response.CreatePermissionVersionResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.create_permission_version

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.create_permission_version.create_permission_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.create_permission_version_request.CreatePermissionVersionRequest = {
            "permission_arn": permission_arn,
            "policy_template": policy_template,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_resource_share(
        self,
        name: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_arns: Optional[
            "capo_ram.types.resource_arn_list.ResourceArnList"
        ] = None,
        principals: Optional[
            "capo_ram.types.principal_arn_or_id_list.PrincipalArnOrIdList"
        ] = None,
        tags: Optional["capo_ram.types.tag_list.TagList"] = None,
        allow_external_principals: Optional["capo_ram.types.boolean.Boolean"] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
        permission_arns: Optional[
            "capo_ram.types.permission_arn_list.PermissionArnList"
        ] = None,
        sources: Optional[
            "capo_ram.types.source_arn_or_account_list.SourceArnOrAccountList"
        ] = None,
        resource_share_configuration: Optional[
            "capo_ram.types.resource_share_configuration.ResourceShareConfiguration"
        ] = None,
    ) -> "capo_ram.types.create_resource_share_response.CreateResourceShareResponse":
        """<p>Creates a resource share. You can provide a list of the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> for the resources that you want to share, a list of principals you want to share the resources with, the permissions to grant those principals, and optionally source constraints to enhance security for service principal sharing.</p> <note> <p>Sharing a resource makes it available for use by principals outside of the Amazon Web Services account that created the resource. Sharing doesn't change any permissions or quotas that apply to the resource in the account that created it.</p> </note>

        Args:
            name: <p>Specifies the name of the resource share.</p>
            resource_arns: <p>Specifies a list of one or more ARNs of the resources to associate with the resource share.</p>
            principals: <p>Specifies a list of one or more principals to associate with the resource share.</p> <p>You can include the following values:</p> <ul> <li> <p>An Amazon Web Services account ID, for example: <code>123456789012</code> </p> </li> <li> <p>An <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an organization in Organizations, for example: <code>organizations::123456789012:organization/o-exampleorgid</code> </p> </li> <li> <p>An ARN of an organizational unit (OU) in Organizations, for example: <code>organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123</code> </p> </li> <li> <p>An ARN of an IAM role, for example: <code>iam::123456789012:role/rolename</code> </p> </li> <li> <p>An ARN of an IAM user, for example: <code>iam::123456789012user/username</code> </p> </li> <li> <p>A service principal name, for example: <code>service-id.amazonaws.com</code> </p> </li> </ul> <note> <p>Not all resource types can be shared with IAM roles and users. For more information, see <a href="https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types">Sharing with IAM roles and users</a> in the <i>Resource Access Manager User Guide</i>.</p> </note>
            tags: <p>Specifies one or more tags to attach to the resource share itself. It doesn't attach the tags to the resources associated with the resource share.</p>
            allow_external_principals: <p>Specifies whether principals outside your organization in Organizations can be associated with a resource share. A value of <code>true</code> lets you share with individual Amazon Web Services accounts that are <i>not</i> in your organization. A value of <code>false</code> only has meaning if your account is a member of an Amazon Web Services Organization. The default value is <code>true</code>.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            permission_arns: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> of the RAM permission to associate with the resource share. If you do not specify an ARN for the permission, RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.</p>
            sources: <p>Specifies source constraints (accounts, ARNs, organization IDs, or organization paths) that limit when service principals can access resources in this resource share. When a service principal attempts to access a shared resource, validation is performed to ensure the request originates from one of the specified sources. This helps prevent confused deputy attacks by applying constraints on where service principals can access resources from.</p>
            resource_share_configuration: <p>Specifies the configuration of this resource share.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_state_transition_exception.InvalidStateTransitionException: <p>The operation failed because the requested operation isn't valid for the resource share in its current state.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.resource_share_limit_exceeded_exception.ResourceShareLimitExceededException: <p>The operation failed because it would exceed the limit for resource shares for your account. You can associate up to 100 resources per call. To view the limits for your Amazon Web Services account, see the <a href="https://console.aws.amazon.com/servicequotas/home/services/ram/quotas">RAM page in the Service Quotas console</a>.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.tag_limit_exceeded_exception.TagLimitExceededException: <p>The operation failed because it would exceed the limit for tags for your Amazon Web Services account.</p>
            capo_ram.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The operation failed because the specified tag key is a reserved word and can't be used.</p>
            capo_ram.errors.throttling_exception.ThrottlingException: <p>The operation failed because it exceeded the rate at which you are allowed to perform this operation. Please try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.create_resource_share_request.CreateResourceShareRequest]",
        ) -> OperationResponse[
            "capo_ram.types.create_resource_share_response.CreateResourceShareResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.create_resource_share

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.create_resource_share.create_resource_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.create_resource_share_request.CreateResourceShareRequest = {
            "name": name
        }
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if principals is not None:
            input_["principals"] = principals
        if tags is not None:
            input_["tags"] = tags
        if allow_external_principals is not None:
            input_["allow_external_principals"] = allow_external_principals
        if client_token is not None:
            input_["client_token"] = client_token
        if permission_arns is not None:
            input_["permission_arns"] = permission_arns
        if sources is not None:
            input_["sources"] = sources
        if resource_share_configuration is not None:
            input_["resource_share_configuration"] = resource_share_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_permission(
        self,
        permission_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.delete_permission_response.DeletePermissionResponse":
        """<p>Deletes the specified customer managed permission in the Amazon Web Services Region in which you call this operation. You can delete a customer managed permission only if it isn't attached to any resource share. The operation deletes all versions associated with the customer managed permission.</p>

        Args:
            permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the customer managed permission that you want to delete.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.delete_permission_request.DeletePermissionRequest]",
        ) -> OperationResponse[
            "capo_ram.types.delete_permission_response.DeletePermissionResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.delete_permission

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.delete_permission.delete_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.delete_permission_request.DeletePermissionRequest = {
            "permission_arn": permission_arn
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_permission_version(
        self,
        permission_arn: "capo_ram.types.string.String",
        permission_version: "capo_ram.types.integer.Integer",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.delete_permission_version_response.DeletePermissionVersionResponse":
        """<p>Deletes one version of a customer managed permission. The version you specify must not be attached to any resource share and must not be the default version for the permission.</p> <p>If a customer managed permission has the maximum of 5 versions, then you must delete at least one version before you can create another.</p>

        Args:
            permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the permission with the version you want to delete.</p>
            permission_version: <p>Specifies the version number to delete.</p> <p>You can't delete the default version for a customer managed permission.</p> <p>You can't delete a version if it's the only version of the permission. You must either first create another version, or delete the permission completely.</p> <p>You can't delete a version if it is attached to any resource shares. If the version is the default, you must first use <a>SetDefaultPermissionVersion</a> to set a different version as the default for the customer managed permission, and then use <a>AssociateResourceSharePermission</a> to update your resource shares to use the new default version.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.delete_permission_version_request.DeletePermissionVersionRequest]",
        ) -> OperationResponse[
            "capo_ram.types.delete_permission_version_response.DeletePermissionVersionResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.delete_permission_version

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.delete_permission_version.delete_permission_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.delete_permission_version_request.DeletePermissionVersionRequest = {
            "permission_arn": permission_arn,
            "permission_version": permission_version,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_share(
        self,
        resource_share_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.delete_resource_share_response.DeleteResourceShareResponse":
        """<p>Deletes the specified resource share.</p> <important> <p>This doesn't delete any of the resources that were associated with the resource share; it only stops the sharing of those resources through this resource share.</p> </important>

        Args:
            resource_share_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share to delete.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_state_transition_exception.InvalidStateTransitionException: <p>The operation failed because the requested operation isn't valid for the resource share in its current state.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.throttling_exception.ThrottlingException: <p>The operation failed because it exceeded the rate at which you are allowed to perform this operation. Please try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.delete_resource_share_request.DeleteResourceShareRequest]",
        ) -> OperationResponse[
            "capo_ram.types.delete_resource_share_response.DeleteResourceShareResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.delete_resource_share

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.delete_resource_share.delete_resource_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.delete_resource_share_request.DeleteResourceShareRequest = {
            "resource_share_arn": resource_share_arn
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_resource_share(
        self,
        resource_share_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_arns: Optional[
            "capo_ram.types.resource_arn_list.ResourceArnList"
        ] = None,
        principals: Optional[
            "capo_ram.types.principal_arn_or_id_list.PrincipalArnOrIdList"
        ] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
        sources: Optional[
            "capo_ram.types.source_arn_or_account_list.SourceArnOrAccountList"
        ] = None,
    ) -> "capo_ram.types.disassociate_resource_share_response.DisassociateResourceShareResponse":
        """<p>Removes the specified principals, resources, or source constraints from participating in the specified resource share.</p>

        Args:
            resource_share_arn: <p>Specifies <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to remove resources or principals from.</p>
            resource_arns: <p>Specifies a list of <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> for one or more resources that you want to remove from the resource share. After the operation runs, these resources are no longer shared with principals associated with the resource share.</p>
            principals: <p>Specifies a list of one or more principals that no longer are to have access to the resources in this resource share.</p> <p>You can include the following values:</p> <ul> <li> <p>An Amazon Web Services account ID, for example: <code>123456789012</code> </p> </li> <li> <p>An <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an organization in Organizations, for example: <code>organizations::123456789012:organization/o-exampleorgid</code> </p> </li> <li> <p>An ARN of an organizational unit (OU) in Organizations, for example: <code>organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123</code> </p> </li> <li> <p>An ARN of an IAM role, for example: <code>iam::123456789012:role/rolename</code> </p> </li> <li> <p>An ARN of an IAM user, for example: <code>iam::123456789012user/username</code> </p> </li> <li> <p>A service principal name, for example: <code>service-id.amazonaws.com</code> </p> </li> </ul> <note> <p>Not all resource types can be shared with IAM roles and users. For more information, see <a href="https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types">Sharing with IAM roles and users</a> in the <i>Resource Access Manager User Guide</i>.</p> </note>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            sources: <p>Specifies source constraints (accounts, ARNs, organization IDs, or organization paths) to remove from the resource share. This enables granular management of source constraints while maintaining service principal associations. At least one source must remain when service principals are present.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_state_transition_exception.InvalidStateTransitionException: <p>The operation failed because the requested operation isn't valid for the resource share in its current state.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.resource_share_limit_exceeded_exception.ResourceShareLimitExceededException: <p>The operation failed because it would exceed the limit for resource shares for your account. You can associate up to 100 resources per call. To view the limits for your Amazon Web Services account, see the <a href="https://console.aws.amazon.com/servicequotas/home/services/ram/quotas">RAM page in the Service Quotas console</a>.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.throttling_exception.ThrottlingException: <p>The operation failed because it exceeded the rate at which you are allowed to perform this operation. Please try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.disassociate_resource_share_request.DisassociateResourceShareRequest]",
        ) -> OperationResponse[
            "capo_ram.types.disassociate_resource_share_response.DisassociateResourceShareResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.disassociate_resource_share

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.disassociate_resource_share.disassociate_resource_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.disassociate_resource_share_request.DisassociateResourceShareRequest = {
            "resource_share_arn": resource_share_arn
        }
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if principals is not None:
            input_["principals"] = principals
        if client_token is not None:
            input_["client_token"] = client_token
        if sources is not None:
            input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_resource_share_permission(
        self,
        resource_share_arn: "capo_ram.types.string.String",
        permission_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.disassociate_resource_share_permission_response.DisassociateResourceSharePermissionResponse":
        """<p>Removes a managed permission from a resource share. Permission changes take effect immediately. You can remove a managed permission from a resource share only if there are currently no resources of the relevant resource type currently attached to the resource share.</p>

        Args:
            resource_share_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to remove the managed permission from.</p>
            permission_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission to disassociate from the resource share. Changes to permissions take effect immediately.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_state_transition_exception.InvalidStateTransitionException: <p>The operation failed because the requested operation isn't valid for the resource share in its current state.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.disassociate_resource_share_permission_request.DisassociateResourceSharePermissionRequest]",
        ) -> OperationResponse[
            "capo_ram.types.disassociate_resource_share_permission_response.DisassociateResourceSharePermissionResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.disassociate_resource_share_permission

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.disassociate_resource_share_permission.disassociate_resource_share_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.disassociate_resource_share_permission_request.DisassociateResourceSharePermissionRequest = {
            "resource_share_arn": resource_share_arn,
            "permission_arn": permission_arn,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_sharing_with_aws_organization(
        self, *, config_overrides: Optional[RAMClientConfig] = None
    ) -> "capo_ram.types.enable_sharing_with_aws_organization_response.EnableSharingWithAwsOrganizationResponse":
        """<p>Enables resource sharing within your organization in Organizations. This operation creates a service-linked role called <code>AWSServiceRoleForResourceAccessManager</code> that has the IAM managed policy named AWSResourceAccessManagerServiceRolePolicy attached. This role permits RAM to retrieve information about the organization and its structure. This lets you share resources with all of the accounts in the calling account's organization by specifying the organization ID, or all of the accounts in an organizational unit (OU) by specifying the OU ID. Until you enable sharing within the organization, you can specify only individual Amazon Web Services accounts, or for supported resource types, IAM roles and users.</p> <p>You must call this operation from an IAM role or user in the organization's management account.</p> <p></p>

        Raises:
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.enable_sharing_with_aws_organization_request.EnableSharingWithAwsOrganizationRequest]",
        ) -> OperationResponse[
            "capo_ram.types.enable_sharing_with_aws_organization_response.EnableSharingWithAwsOrganizationResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.enable_sharing_with_aws_organization

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.enable_sharing_with_aws_organization.enable_sharing_with_aws_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.enable_sharing_with_aws_organization_request.EnableSharingWithAwsOrganizationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_permission(
        self,
        permission_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        permission_version: Optional["capo_ram.types.integer.Integer"] = None,
    ) -> "capo_ram.types.get_permission_response.GetPermissionResponse":
        """<p>Retrieves the contents of a managed permission in JSON format.</p>

        Args:
            permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the permission whose contents you want to retrieve. To find the ARN for a permission, use either the <a>ListPermissions</a> operation or go to the <a href="https://console.aws.amazon.com/ram/home#Permissions:">Permissions library</a> page in the RAM console and then choose the name of the permission. The ARN is displayed on the detail page.</p>
            permission_version: <p>Specifies the version number of the RAM permission to retrieve. If you don't specify this parameter, the operation retrieves the default version.</p> <p>To see the list of available versions, use <a>ListPermissionVersions</a>.</p>

        Raises:
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.get_permission_request.GetPermissionRequest]",
        ) -> OperationResponse[
            "capo_ram.types.get_permission_response.GetPermissionResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.get_permission

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.get_permission.get_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.get_permission_request.GetPermissionRequest = {
            "permission_arn": permission_arn
        }
        if permission_version is not None:
            input_["permission_version"] = permission_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policies(
        self,
        resource_arns: "capo_ram.types.resource_arn_list.ResourceArnList",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        principal: Optional["capo_ram.types.string.String"] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "capo_ram.types.get_resource_policies_response.GetResourcePoliciesResponse":
        """<p>Retrieves the resource policies for the specified resources that you own and have shared.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            resource_arns: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> of the resources whose policies you want to retrieve.</p>
            principal: <p>Specifies the principal.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.resource_arn_not_found_exception.ResourceArnNotFoundException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> was not found.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.get_resource_policies_request.GetResourcePoliciesRequest]",
        ) -> OperationResponse[
            "capo_ram.types.get_resource_policies_response.GetResourcePoliciesResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.get_resource_policies

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.get_resource_policies.get_resource_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.get_resource_policies_request.GetResourcePoliciesRequest = {
            "resource_arns": resource_arns
        }
        if principal is not None:
            input_["principal"] = principal
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

    def iter_get_resource_policies(
        self,
        resource_arns: "capo_ram.types.resource_arn_list.ResourceArnList",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        principal: Optional["capo_ram.types.string.String"] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ram.types.get_resource_policies_response.GetResourcePoliciesResponse]":
        _token = next_token
        while True:
            _response = self.get_resource_policies(
                resource_arns,
                config_overrides=config_overrides,
                principal=principal,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_resource_share_associations(
        self,
        association_type: "capo_ram.types.resource_share_association_type.ResourceShareAssociationType",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        resource_arn: Optional["capo_ram.types.string.String"] = None,
        principal: Optional["capo_ram.types.string.String"] = None,
        association_status: Optional[
            "capo_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "capo_ram.types.get_resource_share_associations_response.GetResourceShareAssociationsResponse":
        """<p>Retrieves the lists of resources and principals that associated for resource shares that you own.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            association_type: <p>Specifies whether you want to retrieve the associations that involve a specified resource or principal.</p> <ul> <li> <p> <code>PRINCIPAL</code> – list the principals whose associations you want to see.</p> </li> <li> <p> <code>RESOURCE</code> – list the resources whose associations you want to see.</p> </li> </ul>
            resource_share_arns: <p>Specifies a list of <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> of the resource share whose associations you want to retrieve.</p>
            resource_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of a resource whose resource shares you want to retrieve.</p> <p>You cannot specify this parameter if the association type is <code>PRINCIPAL</code>.</p>
            principal: <p>Specifies the ID of the principal whose resource shares you want to retrieve. This can be an Amazon Web Services account ID, an organization ID, an organizational unit ID, or the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an individual IAM role or user.</p> <p>You cannot specify this parameter if the association type is <code>RESOURCE</code>.</p>
            association_status: <p>Specifies that you want to retrieve only associations that have this status.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.get_resource_share_associations_request.GetResourceShareAssociationsRequest]",
        ) -> OperationResponse[
            "capo_ram.types.get_resource_share_associations_response.GetResourceShareAssociationsResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.get_resource_share_associations

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.get_resource_share_associations.get_resource_share_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.get_resource_share_associations_request.GetResourceShareAssociationsRequest = {
            "association_type": association_type
        }
        if resource_share_arns is not None:
            input_["resource_share_arns"] = resource_share_arns
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if principal is not None:
            input_["principal"] = principal
        if association_status is not None:
            input_["association_status"] = association_status
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

    def iter_get_resource_share_associations(
        self,
        association_type: "capo_ram.types.resource_share_association_type.ResourceShareAssociationType",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        resource_arn: Optional["capo_ram.types.string.String"] = None,
        principal: Optional["capo_ram.types.string.String"] = None,
        association_status: Optional[
            "capo_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ram.types.get_resource_share_associations_response.GetResourceShareAssociationsResponse]":
        _token = next_token
        while True:
            _response = self.get_resource_share_associations(
                association_type,
                config_overrides=config_overrides,
                resource_share_arns=resource_share_arns,
                resource_arn=resource_arn,
                principal=principal,
                association_status=association_status,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_resource_share_invitations(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_invitation_arns: Optional[
            "capo_ram.types.resource_share_invitation_arn_list.ResourceShareInvitationArnList"
        ] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "capo_ram.types.get_resource_share_invitations_response.GetResourceShareInvitationsResponse":
        """<p>Retrieves details about invitations that you have received for resource shares.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            resource_share_invitation_arns: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> of the resource share invitations you want information about.</p>
            resource_share_arns: <p>Specifies that you want details about invitations only for the resource shares described by this list of <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> </p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>

        Raises:
            capo_ram.errors.invalid_max_results_exception.InvalidMaxResultsException: <p>The operation failed because the specified value for <code>MaxResults</code> isn't valid.</p>
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.resource_share_invitation_arn_not_found_exception.ResourceShareInvitationArnNotFoundException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> for an invitation was not found.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.get_resource_share_invitations_request.GetResourceShareInvitationsRequest]",
        ) -> OperationResponse[
            "capo_ram.types.get_resource_share_invitations_response.GetResourceShareInvitationsResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.get_resource_share_invitations

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.get_resource_share_invitations.get_resource_share_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.get_resource_share_invitations_request.GetResourceShareInvitationsRequest = {}
        if resource_share_invitation_arns is not None:
            input_["resource_share_invitation_arns"] = resource_share_invitation_arns
        if resource_share_arns is not None:
            input_["resource_share_arns"] = resource_share_arns
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

    def iter_get_resource_share_invitations(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_invitation_arns: Optional[
            "capo_ram.types.resource_share_invitation_arn_list.ResourceShareInvitationArnList"
        ] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ram.types.get_resource_share_invitations_response.GetResourceShareInvitationsResponse]":
        _token = next_token
        while True:
            _response = self.get_resource_share_invitations(
                config_overrides=config_overrides,
                resource_share_invitation_arns=resource_share_invitation_arns,
                resource_share_arns=resource_share_arns,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_resource_shares(
        self,
        resource_owner: "capo_ram.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        resource_share_status: Optional[
            "capo_ram.types.resource_share_status.ResourceShareStatus"
        ] = None,
        name: Optional["capo_ram.types.string.String"] = None,
        tag_filters: Optional["capo_ram.types.tag_filters.TagFilters"] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        permission_arn: Optional["capo_ram.types.string.String"] = None,
        permission_version: Optional["capo_ram.types.integer.Integer"] = None,
    ) -> "capo_ram.types.get_resource_shares_response.GetResourceSharesResponse":
        """<p>Retrieves details about the resource shares that you own or that are shared with you.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            resource_share_arns: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> of individual resource shares that you want information about.</p>
            resource_share_status: <p>Specifies that you want to retrieve details of only those resource shares that have this status.</p>
            resource_owner: <p>Specifies that you want to retrieve details of only those resource shares that match the following:</p> <ul> <li> <p> <b> <code>SELF</code> </b> – resource shares that your account shares with other accounts</p> </li> <li> <p> <b> <code>OTHER-ACCOUNTS</code> </b> – resource shares that other accounts share with your account</p> </li> </ul>
            name: <p>Specifies the name of an individual resource share that you want to retrieve details about.</p>
            tag_filters: <p>Specifies that you want to retrieve details of only those resource shares that match the specified tag keys and values.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            permission_arn: <p>Specifies that you want to retrieve details of only those resource shares that use the managed permission with this <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a>.</p>
            permission_version: <p>Specifies that you want to retrieve details for only those resource shares that use the specified version of the managed permission.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.get_resource_shares_request.GetResourceSharesRequest]",
        ) -> OperationResponse[
            "capo_ram.types.get_resource_shares_response.GetResourceSharesResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.get_resource_shares

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.get_resource_shares.get_resource_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.get_resource_shares_request.GetResourceSharesRequest = {
            "resource_owner": resource_owner
        }
        if resource_share_arns is not None:
            input_["resource_share_arns"] = resource_share_arns
        if resource_share_status is not None:
            input_["resource_share_status"] = resource_share_status
        if name is not None:
            input_["name"] = name
        if tag_filters is not None:
            input_["tag_filters"] = tag_filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if permission_arn is not None:
            input_["permission_arn"] = permission_arn
        if permission_version is not None:
            input_["permission_version"] = permission_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_resource_shares(
        self,
        resource_owner: "capo_ram.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        resource_share_status: Optional[
            "capo_ram.types.resource_share_status.ResourceShareStatus"
        ] = None,
        name: Optional["capo_ram.types.string.String"] = None,
        tag_filters: Optional["capo_ram.types.tag_filters.TagFilters"] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        permission_arn: Optional["capo_ram.types.string.String"] = None,
        permission_version: Optional["capo_ram.types.integer.Integer"] = None,
    ) -> "Iterator[capo_ram.types.get_resource_shares_response.GetResourceSharesResponse]":
        _token = next_token
        while True:
            _response = self.get_resource_shares(
                resource_owner,
                config_overrides=config_overrides,
                resource_share_arns=resource_share_arns,
                resource_share_status=resource_share_status,
                name=name,
                tag_filters=tag_filters,
                next_token=_token,
                max_results=max_results,
                permission_arn=permission_arn,
                permission_version=permission_version,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_pending_invitation_resources(
        self,
        resource_share_invitation_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        resource_region_scope: Optional[
            "capo_ram.types.resource_region_scope_filter.ResourceRegionScopeFilter"
        ] = None,
    ) -> "capo_ram.types.list_pending_invitation_resources_response.ListPendingInvitationResourcesResponse":
        """<p>Lists the resources in a resource share that is shared with you but for which the invitation is still <code>PENDING</code>. That means that you haven't accepted or rejected the invitation and the invitation hasn't expired.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            resource_share_invitation_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the invitation. You can use <a>GetResourceShareInvitations</a> to find the ARN of the invitation.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            resource_region_scope: <p>Specifies that you want the results to include only resources that have the specified scope.</p> <ul> <li> <p> <code>ALL</code> – the results include both global and regional resources or resource types.</p> </li> <li> <p> <code>GLOBAL</code> – the results include only global resources or resource types.</p> </li> <li> <p> <code>REGIONAL</code> – the results include only regional resources or resource types.</p> </li> </ul> <p>The default value is <code>ALL</code>.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>The operation failed because a required input parameter is missing.</p>
            capo_ram.errors.resource_share_invitation_already_rejected_exception.ResourceShareInvitationAlreadyRejectedException: <p>The operation failed because the specified invitation was already rejected.</p>
            capo_ram.errors.resource_share_invitation_arn_not_found_exception.ResourceShareInvitationArnNotFoundException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> for an invitation was not found.</p>
            capo_ram.errors.resource_share_invitation_expired_exception.ResourceShareInvitationExpiredException: <p>The operation failed because the specified invitation is past its expiration date and time.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_pending_invitation_resources_request.ListPendingInvitationResourcesRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_pending_invitation_resources_response.ListPendingInvitationResourcesResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_pending_invitation_resources

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_pending_invitation_resources.list_pending_invitation_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_pending_invitation_resources_request.ListPendingInvitationResourcesRequest = {
            "resource_share_invitation_arn": resource_share_invitation_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_region_scope is not None:
            input_["resource_region_scope"] = resource_region_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_pending_invitation_resources(
        self,
        resource_share_invitation_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        resource_region_scope: Optional[
            "capo_ram.types.resource_region_scope_filter.ResourceRegionScopeFilter"
        ] = None,
    ) -> "Iterator[capo_ram.types.list_pending_invitation_resources_response.ListPendingInvitationResourcesResponse]":
        _token = next_token
        while True:
            _response = self.list_pending_invitation_resources(
                resource_share_invitation_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                resource_region_scope=resource_region_scope,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_permission_associations(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        permission_arn: Optional["capo_ram.types.string.String"] = None,
        permission_version: Optional["capo_ram.types.integer.Integer"] = None,
        association_status: Optional[
            "capo_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
        ] = None,
        resource_type: Optional["capo_ram.types.string.String"] = None,
        feature_set: Optional[
            "capo_ram.types.permission_feature_set.PermissionFeatureSet"
        ] = None,
        default_version: Optional["capo_ram.types.boolean.Boolean"] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "capo_ram.types.list_permission_associations_response.ListPermissionAssociationsResponse":
        """<p>Lists information about the managed permission and its associations to any resource shares that use this managed permission. This lets you see which resource shares use which versions of the specified managed permission.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission.</p>
            permission_version: <p>Specifies that you want to list only those associations with resource shares that use this version of the managed permission. If you don't provide a value for this parameter, then the operation returns information about associations with resource shares that use any version of the managed permission.</p>
            association_status: <p>Specifies that you want to list only those associations with resource shares that match this status.</p>
            resource_type: <p>Specifies that you want to list only those associations with resource shares that include at least one resource of this resource type.</p>
            feature_set: <p>Specifies that you want to list only those associations with resource shares that have a <code>featureSet</code> with this value.</p>
            default_version: <p>When <code>true</code>, specifies that you want to list only those associations with resource shares that use the default version of the specified managed permission.</p> <p>When <code>false</code> (the default value), lists associations with resource shares that use any version of the specified managed permission.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_permission_associations_request.ListPermissionAssociationsRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_permission_associations_response.ListPermissionAssociationsResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_permission_associations

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_permission_associations.list_permission_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_permission_associations_request.ListPermissionAssociationsRequest = {}
        if permission_arn is not None:
            input_["permission_arn"] = permission_arn
        if permission_version is not None:
            input_["permission_version"] = permission_version
        if association_status is not None:
            input_["association_status"] = association_status
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if feature_set is not None:
            input_["feature_set"] = feature_set
        if default_version is not None:
            input_["default_version"] = default_version
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

    def iter_list_permission_associations(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        permission_arn: Optional["capo_ram.types.string.String"] = None,
        permission_version: Optional["capo_ram.types.integer.Integer"] = None,
        association_status: Optional[
            "capo_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
        ] = None,
        resource_type: Optional["capo_ram.types.string.String"] = None,
        feature_set: Optional[
            "capo_ram.types.permission_feature_set.PermissionFeatureSet"
        ] = None,
        default_version: Optional["capo_ram.types.boolean.Boolean"] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ram.types.list_permission_associations_response.ListPermissionAssociationsResponse]":
        _token = next_token
        while True:
            _response = self.list_permission_associations(
                config_overrides=config_overrides,
                permission_arn=permission_arn,
                permission_version=permission_version,
                association_status=association_status,
                resource_type=resource_type,
                feature_set=feature_set,
                default_version=default_version,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_permissions(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_type: Optional["capo_ram.types.string.String"] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        permission_type: Optional[
            "capo_ram.types.permission_type_filter.PermissionTypeFilter"
        ] = None,
    ) -> "capo_ram.types.list_permissions_response.ListPermissionsResponse":
        """<p>Retrieves a list of available RAM permissions that you can use for the supported resource types. </p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            resource_type: <p>Specifies that you want to list only those permissions that apply to the specified resource type. This parameter is not case sensitive.</p> <p>For example, to list only permissions that apply to Amazon EC2 subnets, specify <code>ec2:subnet</code>. You can use the <a>ListResourceTypes</a> operation to get the specific string required.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            permission_type: <p>Specifies that you want to list only permissions of this type:</p> <ul> <li> <p> <code>AWS</code> – returns only Amazon Web Services managed permissions.</p> </li> <li> <p> <code>LOCAL</code> – returns only customer managed permissions</p> </li> <li> <p> <code>ALL</code> – returns both Amazon Web Services managed permissions and customer managed permissions.</p> </li> </ul> <p>If you don't specify this parameter, the default is <code>All</code>.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_permissions_request.ListPermissionsRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_permissions_response.ListPermissionsResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_permissions

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_permissions.list_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_permissions_request.ListPermissionsRequest = {}
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if permission_type is not None:
            input_["permission_type"] = permission_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_permissions(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_type: Optional["capo_ram.types.string.String"] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        permission_type: Optional[
            "capo_ram.types.permission_type_filter.PermissionTypeFilter"
        ] = None,
    ) -> "Iterator[capo_ram.types.list_permissions_response.ListPermissionsResponse]":
        _token = next_token
        while True:
            _response = self.list_permissions(
                config_overrides=config_overrides,
                resource_type=resource_type,
                next_token=_token,
                max_results=max_results,
                permission_type=permission_type,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_permission_versions(
        self,
        permission_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "capo_ram.types.list_permission_versions_response.ListPermissionVersionsResponse":
        """<p>Lists the available versions of the specified RAM permission.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the RAM permission whose versions you want to list. You can use the <code>permissionVersion</code> parameter on the <a>AssociateResourceSharePermission</a> operation to specify a non-default version to attach.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_permission_versions_request.ListPermissionVersionsRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_permission_versions_response.ListPermissionVersionsResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_permission_versions

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_permission_versions.list_permission_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_permission_versions_request.ListPermissionVersionsRequest = {
            "permission_arn": permission_arn
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

    def iter_list_permission_versions(
        self,
        permission_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ram.types.list_permission_versions_response.ListPermissionVersionsResponse]":
        _token = next_token
        while True:
            _response = self.list_permission_versions(
                permission_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_principals(
        self,
        resource_owner: "capo_ram.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_arn: Optional["capo_ram.types.string.String"] = None,
        principals: Optional[
            "capo_ram.types.principal_arn_or_id_list.PrincipalArnOrIdList"
        ] = None,
        resource_type: Optional["capo_ram.types.string.String"] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "capo_ram.types.list_principals_response.ListPrincipalsResponse":
        """<p>Lists the principals that you are sharing resources with or that are sharing resources with you.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            resource_owner: <p>Specifies that you want to list information for only resource shares that match the following:</p> <ul> <li> <p> <b> <code>SELF</code> </b> – principals that your account is sharing resources with</p> </li> <li> <p> <b> <code>OTHER-ACCOUNTS</code> </b> – principals that are sharing resources with your account</p> </li> </ul>
            resource_arn: <p>Specifies that you want to list principal information for the resource share with the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a>.</p>
            principals: <p>Specifies that you want to list information for only the listed principals.</p> <p>You can include the following values:</p> <ul> <li> <p>An Amazon Web Services account ID, for example: <code>123456789012</code> </p> </li> <li> <p>An <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an organization in Organizations, for example: <code>organizations::123456789012:organization/o-exampleorgid</code> </p> </li> <li> <p>An ARN of an organizational unit (OU) in Organizations, for example: <code>organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123</code> </p> </li> <li> <p>An ARN of an IAM role, for example: <code>iam::123456789012:role/rolename</code> </p> </li> <li> <p>An ARN of an IAM user, for example: <code>iam::123456789012user/username</code> </p> </li> <li> <p>A service principal name, for example: <code>service-id.amazonaws.com</code> </p> </li> </ul> <note> <p>Not all resource types can be shared with IAM roles and users. For more information, see <a href="https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types">Sharing with IAM roles and users</a> in the <i>Resource Access Manager User Guide</i>.</p> </note>
            resource_type: <p>Specifies that you want to list information for only principals associated with resource shares that include the specified resource type.</p> <p>For a list of valid values, query the <a>ListResourceTypes</a> operation.</p>
            resource_share_arns: <p>Specifies that you want to list information for only principals associated with the resource shares specified by a list the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_principals_request.ListPrincipalsRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_principals_response.ListPrincipalsResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_principals

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_principals.list_principals(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_principals_request.ListPrincipalsRequest = {
            "resource_owner": resource_owner
        }
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if principals is not None:
            input_["principals"] = principals
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_share_arns is not None:
            input_["resource_share_arns"] = resource_share_arns
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

    def iter_list_principals(
        self,
        resource_owner: "capo_ram.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_arn: Optional["capo_ram.types.string.String"] = None,
        principals: Optional[
            "capo_ram.types.principal_arn_or_id_list.PrincipalArnOrIdList"
        ] = None,
        resource_type: Optional["capo_ram.types.string.String"] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ram.types.list_principals_response.ListPrincipalsResponse]":
        _token = next_token
        while True:
            _response = self.list_principals(
                resource_owner,
                config_overrides=config_overrides,
                resource_arn=resource_arn,
                principals=principals,
                resource_type=resource_type,
                resource_share_arns=resource_share_arns,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_replace_permission_associations_work(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        work_ids: Optional[
            "capo_ram.types.replace_permission_associations_work_id_list.ReplacePermissionAssociationsWorkIdList"
        ] = None,
        status: Optional[
            "capo_ram.types.replace_permission_associations_work_status.ReplacePermissionAssociationsWorkStatus"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "capo_ram.types.list_replace_permission_associations_work_response.ListReplacePermissionAssociationsWorkResponse":
        """<p>Retrieves the current status of the asynchronous tasks performed by RAM when you perform the <a>ReplacePermissionAssociationsWork</a> operation.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            work_ids: <p>A list of IDs. These values come from the <code>id</code>field of the <code>replacePermissionAssociationsWork</code>structure returned by the <a>ReplacePermissionAssociations</a> operation. </p>
            status: <p>Specifies that you want to see only the details about requests with a status that matches this value.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_replace_permission_associations_work_request.ListReplacePermissionAssociationsWorkRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_replace_permission_associations_work_response.ListReplacePermissionAssociationsWorkResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_replace_permission_associations_work

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_replace_permission_associations_work.list_replace_permission_associations_work(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_replace_permission_associations_work_request.ListReplacePermissionAssociationsWorkRequest = {}
        if work_ids is not None:
            input_["work_ids"] = work_ids
        if status is not None:
            input_["status"] = status
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

    def iter_list_replace_permission_associations_work(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        work_ids: Optional[
            "capo_ram.types.replace_permission_associations_work_id_list.ReplacePermissionAssociationsWorkIdList"
        ] = None,
        status: Optional[
            "capo_ram.types.replace_permission_associations_work_status.ReplacePermissionAssociationsWorkStatus"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ram.types.list_replace_permission_associations_work_response.ListReplacePermissionAssociationsWorkResponse]":
        _token = next_token
        while True:
            _response = self.list_replace_permission_associations_work(
                config_overrides=config_overrides,
                work_ids=work_ids,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resources(
        self,
        resource_owner: "capo_ram.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        principal: Optional["capo_ram.types.string.String"] = None,
        resource_type: Optional["capo_ram.types.string.String"] = None,
        resource_arns: Optional[
            "capo_ram.types.resource_arn_list.ResourceArnList"
        ] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        resource_region_scope: Optional[
            "capo_ram.types.resource_region_scope_filter.ResourceRegionScopeFilter"
        ] = None,
    ) -> "capo_ram.types.list_resources_response.ListResourcesResponse":
        """<p>Lists the resources that you added to a resource share or the resources that are shared with you.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            resource_owner: <p>Specifies that you want to list only the resource shares that match the following:</p> <ul> <li> <p> <b> <code>SELF</code> </b> – resources that your account shares with other accounts</p> </li> <li> <p> <b> <code>OTHER-ACCOUNTS</code> </b> – resources that other accounts share with your account</p> </li> </ul>
            principal: <p>Specifies that you want to list only the resource shares that are associated with the specified principal.</p>
            resource_type: <p>Specifies that you want to list only the resource shares that include resources of the specified resource type.</p> <p>For valid values, query the <a>ListResourceTypes</a> operation.</p>
            resource_arns: <p>Specifies that you want to list only the resource shares that include resources with the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>
            resource_share_arns: <p>Specifies that you want to list only resources in the resource shares identified by the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            resource_region_scope: <p>Specifies that you want the results to include only resources that have the specified scope.</p> <ul> <li> <p> <code>ALL</code> – the results include both global and regional resources or resource types.</p> </li> <li> <p> <code>GLOBAL</code> – the results include only global resources or resource types.</p> </li> <li> <p> <code>REGIONAL</code> – the results include only regional resources or resource types.</p> </li> </ul> <p>The default value is <code>ALL</code>.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_resource_type_exception.InvalidResourceTypeException: <p>The operation failed because the specified resource type isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_resources_request.ListResourcesRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_resources_response.ListResourcesResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_resources

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_resources.list_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_resources_request.ListResourcesRequest = {
            "resource_owner": resource_owner
        }
        if principal is not None:
            input_["principal"] = principal
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if resource_share_arns is not None:
            input_["resource_share_arns"] = resource_share_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_region_scope is not None:
            input_["resource_region_scope"] = resource_region_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_resources(
        self,
        resource_owner: "capo_ram.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        principal: Optional["capo_ram.types.string.String"] = None,
        resource_type: Optional["capo_ram.types.string.String"] = None,
        resource_arns: Optional[
            "capo_ram.types.resource_arn_list.ResourceArnList"
        ] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        resource_region_scope: Optional[
            "capo_ram.types.resource_region_scope_filter.ResourceRegionScopeFilter"
        ] = None,
    ) -> "Iterator[capo_ram.types.list_resources_response.ListResourcesResponse]":
        _token = next_token
        while True:
            _response = self.list_resources(
                resource_owner,
                config_overrides=config_overrides,
                principal=principal,
                resource_type=resource_type,
                resource_arns=resource_arns,
                resource_share_arns=resource_share_arns,
                next_token=_token,
                max_results=max_results,
                resource_region_scope=resource_region_scope,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_share_permissions(
        self,
        resource_share_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "capo_ram.types.list_resource_share_permissions_response.ListResourceSharePermissionsResponse":
        """<p>Lists the RAM permissions that are associated with a resource share.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            resource_share_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share for which you want to retrieve the associated permissions.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_resource_share_permissions_request.ListResourceSharePermissionsRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_resource_share_permissions_response.ListResourceSharePermissionsResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_resource_share_permissions

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_resource_share_permissions.list_resource_share_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_resource_share_permissions_request.ListResourceSharePermissionsRequest = {
            "resource_share_arn": resource_share_arn
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

    def iter_list_resource_share_permissions(
        self,
        resource_share_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ram.types.list_resource_share_permissions_response.ListResourceSharePermissionsResponse]":
        _token = next_token
        while True:
            _response = self.list_resource_share_permissions(
                resource_share_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_types(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        resource_region_scope: Optional[
            "capo_ram.types.resource_region_scope_filter.ResourceRegionScopeFilter"
        ] = None,
    ) -> "capo_ram.types.list_resource_types_response.ListResourceTypesResponse":
        """<p>Lists the resource types that can be shared by RAM.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            resource_region_scope: <p>Specifies that you want the results to include only resources that have the specified scope.</p> <ul> <li> <p> <code>ALL</code> – the results include both global and regional resources or resource types.</p> </li> <li> <p> <code>GLOBAL</code> – the results include only global resources or resource types.</p> </li> <li> <p> <code>REGIONAL</code> – the results include only regional resources or resource types.</p> </li> </ul> <p>The default value is <code>ALL</code>.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_resource_types_request.ListResourceTypesRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_resource_types_response.ListResourceTypesResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_resource_types

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_resource_types.list_resource_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_resource_types_request.ListResourceTypesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_region_scope is not None:
            input_["resource_region_scope"] = resource_region_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_resource_types(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
        resource_region_scope: Optional[
            "capo_ram.types.resource_region_scope_filter.ResourceRegionScopeFilter"
        ] = None,
    ) -> "Iterator[capo_ram.types.list_resource_types_response.ListResourceTypesResponse]":
        _token = next_token
        while True:
            _response = self.list_resource_types(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                resource_region_scope=resource_region_scope,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_source_associations(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        source_id: Optional["capo_ram.types.string.String"] = None,
        source_type: Optional["capo_ram.types.string.String"] = None,
        association_status: Optional[
            "capo_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "capo_ram.types.list_source_associations_response.ListSourceAssociationsResponse":
        """<p>Lists source associations for resource shares. Source associations control which sources can be used with service principals in resource shares. This operation provides visibility into source associations for resource share owners.</p> <p>You can filter the results by resource share Amazon Resource Name (ARN), source ID, source type, or association status. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            resource_share_arns: <p>The Amazon Resource Names (ARNs) of the resource shares for which you want to retrieve source associations.</p>
            source_id: <p>The identifier of the source for which you want to retrieve associations. This can be an account ID, Amazon Resource Name (ARN), organization ID, or organization path.</p>
            source_type: <p>The type of source for which you want to retrieve associations.</p>
            association_status: <p>The status of the source associations that you want to retrieve.</p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_ram.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The operation failed because the specified value for <code>NextToken</code> isn't valid. You must specify a value you received in the <code>NextToken</code> response of a previous call to this operation.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.list_source_associations_request.ListSourceAssociationsRequest]",
        ) -> OperationResponse[
            "capo_ram.types.list_source_associations_response.ListSourceAssociationsResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.list_source_associations

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.list_source_associations.list_source_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.list_source_associations_request.ListSourceAssociationsRequest = {}
        if resource_share_arns is not None:
            input_["resource_share_arns"] = resource_share_arns
        if source_id is not None:
            input_["source_id"] = source_id
        if source_type is not None:
            input_["source_type"] = source_type
        if association_status is not None:
            input_["association_status"] = association_status
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

    def iter_list_source_associations(
        self,
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_arns: Optional[
            "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
        ] = None,
        source_id: Optional["capo_ram.types.string.String"] = None,
        source_type: Optional["capo_ram.types.string.String"] = None,
        association_status: Optional[
            "capo_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
        ] = None,
        next_token: Optional["capo_ram.types.string.String"] = None,
        max_results: Optional["capo_ram.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ram.types.associated_source.AssociatedSource]":
        _token = next_token
        while True:
            _response = self.list_source_associations(
                config_overrides=config_overrides,
                resource_share_arns=resource_share_arns,
                source_id=source_id,
                source_type=source_type,
                association_status=association_status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("source_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def promote_permission_created_from_policy(
        self,
        permission_arn: "capo_ram.types.string.String",
        name: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.promote_permission_created_from_policy_response.PromotePermissionCreatedFromPolicyResponse":
        """<p>When you attach a resource-based policy to a resource, RAM automatically creates a resource share of <code>featureSet</code>=<code>CREATED_FROM_POLICY</code> with a managed permission that has the same IAM permissions as the original resource-based policy. However, this type of managed permission is visible to only the resource share owner, and the associated resource share can't be modified by using RAM.</p> <p>This operation creates a separate, fully manageable customer managed permission that has the same IAM permissions as the original resource-based policy. You can associate this customer managed permission to any resource shares.</p> <p>Before you use <a>PromoteResourceShareCreatedFromPolicy</a>, you should first run this operation to ensure that you have an appropriate customer managed permission that can be associated with the promoted resource share.</p> <note> <ul> <li> <p>The original <code>CREATED_FROM_POLICY</code> policy isn't deleted, and resource shares using that original policy aren't automatically updated.</p> </li> <li> <p>You can't modify a <code>CREATED_FROM_POLICY</code> resource share so you can't associate the new customer managed permission by using <code>ReplacePermsissionAssociations</code>. However, if you use <a>PromoteResourceShareCreatedFromPolicy</a>, that operation automatically associates the fully manageable customer managed permission to the newly promoted <code>STANDARD</code> resource share.</p> </li> <li> <p>After you promote a resource share, if the original <code>CREATED_FROM_POLICY</code> managed permission has no other associations to A resource share, then RAM automatically deletes it.</p> </li> </ul> </note>

        Args:
            permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the <code>CREATED_FROM_POLICY</code> permission that you want to promote. You can get this <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> by calling the <a>ListResourceSharePermissions</a> operation.</p>
            name: <p>Specifies a name for the promoted customer managed permission.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_policy_exception.InvalidPolicyException: <p>The operation failed because a policy you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>The operation failed because a required input parameter is missing.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.promote_permission_created_from_policy_request.PromotePermissionCreatedFromPolicyRequest]",
        ) -> OperationResponse[
            "capo_ram.types.promote_permission_created_from_policy_response.PromotePermissionCreatedFromPolicyResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.promote_permission_created_from_policy

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.promote_permission_created_from_policy.promote_permission_created_from_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.promote_permission_created_from_policy_request.PromotePermissionCreatedFromPolicyRequest = {
            "permission_arn": permission_arn,
            "name": name,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def promote_resource_share_created_from_policy(
        self,
        resource_share_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
    ) -> "capo_ram.types.promote_resource_share_created_from_policy_response.PromoteResourceShareCreatedFromPolicyResponse":
        """<p>When you attach a resource-based policy to a resource, RAM automatically creates a resource share of <code>featureSet</code>=<code>CREATED_FROM_POLICY</code> with a managed permission that has the same IAM permissions as the original resource-based policy. However, this type of managed permission is visible to only the resource share owner, and the associated resource share can't be modified by using RAM.</p> <p>This operation promotes the resource share to a <code>STANDARD</code> resource share that is fully manageable in RAM. When you promote a resource share, you can then manage the resource share in RAM and it becomes visible to all of the principals you shared it with.</p> <important> <p>Before you perform this operation, you should first run <a>PromotePermissionCreatedFromPolicy</a>to ensure that you have an appropriate customer managed permission that can be associated with this resource share after its is promoted. If this operation can't find a managed permission that exactly matches the existing <code>CREATED_FROM_POLICY</code> permission, then this operation fails.</p> </important>

        Args:
            resource_share_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share to promote.</p>

        Raises:
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.invalid_state_transition_exception.InvalidStateTransitionException: <p>The operation failed because the requested operation isn't valid for the resource share in its current state.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>The operation failed because a required input parameter is missing.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.resource_share_limit_exceeded_exception.ResourceShareLimitExceededException: <p>The operation failed because it would exceed the limit for resource shares for your account. You can associate up to 100 resources per call. To view the limits for your Amazon Web Services account, see the <a href="https://console.aws.amazon.com/servicequotas/home/services/ram/quotas">RAM page in the Service Quotas console</a>.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.unmatched_policy_permission_exception.UnmatchedPolicyPermissionException: <p>There isn't an existing managed permission defined in RAM that has the same IAM permissions as the resource-based policy attached to the resource. You should first run <a>PromotePermissionCreatedFromPolicy</a> to create that managed permission.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.promote_resource_share_created_from_policy_request.PromoteResourceShareCreatedFromPolicyRequest]",
        ) -> OperationResponse[
            "capo_ram.types.promote_resource_share_created_from_policy_response.PromoteResourceShareCreatedFromPolicyResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.promote_resource_share_created_from_policy

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.promote_resource_share_created_from_policy.promote_resource_share_created_from_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.promote_resource_share_created_from_policy_request.PromoteResourceShareCreatedFromPolicyRequest = {
            "resource_share_arn": resource_share_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_resource_share_invitation(
        self,
        resource_share_invitation_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.reject_resource_share_invitation_response.RejectResourceShareInvitationResponse":
        """<p>Rejects an invitation to a resource share from another Amazon Web Services account.</p>

        Args:
            resource_share_invitation_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the invitation that you want to reject.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.resource_share_invitation_already_accepted_exception.ResourceShareInvitationAlreadyAcceptedException: <p>The operation failed because the specified invitation was already accepted.</p>
            capo_ram.errors.resource_share_invitation_already_rejected_exception.ResourceShareInvitationAlreadyRejectedException: <p>The operation failed because the specified invitation was already rejected.</p>
            capo_ram.errors.resource_share_invitation_arn_not_found_exception.ResourceShareInvitationArnNotFoundException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> for an invitation was not found.</p>
            capo_ram.errors.resource_share_invitation_expired_exception.ResourceShareInvitationExpiredException: <p>The operation failed because the specified invitation is past its expiration date and time.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.reject_resource_share_invitation_request.RejectResourceShareInvitationRequest]",
        ) -> OperationResponse[
            "capo_ram.types.reject_resource_share_invitation_response.RejectResourceShareInvitationResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.reject_resource_share_invitation

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.reject_resource_share_invitation.reject_resource_share_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.reject_resource_share_invitation_request.RejectResourceShareInvitationRequest = {
            "resource_share_invitation_arn": resource_share_invitation_arn
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def replace_permission_associations(
        self,
        from_permission_arn: "capo_ram.types.string.String",
        to_permission_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        from_permission_version: Optional["capo_ram.types.integer.Integer"] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.replace_permission_associations_response.ReplacePermissionAssociationsResponse":
        """<p>Updates all resource shares that use a managed permission to a different managed permission. This operation always applies the default version of the target managed permission. You can optionally specify that the update applies to only resource shares that currently use a specified version. This enables you to update to the latest version, without changing the which managed permission is used.</p> <p>You can use this operation to update all of your resource shares to use the current default version of the permission by specifying the same value for the <code>fromPermissionArn</code> and <code>toPermissionArn</code> parameters.</p> <p>You can use the optional <code>fromPermissionVersion</code> parameter to update only those resources that use a specified version of the managed permission to the new managed permission.</p> <important> <p>To successfully perform this operation, you must have permission to update the resource-based policy on all affected resource types.</p> </important>

        Args:
            from_permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission that you want to replace.</p>
            from_permission_version: <p>Specifies that you want to updated the permissions for only those resource shares that use the specified version of the managed permission.</p>
            to_permission_arn: <p>Specifies the ARN of the managed permission that you want to associate with resource shares in place of the one specified by <code>fromPerssionArn</code> and <code>fromPermissionVersion</code>.</p> <p>The operation always associates the version that is currently the default for the specified managed permission.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.replace_permission_associations_request.ReplacePermissionAssociationsRequest]",
        ) -> OperationResponse[
            "capo_ram.types.replace_permission_associations_response.ReplacePermissionAssociationsResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.replace_permission_associations

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.replace_permission_associations.replace_permission_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.replace_permission_associations_request.ReplacePermissionAssociationsRequest = {
            "from_permission_arn": from_permission_arn,
            "to_permission_arn": to_permission_arn,
        }
        if from_permission_version is not None:
            input_["from_permission_version"] = from_permission_version
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_default_permission_version(
        self,
        permission_arn: "capo_ram.types.string.String",
        permission_version: "capo_ram.types.integer.Integer",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.set_default_permission_version_response.SetDefaultPermissionVersionResponse":
        """<p>Designates the specified version number as the default version for the specified customer managed permission. New resource shares automatically use this new default permission. Existing resource shares continue to use their original permission version, but you can use <a>ReplacePermissionAssociations</a> to update them.</p>

        Args:
            permission_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the customer managed permission whose default version you want to change.</p>
            permission_version: <p>Specifies the version number that you want to designate as the default for customer managed permission. To see a list of all available version numbers, use <a>ListPermissionVersions</a>.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.set_default_permission_version_request.SetDefaultPermissionVersionRequest]",
        ) -> OperationResponse[
            "capo_ram.types.set_default_permission_version_response.SetDefaultPermissionVersionResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.set_default_permission_version

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.set_default_permission_version.set_default_permission_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.set_default_permission_version_request.SetDefaultPermissionVersionRequest = {
            "permission_arn": permission_arn,
            "permission_version": permission_version,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        tags: "capo_ram.types.tag_list.TagList",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_arn: Optional["capo_ram.types.string.String"] = None,
        resource_arn: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tag keys and values to a resource share or managed permission. If you choose a resource share, the tags are attached to only the resource share, not to the resources that are in the resource share.</p> <p>The tags on a managed permission are the same for all versions of the managed permission.</p>

        Args:
            resource_share_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to add tags to. You must specify <i>either</i> <code>resourceShareArn</code>, or <code>resourceArn</code>, but not both.</p>
            tags: <p>A list of one or more tag key and value pairs. The tag key must be present and not be an empty string. The tag value must be present but can be an empty string.</p>
            resource_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission that you want to add tags to. You must specify <i>either</i> <code>resourceArn</code>, or <code>resourceShareArn</code>, but not both.</p>

        Raises:
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.resource_arn_not_found_exception.ResourceArnNotFoundException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> was not found.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.tag_limit_exceeded_exception.TagLimitExceededException: <p>The operation failed because it would exceed the limit for tags for your Amazon Web Services account.</p>
            capo_ram.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The operation failed because the specified tag key is a reserved word and can't be used.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_ram.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.tag_resource

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.tag_resource_request.TagResourceRequest = {"tags": tags}
        if resource_share_arn is not None:
            input_["resource_share_arn"] = resource_share_arn
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        tag_keys: "capo_ram.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        resource_share_arn: Optional["capo_ram.types.string.String"] = None,
        resource_arn: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tag key and value pairs from the specified resource share or managed permission.</p>

        Args:
            resource_share_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to remove tags from. The tags are removed from the resource share, not the resources in the resource share. You must specify either <code>resourceShareArn</code>, or <code>resourceArn</code>, but not both.</p>
            tag_keys: <p>Specifies a list of one or more tag keys that you want to remove.</p>
            resource_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission that you want to remove tags from. You must specify either <code>resourceArn</code>, or <code>resourceShareArn</code>, but not both.</p>

        Raises:
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_ram.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.untag_resource

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.untag_resource_request.UntagResourceRequest = {
            "tag_keys": tag_keys
        }
        if resource_share_arn is not None:
            input_["resource_share_arn"] = resource_share_arn
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resource_share(
        self,
        resource_share_arn: "capo_ram.types.string.String",
        *,
        config_overrides: Optional[RAMClientConfig] = None,
        name: Optional["capo_ram.types.string.String"] = None,
        allow_external_principals: Optional["capo_ram.types.boolean.Boolean"] = None,
        client_token: Optional["capo_ram.types.string.String"] = None,
    ) -> "capo_ram.types.update_resource_share_response.UpdateResourceShareResponse":
        """<p>Modifies some of the properties of the specified resource share.</p>

        Args:
            resource_share_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to modify.</p>
            name: <p>If specified, the new name that you want to attach to the resource share.</p>
            allow_external_principals: <p>Specifies whether principals outside your organization in Organizations can be associated with a resource share.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.</p>
            capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The operation failed because the specified client token isn't valid.</p>
            capo_ram.errors.invalid_parameter_exception.InvalidParameterException: <p>The operation failed because a parameter you specified isn't valid.</p>
            capo_ram.errors.malformed_arn_exception.MalformedArnException: <p>The operation failed because the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> has a format that isn't valid.</p>
            capo_ram.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>The operation failed because a required input parameter is missing.</p>
            capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>The operation failed because the requested operation isn't permitted.</p>
            capo_ram.errors.server_internal_exception.ServerInternalException: <p>The operation failed because the service could not respond to the request due to an internal problem. Try again later.</p>
            capo_ram.errors.service_unavailable_exception.ServiceUnavailableException: <p>The operation failed because the service isn't available. Try again later.</p>
            capo_ram.errors.unknown_resource_exception.UnknownResourceException: <p>The operation failed because a specified resource couldn't be found.</p>
            capo_ram.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ram.types.update_resource_share_request.UpdateResourceShareRequest]",
        ) -> OperationResponse[
            "capo_ram.types.update_resource_share_response.UpdateResourceShareResponse"
        ]:
            import capo_ram._operations.amazon_resource_sharing.update_resource_share

            output, http_response = (
                capo_ram._operations.amazon_resource_sharing.update_resource_share.update_resource_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ram.types.update_resource_share_request.UpdateResourceShareRequest = {
            "resource_share_arn": resource_share_arn
        }
        if name is not None:
            input_["name"] = name
        if allow_external_principals is not None:
            input_["allow_external_principals"] = allow_external_principals
        if client_token is not None:
            input_["client_token"] = client_token

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
