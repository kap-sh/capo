"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#VerifiedPermissions``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_verifiedpermissions._auth._signers
import capo_verifiedpermissions._auth._sigv4
from capo_verifiedpermissions._auth._identity import Credentials
from capo_verifiedpermissions._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_verifiedpermissions._auth._zapros_handler import AuthMiddleware
from capo_verifiedpermissions._pagination import resolve_path as _resolve_path
from capo_verifiedpermissions._resources.verified_permissions.policy_store import (
    PolicyStore,
)
from capo_verifiedpermissions._resources.verified_permissions.policy_store_alias import (
    PolicyStoreAlias,
)
from capo_verifiedpermissions._services._aws_config import aws_config
from capo_verifiedpermissions._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.action_identifier
    import capo_verifiedpermissions.types.alias
    import capo_verifiedpermissions.types.amazon_resource_name
    import capo_verifiedpermissions.types.batch_get_policy_input
    import capo_verifiedpermissions.types.batch_get_policy_input_list
    import capo_verifiedpermissions.types.batch_get_policy_output
    import capo_verifiedpermissions.types.batch_is_authorized_input
    import capo_verifiedpermissions.types.batch_is_authorized_input_list
    import capo_verifiedpermissions.types.batch_is_authorized_output
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_input
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_input_list
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_output
    import capo_verifiedpermissions.types.configuration
    import capo_verifiedpermissions.types.context_definition
    import capo_verifiedpermissions.types.create_identity_source_input
    import capo_verifiedpermissions.types.create_identity_source_output
    import capo_verifiedpermissions.types.create_policy_input
    import capo_verifiedpermissions.types.create_policy_output
    import capo_verifiedpermissions.types.create_policy_store_alias_input
    import capo_verifiedpermissions.types.create_policy_store_alias_output
    import capo_verifiedpermissions.types.create_policy_store_input
    import capo_verifiedpermissions.types.create_policy_store_output
    import capo_verifiedpermissions.types.create_policy_template_input
    import capo_verifiedpermissions.types.create_policy_template_output
    import capo_verifiedpermissions.types.delete_identity_source_input
    import capo_verifiedpermissions.types.delete_identity_source_output
    import capo_verifiedpermissions.types.delete_policy_input
    import capo_verifiedpermissions.types.delete_policy_output
    import capo_verifiedpermissions.types.delete_policy_store_alias_input
    import capo_verifiedpermissions.types.delete_policy_store_alias_output
    import capo_verifiedpermissions.types.delete_policy_store_input
    import capo_verifiedpermissions.types.delete_policy_store_output
    import capo_verifiedpermissions.types.delete_policy_template_input
    import capo_verifiedpermissions.types.delete_policy_template_output
    import capo_verifiedpermissions.types.deletion_mode
    import capo_verifiedpermissions.types.deletion_protection
    import capo_verifiedpermissions.types.encryption_settings
    import capo_verifiedpermissions.types.entities_definition
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.get_identity_source_input
    import capo_verifiedpermissions.types.get_identity_source_output
    import capo_verifiedpermissions.types.get_policy_input
    import capo_verifiedpermissions.types.get_policy_output
    import capo_verifiedpermissions.types.get_policy_store_alias_input
    import capo_verifiedpermissions.types.get_policy_store_alias_output
    import capo_verifiedpermissions.types.get_policy_store_input
    import capo_verifiedpermissions.types.get_policy_store_output
    import capo_verifiedpermissions.types.get_policy_template_input
    import capo_verifiedpermissions.types.get_policy_template_output
    import capo_verifiedpermissions.types.get_schema_input
    import capo_verifiedpermissions.types.get_schema_output
    import capo_verifiedpermissions.types.idempotency_token
    import capo_verifiedpermissions.types.identity_source_filters
    import capo_verifiedpermissions.types.identity_source_id
    import capo_verifiedpermissions.types.identity_source_item
    import capo_verifiedpermissions.types.is_authorized_input
    import capo_verifiedpermissions.types.is_authorized_output
    import capo_verifiedpermissions.types.is_authorized_with_token_input
    import capo_verifiedpermissions.types.is_authorized_with_token_output
    import capo_verifiedpermissions.types.list_identity_sources_input
    import capo_verifiedpermissions.types.list_identity_sources_max_results
    import capo_verifiedpermissions.types.list_identity_sources_output
    import capo_verifiedpermissions.types.list_policies_input
    import capo_verifiedpermissions.types.list_policies_output
    import capo_verifiedpermissions.types.list_policy_store_aliases_input
    import capo_verifiedpermissions.types.list_policy_store_aliases_output
    import capo_verifiedpermissions.types.list_policy_stores_input
    import capo_verifiedpermissions.types.list_policy_stores_output
    import capo_verifiedpermissions.types.list_policy_templates_input
    import capo_verifiedpermissions.types.list_policy_templates_output
    import capo_verifiedpermissions.types.list_tags_for_resource_input
    import capo_verifiedpermissions.types.list_tags_for_resource_output
    import capo_verifiedpermissions.types.max_results
    import capo_verifiedpermissions.types.next_token
    import capo_verifiedpermissions.types.policy_definition
    import capo_verifiedpermissions.types.policy_filter
    import capo_verifiedpermissions.types.policy_id
    import capo_verifiedpermissions.types.policy_item
    import capo_verifiedpermissions.types.policy_name
    import capo_verifiedpermissions.types.policy_statement
    import capo_verifiedpermissions.types.policy_store_alias_filter
    import capo_verifiedpermissions.types.policy_store_alias_item
    import capo_verifiedpermissions.types.policy_store_description
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_store_item
    import capo_verifiedpermissions.types.policy_template_description
    import capo_verifiedpermissions.types.policy_template_id
    import capo_verifiedpermissions.types.policy_template_item
    import capo_verifiedpermissions.types.policy_template_name
    import capo_verifiedpermissions.types.principal_entity_type
    import capo_verifiedpermissions.types.put_schema_input
    import capo_verifiedpermissions.types.put_schema_output
    import capo_verifiedpermissions.types.schema_definition
    import capo_verifiedpermissions.types.tag_key_list
    import capo_verifiedpermissions.types.tag_map
    import capo_verifiedpermissions.types.tag_resource_input
    import capo_verifiedpermissions.types.tag_resource_output
    import capo_verifiedpermissions.types.token
    import capo_verifiedpermissions.types.untag_resource_input
    import capo_verifiedpermissions.types.untag_resource_output
    import capo_verifiedpermissions.types.update_configuration
    import capo_verifiedpermissions.types.update_identity_source_input
    import capo_verifiedpermissions.types.update_identity_source_output
    import capo_verifiedpermissions.types.update_policy_definition
    import capo_verifiedpermissions.types.update_policy_input
    import capo_verifiedpermissions.types.update_policy_output
    import capo_verifiedpermissions.types.update_policy_store_input
    import capo_verifiedpermissions.types.update_policy_store_output
    import capo_verifiedpermissions.types.update_policy_template_input
    import capo_verifiedpermissions.types.update_policy_template_output
    import capo_verifiedpermissions.types.validation_settings


class VerifiedPermissionsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class VerifiedPermissionsClient:
    """A client for the ``VerifiedPermissions`` service.

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
        self._config = VerifiedPermissionsClientConfig(
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
        self.policy_store = PolicyStore(self)
        self.policy_store_alias = PolicyStoreAlias(self)

    def operation_options(
        self, config_overrides: Optional[VerifiedPermissionsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: VerifiedPermissionsClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_verifiedpermissions.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns the tags associated with the specified Amazon Verified Permissions resource. In Verified Permissions, policy stores can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to view tags.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListTagsForResource
            The following example lists all the tags for the resource named in the API call.

            >>> client.list_tags_for_resource(resource_arn='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.list_tags_for_resource

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_verifiedpermissions.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_verifiedpermissions.types.tag_map.TagMap",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.tag_resource_output.TagResourceOutput":
        """<p>Assigns one or more tags (key-value pairs) to the specified Amazon Verified Permissions resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In Verified Permissions, policy stores can be tagged.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the TagResource action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you're adding tags to.</p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.too_many_tags_exception.TooManyTagsException: <p>No more tags be added because the limit (50) has been reached. To add new tags, use <code>UntagResource</code> to remove existing tags.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            TagResource
            The following example tags the resource.

            >>> client.tag_resource(resource_arn='C7v5xMplfFH3i3e4Jrzb1a', tags={'key1': 'value1', 'key2': 'value2'})
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.tag_resource

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_verifiedpermissions.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_verifiedpermissions.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from the specified Amazon Verified Permissions resource. In Verified Permissions, policy stores can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the resource from which you are removing tags.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UntagResource
            The following example removes the listed tags from the resource.

            >>> client.untag_resource(resource_arn='C7v5xMplfFH3i3e4Jrzb1a', tag_keys=['key1', 'key2'])
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.untag_resource

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_policy_store(
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

            >>> client.create_policy_store(validation_settings={'mode': 'STRICT'}, client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111')
            To create an encrypted policy store
            The following example creates a new policy store with encryption settings based on a provided KMS key.

            >>> client.create_policy_store(validation_settings={'mode': 'STRICT'}, encryption_settings={'kmsEncryptionSettings': {'key': 'arn:aws:kms:us-east-1:123456789012:key/abcdefgh-ijkl-mnop-qrst-uvwxyz123456', 'encryptionContext': {'policy_store_owner': 'Tim'}}}, client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111')
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def get_policy_store(
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

            >>> client.get_policy_store(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
            GetPolicyStore that is encrypted
            The following example retrieves details about the specified encrypted policy store.

            >>> client.get_policy_store(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def update_policy_store(
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

            >>> client.update_policy_store(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', validation_settings={'mode': 'OFF'})
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_policy_store(
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

            >>> client.delete_policy_store(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_policy_stores(
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

            >>> client.list_policy_stores()
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_policy_stores(
        self,
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_verifiedpermissions.types.policy_store_item.PolicyStoreItem]":
        _token = next_token
        while True:
            _response = self.list_policy_stores(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_stores",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def create_identity_source(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        configuration: "capo_verifiedpermissions.types.configuration.Configuration",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        client_token: Optional[
            "capo_verifiedpermissions.types.idempotency_token.IdempotencyToken"
        ] = None,
        principal_entity_type: Optional[
            "capo_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
        ] = None,
    ) -> "capo_verifiedpermissions.types.create_identity_source_output.CreateIdentitySourceOutput":
        """<p>Adds an identity source to a policy store–an Amazon Cognito user pool or OpenID Connect (OIDC) identity provider (IdP). </p> <p>After you create an identity source, you can use the identities provided by the IdP as proxies for the principal in authorization queries that use the <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html">IsAuthorizedWithToken</a> or <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithToken.html">BatchIsAuthorizedWithToken</a> API operations. These identities take the form of tokens that contain claims about the user, such as IDs, attributes and group memberships. Identity sources provide identity (ID) tokens and access tokens. Verified Permissions derives information about your user and session from token claims. Access tokens provide action <code>context</code> to your policies, and ID tokens provide principal <code>Attributes</code>.</p> <important> <p>Tokens from an identity source user continue to be usable until they expire. Token revocation and resource deletion have no effect on the validity of a token in your policy store</p> </important> <note> <p>To reference a user from this identity source in your Cedar policies, refer to the following syntax examples.</p> <ul> <li> <p>Amazon Cognito user pool: <code>Namespace::[Entity type]::[User pool ID]|[user principal attribute]</code>, for example <code>MyCorp::User::us-east-1_EXAMPLE|a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p> </li> <li> <p>OpenID Connect (OIDC) provider: <code>Namespace::[Entity type]::[entityIdPrefix]|[user principal attribute]</code>, for example <code>MyCorp::User::MyOIDCProvider|a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p> </li> </ul> </note> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            client_token: <p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>ConflictException</code> error.</p> <p>Verified Permissions recognizes a <code>ClientToken</code> for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of <code>ClientToken</code>.</p>
            policy_store_id: <p>Specifies the ID of the policy store in which you want to store this identity source. Only policies and requests made using this policy store can reference identities from the identity provider configured in the new identity source.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            configuration: <p>Specifies the details required to communicate with the identity provider (IdP) associated with this identity source.</p>
            principal_entity_type: <p>Specifies the namespace and data type of the principals generated for identities authenticated by the new identity source.</p>

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
            To create an identity source
            The following ``create-identity-source`` example creates an identity source that lets you reference identities stored in the specified Amazon Cognito user pool. Those identities are available in Verified Permissions as entities of type ``User``.

            >>> client.create_identity_source(configuration={'cognitoUserPoolConfiguration': {'userPoolArn': 'arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5', 'clientIds': ['a1b2c3d4e5f6g7h8i9j0kalbmc']}}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', principal_entity_type='User', client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.create_identity_source_input.CreateIdentitySourceInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.create_identity_source_output.CreateIdentitySourceOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.create_identity_source

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.create_identity_source.create_identity_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.create_identity_source_input.CreateIdentitySourceInput = {
            "policy_store_id": policy_store_id,
            "configuration": configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if principal_entity_type is not None:
            input_["principal_entity_type"] = principal_entity_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_identity_source(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        identity_source_id: "capo_verifiedpermissions.types.identity_source_id.IdentitySourceId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.get_identity_source_output.GetIdentitySourceOutput":
        """<p>Retrieves the details about the specified identity source.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the identity source you want information about.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            identity_source_id: <p>Specifies the ID of the identity source you want information about.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve details about an identity source
            The following example retrieves the details for the specified identity source.

            >>> client.get_identity_source(identity_source_id='ISEXAMPLEabcdefg111111', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.get_identity_source_input.GetIdentitySourceInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.get_identity_source_output.GetIdentitySourceOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.get_identity_source

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.get_identity_source.get_identity_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.get_identity_source_input.GetIdentitySourceInput = {
            "policy_store_id": policy_store_id,
            "identity_source_id": identity_source_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_identity_source(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        identity_source_id: "capo_verifiedpermissions.types.identity_source_id.IdentitySourceId",
        update_configuration: "capo_verifiedpermissions.types.update_configuration.UpdateConfiguration",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        principal_entity_type: Optional[
            "capo_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
        ] = None,
    ) -> "capo_verifiedpermissions.types.update_identity_source_output.UpdateIdentitySourceOutput":
        """<p>Updates the specified identity source to use a new identity provider (IdP), or to change the mapping of identities from the IdP to a different principal entity type.</p> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the identity source that you want to update.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            identity_source_id: <p>Specifies the ID of the identity source that you want to update.</p>
            update_configuration: <p>Specifies the details required to communicate with the identity provider (IdP) associated with this identity source.</p>
            principal_entity_type: <p>Specifies the data type of principals generated for identities authenticated by the identity source.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateIdentitySource
            The following example updates the configuration of the specified identity source with a new configuration.

            >>> client.update_identity_source(identity_source_id='ISEXAMPLEabcdefg111111', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', update_configuration={'cognitoUserPoolConfiguration': {'userPoolArn': 'arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5', 'clientIds': ['a1b2c3d4e5f6g7h8i9j0kalbmc']}})
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.update_identity_source_input.UpdateIdentitySourceInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.update_identity_source_output.UpdateIdentitySourceOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.update_identity_source

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.update_identity_source.update_identity_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.update_identity_source_input.UpdateIdentitySourceInput = {
            "policy_store_id": policy_store_id,
            "identity_source_id": identity_source_id,
            "update_configuration": update_configuration,
        }
        if principal_entity_type is not None:
            input_["principal_entity_type"] = principal_entity_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_identity_source(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        identity_source_id: "capo_verifiedpermissions.types.identity_source_id.IdentitySourceId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.delete_identity_source_output.DeleteIdentitySourceOutput":
        """<p>Deletes an identity source that references an identity provider (IdP) such as Amazon Cognito. After you delete the identity source, you can no longer use tokens for identities from that identity source to represent principals in authorization queries made using <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html">IsAuthorizedWithToken</a>. operations.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the identity source that you want to delete.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            identity_source_id: <p>Specifies the ID of the identity source that you want to delete.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an identity source
            The following example request deletes the specified identity source.

            >>> client.delete_identity_source(identity_source_id='ISEXAMPLEabcdefg111111', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.delete_identity_source_input.DeleteIdentitySourceInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.delete_identity_source_output.DeleteIdentitySourceOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.delete_identity_source

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.delete_identity_source.delete_identity_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.delete_identity_source_input.DeleteIdentitySourceInput = {
            "policy_store_id": policy_store_id,
            "identity_source_id": identity_source_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_identity_sources(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.list_identity_sources_max_results.ListIdentitySourcesMaxResults"
        ] = None,
        filters: Optional[
            "capo_verifiedpermissions.types.identity_source_filters.IdentitySourceFilters"
        ] = None,
    ) -> "capo_verifiedpermissions.types.list_identity_sources_output.ListIdentitySourcesOutput":
        """<p>Returns a paginated list of all of the identity sources defined in the specified policy store.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the identity sources that you want to list.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 10 identity sources per response. You can specify a maximum of 50 identity sources per response.</p>
            filters: <p>Specifies characteristics of an identity source that you can use to limit the output to matching identity sources.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListIdentitySources
            The following example request creates lists the identity sources currently defined in the specified policy store.

            >>> client.list_identity_sources(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.list_identity_sources_input.ListIdentitySourcesInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.list_identity_sources_output.ListIdentitySourcesOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.list_identity_sources

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.list_identity_sources.list_identity_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.list_identity_sources_input.ListIdentitySourcesInput = {
            "policy_store_id": policy_store_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_identity_sources(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.list_identity_sources_max_results.ListIdentitySourcesMaxResults"
        ] = None,
        filters: Optional[
            "capo_verifiedpermissions.types.identity_source_filters.IdentitySourceFilters"
        ] = None,
    ) -> "Iterator[capo_verifiedpermissions.types.identity_source_item.IdentitySourceItem]":
        _token = next_token
        while True:
            _response = self.list_identity_sources(
                policy_store_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("identity_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_policy(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        definition: "capo_verifiedpermissions.types.policy_definition.PolicyDefinition",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        client_token: Optional[
            "capo_verifiedpermissions.types.idempotency_token.IdempotencyToken"
        ] = None,
        name: Optional["capo_verifiedpermissions.types.policy_name.PolicyName"] = None,
    ) -> "capo_verifiedpermissions.types.create_policy_output.CreatePolicyOutput":
        """<p>Creates a Cedar policy and saves it in the specified policy store. You can create either a static policy or a policy linked to a policy template.</p> <ul> <li> <p>To create a static policy, provide the Cedar policy text in the <code>StaticPolicy</code> section of the <code>PolicyDefinition</code>.</p> </li> <li> <p>To create a policy that is dynamically linked to a policy template, specify the policy template ID and the principal and resource to associate with this policy in the <code>templateLinked</code> section of the <code>PolicyDefinition</code>. If the policy template is ever updated, any policies linked to the policy template automatically use the updated template.</p> </li> </ul> <note> <p>Creating a policy causes it to be validated against the schema in the policy store. If the policy doesn't pass validation, the operation fails and the policy isn't stored.</p> </note> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            client_token: <p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>ConflictException</code> error.</p> <p>Verified Permissions recognizes a <code>ClientToken</code> for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of <code>ClientToken</code>.</p>
            policy_store_id: <p>Specifies the <code>PolicyStoreId</code> of the policy store you want to store the policy in.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            definition: <p>A structure that specifies the policy type and content to use for the new policy. You must include either a static or a templateLinked element. The policy content must be written in the Cedar policy language.</p>
            name: <p>Specifies a name for the policy that is unique among all policies within the policy store. You can use the name in place of the policy ID in API operations that reference the policy. The name must be prefixed with <code>name/</code>.</p> <p>If you specify a name that is already associated with another policy in the policy store, you receive a <code>ConflictException</code> error.</p>

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
            To create a static policy
            The following example request creates a static policy with a policy scope that specifies both a principal and a resource. The response includes both the Principal and Resource elements because both were specified in the request policy scope.

            >>> client.create_policy(definition={'static': {'description': 'Grant members of janeFriends UserGroup access to the vacationFolder Album', 'statement': 'permit( principal in UserGroup::"janeFriends", action, resource in Album::"vacationFolder" );'}}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111', name='name/example-policy')
            To create a template-linked policy
            The following example creates a template-linked policy using the specified policy template and associates the specified principal to use with the new template-linked policy.

            >>> client.create_policy(definition={'templateLinked': {'policyTemplateId': 'PTEXAMPLEabcdefg111111', 'principal': {'entityType': 'User', 'entityId': 'alice'}}}, policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111', name='name/example-template-linked-policy')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.create_policy_input.CreatePolicyInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.create_policy_output.CreatePolicyOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.create_policy

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.create_policy.create_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.create_policy_input.CreatePolicyInput = {
            "policy_store_id": policy_store_id,
            "definition": definition,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policy(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.get_policy_output.GetPolicyOutput":
        """<p>Retrieves information about the specified policy.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the policy that you want information about.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            policy_id: <p>Specifies the ID of the policy you want information about.</p> <p>You can use the policy name in place of the policy ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>SPEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy</code> </p> </li> </ul>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve details about a policy
            The following example retrieves information about the specified policy contained in the specified policy store. In this example, the requested policy is a template-linked policy, so it returns the ID of the policy template, and the specific principal and resource used by this policy.

            >>> client.get_policy(policy_id='9wYixMplbbZQb5fcZHyJhY', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
            To retrieve a policy by name
            The following example retrieves information about a policy using its name instead of its ID.

            >>> client.get_policy(policy_id='name/example-policy', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.get_policy_input.GetPolicyInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.get_policy_output.GetPolicyOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.get_policy

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.get_policy_input.GetPolicyInput = {
            "policy_store_id": policy_store_id,
            "policy_id": policy_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_policy(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        definition: Optional[
            "capo_verifiedpermissions.types.update_policy_definition.UpdatePolicyDefinition"
        ] = None,
        name: Optional["capo_verifiedpermissions.types.policy_name.PolicyName"] = None,
    ) -> "capo_verifiedpermissions.types.update_policy_output.UpdatePolicyOutput":
        """<p>Modifies a Cedar static policy in the specified policy store. You can change only certain elements of the <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyInput.html#amazonverifiedpermissions-UpdatePolicy-request-UpdatePolicyDefinition">UpdatePolicyDefinition</a> parameter. You can directly update only static policies. To change a template-linked policy, you must update the template instead, using <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html">UpdatePolicyTemplate</a>.</p> <note> <ul> <li> <p>If policy validation is enabled in the policy store, then updating a static policy causes Verified Permissions to validate the policy against the schema in the policy store. If the updated static policy doesn't pass validation, the operation fails and the update isn't stored.</p> </li> <li> <p>When you edit a static policy, you can change only certain elements of a static policy:</p> <ul> <li> <p>The action referenced by the policy. </p> </li> <li> <p>A condition clause, such as when and unless. </p> </li> </ul> <p>You can't change these elements of a static policy: </p> <ul> <li> <p>Changing a policy from a static policy to a template-linked policy. </p> </li> <li> <p>Changing the effect of a static policy from permit or forbid. </p> </li> <li> <p>The principal referenced by a static policy. </p> </li> <li> <p>The resource referenced by a static policy. </p> </li> </ul> </li> <li> <p>To update a template-linked policy, you must update the template instead. </p> </li> </ul> </note> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the policy that you want to update.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            policy_id: <p>Specifies the ID of the policy that you want to update. To find this value, you can use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html">ListPolicies</a>.</p> <p>You can use the policy name in place of the policy ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>SPEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy</code> </p> </li> </ul>
            definition: <p>Specifies the updated policy content that you want to replace on the specified policy. The content must be valid Cedar policy language text.</p> <p>If you don't specify this parameter, the existing policy definition remains unchanged.</p> <p>You can change only the following elements from the policy definition:</p> <ul> <li> <p>The <code>action</code> referenced by the policy.</p> </li> <li> <p>Any conditional clauses, such as <code>when</code> or <code>unless</code> clauses.</p> </li> </ul> <p>You <b>can't</b> change the following elements:</p> <ul> <li> <p>Changing from <code>static</code> to <code>templateLinked</code>.</p> </li> <li> <p>Changing the effect of the policy from <code>permit</code> or <code>forbid</code>.</p> </li> <li> <p>The <code>principal</code> referenced by the policy.</p> </li> <li> <p>The <code>resource</code> referenced by the policy.</p> </li> </ul>
            name: <p>Specifies a name for the policy that is unique among all policies within the policy store. You can use the name in place of the policy ID in API operations that reference the policy. The name must be prefixed with <code>name/</code>.</p> <note> <p>If you don't include the name in an update request, the existing name is unchanged. To remove a name, set it to an empty string (<code>""</code>).</p> </note> <p>If you specify a name that is already associated with another policy in the policy store, you receive a <code>ConflictException</code> error.</p>

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
            UpdatePolicy
            The following example replaces the definition of the specified static policy with a new one.

            >>> client.update_policy(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', policy_id='9wYxMpljbbZQb5fcZHyJhY', definition={'static': {'statement': 'permit(principal, action, resource in Album::"public_folder");'}}, name='name/example-policy-2')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.update_policy_input.UpdatePolicyInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.update_policy_output.UpdatePolicyOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.update_policy

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.update_policy.update_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.update_policy_input.UpdatePolicyInput = {
            "policy_store_id": policy_store_id,
            "policy_id": policy_id,
        }
        if definition is not None:
            input_["definition"] = definition
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_policy(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.delete_policy_output.DeletePolicyOutput":
        """<p>Deletes the specified policy from the policy store.</p> <p>This operation is idempotent; if you specify a policy that doesn't exist, the request response returns a successful <code>HTTP 200</code> status code.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the policy that you want to delete.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            policy_id: <p>Specifies the ID of the policy that you want to delete.</p> <p>You can use the policy name in place of the policy ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>SPEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy</code> </p> </li> </ul>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a policy
            The following example deletes the specified policy from its policy store.

            >>> client.delete_policy(policy_id='9wYxMpljbbZQb5fcZHyJhY', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.delete_policy_input.DeletePolicyInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.delete_policy_output.DeletePolicyOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.delete_policy

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.delete_policy.delete_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.delete_policy_input.DeletePolicyInput = {
            "policy_store_id": policy_store_id,
            "policy_id": policy_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policies(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "capo_verifiedpermissions.types.policy_filter.PolicyFilter"
        ] = None,
    ) -> "capo_verifiedpermissions.types.list_policies_output.ListPoliciesOutput":
        """<p>Returns a paginated list of all policies stored in the specified policy store.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store you want to list policies from.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 10 policies per response. You can specify a maximum of 50 policies per response.</p>
            filter: <p>Specifies a filter that limits the response to only policies that match the specified criteria. For example, you list only the policies that reference a specified principal.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListPolicies - Example 1
            The following example lists all policies in the policy store.

            >>> client.list_policies(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
            ListPolicies - Example 2
            The following example lists all policies for a specified principal.

            >>> client.list_policies(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', filter={'principal': {'identifier': {'entityType': 'User', 'entityId': 'alice'}}})
            ListPolicies - Example 3
            The following example uses the Filter parameter to list only the template-linked policies in the specified policy store.

            >>> client.list_policies(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', filter={'policyType': 'TEMPLATE_LINKED'})
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.list_policies_input.ListPoliciesInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.list_policies_output.ListPoliciesOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.list_policies

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.list_policies.list_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.list_policies_input.ListPoliciesInput = {
            "policy_store_id": policy_store_id
        }
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

    def iter_list_policies(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "capo_verifiedpermissions.types.policy_filter.PolicyFilter"
        ] = None,
    ) -> "Iterator[capo_verifiedpermissions.types.policy_item.PolicyItem]":
        _token = next_token
        while True:
            _response = self.list_policies(
                policy_store_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_policy_template(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        statement: "capo_verifiedpermissions.types.policy_statement.PolicyStatement",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        client_token: Optional[
            "capo_verifiedpermissions.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "capo_verifiedpermissions.types.policy_template_description.PolicyTemplateDescription"
        ] = None,
        name: Optional[
            "capo_verifiedpermissions.types.policy_template_name.PolicyTemplateName"
        ] = None,
    ) -> "capo_verifiedpermissions.types.create_policy_template_output.CreatePolicyTemplateOutput":
        r"""<p>Creates a policy template. A template can use placeholders for the principal and resource. A template must be instantiated into a policy by associating it with specific principals and resources to use for the placeholders. That instantiated policy can then be considered in authorization decisions. The instantiated policy works identically to any other policy, except that it is dynamically linked to the template. If the template changes, then any policies that are linked to that template are immediately updated as well.</p> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            client_token: <p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>ConflictException</code> error.</p> <p>Verified Permissions recognizes a <code>ClientToken</code> for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of <code>ClientToken</code>.</p>
            policy_store_id: <p>The ID of the policy store in which to create the policy template.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            description: <p>Specifies a description for the policy template.</p>
            statement: <p>Specifies the content that you want to use for the new policy template, written in the Cedar policy language.</p>
            name: <p>Specifies a name for the policy template that is unique among all policy templates within the policy store. You can use the name in place of the policy template ID in API operations that reference the policy template. The name must be prefixed with <code>name/</code>.</p> <p>If you specify a name that is already associated with another policy template in the policy store, you receive a <code>ConflictException</code> error.</p>

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
            To create a policy template
            The following example creates a policy template that has a placeholder for the principal.

            >>> client.create_policy_template(description='Template for research dept', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', statement='"AccessVacation"\npermit(\n    principal in ?principal,\n    action == Action::"view",\n    resource == Photo::"VacationPhoto94.jpg"\n)\nwhen {\n    principal has department && principal.department == "research"\n};', client_token='a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111', name='name/example-policy-template')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.create_policy_template_input.CreatePolicyTemplateInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.create_policy_template_output.CreatePolicyTemplateOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.create_policy_template

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.create_policy_template.create_policy_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.create_policy_template_input.CreatePolicyTemplateInput = {
            "policy_store_id": policy_store_id,
            "statement": statement,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policy_template(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        policy_template_id: "capo_verifiedpermissions.types.policy_template_id.PolicyTemplateId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.get_policy_template_output.GetPolicyTemplateOutput":
        """<p>Retrieve the details for the specified policy template in the specified policy store.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the policy template that you want information about.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            policy_template_id: <p>Specifies the ID of the policy template that you want information about.</p> <p>You can use the policy template name in place of the policy template ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>PTEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy-template</code> </p> </li> </ul>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetPolicyTemplate
            The following example displays the details of the specified policy template.

            >>> client.get_policy_template(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', policy_template_id='PTEXAMPLEabcdefg111111')
            To retrieve a policy template by name
            The following example retrieves the details of a policy template using its name instead of its ID.

            >>> client.get_policy_template(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', policy_template_id='name/example-policy-template')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.get_policy_template_input.GetPolicyTemplateInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.get_policy_template_output.GetPolicyTemplateOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.get_policy_template

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.get_policy_template.get_policy_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.get_policy_template_input.GetPolicyTemplateInput = {
            "policy_store_id": policy_store_id,
            "policy_template_id": policy_template_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_policy_template(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        policy_template_id: "capo_verifiedpermissions.types.policy_template_id.PolicyTemplateId",
        statement: "capo_verifiedpermissions.types.policy_statement.PolicyStatement",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        description: Optional[
            "capo_verifiedpermissions.types.policy_template_description.PolicyTemplateDescription"
        ] = None,
        name: Optional[
            "capo_verifiedpermissions.types.policy_template_name.PolicyTemplateName"
        ] = None,
    ) -> "capo_verifiedpermissions.types.update_policy_template_output.UpdatePolicyTemplateOutput":
        r"""<p>Updates the specified policy template. You can update only the description and the some elements of the <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html#amazonverifiedpermissions-UpdatePolicyTemplate-request-policyBody">policyBody</a>. </p> <important> <p>Changes you make to the policy template content are immediately (within the constraints of eventual consistency) reflected in authorization decisions that involve all template-linked policies instantiated from this template.</p> </important> <note> <p>Verified Permissions is <i> <a href="https://wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

                Args:
                    policy_store_id: <p>Specifies the ID of the policy store that contains the policy template that you want to update.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
                    policy_template_id: <p>Specifies the ID of the policy template that you want to update.</p> <p>You can use the policy template name in place of the policy template ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>PTEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy-template</code> </p> </li> </ul>
                    description: <p>Specifies a new description to apply to the policy template.</p>
                    statement: <p>Specifies new statement content written in Cedar policy language to replace the current body of the policy template.</p> <p>You can change only the following elements of the policy body:</p> <ul> <li> <p>The <code>action</code> referenced by the policy template.</p> </li> <li> <p>Any conditional clauses, such as <code>when</code> or <code>unless</code> clauses.</p> </li> </ul> <p>You <b>can't</b> change the following elements:</p> <ul> <li> <p>The effect (<code>permit</code> or <code>forbid</code>) of the policy template.</p> </li> <li> <p>The <code>principal</code> referenced by the policy template.</p> </li> <li> <p>The <code>resource</code> referenced by the policy template.</p> </li> </ul>
                    name: <p>Specifies a name for the policy template that is unique among all policy templates within the policy store. You can use the name in place of the policy template ID in API operations that reference the policy template. The name must be prefixed with <code>name/</code>.</p> <note> <p>If you don't include the name in an update request, the existing name is unchanged. To remove a name, set it to an empty string (<code>""</code>).</p> </note> <p>If you specify a name that is already associated with another policy template in the policy store, you receive a <code>ConflictException</code> error.</p>

                Raises:
                    capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
                    capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
                    capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
                    capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
                    capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
                    capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
                    capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    UpdatePolicyTemplate
                    The following example updates a policy template with both a new description and a new policy body. The effect, principal, and resource are the same as the original policy template. Only the action in the head, and the when and unless clauses can be different.

        Note
        The JSON in the parameters of this operation are strings that can contain embedded quotation marks (") within the outermost quotation mark pair. This requires that you stringify the JSON object by preceding all embedded quotation marks with a backslash character ( \" ) and combining all lines into a single text line with no line breaks.

        Example strings might be displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

                    >>> client.update_policy_template(description='My updated template description', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', policy_template_id='PTEXAMPLEabcdefg111111', statement='"ResearchAccess"\npermit(\nprincipal in ?principal,\naction == Action::"view",\nresource in ?resource"\n)\nwhen {\nprincipal has department && principal.department == "research"\n};', name='name/example-policy-template-2')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.update_policy_template_input.UpdatePolicyTemplateInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.update_policy_template_output.UpdatePolicyTemplateOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.update_policy_template

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.update_policy_template.update_policy_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.update_policy_template_input.UpdatePolicyTemplateInput = {
            "policy_store_id": policy_store_id,
            "policy_template_id": policy_template_id,
            "statement": statement,
        }
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_policy_template(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        policy_template_id: "capo_verifiedpermissions.types.policy_template_id.PolicyTemplateId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "capo_verifiedpermissions.types.delete_policy_template_output.DeletePolicyTemplateOutput":
        """<p>Deletes the specified policy template from the policy store.</p> <important> <p>This operation also deletes any policies that were created from the specified policy template. Those policies are immediately removed from all future API responses, and are asynchronously deleted from the policy store.</p> </important>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the policy template that you want to delete.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            policy_template_id: <p>Specifies the ID of the policy template that you want to delete.</p> <p>You can use the policy template name in place of the policy template ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>PTEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy-template</code> </p> </li> </ul>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.conflict_exception.ConflictException: <p>The request failed because another request to modify a resource occurred at the same time.</p>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a policy template
            The following example deletes a policy template. Before you can perform this operation, you must first delete any template-linked policies that were instantiated from this policy template. To delete them, use DeletePolicy.

            >>> client.delete_policy_template(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a', policy_template_id='PTEXAMPLEabcdefg111111')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.delete_policy_template_input.DeletePolicyTemplateInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.delete_policy_template_output.DeletePolicyTemplateOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.delete_policy_template

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.delete_policy_template.delete_policy_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.delete_policy_template_input.DeletePolicyTemplateInput = {
            "policy_store_id": policy_store_id,
            "policy_template_id": policy_template_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policy_templates(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_verifiedpermissions.types.list_policy_templates_output.ListPolicyTemplatesOutput":
        """<p>Returns a paginated list of all policy templates in the specified policy store.</p>

        Args:
            policy_store_id: <p>Specifies the ID of the policy store that contains the policy templates you want to list.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 10 policy templates per response. You can specify a maximum of 50 policy templates per response.</p>

        Raises:
            capo_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            capo_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            capo_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href="https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            capo_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            capo_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListPolicyTemplates
            The following example retrieves a list of all of the policy templates in the specified policy store.

            >>> client.list_policy_templates(policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[capo_verifiedpermissions.types.list_policy_templates_input.ListPolicyTemplatesInput]",
        ) -> OperationResponse[
            "capo_verifiedpermissions.types.list_policy_templates_output.ListPolicyTemplatesOutput"
        ]:
            import capo_verifiedpermissions._operations.verified_permissions.list_policy_templates

            output, http_response = (
                capo_verifiedpermissions._operations.verified_permissions.list_policy_templates.list_policy_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_verifiedpermissions.types.list_policy_templates_input.ListPolicyTemplatesInput = {
            "policy_store_id": policy_store_id
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

    def iter_list_policy_templates(
        self,
        policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "capo_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_verifiedpermissions.types.policy_template_item.PolicyTemplateItem]":
        _token = next_token
        while True:
            _response = self.list_policy_templates(
                policy_store_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_policy_store_alias(
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

            >>> client.create_policy_store_alias(alias_name='policy-store-alias/example-policy-store', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def get_policy_store_alias(
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

            >>> client.get_policy_store_alias(alias_name='policy-store-alias/example-policy-store')
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_policy_store_alias(
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

            >>> client.delete_policy_store_alias(alias_name='policy-store-alias/example-policy-store')
            Hard delete a policy store alias
            The following example hard deletes the policy store alias with name example-policy-store. The alias is immediately deleted, bypassing the PendingDeletion state.

            >>> client.delete_policy_store_alias(alias_name='policy-store-alias/example-policy-store', deletion_mode='HardDelete')
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_policy_store_aliases(
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

            >>> client.list_policy_store_aliases()
            ListPolicyStoreAliases - Example 2
            The following example lists all policy store aliases associated with the policy store with ID C7v5xMplfFH3i3e4Jrzb1a

            >>> client.list_policy_store_aliases(filter={'policyStoreId': 'C7v5xMplfFH3i3e4Jrzb1a'})
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_policy_store_aliases(
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
    ) -> "Iterator[capo_verifiedpermissions.types.policy_store_alias_item.PolicyStoreAliasItem]":
        _token = next_token
        while True:
            _response = self.list_policy_store_aliases(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("policy_store_aliases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
