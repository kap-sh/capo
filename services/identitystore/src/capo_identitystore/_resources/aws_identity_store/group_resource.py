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
    import capo_identitystore.types.alternate_identifier
    import capo_identitystore.types.attribute_operations
    import capo_identitystore.types.create_group_request
    import capo_identitystore.types.create_group_response
    import capo_identitystore.types.delete_group_request
    import capo_identitystore.types.delete_group_response
    import capo_identitystore.types.describe_group_request
    import capo_identitystore.types.describe_group_response
    import capo_identitystore.types.filters
    import capo_identitystore.types.get_group_id_request
    import capo_identitystore.types.get_group_id_response
    import capo_identitystore.types.group
    import capo_identitystore.types.group_display_name
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.list_groups_request
    import capo_identitystore.types.list_groups_response
    import capo_identitystore.types.max_results
    import capo_identitystore.types.next_token
    import capo_identitystore.types.resource_id
    import capo_identitystore.types.resource_revision
    import capo_identitystore.types.sensitive_string_type
    import capo_identitystore.types.update_group_request
    import capo_identitystore.types.update_group_response
    from capo_identitystore._services.async_identitystore import (
        AsyncidentitystoreClient,
        AsyncidentitystoreClientConfig,
    )
    from capo_identitystore._services.identitystore import (
        identitystoreClient,
        identitystoreClientConfig,
    )


