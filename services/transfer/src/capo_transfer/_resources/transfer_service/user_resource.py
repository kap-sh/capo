from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_transfer._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_transfer.types.create_user_request
    import capo_transfer.types.create_user_response
    import capo_transfer.types.delete_user_request
    import capo_transfer.types.describe_user_request
    import capo_transfer.types.describe_user_response
    import capo_transfer.types.home_directory
    import capo_transfer.types.home_directory_mappings
    import capo_transfer.types.home_directory_type
    import capo_transfer.types.list_users_request
    import capo_transfer.types.list_users_response
    import capo_transfer.types.listed_user
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.policy
    import capo_transfer.types.posix_profile
    import capo_transfer.types.role
    import capo_transfer.types.server_id
    import capo_transfer.types.ssh_public_key_body
    import capo_transfer.types.tags
    import capo_transfer.types.update_user_request
    import capo_transfer.types.update_user_response
    import capo_transfer.types.user_name
    from capo_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from capo_transfer._services.transfer import TransferClient, TransferClientConfig


class UserResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def put(
        self,
        role: "capo_transfer.types.role.Role",
        server_id: "capo_transfer.types.server_id.ServerId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        home_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        home_directory_type: Optional[
            "capo_transfer.types.home_directory_type.HomeDirectoryType"
        ] = None,
        home_directory_mappings: Optional[
            "capo_transfer.types.home_directory_mappings.HomeDirectoryMappings"
        ] = None,
        policy: Optional["capo_transfer.types.policy.Policy"] = None,
        posix_profile: Optional[
            "capo_transfer.types.posix_profile.PosixProfile"
        ] = None,
        ssh_public_key_body: Optional[
            "capo_transfer.types.ssh_public_key_body.SshPublicKeyBody"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
    ) -> "capo_transfer.types.create_user_response.CreateUserResponse":
        """<p>Creates a user and associates them with an existing file transfer protocol-enabled server. You can only create and associate users with servers that have the <code>IdentityProviderType</code> set to <code>SERVICE_MANAGED</code>. Using parameters for <code>CreateUser</code>, you can specify the user name, set the home directory, store the user's public key, and assign the user's Identity and Access Management (IAM) role. You can also optionally add a session policy, and assign metadata with tags that can be used to group and search for users.</p>

        Args:
            home_directory: <p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>
            home_directory_type: <p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>
            home_directory_mappings: <p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock your user down to the designated home directory ("<code>chroot</code>"). To do this, you can set <code>Entry</code> to <code>/</code> and set <code>Target</code> to the value the user should see for their home directory when they log in.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]</code> </p>
            policy: <p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html">Example session policy</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html">AssumeRole</a> in the <i>Amazon Web Services Security Token Service API Reference</i>.</p> </note>
            posix_profile: <p>Specifies the full POSIX identity, including user ID (<code>Uid</code>), group ID (<code>Gid</code>), and any secondary groups IDs (<code>SecondaryGids</code>), that controls your users' access to your Amazon EFS file systems. The POSIX permissions that are set on files and directories in Amazon EFS determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.</p>
            role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.</p>
            ssh_public_key_body: <p>The public portion of the Secure Shell (SSH) key used to authenticate the user to the server.</p> <p>The three standard SSH public key format elements are <code>&lt;key type&gt;</code>, <code>&lt;body base64&gt;</code>, and an optional <code>&lt;comment&gt;</code>, with spaces between each element.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p> <ul> <li> <p>For RSA keys, the key type is <code>ssh-rsa</code>.</p> </li> <li> <p>For ED25519 keys, the key type is <code>ssh-ed25519</code>.</p> </li> <li> <p>For ECDSA keys, the key type is either <code>ecdsa-sha2-nistp256</code>, <code>ecdsa-sha2-nistp384</code>, or <code>ecdsa-sha2-nistp521</code>, depending on the size of the key you generated.</p> </li> </ul>
            tags: <p>Key-value pairs that can be used to group and search for users. Tags are metadata attached to users for any purpose.</p>
            user_name: <p>A unique string that identifies a user and is associated with a <code>ServerId</code>. This user name must be a minimum of 3 and a maximum of 100 characters long. The following are valid characters: a-z, A-Z, 0-9, underscore '_', hyphen '-', period '.', and at sign '@'. The user name can't start with a hyphen, period, or at sign.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.create_user_response.CreateUserResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_user

            output, http_response = (
                capo_transfer._operations.transfer_service.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.create_user_request.CreateUserRequest = {
            "role": role,
            "server_id": server_id,
            "user_name": user_name,
        }
        if home_directory is not None:
            input_["home_directory"] = home_directory
        if home_directory_type is not None:
            input_["home_directory_type"] = home_directory_type
        if home_directory_mappings is not None:
            input_["home_directory_mappings"] = home_directory_mappings
        if policy is not None:
            input_["policy"] = policy
        if posix_profile is not None:
            input_["posix_profile"] = posix_profile
        if ssh_public_key_body is not None:
            input_["ssh_public_key_body"] = ssh_public_key_body
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
        server_id: "capo_transfer.types.server_id.ServerId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_user_response.DescribeUserResponse":
        """<p>Describes the user assigned to the specific file transfer protocol-enabled server, as identified by its <code>ServerId</code> property.</p> <p>The response from this call returns the properties of the user associated with the <code>ServerId</code> value that was specified.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that has this user assigned.</p>
            user_name: <p>The name of the user assigned to one or more servers. User names are part of the sign-in credentials to use the Transfer Family service and perform file transfer tasks.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.describe_user_request.DescribeUserRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.describe_user_response.DescribeUserResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_user

            output, http_response = (
                capo_transfer._operations.transfer_service.describe_user.describe_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_user_request.DescribeUserRequest = {
            "server_id": server_id,
            "user_name": user_name,
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
        server_id: "capo_transfer.types.server_id.ServerId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        home_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        home_directory_type: Optional[
            "capo_transfer.types.home_directory_type.HomeDirectoryType"
        ] = None,
        home_directory_mappings: Optional[
            "capo_transfer.types.home_directory_mappings.HomeDirectoryMappings"
        ] = None,
        policy: Optional["capo_transfer.types.policy.Policy"] = None,
        posix_profile: Optional[
            "capo_transfer.types.posix_profile.PosixProfile"
        ] = None,
        role: Optional["capo_transfer.types.role.Role"] = None,
    ) -> "capo_transfer.types.update_user_response.UpdateUserResponse":
        r"""<p>Assigns new properties to a user. Parameters you pass modify any or all of the following: the home directory, role, and policy for the <code>UserName</code> and <code>ServerId</code> you specify.</p> <p>The response returns the <code>ServerId</code> and the <code>UserName</code> for the updated user.</p> <p>In the console, you can select <i>Restricted</i> when you create or update a user. This ensures that the user can't access anything outside of their home directory. The programmatic way to configure this behavior is to update the user. Set their <code>HomeDirectoryType</code> to <code>LOGICAL</code>, and specify <code>HomeDirectoryMappings</code> with <code>Entry</code> as root (<code>/</code>) and <code>Target</code> as their home directory.</p> <p>For example, if the user's home directory is <code>/test/admin-user</code>, the following command updates the user so that their configuration in the console shows the <i>Restricted</i> flag as selected.</p> <p> <code> aws transfer update-user --server-id &lt;server-id&gt; --user-name admin-user --home-directory-type LOGICAL --home-directory-mappings "[{\"Entry\":\"/\", \"Target\":\"/test/admin-user\"}]"</code> </p>

        Args:
            home_directory: <p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>
            home_directory_type: <p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>
            home_directory_mappings: <p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock down your user to the designated home directory ("<code>chroot</code>"). To do this, you can set <code>Entry</code> to '/' and set <code>Target</code> to the HomeDirectory parameter value.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]</code> </p>
            policy: <p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/session-policy">Creating a session policy</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html">AssumeRole</a> in the <i>Amazon Web Services Security Token Service API Reference</i>.</p> </note>
            posix_profile: <p>Specifies the full POSIX identity, including user ID (<code>Uid</code>), group ID (<code>Gid</code>), and any secondary groups IDs (<code>SecondaryGids</code>), that controls your users' access to your Amazon Elastic File Systems (Amazon EFS). The POSIX permissions that are set on files and directories in your file system determines the level of access your users get when transferring files into and out of your Amazon EFS file systems.</p>
            role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>
            server_id: <p>A system-assigned unique identifier for a Transfer Family server instance that the user is assigned to.</p>
            user_name: <p>A unique string that identifies a user and is associated with a server as specified by the <code>ServerId</code>. This user name must be a minimum of 3 and a maximum of 100 characters long. The following are valid characters: a-z, A-Z, 0-9, underscore '_', hyphen '-', period '.', and at sign '@'. The user name can't start with a hyphen, period, or at sign.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.update_user_response.UpdateUserResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_user

            output, http_response = (
                capo_transfer._operations.transfer_service.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_user_request.UpdateUserRequest = {
            "server_id": server_id,
            "user_name": user_name,
        }
        if home_directory is not None:
            input_["home_directory"] = home_directory
        if home_directory_type is not None:
            input_["home_directory_type"] = home_directory_type
        if home_directory_mappings is not None:
            input_["home_directory_mappings"] = home_directory_mappings
        if policy is not None:
            input_["policy"] = policy
        if posix_profile is not None:
            input_["posix_profile"] = posix_profile
        if role is not None:
            input_["role"] = role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the user belonging to a file transfer protocol-enabled server you specify.</p> <p>No response returns from this operation.</p> <note> <p>When you delete a user from a server, the user's information is lost.</p> </note>

        Args:
            server_id: <p>A system-assigned unique identifier for a server instance that has the user assigned to it.</p>
            user_name: <p>A unique string that identifies a user that is being deleted from a server.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_user

            output, http_response = (
                capo_transfer._operations.transfer_service.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_user_request.DeleteUserRequest = {
            "server_id": server_id,
            "user_name": user_name,
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
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_users_response.ListUsersResponse":
        """<p>Lists the users for a file transfer protocol-enabled server that you specify by passing the <code>ServerId</code> parameter.</p>

        Args:
            max_results: <p>Specifies the number of users to return as a response to the <code>ListUsers</code> request.</p>
            next_token: <p>If there are additional results from the <code>ListUsers</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> to a subsequent <code>ListUsers</code> command, to continue listing additional users.</p>
            server_id: <p>A system-assigned unique identifier for a server that has users assigned to it.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.list_users_response.ListUsersResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_users

            output, http_response = (
                capo_transfer._operations.transfer_service.list_users.list_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_users_request.ListUsersRequest = {
            "server_id": server_id
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


class AsyncUserResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def put(
        self,
        role: "capo_transfer.types.role.Role",
        server_id: "capo_transfer.types.server_id.ServerId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        home_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        home_directory_type: Optional[
            "capo_transfer.types.home_directory_type.HomeDirectoryType"
        ] = None,
        home_directory_mappings: Optional[
            "capo_transfer.types.home_directory_mappings.HomeDirectoryMappings"
        ] = None,
        policy: Optional["capo_transfer.types.policy.Policy"] = None,
        posix_profile: Optional[
            "capo_transfer.types.posix_profile.PosixProfile"
        ] = None,
        ssh_public_key_body: Optional[
            "capo_transfer.types.ssh_public_key_body.SshPublicKeyBody"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
    ) -> "capo_transfer.types.create_user_response.CreateUserResponse":
        """<p>Creates a user and associates them with an existing file transfer protocol-enabled server. You can only create and associate users with servers that have the <code>IdentityProviderType</code> set to <code>SERVICE_MANAGED</code>. Using parameters for <code>CreateUser</code>, you can specify the user name, set the home directory, store the user's public key, and assign the user's Identity and Access Management (IAM) role. You can also optionally add a session policy, and assign metadata with tags that can be used to group and search for users.</p>

        Args:
            home_directory: <p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>
            home_directory_type: <p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>
            home_directory_mappings: <p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock your user down to the designated home directory ("<code>chroot</code>"). To do this, you can set <code>Entry</code> to <code>/</code> and set <code>Target</code> to the value the user should see for their home directory when they log in.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]</code> </p>
            policy: <p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html">Example session policy</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html">AssumeRole</a> in the <i>Amazon Web Services Security Token Service API Reference</i>.</p> </note>
            posix_profile: <p>Specifies the full POSIX identity, including user ID (<code>Uid</code>), group ID (<code>Gid</code>), and any secondary groups IDs (<code>SecondaryGids</code>), that controls your users' access to your Amazon EFS file systems. The POSIX permissions that are set on files and directories in Amazon EFS determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.</p>
            role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.</p>
            ssh_public_key_body: <p>The public portion of the Secure Shell (SSH) key used to authenticate the user to the server.</p> <p>The three standard SSH public key format elements are <code>&lt;key type&gt;</code>, <code>&lt;body base64&gt;</code>, and an optional <code>&lt;comment&gt;</code>, with spaces between each element.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p> <ul> <li> <p>For RSA keys, the key type is <code>ssh-rsa</code>.</p> </li> <li> <p>For ED25519 keys, the key type is <code>ssh-ed25519</code>.</p> </li> <li> <p>For ECDSA keys, the key type is either <code>ecdsa-sha2-nistp256</code>, <code>ecdsa-sha2-nistp384</code>, or <code>ecdsa-sha2-nistp521</code>, depending on the size of the key you generated.</p> </li> </ul>
            tags: <p>Key-value pairs that can be used to group and search for users. Tags are metadata attached to users for any purpose.</p>
            user_name: <p>A unique string that identifies a user and is associated with a <code>ServerId</code>. This user name must be a minimum of 3 and a maximum of 100 characters long. The following are valid characters: a-z, A-Z, 0-9, underscore '_', hyphen '-', period '.', and at sign '@'. The user name can't start with a hyphen, period, or at sign.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_user_request.CreateUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_user_response.CreateUserResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_user

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_user.async_create_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.create_user_request.CreateUserRequest = {
            "role": role,
            "server_id": server_id,
            "user_name": user_name,
        }
        if home_directory is not None:
            input_["home_directory"] = home_directory
        if home_directory_type is not None:
            input_["home_directory_type"] = home_directory_type
        if home_directory_mappings is not None:
            input_["home_directory_mappings"] = home_directory_mappings
        if policy is not None:
            input_["policy"] = policy
        if posix_profile is not None:
            input_["posix_profile"] = posix_profile
        if ssh_public_key_body is not None:
            input_["ssh_public_key_body"] = ssh_public_key_body
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
        server_id: "capo_transfer.types.server_id.ServerId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_user_response.DescribeUserResponse":
        """<p>Describes the user assigned to the specific file transfer protocol-enabled server, as identified by its <code>ServerId</code> property.</p> <p>The response from this call returns the properties of the user associated with the <code>ServerId</code> value that was specified.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that has this user assigned.</p>
            user_name: <p>The name of the user assigned to one or more servers. User names are part of the sign-in credentials to use the Transfer Family service and perform file transfer tasks.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_user_request.DescribeUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_user_response.DescribeUserResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_user

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_user.async_describe_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_user_request.DescribeUserRequest = {
            "server_id": server_id,
            "user_name": user_name,
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
        server_id: "capo_transfer.types.server_id.ServerId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        home_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        home_directory_type: Optional[
            "capo_transfer.types.home_directory_type.HomeDirectoryType"
        ] = None,
        home_directory_mappings: Optional[
            "capo_transfer.types.home_directory_mappings.HomeDirectoryMappings"
        ] = None,
        policy: Optional["capo_transfer.types.policy.Policy"] = None,
        posix_profile: Optional[
            "capo_transfer.types.posix_profile.PosixProfile"
        ] = None,
        role: Optional["capo_transfer.types.role.Role"] = None,
    ) -> "capo_transfer.types.update_user_response.UpdateUserResponse":
        r"""<p>Assigns new properties to a user. Parameters you pass modify any or all of the following: the home directory, role, and policy for the <code>UserName</code> and <code>ServerId</code> you specify.</p> <p>The response returns the <code>ServerId</code> and the <code>UserName</code> for the updated user.</p> <p>In the console, you can select <i>Restricted</i> when you create or update a user. This ensures that the user can't access anything outside of their home directory. The programmatic way to configure this behavior is to update the user. Set their <code>HomeDirectoryType</code> to <code>LOGICAL</code>, and specify <code>HomeDirectoryMappings</code> with <code>Entry</code> as root (<code>/</code>) and <code>Target</code> as their home directory.</p> <p>For example, if the user's home directory is <code>/test/admin-user</code>, the following command updates the user so that their configuration in the console shows the <i>Restricted</i> flag as selected.</p> <p> <code> aws transfer update-user --server-id &lt;server-id&gt; --user-name admin-user --home-directory-type LOGICAL --home-directory-mappings "[{\"Entry\":\"/\", \"Target\":\"/test/admin-user\"}]"</code> </p>

        Args:
            home_directory: <p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>
            home_directory_type: <p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>
            home_directory_mappings: <p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock down your user to the designated home directory ("<code>chroot</code>"). To do this, you can set <code>Entry</code> to '/' and set <code>Target</code> to the HomeDirectory parameter value.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]</code> </p>
            policy: <p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/session-policy">Creating a session policy</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html">AssumeRole</a> in the <i>Amazon Web Services Security Token Service API Reference</i>.</p> </note>
            posix_profile: <p>Specifies the full POSIX identity, including user ID (<code>Uid</code>), group ID (<code>Gid</code>), and any secondary groups IDs (<code>SecondaryGids</code>), that controls your users' access to your Amazon Elastic File Systems (Amazon EFS). The POSIX permissions that are set on files and directories in your file system determines the level of access your users get when transferring files into and out of your Amazon EFS file systems.</p>
            role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>
            server_id: <p>A system-assigned unique identifier for a Transfer Family server instance that the user is assigned to.</p>
            user_name: <p>A unique string that identifies a user and is associated with a server as specified by the <code>ServerId</code>. This user name must be a minimum of 3 and a maximum of 100 characters long. The following are valid characters: a-z, A-Z, 0-9, underscore '_', hyphen '-', period '.', and at sign '@'. The user name can't start with a hyphen, period, or at sign.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_user_request.UpdateUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_user_response.UpdateUserResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_user

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_user.async_update_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_user_request.UpdateUserRequest = {
            "server_id": server_id,
            "user_name": user_name,
        }
        if home_directory is not None:
            input_["home_directory"] = home_directory
        if home_directory_type is not None:
            input_["home_directory_type"] = home_directory_type
        if home_directory_mappings is not None:
            input_["home_directory_mappings"] = home_directory_mappings
        if policy is not None:
            input_["policy"] = policy
        if posix_profile is not None:
            input_["posix_profile"] = posix_profile
        if role is not None:
            input_["role"] = role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the user belonging to a file transfer protocol-enabled server you specify.</p> <p>No response returns from this operation.</p> <note> <p>When you delete a user from a server, the user's information is lost.</p> </note>

        Args:
            server_id: <p>A system-assigned unique identifier for a server instance that has the user assigned to it.</p>
            user_name: <p>A unique string that identifies a user that is being deleted from a server.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_user_request.DeleteUserRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_user

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_user.async_delete_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_user_request.DeleteUserRequest = {
            "server_id": server_id,
            "user_name": user_name,
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
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_users_response.ListUsersResponse":
        """<p>Lists the users for a file transfer protocol-enabled server that you specify by passing the <code>ServerId</code> parameter.</p>

        Args:
            max_results: <p>Specifies the number of users to return as a response to the <code>ListUsers</code> request.</p>
            next_token: <p>If there are additional results from the <code>ListUsers</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> to a subsequent <code>ListUsers</code> command, to continue listing additional users.</p>
            server_id: <p>A system-assigned unique identifier for a server that has users assigned to it.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_users_request.ListUsersRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_users_response.ListUsersResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_users

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_users.async_list_users(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_users_request.ListUsersRequest = {
            "server_id": server_id
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
