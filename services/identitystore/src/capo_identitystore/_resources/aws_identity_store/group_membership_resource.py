from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_identitystore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_identitystore.types.create_group_membership_request
    import capo_identitystore.types.create_group_membership_response
    import capo_identitystore.types.delete_group_membership_request
    import capo_identitystore.types.delete_group_membership_response
    import capo_identitystore.types.describe_group_membership_request
    import capo_identitystore.types.describe_group_membership_response
    import capo_identitystore.types.get_group_membership_id_request
    import capo_identitystore.types.get_group_membership_id_response
    import capo_identitystore.types.group_ids
    import capo_identitystore.types.group_membership
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.is_member_in_groups_request
    import capo_identitystore.types.is_member_in_groups_response
    import capo_identitystore.types.list_group_memberships_for_member_request
    import capo_identitystore.types.list_group_memberships_for_member_response
    import capo_identitystore.types.list_group_memberships_request
    import capo_identitystore.types.list_group_memberships_response
    import capo_identitystore.types.max_results
    import capo_identitystore.types.member_id
    import capo_identitystore.types.next_token
    import capo_identitystore.types.resource_id
    from capo_identitystore._services.async_identitystore import (
        AsyncidentitystoreClient,
        AsyncidentitystoreClientConfig,
    )
    from capo_identitystore._services.identitystore import (
        identitystoreClient,
        identitystoreClientConfig,
    )