class GroupResource:
    def __init__(self, service: identitystoreClient) -> None:
        self._service = service

    def create(
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
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.describe_group_response.DescribeGroupResponse":
        """<p>Retrieves the group metadata and attributes from <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def update(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        operations: "capo_identitystore.types.attribute_operations.AttributeOperations",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        revision: Optional[
            "capo_identitystore.types.resource_revision.ResourceRevision"
        ] = None,
    ) -> "capo_identitystore.types.update_group_response.UpdateGroupResponse":
        """<p>Updates the specified group metadata and attributes in the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
            operations: <p>A list of <code>AttributeOperation</code> objects to apply to the requested group. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html">Group</a>.</p>
            revision: <p>The expected current revision of the group. When you provide this value, the update is applied only if it matches the current revision of the group in the identity store, which prevents you from overwriting concurrent changes. If the value doesn't match, the operation fails with a <code>ConflictException</code>. If you don't provide this value, the update is applied unconditionally.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.update_group_request.UpdateGroupRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
            "operations": operations,
        }
        if revision is not None:
            input_["revision"] = revision

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
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        revision: Optional[
            "capo_identitystore.types.resource_revision.ResourceRevision"
        ] = None,
    ) -> "capo_identitystore.types.delete_group_response.DeleteGroupResponse":
        """<p>Delete a group within an identity store given <code>GroupId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
            revision: <p>The expected current revision of the group. When you provide this value, the group is deleted only if it matches the current revision of the group in the identity store. If the value doesn't match, the operation fails with a <code>ConflictException</code>. If you don't provide this value, the group is deleted regardless of its current revision.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.delete_group_request.DeleteGroupRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
        }
        if revision is not None:
            input_["revision"] = revision

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
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["capo_identitystore.types.filters.Filters"] = None,
    ) -> "capo_identitystore.types.list_groups_response.ListGroupsResponse":
        """<p>Lists all groups in the identity store. Returns a paginated list of complete <code>Group</code> objects. Filtering for a <code>Group</code> by the <code>DisplayName</code> attribute is deprecated. Instead, use the <code>GetGroupId</code> API action.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in all <code>List</code> requests to specify how many results to return in one page.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code> and <code>ListGroups</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to retrieve the next page of results.</p>
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def get_group_id(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        alternate_identifier: "capo_identitystore.types.alternate_identifier.AlternateIdentifier",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.get_group_id_response.GetGroupIdResponse":
        """<p>Retrieves <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncGroupResource:
    def __init__(self, service: AsyncidentitystoreClient) -> None:
        self._service = service

    async def create(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        display_name: Optional[
            "capo_identitystore.types.group_display_name.GroupDisplayName"
        ] = None,
        description: Optional[
            "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
    ) -> "capo_identitystore.types.create_group_response.CreateGroupResponse":
        """<p>Creates a group within the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
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

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.create_group_request.CreateGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.create_group_response.CreateGroupResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.create_group

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.create_group.async_create_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.create_group_request.CreateGroupRequest = {
            "identity_store_id": identity_store_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description

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
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.describe_group_response.DescribeGroupResponse":
        """<p>Retrieves the group metadata and attributes from <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.describe_group_request.DescribeGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.describe_group_response.DescribeGroupResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.describe_group

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.describe_group.async_describe_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.describe_group_request.DescribeGroupRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
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
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        operations: "capo_identitystore.types.attribute_operations.AttributeOperations",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        revision: Optional[
            "capo_identitystore.types.resource_revision.ResourceRevision"
        ] = None,
    ) -> "capo_identitystore.types.update_group_response.UpdateGroupResponse":
        """<p>Updates the specified group metadata and attributes in the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
            operations: <p>A list of <code>AttributeOperation</code> objects to apply to the requested group. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html">Group</a>.</p>
            revision: <p>The expected current revision of the group. When you provide this value, the update is applied only if it matches the current revision of the group in the identity store, which prevents you from overwriting concurrent changes. If the value doesn't match, the operation fails with a <code>ConflictException</code>. If you don't provide this value, the update is applied unconditionally.</p>

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
            req: "AsyncOperationRequest[capo_identitystore.types.update_group_request.UpdateGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.update_group_response.UpdateGroupResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.update_group

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.update_group.async_update_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.update_group_request.UpdateGroupRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
            "operations": operations,
        }
        if revision is not None:
            input_["revision"] = revision

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
        group_id: "capo_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        revision: Optional[
            "capo_identitystore.types.resource_revision.ResourceRevision"
        ] = None,
    ) -> "capo_identitystore.types.delete_group_response.DeleteGroupResponse":
        """<p>Delete a group within an identity store given <code>GroupId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            group_id: <p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>
            revision: <p>The expected current revision of the group. When you provide this value, the group is deleted only if it matches the current revision of the group in the identity store. If the value doesn't match, the operation fails with a <code>ConflictException</code>. If you don't provide this value, the group is deleted regardless of its current revision.</p>

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
            req: "AsyncOperationRequest[capo_identitystore.types.delete_group_request.DeleteGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.delete_group_response.DeleteGroupResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.delete_group

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.delete_group.async_delete_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.delete_group_request.DeleteGroupRequest = {
            "identity_store_id": identity_store_id,
            "group_id": group_id,
        }
        if revision is not None:
            input_["revision"] = revision

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
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["capo_identitystore.types.filters.Filters"] = None,
    ) -> "capo_identitystore.types.list_groups_response.ListGroupsResponse":
        """<p>Lists all groups in the identity store. Returns a paginated list of complete <code>Group</code> objects. Filtering for a <code>Group</code> by the <code>DisplayName</code> attribute is deprecated. Instead, use the <code>GetGroupId</code> API action.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in all <code>List</code> requests to specify how many results to return in one page.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code> and <code>ListGroups</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to retrieve the next page of results.</p>
            filters: <p>A list of <code>Filter</code> objects, which is used in the <code>ListUsers</code> and <code> ListGroups</code> requests.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.list_groups_request.ListGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.list_groups_response.ListGroupsResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.list_groups

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.list_groups.async_list_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.list_groups_request.ListGroupsRequest = {
            "identity_store_id": identity_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group_id(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        alternate_identifier: "capo_identitystore.types.alternate_identifier.AlternateIdentifier",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.get_group_id_response.GetGroupIdResponse":
        """<p>Retrieves <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            alternate_identifier: <p>A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute. For the unique attribute, the only valid path is <code> displayName</code>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.get_group_id_request.GetGroupIdRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.get_group_id_response.GetGroupIdResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.get_group_id

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.get_group_id.async_get_group_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.get_group_id_request.GetGroupIdRequest = {
            "identity_store_id": identity_store_id,
            "alternate_identifier": alternate_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
