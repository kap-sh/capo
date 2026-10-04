"""Generated from Smithy shape ``com.amazonaws.transfer#TransferService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_transfer._auth._signers
import capo_transfer._auth._sigv4
from capo_transfer._auth._identity import Credentials
from capo_transfer._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_transfer._auth._zapros_handler import AuthMiddleware
from capo_transfer._pagination import resolve_path as _resolve_path
from capo_transfer._resources.transfer_service.agreement_resource import (
    AsyncAgreementResource,
)
from capo_transfer._resources.transfer_service.certificate_resource import (
    AsyncCertificateResource,
)
from capo_transfer._resources.transfer_service.connector_resource import (
    AsyncConnectorResource,
)
from capo_transfer._resources.transfer_service.profile_resource import (
    AsyncProfileResource,
)
from capo_transfer._resources.transfer_service.server_resource import (
    AsyncServerResource,
)
from capo_transfer._resources.transfer_service.user_resource import AsyncUserResource
from capo_transfer._resources.transfer_service.web_app_customization_resource import (
    AsyncWebAppCustomizationResource,
)
from capo_transfer._resources.transfer_service.web_app_resource import (
    AsyncWebAppResource,
)
from capo_transfer._resources.transfer_service.workflow_resource import (
    AsyncWorkflowResource,
)
from capo_transfer._services._aws_config import aaws_config
from capo_transfer._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_transfer.types.agreement_id
    import capo_transfer.types.agreement_status_type
    import capo_transfer.types.arn
    import capo_transfer.types.as2_connector_config
    import capo_transfer.types.as2_id
    import capo_transfer.types.callback_token
    import capo_transfer.types.cert_date
    import capo_transfer.types.certificate
    import capo_transfer.types.certificate_body_type
    import capo_transfer.types.certificate_chain_type
    import capo_transfer.types.certificate_id
    import capo_transfer.types.certificate_ids
    import capo_transfer.types.certificate_usage_type
    import capo_transfer.types.connector_egress_config
    import capo_transfer.types.connector_file_transfer_result
    import capo_transfer.types.connector_id
    import capo_transfer.types.connector_security_policy_name
    import capo_transfer.types.connectors_ip_address_type
    import capo_transfer.types.create_access_request
    import capo_transfer.types.create_access_response
    import capo_transfer.types.create_agreement_request
    import capo_transfer.types.create_agreement_response
    import capo_transfer.types.create_connector_request
    import capo_transfer.types.create_connector_response
    import capo_transfer.types.create_profile_request
    import capo_transfer.types.create_profile_response
    import capo_transfer.types.create_server_request
    import capo_transfer.types.create_server_response
    import capo_transfer.types.create_user_request
    import capo_transfer.types.create_user_response
    import capo_transfer.types.create_web_app_request
    import capo_transfer.types.create_web_app_response
    import capo_transfer.types.create_workflow_request
    import capo_transfer.types.create_workflow_response
    import capo_transfer.types.custom_directories_type
    import capo_transfer.types.custom_http_headers
    import capo_transfer.types.custom_step_status
    import capo_transfer.types.delete_access_request
    import capo_transfer.types.delete_agreement_request
    import capo_transfer.types.delete_certificate_request
    import capo_transfer.types.delete_connector_request
    import capo_transfer.types.delete_host_key_request
    import capo_transfer.types.delete_profile_request
    import capo_transfer.types.delete_server_request
    import capo_transfer.types.delete_ssh_public_key_request
    import capo_transfer.types.delete_user_request
    import capo_transfer.types.delete_web_app_customization_request
    import capo_transfer.types.delete_web_app_request
    import capo_transfer.types.delete_workflow_request
    import capo_transfer.types.describe_access_request
    import capo_transfer.types.describe_access_response
    import capo_transfer.types.describe_agreement_request
    import capo_transfer.types.describe_agreement_response
    import capo_transfer.types.describe_certificate_request
    import capo_transfer.types.describe_certificate_response
    import capo_transfer.types.describe_connector_request
    import capo_transfer.types.describe_connector_response
    import capo_transfer.types.describe_execution_request
    import capo_transfer.types.describe_execution_response
    import capo_transfer.types.describe_host_key_request
    import capo_transfer.types.describe_host_key_response
    import capo_transfer.types.describe_profile_request
    import capo_transfer.types.describe_profile_response
    import capo_transfer.types.describe_security_policy_request
    import capo_transfer.types.describe_security_policy_response
    import capo_transfer.types.describe_server_request
    import capo_transfer.types.describe_server_response
    import capo_transfer.types.describe_user_request
    import capo_transfer.types.describe_user_response
    import capo_transfer.types.describe_web_app_customization_request
    import capo_transfer.types.describe_web_app_customization_response
    import capo_transfer.types.describe_web_app_request
    import capo_transfer.types.describe_web_app_response
    import capo_transfer.types.describe_workflow_request
    import capo_transfer.types.describe_workflow_response
    import capo_transfer.types.description
    import capo_transfer.types.domain
    import capo_transfer.types.endpoint_details
    import capo_transfer.types.endpoint_type
    import capo_transfer.types.enforce_message_signing_type
    import capo_transfer.types.execution_id
    import capo_transfer.types.external_id
    import capo_transfer.types.file_path
    import capo_transfer.types.file_paths
    import capo_transfer.types.home_directory
    import capo_transfer.types.home_directory_mappings
    import capo_transfer.types.home_directory_type
    import capo_transfer.types.host_key
    import capo_transfer.types.host_key_description
    import capo_transfer.types.host_key_id
    import capo_transfer.types.identity_provider_details
    import capo_transfer.types.identity_provider_type
    import capo_transfer.types.import_certificate_request
    import capo_transfer.types.import_certificate_response
    import capo_transfer.types.import_host_key_request
    import capo_transfer.types.import_host_key_response
    import capo_transfer.types.import_ssh_public_key_request
    import capo_transfer.types.import_ssh_public_key_response
    import capo_transfer.types.ip_address_type
    import capo_transfer.types.list_accesses_request
    import capo_transfer.types.list_accesses_response
    import capo_transfer.types.list_agreements_request
    import capo_transfer.types.list_agreements_response
    import capo_transfer.types.list_certificates_request
    import capo_transfer.types.list_certificates_response
    import capo_transfer.types.list_connectors_request
    import capo_transfer.types.list_connectors_response
    import capo_transfer.types.list_executions_request
    import capo_transfer.types.list_executions_response
    import capo_transfer.types.list_file_transfer_results_request
    import capo_transfer.types.list_file_transfer_results_response
    import capo_transfer.types.list_host_keys_request
    import capo_transfer.types.list_host_keys_response
    import capo_transfer.types.list_profiles_request
    import capo_transfer.types.list_profiles_response
    import capo_transfer.types.list_security_policies_request
    import capo_transfer.types.list_security_policies_response
    import capo_transfer.types.list_servers_request
    import capo_transfer.types.list_servers_response
    import capo_transfer.types.list_tags_for_resource_request
    import capo_transfer.types.list_tags_for_resource_response
    import capo_transfer.types.list_users_request
    import capo_transfer.types.list_users_response
    import capo_transfer.types.list_web_apps_request
    import capo_transfer.types.list_web_apps_response
    import capo_transfer.types.list_workflows_request
    import capo_transfer.types.list_workflows_response
    import capo_transfer.types.listed_access
    import capo_transfer.types.listed_agreement
    import capo_transfer.types.listed_certificate
    import capo_transfer.types.listed_connector
    import capo_transfer.types.listed_execution
    import capo_transfer.types.listed_profile
    import capo_transfer.types.listed_server
    import capo_transfer.types.listed_user
    import capo_transfer.types.listed_web_app
    import capo_transfer.types.listed_workflow
    import capo_transfer.types.max_items
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.nullable_role
    import capo_transfer.types.policy
    import capo_transfer.types.posix_profile
    import capo_transfer.types.post_authentication_login_banner
    import capo_transfer.types.pre_authentication_login_banner
    import capo_transfer.types.preserve_filename_type
    import capo_transfer.types.private_key_type
    import capo_transfer.types.profile_id
    import capo_transfer.types.profile_type
    import capo_transfer.types.protocol
    import capo_transfer.types.protocol_details
    import capo_transfer.types.protocols
    import capo_transfer.types.role
    import capo_transfer.types.s3_storage_options
    import capo_transfer.types.security_policy_name
    import capo_transfer.types.send_workflow_step_state_request
    import capo_transfer.types.send_workflow_step_state_response
    import capo_transfer.types.server_id
    import capo_transfer.types.sftp_connector_config
    import capo_transfer.types.source_ip
    import capo_transfer.types.ssh_public_key_body
    import capo_transfer.types.ssh_public_key_id
    import capo_transfer.types.start_directory_listing_request
    import capo_transfer.types.start_directory_listing_response
    import capo_transfer.types.start_file_transfer_request
    import capo_transfer.types.start_file_transfer_response
    import capo_transfer.types.start_remote_delete_request
    import capo_transfer.types.start_remote_delete_response
    import capo_transfer.types.start_remote_move_request
    import capo_transfer.types.start_remote_move_response
    import capo_transfer.types.start_server_request
    import capo_transfer.types.stop_server_request
    import capo_transfer.types.structured_log_destinations
    import capo_transfer.types.tag
    import capo_transfer.types.tag_keys
    import capo_transfer.types.tag_resource_request
    import capo_transfer.types.tags
    import capo_transfer.types.test_connection_request
    import capo_transfer.types.test_connection_response
    import capo_transfer.types.test_identity_provider_request
    import capo_transfer.types.test_identity_provider_response
    import capo_transfer.types.transfer_id
    import capo_transfer.types.untag_resource_request
    import capo_transfer.types.update_access_request
    import capo_transfer.types.update_access_response
    import capo_transfer.types.update_agreement_request
    import capo_transfer.types.update_agreement_response
    import capo_transfer.types.update_certificate_request
    import capo_transfer.types.update_certificate_response
    import capo_transfer.types.update_connector_egress_config
    import capo_transfer.types.update_connector_request
    import capo_transfer.types.update_connector_response
    import capo_transfer.types.update_host_key_request
    import capo_transfer.types.update_host_key_response
    import capo_transfer.types.update_profile_request
    import capo_transfer.types.update_profile_response
    import capo_transfer.types.update_server_request
    import capo_transfer.types.update_server_response
    import capo_transfer.types.update_user_request
    import capo_transfer.types.update_user_response
    import capo_transfer.types.update_web_app_customization_request
    import capo_transfer.types.update_web_app_customization_response
    import capo_transfer.types.update_web_app_endpoint_details
    import capo_transfer.types.update_web_app_identity_provider_details
    import capo_transfer.types.update_web_app_request
    import capo_transfer.types.update_web_app_response
    import capo_transfer.types.url
    import capo_transfer.types.user_name
    import capo_transfer.types.user_password
    import capo_transfer.types.web_app_access_endpoint
    import capo_transfer.types.web_app_endpoint_details
    import capo_transfer.types.web_app_endpoint_policy
    import capo_transfer.types.web_app_favicon_file
    import capo_transfer.types.web_app_id
    import capo_transfer.types.web_app_identity_provider_details
    import capo_transfer.types.web_app_logo_file
    import capo_transfer.types.web_app_title
    import capo_transfer.types.web_app_units
    import capo_transfer.types.workflow_description
    import capo_transfer.types.workflow_details
    import capo_transfer.types.workflow_id
    import capo_transfer.types.workflow_steps


class AsyncTransferClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncTransferClient:
    """A client for the ``Transfer`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncTransferClientConfig(
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
        self.agreement_resource = AsyncAgreementResource(self)
        self.certificate_resource = AsyncCertificateResource(self)
        self.connector_resource = AsyncConnectorResource(self)
        self.profile_resource = AsyncProfileResource(self)
        self.server_resource = AsyncServerResource(self)
        self.user_resource = AsyncUserResource(self)
        self.web_app_customization_resource = AsyncWebAppCustomizationResource(self)
        self.web_app_resource = AsyncWebAppResource(self)
        self.workflow_resource = AsyncWorkflowResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncTransferClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTransferClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def create_access(
        self,
        role: "capo_transfer.types.role.Role",
        server_id: "capo_transfer.types.server_id.ServerId",
        external_id: "capo_transfer.types.external_id.ExternalId",
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
    ) -> "capo_transfer.types.create_access_response.CreateAccessResponse":
        """<p>Used by administrators to choose which groups in the directory should have access to upload and download files over the enabled protocols using Transfer Family. For example, a Microsoft Active Directory might contain 50,000 users, but only a small fraction might need the ability to transfer files to the server. An administrator can use <code>CreateAccess</code> to limit the access to the correct set of users who need this ability.</p>

        Args:
            home_directory: <p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>
            home_directory_type: <p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>
            home_directory_mappings: <p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock down your user to the designated home directory ("<code>chroot</code>"). To do this, you can set <code>Entry</code> to <code>/</code> and set <code>Target</code> to the <code>HomeDirectory</code> parameter value.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]</code> </p>
            policy: <p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html">Example session policy</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html">AssumeRole</a> in the <i>Security Token Service API Reference</i>.</p> </note>
            role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.</p>
            external_id: <p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like "<i>YourGroupName</i>*"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_access_request.CreateAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_access_response.CreateAccessResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_access

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_access.async_create_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.create_access_request.CreateAccessRequest = {
            "role": role,
            "server_id": server_id,
            "external_id": external_id,
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        external_id: "capo_transfer.types.external_id.ExternalId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Allows you to delete the access specified in the <code>ServerID</code> and <code>ExternalID</code> parameters.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that has this user assigned.</p>
            external_id: <p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like "<i>YourGroupName</i>*"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_access_request.DeleteAccessRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_access

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_access.async_delete_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_access_request.DeleteAccessRequest = {
            "server_id": server_id,
            "external_id": external_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_host_key(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        host_key_id: "capo_transfer.types.host_key_id.HostKeyId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the host key that's specified in the <code>HostKeyId</code> parameter.</p>

        Args:
            server_id: <p>The identifier of the server that contains the host key that you are deleting.</p>
            host_key_id: <p>The identifier of the host key that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_host_key_request.DeleteHostKeyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_host_key

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_host_key.async_delete_host_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_host_key_request.DeleteHostKeyRequest = {
            "server_id": server_id,
            "host_key_id": host_key_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ssh_public_key(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        ssh_public_key_id: "capo_transfer.types.ssh_public_key_id.SshPublicKeyId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes a user's Secure Shell (SSH) public key.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a file transfer protocol-enabled server instance that has the user assigned to it.</p>
            ssh_public_key_id: <p>A unique identifier used to reference your user's specific SSH key.</p>
            user_name: <p>A unique string that identifies a user whose public key is being deleted.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_ssh_public_key_request.DeleteSshPublicKeyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_ssh_public_key

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_ssh_public_key.async_delete_ssh_public_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_ssh_public_key_request.DeleteSshPublicKeyRequest = {
            "server_id": server_id,
            "ssh_public_key_id": ssh_public_key_id,
            "user_name": user_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_access(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        external_id: "capo_transfer.types.external_id.ExternalId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_access_response.DescribeAccessResponse":
        """<p>Describes the access that is assigned to the specific file transfer protocol-enabled server, as identified by its <code>ServerId</code> property and its <code>ExternalId</code>.</p> <p>The response from this call returns the properties of the access that is associated with the <code>ServerId</code> value that was specified.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that has this access assigned.</p>
            external_id: <p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like "<i>YourGroupName</i>*"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_access_request.DescribeAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_access_response.DescribeAccessResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_access

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_access.async_describe_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_access_request.DescribeAccessRequest = {
            "server_id": server_id,
            "external_id": external_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_execution(
        self,
        execution_id: "capo_transfer.types.execution_id.ExecutionId",
        workflow_id: "capo_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_execution_response.DescribeExecutionResponse":
        """<p>You can use <code>DescribeExecution</code> to check the details of the execution of the specified workflow.</p> <note> <p>This API call only returns details for in-progress workflows.</p> <p> If you provide an ID for an execution that is not in progress, or if the execution doesn't match the specified workflow ID, you receive a <code>ResourceNotFound</code> exception.</p> </note>

        Args:
            execution_id: <p>A unique identifier for the execution of a workflow.</p>
            workflow_id: <p>A unique identifier for the workflow.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_execution_request.DescribeExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_execution_response.DescribeExecutionResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_execution

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_execution.async_describe_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_execution_request.DescribeExecutionRequest = {
            "execution_id": execution_id,
            "workflow_id": workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_host_key(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        host_key_id: "capo_transfer.types.host_key_id.HostKeyId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_host_key_response.DescribeHostKeyResponse":
        """<p>Returns the details of the host key that's specified by the <code>HostKeyId</code> and <code>ServerId</code>.</p>

        Args:
            server_id: <p>The identifier of the server that contains the host key that you want described.</p>
            host_key_id: <p>The identifier of the host key that you want described.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_host_key_request.DescribeHostKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_host_key_response.DescribeHostKeyResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_host_key

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_host_key.async_describe_host_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_host_key_request.DescribeHostKeyRequest = {
            "server_id": server_id,
            "host_key_id": host_key_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_security_policy(
        self,
        security_policy_name: "capo_transfer.types.security_policy_name.SecurityPolicyName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_security_policy_response.DescribeSecurityPolicyResponse":
        """<p>Describes the security policy that is attached to your server or SFTP connector. The response contains a description of the security policy's properties. For more information about security policies, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/security-policies.html">Working with security policies for servers</a> or <a href="https://docs.aws.amazon.com/transfer/latest/userguide/security-policies-connectors.html">Working with security policies for SFTP connectors</a>.</p>

        Args:
            security_policy_name: <p>Specify the text name of the security policy for which you want the details.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_security_policy_request.DescribeSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_security_policy_response.DescribeSecurityPolicyResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_security_policy

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_security_policy.async_describe_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_security_policy_request.DescribeSecurityPolicyRequest = {
            "security_policy_name": security_policy_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_host_key(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        host_key_body: "capo_transfer.types.host_key.HostKey",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        description: Optional[
            "capo_transfer.types.host_key_description.HostKeyDescription"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
    ) -> "capo_transfer.types.import_host_key_response.ImportHostKeyResponse":
        """<p>Adds a host key to the server that's specified by the <code>ServerId</code> parameter.</p>

        Args:
            server_id: <p>The identifier of the server that contains the host key that you are importing.</p>
            host_key_body: <p>The private key portion of an SSH key pair.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p>
            description: <p>The text description that identifies this host key.</p>
            tags: <p>Key-value pairs that can be used to group and search for host keys.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.import_host_key_request.ImportHostKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.import_host_key_response.ImportHostKeyResponse"
        ]:
            import capo_transfer._operations.transfer_service.import_host_key

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.import_host_key.async_import_host_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.import_host_key_request.ImportHostKeyRequest = {
            "server_id": server_id,
            "host_key_body": host_key_body,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_ssh_public_key(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        ssh_public_key_body: "capo_transfer.types.ssh_public_key_body.SshPublicKeyBody",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> (
        "capo_transfer.types.import_ssh_public_key_response.ImportSshPublicKeyResponse"
    ):
        """<p>Adds a Secure Shell (SSH) public key to a Transfer Family user identified by a <code>UserName</code> value assigned to the specific file transfer protocol-enabled server, identified by <code>ServerId</code>.</p> <p>The response returns the <code>UserName</code> value, the <code>ServerId</code> value, and the name of the <code>SshPublicKeyId</code>.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server.</p>
            ssh_public_key_body: <p>The public key portion of an SSH key pair.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p>
            user_name: <p>The name of the Transfer Family user that is assigned to one or more servers.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.import_ssh_public_key_request.ImportSshPublicKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.import_ssh_public_key_response.ImportSshPublicKeyResponse"
        ]:
            import capo_transfer._operations.transfer_service.import_ssh_public_key

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.import_ssh_public_key.async_import_ssh_public_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.import_ssh_public_key_request.ImportSshPublicKeyRequest = {
            "server_id": server_id,
            "ssh_public_key_body": ssh_public_key_body,
            "user_name": user_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_accesses(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_accesses_response.ListAccessesResponse":
        """<p>Lists the details for all the accesses you have on your server.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListAccesses</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional accesses.</p>
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
            req: "AsyncOperationRequest[capo_transfer.types.list_accesses_request.ListAccessesRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_accesses_response.ListAccessesResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_accesses

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_accesses.async_list_accesses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_accesses_request.ListAccessesRequest = {
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

    async def iter_list_accesses(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_access.ListedAccess]":
        _token = next_token
        while True:
            _response = await self.list_accesses(
                server_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("accesses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_executions(
        self,
        workflow_id: "capo_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_executions_response.ListExecutionsResponse":
        """<p>Lists all in-progress executions for the specified workflow.</p> <note> <p>If the specified workflow ID cannot be found, <code>ListExecutions</code> returns a <code>ResourceNotFound</code> exception.</p> </note>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p> <code>ListExecutions</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional executions.</p> <p> This is useful for pagination, for instance. If you have 100 executions for a workflow, you might only want to list first 10. If so, call the API by specifying the <code>max-results</code>: </p> <p> <code>aws transfer list-executions --max-results 10</code> </p> <p> This returns details for the first 10 executions, as well as the pointer (<code>NextToken</code>) to the eleventh execution. You can now call the API again, supplying the <code>NextToken</code> value you received: </p> <p> <code>aws transfer list-executions --max-results 10 --next-token $somePointerReturnedFromPreviousListResult</code> </p> <p> This call returns the next 10 executions, the 11th through the 20th. You can then repeat the call until the details for all 100 executions have been returned. </p>
            workflow_id: <p>A unique identifier for the workflow.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_executions_request.ListExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_executions_response.ListExecutionsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_executions

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_executions.async_list_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_executions_request.ListExecutionsRequest = {
            "workflow_id": workflow_id
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

    async def iter_list_executions(
        self,
        workflow_id: "capo_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_execution.ListedExecution]":
        _token = next_token
        while True:
            _response = await self.list_executions(
                workflow_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_file_transfer_results(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        transfer_id: "capo_transfer.types.transfer_id.TransferId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
    ) -> "capo_transfer.types.list_file_transfer_results_response.ListFileTransferResultsResponse":
        """<p> Returns real-time updates and detailed information on the status of each individual file being transferred in a specific file transfer operation. You specify the file transfer by providing its <code>ConnectorId</code> and its <code>TransferId</code>.</p> <note> <p>File transfer results are available up to 7 days after an operation has been requested.</p> </note>

        Args:
            connector_id: <p>A unique identifier for a connector. This value should match the value supplied to the corresponding <code>StartFileTransfer</code> call.</p>
            transfer_id: <p>A unique identifier for a file transfer. This value should match the value supplied to the corresponding <code>StartFileTransfer</code> call.</p>
            next_token: <p>If there are more file details than returned in this call, use this value for a subsequent call to <code>ListFileTransferResults</code> to retrieve them.</p>
            max_results: <p>The maximum number of files to return in a single page. Note that currently you can specify a maximum of 10 file paths in a single <a href="https://docs.aws.amazon.com/transfer/latest/APIReference/API_StartFileTransfer.html">StartFileTransfer</a> operation. Thus, the maximum number of file transfer results that can be returned in a single page is 10. </p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_file_transfer_results_request.ListFileTransferResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_file_transfer_results_response.ListFileTransferResultsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_file_transfer_results

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_file_transfer_results.async_list_file_transfer_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_file_transfer_results_request.ListFileTransferResultsRequest = {
            "connector_id": connector_id,
            "transfer_id": transfer_id,
        }
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

    async def iter_list_file_transfer_results(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        transfer_id: "capo_transfer.types.transfer_id.TransferId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_transfer.types.connector_file_transfer_result.ConnectorFileTransferResult]":
        _token = next_token
        while True:
            _response = await self.list_file_transfer_results(
                connector_id,
                transfer_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("file_transfer_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_host_keys(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_host_keys_response.ListHostKeysResponse":
        """<p>Returns a list of host keys for the server that's specified by the <code>ServerId</code> parameter.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When there are additional results that were not returned, a <code>NextToken</code> parameter is returned. You can use that value for a subsequent call to <code>ListHostKeys</code> to continue listing results.</p>
            server_id: <p>The identifier of the server that contains the host keys that you want to view.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_host_keys_request.ListHostKeysRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_host_keys_response.ListHostKeysResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_host_keys

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_host_keys.async_list_host_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_host_keys_request.ListHostKeysRequest = {
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

    async def list_security_policies(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_security_policies_response.ListSecurityPoliciesResponse":
        """<p>Lists the security policies that are attached to your servers and SFTP connectors. For more information about security policies, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/security-policies.html">Working with security policies for servers</a> or <a href="https://docs.aws.amazon.com/transfer/latest/userguide/security-policies-connectors.html">Working with security policies for SFTP connectors</a>.</p>

        Args:
            max_results: <p>Specifies the number of security policies to return as a response to the <code>ListSecurityPolicies</code> query.</p>
            next_token: <p>When additional results are obtained from the <code>ListSecurityPolicies</code> command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional security policies.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_security_policies_request.ListSecurityPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_security_policies_response.ListSecurityPoliciesResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_security_policies

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_security_policies.async_list_security_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_security_policies_request.ListSecurityPoliciesRequest = {}
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

    async def iter_list_security_policies(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.security_policy_name.SecurityPolicyName]":
        _token = next_token
        while True:
            _response = await self.list_security_policies(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("security_policy_names",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        arn: "capo_transfer.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a user, server, or role.</p>

        Args:
            arn: <p>Requests the tags associated with a particular Amazon Resource Name (ARN). An ARN is an identifier for a specific Amazon Web Services resource, such as a server, user, or role.</p>
            max_results: <p>Specifies the number of tags to return as a response to the <code>ListTagsForResource</code> request.</p>
            next_token: <p>When you request additional results from the <code>ListTagsForResource</code> operation, a <code>NextToken</code> parameter is returned in the input. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional tags.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
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

    async def iter_list_tags_for_resource(
        self,
        arn: "capo_transfer.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def send_workflow_step_state(
        self,
        workflow_id: "capo_transfer.types.workflow_id.WorkflowId",
        execution_id: "capo_transfer.types.execution_id.ExecutionId",
        token: "capo_transfer.types.callback_token.CallbackToken",
        status: "capo_transfer.types.custom_step_status.CustomStepStatus",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.send_workflow_step_state_response.SendWorkflowStepStateResponse":
        """<p>Sends a callback for asynchronous custom steps.</p> <p> The <code>ExecutionId</code>, <code>WorkflowId</code>, and <code>Token</code> are passed to the target resource during execution of a custom step of a workflow. You must include those with their callback as well as providing a status. </p>

        Args:
            workflow_id: <p>A unique identifier for the workflow.</p>
            execution_id: <p>A unique identifier for the execution of a workflow.</p>
            token: <p>Used to distinguish between multiple callbacks for multiple Lambda steps within the same execution.</p>
            status: <p>Indicates whether the specified step succeeded or failed.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.send_workflow_step_state_request.SendWorkflowStepStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.send_workflow_step_state_response.SendWorkflowStepStateResponse"
        ]:
            import capo_transfer._operations.transfer_service.send_workflow_step_state

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.send_workflow_step_state.async_send_workflow_step_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.send_workflow_step_state_request.SendWorkflowStepStateRequest = {
            "workflow_id": workflow_id,
            "execution_id": execution_id,
            "token": token,
            "status": status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_directory_listing(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        remote_directory_path: "capo_transfer.types.file_path.FilePath",
        output_directory_path: "capo_transfer.types.file_path.FilePath",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_items: Optional["capo_transfer.types.max_items.MaxItems"] = None,
    ) -> "capo_transfer.types.start_directory_listing_response.StartDirectoryListingResponse":
        """<p>Retrieves a list of the contents of a directory from a remote SFTP server. You specify the connector ID, the output path, and the remote directory path. You can also specify the optional <code>MaxItems</code> value to control the maximum number of items that are listed from the remote directory. This API returns a list of all files and directories in the remote directory (up to the maximum value), but does not return files or folders in sub-directories. That is, it only returns a list of files and directories one-level deep.</p> <p>After you receive the listing file, you can provide the files that you want to transfer to the <code>RetrieveFilePaths</code> parameter of the <code>StartFileTransfer</code> API call.</p> <p>The naming convention for the output file is <code> <i>connector-ID</i>-<i>listing-ID</i>.json</code>. The output file contains the following information:</p> <ul> <li> <p> <code>filePath</code>: the complete path of a remote file, relative to the directory of the listing request for your SFTP connector on the remote server.</p> </li> <li> <p> <code>modifiedTimestamp</code>: the last time the file was modified, in UTC time format. This field is optional. If the remote file attributes don't contain a timestamp, it is omitted from the file listing.</p> </li> <li> <p> <code>size</code>: the size of the file, in bytes. This field is optional. If the remote file attributes don't contain a file size, it is omitted from the file listing.</p> </li> <li> <p> <code>path</code>: the complete path of a remote directory, relative to the directory of the listing request for your SFTP connector on the remote server.</p> </li> <li> <p> <code>truncated</code>: a flag indicating whether the list output contains all of the items contained in the remote directory or not. If your <code>Truncated</code> output value is true, you can increase the value provided in the optional <code>max-items</code> input attribute to be able to list more items (up to the maximum allowed list size of 200,000 items).</p> </li> </ul>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            remote_directory_path: <p>Specifies the directory on the remote SFTP server for which you want to list its contents.</p>
            max_items: <p>An optional parameter where you can specify the maximum number of file/directory names to retrieve. The default value is 1,000.</p>
            output_directory_path: <p>Specifies the path (bucket and prefix) in Amazon S3 storage to store the results of the directory listing.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.start_directory_listing_request.StartDirectoryListingRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.start_directory_listing_response.StartDirectoryListingResponse"
        ]:
            import capo_transfer._operations.transfer_service.start_directory_listing

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.start_directory_listing.async_start_directory_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.start_directory_listing_request.StartDirectoryListingRequest = {
            "connector_id": connector_id,
            "remote_directory_path": remote_directory_path,
            "output_directory_path": output_directory_path,
        }
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_file_transfer(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        send_file_paths: Optional["capo_transfer.types.file_paths.FilePaths"] = None,
        retrieve_file_paths: Optional[
            "capo_transfer.types.file_paths.FilePaths"
        ] = None,
        local_directory_path: Optional["capo_transfer.types.file_path.FilePath"] = None,
        remote_directory_path: Optional[
            "capo_transfer.types.file_path.FilePath"
        ] = None,
        custom_http_headers: Optional[
            "capo_transfer.types.custom_http_headers.CustomHttpHeaders"
        ] = None,
    ) -> "capo_transfer.types.start_file_transfer_response.StartFileTransferResponse":
        """<p>Begins a file transfer between local Amazon Web Services storage and a remote AS2 or SFTP server.</p> <ul> <li> <p>For an AS2 connector, you specify the <code>ConnectorId</code> and one or more <code>SendFilePaths</code> to identify the files you want to transfer.</p> </li> <li> <p>For an SFTP connector, the file transfer can be either outbound or inbound. In both cases, you specify the <code>ConnectorId</code>. Depending on the direction of the transfer, you also specify the following items:</p> <ul> <li> <p>If you are transferring file from a partner's SFTP server to Amazon Web Services storage, you specify one or more <code>RetrieveFilePaths</code> to identify the files you want to transfer, and a <code>LocalDirectoryPath</code> to specify the destination folder.</p> </li> <li> <p>If you are transferring file to a partner's SFTP server from Amazon Web Services storage, you specify one or more <code>SendFilePaths</code> to identify the files you want to transfer, and a <code>RemoteDirectoryPath</code> to specify the destination folder.</p> </li> </ul> </li> </ul>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            send_file_paths: <p>One or more source paths for the Amazon S3 storage. Each string represents a source file path for one outbound file transfer. For example, <code> <i>amzn-s3-demo-bucket</i>/<i>myfile.txt</i> </code>.</p> <note> <p>Replace <code> <i>amzn-s3-demo-bucket</i> </code> with one of your actual buckets.</p> </note>
            retrieve_file_paths: <p>One or more source paths for the partner's SFTP server. Each string represents a source file path for one inbound file transfer.</p>
            local_directory_path: <p>For an inbound transfer, the <code>LocaDirectoryPath</code> specifies the destination for one or more files that are transferred from the partner's SFTP server.</p>
            remote_directory_path: <p>For an outbound transfer, the <code>RemoteDirectoryPath</code> specifies the destination for one or more files that are transferred to the partner's SFTP server. If you don't specify a <code>RemoteDirectoryPath</code>, the destination for transferred files is the SFTP user's home directory.</p>
            custom_http_headers: <p>An array of key-value pairs that represent custom HTTP headers to include in AS2 messages. These headers are added to the AS2 message when sending files to your trading partner.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.start_file_transfer_request.StartFileTransferRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.start_file_transfer_response.StartFileTransferResponse"
        ]:
            import capo_transfer._operations.transfer_service.start_file_transfer

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.start_file_transfer.async_start_file_transfer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.start_file_transfer_request.StartFileTransferRequest = {
            "connector_id": connector_id
        }
        if send_file_paths is not None:
            input_["send_file_paths"] = send_file_paths
        if retrieve_file_paths is not None:
            input_["retrieve_file_paths"] = retrieve_file_paths
        if local_directory_path is not None:
            input_["local_directory_path"] = local_directory_path
        if remote_directory_path is not None:
            input_["remote_directory_path"] = remote_directory_path
        if custom_http_headers is not None:
            input_["custom_http_headers"] = custom_http_headers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_remote_delete(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        delete_path: "capo_transfer.types.file_path.FilePath",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.start_remote_delete_response.StartRemoteDeleteResponse":
        """<p>Deletes a file or directory on the remote SFTP server.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            delete_path: <p>The absolute path of the file or directory to delete. You can only specify one path per call to this operation.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.start_remote_delete_request.StartRemoteDeleteRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.start_remote_delete_response.StartRemoteDeleteResponse"
        ]:
            import capo_transfer._operations.transfer_service.start_remote_delete

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.start_remote_delete.async_start_remote_delete(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.start_remote_delete_request.StartRemoteDeleteRequest = {
            "connector_id": connector_id,
            "delete_path": delete_path,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_remote_move(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        source_path: "capo_transfer.types.file_path.FilePath",
        target_path: "capo_transfer.types.file_path.FilePath",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.start_remote_move_response.StartRemoteMoveResponse":
        """<p>Moves or renames a file or directory on the remote SFTP server.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            source_path: <p>The absolute path of the file or directory to move or rename. You can only specify one path per call to this operation.</p>
            target_path: <p>The absolute path for the target of the move/rename operation.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.start_remote_move_request.StartRemoteMoveRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.start_remote_move_response.StartRemoteMoveResponse"
        ]:
            import capo_transfer._operations.transfer_service.start_remote_move

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.start_remote_move.async_start_remote_move(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.start_remote_move_request.StartRemoteMoveRequest = {
            "connector_id": connector_id,
            "source_path": source_path,
            "target_path": target_path,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_server(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Changes the state of a file transfer protocol-enabled server from <code>OFFLINE</code> to <code>ONLINE</code>. It has no impact on a server that is already <code>ONLINE</code>. An <code>ONLINE</code> server can accept and process file transfer jobs.</p> <p>The state of <code>STARTING</code> indicates that the server is in an intermediate state, either not fully able to respond, or not fully online. The values of <code>START_FAILED</code> can indicate an error condition.</p> <p>No response is returned from this call.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that you start.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.start_server_request.StartServerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.start_server

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.start_server.async_start_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.start_server_request.StartServerRequest = {
            "server_id": server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_server(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Changes the state of a file transfer protocol-enabled server from <code>ONLINE</code> to <code>OFFLINE</code>. An <code>OFFLINE</code> server cannot accept and process file transfer jobs. Information tied to your server, such as server and user properties, are not affected by stopping your server.</p> <note> <p>Stopping the server does not reduce or impact your file transfer protocol endpoint billing; you must delete the server to stop being billed.</p> </note> <p>The state of <code>STOPPING</code> indicates that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of <code>STOP_FAILED</code> can indicate an error condition.</p> <p>No response is returned from this call.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that you stopped.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.stop_server_request.StopServerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.stop_server

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.stop_server.async_stop_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.stop_server_request.StopServerRequest = {
            "server_id": server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        arn: "capo_transfer.types.arn.Arn",
        tags: "capo_transfer.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.</p> <p>There is no response returned from this call.</p>

        Args:
            arn: <p>An Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a server, user, or role.</p>
            tags: <p>Key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (servers, users, workflows, and so on) for any purpose.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.tag_resource_request.TagResourceRequest = {
            "arn": arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_connection(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.test_connection_response.TestConnectionResponse":
        """<p>Tests whether your SFTP connector is set up successfully. We highly recommend that you call this operation to test your ability to transfer files between local Amazon Web Services storage and a trading partner's SFTP server.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.test_connection_request.TestConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.test_connection_response.TestConnectionResponse"
        ]:
            import capo_transfer._operations.transfer_service.test_connection

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.test_connection.async_test_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.test_connection_request.TestConnectionRequest = {
            "connector_id": connector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_identity_provider(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        user_name: "capo_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        server_protocol: Optional["capo_transfer.types.protocol.Protocol"] = None,
        source_ip: Optional["capo_transfer.types.source_ip.SourceIp"] = None,
        user_password: Optional[
            "capo_transfer.types.user_password.UserPassword"
        ] = None,
    ) -> "capo_transfer.types.test_identity_provider_response.TestIdentityProviderResponse":
        """<p>If the <code>IdentityProviderType</code> of a file transfer protocol-enabled server is <code>AWS_DIRECTORY_SERVICE</code> or <code>API_Gateway</code>, tests whether your identity provider is set up successfully. We highly recommend that you call this operation to test your authentication method as soon as you create your server. By doing so, you can troubleshoot issues with the identity provider integration to ensure that your users can successfully use the service.</p> <p> The <code>ServerId</code> and <code>UserName</code> parameters are required. The <code>ServerProtocol</code>, <code>SourceIp</code>, and <code>UserPassword</code> are all optional. </p> <p>Note the following:</p> <ul> <li> <p> You cannot use <code>TestIdentityProvider</code> if the <code>IdentityProviderType</code> of your server is <code>SERVICE_MANAGED</code>.</p> </li> <li> <p> <code>TestIdentityProvider</code> does not work with keys: it only accepts passwords.</p> </li> <li> <p> <code>TestIdentityProvider</code> can test the password operation for a custom Identity Provider that handles keys and passwords.</p> </li> <li> <p> If you provide any incorrect values for any parameters, the <code>Response</code> field is empty. </p> </li> <li> <p> If you provide a server ID for a server that uses service-managed users, you get an error: </p> <p> <code> An error occurred (InvalidRequestException) when calling the TestIdentityProvider operation: s-<i>server-ID</i> not configured for external auth </code> </p> </li> <li> <p> If you enter a Server ID for the <code>--server-id</code> parameter that does not identify an actual Transfer server, you receive the following error: </p> <p> <code>An error occurred (ResourceNotFoundException) when calling the TestIdentityProvider operation: Unknown server</code>. </p> <p>It is possible your sever is in a different region. You can specify a region by adding the following: <code>--region region-code</code>, such as <code>--region us-east-2</code> to specify a server in <b>US East (Ohio)</b>.</p> </li> </ul>

        Args:
            server_id: <p>A system-assigned identifier for a specific server. That server's user authentication method is tested with a user name and password.</p>
            server_protocol: <p>The type of file transfer protocol to be tested.</p> <p>The available protocols are:</p> <ul> <li> <p>Secure Shell (SSH) File Transfer Protocol (SFTP)</p> </li> <li> <p>File Transfer Protocol Secure (FTPS)</p> </li> <li> <p>File Transfer Protocol (FTP)</p> </li> <li> <p>Applicability Statement 2 (AS2)</p> </li> </ul>
            source_ip: <p>The source IP address of the account to be tested.</p>
            user_name: <p>The name of the account to be tested.</p>
            user_password: <p>The password of the account to be tested.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.test_identity_provider_request.TestIdentityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.test_identity_provider_response.TestIdentityProviderResponse"
        ]:
            import capo_transfer._operations.transfer_service.test_identity_provider

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.test_identity_provider.async_test_identity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.test_identity_provider_request.TestIdentityProviderRequest = {
            "server_id": server_id,
            "user_name": user_name,
        }
        if server_protocol is not None:
            input_["server_protocol"] = server_protocol
        if source_ip is not None:
            input_["source_ip"] = source_ip
        if user_password is not None:
            input_["user_password"] = user_password

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        arn: "capo_transfer.types.arn.Arn",
        tag_keys: "capo_transfer.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.</p> <p>No response is returned from this call.</p>

        Args:
            arn: <p>The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific Amazon Web Services resource, such as a server, user, or role.</p>
            tag_keys: <p>TagKeys are key-value pairs assigned to ARNs that can be used to group and search for resources by type. This metadata can be attached to resources for any purpose.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.untag_resource_request.UntagResourceRequest = {
            "arn": arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_access(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        external_id: "capo_transfer.types.external_id.ExternalId",
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
    ) -> "capo_transfer.types.update_access_response.UpdateAccessResponse":
        """<p>Allows you to update parameters for the access specified in the <code>ServerID</code> and <code>ExternalID</code> parameters.</p>

        Args:
            home_directory: <p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>
            home_directory_type: <p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>
            home_directory_mappings: <p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock down your user to the designated home directory ("<code>chroot</code>"). To do this, you can set <code>Entry</code> to <code>/</code> and set <code>Target</code> to the <code>HomeDirectory</code> parameter value.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]</code> </p>
            policy: <p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html">Example session policy</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html">AssumeRole</a> in the <i>Amazon Web ServicesSecurity Token Service API Reference</i>.</p> </note>
            role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.</p>
            external_id: <p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like "<i>YourGroupName</i>*"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_access_request.UpdateAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_access_response.UpdateAccessResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_access

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_access.async_update_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.update_access_request.UpdateAccessRequest = {
            "server_id": server_id,
            "external_id": external_id,
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

    async def update_host_key(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        host_key_id: "capo_transfer.types.host_key_id.HostKeyId",
        description: "capo_transfer.types.host_key_description.HostKeyDescription",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.update_host_key_response.UpdateHostKeyResponse":
        """<p>Updates the description for the host key that's specified by the <code>ServerId</code> and <code>HostKeyId</code> parameters.</p>

        Args:
            server_id: <p>The identifier of the server that contains the host key that you are updating.</p>
            host_key_id: <p>The identifier of the host key that you are updating.</p>
            description: <p>An updated description for the host key.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_host_key_request.UpdateHostKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_host_key_response.UpdateHostKeyResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_host_key

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_host_key.async_update_host_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.update_host_key_request.UpdateHostKeyRequest = {
            "server_id": server_id,
            "host_key_id": host_key_id,
            "description": description,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_agreement(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        local_profile_id: "capo_transfer.types.profile_id.ProfileId",
        partner_profile_id: "capo_transfer.types.profile_id.ProfileId",
        access_role: "capo_transfer.types.role.Role",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
        base_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        status: Optional[
            "capo_transfer.types.agreement_status_type.AgreementStatusType"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
        preserve_filename: Optional[
            "capo_transfer.types.preserve_filename_type.PreserveFilenameType"
        ] = None,
        enforce_message_signing: Optional[
            "capo_transfer.types.enforce_message_signing_type.EnforceMessageSigningType"
        ] = None,
        custom_directories: Optional[
            "capo_transfer.types.custom_directories_type.CustomDirectoriesType"
        ] = None,
    ) -> "capo_transfer.types.create_agreement_response.CreateAgreementResponse":
        """<p>Creates an agreement. An agreement is a bilateral trading partner agreement, or partnership, between an Transfer Family server and an AS2 process. The agreement defines the file and message transfer relationship between the server and the AS2 process. To define an agreement, Transfer Family combines a server, local profile, partner profile, certificate, and other attributes.</p> <p>The partner is identified with the <code>PartnerProfileId</code>, and the AS2 process is identified with the <code>LocalProfileId</code>.</p> <note> <p>Specify <i>either</i> <code>BaseDirectory</code> or <code>CustomDirectories</code>, but not both. Specifying both causes the command to fail.</p> </note>

        Args:
            description: <p>A name or short description to identify the agreement. </p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.</p>
            local_profile_id: <p>A unique identifier for the AS2 local profile.</p>
            partner_profile_id: <p>A unique identifier for the partner profile used in the agreement.</p>
            base_directory: <p>The landing directory (folder) for files transferred by using the AS2 protocol.</p> <p>A <code>BaseDirectory</code> example is <code>/<i>amzn-s3-demo-bucket</i>/home/mydirectory</code>.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            status: <p>The status of the agreement. The agreement can be either <code>ACTIVE</code> or <code>INACTIVE</code>.</p>
            tags: <p>Key-value pairs that can be used to group and search for agreements.</p>
            preserve_filename: <p> Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it. </p> <ul> <li> <p> <code>ENABLED</code>: the filename provided by your trading parter is preserved when the file is saved.</p> </li> <li> <p> <code>DISABLED</code> (default value): when Transfer Family saves the file, the filename is adjusted, as described in <a href="https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2">File names and locations</a>.</p> </li> </ul>
            enforce_message_signing: <p> Determines whether or not unsigned messages from your trading partners will be accepted. </p> <ul> <li> <p> <code>ENABLED</code>: Transfer Family rejects unsigned messages from your trading partner.</p> </li> <li> <p> <code>DISABLED</code> (default value): Transfer Family accepts unsigned messages from your trading partner.</p> </li> </ul>
            custom_directories: <p>A <code>CustomDirectoriesType</code> structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.</p> <ul> <li> <p>Failed files</p> </li> <li> <p>MDN files</p> </li> <li> <p>Payload files</p> </li> <li> <p>Status files</p> </li> <li> <p>Temporary files</p> </li> </ul>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_agreement_request.CreateAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_agreement_response.CreateAgreementResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_agreement

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_agreement.async_create_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.create_agreement_request.CreateAgreementRequest = {
            "server_id": server_id,
            "local_profile_id": local_profile_id,
            "partner_profile_id": partner_profile_id,
            "access_role": access_role,
        }
        if description is not None:
            input_["description"] = description
        if base_directory is not None:
            input_["base_directory"] = base_directory
        if status is not None:
            input_["status"] = status
        if tags is not None:
            input_["tags"] = tags
        if preserve_filename is not None:
            input_["preserve_filename"] = preserve_filename
        if enforce_message_signing is not None:
            input_["enforce_message_signing"] = enforce_message_signing
        if custom_directories is not None:
            input_["custom_directories"] = custom_directories

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_agreement(
        self,
        agreement_id: "capo_transfer.types.agreement_id.AgreementId",
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_agreement_response.DescribeAgreementResponse":
        """<p>Describes the agreement that's identified by the <code>AgreementId</code>.</p>

        Args:
            agreement_id: <p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>
            server_id: <p>The server identifier that's associated with the agreement.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_agreement_request.DescribeAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_agreement_response.DescribeAgreementResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_agreement

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_agreement.async_describe_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_agreement_request.DescribeAgreementRequest = {
            "agreement_id": agreement_id,
            "server_id": server_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_agreement(
        self,
        agreement_id: "capo_transfer.types.agreement_id.AgreementId",
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
        status: Optional[
            "capo_transfer.types.agreement_status_type.AgreementStatusType"
        ] = None,
        local_profile_id: Optional["capo_transfer.types.profile_id.ProfileId"] = None,
        partner_profile_id: Optional["capo_transfer.types.profile_id.ProfileId"] = None,
        base_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        access_role: Optional["capo_transfer.types.role.Role"] = None,
        preserve_filename: Optional[
            "capo_transfer.types.preserve_filename_type.PreserveFilenameType"
        ] = None,
        enforce_message_signing: Optional[
            "capo_transfer.types.enforce_message_signing_type.EnforceMessageSigningType"
        ] = None,
        custom_directories: Optional[
            "capo_transfer.types.custom_directories_type.CustomDirectoriesType"
        ] = None,
    ) -> "capo_transfer.types.update_agreement_response.UpdateAgreementResponse":
        """<p>Updates some of the parameters for an existing agreement. Provide the <code>AgreementId</code> and the <code>ServerId</code> for the agreement that you want to update, along with the new values for the parameters to update.</p> <note> <p>Specify <i>either</i> <code>BaseDirectory</code> or <code>CustomDirectories</code>, but not both. Specifying both causes the command to fail.</p> <p>If you update an agreement from using base directory to custom directories, the base directory is no longer used. Similarly, if you change from custom directories to a base directory, the custom directories are no longer used.</p> </note>

        Args:
            agreement_id: <p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.</p>
            description: <p>To replace the existing description, provide a short description for the agreement. </p>
            status: <p>You can update the status for the agreement, either activating an inactive agreement or the reverse.</p>
            local_profile_id: <p>A unique identifier for the AS2 local profile.</p> <p>To change the local profile identifier, provide a new value here.</p>
            partner_profile_id: <p>A unique identifier for the partner profile. To change the partner profile identifier, provide a new value here.</p>
            base_directory: <p>To change the landing directory (folder) for files that are transferred, provide the bucket folder that you want to use; for example, <code>/<i>amzn-s3-demo-bucket</i>/<i>home</i>/<i>mydirectory</i> </code>.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            preserve_filename: <p> Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it. </p> <ul> <li> <p> <code>ENABLED</code>: the filename provided by your trading parter is preserved when the file is saved.</p> </li> <li> <p> <code>DISABLED</code> (default value): when Transfer Family saves the file, the filename is adjusted, as described in <a href="https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2">File names and locations</a>.</p> </li> </ul>
            enforce_message_signing: <p> Determines whether or not unsigned messages from your trading partners will be accepted. </p> <ul> <li> <p> <code>ENABLED</code>: Transfer Family rejects unsigned messages from your trading partner.</p> </li> <li> <p> <code>DISABLED</code> (default value): Transfer Family accepts unsigned messages from your trading partner.</p> </li> </ul>
            custom_directories: <p>A <code>CustomDirectoriesType</code> structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.</p> <ul> <li> <p>Failed files</p> </li> <li> <p>MDN files</p> </li> <li> <p>Payload files</p> </li> <li> <p>Status files</p> </li> <li> <p>Temporary files</p> </li> </ul>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_agreement_request.UpdateAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_agreement_response.UpdateAgreementResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_agreement

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_agreement.async_update_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.update_agreement_request.UpdateAgreementRequest = {
            "agreement_id": agreement_id,
            "server_id": server_id,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if local_profile_id is not None:
            input_["local_profile_id"] = local_profile_id
        if partner_profile_id is not None:
            input_["partner_profile_id"] = partner_profile_id
        if base_directory is not None:
            input_["base_directory"] = base_directory
        if access_role is not None:
            input_["access_role"] = access_role
        if preserve_filename is not None:
            input_["preserve_filename"] = preserve_filename
        if enforce_message_signing is not None:
            input_["enforce_message_signing"] = enforce_message_signing
        if custom_directories is not None:
            input_["custom_directories"] = custom_directories

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_agreement(
        self,
        agreement_id: "capo_transfer.types.agreement_id.AgreementId",
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Delete the agreement that's specified in the provided <code>AgreementId</code>.</p>

        Args:
            agreement_id: <p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>
            server_id: <p>The server identifier associated with the agreement that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_agreement_request.DeleteAgreementRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_agreement

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_agreement.async_delete_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_agreement_request.DeleteAgreementRequest = {
            "agreement_id": agreement_id,
            "server_id": server_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agreements(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_agreements_response.ListAgreementsResponse":
        """<p>Returns a list of the agreements for the server that's identified by the <code>ServerId</code> that you supply. If you want to limit the results to a certain number, supply a value for the <code>MaxResults</code> parameter. If you ran the command previously and received a value for <code>NextToken</code>, you can supply that value to continue listing agreements from where you left off.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListAgreements</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional agreements.</p>
            server_id: <p>The identifier of the server for which you want a list of agreements.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_agreements_request.ListAgreementsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_agreements_response.ListAgreementsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_agreements

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_agreements.async_list_agreements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_agreements_request.ListAgreementsRequest = {
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

    async def iter_list_agreements(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_agreement.ListedAgreement]":
        _token = next_token
        while True:
            _response = await self.list_agreements(
                server_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agreements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def import_certificate(
        self,
        usage: "capo_transfer.types.certificate_usage_type.CertificateUsageType",
        certificate: "capo_transfer.types.certificate_body_type.CertificateBodyType",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate_chain: Optional[
            "capo_transfer.types.certificate_chain_type.CertificateChainType"
        ] = None,
        private_key: Optional[
            "capo_transfer.types.private_key_type.PrivateKeyType"
        ] = None,
        active_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        inactive_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
    ) -> "capo_transfer.types.import_certificate_response.ImportCertificateResponse":
        """<p>Imports the signing and encryption certificates that you need to create local (AS2) profiles and partner profiles.</p> <p>You can import both the certificate and its chain in the <code>Certificate</code> parameter.</p> <p>After importing a certificate, Transfer Family automatically creates a Amazon CloudWatch metric called <code>DaysUntilExpiry</code> that tracks the number of days until the certificate expires. The metric is based on the <code>InactiveDate</code> parameter and is published daily in the <code>AWS/Transfer</code> namespace.</p> <important> <p>It can take up to a full day after importing a certificate for Transfer Family to emit the <code>DaysUntilExpiry</code> metric to your account.</p> </important> <note> <p>If you use the <code>Certificate</code> parameter to upload both the certificate and its chain, don't use the <code>CertificateChain</code> parameter.</p> </note> <p> <b>CloudWatch monitoring</b> </p> <p>The <code>DaysUntilExpiry</code> metric includes the following specifications:</p> <ul> <li> <p> <b>Units:</b> Count (days)</p> </li> <li> <p> <b>Dimensions:</b> <code>CertificateId</code> (always present), <code>Description</code> (if provided during certificate import)</p> </li> <li> <p> <b>Statistics:</b> Minimum, Maximum, Average</p> </li> <li> <p> <b>Frequency:</b> Published daily</p> </li> </ul>

        Args:
            usage: <p>Specifies how this certificate is used. It can be used in the following ways:</p> <ul> <li> <p> <code>SIGNING</code>: For signing AS2 messages</p> </li> <li> <p> <code>ENCRYPTION</code>: For encrypting AS2 messages</p> </li> <li> <p> <code>TLS</code>: For securing AS2 communications sent over HTTPS</p> </li> </ul>
            certificate: <ul> <li> <p>For the CLI, provide a file path for a certificate in URI format. For example, <code>--certificate file://encryption-cert.pem</code>. Alternatively, you can provide the raw content.</p> </li> <li> <p>For the SDK, specify the raw content of a certificate file. For example, <code>--certificate "`cat encryption-cert.pem`"</code>.</p> </li> </ul> <note> <p>You can provide both the certificate and its chain in this parameter, without needing to use the <code>CertificateChain</code> parameter. If you use this parameter for both the certificate and its chain, do not use the <code>CertificateChain</code> parameter.</p> </note>
            certificate_chain: <p>An optional list of certificates that make up the chain for the certificate that's being imported.</p>
            private_key: <ul> <li> <p>For the CLI, provide a file path for a private key in URI format. For example, <code>--private-key file://encryption-key.pem</code>. Alternatively, you can provide the raw content of the private key file.</p> </li> <li> <p>For the SDK, specify the raw content of a private key file. For example, <code>--private-key "`cat encryption-key.pem`"</code> </p> </li> </ul>
            active_date: <p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>
            inactive_date: <p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>
            description: <p>A short description that helps identify the certificate. </p>
            tags: <p>Key-value pairs that can be used to group and search for certificates.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.import_certificate_request.ImportCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.import_certificate_response.ImportCertificateResponse"
        ]:
            import capo_transfer._operations.transfer_service.import_certificate

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.import_certificate.async_import_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.import_certificate_request.ImportCertificateRequest = {
            "usage": usage,
            "certificate": certificate,
        }
        if certificate_chain is not None:
            input_["certificate_chain"] = certificate_chain
        if private_key is not None:
            input_["private_key"] = private_key
        if active_date is not None:
            input_["active_date"] = active_date
        if inactive_date is not None:
            input_["inactive_date"] = inactive_date
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_certificate(
        self,
        certificate_id: "capo_transfer.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> (
        "capo_transfer.types.describe_certificate_response.DescribeCertificateResponse"
    ):
        """<p>Describes the certificate that's identified by the <code>CertificateId</code>.</p> <note> <p>Transfer Family automatically publishes a Amazon CloudWatch metric called <code>DaysUntilExpiry</code> for imported certificates. This metric tracks the number of days until the certificate expires based on the <code>InactiveDate</code>. The metric is available in the <code>AWS/Transfer</code> namespace and includes the <code>CertificateId</code> as a dimension.</p> </note>

        Args:
            certificate_id: <p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_certificate_request.DescribeCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_certificate_response.DescribeCertificateResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_certificate

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_certificate.async_describe_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_certificate_request.DescribeCertificateRequest = {
            "certificate_id": certificate_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_certificate(
        self,
        certificate_id: "capo_transfer.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        active_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        inactive_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
    ) -> "capo_transfer.types.update_certificate_response.UpdateCertificateResponse":
        """<p>Updates the active and inactive dates for a certificate.</p>

        Args:
            certificate_id: <p>The identifier of the certificate object that you are updating.</p>
            active_date: <p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>
            inactive_date: <p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>
            description: <p>A short description to help identify the certificate.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_certificate_request.UpdateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_certificate_response.UpdateCertificateResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_certificate

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_certificate.async_update_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.update_certificate_request.UpdateCertificateRequest = {
            "certificate_id": certificate_id
        }
        if active_date is not None:
            input_["active_date"] = active_date
        if inactive_date is not None:
            input_["inactive_date"] = inactive_date
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_certificate(
        self,
        certificate_id: "capo_transfer.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the certificate that's specified in the <code>CertificateId</code> parameter.</p>

        Args:
            certificate_id: <p>The identifier of the certificate object that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_certificate_request.DeleteCertificateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_certificate

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_certificate.async_delete_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_certificate_request.DeleteCertificateRequest = {
            "certificate_id": certificate_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_certificates(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_certificates_response.ListCertificatesResponse":
        """<p>Returns a list of the current certificates that have been imported into Transfer Family. If you want to limit the results to a certain number, supply a value for the <code>MaxResults</code> parameter. If you ran the command previously and received a value for the <code>NextToken</code> parameter, you can supply that value to continue listing certificates from where you left off.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListCertificates</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional certificates.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_certificates_request.ListCertificatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_certificates_response.ListCertificatesResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_certificates

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_certificates.async_list_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_certificates_request.ListCertificatesRequest = {}
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

    async def iter_list_certificates(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_certificate.ListedCertificate]":
        _token = next_token
        while True:
            _response = await self.list_certificates(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("certificates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_connector(
        self,
        access_role: "capo_transfer.types.role.Role",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        url: Optional["capo_transfer.types.url.Url"] = None,
        as2_config: Optional[
            "capo_transfer.types.as2_connector_config.As2ConnectorConfig"
        ] = None,
        logging_role: Optional["capo_transfer.types.role.Role"] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
        sftp_config: Optional[
            "capo_transfer.types.sftp_connector_config.SftpConnectorConfig"
        ] = None,
        security_policy_name: Optional[
            "capo_transfer.types.connector_security_policy_name.ConnectorSecurityPolicyName"
        ] = None,
        egress_config: Optional[
            "capo_transfer.types.connector_egress_config.ConnectorEgressConfig"
        ] = None,
        ip_address_type: Optional[
            "capo_transfer.types.connectors_ip_address_type.ConnectorsIpAddressType"
        ] = None,
    ) -> "capo_transfer.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates the connector, which captures the parameters for a connection for the AS2 or SFTP protocol. For AS2, the connector is required for sending files to an externally hosted AS2 server. For SFTP, the connector is required when sending files to an SFTP server or receiving files from an SFTP server. For more details about connectors, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/configure-as2-connector.html">Configure AS2 connectors</a> and <a href="https://docs.aws.amazon.com/transfer/latest/userguide/configure-sftp-connector.html">Create SFTP connectors</a>.</p> <note> <p>You must specify exactly one configuration object: either for AS2 (<code>As2Config</code>) or SFTP (<code>SftpConfig</code>).</p> </note>

        Args:
            url: <p>The URL of the partner's AS2 or SFTP endpoint.</p> <p>When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.</p>
            as2_config: <p>A structure that contains the parameters for an AS2 connector object.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.</p>
            tags: <p>Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.</p>
            sftp_config: <p>A structure that contains the parameters for an SFTP connector object.</p>
            security_policy_name: <p>Specifies the name of the security policy for the connector.</p>
            egress_config: <p>Specifies the egress configuration for the connector, which determines how traffic is routed from the connector to the SFTP server. When set to VPC, enables routing through customer VPCs using VPC_LATTICE for private connectivity.</p>
            ip_address_type: <p>Specifies the IP address type for the connector's network connections. When set to <code>IPV4</code>, the connector uses IPv4 addresses only. When set to <code>DUALSTACK</code>, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_connector_request.CreateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_connector_response.CreateConnectorResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_connector

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_connector.async_create_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.create_connector_request.CreateConnectorRequest = {
            "access_role": access_role
        }
        if url is not None:
            input_["url"] = url
        if as2_config is not None:
            input_["as2_config"] = as2_config
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if tags is not None:
            input_["tags"] = tags
        if sftp_config is not None:
            input_["sftp_config"] = sftp_config
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if egress_config is not None:
            input_["egress_config"] = egress_config
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_connector(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_connector_response.DescribeConnectorResponse":
        """<p>Describes the connector that's identified by the <code>ConnectorId.</code> </p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_connector_request.DescribeConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_connector_response.DescribeConnectorResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_connector

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_connector.async_describe_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_connector_request.DescribeConnectorRequest = {
            "connector_id": connector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connector(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        url: Optional["capo_transfer.types.url.Url"] = None,
        as2_config: Optional[
            "capo_transfer.types.as2_connector_config.As2ConnectorConfig"
        ] = None,
        access_role: Optional["capo_transfer.types.role.Role"] = None,
        logging_role: Optional["capo_transfer.types.role.Role"] = None,
        sftp_config: Optional[
            "capo_transfer.types.sftp_connector_config.SftpConnectorConfig"
        ] = None,
        security_policy_name: Optional[
            "capo_transfer.types.connector_security_policy_name.ConnectorSecurityPolicyName"
        ] = None,
        egress_config: Optional[
            "capo_transfer.types.update_connector_egress_config.UpdateConnectorEgressConfig"
        ] = None,
        ip_address_type: Optional[
            "capo_transfer.types.connectors_ip_address_type.ConnectorsIpAddressType"
        ] = None,
    ) -> "capo_transfer.types.update_connector_response.UpdateConnectorResponse":
        """<p>Updates some of the parameters for an existing connector. Provide the <code>ConnectorId</code> for the connector that you want to update, along with the new values for the parameters to update.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            url: <p>The URL of the partner's AS2 or SFTP endpoint.</p> <p>When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.</p>
            as2_config: <p>A structure that contains the parameters for an AS2 connector object.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.</p>
            sftp_config: <p>A structure that contains the parameters for an SFTP connector object.</p>
            security_policy_name: <p>Specifies the name of the security policy for the connector.</p>
            egress_config: <p>Updates the egress configuration for the connector, allowing you to modify how traffic is routed from the connector to the SFTP server. Changes to VPC configuration may require connector restart.</p>
            ip_address_type: <p>Specifies the IP address type for the connector's network connections. When set to <code>IPV4</code>, the connector uses IPv4 addresses only. When set to <code>DUALSTACK</code>, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_connector_request.UpdateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_connector_response.UpdateConnectorResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_connector

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_connector.async_update_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.update_connector_request.UpdateConnectorRequest = {
            "connector_id": connector_id
        }
        if url is not None:
            input_["url"] = url
        if as2_config is not None:
            input_["as2_config"] = as2_config
        if access_role is not None:
            input_["access_role"] = access_role
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if sftp_config is not None:
            input_["sftp_config"] = sftp_config
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if egress_config is not None:
            input_["egress_config"] = egress_config
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connector(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the connector that's specified in the provided <code>ConnectorId</code>.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_connector

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_connector.async_delete_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_id": connector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_connectors_response.ListConnectorsResponse":
        """<p>Lists the connectors for the specified Region.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListConnectors</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional connectors.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_connectors

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_connectors_request.ListConnectorsRequest = {}
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

    async def iter_list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_connector.ListedConnector]":
        _token = next_token
        while True:
            _response = await self.list_connectors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("connectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_profile(
        self,
        as2_id: "capo_transfer.types.as2_id.As2Id",
        profile_type: "capo_transfer.types.profile_type.ProfileType",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate_ids: Optional[
            "capo_transfer.types.certificate_ids.CertificateIds"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
    ) -> "capo_transfer.types.create_profile_response.CreateProfileResponse":
        """<p>Creates the local or partner profile to use for AS2 transfers.</p>

        Args:
            as2_id: <p>The <code>As2Id</code> is the <i>AS2-name</i>, as defined in the <a href="https://datatracker.ietf.org/doc/html/rfc4130">RFC 4130</a>. For inbound transfers, this is the <code>AS2-From</code> header for the AS2 messages sent from the partner. For outbound connectors, this is the <code>AS2-To</code> header for the AS2 messages sent to the partner using the <code>StartFileTransfer</code> API operation. This ID cannot include spaces.</p>
            profile_type: <p>Determines the type of profile to create:</p> <ul> <li> <p>Specify <code>LOCAL</code> to create a local profile. A local profile represents the AS2-enabled Transfer Family server organization or party.</p> </li> <li> <p>Specify <code>PARTNER</code> to create a partner profile. A partner profile represents a remote organization, external to Transfer Family.</p> </li> </ul>
            certificate_ids: <p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>
            tags: <p>Key-value pairs that can be used to group and search for AS2 profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_profile_request.CreateProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_profile_response.CreateProfileResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_profile

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_profile.async_create_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.create_profile_request.CreateProfileRequest = {
            "as2_id": as2_id,
            "profile_type": profile_type,
        }
        if certificate_ids is not None:
            input_["certificate_ids"] = certificate_ids
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_profile(
        self,
        profile_id: "capo_transfer.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_profile_response.DescribeProfileResponse":
        """<p>Returns the details of the profile that's specified by the <code>ProfileId</code>.</p>

        Args:
            profile_id: <p>The identifier of the profile that you want described.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_profile_request.DescribeProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_profile_response.DescribeProfileResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_profile

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_profile.async_describe_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_profile_request.DescribeProfileRequest = {
            "profile_id": profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_profile(
        self,
        profile_id: "capo_transfer.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate_ids: Optional[
            "capo_transfer.types.certificate_ids.CertificateIds"
        ] = None,
    ) -> "capo_transfer.types.update_profile_response.UpdateProfileResponse":
        """<p>Updates some of the parameters for an existing profile. Provide the <code>ProfileId</code> for the profile that you want to update, along with the new values for the parameters to update.</p>

        Args:
            profile_id: <p>The identifier of the profile object that you are updating.</p>
            certificate_ids: <p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_profile_request.UpdateProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_profile_response.UpdateProfileResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_profile

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_profile.async_update_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.update_profile_request.UpdateProfileRequest = {
            "profile_id": profile_id
        }
        if certificate_ids is not None:
            input_["certificate_ids"] = certificate_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_profile(
        self,
        profile_id: "capo_transfer.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the profile that's specified in the <code>ProfileId</code> parameter.</p>

        Args:
            profile_id: <p>The identifier of the profile that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_profile_request.DeleteProfileRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_profile

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_profile.async_delete_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_profile_request.DeleteProfileRequest = {
            "profile_id": profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_profiles(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
        profile_type: Optional["capo_transfer.types.profile_type.ProfileType"] = None,
    ) -> "capo_transfer.types.list_profiles_response.ListProfilesResponse":
        """<p>Returns a list of the profiles for your system. If you want to limit the results to a certain number, supply a value for the <code>MaxResults</code> parameter. If you ran the command previously and received a value for <code>NextToken</code>, you can supply that value to continue listing profiles from where you left off.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When there are additional results that were not returned, a <code>NextToken</code> parameter is returned. You can use that value for a subsequent call to <code>ListProfiles</code> to continue listing results.</p>
            profile_type: <p>Indicates whether to list only <code>LOCAL</code> type profiles or only <code>PARTNER</code> type profiles. If not supplied in the request, the command lists all types of profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_profiles_request.ListProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_profiles_response.ListProfilesResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_profiles

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_profiles.async_list_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_profiles_request.ListProfilesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if profile_type is not None:
            input_["profile_type"] = profile_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_profiles(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
        profile_type: Optional["capo_transfer.types.profile_type.ProfileType"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_profile.ListedProfile]":
        _token = next_token
        while True:
            _response = await self.list_profiles(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                profile_type=profile_type,
            )
            _page = _resolve_path(_response, ("profiles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_server(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate: Optional["capo_transfer.types.certificate.Certificate"] = None,
        domain: Optional["capo_transfer.types.domain.Domain"] = None,
        endpoint_details: Optional[
            "capo_transfer.types.endpoint_details.EndpointDetails"
        ] = None,
        endpoint_type: Optional[
            "capo_transfer.types.endpoint_type.EndpointType"
        ] = None,
        host_key: Optional["capo_transfer.types.host_key.HostKey"] = None,
        identity_provider_details: Optional[
            "capo_transfer.types.identity_provider_details.IdentityProviderDetails"
        ] = None,
        identity_provider_type: Optional[
            "capo_transfer.types.identity_provider_type.IdentityProviderType"
        ] = None,
        logging_role: Optional["capo_transfer.types.nullable_role.NullableRole"] = None,
        post_authentication_login_banner: Optional[
            "capo_transfer.types.post_authentication_login_banner.PostAuthenticationLoginBanner"
        ] = None,
        pre_authentication_login_banner: Optional[
            "capo_transfer.types.pre_authentication_login_banner.PreAuthenticationLoginBanner"
        ] = None,
        protocols: Optional["capo_transfer.types.protocols.Protocols"] = None,
        protocol_details: Optional[
            "capo_transfer.types.protocol_details.ProtocolDetails"
        ] = None,
        security_policy_name: Optional[
            "capo_transfer.types.security_policy_name.SecurityPolicyName"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
        workflow_details: Optional[
            "capo_transfer.types.workflow_details.WorkflowDetails"
        ] = None,
        structured_log_destinations: Optional[
            "capo_transfer.types.structured_log_destinations.StructuredLogDestinations"
        ] = None,
        s3_storage_options: Optional[
            "capo_transfer.types.s3_storage_options.S3StorageOptions"
        ] = None,
        ip_address_type: Optional[
            "capo_transfer.types.ip_address_type.IpAddressType"
        ] = None,
    ) -> "capo_transfer.types.create_server_response.CreateServerResponse":
        """<p>Instantiates an auto-scaling virtual server based on the selected file transfer protocol in Amazon Web Services. When you make updates to your file transfer protocol-enabled server or when you work with users, use the service-generated <code>ServerId</code> property that is assigned to the newly created server.</p>

        Args:
            certificate: <p>The Amazon Resource Name (ARN) of the Certificate Manager (ACM) certificate. Required when <code>Protocols</code> is set to <code>FTPS</code>.</p> <p>To request a new public certificate, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html">Request a public certificate</a> in the <i>Certificate Manager User Guide</i>.</p> <p>To import an existing certificate into ACM, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html">Importing certificates into ACM</a> in the <i>Certificate Manager User Guide</i>.</p> <p>To request a private certificate to use FTPS through private IP addresses, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html">Request a private certificate</a> in the <i>Certificate Manager User Guide</i>.</p> <p>Certificates with the following cryptographic algorithms and key sizes are supported:</p> <ul> <li> <p>2048-bit RSA (RSA_2048)</p> </li> <li> <p>4096-bit RSA (RSA_4096)</p> </li> <li> <p>Elliptic Prime Curve 256 bit (EC_prime256v1)</p> </li> <li> <p>Elliptic Prime Curve 384 bit (EC_secp384r1)</p> </li> <li> <p>Elliptic Prime Curve 521 bit (EC_secp521r1)</p> </li> </ul> <note> <p>The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.</p> </note>
            domain: <p>The domain of the storage system that is used for file transfers. There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.</p> <note> <p>After the server is created, the domain cannot be changed.</p> </note>
            endpoint_details: <p>The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.</p>
            endpoint_type: <p>The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it.</p> <note> <p> After May 19, 2021, you won't be able to create a server using <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account if your account hasn't already done so before May 19, 2021. If you have already created servers with <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account on or before May 19, 2021, you will not be affected. After this date, use <code>EndpointType</code>=<code>VPC</code>.</p> <p>For more information, see https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.</p> <p>It is recommended that you use <code>VPC</code> as the <code>EndpointType</code>. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with <code>EndpointType</code> set to <code>VPC_ENDPOINT</code>.</p> </note>
            host_key: <p>The RSA, ECDSA, or ED25519 private key to use for your SFTP-enabled server. You can add multiple host keys, in case you want to rotate keys, or have a set of active keys that use different algorithms.</p> <p>Use the following command to generate an RSA 2048 bit key with no passphrase:</p> <p> <code>ssh-keygen -t rsa -b 2048 -N "" -m PEM -f my-new-server-key</code>.</p> <p>Use a minimum value of 2048 for the <code>-b</code> option. You can create a stronger key by using 3072 or 4096.</p> <p>Use the following command to generate an ECDSA 256 bit key with no passphrase:</p> <p> <code>ssh-keygen -t ecdsa -b 256 -N "" -m PEM -f my-new-server-key</code>.</p> <p>Valid values for the <code>-b</code> option for ECDSA are 256, 384, and 521.</p> <p>Use the following command to generate an ED25519 key with no passphrase:</p> <p> <code>ssh-keygen -t ed25519 -N "" -f my-new-server-key</code>.</p> <p>For all of these commands, you can replace <i>my-new-server-key</i> with a string of your choice.</p> <important> <p>If you aren't planning to migrate existing users from an existing SFTP-enabled server to a new server, don't update the host key. Accidentally changing a server's host key can be disruptive.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html#configuring-servers-change-host-key">Manage host keys for your SFTP-enabled server</a> in the <i>Transfer Family User Guide</i>.</p>
            identity_provider_details: <p>Required when <code>IdentityProviderType</code> is set to <code>AWS_DIRECTORY_SERVICE</code>, <code>Amazon Web Services_LAMBDA</code> or <code>API_GATEWAY</code>. Accepts an array containing all of the information required to use a directory in <code>AWS_DIRECTORY_SERVICE</code> or invoke a customer-supplied authentication API, including the API Gateway URL. Cannot be specified when <code>IdentityProviderType</code> is set to <code>SERVICE_MANAGED</code>.</p>
            identity_provider_type: <p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.</p>
            post_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.</p> <note> <p>The SFTP protocol does not support post-authentication display banners.</p> </note>
            pre_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:</p> <p> <code>This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.</code> </p>
            protocols: <p>Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are:</p> <ul> <li> <p> <code>SFTP</code> (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH</p> </li> <li> <p> <code>FTPS</code> (File Transfer Protocol Secure): File transfer with TLS encryption</p> </li> <li> <p> <code>FTP</code> (File Transfer Protocol): Unencrypted file transfer</p> </li> <li> <p> <code>AS2</code> (Applicability Statement 2): used for transporting structured business-to-business data</p> </li> </ul> <note> <ul> <li> <p>If you select <code>FTPS</code>, you must choose a certificate stored in Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.</p> </li> <li> <p>If <code>Protocol</code> includes either <code>FTP</code> or <code>FTPS</code>, then the <code>EndpointType</code> must be <code>VPC</code> and the <code>IdentityProviderType</code> must be either <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>FTP</code>, then <code>AddressAllocationIds</code> cannot be associated.</p> </li> <li> <p>If <code>Protocol</code> is set only to <code>SFTP</code>, the <code>EndpointType</code> can be set to <code>PUBLIC</code> and the <code>IdentityProviderType</code> can be set any of the supported identity types: <code>SERVICE_MANAGED</code>, <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>AS2</code>, then the <code>EndpointType</code> must be <code>VPC</code>, and domain must be Amazon S3.</p> </li> </ul> </note>
            protocol_details: <p>The protocol settings that are configured for your server.</p> <note> <p>Avoid placing Network Load Balancers (NLBs) or NAT gateways in front of Transfer Family servers, as this increases costs and can cause performance issues, including reduced connection limits for FTPS. For more details, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html#nlb-considerations"> Avoid placing NLBs and NATs in front of Transfer Family</a>.</p> </note> <ul> <li> <p> To indicate passive mode (for FTP and FTPS protocols), use the <code>PassiveIp</code> parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer. </p> </li> <li> <p>To ignore the error that is generated when the client attempts to use the <code>SETSTAT</code> command on a file that you are uploading to an Amazon S3 bucket, use the <code>SetStatOption</code> parameter. To have the Transfer Family server ignore the <code>SETSTAT</code> command and upload files without needing to make any changes to your SFTP client, set the value to <code>ENABLE_NO_OP</code>. If you set the <code>SetStatOption</code> parameter to <code>ENABLE_NO_OP</code>, Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a <code>SETSTAT</code> call.</p> </li> <li> <p>To specify which ports your Transfer Family server listens to, use the <code>SftpPorts</code> parameter.</p> </li> <li> <p>To determine whether your Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the <code>TlsSessionResumptionMode</code> parameter.</p> </li> <li> <p> <code>As2Transports</code> indicates the transport method for the AS2 messages. Currently, only HTTP is supported.</p> </li> </ul>
            security_policy_name: <p>Specifies the name of the security policy for the server.</p>
            tags: <p>Key-value pairs that can be used to group and search for servers.</p>
            workflow_details: <p>Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.</p> <p>In addition to a workflow to execute when a file is uploaded completely, <code>WorkflowDetails</code> can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.</p>
            structured_log_destinations: <p>Specifies the log groups to which your server logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:partition:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p> <p>If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an <code>update-server</code> call. For example:</p> <p> <code>update-server --server-id s-1234567890abcdef0 --structured-log-destinations</code> </p>
            s3_storage_options: <p>Specifies whether or not performance for your Amazon S3 directories is optimized.</p> <ul> <li> <p>If using the console, this is enabled by default.</p> </li> <li> <p>If using the API or CLI, this is disabled by default.</p> </li> </ul> <p>By default, home directory mappings have a <code>TYPE</code> of <code>DIRECTORY</code>. If you enable this option, you would then need to explicitly set the <code>HomeDirectoryMapEntry</code> <code>Type</code> to <code>FILE</code> if you want a mapping to have a file target.</p>
            ip_address_type: <p>Specifies whether to use IPv4 only, or to use dual-stack (IPv4 and IPv6) for your Transfer Family endpoint. The default value is <code>IPV4</code>.</p> <important> <p>The <code>IpAddressType</code> parameter has the following limitations:</p> <ul> <li> <p>It cannot be changed while the server is online. You must stop the server before modifying this parameter.</p> </li> <li> <p>It cannot be updated to <code>DUALSTACK</code> if the server has <code>AddressAllocationIds</code> specified.</p> </li> </ul> </important> <note> <p>When using <code>DUALSTACK</code> as the <code>IpAddressType</code>, you cannot set the <code>AddressAllocationIds</code> parameter for the <a href="https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html">EndpointDetails</a> for the server.</p> </note>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_server_request.CreateServerRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_server_response.CreateServerResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_server

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_server.async_create_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.create_server_request.CreateServerRequest = {}
        if certificate is not None:
            input_["certificate"] = certificate
        if domain is not None:
            input_["domain"] = domain
        if endpoint_details is not None:
            input_["endpoint_details"] = endpoint_details
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
        if host_key is not None:
            input_["host_key"] = host_key
        if identity_provider_details is not None:
            input_["identity_provider_details"] = identity_provider_details
        if identity_provider_type is not None:
            input_["identity_provider_type"] = identity_provider_type
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if post_authentication_login_banner is not None:
            input_["post_authentication_login_banner"] = (
                post_authentication_login_banner
            )
        if pre_authentication_login_banner is not None:
            input_["pre_authentication_login_banner"] = pre_authentication_login_banner
        if protocols is not None:
            input_["protocols"] = protocols
        if protocol_details is not None:
            input_["protocol_details"] = protocol_details
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if tags is not None:
            input_["tags"] = tags
        if workflow_details is not None:
            input_["workflow_details"] = workflow_details
        if structured_log_destinations is not None:
            input_["structured_log_destinations"] = structured_log_destinations
        if s3_storage_options is not None:
            input_["s3_storage_options"] = s3_storage_options
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_server(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_server_response.DescribeServerResponse":
        """<p>Describes a file transfer protocol-enabled server that you specify by passing the <code>ServerId</code> parameter.</p> <p>The response contains a description of a server's properties. When you set <code>EndpointType</code> to VPC, the response will contain the <code>EndpointDetails</code>.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_server_request.DescribeServerRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_server_response.DescribeServerResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_server

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_server.async_describe_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_server_request.DescribeServerRequest = {
            "server_id": server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_server(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate: Optional["capo_transfer.types.certificate.Certificate"] = None,
        protocol_details: Optional[
            "capo_transfer.types.protocol_details.ProtocolDetails"
        ] = None,
        endpoint_details: Optional[
            "capo_transfer.types.endpoint_details.EndpointDetails"
        ] = None,
        endpoint_type: Optional[
            "capo_transfer.types.endpoint_type.EndpointType"
        ] = None,
        host_key: Optional["capo_transfer.types.host_key.HostKey"] = None,
        identity_provider_details: Optional[
            "capo_transfer.types.identity_provider_details.IdentityProviderDetails"
        ] = None,
        logging_role: Optional["capo_transfer.types.nullable_role.NullableRole"] = None,
        post_authentication_login_banner: Optional[
            "capo_transfer.types.post_authentication_login_banner.PostAuthenticationLoginBanner"
        ] = None,
        pre_authentication_login_banner: Optional[
            "capo_transfer.types.pre_authentication_login_banner.PreAuthenticationLoginBanner"
        ] = None,
        protocols: Optional["capo_transfer.types.protocols.Protocols"] = None,
        security_policy_name: Optional[
            "capo_transfer.types.security_policy_name.SecurityPolicyName"
        ] = None,
        workflow_details: Optional[
            "capo_transfer.types.workflow_details.WorkflowDetails"
        ] = None,
        structured_log_destinations: Optional[
            "capo_transfer.types.structured_log_destinations.StructuredLogDestinations"
        ] = None,
        s3_storage_options: Optional[
            "capo_transfer.types.s3_storage_options.S3StorageOptions"
        ] = None,
        ip_address_type: Optional[
            "capo_transfer.types.ip_address_type.IpAddressType"
        ] = None,
        identity_provider_type: Optional[
            "capo_transfer.types.identity_provider_type.IdentityProviderType"
        ] = None,
    ) -> "capo_transfer.types.update_server_response.UpdateServerResponse":
        """<p>Updates the file transfer protocol-enabled server's properties after that server has been created.</p> <p>The <code>UpdateServer</code> call returns the <code>ServerId</code> of the server you updated.</p>

        Args:
            certificate: <p>The Amazon Resource Name (ARN) of the Amazon Web ServicesCertificate Manager (ACM) certificate. Required when <code>Protocols</code> is set to <code>FTPS</code>.</p> <p>To request a new public certificate, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html">Request a public certificate</a> in the <i> Amazon Web ServicesCertificate Manager User Guide</i>.</p> <p>To import an existing certificate into ACM, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html">Importing certificates into ACM</a> in the <i> Amazon Web ServicesCertificate Manager User Guide</i>.</p> <p>To request a private certificate to use FTPS through private IP addresses, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html">Request a private certificate</a> in the <i> Amazon Web ServicesCertificate Manager User Guide</i>.</p> <p>Certificates with the following cryptographic algorithms and key sizes are supported:</p> <ul> <li> <p>2048-bit RSA (RSA_2048)</p> </li> <li> <p>4096-bit RSA (RSA_4096)</p> </li> <li> <p>Elliptic Prime Curve 256 bit (EC_prime256v1)</p> </li> <li> <p>Elliptic Prime Curve 384 bit (EC_secp384r1)</p> </li> <li> <p>Elliptic Prime Curve 521 bit (EC_secp521r1)</p> </li> </ul> <note> <p>The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.</p> </note>
            protocol_details: <p>The protocol settings that are configured for your server.</p> <note> <p>Avoid placing Network Load Balancers (NLBs) or NAT gateways in front of Transfer Family servers, as this increases costs and can cause performance issues, including reduced connection limits for FTPS. For more details, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html#nlb-considerations"> Avoid placing NLBs and NATs in front of Transfer Family</a>.</p> </note> <ul> <li> <p> To indicate passive mode (for FTP and FTPS protocols), use the <code>PassiveIp</code> parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer. </p> </li> <li> <p>To ignore the error that is generated when the client attempts to use the <code>SETSTAT</code> command on a file that you are uploading to an Amazon S3 bucket, use the <code>SetStatOption</code> parameter. To have the Transfer Family server ignore the <code>SETSTAT</code> command and upload files without needing to make any changes to your SFTP client, set the value to <code>ENABLE_NO_OP</code>. If you set the <code>SetStatOption</code> parameter to <code>ENABLE_NO_OP</code>, Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a <code>SETSTAT</code> call.</p> </li> <li> <p>To specify which ports your Transfer Family server listens to, use the <code>SftpPorts</code> parameter.</p> </li> <li> <p>To determine whether your Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the <code>TlsSessionResumptionMode</code> parameter.</p> </li> <li> <p> <code>As2Transports</code> indicates the transport method for the AS2 messages. Currently, only HTTP is supported.</p> </li> </ul>
            endpoint_details: <p>The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.</p>
            endpoint_type: <p>The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it.</p> <note> <p> After May 19, 2021, you won't be able to create a server using <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account if your account hasn't already done so before May 19, 2021. If you have already created servers with <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account on or before May 19, 2021, you will not be affected. After this date, use <code>EndpointType</code>=<code>VPC</code>.</p> <p>For more information, see https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.</p> <p>It is recommended that you use <code>VPC</code> as the <code>EndpointType</code>. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with <code>EndpointType</code> set to <code>VPC_ENDPOINT</code>.</p> </note>
            host_key: <p>The RSA, ECDSA, or ED25519 private key to use for your SFTP-enabled server. You can add multiple host keys, in case you want to rotate keys, or have a set of active keys that use different algorithms.</p> <p>Use the following command to generate an RSA 2048 bit key with no passphrase:</p> <p> <code>ssh-keygen -t rsa -b 2048 -N "" -m PEM -f my-new-server-key</code>.</p> <p>Use a minimum value of 2048 for the <code>-b</code> option. You can create a stronger key by using 3072 or 4096.</p> <p>Use the following command to generate an ECDSA 256 bit key with no passphrase:</p> <p> <code>ssh-keygen -t ecdsa -b 256 -N "" -m PEM -f my-new-server-key</code>.</p> <p>Valid values for the <code>-b</code> option for ECDSA are 256, 384, and 521.</p> <p>Use the following command to generate an ED25519 key with no passphrase:</p> <p> <code>ssh-keygen -t ed25519 -N "" -f my-new-server-key</code>.</p> <p>For all of these commands, you can replace <i>my-new-server-key</i> with a string of your choice.</p> <important> <p>If you aren't planning to migrate existing users from an existing SFTP-enabled server to a new server, don't update the host key. Accidentally changing a server's host key can be disruptive.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html#configuring-servers-change-host-key">Manage host keys for your SFTP-enabled server</a> in the <i>Transfer Family User Guide</i>.</p>
            identity_provider_details: <p>An array containing all of the information required to call a customer's authentication API method.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.</p>
            post_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.</p> <note> <p>The SFTP protocol does not support post-authentication display banners.</p> </note>
            pre_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:</p> <p> <code>This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.</code> </p>
            protocols: <p>Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are:</p> <ul> <li> <p> <code>SFTP</code> (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH</p> </li> <li> <p> <code>FTPS</code> (File Transfer Protocol Secure): File transfer with TLS encryption</p> </li> <li> <p> <code>FTP</code> (File Transfer Protocol): Unencrypted file transfer</p> </li> <li> <p> <code>AS2</code> (Applicability Statement 2): used for transporting structured business-to-business data</p> </li> </ul> <note> <ul> <li> <p>If you select <code>FTPS</code>, you must choose a certificate stored in Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.</p> </li> <li> <p>If <code>Protocol</code> includes either <code>FTP</code> or <code>FTPS</code>, then the <code>EndpointType</code> must be <code>VPC</code> and the <code>IdentityProviderType</code> must be either <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>FTP</code>, then <code>AddressAllocationIds</code> cannot be associated.</p> </li> <li> <p>If <code>Protocol</code> is set only to <code>SFTP</code>, the <code>EndpointType</code> can be set to <code>PUBLIC</code> and the <code>IdentityProviderType</code> can be set any of the supported identity types: <code>SERVICE_MANAGED</code>, <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>AS2</code>, then the <code>EndpointType</code> must be <code>VPC</code>, and domain must be Amazon S3.</p> </li> </ul> </note>
            security_policy_name: <p>Specifies the name of the security policy for the server.</p>
            server_id: <p>A system-assigned unique identifier for a server instance that the Transfer Family user is assigned to.</p>
            workflow_details: <p>Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.</p> <p>In addition to a workflow to execute when a file is uploaded completely, <code>WorkflowDetails</code> can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.</p> <p>To remove an associated workflow from a server, you can provide an empty <code>OnUpload</code> object, as in the following example.</p> <p> <code>aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{"OnUpload":[]}'</code> </p>
            structured_log_destinations: <p>Specifies the log groups to which your server logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:partition:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p> <p>If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an <code>update-server</code> call. For example:</p> <p> <code>update-server --server-id s-1234567890abcdef0 --structured-log-destinations</code> </p>
            s3_storage_options: <p>Specifies whether or not performance for your Amazon S3 directories is optimized.</p> <ul> <li> <p>If using the console, this is enabled by default.</p> </li> <li> <p>If using the API or CLI, this is disabled by default.</p> </li> </ul> <p>By default, home directory mappings have a <code>TYPE</code> of <code>DIRECTORY</code>. If you enable this option, you would then need to explicitly set the <code>HomeDirectoryMapEntry</code> <code>Type</code> to <code>FILE</code> if you want a mapping to have a file target.</p>
            ip_address_type: <p>Specifies whether to use IPv4 only, or to use dual-stack (IPv4 and IPv6) for your Transfer Family endpoint. The default value is <code>IPV4</code>.</p> <important> <p>The <code>IpAddressType</code> parameter has the following limitations:</p> <ul> <li> <p>It cannot be changed while the server is online. You must stop the server before modifying this parameter.</p> </li> <li> <p>It cannot be updated to <code>DUALSTACK</code> if the server has <code>AddressAllocationIds</code> specified.</p> </li> </ul> </important> <note> <p>When using <code>DUALSTACK</code> as the <code>IpAddressType</code>, you cannot set the <code>AddressAllocationIds</code> parameter for the <a href="https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html">EndpointDetails</a> for the server.</p> </note>
            identity_provider_type: <p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.conflict_exception.ConflictException: <p>This exception is thrown when the <code>UpdateServer</code> is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's <code>VpcEndpointID</code> is not in the available state.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_server_request.UpdateServerRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_server_response.UpdateServerResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_server

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_server.async_update_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.update_server_request.UpdateServerRequest = {
            "server_id": server_id
        }
        if certificate is not None:
            input_["certificate"] = certificate
        if protocol_details is not None:
            input_["protocol_details"] = protocol_details
        if endpoint_details is not None:
            input_["endpoint_details"] = endpoint_details
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
        if host_key is not None:
            input_["host_key"] = host_key
        if identity_provider_details is not None:
            input_["identity_provider_details"] = identity_provider_details
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if post_authentication_login_banner is not None:
            input_["post_authentication_login_banner"] = (
                post_authentication_login_banner
            )
        if pre_authentication_login_banner is not None:
            input_["pre_authentication_login_banner"] = pre_authentication_login_banner
        if protocols is not None:
            input_["protocols"] = protocols
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if workflow_details is not None:
            input_["workflow_details"] = workflow_details
        if structured_log_destinations is not None:
            input_["structured_log_destinations"] = structured_log_destinations
        if s3_storage_options is not None:
            input_["s3_storage_options"] = s3_storage_options
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if identity_provider_type is not None:
            input_["identity_provider_type"] = identity_provider_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_server(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the file transfer protocol-enabled server that you specify.</p> <p>No response returns from this operation.</p>

        Args:
            server_id: <p>A unique system-assigned identifier for a server instance.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_server_request.DeleteServerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_server

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_server.async_delete_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_server_request.DeleteServerRequest = {
            "server_id": server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_servers(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_servers_response.ListServersResponse":
        """<p>Lists the file transfer protocol-enabled servers that are associated with your Amazon Web Services account.</p>

        Args:
            max_results: <p>Specifies the number of servers to return as a response to the <code>ListServers</code> query.</p>
            next_token: <p>When additional results are obtained from the <code>ListServers</code> command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional servers.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_servers_request.ListServersRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_servers_response.ListServersResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_servers

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_servers.async_list_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_servers_request.ListServersRequest = {}
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

    async def iter_list_servers(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_server.ListedServer]":
        _token = next_token
        while True:
            _response = await self.list_servers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("servers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_user(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def describe_user(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def update_user(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def delete_user(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def list_users(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def iter_list_users(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_user.ListedUser]":
        _token = next_token
        while True:
            _response = await self.list_users(
                server_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_web_app_customization(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse":
        """<p>Describes the web app customization object that's identified by <code>WebAppId</code>.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_web_app_customization

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_web_app_customization.async_describe_web_app_customization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest = {
            "web_app_id": web_app_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_web_app_customization(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        title: Optional["capo_transfer.types.web_app_title.WebAppTitle"] = None,
        logo_file: Optional[
            "capo_transfer.types.web_app_logo_file.WebAppLogoFile"
        ] = None,
        favicon_file: Optional[
            "capo_transfer.types.web_app_favicon_file.WebAppFaviconFile"
        ] = None,
    ) -> "capo_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse":
        """<p>Assigns new customization properties to a web app. You can modify the icon file, logo file, and title.</p>

        Args:
            web_app_id: <p>Provide the identifier of the web app that you are updating.</p>
            title: <p>Provide an updated title.</p>
            logo_file: <p>Specify logo file data string (in base64 encoding).</p>
            favicon_file: <p>Specify an icon file data string (in base64 encoding).</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.conflict_exception.ConflictException: <p>This exception is thrown when the <code>UpdateServer</code> is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's <code>VpcEndpointID</code> is not in the available state.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_web_app_customization

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_web_app_customization.async_update_web_app_customization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest = {
            "web_app_id": web_app_id
        }
        if title is not None:
            input_["title"] = title
        if logo_file is not None:
            input_["logo_file"] = logo_file
        if favicon_file is not None:
            input_["favicon_file"] = favicon_file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_web_app_customization(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the <code>WebAppCustomization</code> object that corresponds to the web app ID specified.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app that contains the customizations that you are deleting.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.conflict_exception.ConflictException: <p>This exception is thrown when the <code>UpdateServer</code> is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's <code>VpcEndpointID</code> is not in the available state.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_web_app_customization

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_web_app_customization.async_delete_web_app_customization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest = {
            "web_app_id": web_app_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_web_app(
        self,
        identity_provider_details: "capo_transfer.types.web_app_identity_provider_details.WebAppIdentityProviderDetails",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        access_endpoint: Optional[
            "capo_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
        ] = None,
        web_app_units: Optional["capo_transfer.types.web_app_units.WebAppUnits"] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
        web_app_endpoint_policy: Optional[
            "capo_transfer.types.web_app_endpoint_policy.WebAppEndpointPolicy"
        ] = None,
        endpoint_details: Optional[
            "capo_transfer.types.web_app_endpoint_details.WebAppEndpointDetails"
        ] = None,
    ) -> "capo_transfer.types.create_web_app_response.CreateWebAppResponse":
        """<p>Creates a web app based on specified parameters, and returns the ID for the new web app. You can configure the web app to be publicly accessible or hosted within a VPC.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            identity_provider_details: <p>You can provide a structure that contains the details for the identity provider to use with your web app.</p> <p>For more details about this parameter, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/webapp-identity-center.html">Configure your identity provider for Transfer Family web apps</a>.</p>
            access_endpoint: <p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p> <p>Before you enter a custom URL for this parameter, follow the steps described in <a href="https://docs.aws.amazon.com/transfer/latest/userguide/webapp-customize.html">Update your access endpoint with a custom URL</a>.</p>
            web_app_units: <p>A union that contains the value for number of concurrent connections or the user sessions on your web app.</p>
            tags: <p>Key-value pairs that can be used to group and search for web apps.</p>
            web_app_endpoint_policy: <p> Setting for the type of endpoint policy for the web app. The default value is <code>STANDARD</code>. </p> <p>If you are creating the web app in an Amazon Web Services GovCloud (US) Region, you can set this parameter to <code>FIPS</code>.</p>
            endpoint_details: <p>The endpoint configuration for the web app. You can specify whether the web app endpoint is publicly accessible or hosted within a VPC.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_web_app_request.CreateWebAppRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_web_app_response.CreateWebAppResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_web_app

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_web_app.async_create_web_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.create_web_app_request.CreateWebAppRequest = {
            "identity_provider_details": identity_provider_details
        }
        if access_endpoint is not None:
            input_["access_endpoint"] = access_endpoint
        if web_app_units is not None:
            input_["web_app_units"] = web_app_units
        if tags is not None:
            input_["tags"] = tags
        if web_app_endpoint_policy is not None:
            input_["web_app_endpoint_policy"] = web_app_endpoint_policy
        if endpoint_details is not None:
            input_["endpoint_details"] = endpoint_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_web_app(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_web_app_response.DescribeWebAppResponse":
        """<p>Describes the web app that's identified by <code>WebAppId</code>. The response includes endpoint configuration details such as whether the web app is publicly accessible or VPC hosted.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_web_app_request.DescribeWebAppRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_web_app_response.DescribeWebAppResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_web_app

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_web_app.async_describe_web_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_web_app_request.DescribeWebAppRequest = {
            "web_app_id": web_app_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_web_app(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        identity_provider_details: Optional[
            "capo_transfer.types.update_web_app_identity_provider_details.UpdateWebAppIdentityProviderDetails"
        ] = None,
        access_endpoint: Optional[
            "capo_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
        ] = None,
        web_app_units: Optional["capo_transfer.types.web_app_units.WebAppUnits"] = None,
        endpoint_details: Optional[
            "capo_transfer.types.update_web_app_endpoint_details.UpdateWebAppEndpointDetails"
        ] = None,
    ) -> "capo_transfer.types.update_web_app_response.UpdateWebAppResponse":
        """<p>Assigns new properties to a web app. You can modify the access point, identity provider details, endpoint configuration, and the web app units.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            web_app_id: <p>Provide the identifier of the web app that you are updating.</p>
            identity_provider_details: <p>Provide updated identity provider values in a <code>WebAppIdentityProviderDetails</code> object.</p>
            access_endpoint: <p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p>
            web_app_units: <p>A union that contains the value for number of concurrent connections or the user sessions on your web app.</p>
            endpoint_details: <p>The updated endpoint configuration for the web app. You can modify the endpoint type and VPC configuration settings.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.conflict_exception.ConflictException: <p>This exception is thrown when the <code>UpdateServer</code> is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's <code>VpcEndpointID</code> is not in the available state.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_web_app_request.UpdateWebAppRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_web_app_response.UpdateWebAppResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_web_app

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_web_app.async_update_web_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.update_web_app_request.UpdateWebAppRequest = {
            "web_app_id": web_app_id
        }
        if identity_provider_details is not None:
            input_["identity_provider_details"] = identity_provider_details
        if access_endpoint is not None:
            input_["access_endpoint"] = access_endpoint
        if web_app_units is not None:
            input_["web_app_units"] = web_app_units
        if endpoint_details is not None:
            input_["endpoint_details"] = endpoint_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_web_app(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified web app.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app that you are deleting.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_web_app_request.DeleteWebAppRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_web_app

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_web_app.async_delete_web_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_web_app_request.DeleteWebAppRequest = {
            "web_app_id": web_app_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_web_apps(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_web_apps_response.ListWebAppsResponse":
        """<p>Lists all web apps associated with your Amazon Web Services account for your current region. The response includes the endpoint type for each web app, showing whether it is publicly accessible or VPC hosted.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>Returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional web apps.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_web_apps_request.ListWebAppsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_web_apps_response.ListWebAppsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_web_apps

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_web_apps.async_list_web_apps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_web_apps_request.ListWebAppsRequest = {}
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

    async def iter_list_web_apps(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_web_app.ListedWebApp]":
        _token = next_token
        while True:
            _response = await self.list_web_apps(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("web_apps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_workflow(
        self,
        steps: "capo_transfer.types.workflow_steps.WorkflowSteps",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        description: Optional[
            "capo_transfer.types.workflow_description.WorkflowDescription"
        ] = None,
        on_exception_steps: Optional[
            "capo_transfer.types.workflow_steps.WorkflowSteps"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
        structured_log_destinations: Optional[
            "capo_transfer.types.structured_log_destinations.StructuredLogDestinations"
        ] = None,
    ) -> "capo_transfer.types.create_workflow_response.CreateWorkflowResponse":
        """<p> Allows you to create a workflow with specified steps and step details the workflow invokes after file transfer completes. After creating a workflow, you can associate the workflow created with any transfer servers by specifying the <code>workflow-details</code> field in <code>CreateServer</code> and <code>UpdateServer</code> operations. </p>

        Args:
            description: <p>A textual description for the workflow.</p>
            steps: <p>Specifies the details for the steps that are in the specified workflow.</p> <p> The <code>TYPE</code> specifies which of the following actions is being taken for this step. </p> <ul> <li> <p> <b> <code>COPY</code> </b> - Copy the file to another location.</p> </li> <li> <p> <b> <code>CUSTOM</code> </b> - Perform a custom step with an Lambda function target.</p> </li> <li> <p> <b> <code>DECRYPT</code> </b> - Decrypt a file that was encrypted before it was uploaded.</p> </li> <li> <p> <b> <code>DELETE</code> </b> - Delete the file.</p> </li> <li> <p> <b> <code>TAG</code> </b> - Add a tag to the file.</p> </li> </ul> <note> <p> Currently, copying and tagging are supported only on S3. </p> </note> <p> For file location, you specify either the Amazon S3 bucket and key, or the Amazon EFS file system ID and path. </p>
            on_exception_steps: <p>Specifies the steps (actions) to take if errors are encountered during execution of the workflow.</p> <note> <p>For custom steps, the Lambda function needs to send <code>FAILURE</code> to the call back API to kick off the exception steps. Additionally, if the Lambda does not send <code>SUCCESS</code> before it times out, the exception steps are executed.</p> </note>
            tags: <p>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</p>
            structured_log_destinations: <p>Specifies the log groups to which your workflow logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:partition:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_workflow

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_workflow.async_create_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.create_workflow_request.CreateWorkflowRequest = {
            "steps": steps
        }
        if description is not None:
            input_["description"] = description
        if on_exception_steps is not None:
            input_["on_exception_steps"] = on_exception_steps
        if tags is not None:
            input_["tags"] = tags
        if structured_log_destinations is not None:
            input_["structured_log_destinations"] = structured_log_destinations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_workflow(
        self,
        workflow_id: "capo_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_workflow_response.DescribeWorkflowResponse":
        """<p>Describes the specified workflow.</p>

        Args:
            workflow_id: <p>A unique identifier for the workflow.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_workflow_request.DescribeWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_workflow_response.DescribeWorkflowResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_workflow

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_workflow.async_describe_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.describe_workflow_request.DescribeWorkflowRequest = {
            "workflow_id": workflow_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workflow(
        self,
        workflow_id: "capo_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified workflow.</p>

        Args:
            workflow_id: <p>A unique identifier for the workflow.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_workflow

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_workflow.async_delete_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.delete_workflow_request.DeleteWorkflowRequest = {
            "workflow_id": workflow_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workflows(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Lists all workflows associated with your Amazon Web Services account for your current region.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p> <code>ListWorkflows</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional workflows.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_workflows

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_workflows.async_list_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transfer.types.list_workflows_request.ListWorkflowsRequest = {}
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

    async def iter_list_workflows(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_transfer.types.listed_workflow.ListedWorkflow]":
        _token = next_token
        while True:
            _response = await self.list_workflows(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workflows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