class GroupMembershipResource:
    def __init__(self, service: identitystoreClient) -> None:
        self._service = service

    def create(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.create_group_membership_response.CreateGroupMembershipResponse":
        """<p>Creates a relationship between a member and a group. The following identifiers must be specified: <code>GroupId</code>, <code>IdentityStoreId</code>, and <code>MemberId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.describe_group_membership_response.DescribeGroupMembershipResponse":
        """<p>Retrieves membership metadata and attributes from <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p> <p>You can specify the group membership by ID or by Amazon Resource Name (ARN). For example, membership ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code> or membership ARN <code>arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code>.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def delete(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.delete_group_membership_response.DeleteGroupMembershipResponse":
        """<p>Delete a membership within a group given <code>MembershipId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p> <p>You can specify the group membership by ID or by Amazon Resource Name (ARN). For example, membership ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code> or membership ARN <code>arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code>.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def list(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
    ) -> "capo_identitystore.types.list_group_memberships_response.ListGroupMembershipsResponse":
        """<p>For the specified group in the specified identity store, returns the list of all <code> GroupMembership</code> objects and returns results in paginated form.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in all <code> List</code> requests to specify how many results to return in one page.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code>, <code>ListGroups</code> and <code> ListGroupMemberships</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to retrieve the next page of results.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def get_group_membership_id(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.get_group_membership_id_response.GetGroupMembershipIdResponse":
        """<p>Retrieves the <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
        """<p>Checks the user's membership in all requested groups and returns if the member exists in all queried groups.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            member_id: <p>An object containing the identifier of a group member.</p>
            group_ids: <p>A list of identifiers for groups in the identity store.</p> <p>You can specify each group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
        """<p>For the specified member in the specified identity store, returns the list of all <code> GroupMembership</code> objects and returns results in paginated form.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in all <code>List</code> requests to specify how many results to return in one page.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code>, <code>ListGroups</code>, and <code> ListGroupMemberships</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to retrieve the next page of results.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncGroupMembershipResource:
    def __init__(self, service: AsyncidentitystoreClient) -> None:
        self._service = service

    async def create(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.create_group_membership_response.CreateGroupMembershipResponse":
        """<p>Creates a relationship between a member and a group. The following identifiers must be specified: <code>GroupId</code>, <code>IdentityStoreId</code>, and <code>MemberId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
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

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.create_group_membership_request.CreateGroupMembershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.create_group_membership_response.CreateGroupMembershipResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.create_group_membership

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.create_group_membership.async_create_group_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.create_group_membership_request.CreateGroupMembershipRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
            "member_id": member_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.describe_group_membership_response.DescribeGroupMembershipResponse":
        """<p>Retrieves membership metadata and attributes from <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p> <p>You can specify the group membership by ID or by Amazon Resource Name (ARN). For example, membership ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code> or membership ARN <code>arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.describe_group_membership_request.DescribeGroupMembershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.describe_group_membership_response.DescribeGroupMembershipResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.describe_group_membership

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.describe_group_membership.async_describe_group_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.describe_group_membership_request.DescribeGroupMembershipRequest = {
            "identity_store_id": identity_store_id,
            "membership_id": membership_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.delete_group_membership_response.DeleteGroupMembershipResponse":
        """<p>Delete a membership within a group given <code>MembershipId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p> <p>You can specify the group membership by ID or by Amazon Resource Name (ARN). For example, membership ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code> or membership ARN <code>arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.delete_group_membership_request.DeleteGroupMembershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.delete_group_membership_response.DeleteGroupMembershipResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.delete_group_membership

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.delete_group_membership.async_delete_group_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.delete_group_membership_request.DeleteGroupMembershipRequest = {
            "identity_store_id": identity_store_id,
            "membership_id": membership_id,
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
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
    ) -> "capo_identitystore.types.list_group_memberships_response.ListGroupMembershipsResponse":
        """<p>For the specified group in the specified identity store, returns the list of all <code> GroupMembership</code> objects and returns results in paginated form.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in all <code> List</code> requests to specify how many results to return in one page.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code>, <code>ListGroups</code> and <code> ListGroupMemberships</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to retrieve the next page of results.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.list_group_memberships_request.ListGroupMembershipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.list_group_memberships_response.ListGroupMembershipsResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.list_group_memberships

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.list_group_memberships.async_list_group_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.list_group_memberships_request.ListGroupMembershipsRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
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

    async def get_group_membership_id(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.get_group_membership_id_response.GetGroupMembershipIdResponse":
        """<p>Retrieves the <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.get_group_membership_id_request.GetGroupMembershipIdRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.get_group_membership_id_response.GetGroupMembershipIdResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.get_group_membership_id

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.get_group_membership_id.async_get_group_membership_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.get_group_membership_id_request.GetGroupMembershipIdRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
            "member_id": member_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def is_member_in_groups(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        group_ids: "capo_identitystore.types.group_ids.GroupIds",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> (
        "capo_identitystore.types.is_member_in_groups_response.IsMemberInGroupsResponse"
    ):
        """<p>Checks the user's membership in all requested groups and returns if the member exists in all queried groups.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            member_id: <p>An object containing the identifier of a group member.</p>
            group_ids: <p>A list of identifiers for groups in the identity store.</p> <p>You can specify each group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.is_member_in_groups_request.IsMemberInGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.is_member_in_groups_response.IsMemberInGroupsResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.is_member_in_groups

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.is_member_in_groups.async_is_member_in_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.is_member_in_groups_request.IsMemberInGroupsRequest = {
            "identity_store_id": identity_store_id,
            "member_id": member_id,
            "group_ids": group_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_group_memberships_for_member(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "capo_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
    ) -> "capo_identitystore.types.list_group_memberships_for_member_response.ListGroupMembershipsForMemberResponse":
        """<p>For the specified member in the specified identity store, returns the list of all <code> GroupMembership</code> objects and returns results in paginated form.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in all <code>List</code> requests to specify how many results to return in one page.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code>, <code>ListGroups</code>, and <code> ListGroupMemberships</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to retrieve the next page of results.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.list_group_memberships_for_member_request.ListGroupMembershipsForMemberRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.list_group_memberships_for_member_response.ListGroupMembershipsForMemberResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.list_group_memberships_for_member

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.list_group_memberships_for_member.async_list_group_memberships_for_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.list_group_memberships_for_member_request.ListGroupMembershipsForMemberRequest = {
            "identity_store_id": identity_store_id,
            "member_id": member_id,
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
