from __future__ import annotations

import uuid
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
    import capo_verifiedpermissions.types.action_identifier
    import capo_verifiedpermissions.types.batch_get_policy_input
    import capo_verifiedpermissions.types.batch_get_policy_input_list
    import capo_verifiedpermissions.types.batch_get_policy_output
    import capo_verifiedpermissions.types.batch_is_authorized_input
    import capo_verifiedpermissions.types.batch_is_authorized_input_list
    import capo_verifiedpermissions.types.batch_is_authorized_output
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_input
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_input_list
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_output
    import capo_verifiedpermissions.types.context_definition
    import capo_verifiedpermissions.types.create_policy_store_input
    import capo_verifiedpermissions.types.create_policy_store_output
    import capo_verifiedpermissions.types.delete_policy_store_input
    import capo_verifiedpermissions.types.delete_policy_store_output
    import capo_verifiedpermissions.types.deletion_protection
    import capo_verifiedpermissions.types.encryption_settings
    import capo_verifiedpermissions.types.entities_definition
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.get_policy_store_input
    import capo_verifiedpermissions.types.get_policy_store_output
    import capo_verifiedpermissions.types.get_schema_input
    import capo_verifiedpermissions.types.get_schema_output
    import capo_verifiedpermissions.types.idempotency_token
    import capo_verifiedpermissions.types.is_authorized_input
    import capo_verifiedpermissions.types.is_authorized_output
    import capo_verifiedpermissions.types.is_authorized_with_token_input
    import capo_verifiedpermissions.types.is_authorized_with_token_output
    import capo_verifiedpermissions.types.list_policy_stores_input
    import capo_verifiedpermissions.types.list_policy_stores_output
    import capo_verifiedpermissions.types.max_results
    import capo_verifiedpermissions.types.next_token
    import capo_verifiedpermissions.types.policy_store_description
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_store_item
    import capo_verifiedpermissions.types.put_schema_input
    import capo_verifiedpermissions.types.put_schema_output
    import capo_verifiedpermissions.types.schema_definition
    import capo_verifiedpermissions.types.tag_map
    import capo_verifiedpermissions.types.token
    import capo_verifiedpermissions.types.update_policy_store_input
    import capo_verifiedpermissions.types.update_policy_store_output
    import capo_verifiedpermissions.types.validation_settings
    from capo_verifiedpermissions._services.async_verified_permissions import (
        AsyncVerifiedPermissionsClient,
        AsyncVerifiedPermissionsClientConfig,
    )
    from capo_verifiedpermissions._services.verified_permissions import (
        VerifiedPermissionsClient,
        VerifiedPermissionsClientConfig,
    )


