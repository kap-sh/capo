"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DirectoryServiceData``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_directory_service_data._auth._signers
import capo_directory_service_data._auth._sigv4
from capo_directory_service_data._auth._identity import Credentials
from capo_directory_service_data._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_directory_service_data._auth._zapros_handler import AuthMiddleware
from capo_directory_service_data._pagination import resolve_path as _resolve_path
from capo_directory_service_data._services._aws_config import aws_config
from capo_directory_service_data._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_directory_service_data.types.add_group_member_request
    import capo_directory_service_data.types.add_group_member_result
    import capo_directory_service_data.types.attributes
    import capo_directory_service_data.types.client_token
    import capo_directory_service_data.types.create_group_request
    import capo_directory_service_data.types.create_group_result
    import capo_directory_service_data.types.create_user_request
    import capo_directory_service_data.types.create_user_result
    import capo_directory_service_data.types.delete_group_request
    import capo_directory_service_data.types.delete_group_result
    import capo_directory_service_data.types.delete_user_request
    import capo_directory_service_data.types.delete_user_result
    import capo_directory_service_data.types.describe_group_request
    import capo_directory_service_data.types.describe_group_result
    import capo_directory_service_data.types.describe_user_request
    import capo_directory_service_data.types.describe_user_result
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.disable_user_request
    import capo_directory_service_data.types.disable_user_result
    import capo_directory_service_data.types.email_address
    import capo_directory_service_data.types.given_name
    import capo_directory_service_data.types.group
    import capo_directory_service_data.types.group_name
    import capo_directory_service_data.types.group_scope
    import capo_directory_service_data.types.group_summary
    import capo_directory_service_data.types.group_type
    import capo_directory_service_data.types.ldap_display_name_list
    import capo_directory_service_data.types.list_group_members_request
    import capo_directory_service_data.types.list_group_members_result
    import capo_directory_service_data.types.list_groups_for_member_request
    import capo_directory_service_data.types.list_groups_for_member_result
    import capo_directory_service_data.types.list_groups_request
    import capo_directory_service_data.types.list_groups_result
    import capo_directory_service_data.types.list_users_request
    import capo_directory_service_data.types.list_users_result
    import capo_directory_service_data.types.max_results
    import capo_directory_service_data.types.member
    import capo_directory_service_data.types.member_name
    import capo_directory_service_data.types.next_token
    import capo_directory_service_data.types.realm
    import capo_directory_service_data.types.remove_group_member_request
    import capo_directory_service_data.types.remove_group_member_result
    import capo_directory_service_data.types.search_groups_request
    import capo_directory_service_data.types.search_groups_result
    import capo_directory_service_data.types.search_string
    import capo_directory_service_data.types.search_users_request
    import capo_directory_service_data.types.search_users_result
    import capo_directory_service_data.types.surname
    import capo_directory_service_data.types.update_group_request
    import capo_directory_service_data.types.update_group_result
    import capo_directory_service_data.types.update_type
    import capo_directory_service_data.types.update_user_request
    import capo_directory_service_data.types.update_user_result
    import capo_directory_service_data.types.user
    import capo_directory_service_data.types.user_name
    import capo_directory_service_data.types.user_summary


class DirectoryServiceDataClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class DirectoryServiceDataClient:
    """A client for the ``DirectoryServiceData`` service.

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
        self._config = DirectoryServiceDataClientConfig(
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
        self, config_overrides: Optional[DirectoryServiceDataClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DirectoryServiceDataClientConfig = config_overrides or {}
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

    def add_group_member(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        group_name: "capo_directory_service_data.types.group_name.GroupName",
        member_name: "capo_directory_service_data.types.member_name.MemberName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        member_realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        client_token: Optional[
            "capo_directory_service_data.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_directory_service_data.types.add_group_member_result.AddGroupMemberResult"
    ):
        """<p>Adds an existing user, group, or computer as a group member.</p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the group. </p>
            group_name: <p> The name of the group. </p>
            member_name: <p> The <code>SAMAccountName</code> of the user, group, or computer to add as a group member. </p>
            member_realm: <p> The domain name that's associated with the group member. This parameter is required only when adding a member outside of your Managed Microsoft AD domain to a group inside of your Managed Microsoft AD domain. This parameter defaults to the Managed Microsoft AD domain. </p> <note> <p> This parameter is case insensitive. </p> </note>
            client_token: <p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.conflict_exception.ConflictException: <p> This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.</p> <p> This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a member to the Marketing group
            The following command adds an existing user to the Marketing group in the europe.example.com domain.

            >>> client.add_group_member(client_token='550e8400-e29b-41d4-a716-446655440000', directory_id='d-12233abcde', group_name='Marketing', member_name='Pat Candella', member_realm='europe.example.com')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.add_group_member_request.AddGroupMemberRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.add_group_member_result.AddGroupMemberResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.add_group_member

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.add_group_member.add_group_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.add_group_member_request.AddGroupMemberRequest = {
            "directory_id": directory_id,
            "group_name": group_name,
            "member_name": member_name,
        }
        if member_realm is not None:
            input_["member_realm"] = member_realm
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

    def create_group(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.group_name.GroupName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        group_type: Optional[
            "capo_directory_service_data.types.group_type.GroupType"
        ] = None,
        group_scope: Optional[
            "capo_directory_service_data.types.group_scope.GroupScope"
        ] = None,
        other_attributes: Optional[
            "capo_directory_service_data.types.attributes.Attributes"
        ] = None,
        client_token: Optional[
            "capo_directory_service_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_directory_service_data.types.create_group_result.CreateGroupResult":
        """<p>Creates a new group.</p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the group. </p>
            sam_account_name: <p> The name of the group. </p>
            group_type: <p> The AD group type. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work">Active Directory security group type</a>.</p>
            group_scope: <p> The scope of the AD group. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope">Active Directory security group scope</a>. </p>
            other_attributes: <p> An expression that defines one or more attributes with the data type and value of each attribute. </p>
            client_token: <p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.conflict_exception.ConflictException: <p> This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.</p> <p> This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a group
            The following command creates a distribution list group named AcctngMail.

            >>> client.create_group(client_token='550e8400-e29b-41d4-a716-446655440000', directory_id='d-12233abcde', group_scope='DomainLocal', group_type='Distribution', other_attributes={'displayName': {'S': 'Acctng-mailing-list'}, 'description': {'S': 'Accounting dept mailing list'}}, sam_account_name='AcctngMail')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.create_group_request.CreateGroupRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.create_group_result.CreateGroupResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.create_group

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.create_group.create_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.create_group_request.CreateGroupRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
        }
        if group_type is not None:
            input_["group_type"] = group_type
        if group_scope is not None:
            input_["group_scope"] = group_scope
        if other_attributes is not None:
            input_["other_attributes"] = other_attributes
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

    def create_user(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.user_name.UserName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        email_address: Optional[
            "capo_directory_service_data.types.email_address.EmailAddress"
        ] = None,
        given_name: Optional[
            "capo_directory_service_data.types.given_name.GivenName"
        ] = None,
        surname: Optional["capo_directory_service_data.types.surname.Surname"] = None,
        other_attributes: Optional[
            "capo_directory_service_data.types.attributes.Attributes"
        ] = None,
        client_token: Optional[
            "capo_directory_service_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_directory_service_data.types.create_user_result.CreateUserResult":
        """<p>Creates a new user.</p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that’s associated with the user. </p>
            sam_account_name: <p> The name of the user. </p>
            email_address: <p> The email address of the user. </p>
            given_name: <p> The first name of the user. </p>
            surname: <p> The last name of the user. </p>
            other_attributes: <p> An expression that defines one or more attribute names with the data type and value of each attribute. A key is an attribute name, and the value is a list of maps. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p> <note> <p> Attribute names are case insensitive. </p> </note>
            client_token: <p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.conflict_exception.ConflictException: <p> This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.</p> <p> This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new user in the directory
            The following command

            >>> client.create_user(client_token='550e8400-e29b-41d4-a716-446655440000', directory_id='d-12233abcde', email_address='pcandella@exampledomain.com', given_name='Pat Candella', other_attributes={'department': {'S': 'HR'}, 'homePhone': {'S': '212-555-0100'}}, sam_account_name='pcandella', surname='Candella')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.create_user_result.CreateUserResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.create_user

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.create_user_request.CreateUserRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
        }
        if email_address is not None:
            input_["email_address"] = email_address
        if given_name is not None:
            input_["given_name"] = given_name
        if surname is not None:
            input_["surname"] = surname
        if other_attributes is not None:
            input_["other_attributes"] = other_attributes
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

    def delete_group(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.group_name.GroupName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        client_token: Optional[
            "capo_directory_service_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_directory_service_data.types.delete_group_result.DeleteGroupResult":
        """<p>Deletes a group.</p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the group. </p>
            sam_account_name: <p> The name of the group. </p>
            client_token: <p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.conflict_exception.ConflictException: <p> This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.</p> <p> This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a group
            The following command deletes the marketing group from the specified directory.

            >>> client.delete_group(client_token='550e8400-e29b-41d4-a716-446655440000', directory_id='d-12233abcde', sam_account_name='marketing')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.delete_group_request.DeleteGroupRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.delete_group_result.DeleteGroupResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.delete_group

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.delete_group.delete_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.delete_group_request.DeleteGroupRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
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

    def delete_user(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.user_name.UserName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        client_token: Optional[
            "capo_directory_service_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_directory_service_data.types.delete_user_result.DeleteUserResult":
        """<p>Deletes a user.</p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the user. </p>
            sam_account_name: <p> The name of the user. </p>
            client_token: <p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.conflict_exception.ConflictException: <p> This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.</p> <p> This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a user
            The following command deletes a group from the directory.

            >>> client.delete_user(client_token='550e8400-e29b-41d4-a716-446655440000', directory_id='d-12233abcde', sam_account_name='pcandella')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.delete_user_result.DeleteUserResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.delete_user

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.delete_user_request.DeleteUserRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
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

    def describe_group(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.group_name.GroupName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        other_attributes: Optional[
            "capo_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList"
        ] = None,
    ) -> "capo_directory_service_data.types.describe_group_result.DescribeGroupResult":
        """<p>Returns information about a specific group.</p>

        Args:
            directory_id: <p>The Identifier (ID) of the directory associated with the group.</p>
            realm: <p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive. </p> </note>
            sam_account_name: <p> The name of the group. </p>
            other_attributes: <p> One or more attributes to be returned for the group. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To return the attributes of a group
            The following command returns the mapped attributes for a group along with the display name, description, and GUID for the group.

            >>> client.describe_group(directory_id='d-12233abcde', other_attributes=['displayName', 'description', 'objectGUID'], realm='example.domain.com', sam_account_name='DevOpsMail')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.describe_group_request.DescribeGroupRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.describe_group_result.DescribeGroupResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.describe_group

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.describe_group.describe_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.describe_group_request.DescribeGroupRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
        }
        if realm is not None:
            input_["realm"] = realm
        if other_attributes is not None:
            input_["other_attributes"] = other_attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_user(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.user_name.UserName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        other_attributes: Optional[
            "capo_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList"
        ] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
    ) -> "capo_directory_service_data.types.describe_user_result.DescribeUserResult":
        """<p>Returns information about a specific user.</p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the user. </p>
            sam_account_name: <p> The name of the user. </p>
            other_attributes: <p> One or more attribute names to be returned for the user. A key is an attribute name, and the value is a list of maps. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p>
            realm: <p> The domain name that's associated with the user. </p> <note> <p> This parameter is optional, so you can return users outside your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD users are returned. </p> <p> This value is case insensitive. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To return the attributes of a user
            The following command returns the mapped attributes for a user along with the department, manager, IP phone, and date the user last set a password.

            >>> client.describe_user(directory_id='d-12233abcde', other_attributes=['department', 'manager', 'ipPhone', 'pwdLastSet'], realm='examplecorp.com', sam_account_name='twhitlock')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.describe_user_request.DescribeUserRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.describe_user_result.DescribeUserResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.describe_user

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.describe_user.describe_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.describe_user_request.DescribeUserRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
        }
        if other_attributes is not None:
            input_["other_attributes"] = other_attributes
        if realm is not None:
            input_["realm"] = realm

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_user(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.user_name.UserName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        client_token: Optional[
            "capo_directory_service_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_directory_service_data.types.disable_user_result.DisableUserResult":
        """<p> Deactivates an active user account. For information about how to enable an inactive user account, see <a href="https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html">ResetUserPassword</a> in the <i>Directory Service API Reference</i>.</p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the user. </p>
            sam_account_name: <p> The name of the user. </p>
            client_token: <p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.conflict_exception.ConflictException: <p> This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.</p> <p> This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disable a user account
            The following command disables the account for twhitlock.

            >>> client.disable_user(client_token='550e8400-e29b-41d4-a716-446655440000', directory_id='d-12233abcde', sam_account_name='twhitlock')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.disable_user_request.DisableUserRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.disable_user_result.DisableUserResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.disable_user

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.disable_user.disable_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.disable_user_request.DisableUserRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
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

    def list_group_members(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.group_name.GroupName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        member_realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_directory_service_data.types.list_group_members_result.ListGroupMembersResult":
        """<p> Returns member information for the specified group. </p> <p> This operation supports pagination with the use of the <code>NextToken</code> request and response parameters. If more results are available, the <code>ListGroupMembers.NextToken</code> member contains a token that you pass in the next call to <code>ListGroupMembers</code>. This retrieves the next set of items. </p> <p> You can also specify a maximum number of return results with the <code>MaxResults</code> parameter. </p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the group. </p>
            realm: <p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return members from a group outside of your Managed Microsoft AD domain. When no value is defined, only members of your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive. </p> </note>
            member_realm: <p> The domain name that's associated with the group member. This parameter defaults to the Managed Microsoft AD domain. </p> <note> <p> This parameter is optional and case insensitive. </p> </note>
            sam_account_name: <p> The name of the group. </p>
            next_token: <p>An encoded paging token for paginated calls that can be passed back to retrieve the next page.</p>
            max_results: <p> The maximum number of results to be returned per request. </p>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list members of a group
            The following command lists Marketing users in the trusted domain example.local.

            >>> client.list_group_members(directory_id='d-12233abcde', sam_account_name='marketing', member_realm='example.local', realm='examplecorp.com')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.list_group_members_request.ListGroupMembersRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.list_group_members_result.ListGroupMembersResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.list_group_members

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.list_group_members.list_group_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.list_group_members_request.ListGroupMembersRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
        }
        if realm is not None:
            input_["realm"] = realm
        if member_realm is not None:
            input_["member_realm"] = member_realm
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

    def iter_list_group_members(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.group_name.GroupName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        member_realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_directory_service_data.types.member.Member]":
        _token = next_token
        while True:
            _response = self.list_group_members(
                directory_id,
                sam_account_name,
                config_overrides=config_overrides,
                realm=realm,
                member_realm=member_realm,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_groups(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_directory_service_data.types.list_groups_result.ListGroupsResult":
        """<p> Returns group information for the specified directory. </p> <p> This operation supports pagination with the use of the <code>NextToken</code> request and response parameters. If more results are available, the <code>ListGroups.NextToken</code> member contains a token that you pass in the next call to <code>ListGroups</code>. This retrieves the next set of items. </p> <p> You can also specify a maximum number of return results with the <code>MaxResults</code> parameter. </p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the group. </p>
            realm: <p> The domain name associated with the directory. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive. </p> </note>
            next_token: <p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>
            max_results: <p> The maximum number of results to be returned per request. </p>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list domain groups
            The following command lists the name and default attributes for groups on the examplecorp.com domain.

            >>> client.list_groups(directory_id='d-12233abcde', max_results=123, next_token='123456', realm='examplecorp.com')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.list_groups_request.ListGroupsRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.list_groups_result.ListGroupsResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.list_groups

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.list_groups.list_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.list_groups_request.ListGroupsRequest = {
            "directory_id": directory_id
        }
        if realm is not None:
            input_["realm"] = realm
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

    def iter_list_groups(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_directory_service_data.types.group_summary.GroupSummary]":
        _token = next_token
        while True:
            _response = self.list_groups(
                directory_id,
                config_overrides=config_overrides,
                realm=realm,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_groups_for_member(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.member_name.MemberName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        member_realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_directory_service_data.types.list_groups_for_member_result.ListGroupsForMemberResult":
        """<p> Returns group information for the specified member. </p> <p> This operation supports pagination with the use of the <code>NextToken</code> request and response parameters. If more results are available, the <code>ListGroupsForMember.NextToken</code> member contains a token that you pass in the next call to <code>ListGroupsForMember</code>. This retrieves the next set of items. </p> <p> You can also specify a maximum number of return results with the <code>MaxResults</code> parameter. </p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the member. </p>
            realm: <p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive and defaults to your Managed Microsoft AD domain. </p> </note>
            member_realm: <p> The domain name that's associated with the group member. </p> <note> <p> This parameter is optional, so you can limit your results to the group members in a specific domain. </p> <p> This parameter is case insensitive and defaults to <code>Realm</code> </p> </note>
            sam_account_name: <p> The <code>SAMAccountName</code> of the user, group, or computer that's a member of the group. </p>
            next_token: <p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>
            max_results: <p> The maximum number of results to be returned per request. </p>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list groups for a member
            The following command

            >>> client.list_groups_for_member(directory_id='d-12233abcde', sam_account_name='twhitlock', member_realm='example.local', realm='examplecorp.com')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.list_groups_for_member_request.ListGroupsForMemberRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.list_groups_for_member_result.ListGroupsForMemberResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.list_groups_for_member

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.list_groups_for_member.list_groups_for_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.list_groups_for_member_request.ListGroupsForMemberRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
        }
        if realm is not None:
            input_["realm"] = realm
        if member_realm is not None:
            input_["member_realm"] = member_realm
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

    def iter_list_groups_for_member(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.member_name.MemberName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        member_realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_directory_service_data.types.group_summary.GroupSummary]":
        _token = next_token
        while True:
            _response = self.list_groups_for_member(
                directory_id,
                sam_account_name,
                config_overrides=config_overrides,
                realm=realm,
                member_realm=member_realm,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_users(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_directory_service_data.types.list_users_result.ListUsersResult":
        """<p> Returns user information for the specified directory. </p> <p> This operation supports pagination with the use of the <code>NextToken</code> request and response parameters. If more results are available, the <code>ListUsers.NextToken</code> member contains a token that you pass in the next call to <code>ListUsers</code>. This retrieves the next set of items. </p> <p> You can also specify a maximum number of return results with the <code>MaxResults</code> parameter. </p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the user. </p>
            realm: <p> The domain name that's associated with the user. </p> <note> <p> This parameter is optional, so you can return users outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD users are returned. </p> <p> This value is case insensitive. </p> </note>
            next_token: <p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>
            max_results: <p> The maximum number of results to be returned per request. </p>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list users in a realm
            The following command lists users on the examplecorp.com domain.

            >>> client.list_users(directory_id='d-12233abcde', realm='examplecorp.com')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.list_users_result.ListUsersResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.list_users

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.list_users.list_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.list_users_request.ListUsersRequest = {
            "directory_id": directory_id
        }
        if realm is not None:
            input_["realm"] = realm
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

    def iter_list_users(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_directory_service_data.types.user_summary.UserSummary]":
        _token = next_token
        while True:
            _response = self.list_users(
                directory_id,
                config_overrides=config_overrides,
                realm=realm,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def remove_group_member(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        group_name: "capo_directory_service_data.types.group_name.GroupName",
        member_name: "capo_directory_service_data.types.member_name.MemberName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        member_realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        client_token: Optional[
            "capo_directory_service_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_directory_service_data.types.remove_group_member_result.RemoveGroupMemberResult":
        """<p> Removes a member from a group. </p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the member. </p>
            group_name: <p> The name of the group. </p>
            member_name: <p> The <code>SAMAccountName</code> of the user, group, or computer to remove from the group. </p>
            member_realm: <p> The domain name that's associated with the group member. This parameter defaults to the Managed Microsoft AD domain. </p> <note> <p> This parameter is optional and case insensitive. </p> </note>
            client_token: <p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.conflict_exception.ConflictException: <p> This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.</p> <p> This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove a member from a group
            The following command removes the specified member from the example.local domain.

            >>> client.remove_group_member(client_token='550e8400-e29b-41d4-a716-446655440000', directory_id='d-12233abcde', group_name='DevOps', member_name='Pat Candella', member_realm='example.local')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.remove_group_member_request.RemoveGroupMemberRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.remove_group_member_result.RemoveGroupMemberResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.remove_group_member

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.remove_group_member.remove_group_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.remove_group_member_request.RemoveGroupMemberRequest = {
            "directory_id": directory_id,
            "group_name": group_name,
            "member_name": member_name,
        }
        if member_realm is not None:
            input_["member_realm"] = member_realm
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

    def search_groups(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        search_string: "capo_directory_service_data.types.search_string.SearchString",
        search_attributes: "capo_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_directory_service_data.types.search_groups_result.SearchGroupsResult":
        """<p> Searches the specified directory for a group. You can find groups that match the <code>SearchString</code> parameter with the value of their attributes included in the <code>SearchString</code> parameter. </p> <p> This operation supports pagination with the use of the <code>NextToken</code> request and response parameters. If more results are available, the <code>SearchGroups.NextToken</code> member contains a token that you pass in the next call to <code>SearchGroups</code>. This retrieves the next set of items. </p> <p> You can also specify a maximum number of return results with the <code>MaxResults</code> parameter. </p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the group. </p>
            search_string: <p> The attribute value that you want to search for. </p> <note> <p> Wildcard <code>(*)</code> searches aren't supported. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p> </note>
            search_attributes: <p> One or more data attributes that are used to search for a group. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p>
            realm: <p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive. </p> </note>
            next_token: <p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>
            max_results: <p> The maximum number of results to be returned per request. </p>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To search for groups
            The following command searches the examplecorp.com domain for groups with the GroupType security.

            >>> client.search_groups(directory_id='d-12233abcde', max_results=123, next_token='123456', realm='examplecorp.com', search_attributes=['GroupScope'], search_string='Security')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.search_groups_request.SearchGroupsRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.search_groups_result.SearchGroupsResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.search_groups

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.search_groups.search_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.search_groups_request.SearchGroupsRequest = {
            "directory_id": directory_id,
            "search_string": search_string,
            "search_attributes": search_attributes,
        }
        if realm is not None:
            input_["realm"] = realm
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

    def iter_search_groups(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        search_string: "capo_directory_service_data.types.search_string.SearchString",
        search_attributes: "capo_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_directory_service_data.types.group.Group]":
        _token = next_token
        while True:
            _response = self.search_groups(
                directory_id,
                search_string,
                search_attributes,
                config_overrides=config_overrides,
                realm=realm,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_users(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        search_string: "capo_directory_service_data.types.search_string.SearchString",
        search_attributes: "capo_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_directory_service_data.types.search_users_result.SearchUsersResult":
        """<p> Searches the specified directory for a user. You can find users that match the <code>SearchString</code> parameter with the value of their attributes included in the <code>SearchString</code> parameter.</p> <p> This operation supports pagination with the use of the <code>NextToken</code> request and response parameters. If more results are available, the <code>SearchUsers.NextToken</code> member contains a token that you pass in the next call to <code>SearchUsers</code>. This retrieves the next set of items. </p> <p> You can also specify a maximum number of return results with the <code>MaxResults</code> parameter. </p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the user. </p>
            realm: <p> The domain name that's associated with the user. </p> <note> <p> This parameter is optional, so you can return users outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD users are returned. </p> <p> This value is case insensitive. </p> </note>
            search_string: <p> The attribute value that you want to search for. </p> <note> <p> Wildcard <code>(*)</code> searches aren't supported. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p> </note>
            search_attributes: <p> One or more data attributes that are used to search for a user. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p>
            next_token: <p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>
            max_results: <p> The maximum number of results to be returned per request. </p>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To search for users
            The following command searches for users in the domain based on the SearchAttributes.

            >>> client.search_users(directory_id='d-12233abcde', realm='examplecorp.com', search_attributes=['department'], search_string='DevOps')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.search_users_request.SearchUsersRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.search_users_result.SearchUsersResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.search_users

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.search_users.search_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.search_users_request.SearchUsersRequest = {
            "directory_id": directory_id,
            "search_string": search_string,
            "search_attributes": search_attributes,
        }
        if realm is not None:
            input_["realm"] = realm
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

    def iter_search_users(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        search_string: "capo_directory_service_data.types.search_string.SearchString",
        search_attributes: "capo_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        realm: Optional["capo_directory_service_data.types.realm.Realm"] = None,
        next_token: Optional[
            "capo_directory_service_data.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_directory_service_data.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_directory_service_data.types.user.User]":
        _token = next_token
        while True:
            _response = self.search_users(
                directory_id,
                search_string,
                search_attributes,
                config_overrides=config_overrides,
                realm=realm,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_group(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.group_name.GroupName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        group_type: Optional[
            "capo_directory_service_data.types.group_type.GroupType"
        ] = None,
        group_scope: Optional[
            "capo_directory_service_data.types.group_scope.GroupScope"
        ] = None,
        other_attributes: Optional[
            "capo_directory_service_data.types.attributes.Attributes"
        ] = None,
        update_type: Optional[
            "capo_directory_service_data.types.update_type.UpdateType"
        ] = None,
        client_token: Optional[
            "capo_directory_service_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_directory_service_data.types.update_group_result.UpdateGroupResult":
        """<p> Updates group information. </p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the group. </p>
            sam_account_name: <p> The name of the group. </p>
            group_type: <p> The AD group type. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work">Active Directory security group type</a>. </p>
            group_scope: <p> The scope of the AD group. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope">Active Directory security groups</a>. </p>
            other_attributes: <p> An expression that defines one or more attributes with the data type and the value of each attribute. </p>
            update_type: <p> The type of update to be performed. If no value exists for the attribute, use <code>ADD</code>. Otherwise, use <code>REPLACE</code> to change an attribute value or <code>REMOVE</code> to clear the attribute value. </p>
            client_token: <p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.conflict_exception.ConflictException: <p> This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.</p> <p> This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a group
            The following command updates the preferred language and country attributes for the GuestsLocal group.

            >>> client.update_group(client_token='550e8400-e29b-41d4-a716-446655440000', directory_id='d-12233abcde', group_scope='Global', group_type='Security', other_attributes={'preferredLanguage': {'S': 'English'}, 'co': {'S': 'US'}}, sam_account_name='GuestsLocal', update_type='REPLACE')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.update_group_request.UpdateGroupRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.update_group_result.UpdateGroupResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.update_group

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.update_group.update_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.update_group_request.UpdateGroupRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
        }
        if group_type is not None:
            input_["group_type"] = group_type
        if group_scope is not None:
            input_["group_scope"] = group_scope
        if other_attributes is not None:
            input_["other_attributes"] = other_attributes
        if update_type is not None:
            input_["update_type"] = update_type
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

    def update_user(
        self,
        directory_id: "capo_directory_service_data.types.directory_id.DirectoryId",
        sam_account_name: "capo_directory_service_data.types.user_name.UserName",
        *,
        config_overrides: Optional[DirectoryServiceDataClientConfig] = None,
        email_address: Optional[
            "capo_directory_service_data.types.email_address.EmailAddress"
        ] = None,
        given_name: Optional[
            "capo_directory_service_data.types.given_name.GivenName"
        ] = None,
        surname: Optional["capo_directory_service_data.types.surname.Surname"] = None,
        other_attributes: Optional[
            "capo_directory_service_data.types.attributes.Attributes"
        ] = None,
        update_type: Optional[
            "capo_directory_service_data.types.update_type.UpdateType"
        ] = None,
        client_token: Optional[
            "capo_directory_service_data.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_directory_service_data.types.update_user_result.UpdateUserResult":
        """<p> Updates user information. </p>

        Args:
            directory_id: <p> The identifier (ID) of the directory that's associated with the user. </p>
            sam_account_name: <p> The name of the user. </p>
            email_address: <p> The email address of the user. </p>
            given_name: <p> The first name of the user. </p>
            surname: <p> The last name of the user. </p>
            other_attributes: <p> An expression that defines one or more attribute names with the data type and value of each attribute. A key is an attribute name, and the value is a list of maps. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p> <note> <p> Attribute names are case insensitive. </p> </note>
            update_type: <p> The type of update to be performed. If no value exists for the attribute, use <code>ADD</code>. Otherwise, use <code>REPLACE</code> to change an attribute value or <code>REMOVE</code> to clear the attribute value. </p>
            client_token: <p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>

        Raises:
            capo_directory_service_data.errors.access_denied_exception.AccessDeniedException: <p> You don't have permission to perform the request or access the directory. It can also occur when the <code>DirectoryId</code> doesn't exist or the user, member, or group might be outside of your organizational unit (OU). </p> <p> Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU. </p>
            capo_directory_service_data.errors.conflict_exception.ConflictException: <p> This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.</p> <p> This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request. </p>
            capo_directory_service_data.errors.directory_unavailable_exception.DirectoryUnavailableException: <p> The request could not be completed due to a problem in the configuration or current state of the specified directory. </p>
            capo_directory_service_data.errors.internal_server_exception.InternalServerException: <p> The operation didn't succeed because an internal error occurred. Try again later. </p>
            capo_directory_service_data.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource couldn't be found. </p>
            capo_directory_service_data.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second has been exceeded. </p>
            capo_directory_service_data.errors.validation_exception.ValidationException: <p> The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request. </p>
            capo_directory_service_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update user attributes
            The following command

            >>> client.update_user(client_token='550e8400-e29b-41d4-a716-446655440000', directory_id='d-12233abcde', email_address='twhitlock@examplecorp.com', given_name='Terry', other_attributes={'telephoneNumber': {'S': '212-555-1111'}, 'homePhone': {'S': '333-333-3333'}, 'physicalDeliveryOfficeName': {'S': 'Example Company'}, 'streetAddress': {'S': '123 Any Street'}, 'postalCode': {'S': '54321'}, 'st': {'S': 'WA'}, 'co': {'S': 'US'}}, sam_account_name='twhitlock', surname='Whitlock', update_type='ADD')
        """

        def _handler(
            req: "OperationRequest[capo_directory_service_data.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "capo_directory_service_data.types.update_user_result.UpdateUserResult"
        ]:
            import capo_directory_service_data._operations.directory_service_data.update_user

            output, http_response = (
                capo_directory_service_data._operations.directory_service_data.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service_data.types.update_user_request.UpdateUserRequest = {
            "directory_id": directory_id,
            "sam_account_name": sam_account_name,
        }
        if email_address is not None:
            input_["email_address"] = email_address
        if given_name is not None:
            input_["given_name"] = given_name
        if surname is not None:
            input_["surname"] = surname
        if other_attributes is not None:
            input_["other_attributes"] = other_attributes
        if update_type is not None:
            input_["update_type"] = update_type
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
