from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_verifiedpermissions._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.alias
    import capo_verifiedpermissions.types.create_policy_store_alias_input
    import capo_verifiedpermissions.types.create_policy_store_alias_output
    import capo_verifiedpermissions.types.delete_policy_store_alias_input
    import capo_verifiedpermissions.types.delete_policy_store_alias_output
    import capo_verifiedpermissions.types.deletion_mode
    import capo_verifiedpermissions.types.get_policy_store_alias_input
    import capo_verifiedpermissions.types.get_policy_store_alias_output
    import capo_verifiedpermissions.types.list_policy_store_aliases_input
    import capo_verifiedpermissions.types.list_policy_store_aliases_output
    import capo_verifiedpermissions.types.max_results
    import capo_verifiedpermissions.types.next_token
    import capo_verifiedpermissions.types.policy_store_alias_filter
    import capo_verifiedpermissions.types.policy_store_alias_item
    import capo_verifiedpermissions.types.policy_store_id
    from capo_verifiedpermissions._services.async_verified_permissions import (
        AsyncVerifiedPermissionsClient,
        AsyncVerifiedPermissionsClientConfig,
    )
    from capo_verifiedpermissions._services.verified_permissions import (
        VerifiedPermissionsClient,
        VerifiedPermissionsClientConfig,
    )


