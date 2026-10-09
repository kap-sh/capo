"""Generated from Smithy shape ``com.amazonaws.wickr#WickrAdminApi``."""

import datetime
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_wickr._auth._signers
import capo_wickr._auth._sigv4
from capo_wickr._auth._identity import Credentials
from capo_wickr._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_wickr._auth._zapros_handler import AuthMiddleware
from capo_wickr._pagination import resolve_path as _resolve_path
from capo_wickr._services._aws_config import aws_config
from capo_wickr._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_wickr.types.access_level
    import capo_wickr.types.app_ids
    import capo_wickr.types.basic_device_object
    import capo_wickr.types.batch_create_user_request
    import capo_wickr.types.batch_create_user_request_items
    import capo_wickr.types.batch_create_user_response
    import capo_wickr.types.batch_delete_user_request
    import capo_wickr.types.batch_delete_user_response
    import capo_wickr.types.batch_lookup_user_uname_request
    import capo_wickr.types.batch_lookup_user_uname_response
    import capo_wickr.types.batch_reinvite_user_request
    import capo_wickr.types.batch_reinvite_user_response
    import capo_wickr.types.batch_reset_devices_for_user_request
    import capo_wickr.types.batch_reset_devices_for_user_response
    import capo_wickr.types.batch_toggle_user_suspend_status_request
    import capo_wickr.types.batch_toggle_user_suspend_status_response
    import capo_wickr.types.blocked_guest_user
    import capo_wickr.types.bot
    import capo_wickr.types.bot_id
    import capo_wickr.types.bot_status
    import capo_wickr.types.client_token
    import capo_wickr.types.create_bot_request
    import capo_wickr.types.create_bot_response
    import capo_wickr.types.create_data_retention_bot_challenge_request
    import capo_wickr.types.create_data_retention_bot_challenge_response
    import capo_wickr.types.create_data_retention_bot_request
    import capo_wickr.types.create_data_retention_bot_response
    import capo_wickr.types.create_network_request
    import capo_wickr.types.create_network_response
    import capo_wickr.types.create_security_group_request
    import capo_wickr.types.create_security_group_response
    import capo_wickr.types.data_retention_action_type
    import capo_wickr.types.delete_bot_request
    import capo_wickr.types.delete_bot_response
    import capo_wickr.types.delete_data_retention_bot_request
    import capo_wickr.types.delete_data_retention_bot_response
    import capo_wickr.types.delete_network_request
    import capo_wickr.types.delete_network_response
    import capo_wickr.types.delete_security_group_request
    import capo_wickr.types.delete_security_group_response
    import capo_wickr.types.generic_string
    import capo_wickr.types.get_bot_request
    import capo_wickr.types.get_bot_response
    import capo_wickr.types.get_bots_count_request
    import capo_wickr.types.get_bots_count_response
    import capo_wickr.types.get_data_retention_bot_request
    import capo_wickr.types.get_data_retention_bot_response
    import capo_wickr.types.get_guest_user_history_count_request
    import capo_wickr.types.get_guest_user_history_count_response
    import capo_wickr.types.get_network_request
    import capo_wickr.types.get_network_response
    import capo_wickr.types.get_network_settings_request
    import capo_wickr.types.get_network_settings_response
    import capo_wickr.types.get_oidc_info_request
    import capo_wickr.types.get_oidc_info_response
    import capo_wickr.types.get_opentdf_config_request
    import capo_wickr.types.get_opentdf_config_response
    import capo_wickr.types.get_security_group_request
    import capo_wickr.types.get_security_group_response
    import capo_wickr.types.get_user_request
    import capo_wickr.types.get_user_response
    import capo_wickr.types.get_users_count_request
    import capo_wickr.types.get_users_count_response
    import capo_wickr.types.guest_user
    import capo_wickr.types.list_blocked_guest_users_request
    import capo_wickr.types.list_blocked_guest_users_response
    import capo_wickr.types.list_bots_request
    import capo_wickr.types.list_bots_response
    import capo_wickr.types.list_devices_for_user_request
    import capo_wickr.types.list_devices_for_user_response
    import capo_wickr.types.list_guest_users_request
    import capo_wickr.types.list_guest_users_response
    import capo_wickr.types.list_networks_request
    import capo_wickr.types.list_networks_response
    import capo_wickr.types.list_security_group_users_request
    import capo_wickr.types.list_security_group_users_response
    import capo_wickr.types.list_security_groups_request
    import capo_wickr.types.list_security_groups_response
    import capo_wickr.types.list_users_request
    import capo_wickr.types.list_users_response
    import capo_wickr.types.network
    import capo_wickr.types.network_id
    import capo_wickr.types.network_settings
    import capo_wickr.types.register_oidc_config_request
    import capo_wickr.types.register_oidc_config_response
    import capo_wickr.types.register_oidc_config_test_request
    import capo_wickr.types.register_oidc_config_test_response
    import capo_wickr.types.register_opentdf_config_request
    import capo_wickr.types.register_opentdf_config_response
    import capo_wickr.types.security_group
    import capo_wickr.types.security_group_settings
    import capo_wickr.types.security_group_settings_request
    import capo_wickr.types.sensitive_string
    import capo_wickr.types.sort_direction
    import capo_wickr.types.unames
    import capo_wickr.types.update_bot_request
    import capo_wickr.types.update_bot_response
    import capo_wickr.types.update_data_retention_request
    import capo_wickr.types.update_data_retention_response
    import capo_wickr.types.update_guest_user_request
    import capo_wickr.types.update_guest_user_response
    import capo_wickr.types.update_network_request
    import capo_wickr.types.update_network_response
    import capo_wickr.types.update_network_settings_request
    import capo_wickr.types.update_network_settings_response
    import capo_wickr.types.update_security_group_request
    import capo_wickr.types.update_security_group_response
    import capo_wickr.types.update_user_details
    import capo_wickr.types.update_user_request
    import capo_wickr.types.update_user_response
    import capo_wickr.types.user
    import capo_wickr.types.user_id
    import capo_wickr.types.user_ids
    import capo_wickr.types.user_status


class WickrClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class WickrClient:
    """A client for the ``Wickr`` service.

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
        self._config = WickrClientConfig(
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
        self, config_overrides: Optional[WickrClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WickrClientConfig = config_overrides or {}
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

    def batch_create_user(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        users: "capo_wickr.types.batch_create_user_request_items.BatchCreateUserRequestItems",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_token: Optional["capo_wickr.types.client_token.ClientToken"] = None,
    ) -> "capo_wickr.types.batch_create_user_response.BatchCreateUserResponse":
        """<p>Creates multiple users in a specified Wickr network. This operation allows you to provision multiple user accounts simultaneously, optionally specifying security groups, and validation requirements for each user.</p> <note> <p> <code>codeValidation</code>, <code>inviteCode</code>, and <code>inviteCodeTtl</code> are restricted to networks under preview only.</p> </note>

        Args:
            network_id: <p>The ID of the Wickr network where users will be created.</p>
            users: <p>A list of user objects containing the details for each user to be created, including username, name, security groups, and optional invite codes. Maximum 50 users per batch request.</p>
            client_token: <p>A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without creating duplicate users.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create multiple users

            >>> client.batch_create_user(network_id='12345678', users=[{'firstName': 'John', 'lastName': 'Doe', 'username': 'john.doe@example.com', 'securityGroupIds': ['BCTY8Qhe'], 'inviteCode': 'INVITE123', 'inviteCodeTtl': 7, 'codeValidation': True}, {'firstName': 'Jane', 'lastName': 'Smith', 'username': 'jane.smith@example.com', 'securityGroupIds': ['BCTY8Qhe']}], client_token='550e8400-e29b-41d4-a716-446655440000')
            Partial failure - duplicate user

            >>> client.batch_create_user(network_id='12345678', users=[{'firstName': 'Alice', 'lastName': 'Johnson', 'username': 'alice.johnson@example.com', 'securityGroupIds': ['BCTY8Qhe']}, {'firstName': 'Bob', 'lastName': 'Wilson', 'username': 'existing.user@example.com', 'securityGroupIds': ['BCTY8Qhe']}])
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.batch_create_user_request.BatchCreateUserRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.batch_create_user_response.BatchCreateUserResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.batch_create_user

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.batch_create_user.batch_create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.batch_create_user_request.BatchCreateUserRequest = {
            "network_id": network_id,
            "users": users,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_user(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        user_ids: "capo_wickr.types.user_ids.UserIds",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_token: Optional["capo_wickr.types.client_token.ClientToken"] = None,
    ) -> "capo_wickr.types.batch_delete_user_response.BatchDeleteUserResponse":
        """<p>Deletes multiple users from a specified Wickr network. This operation permanently removes user accounts and their associated data from the network.</p>

        Args:
            network_id: <p>The ID of the Wickr network from which users will be deleted.</p>
            user_ids: <p>A list of user IDs identifying the users to be deleted from the network. Maximum 50 users per batch request.</p>
            client_token: <p>A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without attempting to delete users again.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete multiple users

            >>> client.batch_delete_user(network_id='12345678', user_ids=['123', '456'], client_token='6ba7b814-9dad-11d1-80b4-00c04fd430c8')
            Partial failure - user not found

            >>> client.batch_delete_user(network_id='12345678', user_ids=['123', '456'])
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.batch_delete_user_request.BatchDeleteUserRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.batch_delete_user_response.BatchDeleteUserResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.batch_delete_user

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.batch_delete_user.batch_delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.batch_delete_user_request.BatchDeleteUserRequest = {
            "network_id": network_id,
            "user_ids": user_ids,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_lookup_user_uname(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        unames: "capo_wickr.types.unames.Unames",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_token: Optional["capo_wickr.types.client_token.ClientToken"] = None,
    ) -> (
        "capo_wickr.types.batch_lookup_user_uname_response.BatchLookupUserUnameResponse"
    ):
        """<p>Looks up multiple user usernames from their unique username hashes (unames). This operation allows you to retrieve the email addresses associated with a list of username hashes.</p>

        Args:
            network_id: <p>The ID of the Wickr network where the users will be looked up.</p>
            unames: <p>A list of username hashes (unames) to look up. Each uname is a unique identifier for a user's username. Maximum 50 unames per batch request.</p>
            client_token: <p>A unique identifier for this request to ensure idempotency.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Lookup multiple user unames

            >>> client.batch_lookup_user_uname(network_id='12345678', unames=['a1b2c3d4e5f6', 'g7h8i9j0k1l2'], client_token='f47ac10b-58cc-4372-a567-0e02b2c3d479')
            Partial failure - uname not found

            >>> client.batch_lookup_user_uname(network_id='12345678', unames=['a1b2c3d4e5f6', 'invaliduname'])
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.batch_lookup_user_uname_request.BatchLookupUserUnameRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.batch_lookup_user_uname_response.BatchLookupUserUnameResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.batch_lookup_user_uname

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.batch_lookup_user_uname.batch_lookup_user_uname(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.batch_lookup_user_uname_request.BatchLookupUserUnameRequest = {
            "network_id": network_id,
            "unames": unames,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_reinvite_user(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        user_ids: "capo_wickr.types.user_ids.UserIds",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_token: Optional["capo_wickr.types.client_token.ClientToken"] = None,
    ) -> "capo_wickr.types.batch_reinvite_user_response.BatchReinviteUserResponse":
        """<p>Resends invitation codes to multiple users who have pending invitations in a Wickr network. This operation is useful when users haven't accepted their initial invitations or when invitations have expired.</p>

        Args:
            network_id: <p>The ID of the Wickr network where users will be reinvited.</p>
            user_ids: <p>A list of user IDs identifying the users to be reinvited to the network. Maximum 50 users per batch request.</p>
            client_token: <p>A unique identifier for this request to ensure idempotency.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Batch reinvite users successfully

            >>> client.batch_reinvite_user(network_id='12345678', user_ids=['12345', '67890'])
            Batch reinvite users - partial success

            >>> client.batch_reinvite_user(network_id='12345678', user_ids=['12345', '99999'])
            Batch reinvite users - cannot reinvite

            >>> client.batch_reinvite_user(network_id='12345678', user_ids=['54321'])
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.batch_reinvite_user_request.BatchReinviteUserRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.batch_reinvite_user_response.BatchReinviteUserResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.batch_reinvite_user

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.batch_reinvite_user.batch_reinvite_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.batch_reinvite_user_request.BatchReinviteUserRequest = {
            "network_id": network_id,
            "user_ids": user_ids,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_reset_devices_for_user(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        user_id: "capo_wickr.types.user_id.UserId",
        app_ids: "capo_wickr.types.app_ids.AppIds",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_token: Optional["capo_wickr.types.client_token.ClientToken"] = None,
    ) -> "capo_wickr.types.batch_reset_devices_for_user_response.BatchResetDevicesForUserResponse":
        """<p>Resets multiple devices for a specific user in a Wickr network. This operation forces the selected devices to log out and requires users to re-authenticate, which is useful for security purposes or when devices need to be revoked.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the user whose devices will be reset.</p>
            user_id: <p>The ID of the user whose devices will be reset.</p>
            app_ids: <p>A list of application IDs identifying the specific devices to be reset for the user. Maximum 50 devices per batch request.</p>
            client_token: <p>A unique identifier for this request to ensure idempotency.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful device reset

            >>> client.batch_reset_devices_for_user(network_id='12345678', user_id='12345', app_ids=['d3135a42dcb6437780b16c3ca9581fe64e6822773cd6b965d25fc9929c89aca6', 'e4246b53edc7548891c27d4da0692fe75f7933884de7c076e36gca030d90bdb7'])
            Partial failure device reset

            >>> client.batch_reset_devices_for_user(network_id='12345678', user_id='12345', app_ids=['d3135a42dcb6437780b16c3ca9581fe64e6822773cd6b965d25fc9929c89aca6', 'invalid-app-id'])
            Invalid network ID error

            >>> client.batch_reset_devices_for_user(network_id='00000000', user_id='12345', app_ids=['d3135a42dcb6437780b16c3ca9581fe64e6822773cd6b965d25fc9929c89aca6'])
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.batch_reset_devices_for_user_request.BatchResetDevicesForUserRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.batch_reset_devices_for_user_response.BatchResetDevicesForUserResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.batch_reset_devices_for_user

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.batch_reset_devices_for_user.batch_reset_devices_for_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.batch_reset_devices_for_user_request.BatchResetDevicesForUserRequest = {
            "network_id": network_id,
            "user_id": user_id,
            "app_ids": app_ids,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_toggle_user_suspend_status(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        suspend: bool,
        user_ids: "capo_wickr.types.user_ids.UserIds",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_token: Optional["capo_wickr.types.client_token.ClientToken"] = None,
    ) -> "capo_wickr.types.batch_toggle_user_suspend_status_response.BatchToggleUserSuspendStatusResponse":
        """<p>Suspends or unsuspends multiple users in a Wickr network. Suspended users cannot access the network until they are unsuspended. This operation is useful for temporarily restricting access without deleting user accounts.</p>

        Args:
            network_id: <p>The ID of the Wickr network where users will be suspended or unsuspended.</p>
            suspend: <p>A boolean value indicating whether to suspend (true) or unsuspend (false) the specified users.</p>
            user_ids: <p>A list of user IDs identifying the users whose suspend status will be toggled. Maximum 50 users per batch request.</p>
            client_token: <p>A unique identifier for this request to ensure idempotency.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Suspend multiple users

            >>> client.batch_toggle_user_suspend_status(network_id='12345678', user_ids=['123', '456'], suspend=True, client_token='6ba7b815-9dad-11d1-80b4-00c04fd430c8')
            Unsuspend users with partial failure

            >>> client.batch_toggle_user_suspend_status(network_id='12345678', user_ids=['123', '456'], suspend=False)
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.batch_toggle_user_suspend_status_request.BatchToggleUserSuspendStatusRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.batch_toggle_user_suspend_status_response.BatchToggleUserSuspendStatusResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.batch_toggle_user_suspend_status

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.batch_toggle_user_suspend_status.batch_toggle_user_suspend_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.batch_toggle_user_suspend_status_request.BatchToggleUserSuspendStatusRequest = {
            "network_id": network_id,
            "suspend": suspend,
            "user_ids": user_ids,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_bot(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        username: "capo_wickr.types.generic_string.GenericString",
        group_id: "capo_wickr.types.generic_string.GenericString",
        challenge: "capo_wickr.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        display_name: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "capo_wickr.types.create_bot_response.CreateBotResponse":
        """<p>Creates a new bot in a specified Wickr network. Bots are automated accounts that can send and receive messages, enabling integration with external systems and automation of tasks.</p>

        Args:
            network_id: <p>The ID of the Wickr network where the bot will be created.</p>
            username: <p>The username for the bot. This must be unique within the network and follow the network's naming conventions.</p>
            display_name: <p>The display name for the bot that will be visible to users in the network.</p>
            group_id: <p>The ID of the security group to which the bot will be assigned.</p>
            challenge: <p>The password for the bot account.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create bot successfully

            >>> client.create_bot(network_id='12345678', username='analytics_bot', display_name='Analytics Bot', challenge='SecureP@ssw0rd123', group_id='analytics_group')
            Create bot - username unavailable

            >>> client.create_bot(network_id='12345678', username='support_bot', display_name='Support Bot', group_id='default_group', challenge='SecureP@ssw0rd123')
            Create bot - invalid username format

            >>> client.create_bot(network_id='12345678', username='bot@invalid', display_name='Test Bot', group_id='default_group', challenge='SecureP@ssw0rd123')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.create_bot_request.CreateBotRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.create_bot_response.CreateBotResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.create_bot

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.create_bot.create_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.create_bot_request.CreateBotRequest = {
            "network_id": network_id,
            "username": username,
            "group_id": group_id,
            "challenge": challenge,
        }
        if display_name is not None:
            input_["display_name"] = display_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_retention_bot(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.create_data_retention_bot_response.CreateDataRetentionBotResponse":
        """<p>Creates a data retention bot in a Wickr network. Data retention bots are specialized bots that handle message archiving and compliance by capturing and storing messages for regulatory or organizational requirements.</p>

        Args:
            network_id: <p>The ID of the Wickr network where the data retention bot will be created.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create data retention bot successfully

            >>> client.create_data_retention_bot(network_id='12345678')
            Create data retention bot - users already exist

            >>> client.create_data_retention_bot(network_id='12345678')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.create_data_retention_bot_request.CreateDataRetentionBotRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.create_data_retention_bot_response.CreateDataRetentionBotResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.create_data_retention_bot

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.create_data_retention_bot.create_data_retention_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.create_data_retention_bot_request.CreateDataRetentionBotRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_retention_bot_challenge(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.create_data_retention_bot_challenge_response.CreateDataRetentionBotChallengeResponse":
        """<p>Creates a new challenge password for the data retention bot. This password is used for authentication when the bot connects to the network.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the data retention bot.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create data retention bot challenge successfully

            >>> client.create_data_retention_bot_challenge(network_id='12345678')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.create_data_retention_bot_challenge_request.CreateDataRetentionBotChallengeRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.create_data_retention_bot_challenge_response.CreateDataRetentionBotChallengeResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.create_data_retention_bot_challenge

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.create_data_retention_bot_challenge.create_data_retention_bot_challenge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.create_data_retention_bot_challenge_request.CreateDataRetentionBotChallengeRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_network(
        self,
        network_name: "capo_wickr.types.generic_string.GenericString",
        access_level: "capo_wickr.types.access_level.AccessLevel",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        enable_premium_free_trial: Optional[bool] = None,
        encryption_key_arn: Optional[
            "capo_wickr.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_wickr.types.create_network_response.CreateNetworkResponse":
        """<p>Creates a new Wickr network with specified access level and configuration. This operation provisions a new communication network for your organization.</p>

        Args:
            network_name: <p>The name for the new network. Must be between 1 and 20 characters.</p>
            access_level: <p>The access level for the network. Valid values are STANDARD or PREMIUM, which determine the features and capabilities available to network members.</p>
            enable_premium_free_trial: <p>Specifies whether to enable a premium free trial for the network. It is optional and has a default value as false. When set to true, the network starts with premium features for a limited trial period. </p>
            encryption_key_arn: <p>The ARN of the Amazon Web Services KMS customer managed key to use for encrypting sensitive data in the network.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create network successfully

            >>> client.create_network(network_name='Production Network', access_level='PREMIUM', enable_premium_free_trial=False)
            Create network with free trial

            >>> client.create_network(network_name='Trial Network', access_level='PREMIUM', enable_premium_free_trial=True)
            Create network - invalid name

            >>> client.create_network(network_name='This network name is way too long', access_level='STANDARD')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.create_network_request.CreateNetworkRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.create_network_response.CreateNetworkResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.create_network

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.create_network.create_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.create_network_request.CreateNetworkRequest = {
            "network_name": network_name,
            "access_level": access_level,
        }
        if enable_premium_free_trial is not None:
            input_["enable_premium_free_trial"] = enable_premium_free_trial
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_security_group(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        name: "capo_wickr.types.generic_string.GenericString",
        security_group_settings: "capo_wickr.types.security_group_settings_request.SecurityGroupSettingsRequest",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_token: Optional["capo_wickr.types.client_token.ClientToken"] = None,
    ) -> "capo_wickr.types.create_security_group_response.CreateSecurityGroupResponse":
        """<p>Creates a new security group in a Wickr network. Security groups allow you to organize users and control their permissions, features, and security settings.</p>

        Args:
            network_id: <p>The ID of the Wickr network where the security group will be created.</p>
            name: <p>The name for the new security group.</p>
            security_group_settings: <p>The configuration settings for the security group, including permissions, federation settings, and feature controls.</p>
            client_token: <p>A unique identifier for this request to ensure idempotency.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create security group successfully

            >>> client.create_security_group(network_id='12345678', name='engineering', security_group_settings={'federationMode': 1, 'lockoutThreshold': 10})
            Create security group - missing name

            >>> client.create_security_group(network_id='12345678', name='', security_group_settings={'federationMode': 1})
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.create_security_group_request.CreateSecurityGroupRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.create_security_group_response.CreateSecurityGroupResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.create_security_group

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.create_security_group.create_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.create_security_group_request.CreateSecurityGroupRequest = {
            "network_id": network_id,
            "name": name,
            "security_group_settings": security_group_settings,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_bot(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        bot_id: "capo_wickr.types.bot_id.BotId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.delete_bot_response.DeleteBotResponse":
        """<p>Deletes a bot from a specified Wickr network. This operation permanently removes the bot account and its associated data from the network.</p>

        Args:
            network_id: <p>The ID of the Wickr network from which the bot will be deleted.</p>
            bot_id: <p>The unique identifier of the bot to be deleted.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete bot successfully

            >>> client.delete_bot(network_id='12345678', bot_id='98765')
            Delete bot - bot not found

            >>> client.delete_bot(network_id='12345678', bot_id='99999')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.delete_bot_request.DeleteBotRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.delete_bot_response.DeleteBotResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.delete_bot

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.delete_bot.delete_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.delete_bot_request.DeleteBotRequest = {
            "network_id": network_id,
            "bot_id": bot_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_retention_bot(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.delete_data_retention_bot_response.DeleteDataRetentionBotResponse":
        """<p>Deletes the data retention bot from a Wickr network. This operation permanently removes the bot and all its associated data from the database.</p>

        Args:
            network_id: <p>The ID of the Wickr network from which the data retention bot will be deleted.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete data retention bot successfully

            >>> client.delete_data_retention_bot(network_id='12345678')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.delete_data_retention_bot_request.DeleteDataRetentionBotRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.delete_data_retention_bot_response.DeleteDataRetentionBotResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.delete_data_retention_bot

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.delete_data_retention_bot.delete_data_retention_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.delete_data_retention_bot_request.DeleteDataRetentionBotRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_network(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_token: Optional["capo_wickr.types.client_token.ClientToken"] = None,
    ) -> "capo_wickr.types.delete_network_response.DeleteNetworkResponse":
        """<p>Deletes a Wickr network and all its associated resources, including users, bots, security groups, and settings. This operation is permanent and cannot be undone.</p>

        Args:
            network_id: <p>The ID of the Wickr network to delete.</p>
            client_token: <p>A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without attempting to delete the network again.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete network successfully

            >>> client.delete_network(network_id='12345678')
            Delete network - not found

            >>> client.delete_network(network_id='99999999')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.delete_network_request.DeleteNetworkRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.delete_network_response.DeleteNetworkResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.delete_network

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.delete_network.delete_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.delete_network_request.DeleteNetworkRequest = {
            "network_id": network_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_security_group(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        group_id: "capo_wickr.types.generic_string.GenericString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.delete_security_group_response.DeleteSecurityGroupResponse":
        """<p>Deletes a security group from a Wickr network. This operation cannot be performed on the default security group.</p>

        Args:
            network_id: <p>The ID of the Wickr network from which the security group will be deleted.</p>
            group_id: <p>The unique identifier of the security group to delete.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete security group successfully

            >>> client.delete_security_group(network_id='12345678', group_id='def67890')
            Delete security group - not found

            >>> client.delete_security_group(network_id='12345678', group_id='invalid99')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.delete_security_group_request.DeleteSecurityGroupRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.delete_security_group_response.DeleteSecurityGroupResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.delete_security_group

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.delete_security_group.delete_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.delete_security_group_request.DeleteSecurityGroupRequest = {
            "network_id": network_id,
            "group_id": group_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_bot(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        bot_id: "capo_wickr.types.bot_id.BotId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.get_bot_response.GetBotResponse":
        """<p>Retrieves detailed information about a specific bot in a Wickr network, including its status, group membership, and authentication details.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the bot.</p>
            bot_id: <p>The unique identifier of the bot to retrieve.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get bot successfully

            >>> client.get_bot(network_id='12345678', bot_id='98765')
            Get bot - bot not found

            >>> client.get_bot(network_id='12345678', bot_id='99999')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_bot_request.GetBotRequest]",
        ) -> OperationResponse["capo_wickr.types.get_bot_response.GetBotResponse"]:
            import capo_wickr._operations.wickr_admin_api.get_bot

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_bot.get_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_bot_request.GetBotRequest = {
            "network_id": network_id,
            "bot_id": bot_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_bots_count(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.get_bots_count_response.GetBotsCountResponse":
        """<p>Retrieves the count of bots in a Wickr network, categorized by their status (pending, active, and total).</p>

        Args:
            network_id: <p>The ID of the Wickr network for which to retrieve bot counts.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get bots count successfully

            >>> client.get_bots_count(network_id='12345678')
            Get bots count with filters

            >>> client.get_bots_count(network_id='12345678')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_bots_count_request.GetBotsCountRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.get_bots_count_response.GetBotsCountResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.get_bots_count

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_bots_count.get_bots_count(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_bots_count_request.GetBotsCountRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_retention_bot(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.get_data_retention_bot_response.GetDataRetentionBotResponse":
        """<p>Retrieves information about the data retention bot in a Wickr network, including its status and whether the data retention service is enabled.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the data retention bot.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get data retention bot successfully

            >>> client.get_data_retention_bot(network_id='12345678')
            Get data retention bot - not provisioned

            >>> client.get_data_retention_bot(network_id='12345678')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_data_retention_bot_request.GetDataRetentionBotRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.get_data_retention_bot_response.GetDataRetentionBotResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.get_data_retention_bot

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_data_retention_bot.get_data_retention_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_data_retention_bot_request.GetDataRetentionBotRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_guest_user_history_count(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.get_guest_user_history_count_response.GetGuestUserHistoryCountResponse":
        """<p>Retrieves historical guest user count data for a Wickr network, showing the number of guest users per billing period over the past 90 days.</p>

        Args:
            network_id: <p>The ID of the Wickr network for which to retrieve guest user history.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get guest user history count

            >>> client.get_guest_user_history_count(network_id='12345678')
            Empty response for network with no guest user history

            >>> client.get_guest_user_history_count(network_id='87654321')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_guest_user_history_count_request.GetGuestUserHistoryCountRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.get_guest_user_history_count_response.GetGuestUserHistoryCountResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.get_guest_user_history_count

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_guest_user_history_count.get_guest_user_history_count(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_guest_user_history_count_request.GetGuestUserHistoryCountRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_network(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.get_network_response.GetNetworkResponse":
        """<p>Retrieves detailed information about a specific Wickr network, including its configuration, access level, and status.</p>

        Args:
            network_id: <p>The ID of the Wickr network to retrieve.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get network successfully

            >>> client.get_network(network_id='12345678')
            Get network - not found

            >>> client.get_network(network_id='99999999')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_network_request.GetNetworkRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.get_network_response.GetNetworkResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.get_network

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_network.get_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_network_request.GetNetworkRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_network_settings(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.get_network_settings_response.GetNetworkSettingsResponse":
        """<p>Retrieves all network-level settings for a Wickr network, including client metrics, data retention, and other configuration options.</p>

        Args:
            network_id: <p>The ID of the Wickr network whose settings will be retrieved.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get network settings with mixed value types

            >>> client.get_network_settings(network_id='12345678')
            Get settings for network with defaults only

            >>> client.get_network_settings(network_id='87654321')
            Network not found error

            >>> client.get_network_settings(network_id='99999999')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_network_settings_request.GetNetworkSettingsRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.get_network_settings_response.GetNetworkSettingsResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.get_network_settings

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_network_settings.get_network_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_network_settings_request.GetNetworkSettingsRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_oidc_info(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_id: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        code: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        grant_type: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        redirect_uri: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        url: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        client_secret: Optional[
            "capo_wickr.types.sensitive_string.SensitiveString"
        ] = None,
        code_verifier: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        certificate: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "capo_wickr.types.get_oidc_info_response.GetOidcInfoResponse":
        """<p>Retrieves the OpenID Connect (OIDC) configuration for a Wickr network, including SSO settings and optional token information if access token parameters are provided.</p>

        Args:
            network_id: <p>The ID of the Wickr network whose OIDC configuration will be retrieved.</p>
            client_id: <p>The OAuth client ID for retrieving access tokens (optional).</p>
            code: <p>The authorization code for retrieving access tokens (optional).</p>
            grant_type: <p>The OAuth grant type for retrieving access tokens (optional).</p>
            redirect_uri: <p>The redirect URI for the OAuth flow (optional).</p>
            url: <p>The URL for the OIDC provider (optional).</p>
            client_secret: <p>The OAuth client secret for retrieving access tokens (optional).</p>
            code_verifier: <p>The PKCE code verifier for enhanced security in the OAuth flow (optional).</p>
            certificate: <p>The CA certificate for secure communication with the OIDC provider (optional).</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get OIDC info successfully

            >>> client.get_oidc_info(network_id='12345678')
            Get OIDC info - not configured

            >>> client.get_oidc_info(network_id='12345678')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_oidc_info_request.GetOidcInfoRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.get_oidc_info_response.GetOidcInfoResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.get_oidc_info

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_oidc_info.get_oidc_info(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_oidc_info_request.GetOidcInfoRequest = {
            "network_id": network_id
        }
        if client_id is not None:
            input_["client_id"] = client_id
        if code is not None:
            input_["code"] = code
        if grant_type is not None:
            input_["grant_type"] = grant_type
        if redirect_uri is not None:
            input_["redirect_uri"] = redirect_uri
        if url is not None:
            input_["url"] = url
        if client_secret is not None:
            input_["client_secret"] = client_secret
        if code_verifier is not None:
            input_["code_verifier"] = code_verifier
        if certificate is not None:
            input_["certificate"] = certificate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_opentdf_config(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.get_opentdf_config_response.GetOpentdfConfigResponse":
        """<p>Retrieves the OpenTDF integration configuration for a Wickr network.</p>

        Args:
            network_id: <p>The ID of the Wickr network for which OpenTDF integration will be retrieved.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get OpenTDF info successfully

            >>> client.get_opentdf_config(network_id='12345678')
            Get OpenTDF info - not configured

            >>> client.get_opentdf_config(network_id='12345678')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_opentdf_config_request.GetOpentdfConfigRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.get_opentdf_config_response.GetOpentdfConfigResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.get_opentdf_config

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_opentdf_config.get_opentdf_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_opentdf_config_request.GetOpentdfConfigRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_security_group(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        group_id: "capo_wickr.types.generic_string.GenericString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.get_security_group_response.GetSecurityGroupResponse":
        """<p>Retrieves detailed information about a specific security group in a Wickr network, including its settings, member counts, and configuration.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the security group.</p>
            group_id: <p>The unique identifier of the security group to retrieve.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get security group successfully

            >>> client.get_security_group(network_id='12345678', group_id='abc12345')
            Get security group - not found

            >>> client.get_security_group(network_id='12345678', group_id='invalid99')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_security_group_request.GetSecurityGroupRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.get_security_group_response.GetSecurityGroupResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.get_security_group

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_security_group.get_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_security_group_request.GetSecurityGroupRequest = {
            "network_id": network_id,
            "group_id": group_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_user(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        user_id: "capo_wickr.types.user_id.UserId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "capo_wickr.types.get_user_response.GetUserResponse":
        """<p>Retrieves detailed information about a specific user in a Wickr network, including their profile, status, and activity history.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the user.</p>
            user_id: <p>The unique identifier of the user to retrieve.</p>
            start_time: <p>The start time for filtering the user's last activity. Only activity after this timestamp will be considered. Time is specified in epoch seconds.</p>
            end_time: <p>The end time for filtering the user's last activity. Only activity before this timestamp will be considered. Time is specified in epoch seconds.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get user information

            >>> client.get_user(network_id='12345678', user_id='12345')
            Get user info with activity time range

            >>> client.get_user(network_id='12345678', user_id='12345', start_time=1704067200, end_time=1705500000)
            User not found error

            >>> client.get_user(network_id='12345678', user_id='99999')
            Invalid userId error

            >>> client.get_user(network_id='12345678', user_id='99999')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_user_request.GetUserRequest]",
        ) -> OperationResponse["capo_wickr.types.get_user_response.GetUserResponse"]:
            import capo_wickr._operations.wickr_admin_api.get_user

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_user.get_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_user_request.GetUserRequest = {
            "network_id": network_id,
            "user_id": user_id,
        }
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_users_count(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.get_users_count_response.GetUsersCountResponse":
        """<p>Retrieves the count of users in a Wickr network, categorized by their status (pending, active, rejected) and showing how many users can still be added.</p>

        Args:
            network_id: <p>The ID of the Wickr network for which to retrieve user counts.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get user counts for network

            >>> client.get_users_count(network_id='12345678')
            Network with no users

            >>> client.get_users_count(network_id='87654321')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.get_users_count_request.GetUsersCountRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.get_users_count_response.GetUsersCountResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.get_users_count

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.get_users_count.get_users_count(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.get_users_count_request.GetUsersCountRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_blocked_guest_users(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        max_results: Optional[int] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        username: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        admin: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "capo_wickr.types.list_blocked_guest_users_response.ListBlockedGuestUsersResponse":
        """<p>Retrieves a paginated list of guest users who have been blocked from a Wickr network. You can filter and sort the results.</p>

        Args:
            network_id: <p>The ID of the Wickr network from which to list blocked guest users.</p>
            max_results: <p>The maximum number of blocked guest users to return in a single page. Valid range is 1-100. Default is 10.</p>
            sort_direction: <p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>
            sort_fields: <p>The field to sort blocked guest users by. Accepted values include 'username', 'admin', and 'modified'.</p>
            username: <p>Filter results to only include blocked guest users with usernames matching this value.</p>
            admin: <p>Filter results to only include blocked guest users that were blocked by this administrator.</p>
            next_token: <p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get paginated list of blocked guest users

            >>> client.list_blocked_guest_users(network_id='12345678', max_results=10, sort_direction='DESC', sort_fields='modified')
            Filter by username

            >>> client.list_blocked_guest_users(network_id='12345678', username='john.doe@example.com')
            Empty blocklist

            >>> client.list_blocked_guest_users(network_id='12345678')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.list_blocked_guest_users_request.ListBlockedGuestUsersRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.list_blocked_guest_users_response.ListBlockedGuestUsersResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.list_blocked_guest_users

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.list_blocked_guest_users.list_blocked_guest_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.list_blocked_guest_users_request.ListBlockedGuestUsersRequest = {
            "network_id": network_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_direction is not None:
            input_["sort_direction"] = sort_direction
        if sort_fields is not None:
            input_["sort_fields"] = sort_fields
        if username is not None:
            input_["username"] = username
        if admin is not None:
            input_["admin"] = admin
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_blocked_guest_users(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        max_results: Optional[int] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        username: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        admin: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "Iterator[capo_wickr.types.blocked_guest_user.BlockedGuestUser]":
        _token = next_token
        while True:
            _response = self.list_blocked_guest_users(
                network_id,
                config_overrides=config_overrides,
                max_results=max_results,
                sort_direction=sort_direction,
                sort_fields=sort_fields,
                username=username,
                admin=admin,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("blocklist",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_bots(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        display_name: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        username: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        status: Optional["capo_wickr.types.bot_status.BotStatus"] = None,
        group_id: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "capo_wickr.types.list_bots_response.ListBotsResponse":
        """<p>Retrieves a paginated list of bots in a specified Wickr network. You can filter and sort the results based on various criteria.</p>

        Args:
            network_id: <p>The ID of the Wickr network from which to list bots.</p>
            next_token: <p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>
            max_results: <p>The maximum number of bots to return in a single page. Valid range is 1-100. Default is 10.</p>
            sort_fields: <p>The fields to sort bots by. Multiple fields can be specified by separating them with '+'. Accepted values include 'username', 'firstName', 'displayName', 'status', and 'groupId'.</p>
            sort_direction: <p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>
            display_name: <p>Filter results to only include bots with display names matching this value.</p>
            username: <p>Filter results to only include bots with usernames matching this value.</p>
            status: <p>Filter results to only include bots with this status (1 for pending, 2 for active).</p>
            group_id: <p>Filter results to only include bots belonging to this security group.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List bots with pagination

            >>> client.list_bots(network_id='12345678', max_results=10, sort_fields='username', sort_direction='ASC')
            List bots with filters

            >>> client.list_bots(network_id='12345678', max_results=10, display_name='Support', status=2)
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.list_bots_request.ListBotsRequest]",
        ) -> OperationResponse["capo_wickr.types.list_bots_response.ListBotsResponse"]:
            import capo_wickr._operations.wickr_admin_api.list_bots

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.list_bots.list_bots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.list_bots_request.ListBotsRequest = {
            "network_id": network_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_fields is not None:
            input_["sort_fields"] = sort_fields
        if sort_direction is not None:
            input_["sort_direction"] = sort_direction
        if display_name is not None:
            input_["display_name"] = display_name
        if username is not None:
            input_["username"] = username
        if status is not None:
            input_["status"] = status
        if group_id is not None:
            input_["group_id"] = group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_bots(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        display_name: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        username: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        status: Optional["capo_wickr.types.bot_status.BotStatus"] = None,
        group_id: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "Iterator[capo_wickr.types.bot.Bot]":
        _token = next_token
        while True:
            _response = self.list_bots(
                network_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                sort_fields=sort_fields,
                sort_direction=sort_direction,
                display_name=display_name,
                username=username,
                status=status,
                group_id=group_id,
            )
            _page = _resolve_path(_response, ("bots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_devices_for_user(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        user_id: "capo_wickr.types.user_id.UserId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
    ) -> "capo_wickr.types.list_devices_for_user_response.ListDevicesForUserResponse":
        """<p>Retrieves a paginated list of devices associated with a specific user in a Wickr network. This operation returns information about all devices where the user has logged into Wickr.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the user.</p>
            user_id: <p>The unique identifier of the user whose devices will be listed.</p>
            next_token: <p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>
            max_results: <p>The maximum number of devices to return in a single page. Valid range is 1-100. Default is 10.</p>
            sort_fields: <p>The fields to sort devices by. Multiple fields can be specified by separating them with '+'. Accepted values include 'lastlogin', 'type', 'suspend', and 'created'.</p>
            sort_direction: <p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful device list retrieval

            >>> client.list_devices_for_user(network_id='12345678', user_id='12345', max_results=10, sort_fields='appId', sort_direction='DESC')
            Retrieving subsequent page of devices

            >>> client.list_devices_for_user(network_id='12345678', user_id='12345', max_results=10, next_token='v1:pagination:6ba7b810-9dad-11d1-80b4-00c04fd430c8')
            Invalid userId error

            >>> client.list_devices_for_user(network_id='12345678', user_id='99999', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.list_devices_for_user_request.ListDevicesForUserRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.list_devices_for_user_response.ListDevicesForUserResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.list_devices_for_user

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.list_devices_for_user.list_devices_for_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.list_devices_for_user_request.ListDevicesForUserRequest = {
            "network_id": network_id,
            "user_id": user_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_fields is not None:
            input_["sort_fields"] = sort_fields
        if sort_direction is not None:
            input_["sort_direction"] = sort_direction

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_devices_for_user(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        user_id: "capo_wickr.types.user_id.UserId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
    ) -> "Iterator[capo_wickr.types.basic_device_object.BasicDeviceObject]":
        _token = next_token
        while True:
            _response = self.list_devices_for_user(
                network_id,
                user_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                sort_fields=sort_fields,
                sort_direction=sort_direction,
            )
            _page = _resolve_path(_response, ("devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_guest_users(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        max_results: Optional[int] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        username: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        billing_period: Optional[
            "capo_wickr.types.generic_string.GenericString"
        ] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "capo_wickr.types.list_guest_users_response.ListGuestUsersResponse":
        """<p>Retrieves a paginated list of guest users who have communicated with your Wickr network. Guest users are external users from federated networks who can communicate with network members.</p>

        Args:
            network_id: <p>The ID of the Wickr network from which to list guest users.</p>
            max_results: <p>The maximum number of guest users to return in a single page. Valid range is 1-100. Default is 10.</p>
            sort_direction: <p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>
            sort_fields: <p>The field to sort guest users by. Accepted values include 'username' and 'billingPeriod'.</p>
            username: <p>Filter results to only include guest users with usernames matching this value.</p>
            billing_period: <p>Filter results to only include guest users from this billing period (e.g., '2024-01').</p>
            next_token: <p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get paginated list of guest users

            >>> client.list_guest_users(network_id='12345678', max_results=20, sort_direction='DESC', sort_fields='billingPeriod')
            Filter by billing period

            >>> client.list_guest_users(network_id='12345678', billing_period='2024-01', max_results=10)
            Empty guest list

            >>> client.list_guest_users(network_id='87654321')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.list_guest_users_request.ListGuestUsersRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.list_guest_users_response.ListGuestUsersResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.list_guest_users

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.list_guest_users.list_guest_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.list_guest_users_request.ListGuestUsersRequest = {
            "network_id": network_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_direction is not None:
            input_["sort_direction"] = sort_direction
        if sort_fields is not None:
            input_["sort_fields"] = sort_fields
        if username is not None:
            input_["username"] = username
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_guest_users(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        max_results: Optional[int] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        username: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        billing_period: Optional[
            "capo_wickr.types.generic_string.GenericString"
        ] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "Iterator[capo_wickr.types.guest_user.GuestUser]":
        _token = next_token
        while True:
            _response = self.list_guest_users(
                network_id,
                config_overrides=config_overrides,
                max_results=max_results,
                sort_direction=sort_direction,
                sort_fields=sort_fields,
                username=username,
                billing_period=billing_period,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("guestlist",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_networks(
        self,
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "capo_wickr.types.list_networks_response.ListNetworksResponse":
        """<p>Retrieves a paginated list of all Wickr networks associated with your Amazon Web Services account. You can sort the results by network ID or name.</p>

        Args:
            max_results: <p>The maximum number of networks to return in a single page. Valid range is 1-100. Default is 10.</p>
            sort_fields: <p>The field to sort networks by. Accepted values are 'networkId' and 'networkName'. Default is 'networkId'.</p>
            sort_direction: <p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>
            next_token: <p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List networks with pagination

            >>> client.list_networks(max_results=10, sort_fields='networkName', sort_direction='ASC')
            List networks - first page

            >>> client.list_networks(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.list_networks_request.ListNetworksRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.list_networks_response.ListNetworksResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.list_networks

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.list_networks.list_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.list_networks_request.ListNetworksRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_fields is not None:
            input_["sort_fields"] = sort_fields
        if sort_direction is not None:
            input_["sort_direction"] = sort_direction
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_networks(
        self,
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "Iterator[capo_wickr.types.network.Network]":
        _token = next_token
        while True:
            _response = self.list_networks(
                config_overrides=config_overrides,
                max_results=max_results,
                sort_fields=sort_fields,
                sort_direction=sort_direction,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("networks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_security_groups(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
    ) -> "capo_wickr.types.list_security_groups_response.ListSecurityGroupsResponse":
        """<p>Retrieves a paginated list of security groups in a specified Wickr network. You can sort the results by various criteria.</p>

        Args:
            network_id: <p>The ID of the Wickr network from which to list security groups.</p>
            next_token: <p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>
            max_results: <p>The maximum number of security groups to return in a single page. Valid range is 1-100. Default is 10.</p>
            sort_fields: <p>The field to sort security groups by. Accepted values include 'id' and 'name'.</p>
            sort_direction: <p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List security groups with pagination

            >>> client.list_security_groups(network_id='12345678', max_results=10, sort_fields='name', sort_direction='ASC')
            List security groups - first page

            >>> client.list_security_groups(network_id='12345678', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.list_security_groups_request.ListSecurityGroupsRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.list_security_groups_response.ListSecurityGroupsResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.list_security_groups

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.list_security_groups.list_security_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.list_security_groups_request.ListSecurityGroupsRequest = {
            "network_id": network_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_fields is not None:
            input_["sort_fields"] = sort_fields
        if sort_direction is not None:
            input_["sort_direction"] = sort_direction

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_security_groups(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
    ) -> "Iterator[capo_wickr.types.security_group.SecurityGroup]":
        _token = next_token
        while True:
            _response = self.list_security_groups(
                network_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                sort_fields=sort_fields,
                sort_direction=sort_direction,
            )
            _page = _resolve_path(_response, ("security_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_security_group_users(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        group_id: "capo_wickr.types.generic_string.GenericString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
    ) -> "capo_wickr.types.list_security_group_users_response.ListSecurityGroupUsersResponse":
        """<p>Retrieves a paginated list of users who belong to a specific security group in a Wickr network.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the security group.</p>
            group_id: <p>The unique identifier of the security group whose users will be listed.</p>
            next_token: <p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>
            max_results: <p>The maximum number of users to return in a single page. Valid range is 1-100. Default is 10.</p>
            sort_fields: <p>The field to sort users by. Multiple fields can be specified by separating them with '+'. Accepted values include 'username', 'firstName', and 'lastName'.</p>
            sort_direction: <p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List security group users with pagination

            >>> client.list_security_group_users(network_id='12345678', group_id='abc12345', max_results=10, sort_fields='username', sort_direction='ASC')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.list_security_group_users_request.ListSecurityGroupUsersRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.list_security_group_users_response.ListSecurityGroupUsersResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.list_security_group_users

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.list_security_group_users.list_security_group_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.list_security_group_users_request.ListSecurityGroupUsersRequest = {
            "network_id": network_id,
            "group_id": group_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_fields is not None:
            input_["sort_fields"] = sort_fields
        if sort_direction is not None:
            input_["sort_direction"] = sort_direction

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_security_group_users(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        group_id: "capo_wickr.types.generic_string.GenericString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
    ) -> "Iterator[capo_wickr.types.user.User]":
        _token = next_token
        while True:
            _response = self.list_security_group_users(
                network_id,
                group_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                sort_fields=sort_fields,
                sort_direction=sort_direction,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_users(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        first_name: Optional[
            "capo_wickr.types.sensitive_string.SensitiveString"
        ] = None,
        last_name: Optional["capo_wickr.types.sensitive_string.SensitiveString"] = None,
        username: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        status: Optional["capo_wickr.types.user_status.UserStatus"] = None,
        group_id: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "capo_wickr.types.list_users_response.ListUsersResponse":
        """<p>Retrieves a paginated list of users in a specified Wickr network. You can filter and sort the results based on various criteria such as name, status, or security group membership.</p>

        Args:
            network_id: <p>The ID of the Wickr network from which to list users.</p>
            next_token: <p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>
            max_results: <p>The maximum number of users to return in a single page. Valid range is 1-100. Default is 10.</p>
            sort_fields: <p>The fields to sort users by. Multiple fields can be specified by separating them with '+'. Accepted values include 'username', 'firstName', 'lastName', 'status', and 'groupId'.</p>
            sort_direction: <p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>
            first_name: <p>Filter results to only include users with first names matching this value.</p>
            last_name: <p>Filter results to only include users with last names matching this value.</p>
            username: <p>Filter results to only include users with usernames matching this value.</p>
            status: <p>Filter results to only include users with this status (1 for pending, 2 for active).</p>
            group_id: <p>Filter results to only include users belonging to this security group.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get paginated list of users

            >>> client.list_users(network_id='12345678', max_results=20, sort_fields='username', sort_direction='ASC')
            Filter by status and group

            >>> client.list_users(network_id='12345678', status=1, group_id='BCTY8Qhe', max_results=10)
            Empty user list for network with no users

            >>> client.list_users(network_id='12345678')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.list_users_response.ListUsersResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.list_users

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.list_users.list_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.list_users_request.ListUsersRequest = {
            "network_id": network_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_fields is not None:
            input_["sort_fields"] = sort_fields
        if sort_direction is not None:
            input_["sort_direction"] = sort_direction
        if first_name is not None:
            input_["first_name"] = first_name
        if last_name is not None:
            input_["last_name"] = last_name
        if username is not None:
            input_["username"] = username
        if status is not None:
            input_["status"] = status
        if group_id is not None:
            input_["group_id"] = group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_users(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        next_token: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        max_results: Optional[int] = None,
        sort_fields: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        sort_direction: Optional[
            "capo_wickr.types.sort_direction.SortDirection"
        ] = None,
        first_name: Optional[
            "capo_wickr.types.sensitive_string.SensitiveString"
        ] = None,
        last_name: Optional["capo_wickr.types.sensitive_string.SensitiveString"] = None,
        username: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        status: Optional["capo_wickr.types.user_status.UserStatus"] = None,
        group_id: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "Iterator[capo_wickr.types.user.User]":
        _token = next_token
        while True:
            _response = self.list_users(
                network_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                sort_fields=sort_fields,
                sort_direction=sort_direction,
                first_name=first_name,
                last_name=last_name,
                username=username,
                status=status,
                group_id=group_id,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def register_oidc_config(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        company_id: "capo_wickr.types.generic_string.GenericString",
        issuer: "capo_wickr.types.generic_string.GenericString",
        scopes: "capo_wickr.types.generic_string.GenericString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        custom_username: Optional[
            "capo_wickr.types.generic_string.GenericString"
        ] = None,
        extra_auth_params: Optional[
            "capo_wickr.types.generic_string.GenericString"
        ] = None,
        secret: Optional["capo_wickr.types.sensitive_string.SensitiveString"] = None,
        sso_token_buffer_minutes: Optional[int] = None,
        user_id: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "capo_wickr.types.register_oidc_config_response.RegisterOidcConfigResponse":
        """<p>Registers and saves an OpenID Connect (OIDC) configuration for a Wickr network, enabling Single Sign-On (SSO) authentication through an identity provider.</p>

        Args:
            network_id: <p>The ID of the Wickr network for which OIDC will be configured.</p>
            company_id: <p>Custom identifier your end users will use to sign in with SSO.</p>
            custom_username: <p>A custom field mapping to extract the username from the OIDC token (optional). </p> <note> <p>The customUsername is only required if you use something other than email as the username field.</p> </note>
            extra_auth_params: <p>Additional authentication parameters to include in the OIDC flow (optional).</p>
            issuer: <p>The issuer URL of the OIDC provider (e.g., 'https://login.example.com').</p>
            scopes: <p>The OAuth scopes to request from the OIDC provider (e.g., 'openid profile email').</p>
            secret: <p>The client secret for authenticating with the OIDC provider (optional).</p>
            sso_token_buffer_minutes: <p>The buffer time in minutes before the SSO token expires to refresh it (optional).</p>
            user_id: <p>Unique identifier provided by your identity provider to authenticate the access request. Also referred to as clientID.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Save OIDC config successfully

            >>> client.register_oidc_config(network_id='12345678', company_id='us-east-1-company123', issuer='https://login.example.com', scopes='openid profile email', user_id='email', sso_token_buffer_minutes=5)
            Save OIDC config - missing company ID

            >>> client.register_oidc_config(network_id='12345678', company_id='', issuer='https://login.example.com', scopes='openid profile email')
            Save OIDC config - invalid company ID prefix

            >>> client.register_oidc_config(network_id='12345678', company_id='invalid-company123', issuer='https://login.example.com', scopes='openid profile email')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.register_oidc_config_request.RegisterOidcConfigRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.register_oidc_config_response.RegisterOidcConfigResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.register_oidc_config

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.register_oidc_config.register_oidc_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.register_oidc_config_request.RegisterOidcConfigRequest = {
            "network_id": network_id,
            "company_id": company_id,
            "issuer": issuer,
            "scopes": scopes,
        }
        if custom_username is not None:
            input_["custom_username"] = custom_username
        if extra_auth_params is not None:
            input_["extra_auth_params"] = extra_auth_params
        if secret is not None:
            input_["secret"] = secret
        if sso_token_buffer_minutes is not None:
            input_["sso_token_buffer_minutes"] = sso_token_buffer_minutes
        if user_id is not None:
            input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_oidc_config_test(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        issuer: "capo_wickr.types.generic_string.GenericString",
        scopes: "capo_wickr.types.generic_string.GenericString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        extra_auth_params: Optional[
            "capo_wickr.types.generic_string.GenericString"
        ] = None,
        certificate: Optional["capo_wickr.types.generic_string.GenericString"] = None,
    ) -> "capo_wickr.types.register_oidc_config_test_response.RegisterOidcConfigTestResponse":
        """<p>Tests an OpenID Connect (OIDC) configuration for a Wickr network by validating the connection to the identity provider and retrieving its supported capabilities.</p>

        Args:
            network_id: <p>The ID of the Wickr network for which the OIDC configuration will be tested.</p>
            extra_auth_params: <p>Additional authentication parameters to include in the test (optional).</p>
            issuer: <p>The issuer URL of the OIDC provider to test.</p>
            scopes: <p>The OAuth scopes to test with the OIDC provider.</p>
            certificate: <p>The CA certificate for secure communication with the OIDC provider (optional).</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Test OIDC config successfully

            >>> client.register_oidc_config_test(network_id='12345678', issuer='https://login.example.com', scopes='openid profile email')
            Test OIDC config - missing issuer

            >>> client.register_oidc_config_test(network_id='12345678', issuer='', scopes='openid profile email')
            Test OIDC config - invalid endpoint

            >>> client.register_oidc_config_test(network_id='12345678', issuer='https://blocked-endpoint.com', scopes='openid profile email')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.register_oidc_config_test_request.RegisterOidcConfigTestRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.register_oidc_config_test_response.RegisterOidcConfigTestResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.register_oidc_config_test

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.register_oidc_config_test.register_oidc_config_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.register_oidc_config_test_request.RegisterOidcConfigTestRequest = {
            "network_id": network_id,
            "issuer": issuer,
            "scopes": scopes,
        }
        if extra_auth_params is not None:
            input_["extra_auth_params"] = extra_auth_params
        if certificate is not None:
            input_["certificate"] = certificate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_opentdf_config(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        client_id: "capo_wickr.types.generic_string.GenericString",
        client_secret: "capo_wickr.types.sensitive_string.SensitiveString",
        domain: "capo_wickr.types.generic_string.GenericString",
        provider: "capo_wickr.types.generic_string.GenericString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_wickr.types.register_opentdf_config_response.RegisterOpentdfConfigResponse":
        """<p>Registers and saves OpenTDF configuration for a Wickr network, enabling attribute-based access control for Wickr through an OpenTDF provider.</p>

        Args:
            network_id: <p>The ID of the Wickr network for which OpenTDF integration will be configured.</p>
            client_id: <p>The OIDC client ID used for authenticating with the OpenTDF provider.</p>
            client_secret: <p>The OIDC client secret used for authenticating with the OpenTDF provider</p>
            domain: <p>The domain of the OpenTDF server.</p>
            provider: <p>The provider of the OpenTDF platform.</p> <note> <p>Currently only Virtru is supported as the OpenTDF provider.</p> </note>
            dry_run: <p>Perform dry-run test connection of OpenTDF configuration (optional).</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Save OpenTDF config successfully

            >>> client.register_opentdf_config(network_id='12345678', client_id='client123', client_secret='secret456', domain='https://api.sample.com', provider='virtru')
            Dry run saving OpenTDF config

            >>> client.register_opentdf_config(network_id='12345678', client_id='client123', client_secret='secret456', domain='https://api.sample.com', provider='virtru', dry_run=True)
            Dry run saving OpenTDF config - failed test

            >>> client.register_opentdf_config(network_id='12345678', client_id='client123', client_secret='secret456', domain='https://api.sample.com', provider='virtru', dry_run=True)
            Save OpenTDF config - invalid provider

            >>> client.register_opentdf_config(network_id='12345678', client_id='client123', client_secret='secret456', domain='https://api.sample.com', provider='invalid provider')
            Save OpenTDF config - network not found

            >>> client.register_opentdf_config(network_id='99999999', client_id='client123', client_secret='secret456', domain='https://api.sample.com', provider='virtru')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.register_opentdf_config_request.RegisterOpentdfConfigRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.register_opentdf_config_response.RegisterOpentdfConfigResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.register_opentdf_config

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.register_opentdf_config.register_opentdf_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.register_opentdf_config_request.RegisterOpentdfConfigRequest = {
            "network_id": network_id,
            "client_id": client_id,
            "client_secret": client_secret,
            "domain": domain,
            "provider": provider,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bot(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        bot_id: "capo_wickr.types.bot_id.BotId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        display_name: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        group_id: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        challenge: Optional["capo_wickr.types.sensitive_string.SensitiveString"] = None,
        suspend: Optional[bool] = None,
    ) -> "capo_wickr.types.update_bot_response.UpdateBotResponse":
        """<p>Updates the properties of an existing bot in a Wickr network. This operation allows you to modify the bot's display name, security group, password, or suspension status.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the bot to update.</p>
            bot_id: <p>The unique identifier of the bot to update.</p>
            display_name: <p>The new display name for the bot.</p>
            group_id: <p>The ID of the new security group to assign the bot to.</p>
            challenge: <p>The new password for the bot account.</p>
            suspend: <p>Set to true to suspend the bot or false to unsuspend it. Omit this field for standard updates that don't affect suspension status.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update bot successfully

            >>> client.update_bot(network_id='12345678', bot_id='98765', display_name='Updated Support Bot', group_id='support_group')
            Update bot - bot not found

            >>> client.update_bot(network_id='12345678', bot_id='99999', display_name='Updated Bot')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.update_bot_request.UpdateBotRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.update_bot_response.UpdateBotResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.update_bot

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.update_bot.update_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.update_bot_request.UpdateBotRequest = {
            "network_id": network_id,
            "bot_id": bot_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if group_id is not None:
            input_["group_id"] = group_id
        if challenge is not None:
            input_["challenge"] = challenge
        if suspend is not None:
            input_["suspend"] = suspend

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_retention(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        action_type: "capo_wickr.types.data_retention_action_type.DataRetentionActionType",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.update_data_retention_response.UpdateDataRetentionResponse":
        """<p>Updates the data retention bot settings, allowing you to enable or disable the data retention service, or acknowledge the public key message.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the data retention bot.</p>
            action_type: <p>The action to perform. Valid values are 'ENABLE' (to enable the data retention service), 'DISABLE' (to disable the service), or 'PUBKEY_MSG_ACK' (to acknowledge the public key message).</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update data retention - enable service

            >>> client.update_data_retention(network_id='12345678', action_type='ENABLE')
            Update data retention - disable service

            >>> client.update_data_retention(network_id='12345678', action_type='DISABLE')
            Update data retention - acknowledge pubkey message

            >>> client.update_data_retention(network_id='12345678', action_type='PUBKEY_MSG_ACK')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.update_data_retention_request.UpdateDataRetentionRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.update_data_retention_response.UpdateDataRetentionResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.update_data_retention

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.update_data_retention.update_data_retention(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.update_data_retention_request.UpdateDataRetentionRequest = {
            "network_id": network_id,
            "action_type": action_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_guest_user(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        username_hash: "capo_wickr.types.generic_string.GenericString",
        block: bool,
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.update_guest_user_response.UpdateGuestUserResponse":
        """<p>Updates the block status of a guest user in a Wickr network. This operation allows you to block or unblock a guest user from accessing the network.</p>

        Args:
            network_id: <p>The ID of the Wickr network where the guest user's status will be updated.</p>
            username_hash: <p>The username hash (unique identifier) of the guest user to update.</p>
            block: <p>Set to true to block the guest user or false to unblock them.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Block a guest user

            >>> client.update_guest_user(network_id='12345678', username_hash='032c36d5623781204592a69269ed9480d604484269c8a4c2d39528885a56470d', block=True)
            Unblock a guest user

            >>> client.update_guest_user(network_id='12345678', username_hash='032c36d5623781204592a69269ed9480d604484269c8a4c2d39528885a56470d', block=False)
            User already blocked error

            >>> client.update_guest_user(network_id='12345678', username_hash='032c36d5623781204592a69269ed9480d604484269c8a4c2d39528885a56470d', block=True)
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.update_guest_user_request.UpdateGuestUserRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.update_guest_user_response.UpdateGuestUserResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.update_guest_user

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.update_guest_user.update_guest_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.update_guest_user_request.UpdateGuestUserRequest = {
            "network_id": network_id,
            "username_hash": username_hash,
            "block": block,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_network(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        network_name: "capo_wickr.types.generic_string.GenericString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        client_token: Optional["capo_wickr.types.client_token.ClientToken"] = None,
        encryption_key_arn: Optional[
            "capo_wickr.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_wickr.types.update_network_response.UpdateNetworkResponse":
        """<p>Updates the properties of an existing Wickr network, such as its name or encryption key configuration.</p>

        Args:
            network_id: <p>The ID of the Wickr network to update.</p>
            network_name: <p>The new name for the network. Must be between 1 and 20 characters.</p>
            client_token: <p>A unique identifier for this request to ensure idempotency.</p>
            encryption_key_arn: <p>The ARN of the Amazon Web Services KMS customer managed key to use for encrypting sensitive data in the network.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update network name successfully

            >>> client.update_network(network_id='12345678', network_name='Updated Network Name')
            Update network - invalid name

            >>> client.update_network(network_id='12345678', network_name='This name is way too long for a network')
            Update network - not found

            >>> client.update_network(network_id='99999999', network_name='New Name')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.update_network_request.UpdateNetworkRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.update_network_response.UpdateNetworkResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.update_network

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.update_network.update_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.update_network_request.UpdateNetworkRequest = {
            "network_id": network_id,
            "network_name": network_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_network_settings(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        settings: "capo_wickr.types.network_settings.NetworkSettings",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
    ) -> "capo_wickr.types.update_network_settings_response.UpdateNetworkSettingsResponse":
        """<p>Updates network-level settings for a Wickr network. You can modify settings such as client metrics, data retention, and other network-wide options.</p>

        Args:
            network_id: <p>The ID of the Wickr network whose settings will be updated.</p>
            settings: <p>A map of setting names to their new values. Each setting should be provided with its appropriate type (boolean, string, number, etc.).</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update multiple network settings

            >>> client.update_network_settings(network_id='12345678', settings={'enableClientMetrics': True, 'dataRetention': True})
            Update single boolean setting

            >>> client.update_network_settings(network_id='12345678', settings={'enableClientMetrics': False})
            Update client metrics settings

            >>> client.update_network_settings(network_id='12345678', settings={'enableClientMetrics': True})
            Invalid setting name error

            >>> client.update_network_settings(network_id='12345678', settings={'enableClientMetrics': False})
            Network not found error

            >>> client.update_network_settings(network_id='99999999', settings={'enableClientMetrics': True})
            Invalid value type error

            >>> client.update_network_settings(network_id='12345678', settings={'dataRetention': True})
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.update_network_settings_request.UpdateNetworkSettingsRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.update_network_settings_response.UpdateNetworkSettingsResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.update_network_settings

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.update_network_settings.update_network_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.update_network_settings_request.UpdateNetworkSettingsRequest = {
            "network_id": network_id,
            "settings": settings,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_security_group(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        group_id: "capo_wickr.types.generic_string.GenericString",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        name: Optional["capo_wickr.types.generic_string.GenericString"] = None,
        security_group_settings: Optional[
            "capo_wickr.types.security_group_settings.SecurityGroupSettings"
        ] = None,
    ) -> "capo_wickr.types.update_security_group_response.UpdateSecurityGroupResponse":
        """<p>Updates the properties of an existing security group in a Wickr network, such as its name or settings.</p>

        Args:
            network_id: <p>The ID of the Wickr network containing the security group to update.</p>
            group_id: <p>The unique identifier of the security group to update.</p>
            name: <p>The new name for the security group.</p>
            security_group_settings: <p>The updated configuration settings for the security group.</p> <p>Federation mode - 0 (Local federation), 1 (Restricted federation), 2 (Global federation) </p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update security group successfully

            >>> client.update_security_group(network_id='12345678', group_id='abc12345', name='Updated Group Name', security_group_settings={'lockoutThreshold': 15})
            Update security group - not found

            >>> client.update_security_group(network_id='12345678', group_id='invalid99', name='New Name')
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.update_security_group_request.UpdateSecurityGroupRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.update_security_group_response.UpdateSecurityGroupResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.update_security_group

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.update_security_group.update_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.update_security_group_request.UpdateSecurityGroupRequest = {
            "network_id": network_id,
            "group_id": group_id,
        }
        if name is not None:
            input_["name"] = name
        if security_group_settings is not None:
            input_["security_group_settings"] = security_group_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_user(
        self,
        network_id: "capo_wickr.types.network_id.NetworkId",
        user_id: "capo_wickr.types.user_id.UserId",
        *,
        config_overrides: Optional[WickrClientConfig] = None,
        user_details: Optional[
            "capo_wickr.types.update_user_details.UpdateUserDetails"
        ] = None,
    ) -> "capo_wickr.types.update_user_response.UpdateUserResponse":
        """<p>Updates the properties of an existing user in a Wickr network. This operation allows you to modify the user's name, password, security group membership, and invite code settings.</p> <note> <p> <code>codeValidation</code>, <code>inviteCode</code>, and <code>inviteCodeTtl</code> are restricted to networks under preview only.</p> </note>

        Args:
            network_id: <p>The ID of the Wickr network containing the user to update.</p>
            user_id: <p>The unique identifier of the user to update.</p>
            user_details: <p>An object containing the user details to be updated, such as name, password, security groups, and invite code settings.</p>

        Raises:
            capo_wickr.errors.bad_request_error.BadRequestError: <p>The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.</p>
            capo_wickr.errors.forbidden_error.ForbiddenError: <p>Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.</p>
            capo_wickr.errors.internal_server_error.InternalServerError: <p>An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact Amazon Web Services Support.</p>
            capo_wickr.errors.rate_limit_error.RateLimitError: <p>The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.</p>
            capo_wickr.errors.resource_not_found_error.ResourceNotFoundError: <p>The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.</p>
            capo_wickr.errors.unauthorized_error.UnauthorizedError: <p>The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.</p>
            capo_wickr.errors.validation_error.ValidationError: <p>One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.</p>
            capo_wickr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update user information

            >>> client.update_user(network_id='12345678', user_id='12345', user_details={'firstName': 'Jonathan', 'lastName': 'Doe', 'username': 'john.doe@example.com', 'securityGroupIds': ['BCTY8Qhe', 'DEPT001']})
            Update user with invite code

            >>> client.update_user(network_id='12345678', user_id='12345', user_details={'firstName': 'Jane', 'lastName': 'Smith', 'username': 'jane.smith@example.com', 'inviteCode': 'NEWINVITE789', 'inviteCodeTtl': 14, 'codeValidation': True})
            User not found error

            >>> client.update_user(network_id='12345678', user_id='99999', user_details={'firstName': 'Non', 'lastName': 'Existent', 'username': 'nonexistent@example.com'})
            Invalid userId error

            >>> client.update_user(network_id='12345678', user_id='99999', user_details={'firstName': 'John', 'lastName': 'Doe', 'username': 'john.doe@example.com', 'securityGroupIds': ['BCTY8Qhe']})
        """

        def _handler(
            req: "OperationRequest[capo_wickr.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "capo_wickr.types.update_user_response.UpdateUserResponse"
        ]:
            import capo_wickr._operations.wickr_admin_api.update_user

            output, http_response = (
                capo_wickr._operations.wickr_admin_api.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wickr.types.update_user_request.UpdateUserRequest = {
            "network_id": network_id,
            "user_id": user_id,
        }
        if user_details is not None:
            input_["user_details"] = user_details

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
