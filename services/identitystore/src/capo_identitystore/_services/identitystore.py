"""Generated from Smithy shape ``com.amazonaws.identitystore#AWSIdentityStore``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_identitystore._auth._signers
import capo_identitystore._auth._sigv4
from capo_identitystore._auth._identity import Credentials
from capo_identitystore._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_identitystore._auth._zapros_handler import AuthMiddleware
from capo_identitystore._pagination import resolve_path as _resolve_path
from capo_identitystore._resources.aws_identity_store.group_membership_resource import (
    GroupMembershipResource,
)
from capo_identitystore._resources.aws_identity_store.group_resource import (
    GroupResource,
)
from capo_identitystore._resources.aws_identity_store.user_resource import UserResource
from capo_identitystore._services._aws_config import aws_config
from capo_identitystore._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_identitystore.types.addresses
    import capo_identitystore.types.alternate_identifier
    import capo_identitystore.types.attribute_operations
    import capo_identitystore.types.create_group_membership_request
    import capo_identitystore.types.create_group_membership_response
    import capo_identitystore.types.create_group_request
    import capo_identitystore.types.create_group_response
    import capo_identitystore.types.create_user_request
    import capo_identitystore.types.create_user_response
    import capo_identitystore.types.delete_group_membership_request
    import capo_identitystore.types.delete_group_membership_response
    import capo_identitystore.types.delete_group_request
    import capo_identitystore.types.delete_group_response
    import capo_identitystore.types.delete_user_request
    import capo_identitystore.types.delete_user_response
    import capo_identitystore.types.describe_group_membership_request
    import capo_identitystore.types.describe_group_membership_response
    import capo_identitystore.types.describe_group_request
    import capo_identitystore.types.describe_group_response
    import capo_identitystore.types.describe_user_request
    import capo_identitystore.types.describe_user_response
    import capo_identitystore.types.emails
    import capo_identitystore.types.extension_names
    import capo_identitystore.types.extensions
    import capo_identitystore.types.filters
    import capo_identitystore.types.get_group_id_request
    import capo_identitystore.types.get_group_id_response
    import capo_identitystore.types.get_group_membership_id_request
    import capo_identitystore.types.get_group_membership_id_response
    import capo_identitystore.types.get_user_id_request
    import capo_identitystore.types.get_user_id_response
    import capo_identitystore.types.group
    import capo_identitystore.types.group_display_name
    import capo_identitystore.types.group_ids
    import capo_identitystore.types.group_membership
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.is_member_in_groups_request
    import capo_identitystore.types.is_member_in_groups_response
    import capo_identitystore.types.list_group_memberships_for_member_request
    import capo_identitystore.types.list_group_memberships_for_member_response
    import capo_identitystore.types.list_group_memberships_request
    import capo_identitystore.types.list_group_memberships_response
    import capo_identitystore.types.list_groups_request
    import capo_identitystore.types.list_groups_response
    import capo_identitystore.types.list_users_request
    import capo_identitystore.types.list_users_response
    import capo_identitystore.types.max_results
    import capo_identitystore.types.member_id
    import capo_identitystore.types.name
    import capo_identitystore.types.next_token
    import capo_identitystore.types.phone_numbers
    import capo_identitystore.types.photos
    import capo_identitystore.types.resource_id
    import capo_identitystore.types.roles
    import capo_identitystore.types.sensitive_string_type
    import capo_identitystore.types.update_group_request
    import capo_identitystore.types.update_group_response
    import capo_identitystore.types.update_user_request
    import capo_identitystore.types.update_user_response
    import capo_identitystore.types.user
    import capo_identitystore.types.user_name


class identitystoreClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class identitystoreClient:
    """A client for the ``identitystore`` service.

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
        self._config = identitystoreClientConfig(
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
        self.group_membership_resource = GroupMembershipResource(self)
        self.group_resource = GroupResource(self)
        self.user_resource = UserResource(self)

    def operation_options(
        self, config_overrides: Optional[identitystoreClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: identitystoreClientConfig = config_overrides or {}
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

    def get_group_id(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        alternate_identifier: "capo_identitystore.types.alternate_identifier.AlternateIdentifier",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.get_group_id_response.GetGroupIdResponse":
        r"""<p>Retrieves <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            alternate_identifier: <p>A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute. For the unique attribute, the only valid path is <code> displayName</code>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.get_group_id_request.GetGroupIdRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.get_group_id_response.GetGroupIdResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.get_group_id

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.get_group_id.get_group_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.get_group_id_request.GetGroupIdRequest = {
            "identity_store_id": identity_store_id,
            "alternate_identifier": alternate_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_group_membership_id(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.get_group_membership_id_response.GetGroupMembershipIdResponse":
        r"""<p>Retrieves the <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.get_group_membership_id_request.GetGroupMembershipIdRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.get_group_membership_id_response.GetGroupMembershipIdResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.get_group_membership_id

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.get_group_membership_id.get_group_membership_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.get_group_membership_id_request.GetGroupMembershipIdRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
            "member_id": member_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_user_id(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        alternate_identifier: "capo_identitystore.types.alternate_identifier.AlternateIdentifier",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.get_user_id_response.GetUserIdResponse":
        r"""<p>Retrieves the <code>UserId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            alternate_identifier: <p>A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute. For the unique attribute, the only valid paths are <code> userName</code> and <code>emails.value</code>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.get_user_id_request.GetUserIdRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.get_user_id_response.GetUserIdResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.get_user_id

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.get_user_id.get_user_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.get_user_id_request.GetUserIdRequest = {
            "identity_store_id": identity_store_id,
            "alternate_identifier": alternate_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def is_member_in_groups(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        group_ids: "capo_identitystore.types.group_ids.GroupIds",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> (
        "capo_identitystore.types.is_member_in_groups_response.IsMemberInGroupsResponse"
    ):
        r"""<p>Checks the user's membership in all requested groups and returns if the member exists in all queried groups.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            member_id: <p>An object containing the identifier of a group member.</p>
            group_ids: <p>A list of identifiers for groups in the identity store.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.is_member_in_groups_request.IsMemberInGroupsRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.is_member_in_groups_response.IsMemberInGroupsResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.is_member_in_groups

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.is_member_in_groups.is_member_in_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.is_member_in_groups_request.IsMemberInGroupsRequest = {
            "identity_store_id": identity_store_id,
            "member_id": member_id,
            "group_ids": group_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_group_memberships_for_member(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
    ) -> "capo_identitystore.types.list_group_memberships_for_member_response.ListGroupMembershipsForMemberResponse":
        r"""<p>For the specified member in the specified identity store, returns the list of all <code> GroupMembership</code> objects and returns results in paginated form.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in the <code> ListUsers</code> and <code>ListGroups</code> requests to specify how many results to return in one page. The length limit is 50 characters.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code>, <code>ListGroups</code>, and <code> ListGroupMemberships</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.list_group_memberships_for_member_request.ListGroupMembershipsForMemberRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.list_group_memberships_for_member_response.ListGroupMembershipsForMemberResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.list_group_memberships_for_member

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.list_group_memberships_for_member.list_group_memberships_for_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.list_group_memberships_for_member_request.ListGroupMembershipsForMemberRequest = {
            "identity_store_id": identity_store_id,
            "member_id": member_id,
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

    def iter_list_group_memberships_for_member(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_identitystore.types.group_membership.GroupMembership]":
        _token = next_token
        while True:
            _response = self.list_group_memberships_for_member(
                identity_store_id,
                member_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("group_memberships",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_group_membership(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.create_group_membership_response.CreateGroupMembershipResponse":
        """<p>Creates a relationship between a member and a group. The following identifiers must be specified: <code>GroupId</code>, <code>IdentityStoreId</code>, and <code>MemberId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.create_group_membership_request.CreateGroupMembershipRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.create_group_membership_response.CreateGroupMembershipResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.create_group_membership

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.create_group_membership.create_group_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.create_group_membership_request.CreateGroupMembershipRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
            "member_id": member_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_group_membership(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.describe_group_membership_response.DescribeGroupMembershipResponse":
        r"""<p>Retrieves membership metadata and attributes from <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.describe_group_membership_request.DescribeGroupMembershipRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.describe_group_membership_response.DescribeGroupMembershipResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.describe_group_membership

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.describe_group_membership.describe_group_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.describe_group_membership_request.DescribeGroupMembershipRequest = {
            "identity_store_id": identity_store_id,
            "membership_id": membership_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_group_membership(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.delete_group_membership_response.DeleteGroupMembershipResponse":
        """<p>Delete a membership within a group given <code>MembershipId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.delete_group_membership_request.DeleteGroupMembershipRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.delete_group_membership_response.DeleteGroupMembershipResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.delete_group_membership

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.delete_group_membership.delete_group_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.delete_group_membership_request.DeleteGroupMembershipRequest = {
            "identity_store_id": identity_store_id,
            "membership_id": membership_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_group_memberships(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
    ) -> "capo_identitystore.types.list_group_memberships_response.ListGroupMembershipsResponse":
        r"""<p>For the specified group in the specified identity store, returns the list of all <code> GroupMembership</code> objects and returns results in paginated form.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in all <code> List</code> requests to specify how many results to return in one page.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code>, <code>ListGroups</code> and <code> ListGroupMemberships</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.list_group_memberships_request.ListGroupMembershipsRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.list_group_memberships_response.ListGroupMembershipsResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.list_group_memberships

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.list_group_memberships.list_group_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.list_group_memberships_request.ListGroupMembershipsRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
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

    def iter_list_group_memberships(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_identitystore.types.group_membership.GroupMembership]":
        _token = next_token
        while True:
            _response = self.list_group_memberships(
                identity_store_id,
                group_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("group_memberships",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_group(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        display_name: Optional[
            "capo_identitystore.types.group_display_name.GroupDisplayName"
        ] = None,
        description: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
    ) -> "capo_identitystore.types.create_group_response.CreateGroupResponse":
        """<p>Creates a group within the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            display_name: <p>A string containing the name of the group. This value is commonly displayed when the group is referenced. <code>Administrator</code> and <code>AWSAdministrators</code> are reserved names and can't be used for users or groups.</p>
            description: <p>A string containing the description of the group.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.create_group_request.CreateGroupRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.create_group_response.CreateGroupResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.create_group

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.create_group.create_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.create_group_request.CreateGroupRequest = {
            "identity_store_id": identity_store_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_group(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.describe_group_response.DescribeGroupResponse":
        r"""<p>Retrieves the group metadata and attributes from <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            group_id: <p>The identifier for a group in the identity store.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.describe_group_request.DescribeGroupRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.describe_group_response.DescribeGroupResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.describe_group

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.describe_group.describe_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.describe_group_request.DescribeGroupRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_group(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        operations: "capo_identitystore.types.attribute_operations.AttributeOperations",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.update_group_response.UpdateGroupResponse":
        r"""<p>Updates the specified group metadata and attributes in the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            operations: <p>A list of <code>AttributeOperation</code> objects to apply to the requested group. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html\">Group</a>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.update_group_request.UpdateGroupRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.update_group_response.UpdateGroupResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.update_group

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.update_group.update_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.update_group_request.UpdateGroupRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
            "operations": operations,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_group(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.delete_group_response.DeleteGroupResponse":
        """<p>Delete a group within an identity store given <code>GroupId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.delete_group_request.DeleteGroupRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.delete_group_response.DeleteGroupResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.delete_group

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.delete_group.delete_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.delete_group_request.DeleteGroupRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_groups(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["capo_identitystore.types.filters.Filters"] = None,
    ) -> "capo_identitystore.types.list_groups_response.ListGroupsResponse":
        r"""<p>Lists all groups in the identity store. Returns a paginated list of complete <code>Group</code> objects. Filtering for a <code>Group</code> by the <code>DisplayName</code> attribute is deprecated. Instead, use the <code>GetGroupId</code> API action.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in the <code> ListUsers</code> and <code>ListGroups</code> requests to specify how many results to return in one page. The length limit is 50 characters.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code> and <code>ListGroups</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>
            filters: <p>A list of <code>Filter</code> objects, which is used in the <code>ListUsers</code> and <code> ListGroups</code> requests.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.list_groups_request.ListGroupsRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.list_groups_response.ListGroupsResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.list_groups

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.list_groups.list_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.list_groups_request.ListGroupsRequest = {
            "identity_store_id": identity_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_groups(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["capo_identitystore.types.filters.Filters"] = None,
    ) -> "Iterator[capo_identitystore.types.group.Group]":
        _token = next_token
        while True:
            _response = self.list_groups(
                identity_store_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_user(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        user_name: Optional["capo_identitystore.types.user_name.UserName"] = None,
        name: Optional["capo_identitystore.types.name.Name"] = None,
        display_name: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        nick_name: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        profile_url: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        emails: Optional["capo_identitystore.types.emails.Emails"] = None,
        addresses: Optional["capo_identitystore.types.addresses.Addresses"] = None,
        phone_numbers: Optional[
            "capo_identitystore.types.phone_numbers.PhoneNumbers"
        ] = None,
        user_type: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        title: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        preferred_language: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        locale: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        timezone: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        photos: Optional["capo_identitystore.types.photos.Photos"] = None,
        website: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        birthdate: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        roles: Optional["capo_identitystore.types.roles.Roles"] = None,
        extensions: Optional["capo_identitystore.types.extensions.Extensions"] = None,
    ) -> "capo_identitystore.types.create_user_response.CreateUserResponse":
        r"""<p>Creates a user within the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            user_name: <p>A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store. <code>Administrator</code> and <code>AWSAdministrators</code> are reserved names and can't be used for users or groups.</p>
            name: <p>An object containing the name of the user. When used in IAM Identity Center, this parameter is required.</p>
            display_name: <p>A string containing the name of the user. This value is typically formatted for display when the user is referenced. For example, \"John Doe.\" When used in IAM Identity Center, this parameter is required.</p>
            nick_name: <p>A string containing an alternate name for the user.</p>
            profile_url: <p>A string containing a URL that might be associated with the user.</p>
            emails: <p>A list of <code>Email</code> objects containing email addresses associated with the user.</p>
            addresses: <p>A list of <code>Address</code> objects containing addresses associated with the user.</p>
            phone_numbers: <p>A list of <code>PhoneNumber</code> objects containing phone numbers associated with the user.</p>
            user_type: <p>A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case.</p>
            title: <p>A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case.</p>
            preferred_language: <p>A string containing the preferred language of the user. For example, \"American English\" or \"en-us.\"</p>
            locale: <p>A string containing the geographical region or location of the user.</p>
            timezone: <p>A string containing the time zone of the user.</p>
            photos: <p>A list of photos associated with the user. You can add up to 3 photos per user. Each photo can include a value, type, display name, and primary designation.</p>
            website: <p>The user's personal website or blog URL. This field allows users to provide a link to their personal or professional website.</p>
            birthdate: <p>The user's birthdate in YYYY-MM-DD format. This field supports standard date format for storing personal information.</p>
            roles: <p>A list of <code>Role</code> objects containing roles associated with the user.</p>
            extensions: <p>A map with additional attribute extensions for the user. Each map key corresponds to an extension name, while map values represent extension data in <code>Document</code> type (not supported by Java V1, Go V1 and older versions of the CLI). <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.create_user_response.CreateUserResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.create_user

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.create_user_request.CreateUserRequest = {
            "identity_store_id": identity_store_id
        }
        if user_name is not None:
            input_["user_name"] = user_name
        if name is not None:
            input_["name"] = name
        if display_name is not None:
            input_["display_name"] = display_name
        if nick_name is not None:
            input_["nick_name"] = nick_name
        if profile_url is not None:
            input_["profile_url"] = profile_url
        if emails is not None:
            input_["emails"] = emails
        if addresses is not None:
            input_["addresses"] = addresses
        if phone_numbers is not None:
            input_["phone_numbers"] = phone_numbers
        if user_type is not None:
            input_["user_type"] = user_type
        if title is not None:
            input_["title"] = title
        if preferred_language is not None:
            input_["preferred_language"] = preferred_language
        if locale is not None:
            input_["locale"] = locale
        if timezone is not None:
            input_["timezone"] = timezone
        if photos is not None:
            input_["photos"] = photos
        if website is not None:
            input_["website"] = website
        if birthdate is not None:
            input_["birthdate"] = birthdate
        if roles is not None:
            input_["roles"] = roles
        if extensions is not None:
            input_["extensions"] = extensions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_user(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        user_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        extensions: Optional[
            "capo_identitystore.types.extension_names.ExtensionNames"
        ] = None,
    ) -> "capo_identitystore.types.describe_user_response.DescribeUserResponse":
        r"""<p>Retrieves the user metadata and attributes from the <code>UserId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            user_id: <p>The identifier for a user in the identity store.</p>
            extensions: <p>A collection of extension names indicating what extensions the service should retrieve alongside other user attributes. <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.describe_user_request.DescribeUserRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.describe_user_response.DescribeUserResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.describe_user

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.describe_user.describe_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.describe_user_request.DescribeUserRequest = {
            "identity_store_id": identity_store_id,
            "user_id": user_id,
        }
        if extensions is not None:
            input_["extensions"] = extensions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_user(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        user_id: "capo_identitystore.types.resource_id.ResourceId",
        operations: "capo_identitystore.types.attribute_operations.AttributeOperations",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.update_user_response.UpdateUserResponse":
        r"""<p>Updates the specified user metadata and attributes in the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            user_id: <p>The identifier for a user in the identity store.</p>
            operations: <p>A list of <code>AttributeOperation</code> objects to apply to the requested user. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html\">User</a>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.update_user_response.UpdateUserResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.update_user

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.update_user_request.UpdateUserRequest = {
            "identity_store_id": identity_store_id,
            "user_id": user_id,
            "operations": operations,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_user(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        user_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes a user within an identity store given <code>UserId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            user_id: <p>The identifier for a user in the identity store.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.delete_user_response.DeleteUserResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.delete_user

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.delete_user_request.DeleteUserRequest = {
            "identity_store_id": identity_store_id,
            "user_id": user_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_users(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        extensions: Optional[
            "capo_identitystore.types.extension_names.ExtensionNames"
        ] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["capo_identitystore.types.filters.Filters"] = None,
    ) -> "capo_identitystore.types.list_users_response.ListUsersResponse":
        r"""<p>Lists all users in the identity store. Returns a paginated list of complete <code>User</code> objects. Filtering for a <code>User</code> by the <code>UserName</code> attribute is deprecated. Instead, use the <code>GetUserId</code> API action.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            extensions: <p>A collection of extension names indicating what extensions the service should retrieve alongside other user attributes. <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in the <code> ListUsers</code> and <code>ListGroups</code> requests to specify how many results to return in one page. The length limit is 50 characters.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code> and <code>ListGroups</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>
            filters: <p>A list of <code>Filter</code> objects, which is used in the <code>ListUsers</code> and <code> ListGroups</code> requests. </p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.list_users_response.ListUsersResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.list_users

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.list_users.list_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_identitystore.types.list_users_request.ListUsersRequest = {
            "identity_store_id": identity_store_id
        }
        if extensions is not None:
            input_["extensions"] = extensions
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_users(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        extensions: Optional[
            "capo_identitystore.types.extension_names.ExtensionNames"
        ] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["capo_identitystore.types.filters.Filters"] = None,
    ) -> "Iterator[capo_identitystore.types.user.User]":
        _token = next_token
        while True:
            _response = self.list_users(
                identity_store_id,
                config_overrides=config_overrides,
                extensions=extensions,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