class PolicyStore:
    def __init__(self, service: VerifiedPermissionsClient) -> None:
        self._service = service

    def create(
        self,
        validation_settings: "capo_verifiedpermissions.types.validation_settings.ValidationSettings",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        client_token: Optional[
            "capo_verifiedpermissions.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "capo_verifiedpermissions.types.policy_store_description.PolicyStoreDescription"
        ] = None,
        deletion_protection: Optional[
            "capo_verifiedpermissions.types.deletion_protection.DeletionProtection"
        ] = None,
        encryption_settings: Optional[
            "capo_verifiedpermissions.types.encryption_settings.EncryptionSettings"
        ] = None,
        tags: Optional["capo_verifiedpermissions.types.tag_map.TagMap"] = None,
    ) -> "capo_verifiedpermissions.types.create_policy_store_output.CreatePolicyStoreOutput":
        """<p>Creates a policy store. A policy store is a container for policy resources.</p> <note> <p>As of May 2026, Verified Permissions has aligned with Cedar and now supports multiple namespaces.</p> </note> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            client_token: <p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>ConflictException</code> error.</p> <p>Verified Permissions recognizes a <code>ClientToken</code> for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of <code>ClientToken</code>.</p>
            validation_settings: <p>Specifies the validation setting for this policy store.</p> <p>Currently, the only valid and required value is <code>Mode</code>.</p> <important> <p>We recommend that you turn on <code>STRICT</code> mode only after you define a schema. If a schema doesn't exist, then <code>STRICT</code> mode causes any policy to fail validation, and Verified Permissions rejects the policy. You can turn off validation by using the <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore">UpdatePolicyStore</a>. Then, when you have a schema defined, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore">UpdatePolicyStore</a> again to turn validation back on.</p> </important>
            description: <p>Descriptive text that you can provide to help with identification of the current policy store.</p>
            deletion_protection: <p>Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.</p> <p>The default state is <code>DISABLED</code>.</p>
            encryption_settings: <p>Specifies the encryption settings used to encrypt the policy store and their child resources. Allows for the ability to use a customer owned KMS key for encryption of data.</p> <p>This is an optional field to be used when providing a customer-managed KMS key for encryption.</p>
            tags: <p>The list of key-value pairs to associate with the policy store.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because it would cause a service quota to be exceeded.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create policy store
            The following example creates a new policy store with strict validation turned on.

            >>> client.create(validation_settings={'mode': 'STRICT'}, client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111')
            To create an encrypted policy store
            The following example creates a new policy store with encryption settings based on a provided KMS key.

            >>> client.create(validation_settings={'mode': 'STRICT'}, encryption_settings={'kmsEncryptionSettings': {'key': 'arn:aws:kms:us-east-1:123456789012:key/abcdefgh-ijkl-mnop-qrst-uvwxyz123456', 'encryptionContext': {'policy_store_owner': 'Tim'}}}, client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.create_policy_store_input.CreatePolicyStoreInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.create_policy_store_output.CreatePolicyStoreOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.create_policy_store

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.create_policy_store.create_policy_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.create_policy_store_input.CreatePolicyStoreInput = {
            "validation_settings": validation_settings
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if encryption_settings is not None:
            input_["encryption_settings"] = encryption_settings
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        tags: Optional[bool] = None,
    ) -> "capo_verifiedpermissions.types.get_policy_store_output.GetPolicyStoreOutput":
        """<p>Retrieves details about a policy store.</p>

        Args:
            policy_store_id: <p>Specifies the policy store that you want information about.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            tags: <p>Specifies whether to return the tags that are attached to the policy store. If this parameter is included in the API call, the tags are returned, otherwise they are not returned.</p> <note> <p>If this parameter is included in the API call but there are no tags attached to the policy store, the <code>tags</code> response parameter is omitted from the response.</p> </note>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetPolicyStore
            The following example retrieves details about the specified policy store.

            >>> client.read(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
            GetPolicyStore that is encrypted
            The following example retrieves details about the specified encrypted policy store.

            >>> client.read(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.get_policy_store_input.GetPolicyStoreInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.get_policy_store_output.GetPolicyStoreOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.get_policy_store

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.get_policy_store.get_policy_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.get_policy_store_input.GetPolicyStoreInput = {
            "policy_store_id": policy_store_id
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        validation_settings: "capo_verifiedpermissions.types.validation_settings.ValidationSettings",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        deletion_protection: Optional[
            "capo_verifiedpermissions.types.deletion_protection.DeletionProtection"
        ] = None,
        description: Optional[
            "capo_verifiedpermissions.types.policy_store_description.PolicyStoreDescription"
        ] = None,
    ) -> "capo_verifiedpermissions.types.update_policy_store_output.UpdatePolicyStoreOutput":
        """<p>Modifies the validation setting for a policy store.</p> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that you want to update</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            validation_settings: <p>A structure that defines the validation settings that want to enable for the policy store.</p>
            deletion_protection: <p>Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.</p> <p>When you call <code>UpdatePolicyStore</code>, this parameter is unchanged unless explicitly included in the call.</p>
            description: <p>Descriptive text that you can provide to help with identification of the current policy store.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdatePolicyStore
            The following example turns off the validation settings for a policy store.

            >>> client.update(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', validation_settings={'mode': 'OFF'})
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.update_policy_store_input.UpdatePolicyStoreInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.update_policy_store_output.UpdatePolicyStoreOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.update_policy_store

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.update_policy_store.update_policy_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.update_policy_store_input.UpdatePolicyStoreInput = {
            "policy_store_id": policy_store_id,
            "validation_settings": validation_settings,
        }
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.delete_policy_store_output.DeletePolicyStoreOutput":
        """<p>Deletes the specified policy store.</p> <p>This operation is idempotent. If you specify a policy store that does not exist, the request response will still return a successful HTTP 200 status code.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that you want to delete.</p> <note> <p>To specify a policy store, the alias name cannot be used. Only the ID can be used.</p> </note>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.invalid_state_exception.InvalidStateException: <p>The policy store can't be deleted because deletion protection is enabled. To delete this policy store, disable deletion protection.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a policy store
            The following example deletes the specified policy store.

            >>> client.delete(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.delete_policy_store_input.DeletePolicyStoreInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.delete_policy_store_output.DeletePolicyStoreOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.delete_policy_store

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.delete_policy_store.delete_policy_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.delete_policy_store_input.DeletePolicyStoreInput = {
            "policy_store_id": policy_store_id
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
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_verifiedpermissions.types.list_policy_stores_output.ListPolicyStoresOutput":
        """<p>Returns a paginated list of all policy stores in the calling Amazon Web Services account.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 10 policy stores per response. You can specify a maximum of 50 policy stores per response.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListPolicyStores
            The following example lists all policy stores in the AWS account in the AWS Region in which you call the operation.

            >>> client.list()
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.list_policy_stores_input.ListPolicyStoresInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.list_policy_stores_output.ListPolicyStoresOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.list_policy_stores

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.list_policy_stores.list_policy_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.list_policy_stores_input.ListPolicyStoresInput = {}
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

    def batch_is_authorized(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        requests: "capo_verifiedpermissions.types.batch_is_authorized_input_list.BatchIsAuthorizedInputList",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        entities: Optional[
            "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
        ] = None,
    ) -> "capo_verifiedpermissions.types.batch_is_authorized_output.BatchIsAuthorizedOutput":
        """<p>Makes a series of decisions about multiple authorization requests for one principal or resource. Each request contains the equivalent content of an <code>IsAuthorized</code> request: principal, action, resource, and context. Either the <code>principal</code> or the <code>resource</code> parameter must be identical across all requests. For example, Verified Permissions won't evaluate a pair of requests where <code>bob</code> views <code>photo1</code> and <code>alice</code> views <code>photo2</code>. Authorization of <code>bob</code> to view <code>photo1</code> and <code>photo2</code>, or <code>bob</code> and <code>alice</code> to view <code>photo1</code>, are valid batches. </p> <p>The request is evaluated against all policies in the specified policy store that match the entities that you declare. The result of the decisions is a series of <code>Allow</code> or <code>Deny</code> responses, along with the IDs of the policies that produced each decision.</p> <p>The <code>entities</code> of a <code>BatchIsAuthorized</code> API request can contain up to 100 principals and up to 100 resources. The <code>requests</code> of a <code>BatchIsAuthorized</code> API request can contain up to 30 requests.</p> <note> <p>The <code>BatchIsAuthorized</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>verifiedpermissions:IsAuthorized</code> in their IAM policies.</p> </note>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store. Policies in this policy store will be used to make the authorization decisions for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            entities: <p>(Optional) Specifies the list of resources and principals and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <note> <p>You can include only principal and resource entities in this parameter; you can't include actions. You must specify actions in the schema.</p> </note>
            requests: <p>An array of up to 30 requests that you want Verified Permissions to evaluate.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Batch - Example 1
            The following example requests two authorization decisions for two principals                     of type Usernamed Alice and Annalisa.

            >>> client.batch_is_authorized(requests=[{'principal': {'entityType': 'PhotoFlash::User', 'entityId': 'Alice'}, 'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'ViewPhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}}, {'principal': {'entityType': 'PhotoFlash::User', 'entityId': 'Annalisa'}, 'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'DeletePhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}}], entities={'entityList': [{'identifier': {'entityType': 'PhotoFlash::User', 'entityId': 'Alice'}, 'attributes': {'Account': {'entityIdentifier': {'entityType': 'PhotoFlash::Account', 'entityId': '1234'}}, 'Email': {'string': ''}}, 'parents': []}, {'identifier': {'entityType': 'PhotoFlash::User', 'entityId': 'Annalisa'}, 'attributes': {'Account': {'entityIdentifier': {'entityType': 'PhotoFlash::Account', 'entityId': '5678'}}, 'Email': {'string': ''}}, 'parents': []}, {'identifier': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}, 'attributes': {'IsPrivate': {'boolean': False}, 'Name': {'string': ''}}, 'parents': [{'entityType': 'PhotoFlash::Account', 'entityId': '1234'}]}, {'identifier': {'entityType': 'PhotoFlash::Account', 'entityId': '1234'}, 'attributes': {'Name': {'string': ''}}, 'parents': []}]}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.batch_is_authorized_input.BatchIsAuthorizedInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.batch_is_authorized_output.BatchIsAuthorizedOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.batch_is_authorized

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.batch_is_authorized.batch_is_authorized(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.batch_is_authorized_input.BatchIsAuthorizedInput = {
            "policy_store_id": policy_store_id,
            "requests": requests,
        }
        if entities is not None:
            input_["entities"] = entities

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_is_authorized_with_token(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        requests: "capo_verifiedpermissions.types.batch_is_authorized_with_token_input_list.BatchIsAuthorizedWithTokenInputList",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        identity_token: Optional["capo_verifiedpermissions.types.token.Token"] = None,
        access_token: Optional["capo_verifiedpermissions.types.token.Token"] = None,
        entities: Optional[
            "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
        ] = None,
    ) -> "capo_verifiedpermissions.types.batch_is_authorized_with_token_output.BatchIsAuthorizedWithTokenOutput":
        """<p>Makes a series of decisions about multiple authorization requests for one token. The principal in this request comes from an external identity source in the form of an identity or access token, formatted as a <a href="https://wikipedia.org/wiki/JSON_Web_Token">JSON web token (JWT)</a>. The information in the parameters can also define additional context that Verified Permissions can include in the evaluations.</p> <p>The request is evaluated against all policies in the specified policy store that match the entities that you provide in the entities declaration and in the token. The result of the decisions is a series of <code>Allow</code> or <code>Deny</code> responses, along with the IDs of the policies that produced each decision.</p> <p>The <code>entities</code> of a <code>BatchIsAuthorizedWithToken</code> API request can contain up to 100 resources and up to 99 user groups. The <code>requests</code> of a <code>BatchIsAuthorizedWithToken</code> API request can contain up to 30 requests.</p> <note> <p>The <code>BatchIsAuthorizedWithToken</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>verifiedpermissions:IsAuthorizedWithToken</code> in their IAM policies.</p> </note>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            identity_token: <p>Specifies an identity (ID) token for the principal that you want to authorize in each request. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an ID token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>id</code>.</p>
            access_token: <p>Specifies an access token for the principal that you want to authorize in each request. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an access token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>access</code>.</p>
            entities: <p>(Optional) Specifies the list of resources and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <important> <p>You can't include principals in this parameter, only resource and action entities. This parameter can't include any entities of a type that matches the user or group entity types that you defined in your identity source.</p> <ul> <li> <p>The <code>BatchIsAuthorizedWithToken</code> operation takes principal attributes from <b> <i>only</i> </b> the <code>identityToken</code> or <code>accessToken</code> passed to the operation.</p> </li> <li> <p>For action entities, you can include only their <code>Identifier</code> and <code>EntityType</code>. </p> </li> </ul> </important>
            requests: <p>An array of up to 30 requests that you want Verified Permissions to evaluate.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Batch - Example 1
            The following example requests three authorization decisions for two resources                     and two actions in different photo albums.

            >>> client.batch_is_authorized_with_token(identity_token='eyJra12345EXAMPLE', requests=[{'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'ViewPhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}}, {'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'SharePhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}}, {'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'ViewPhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'OfficePhoto94.jpg'}}], entities={'entityList': [{'identifier': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}, 'parents': [{'entityType': 'PhotoFlash::Album', 'entityId': 'MyExampleAlbum1'}]}, {'identifier': {'entityType': 'PhotoFlash::Photo', 'entityId': 'OfficePhoto94.jpg'}, 'parents': [{'entityType': 'PhotoFlash::Album', 'entityId': 'MyExampleAlbum2'}]}]}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.batch_is_authorized_with_token_input.BatchIsAuthorizedWithTokenInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.batch_is_authorized_with_token_output.BatchIsAuthorizedWithTokenOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.batch_is_authorized_with_token

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.batch_is_authorized_with_token.batch_is_authorized_with_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.batch_is_authorized_with_token_input.BatchIsAuthorizedWithTokenInput = {
            "policy_store_id": policy_store_id,
            "requests": requests,
        }
        if identity_token is not None:
            input_["identity_token"] = identity_token
        if access_token is not None:
            input_["access_token"] = access_token
        if entities is not None:
            input_["entities"] = entities

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_schema(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.get_schema_output.GetSchemaOutput":
        r"""<p>Retrieve the details for the specified schema in the specified policy store.</p>

                Args:
                    policy_store_id: <p>Specifies the ID of the policy store that contains the schema.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>

                Raises:
                    capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
                    capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
                    capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
                    capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
                    capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
                    capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    GetSchema
                    The following example retrieves the current schema stored in the specified policy store.

        Note
        The JSON in the parameters of this operation are strings that can contain embedded quotation marks (") within the outermost quotation mark pair. This requires that you stringify the JSON object by preceding all embedded quotation marks with a backslash character ( \" ) and combining all lines into a single text line with no line breaks.

        Example strings might be displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

                    >>> client.get_schema(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.get_schema_input.GetSchemaInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.get_schema_output.GetSchemaOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.get_schema

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.get_schema.get_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.get_schema_input.GetSchemaInput = {
            "policy_store_id": policy_store_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def is_authorized(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        principal: Optional[
            "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
        ] = None,
        action: Optional[
            "capo_verifiedpermissions.types.action_identifier.ActionIdentifier"
        ] = None,
        resource: Optional[
            "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
        ] = None,
        context: Optional[
            "capo_verifiedpermissions.types.context_definition.ContextDefinition"
        ] = None,
        entities: Optional[
            "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
        ] = None,
    ) -> "capo_verifiedpermissions.types.is_authorized_output.IsAuthorizedOutput":
        """<p>Makes an authorization decision about a service request described in the parameters. The information in the parameters can also define additional context that Verified Permissions can include in the evaluation. The request is evaluated against all matching policies in the specified policy store. The result of the decision is either <code>Allow</code> or <code>Deny</code>, along with a list of the policies that resulted in the decision.</p>

                Args:
                    policy_store_id: <p>Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
                    principal: <p>Specifies the principal for which the authorization decision is to be made.</p>
                    action: <p>Specifies the requested action to be authorized. For example, is the principal authorized to perform this action on the resource?</p>
                    resource: <p>Specifies the resource for which the authorization decision is to be made.</p>
                    context: <p>Specifies additional context that can be used to make more granular authorization decisions.</p>
                    entities: <p>(Optional) Specifies the list of resources and principals and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <note> <p>You can include only principal and resource entities in this parameter; you can't include actions. You must specify actions in the schema.</p> </note>

                Raises:
                    capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
                    capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
                    capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
                    capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
                    capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
                    capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    IsAuthorized - Example 1
                    The following example requests an authorization decision for a principal of type User named Alice, who wants to perform the updatePhoto operation, on a resource of type Photo named VacationPhoto94.jpg.

        The response shows that the request was allowed by one policy.

                    >>> client.is_authorized(principal={'entityType': 'User', 'entityId': 'alice'}, action={'actionType': 'Action', 'actionId': 'updatePhoto'}, resource={'entityType': 'Photo', 'entityId': 'VacationPhoto94.jpg'}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
                    IsAuthorized - Example 2
                    The following example is the same as the previous example, except that the principal is User::"bob", and the policy store doesn't contain any policy that allows that user access to Album::"alice_folder". The output infers that the Deny was implicit because the list of DeterminingPolicies is empty.

                    >>> client.is_authorized(principal={'entityType': 'User', 'entityId': 'bob'}, action={'actionType': 'Action', 'actionId': 'view'}, resource={'entityType': 'Photo', 'entityId': 'VacationPhoto94.jpg'}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.is_authorized_input.IsAuthorizedInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.is_authorized_output.IsAuthorizedOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.is_authorized

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.is_authorized.is_authorized(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.is_authorized_input.IsAuthorizedInput = {
            "policy_store_id": policy_store_id
        }
        if principal is not None:
            input_["principal"] = principal
        if action is not None:
            input_["action"] = action
        if resource is not None:
            input_["resource"] = resource
        if context is not None:
            input_["context"] = context
        if entities is not None:
            input_["entities"] = entities

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def is_authorized_with_token(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        identity_token: Optional["capo_verifiedpermissions.types.token.Token"] = None,
        access_token: Optional["capo_verifiedpermissions.types.token.Token"] = None,
        action: Optional[
            "capo_verifiedpermissions.types.action_identifier.ActionIdentifier"
        ] = None,
        resource: Optional[
            "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
        ] = None,
        context: Optional[
            "capo_verifiedpermissions.types.context_definition.ContextDefinition"
        ] = None,
        entities: Optional[
            "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
        ] = None,
    ) -> "capo_verifiedpermissions.types.is_authorized_with_token_output.IsAuthorizedWithTokenOutput":
        """<p>Makes an authorization decision about a service request described in the parameters. The principal in this request comes from an external identity source in the form of an identity token formatted as a <a href="https://wikipedia.org/wiki/JSON_Web_Token">JSON web token (JWT)</a>. The information in the parameters can also define additional context that Verified Permissions can include in the evaluation. The request is evaluated against all matching policies in the specified policy store. The result of the decision is either <code>Allow</code> or <code>Deny</code>, along with a list of the policies that resulted in the decision.</p> <p>Verified Permissions validates each token that is specified in a request by checking its expiration date and its signature.</p> <important> <p>Tokens from an identity source user continue to be usable until they expire. Token revocation and resource deletion have no effect on the validity of a token in your policy store</p> </important>

                Args:
                    policy_store_id: <p>Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
                    identity_token: <p>Specifies an identity token for the principal to be authorized. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an ID token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>id</code>.</p>
                    access_token: <p>Specifies an access token for the principal to be authorized. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an access token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>access</code>.</p>
                    action: <p>Specifies the requested action to be authorized. Is the specified principal authorized to perform this action on the specified resource.</p>
                    resource: <p>Specifies the resource for which the authorization decision is made. For example, is the principal allowed to perform the action on the resource?</p>
                    context: <p>Specifies additional context that can be used to make more granular authorization decisions.</p>
                    entities: <p>(Optional) Specifies the list of resources and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <important> <p>You can't include principals in this parameter, only resource and action entities. This parameter can't include any entities of a type that matches the user or group entity types that you defined in your identity source.</p> <ul> <li> <p>The <code>IsAuthorizedWithToken</code> operation takes principal attributes from <b> <i>only</i> </b> the <code>identityToken</code> or <code>accessToken</code> passed to the operation.</p> </li> <li> <p>For action entities, you can include only their <code>Identifier</code> and <code>EntityType</code>. </p> </li> </ul> </important>

                Raises:
                    capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
                    capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
                    capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
                    capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
                    capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
                    capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    IsAuthorizedWithToken - Example 1
                    The following example requests an authorization decision for a user who was authenticated by Amazon Cognito. The request uses the identity token provided by Amazon Cognito instead of the access token. In this example, the specified information store is configured to return principals as entities of type CognitoUser. The policy store contains a policy with the following statement.

        permit(
            principal == CognitoUser::"us-east-1_1a2b3c4d5|a1b2c3d4e5f6g7h8i9j0kalbmc",
            action,
            resource == Photo::"VacationPhoto94.jpg"
        );

                    >>> client.is_authorized_with_token(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', action={'actionId': 'View', 'actionType': 'Action'}, resource={'entityId': 'vacationPhoto94.jpg', 'entityType': 'Photo'}, identity_token='EgZjxMPlbWUyBggAEEUYOdIBCDM3NDlqMGo3qAIAsAIA')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.is_authorized_with_token_input.IsAuthorizedWithTokenInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.is_authorized_with_token_output.IsAuthorizedWithTokenOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.is_authorized_with_token

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.is_authorized_with_token.is_authorized_with_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.is_authorized_with_token_input.IsAuthorizedWithTokenInput = {
            "policy_store_id": policy_store_id
        }
        if identity_token is not None:
            input_["identity_token"] = identity_token
        if access_token is not None:
            input_["access_token"] = access_token
        if action is not None:
            input_["action"] = action
        if resource is not None:
            input_["resource"] = resource
        if context is not None:
            input_["context"] = context
        if entities is not None:
            input_["entities"] = entities

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_schema(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        definition: "capo_verifiedpermissions.types.schema_definition.SchemaDefinition",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.put_schema_output.PutSchemaOutput":
        r"""<p>Creates or updates the policy schema in the specified policy store. The schema is used to validate any Cedar policies and policy templates submitted to the policy store. Any changes to the schema validate only policies and templates submitted after the schema change. Existing policies and templates are not re-evaluated against the changed schema. If you later update a policy, then it is evaluated against the new schema at that time.</p> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

                Args:
                    policy_store_id: <p>Specifies the ID of the policy store in which to place the schema.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
                    definition: <p>Specifies the definition of the schema to be stored. The schema definition must be written in Cedar schema JSON.</p>

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
                    PutSchema
                    The following example creates a new schema, or updates an existing schema, in the specified policy store. Note that the schema text is shown line wrapped for readability. You should submit the entire schema text as a single line of text.

        Note
        The JSON in the parameters of this operation are strings that can contain embedded quotation marks (") within the outermost quotation mark pair. This requires that you stringify the JSON object by preceding all embedded quotation marks with a backslash character ( \" ) and combining all lines into a single text line with no line breaks.

        Example strings might be displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

                    >>> client.put_schema(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', definition={'cedarJson': '{"MySampleNamespace": {"actions": {"remoteAccess": {"appliesTo": {"principalTypes": ["Employee"]}}},"entityTypes": {"Employee": {"shape": {"attributes": {"jobLevel": {"type": "Long"},"name": {"type": "String"}},"type": "Record"}}}}}'})
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.put_schema_input.PutSchemaInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.put_schema_output.PutSchemaOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.put_schema

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.put_schema.put_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.put_schema_input.PutSchemaInput = {
            "policy_store_id": policy_store_id,
            "definition": definition,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_policy(
        self,
        requests: "capo_verifiedpermissions.types.batch_get_policy_input_list.BatchGetPolicyInputList",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.batch_get_policy_output.BatchGetPolicyOutput":
        """<p>Retrieves information about a group (batch) of policies.</p> <note> <p>The <code>BatchGetPolicy</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>verifiedpermissions:GetPolicy</code> in their IAM policies.</p> </note>

        Args:
            requests: <p>An array of up to 100 policies you want information about.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve details about a policy
            The following example retrieves information about the specified policy contained in the specified policy store. In this example, the requested policy is a template-linked policy, so it returns the ID of the policy template, and the specific principal and resource used by this policy.

            >>> client.batch_get_policy(requests=[{'policyId': 'PWv5M6d5HePx3gVVLKY1nK', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}, {'policyId': 'LzFn6KgLWvv4Mbegus35jn', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}, {'policyId': '77gLjer8H5o3mvrnMGrSL5', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}])
            To retrieve policies by name
            The following example retrieves information about policies using their names instead of their IDs.

            >>> client.batch_get_policy(requests=[{'policyId': 'name/example-policy', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}, {'policyId': 'name/example-policy-2', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}])
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.batch_get_policy_input.BatchGetPolicyInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.batch_get_policy_output.BatchGetPolicyOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.batch_get_policy

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.batch_get_policy.batch_get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.batch_get_policy_input.BatchGetPolicyInput = {
            "requests": requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPolicyStore:
    def __init__(self, service: AsyncVerifiedPermissionsClient) -> None:
        self._service = service

    async def create(
        self,
        validation_settings: "capo_verifiedpermissions.types.validation_settings.ValidationSettings",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        client_token: Optional[
            "capo_verifiedpermissions.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "capo_verifiedpermissions.types.policy_store_description.PolicyStoreDescription"
        ] = None,
        deletion_protection: Optional[
            "capo_verifiedpermissions.types.deletion_protection.DeletionProtection"
        ] = None,
        encryption_settings: Optional[
            "capo_verifiedpermissions.types.encryption_settings.EncryptionSettings"
        ] = None,
        tags: Optional["capo_verifiedpermissions.types.tag_map.TagMap"] = None,
    ) -> "capo_verifiedpermissions.types.create_policy_store_output.CreatePolicyStoreOutput":
        """<p>Creates a policy store. A policy store is a container for policy resources.</p> <note> <p>As of May 2026, Verified Permissions has aligned with Cedar and now supports multiple namespaces.</p> </note> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            client_token: <p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>ConflictException</code> error.</p> <p>Verified Permissions recognizes a <code>ClientToken</code> for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of <code>ClientToken</code>.</p>
            validation_settings: <p>Specifies the validation setting for this policy store.</p> <p>Currently, the only valid and required value is <code>Mode</code>.</p> <important> <p>We recommend that you turn on <code>STRICT</code> mode only after you define a schema. If a schema doesn't exist, then <code>STRICT</code> mode causes any policy to fail validation, and Verified Permissions rejects the policy. You can turn off validation by using the <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore">UpdatePolicyStore</a>. Then, when you have a schema defined, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore">UpdatePolicyStore</a> again to turn validation back on.</p> </important>
            description: <p>Descriptive text that you can provide to help with identification of the current policy store.</p>
            deletion_protection: <p>Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.</p> <p>The default state is <code>DISABLED</code>.</p>
            encryption_settings: <p>Specifies the encryption settings used to encrypt the policy store and their child resources. Allows for the ability to use a customer owned KMS key for encryption of data.</p> <p>This is an optional field to be used when providing a customer-managed KMS key for encryption.</p>
            tags: <p>The list of key-value pairs to associate with the policy store.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because it would cause a service quota to be exceeded.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create policy store
            The following example creates a new policy store with strict validation turned on.

            >>> await client.create(validation_settings={'mode': 'STRICT'}, client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111')
            To create an encrypted policy store
            The following example creates a new policy store with encryption settings based on a provided KMS key.

            >>> await client.create(validation_settings={'mode': 'STRICT'}, encryption_settings={'kmsEncryptionSettings': {'key': 'arn:aws:kms:us-east-1:123456789012:key/abcdefgh-ijkl-mnop-qrst-uvwxyz123456', 'encryptionContext': {'policy_store_owner': 'Tim'}}}, client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.create_policy_store_input.CreatePolicyStoreInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.create_policy_store_output.CreatePolicyStoreOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.create_policy_store

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.create_policy_store.async_create_policy_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.create_policy_store_input.CreatePolicyStoreInput = {
            "validation_settings": validation_settings
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if encryption_settings is not None:
            input_["encryption_settings"] = encryption_settings
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        tags: Optional[bool] = None,
    ) -> "capo_verifiedpermissions.types.get_policy_store_output.GetPolicyStoreOutput":
        """<p>Retrieves details about a policy store.</p>

        Args:
            policy_store_id: <p>Specifies the policy store that you want information about.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            tags: <p>Specifies whether to return the tags that are attached to the policy store. If this parameter is included in the API call, the tags are returned, otherwise they are not returned.</p> <note> <p>If this parameter is included in the API call but there are no tags attached to the policy store, the <code>tags</code> response parameter is omitted from the response.</p> </note>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetPolicyStore
            The following example retrieves details about the specified policy store.

            >>> await client.read(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
            GetPolicyStore that is encrypted
            The following example retrieves details about the specified encrypted policy store.

            >>> await client.read(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.get_policy_store_input.GetPolicyStoreInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.get_policy_store_output.GetPolicyStoreOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.get_policy_store

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.get_policy_store.async_get_policy_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.get_policy_store_input.GetPolicyStoreInput = {
            "policy_store_id": policy_store_id
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        validation_settings: "capo_verifiedpermissions.types.validation_settings.ValidationSettings",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        deletion_protection: Optional[
            "capo_verifiedpermissions.types.deletion_protection.DeletionProtection"
        ] = None,
        description: Optional[
            "capo_verifiedpermissions.types.policy_store_description.PolicyStoreDescription"
        ] = None,
    ) -> "capo_verifiedpermissions.types.update_policy_store_output.UpdatePolicyStoreOutput":
        """<p>Modifies the validation setting for a policy store.</p> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that you want to update</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            validation_settings: <p>A structure that defines the validation settings that want to enable for the policy store.</p>
            deletion_protection: <p>Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.</p> <p>When you call <code>UpdatePolicyStore</code>, this parameter is unchanged unless explicitly included in the call.</p>
            description: <p>Descriptive text that you can provide to help with identification of the current policy store.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdatePolicyStore
            The following example turns off the validation settings for a policy store.

            >>> await client.update(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', validation_settings={'mode': 'OFF'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.update_policy_store_input.UpdatePolicyStoreInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.update_policy_store_output.UpdatePolicyStoreOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.update_policy_store

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.update_policy_store.async_update_policy_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.update_policy_store_input.UpdatePolicyStoreInput = {
            "policy_store_id": policy_store_id,
            "validation_settings": validation_settings,
        }
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.delete_policy_store_output.DeletePolicyStoreOutput":
        """<p>Deletes the specified policy store.</p> <p>This operation is idempotent. If you specify a policy store that does not exist, the request response will still return a successful HTTP 200 status code.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that you want to delete.</p> <note> <p>To specify a policy store, the alias name cannot be used. Only the ID can be used.</p> </note>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.invalid_state_exception.InvalidStateException: <p>The policy store can't be deleted because deletion protection is enabled. To delete this policy store, disable deletion protection.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a policy store
            The following example deletes the specified policy store.

            >>> await client.delete(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.delete_policy_store_input.DeletePolicyStoreInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.delete_policy_store_output.DeletePolicyStoreOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.delete_policy_store

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.delete_policy_store.async_delete_policy_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.delete_policy_store_input.DeletePolicyStoreInput = {
            "policy_store_id": policy_store_id
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
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_verifiedpermissions.types.list_policy_stores_output.ListPolicyStoresOutput":
        """<p>Returns a paginated list of all policy stores in the calling Amazon Web Services account.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 10 policy stores per response. You can specify a maximum of 50 policy stores per response.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListPolicyStores
            The following example lists all policy stores in the AWS account in the AWS Region in which you call the operation.

            >>> await client.list()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.list_policy_stores_input.ListPolicyStoresInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.list_policy_stores_output.ListPolicyStoresOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.list_policy_stores

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.list_policy_stores.async_list_policy_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.list_policy_stores_input.ListPolicyStoresInput = {}
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

    async def batch_is_authorized(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        requests: "capo_verifiedpermissions.types.batch_is_authorized_input_list.BatchIsAuthorizedInputList",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        entities: Optional[
            "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
        ] = None,
    ) -> "capo_verifiedpermissions.types.batch_is_authorized_output.BatchIsAuthorizedOutput":
        """<p>Makes a series of decisions about multiple authorization requests for one principal or resource. Each request contains the equivalent content of an <code>IsAuthorized</code> request: principal, action, resource, and context. Either the <code>principal</code> or the <code>resource</code> parameter must be identical across all requests. For example, Verified Permissions won't evaluate a pair of requests where <code>bob</code> views <code>photo1</code> and <code>alice</code> views <code>photo2</code>. Authorization of <code>bob</code> to view <code>photo1</code> and <code>photo2</code>, or <code>bob</code> and <code>alice</code> to view <code>photo1</code>, are valid batches. </p> <p>The request is evaluated against all policies in the specified policy store that match the entities that you declare. The result of the decisions is a series of <code>Allow</code> or <code>Deny</code> responses, along with the IDs of the policies that produced each decision.</p> <p>The <code>entities</code> of a <code>BatchIsAuthorized</code> API request can contain up to 100 principals and up to 100 resources. The <code>requests</code> of a <code>BatchIsAuthorized</code> API request can contain up to 30 requests.</p> <note> <p>The <code>BatchIsAuthorized</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>verifiedpermissions:IsAuthorized</code> in their IAM policies.</p> </note>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store. Policies in this policy store will be used to make the authorization decisions for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            entities: <p>(Optional) Specifies the list of resources and principals and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <note> <p>You can include only principal and resource entities in this parameter; you can't include actions. You must specify actions in the schema.</p> </note>
            requests: <p>An array of up to 30 requests that you want Verified Permissions to evaluate.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Batch - Example 1
            The following example requests two authorization decisions for two principals                     of type Usernamed Alice and Annalisa.

            >>> await client.batch_is_authorized(requests=[{'principal': {'entityType': 'PhotoFlash::User', 'entityId': 'Alice'}, 'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'ViewPhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}}, {'principal': {'entityType': 'PhotoFlash::User', 'entityId': 'Annalisa'}, 'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'DeletePhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}}], entities={'entityList': [{'identifier': {'entityType': 'PhotoFlash::User', 'entityId': 'Alice'}, 'attributes': {'Account': {'entityIdentifier': {'entityType': 'PhotoFlash::Account', 'entityId': '1234'}}, 'Email': {'string': ''}}, 'parents': []}, {'identifier': {'entityType': 'PhotoFlash::User', 'entityId': 'Annalisa'}, 'attributes': {'Account': {'entityIdentifier': {'entityType': 'PhotoFlash::Account', 'entityId': '5678'}}, 'Email': {'string': ''}}, 'parents': []}, {'identifier': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}, 'attributes': {'IsPrivate': {'boolean': False}, 'Name': {'string': ''}}, 'parents': [{'entityType': 'PhotoFlash::Account', 'entityId': '1234'}]}, {'identifier': {'entityType': 'PhotoFlash::Account', 'entityId': '1234'}, 'attributes': {'Name': {'string': ''}}, 'parents': []}]}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.batch_is_authorized_input.BatchIsAuthorizedInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.batch_is_authorized_output.BatchIsAuthorizedOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.batch_is_authorized

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.batch_is_authorized.async_batch_is_authorized(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.batch_is_authorized_input.BatchIsAuthorizedInput = {
            "policy_store_id": policy_store_id,
            "requests": requests,
        }
        if entities is not None:
            input_["entities"] = entities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_is_authorized_with_token(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        requests: "capo_verifiedpermissions.types.batch_is_authorized_with_token_input_list.BatchIsAuthorizedWithTokenInputList",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        identity_token: Optional["capo_verifiedpermissions.types.token.Token"] = None,
        access_token: Optional["capo_verifiedpermissions.types.token.Token"] = None,
        entities: Optional[
            "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
        ] = None,
    ) -> "capo_verifiedpermissions.types.batch_is_authorized_with_token_output.BatchIsAuthorizedWithTokenOutput":
        """<p>Makes a series of decisions about multiple authorization requests for one token. The principal in this request comes from an external identity source in the form of an identity or access token, formatted as a <a href="https://wikipedia.org/wiki/JSON_Web_Token">JSON web token (JWT)</a>. The information in the parameters can also define additional context that Verified Permissions can include in the evaluations.</p> <p>The request is evaluated against all policies in the specified policy store that match the entities that you provide in the entities declaration and in the token. The result of the decisions is a series of <code>Allow</code> or <code>Deny</code> responses, along with the IDs of the policies that produced each decision.</p> <p>The <code>entities</code> of a <code>BatchIsAuthorizedWithToken</code> API request can contain up to 100 resources and up to 99 user groups. The <code>requests</code> of a <code>BatchIsAuthorizedWithToken</code> API request can contain up to 30 requests.</p> <note> <p>The <code>BatchIsAuthorizedWithToken</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>verifiedpermissions:IsAuthorizedWithToken</code> in their IAM policies.</p> </note>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            identity_token: <p>Specifies an identity (ID) token for the principal that you want to authorize in each request. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an ID token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>id</code>.</p>
            access_token: <p>Specifies an access token for the principal that you want to authorize in each request. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an access token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>access</code>.</p>
            entities: <p>(Optional) Specifies the list of resources and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <important> <p>You can't include principals in this parameter, only resource and action entities. This parameter can't include any entities of a type that matches the user or group entity types that you defined in your identity source.</p> <ul> <li> <p>The <code>BatchIsAuthorizedWithToken</code> operation takes principal attributes from <b> <i>only</i> </b> the <code>identityToken</code> or <code>accessToken</code> passed to the operation.</p> </li> <li> <p>For action entities, you can include only their <code>Identifier</code> and <code>EntityType</code>. </p> </li> </ul> </important>
            requests: <p>An array of up to 30 requests that you want Verified Permissions to evaluate.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Batch - Example 1
            The following example requests three authorization decisions for two resources                     and two actions in different photo albums.

            >>> await client.batch_is_authorized_with_token(identity_token='eyJra12345EXAMPLE', requests=[{'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'ViewPhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}}, {'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'SharePhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}}, {'action': {'actionType': 'PhotoFlash::Action', 'actionId': 'ViewPhoto'}, 'resource': {'entityType': 'PhotoFlash::Photo', 'entityId': 'OfficePhoto94.jpg'}}], entities={'entityList': [{'identifier': {'entityType': 'PhotoFlash::Photo', 'entityId': 'VacationPhoto94.jpg'}, 'parents': [{'entityType': 'PhotoFlash::Album', 'entityId': 'MyExampleAlbum1'}]}, {'identifier': {'entityType': 'PhotoFlash::Photo', 'entityId': 'OfficePhoto94.jpg'}, 'parents': [{'entityType': 'PhotoFlash::Album', 'entityId': 'MyExampleAlbum2'}]}]}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.batch_is_authorized_with_token_input.BatchIsAuthorizedWithTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.batch_is_authorized_with_token_output.BatchIsAuthorizedWithTokenOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.batch_is_authorized_with_token

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.batch_is_authorized_with_token.async_batch_is_authorized_with_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.batch_is_authorized_with_token_input.BatchIsAuthorizedWithTokenInput = {
            "policy_store_id": policy_store_id,
            "requests": requests,
        }
        if identity_token is not None:
            input_["identity_token"] = identity_token
        if access_token is not None:
            input_["access_token"] = access_token
        if entities is not None:
            input_["entities"] = entities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_schema(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.get_schema_output.GetSchemaOutput":
        r"""<p>Retrieve the details for the specified schema in the specified policy store.</p>

                Args:
                    policy_store_id: <p>Specifies the ID of the policy store that contains the schema.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>

                Raises:
                    capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
                    capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
                    capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
                    capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
                    capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
                    capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    GetSchema
                    The following example retrieves the current schema stored in the specified policy store.

        Note
        The JSON in the parameters of this operation are strings that can contain embedded quotation marks (") within the outermost quotation mark pair. This requires that you stringify the JSON object by preceding all embedded quotation marks with a backslash character ( \" ) and combining all lines into a single text line with no line breaks.

        Example strings might be displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

                    >>> await client.get_schema(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.get_schema_input.GetSchemaInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.get_schema_output.GetSchemaOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.get_schema

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.get_schema.async_get_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.get_schema_input.GetSchemaInput = {
            "policy_store_id": policy_store_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def is_authorized(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        principal: Optional[
            "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
        ] = None,
        action: Optional[
            "capo_verifiedpermissions.types.action_identifier.ActionIdentifier"
        ] = None,
        resource: Optional[
            "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
        ] = None,
        context: Optional[
            "capo_verifiedpermissions.types.context_definition.ContextDefinition"
        ] = None,
        entities: Optional[
            "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
        ] = None,
    ) -> "capo_verifiedpermissions.types.is_authorized_output.IsAuthorizedOutput":
        """<p>Makes an authorization decision about a service request described in the parameters. The information in the parameters can also define additional context that Verified Permissions can include in the evaluation. The request is evaluated against all matching policies in the specified policy store. The result of the decision is either <code>Allow</code> or <code>Deny</code>, along with a list of the policies that resulted in the decision.</p>

                Args:
                    policy_store_id: <p>Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
                    principal: <p>Specifies the principal for which the authorization decision is to be made.</p>
                    action: <p>Specifies the requested action to be authorized. For example, is the principal authorized to perform this action on the resource?</p>
                    resource: <p>Specifies the resource for which the authorization decision is to be made.</p>
                    context: <p>Specifies additional context that can be used to make more granular authorization decisions.</p>
                    entities: <p>(Optional) Specifies the list of resources and principals and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <note> <p>You can include only principal and resource entities in this parameter; you can't include actions. You must specify actions in the schema.</p> </note>

                Raises:
                    capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
                    capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
                    capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
                    capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
                    capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
                    capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    IsAuthorized - Example 1
                    The following example requests an authorization decision for a principal of type User named Alice, who wants to perform the updatePhoto operation, on a resource of type Photo named VacationPhoto94.jpg.

        The response shows that the request was allowed by one policy.

                    >>> await client.is_authorized(principal={'entityType': 'User', 'entityId': 'alice'}, action={'actionType': 'Action', 'actionId': 'updatePhoto'}, resource={'entityType': 'Photo', 'entityId': 'VacationPhoto94.jpg'}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
                    IsAuthorized - Example 2
                    The following example is the same as the previous example, except that the principal is User::"bob", and the policy store doesn't contain any policy that allows that user access to Album::"alice_folder". The output infers that the Deny was implicit because the list of DeterminingPolicies is empty.

                    >>> await client.is_authorized(principal={'entityType': 'User', 'entityId': 'bob'}, action={'actionType': 'Action', 'actionId': 'view'}, resource={'entityType': 'Photo', 'entityId': 'VacationPhoto94.jpg'}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.is_authorized_input.IsAuthorizedInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.is_authorized_output.IsAuthorizedOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.is_authorized

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.is_authorized.async_is_authorized(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.is_authorized_input.IsAuthorizedInput = {
            "policy_store_id": policy_store_id
        }
        if principal is not None:
            input_["principal"] = principal
        if action is not None:
            input_["action"] = action
        if resource is not None:
            input_["resource"] = resource
        if context is not None:
            input_["context"] = context
        if entities is not None:
            input_["entities"] = entities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def is_authorized_with_token(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        identity_token: Optional["capo_verifiedpermissions.types.token.Token"] = None,
        access_token: Optional["capo_verifiedpermissions.types.token.Token"] = None,
        action: Optional[
            "capo_verifiedpermissions.types.action_identifier.ActionIdentifier"
        ] = None,
        resource: Optional[
            "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
        ] = None,
        context: Optional[
            "capo_verifiedpermissions.types.context_definition.ContextDefinition"
        ] = None,
        entities: Optional[
            "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
        ] = None,
    ) -> "capo_verifiedpermissions.types.is_authorized_with_token_output.IsAuthorizedWithTokenOutput":
        """<p>Makes an authorization decision about a service request described in the parameters. The principal in this request comes from an external identity source in the form of an identity token formatted as a <a href="https://wikipedia.org/wiki/JSON_Web_Token">JSON web token (JWT)</a>. The information in the parameters can also define additional context that Verified Permissions can include in the evaluation. The request is evaluated against all matching policies in the specified policy store. The result of the decision is either <code>Allow</code> or <code>Deny</code>, along with a list of the policies that resulted in the decision.</p> <p>Verified Permissions validates each token that is specified in a request by checking its expiration date and its signature.</p> <important> <p>Tokens from an identity source user continue to be usable until they expire. Token revocation and resource deletion have no effect on the validity of a token in your policy store</p> </important>

                Args:
                    policy_store_id: <p>Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
                    identity_token: <p>Specifies an identity token for the principal to be authorized. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an ID token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>id</code>.</p>
                    access_token: <p>Specifies an access token for the principal to be authorized. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an access token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>access</code>.</p>
                    action: <p>Specifies the requested action to be authorized. Is the specified principal authorized to perform this action on the specified resource.</p>
                    resource: <p>Specifies the resource for which the authorization decision is made. For example, is the principal allowed to perform the action on the resource?</p>
                    context: <p>Specifies additional context that can be used to make more granular authorization decisions.</p>
                    entities: <p>(Optional) Specifies the list of resources and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <important> <p>You can't include principals in this parameter, only resource and action entities. This parameter can't include any entities of a type that matches the user or group entity types that you defined in your identity source.</p> <ul> <li> <p>The <code>IsAuthorizedWithToken</code> operation takes principal attributes from <b> <i>only</i> </b> the <code>identityToken</code> or <code>accessToken</code> passed to the operation.</p> </li> <li> <p>For action entities, you can include only their <code>Identifier</code> and <code>EntityType</code>. </p> </li> </ul> </important>

                Raises:
                    capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
                    capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
                    capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
                    capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
                    capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
                    capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    IsAuthorizedWithToken - Example 1
                    The following example requests an authorization decision for a user who was authenticated by Amazon Cognito. The request uses the identity token provided by Amazon Cognito instead of the access token. In this example, the specified information store is configured to return principals as entities of type CognitoUser. The policy store contains a policy with the following statement.

        permit(
            principal == CognitoUser::"us-east-1_1a2b3c4d5|a1b2c3d4e5f6g7h8i9j0kalbmc",
            action,
            resource == Photo::"VacationPhoto94.jpg"
        );

                    >>> await client.is_authorized_with_token(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', action={'actionId': 'View', 'actionType': 'Action'}, resource={'entityId': 'vacationPhoto94.jpg', 'entityType': 'Photo'}, identity_token='EgZjxMPlbWUyBggAEEUYOdIBCDM3NDlqMGo3qAIAsAIA')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.is_authorized_with_token_input.IsAuthorizedWithTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.is_authorized_with_token_output.IsAuthorizedWithTokenOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.is_authorized_with_token

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.is_authorized_with_token.async_is_authorized_with_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.is_authorized_with_token_input.IsAuthorizedWithTokenInput = {
            "policy_store_id": policy_store_id
        }
        if identity_token is not None:
            input_["identity_token"] = identity_token
        if access_token is not None:
            input_["access_token"] = access_token
        if action is not None:
            input_["action"] = action
        if resource is not None:
            input_["resource"] = resource
        if context is not None:
            input_["context"] = context
        if entities is not None:
            input_["entities"] = entities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_schema(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        definition: "capo_verifiedpermissions.types.schema_definition.SchemaDefinition",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.put_schema_output.PutSchemaOutput":
        r"""<p>Creates or updates the policy schema in the specified policy store. The schema is used to validate any Cedar policies and policy templates submitted to the policy store. Any changes to the schema validate only policies and templates submitted after the schema change. Existing policies and templates are not re-evaluated against the changed schema. If you later update a policy, then it is evaluated against the new schema at that time.</p> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

                Args:
                    policy_store_id: <p>Specifies the ID of the policy store in which to place the schema.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
                    definition: <p>Specifies the definition of the schema to be stored. The schema definition must be written in Cedar schema JSON.</p>

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
                    PutSchema
                    The following example creates a new schema, or updates an existing schema, in the specified policy store. Note that the schema text is shown line wrapped for readability. You should submit the entire schema text as a single line of text.

        Note
        The JSON in the parameters of this operation are strings that can contain embedded quotation marks (") within the outermost quotation mark pair. This requires that you stringify the JSON object by preceding all embedded quotation marks with a backslash character ( \" ) and combining all lines into a single text line with no line breaks.

        Example strings might be displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

                    >>> await client.put_schema(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', definition={'cedarJson': '{"MySampleNamespace": {"actions": {"remoteAccess": {"appliesTo": {"principalTypes": ["Employee"]}}},"entityTypes": {"Employee": {"shape": {"attributes": {"jobLevel": {"type": "Long"},"name": {"type": "String"}},"type": "Record"}}}}}'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.put_schema_input.PutSchemaInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.put_schema_output.PutSchemaOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.put_schema

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.put_schema.async_put_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.put_schema_input.PutSchemaInput = {
            "policy_store_id": policy_store_id,
            "definition": definition,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_policy(
        self,
        requests: "capo_verifiedpermissions.types.batch_get_policy_input_list.BatchGetPolicyInputList",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.batch_get_policy_output.BatchGetPolicyOutput":
        """<p>Retrieves information about a group (batch) of policies.</p> <note> <p>The <code>BatchGetPolicy</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>verifiedpermissions:GetPolicy</code> in their IAM policies.</p> </note>

        Args:
            requests: <p>An array of up to 100 policies you want information about.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve details about a policy
            The following example retrieves information about the specified policy contained in the specified policy store. In this example, the requested policy is a template-linked policy, so it returns the ID of the policy template, and the specific principal and resource used by this policy.

            >>> await client.batch_get_policy(requests=[{'policyId': 'PWv5M6d5HePx3gVVLKY1nK', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}, {'policyId': 'LzFn6KgLWvv4Mbegus35jn', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}, {'policyId': '77gLjer8H5o3mvrnMGrSL5', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}])
            To retrieve policies by name
            The following example retrieves information about policies using their names instead of their IDs.

            >>> await client.batch_get_policy(requests=[{'policyId': 'name/example-policy', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}, {'policyId': 'name/example-policy-2', 'policyStoreId': 'ERZeDpRc34dkYZeb6FZRVC'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_verifiedpermissions.types.batch_get_policy_input.BatchGetPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_verifiedpermissions.types.batch_get_policy_output.BatchGetPolicyOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.batch_get_policy

            (
                output,
                http_response,
            ) = await capo_verifiedpermissions._operations.verified_permissions.batch_get_policy.async_batch_get_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.batch_get_policy_input.BatchGetPolicyInput = {
            "requests": requests
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