class PolicyStoreAlias:
    def __init__(self, service: VerifiedPermissionsClient) -> None:
        self._service = service

    def put(
        self,
        alias_name: "capo_verifiedpermissions.types.alias.Alias",
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.create_policy_store_alias_output.CreatePolicyStoreAliasOutput":
        """<p>Creates a policy store alias for the specified policy store. A policy store alias is an alternative identifier that you can use to reference a policy store in API operations.</p> <p>This operation is idempotent. If multiple CreatePolicyStoreAlias requests are made where the <code>aliasName</code> and <code>policyStoreId</code> fields are the same between the requests, subsequent requests will be ignored. For each duplicate CreatePolicyStoreAlias request, a Success response will be returned and a new policy store alias will not be created.</p> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            alias_name: <p>Specifies the name of the policy store alias to create. The name must be unique within your Amazon Web Services account and Amazon Web Services Region.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>
            policy_store_id: <p>Specifies the ID of the policy store to associate with the alias.</p> <note> <p>The associated policy store must be specified using its ID. The alias name cannot be used.</p> </note>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because it would cause a service quota to be exceeded.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreatePolicyStoreAlias
            The following example creates a new policy store alias.

            >>> client.put(alias_name='policy-store-alias/example-policy-store', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.create_policy_store_alias_input.CreatePolicyStoreAliasInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.create_policy_store_alias_output.CreatePolicyStoreAliasOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.create_policy_store_alias

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.create_policy_store_alias.create_policy_store_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.create_policy_store_alias_input.CreatePolicyStoreAliasInput = {
            "alias_name": alias_name,
            "policy_store_id": policy_store_id,
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
        alias_name: "capo_verifiedpermissions.types.alias.Alias",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.get_policy_store_alias_output.GetPolicyStoreAliasOutput":
        """<p>Retrieves details about the specified policy store alias.</p>

        Args:
            alias_name: <p>Specifies the name of the policy store alias that you want information about.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetPolicyStoreAlias
            The following example retrieves details about the policy store alias with name example-policy-store.

            >>> client.read(alias_name='policy-store-alias/example-policy-store')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.get_policy_store_alias_input.GetPolicyStoreAliasInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.get_policy_store_alias_output.GetPolicyStoreAliasOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.get_policy_store_alias

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.get_policy_store_alias.get_policy_store_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.get_policy_store_alias_input.GetPolicyStoreAliasInput = {
            "alias_name": alias_name
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
        alias_name: "capo_verifiedpermissions.types.alias.Alias",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        deletion_mode: Optional[
            "capo_verifiedpermissions.types.deletion_mode.DeletionMode"
        ] = None,
    ) -> "capo_verifiedpermissions.types.delete_policy_store_alias_output.DeletePolicyStoreAliasOutput":
        """<p>Deletes the specified policy store alias.</p> <p>This operation is idempotent. If you specify a policy store alias that does not exist, the request response will still return a successful HTTP 200 status code.</p> <p>By default, when a policy store alias is deleted, it enters the <code>PendingDeletion</code> state. When a policy store alias is in the <code>PendingDeletion</code> state, new policy store aliases cannot be created with the same name. If the policy store alias is used in an API that has a <code>policyStoreId</code> field, the operation will fail with a <code>ResourceNotFound</code> exception.</p> <p>To immediately delete a policy store alias and bypass the <code>PendingDeletion</code> state, set the <code>deletionMode</code> parameter to <code>HardDelete</code>.</p> <important> <p>Verified Permissions is eventually consistent. If you hard delete a policy store alias and then immediately recreate it to be associated with a different policy store, requests that reference this alias may continue to be evaluated against the previously associated policy store for a short period of time.</p> </important>

        Args:
            alias_name: <p>Specifies the name of the policy store alias that you want to delete.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>
            deletion_mode: <p>Specifies the deletion mode for the policy store alias. The valid values are:</p> <ul> <li> <p> <b>SoftDelete</b> – The policy store alias enters the <code>PendingDeletion</code> state. This is the default behavior when no <code>deletionMode</code> is specified.</p> </li> <li> <p> <b>HardDelete</b> – The policy store alias is immediately deleted, bypassing the <code>PendingDeletion</code> state.</p> </li> </ul>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.invalid_state_exception.InvalidStateException: <p>The policy store can't be deleted because deletion protection is enabled. To delete this policy store, disable deletion protection.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Soft delete a policy store alias
            The following example soft deletes the policy store alias with name example-policy-store. The alias enters the PendingDeletion state.

            >>> client.delete(alias_name='policy-store-alias/example-policy-store')
            Hard delete a policy store alias
            The following example hard deletes the policy store alias with name example-policy-store. The alias is immediately deleted, bypassing the PendingDeletion state.

            >>> client.delete(alias_name='policy-store-alias/example-policy-store', deletion_mode='HardDelete')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.delete_policy_store_alias_input.DeletePolicyStoreAliasInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.delete_policy_store_alias_output.DeletePolicyStoreAliasOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.delete_policy_store_alias

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.delete_policy_store_alias.delete_policy_store_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.delete_policy_store_alias_input.DeletePolicyStoreAliasInput = {
            "alias_name": alias_name
        }
        if deletion_mode is not None:
            input_["deletion_mode"] = deletion_mode

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
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "capo_verifiedpermissions.types.policy_store_alias_filter.PolicyStoreAliasFilter"
        ] = None,
    ) -> "capo_verifiedpermissions.types.list_policy_store_aliases_output.ListPolicyStoreAliasesOutput":
        """<p>Returns a paginated list of all policy store aliases in the calling Amazon Web Services account.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 5 policy store aliases per response. You can specify a maximum of 50 policy store aliases per response.</p>
            filter: <p>Specifies a filter to narrow the results. You can filter by <code>policyStoreId</code> to list only the policy store aliases associated with a specific policy store.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListPolicyStoreAliases - Example 1
            The following example lists all policy store aliases in the AWS account in the AWS Region in which you call the operation.

            >>> client.list()
            ListPolicyStoreAliases - Example 2
            The following example lists all policy store aliases associated with the policy store with ID C7v5xMplfFH3i3e4Jrzb1a

            >>> client.list(filter={'policyStoreId': 'C7v5xMplfFH3i3e4Jrzb1a'})
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.list_policy_store_aliases_input.ListPolicyStoreAliasesInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.list_policy_store_aliases_output.ListPolicyStoreAliasesOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.list_policy_store_aliases

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.list_policy_store_aliases.list_policy_store_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.list_policy_store_aliases_input.ListPolicyStoreAliasesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPolicyStoreAlias:
    def __init__(self, service: AsyncVerifiedPermissionsClient) -> None:
        self._service = service

    async def put(
        self,
        alias_name: "capo_verifiedpermissions.types.alias.Alias",
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.create_policy_store_alias_output.CreatePolicyStoreAliasOutput":
        """<p>Creates a policy store alias for the specified policy store. A policy store alias is an alternative identifier that you can use to reference a policy store in API operations.</p> <p>This operation is idempotent. If multiple CreatePolicyStoreAlias requests are made where the <code>aliasName</code> and <code>policyStoreId</code> fields are the same between the requests, subsequent requests will be ignored. For each duplicate CreatePolicyStoreAlias request, a Success response will be returned and a new policy store alias will not be created.</p> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            alias_name: <p>Specifies the name of the policy store alias to create. The name must be unique within your Amazon Web Services account and Amazon Web Services Region.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>
            policy_store_id: <p>Specifies the ID of the policy store to associate with the alias.</p> <note> <p>The associated policy store must be specified using its ID. The alias name cannot be used.</p> </note>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because it would cause a service quota to be exceeded.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreatePolicyStoreAlias
            The following example creates a new policy store alias.

            >>> await client.put(alias_name='policy-store-alias/example-policy-store', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.create_policy_store_alias_input.CreatePolicyStoreAliasInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.create_policy_store_alias_output.CreatePolicyStoreAliasOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.create_policy_store_alias

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.create_policy_store_alias.async_create_policy_store_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.create_policy_store_alias_input.CreatePolicyStoreAliasInput = {
            "alias_name": alias_name,
            "policy_store_id": policy_store_id,
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
        alias_name: "capo_verifiedpermissions.types.alias.Alias",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.get_policy_store_alias_output.GetPolicyStoreAliasOutput":
        """<p>Retrieves details about the specified policy store alias.</p>

        Args:
            alias_name: <p>Specifies the name of the policy store alias that you want information about.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetPolicyStoreAlias
            The following example retrieves details about the policy store alias with name example-policy-store.

            >>> await client.read(alias_name='policy-store-alias/example-policy-store')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.get_policy_store_alias_input.GetPolicyStoreAliasInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.get_policy_store_alias_output.GetPolicyStoreAliasOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.get_policy_store_alias

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.get_policy_store_alias.async_get_policy_store_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.get_policy_store_alias_input.GetPolicyStoreAliasInput = {
            "alias_name": alias_name
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
        alias_name: "capo_verifiedpermissions.types.alias.Alias",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        deletion_mode: Optional[
            "capo_verifiedpermissions.types.deletion_mode.DeletionMode"
        ] = None,
    ) -> "capo_verifiedpermissions.types.delete_policy_store_alias_output.DeletePolicyStoreAliasOutput":
        """<p>Deletes the specified policy store alias.</p> <p>This operation is idempotent. If you specify a policy store alias that does not exist, the request response will still return a successful HTTP 200 status code.</p> <p>By default, when a policy store alias is deleted, it enters the <code>PendingDeletion</code> state. When a policy store alias is in the <code>PendingDeletion</code> state, new policy store aliases cannot be created with the same name. If the policy store alias is used in an API that has a <code>policyStoreId</code> field, the operation will fail with a <code>ResourceNotFound</code> exception.</p> <p>To immediately delete a policy store alias and bypass the <code>PendingDeletion</code> state, set the <code>deletionMode</code> parameter to <code>HardDelete</code>.</p> <important> <p>Verified Permissions is eventually consistent. If you hard delete a policy store alias and then immediately recreate it to be associated with a different policy store, requests that reference this alias may continue to be evaluated against the previously associated policy store for a short period of time.</p> </important>

        Args:
            alias_name: <p>Specifies the name of the policy store alias that you want to delete.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>
            deletion_mode: <p>Specifies the deletion mode for the policy store alias. The valid values are:</p> <ul> <li> <p> <b>SoftDelete</b> – The policy store alias enters the <code>PendingDeletion</code> state. This is the default behavior when no <code>deletionMode</code> is specified.</p> </li> <li> <p> <b>HardDelete</b> – The policy store alias is immediately deleted, bypassing the <code>PendingDeletion</code> state.</p> </li> </ul>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.invalid_state_exception.InvalidStateException: <p>The policy store can't be deleted because deletion protection is enabled. To delete this policy store, disable deletion protection.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Soft delete a policy store alias
            The following example soft deletes the policy store alias with name example-policy-store. The alias enters the PendingDeletion state.

            >>> await client.delete(alias_name='policy-store-alias/example-policy-store')
            Hard delete a policy store alias
            The following example hard deletes the policy store alias with name example-policy-store. The alias is immediately deleted, bypassing the PendingDeletion state.

            >>> await client.delete(alias_name='policy-store-alias/example-policy-store', deletion_mode='HardDelete')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.delete_policy_store_alias_input.DeletePolicyStoreAliasInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.delete_policy_store_alias_output.DeletePolicyStoreAliasOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.delete_policy_store_alias

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.delete_policy_store_alias.async_delete_policy_store_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.delete_policy_store_alias_input.DeletePolicyStoreAliasInput = {
            "alias_name": alias_name
        }
        if deletion_mode is not None:
            input_["deletion_mode"] = deletion_mode

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
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "capo_verifiedpermissions.types.policy_store_alias_filter.PolicyStoreAliasFilter"
        ] = None,
    ) -> "capo_verifiedpermissions.types.list_policy_store_aliases_output.ListPolicyStoreAliasesOutput":
        """<p>Returns a paginated list of all policy store aliases in the calling Amazon Web Services account.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 5 policy store aliases per response. You can specify a maximum of 50 policy store aliases per response.</p>
            filter: <p>Specifies a filter to narrow the results. You can filter by <code>policyStoreId</code> to list only the policy store aliases associated with a specific policy store.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListPolicyStoreAliases - Example 1
            The following example lists all policy store aliases in the AWS account in the AWS Region in which you call the operation.

            >>> await client.list()
            ListPolicyStoreAliases - Example 2
            The following example lists all policy store aliases associated with the policy store with ID C7v5xMplfFH3i3e4Jrzb1a

            >>> await client.list(filter={'policyStoreId': 'C7v5xMplfFH3i3e4Jrzb1a'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.list_policy_store_aliases_input.ListPolicyStoreAliasesInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.list_policy_store_aliases_output.ListPolicyStoreAliasesOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.list_policy_store_aliases

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.list_policy_store_aliases.async_list_policy_store_aliases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.list_policy_store_aliases_input.ListPolicyStoreAliasesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
