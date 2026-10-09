"""Generated from Smithy shape ``com.amazonaws.datasync#FmrsService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_datasync._auth._signers
import capo_datasync._auth._sigv4
from capo_datasync._auth._identity import Credentials
from capo_datasync._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_datasync._auth._zapros_handler import AuthMiddleware
from capo_datasync._pagination import resolve_path as _resolve_path
from capo_datasync._services._aws_config import aws_config
from capo_datasync._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_datasync.types.activation_key
    import capo_datasync.types.agent_arn
    import capo_datasync.types.agent_arn_list
    import capo_datasync.types.agent_list_entry
    import capo_datasync.types.azure_access_tier
    import capo_datasync.types.azure_blob_authentication_type
    import capo_datasync.types.azure_blob_container_url
    import capo_datasync.types.azure_blob_sas_configuration
    import capo_datasync.types.azure_blob_subdirectory
    import capo_datasync.types.azure_blob_type
    import capo_datasync.types.cancel_task_execution_request
    import capo_datasync.types.cancel_task_execution_response
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.create_agent_request
    import capo_datasync.types.create_agent_response
    import capo_datasync.types.create_location_azure_blob_request
    import capo_datasync.types.create_location_azure_blob_response
    import capo_datasync.types.create_location_efs_request
    import capo_datasync.types.create_location_efs_response
    import capo_datasync.types.create_location_fsx_lustre_request
    import capo_datasync.types.create_location_fsx_lustre_response
    import capo_datasync.types.create_location_fsx_ontap_request
    import capo_datasync.types.create_location_fsx_ontap_response
    import capo_datasync.types.create_location_fsx_open_zfs_request
    import capo_datasync.types.create_location_fsx_open_zfs_response
    import capo_datasync.types.create_location_fsx_windows_request
    import capo_datasync.types.create_location_fsx_windows_response
    import capo_datasync.types.create_location_hdfs_request
    import capo_datasync.types.create_location_hdfs_response
    import capo_datasync.types.create_location_nfs_request
    import capo_datasync.types.create_location_nfs_response
    import capo_datasync.types.create_location_object_storage_request
    import capo_datasync.types.create_location_object_storage_response
    import capo_datasync.types.create_location_s3_request
    import capo_datasync.types.create_location_s3_response
    import capo_datasync.types.create_location_smb_request
    import capo_datasync.types.create_location_smb_response
    import capo_datasync.types.create_task_request
    import capo_datasync.types.create_task_response
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.delete_agent_request
    import capo_datasync.types.delete_agent_response
    import capo_datasync.types.delete_location_request
    import capo_datasync.types.delete_location_response
    import capo_datasync.types.delete_task_request
    import capo_datasync.types.delete_task_response
    import capo_datasync.types.describe_agent_request
    import capo_datasync.types.describe_agent_response
    import capo_datasync.types.describe_location_azure_blob_request
    import capo_datasync.types.describe_location_azure_blob_response
    import capo_datasync.types.describe_location_efs_request
    import capo_datasync.types.describe_location_efs_response
    import capo_datasync.types.describe_location_fsx_lustre_request
    import capo_datasync.types.describe_location_fsx_lustre_response
    import capo_datasync.types.describe_location_fsx_ontap_request
    import capo_datasync.types.describe_location_fsx_ontap_response
    import capo_datasync.types.describe_location_fsx_open_zfs_request
    import capo_datasync.types.describe_location_fsx_open_zfs_response
    import capo_datasync.types.describe_location_fsx_windows_request
    import capo_datasync.types.describe_location_fsx_windows_response
    import capo_datasync.types.describe_location_hdfs_request
    import capo_datasync.types.describe_location_hdfs_response
    import capo_datasync.types.describe_location_nfs_request
    import capo_datasync.types.describe_location_nfs_response
    import capo_datasync.types.describe_location_object_storage_request
    import capo_datasync.types.describe_location_object_storage_response
    import capo_datasync.types.describe_location_s3_request
    import capo_datasync.types.describe_location_s3_response
    import capo_datasync.types.describe_location_smb_request
    import capo_datasync.types.describe_location_smb_response
    import capo_datasync.types.describe_task_execution_request
    import capo_datasync.types.describe_task_execution_response
    import capo_datasync.types.describe_task_request
    import capo_datasync.types.describe_task_response
    import capo_datasync.types.dns_ip_list
    import capo_datasync.types.ec2_config
    import capo_datasync.types.ec2_security_group_arn_list
    import capo_datasync.types.efs_access_point_arn
    import capo_datasync.types.efs_filesystem_arn
    import capo_datasync.types.efs_in_transit_encryption
    import capo_datasync.types.efs_subdirectory
    import capo_datasync.types.filter_list
    import capo_datasync.types.fsx_filesystem_arn
    import capo_datasync.types.fsx_lustre_subdirectory
    import capo_datasync.types.fsx_ontap_subdirectory
    import capo_datasync.types.fsx_open_zfs_subdirectory
    import capo_datasync.types.fsx_protocol
    import capo_datasync.types.fsx_update_protocol
    import capo_datasync.types.fsx_windows_subdirectory
    import capo_datasync.types.hdfs_authentication_type
    import capo_datasync.types.hdfs_block_size
    import capo_datasync.types.hdfs_name_node_list
    import capo_datasync.types.hdfs_replication_factor
    import capo_datasync.types.hdfs_subdirectory
    import capo_datasync.types.hdfs_user
    import capo_datasync.types.iam_role_arn
    import capo_datasync.types.input_tag_list
    import capo_datasync.types.kerberos_keytab_file
    import capo_datasync.types.kerberos_krb5_conf_file
    import capo_datasync.types.kerberos_principal
    import capo_datasync.types.kms_key_provider_uri
    import capo_datasync.types.list_agents_request
    import capo_datasync.types.list_agents_response
    import capo_datasync.types.list_locations_request
    import capo_datasync.types.list_locations_response
    import capo_datasync.types.list_tags_for_resource_request
    import capo_datasync.types.list_tags_for_resource_response
    import capo_datasync.types.list_task_executions_request
    import capo_datasync.types.list_task_executions_response
    import capo_datasync.types.list_tasks_request
    import capo_datasync.types.list_tasks_response
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_filters
    import capo_datasync.types.location_list_entry
    import capo_datasync.types.log_group_arn
    import capo_datasync.types.manifest_config
    import capo_datasync.types.max_results
    import capo_datasync.types.next_token
    import capo_datasync.types.nfs_mount_options
    import capo_datasync.types.nfs_subdirectory
    import capo_datasync.types.object_storage_access_key
    import capo_datasync.types.object_storage_bucket_name
    import capo_datasync.types.object_storage_certificate
    import capo_datasync.types.object_storage_secret_key
    import capo_datasync.types.object_storage_server_port
    import capo_datasync.types.object_storage_server_protocol
    import capo_datasync.types.on_prem_config
    import capo_datasync.types.options
    import capo_datasync.types.pl_security_group_arn_list
    import capo_datasync.types.pl_subnet_arn_list
    import capo_datasync.types.qop_configuration
    import capo_datasync.types.s3_bucket_arn
    import capo_datasync.types.s3_config
    import capo_datasync.types.s3_storage_class
    import capo_datasync.types.s3_subdirectory
    import capo_datasync.types.server_hostname
    import capo_datasync.types.smb_authentication_type
    import capo_datasync.types.smb_domain
    import capo_datasync.types.smb_mount_options
    import capo_datasync.types.smb_password
    import capo_datasync.types.smb_subdirectory
    import capo_datasync.types.smb_user
    import capo_datasync.types.start_task_execution_request
    import capo_datasync.types.start_task_execution_response
    import capo_datasync.types.storage_virtual_machine_arn
    import capo_datasync.types.tag_key_list
    import capo_datasync.types.tag_list_entry
    import capo_datasync.types.tag_resource_request
    import capo_datasync.types.tag_resource_response
    import capo_datasync.types.tag_value
    import capo_datasync.types.taggable_resource_arn
    import capo_datasync.types.task_arn
    import capo_datasync.types.task_execution_arn
    import capo_datasync.types.task_execution_list_entry
    import capo_datasync.types.task_filters
    import capo_datasync.types.task_list_entry
    import capo_datasync.types.task_mode
    import capo_datasync.types.task_report_config
    import capo_datasync.types.task_schedule
    import capo_datasync.types.untag_resource_request
    import capo_datasync.types.untag_resource_response
    import capo_datasync.types.update_agent_request
    import capo_datasync.types.update_agent_response
    import capo_datasync.types.update_location_azure_blob_request
    import capo_datasync.types.update_location_azure_blob_response
    import capo_datasync.types.update_location_efs_request
    import capo_datasync.types.update_location_efs_response
    import capo_datasync.types.update_location_fsx_lustre_request
    import capo_datasync.types.update_location_fsx_lustre_response
    import capo_datasync.types.update_location_fsx_ontap_request
    import capo_datasync.types.update_location_fsx_ontap_response
    import capo_datasync.types.update_location_fsx_open_zfs_request
    import capo_datasync.types.update_location_fsx_open_zfs_response
    import capo_datasync.types.update_location_fsx_windows_request
    import capo_datasync.types.update_location_fsx_windows_response
    import capo_datasync.types.update_location_hdfs_request
    import capo_datasync.types.update_location_hdfs_response
    import capo_datasync.types.update_location_nfs_request
    import capo_datasync.types.update_location_nfs_response
    import capo_datasync.types.update_location_object_storage_request
    import capo_datasync.types.update_location_object_storage_response
    import capo_datasync.types.update_location_s3_request
    import capo_datasync.types.update_location_s3_response
    import capo_datasync.types.update_location_smb_request
    import capo_datasync.types.update_location_smb_response
    import capo_datasync.types.update_smb_domain
    import capo_datasync.types.update_task_execution_request
    import capo_datasync.types.update_task_execution_response
    import capo_datasync.types.update_task_request
    import capo_datasync.types.update_task_response
    import capo_datasync.types.updated_efs_access_point_arn
    import capo_datasync.types.updated_efs_iam_role_arn
    import capo_datasync.types.vpc_endpoint_id


class DataSyncClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class DataSyncClient:
    """A client for the ``DataSync`` service.

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
        self._config = DataSyncClientConfig(
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
        self, config_overrides: Optional[DataSyncClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DataSyncClientConfig = config_overrides or {}
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

    def cancel_task_execution(
        self,
        task_execution_arn: "capo_datasync.types.task_execution_arn.TaskExecutionArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> (
        "capo_datasync.types.cancel_task_execution_response.CancelTaskExecutionResponse"
    ):
        """<p>Stops an DataSync task execution that's in progress. The transfer of some files are abruptly interrupted. File contents that're transferred to the destination might be incomplete or inconsistent with the source files.</p> <p>However, if you start a new task execution using the same task and allow it to finish, file content on the destination will be complete and consistent. This applies to other unexpected failures that interrupt a task execution. In all of these cases, DataSync successfully completes the transfer when you start the next task execution.</p>

        Args:
            task_execution_arn: <p>The Amazon Resource Name (ARN) of the task execution to stop.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.cancel_task_execution_request.CancelTaskExecutionRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.cancel_task_execution_response.CancelTaskExecutionResponse"
        ]:
            import capo_datasync._operations.fmrs_service.cancel_task_execution

            output, http_response = (
                capo_datasync._operations.fmrs_service.cancel_task_execution.cancel_task_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.cancel_task_execution_request.CancelTaskExecutionRequest = {
            "task_execution_arn": task_execution_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_agent(
        self,
        activation_key: "capo_datasync.types.activation_key.ActivationKey",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        agent_name: Optional["capo_datasync.types.tag_value.TagValue"] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
        vpc_endpoint_id: Optional[
            "capo_datasync.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        subnet_arns: Optional[
            "capo_datasync.types.pl_subnet_arn_list.PLSubnetArnList"
        ] = None,
        security_group_arns: Optional[
            "capo_datasync.types.pl_security_group_arn_list.PLSecurityGroupArnList"
        ] = None,
    ) -> "capo_datasync.types.create_agent_response.CreateAgentResponse":
        """<p>Activates an DataSync agent that you deploy in your storage environment. The activation process associates the agent with your Amazon Web Services account.</p> <p>If you haven't deployed an agent yet, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html">Do I need a DataSync agent?</a> </p>

        Args:
            activation_key: <p>Specifies your DataSync agent's activation key. If you don't have an activation key, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html">Activating your agent</a>.</p>
            agent_name: <p>Specifies a name for your agent. We recommend specifying a name that you can remember.</p>
            tags: <p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least one tag for your agent.</p>
            vpc_endpoint_id: <p>Specifies the ID of the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#datasync-in-vpc">VPC service endpoint</a> that you're using. For example, a VPC endpoint ID looks like <code>vpce-01234d5aff67890e1</code>.</p> <important> <p>The VPC service endpoint you use must include the DataSync service name (for example, <code>com.amazonaws.us-east-2.datasync</code>).</p> </important>
            subnet_arns: <p>Specifies the ARN of the subnet where your VPC service endpoint is located. You can only specify one ARN.</p>
            security_group_arns: <p>Specifies the Amazon Resource Name (ARN) of the security group that allows traffic between your agent and VPC service endpoint. You can only specify one ARN.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_agent_request.CreateAgentRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_agent_response.CreateAgentResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_agent

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_agent.create_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_agent_request.CreateAgentRequest = {
            "activation_key": activation_key
        }
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if tags is not None:
            input_["tags"] = tags
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if subnet_arns is not None:
            input_["subnet_arns"] = subnet_arns
        if security_group_arns is not None:
            input_["security_group_arns"] = security_group_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_azure_blob(
        self,
        container_url: "capo_datasync.types.azure_blob_container_url.AzureBlobContainerUrl",
        authentication_type: "capo_datasync.types.azure_blob_authentication_type.AzureBlobAuthenticationType",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        sas_configuration: Optional[
            "capo_datasync.types.azure_blob_sas_configuration.AzureBlobSasConfiguration"
        ] = None,
        blob_type: Optional["capo_datasync.types.azure_blob_type.AzureBlobType"] = None,
        access_tier: Optional[
            "capo_datasync.types.azure_access_tier.AzureAccessTier"
        ] = None,
        subdirectory: Optional[
            "capo_datasync.types.azure_blob_subdirectory.AzureBlobSubdirectory"
        ] = None,
        agent_arns: Optional["capo_datasync.types.agent_arn_list.AgentArnList"] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
    ) -> "capo_datasync.types.create_location_azure_blob_response.CreateLocationAzureBlobResponse":
        """<p>Creates a transfer <i>location</i> for a Microsoft Azure Blob Storage container. DataSync can use this location as a transfer source or destination. You can make transfers with or without a <a href="https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-creating-agent">DataSync agent</a> that connects to your container.</p> <p>Before you begin, make sure you know <a href="https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access">how DataSync accesses Azure Blob Storage</a> and works with <a href="https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers">access tiers</a> and <a href="https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#blob-types">blob types</a>.</p>

        Args:
            container_url: <p>Specifies the URL of the Azure Blob Storage container involved in your transfer.</p>
            authentication_type: <p>Specifies the authentication method DataSync uses to access your Azure Blob Storage. DataSync can access blob storage using a shared access signature (SAS).</p>
            sas_configuration: <p>Specifies the SAS configuration that allows DataSync to access your Azure Blob Storage.</p> <note> <p>If you provide an authentication token using <code>SasConfiguration</code>, but do not provide secret configuration details using <code>CmkSecretConfig</code> or <code>CustomSecretConfig</code>, then DataSync stores the token using your Amazon Web Services account's secrets manager secret.</p> </note>
            blob_type: <p>Specifies the type of blob that you want your objects or files to be when transferring them into Azure Blob Storage. Currently, DataSync only supports moving data into Azure Blob Storage as block blobs. For more information on blob types, see the <a href="https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs">Azure Blob Storage documentation</a>.</p>
            access_tier: <p>Specifies the access tier that you want your objects or files transferred into. This only applies when using the location as a transfer destination. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers">Access tiers</a>.</p>
            subdirectory: <p>Specifies path segments if you want to limit your transfer to a virtual directory in your container (for example, <code>/my/images</code>).</p>
            agent_arns: <p>(Optional) Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect with your Azure Blob Storage container. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.</p> <p>You can specify more than one agent. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html">Using multiple agents for your transfer</a>.</p> <note> <p>Make sure you configure this parameter correctly when you first create your storage location. You cannot add or remove agents from a storage location after you create it.</p> </note>
            tags: <p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your transfer location.</p>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, which includes the authentication token that DataSync uses to access a specific AzureBlob storage location, with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationAzureBlob</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with the authentication token you specify for <code>SasConfiguration</code> to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>SasConfiguration</code>) or <code>CustomSecretConfig</code> (without <code>SasConfiguration</code>) to provide credentials for a <code>CreateLocationAzureBlob</code> request. Do not provide both parameters for the same request.</p> </note>
            custom_secret_config: <p>Specifies configuration information for a customer-managed Secrets Manager secret where the authentication token for an AzureBlob storage location is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>SasConfiguration</code>) or <code>CustomSecretConfig</code> (without <code>SasConfiguration</code>) to provide credentials for a <code>CreateLocationAzureBlob</code> request. Do not provide both parameters for the same request.</p> </note>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_azure_blob_request.CreateLocationAzureBlobRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_azure_blob_response.CreateLocationAzureBlobResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_azure_blob

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_azure_blob.create_location_azure_blob(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_azure_blob_request.CreateLocationAzureBlobRequest = {
            "container_url": container_url,
            "authentication_type": authentication_type,
        }
        if sas_configuration is not None:
            input_["sas_configuration"] = sas_configuration
        if blob_type is not None:
            input_["blob_type"] = blob_type
        if access_tier is not None:
            input_["access_tier"] = access_tier
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if agent_arns is not None:
            input_["agent_arns"] = agent_arns
        if tags is not None:
            input_["tags"] = tags
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_efs(
        self,
        efs_filesystem_arn: "capo_datasync.types.efs_filesystem_arn.EfsFilesystemArn",
        ec2_config: "capo_datasync.types.ec2_config.Ec2Config",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.efs_subdirectory.EfsSubdirectory"
        ] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
        access_point_arn: Optional[
            "capo_datasync.types.efs_access_point_arn.EfsAccessPointArn"
        ] = None,
        file_system_access_role_arn: Optional[
            "capo_datasync.types.iam_role_arn.IamRoleArn"
        ] = None,
        in_transit_encryption: Optional[
            "capo_datasync.types.efs_in_transit_encryption.EfsInTransitEncryption"
        ] = None,
    ) -> "capo_datasync.types.create_location_efs_response.CreateLocationEfsResponse":
        """<p>Creates a transfer <i>location</i> for an Amazon EFS file system. DataSync can use this location as a source or destination for transferring data.</p> <p>Before you begin, make sure that you understand how DataSync <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-access">accesses Amazon EFS file systems</a>.</p>

        Args:
            subdirectory: <p>Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data on your file system (depending on if this is a source or destination location).</p> <p>By default, DataSync uses the root directory (or <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html">access point</a> if you provide one by using <code>AccessPointArn</code>). You can also include subdirectories using forward slashes (for example, <code>/path/to/folder</code>).</p>
            efs_filesystem_arn: <p>Specifies the ARN for your Amazon EFS file system.</p>
            ec2_config: <p>Specifies the subnet and security groups DataSync uses to connect to one of your Amazon EFS file system's <a href="https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html">mount targets</a>.</p>
            tags: <p>Specifies the key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.</p>
            access_point_arn: <p>Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to mount your Amazon EFS file system.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam">Accessing restricted file systems</a>.</p>
            file_system_access_role_arn: <p>Specifies an Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.</p> <p>For information on creating this role, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam-role">Creating a DataSync IAM role for file system access</a>.</p>
            in_transit_encryption: <p>Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it transfers data to or from your Amazon EFS file system.</p> <p>If you specify an access point using <code>AccessPointArn</code> or an IAM role using <code>FileSystemAccessRoleArn</code>, you must set this parameter to <code>TLS1_2</code>.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_efs_request.CreateLocationEfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_efs_response.CreateLocationEfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_efs

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_efs.create_location_efs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_efs_request.CreateLocationEfsRequest = {
            "efs_filesystem_arn": efs_filesystem_arn,
            "ec2_config": ec2_config,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if tags is not None:
            input_["tags"] = tags
        if access_point_arn is not None:
            input_["access_point_arn"] = access_point_arn
        if file_system_access_role_arn is not None:
            input_["file_system_access_role_arn"] = file_system_access_role_arn
        if in_transit_encryption is not None:
            input_["in_transit_encryption"] = in_transit_encryption

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_fsx_lustre(
        self,
        fsx_filesystem_arn: "capo_datasync.types.fsx_filesystem_arn.FsxFilesystemArn",
        security_group_arns: "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.fsx_lustre_subdirectory.FsxLustreSubdirectory"
        ] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
    ) -> "capo_datasync.types.create_location_fsx_lustre_response.CreateLocationFsxLustreResponse":
        """<p>Creates a transfer <i>location</i> for an Amazon FSx for Lustre file system. DataSync can use this location as a source or destination for transferring data.</p> <p>Before you begin, make sure that you understand how DataSync <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-lustre-location.html#create-lustre-location-access">accesses FSx for Lustre file systems</a>.</p>

        Args:
            fsx_filesystem_arn: <p>Specifies the Amazon Resource Name (ARN) of the FSx for Lustre file system.</p>
            security_group_arns: <p>Specifies the Amazon Resource Names (ARNs) of up to five security groups that provide access to your FSx for Lustre file system.</p> <p>The security groups must be able to access the file system's ports. The file system must also allow access from the security groups. For information about file system access, see the <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/limit-access-security-groups.html"> <i>Amazon FSx for Lustre User Guide</i> </a>.</p>
            subdirectory: <p>Specifies a mount path for your FSx for Lustre file system. The path can include subdirectories.</p> <p>When the location is used as a source, DataSync reads data from the mount path. When the location is used as a destination, DataSync writes data to the mount path. If you don't include this parameter, DataSync uses the file system's root directory (<code>/</code>).</p>
            tags: <p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_fsx_lustre_request.CreateLocationFsxLustreRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_fsx_lustre_response.CreateLocationFsxLustreResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_fsx_lustre

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_fsx_lustre.create_location_fsx_lustre(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_fsx_lustre_request.CreateLocationFsxLustreRequest = {
            "fsx_filesystem_arn": fsx_filesystem_arn,
            "security_group_arns": security_group_arns,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_fsx_ontap(
        self,
        protocol: "capo_datasync.types.fsx_protocol.FsxProtocol",
        security_group_arns: "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList",
        storage_virtual_machine_arn: "capo_datasync.types.storage_virtual_machine_arn.StorageVirtualMachineArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.fsx_ontap_subdirectory.FsxOntapSubdirectory"
        ] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
    ) -> "capo_datasync.types.create_location_fsx_ontap_response.CreateLocationFsxOntapResponse":
        """<p>Creates a transfer <i>location</i> for an Amazon FSx for NetApp ONTAP file system. DataSync can use this location as a source or destination for transferring data.</p> <p>Before you begin, make sure that you understand how DataSync <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-access">accesses FSx for ONTAP file systems</a>.</p>

        Args:
            security_group_arns: <p>Specifies the Amazon EC2 security groups that provide access to your file system's preferred subnet.</p> <p>The security groups must allow outbound traffic on the following ports (depending on the protocol you use):</p> <ul> <li> <p> <b>Network File System (NFS)</b>: TCP ports 111, 635, and 2049</p> </li> <li> <p> <b>Server Message Block (SMB)</b>: TCP port 445</p> </li> </ul> <p>Your file system's security groups must also allow inbound traffic on the same ports.</p>
            storage_virtual_machine_arn: <p>Specifies the ARN of the storage virtual machine (SVM) in your file system where you want to copy data to or from.</p>
            subdirectory: <p>Specifies a path to the file share in the SVM where you want to transfer data to or from.</p> <p>You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be <code>/vol1</code>, <code>/vol1/tree1</code>, or <code>/share1</code>.</p> <note> <p>Don't specify a junction path in the SVM's root volume. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html">Managing FSx for ONTAP storage virtual machines</a> in the <i>Amazon FSx for NetApp ONTAP User Guide</i>.</p> </note>
            tags: <p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_fsx_ontap_request.CreateLocationFsxOntapRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_fsx_ontap_response.CreateLocationFsxOntapResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_fsx_ontap

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_fsx_ontap.create_location_fsx_ontap(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_fsx_ontap_request.CreateLocationFsxOntapRequest = {
            "protocol": protocol,
            "security_group_arns": security_group_arns,
            "storage_virtual_machine_arn": storage_virtual_machine_arn,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_fsx_open_zfs(
        self,
        fsx_filesystem_arn: "capo_datasync.types.fsx_filesystem_arn.FsxFilesystemArn",
        protocol: "capo_datasync.types.fsx_protocol.FsxProtocol",
        security_group_arns: "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.fsx_open_zfs_subdirectory.FsxOpenZfsSubdirectory"
        ] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
    ) -> "capo_datasync.types.create_location_fsx_open_zfs_response.CreateLocationFsxOpenZfsResponse":
        """<p>Creates a transfer <i>location</i> for an Amazon FSx for OpenZFS file system. DataSync can use this location as a source or destination for transferring data.</p> <p>Before you begin, make sure that you understand how DataSync <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-openzfs-location.html#create-openzfs-access">accesses FSx for OpenZFS file systems</a>.</p> <note> <p>Request parameters related to <code>SMB</code> aren't supported with the <code>CreateLocationFsxOpenZfs</code> operation.</p> </note>

        Args:
            fsx_filesystem_arn: <p>The Amazon Resource Name (ARN) of the FSx for OpenZFS file system.</p>
            protocol: <p>The type of protocol that DataSync uses to access your file system.</p>
            security_group_arns: <p>The ARNs of the security groups that are used to configure the FSx for OpenZFS file system.</p>
            subdirectory: <p>A subdirectory in the location's path that must begin with <code>/fsx</code>. DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).</p>
            tags: <p>The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_fsx_open_zfs_request.CreateLocationFsxOpenZfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_fsx_open_zfs_response.CreateLocationFsxOpenZfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_fsx_open_zfs

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_fsx_open_zfs.create_location_fsx_open_zfs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_fsx_open_zfs_request.CreateLocationFsxOpenZfsRequest = {
            "fsx_filesystem_arn": fsx_filesystem_arn,
            "protocol": protocol,
            "security_group_arns": security_group_arns,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_fsx_windows(
        self,
        fsx_filesystem_arn: "capo_datasync.types.fsx_filesystem_arn.FsxFilesystemArn",
        security_group_arns: "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList",
        user: "capo_datasync.types.smb_user.SmbUser",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.fsx_windows_subdirectory.FsxWindowsSubdirectory"
        ] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
        domain: Optional["capo_datasync.types.smb_domain.SmbDomain"] = None,
        password: Optional["capo_datasync.types.smb_password.SmbPassword"] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
    ) -> "capo_datasync.types.create_location_fsx_windows_response.CreateLocationFsxWindowsResponse":
        """<p>Creates a transfer <i>location</i> for an Amazon FSx for Windows File Server file system. DataSync can use this location as a source or destination for transferring data.</p> <p>Before you begin, make sure that you understand how DataSync <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#create-fsx-location-access">accesses FSx for Windows File Server file systems</a>.</p>

        Args:
            subdirectory: <p>Specifies a mount path for your file system using forward slashes. This is where DataSync reads or writes data (depending on if this is a source or destination location).</p>
            fsx_filesystem_arn: <p>Specifies the Amazon Resource Name (ARN) for the FSx for Windows File Server file system.</p>
            security_group_arns: <p>Specifies the ARNs of the Amazon EC2 security groups that provide access to your file system's preferred subnet.</p> <p>The security groups that you specify must be able to communicate with your file system's security groups. For information about configuring security groups for file system access, see the <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html"> <i>Amazon FSx for Windows File Server User Guide</i> </a>.</p> <note> <p>If you choose a security group that doesn't allow connections from within itself, do one of the following:</p> <ul> <li> <p>Configure the security group to allow it to communicate within itself.</p> </li> <li> <p>Choose a different security group that can communicate with the mount target's security group.</p> </li> </ul> </note>
            tags: <p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>
            user: <p>Specifies the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.</p> <p>For information about choosing a user with the right level of access for your transfer, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#create-fsx-windows-location-permissions">required permissions</a> for FSx for Windows File Server locations.</p>
            domain: <p>Specifies the name of the Windows domain that the FSx for Windows File Server file system belongs to.</p> <p>If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file system.</p>
            password: <p>Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.</p>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, which includes the password that DataSync uses to access a specific FSx Windows storage location, with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationFsxWindows</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with the <code>Password</code> you specify for to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>Password</code>) or <code>CustomSecretConfig</code> (without <code>Password</code>) to provide credentials for a <code>CreateLocationFsxWindows</code> request. Do not provide both parameters for the same request.</p> </note>
            custom_secret_config: <p>Specifies configuration information for a customer-managed Secrets Manager secret where the password for an FSx for Windows File Server storage location is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>Password</code>) or <code>CustomSecretConfig</code> (without <code>Password</code>) to provide credentials for a <code>CreateLocationFsxWindows</code> request. Do not provide both parameters for the same request.</p> </note>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_fsx_windows_request.CreateLocationFsxWindowsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_fsx_windows_response.CreateLocationFsxWindowsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_fsx_windows

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_fsx_windows.create_location_fsx_windows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_fsx_windows_request.CreateLocationFsxWindowsRequest = {
            "fsx_filesystem_arn": fsx_filesystem_arn,
            "security_group_arns": security_group_arns,
            "user": user,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if tags is not None:
            input_["tags"] = tags
        if domain is not None:
            input_["domain"] = domain
        if password is not None:
            input_["password"] = password
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_hdfs(
        self,
        name_nodes: "capo_datasync.types.hdfs_name_node_list.HdfsNameNodeList",
        authentication_type: "capo_datasync.types.hdfs_authentication_type.HdfsAuthenticationType",
        agent_arns: "capo_datasync.types.agent_arn_list.AgentArnList",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.hdfs_subdirectory.HdfsSubdirectory"
        ] = None,
        block_size: Optional[
            "capo_datasync.types.hdfs_block_size.HdfsBlockSize"
        ] = None,
        replication_factor: Optional[
            "capo_datasync.types.hdfs_replication_factor.HdfsReplicationFactor"
        ] = None,
        kms_key_provider_uri: Optional[
            "capo_datasync.types.kms_key_provider_uri.KmsKeyProviderUri"
        ] = None,
        qop_configuration: Optional[
            "capo_datasync.types.qop_configuration.QopConfiguration"
        ] = None,
        simple_user: Optional["capo_datasync.types.hdfs_user.HdfsUser"] = None,
        kerberos_principal: Optional[
            "capo_datasync.types.kerberos_principal.KerberosPrincipal"
        ] = None,
        kerberos_keytab: Optional[
            "capo_datasync.types.kerberos_keytab_file.KerberosKeytabFile"
        ] = None,
        kerberos_krb5_conf: Optional[
            "capo_datasync.types.kerberos_krb5_conf_file.KerberosKrb5ConfFile"
        ] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
    ) -> "capo_datasync.types.create_location_hdfs_response.CreateLocationHdfsResponse":
        """<p>Creates a transfer <i>location</i> for a Hadoop Distributed File System (HDFS). DataSync can use this location as a source or destination for transferring data.</p> <p>Before you begin, make sure that you understand how DataSync <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-hdfs-location.html#accessing-hdfs">accesses HDFS clusters</a>.</p>

        Args:
            subdirectory: <p>A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write data to the HDFS cluster. If the subdirectory isn't specified, it will default to <code>/</code>.</p>
            name_nodes: <p>The NameNode that manages the HDFS namespace. The NameNode performs operations such as opening, closing, and renaming files and directories. The NameNode contains the information to map blocks of data to the DataNodes.</p> <p>The number of NameNodes you can specify depends on the task mode:</p> <ul> <li> <p> <b>Enhanced mode</b> – You can specify multiple NameNodes for HDFS High Availability (HA) configurations.</p> </li> <li> <p> <b>Basic mode</b> – You can specify only one NameNode.</p> </li> </ul>
            block_size: <p>The size of data blocks to write into the HDFS cluster. The block size must be a multiple of 512 bytes. The default block size is 128 mebibytes (MiB).</p>
            replication_factor: <p>The number of DataNodes to replicate the data to when writing to the HDFS cluster. By default, data is replicated to three DataNodes.</p>
            kms_key_provider_uri: <p>The URI of the HDFS cluster's Key Management Server (KMS). </p>
            qop_configuration: <p>The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the Hadoop Distributed File System (HDFS) cluster. If <code>QopConfiguration</code> isn't specified, <code>RpcProtection</code> and <code>DataTransferProtection</code> default to <code>PRIVACY</code>. If you set <code>RpcProtection</code> or <code>DataTransferProtection</code>, the other parameter assumes the same value. </p>
            authentication_type: <p>The type of authentication used to determine the identity of the user. </p>
            simple_user: <p>The user name used to identify the client on the host operating system. </p> <note> <p>If <code>SIMPLE</code> is specified for <code>AuthenticationType</code>, this parameter is required. </p> </note>
            kerberos_principal: <p>The Kerberos principal with access to the files and folders on the HDFS cluster. </p> <note> <p>If <code>KERBEROS</code> is specified for <code>AuthenticationType</code>, this parameter is required.</p> </note>
            kerberos_keytab: <p>The Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and the encrypted keys. You can load the keytab from a file by providing the file's address.</p> <note> <p>If <code>KERBEROS</code> is specified for <code>AuthenticationType</code>, this parameter is required. </p> </note>
            kerberos_krb5_conf: <p>The <code>krb5.conf</code> file that contains the Kerberos configuration information. You can load the <code>krb5.conf</code> file by providing the file's address. If you're using the CLI, it performs the base64 encoding for you. Otherwise, provide the base64-encoded text. </p> <note> <p>If <code>KERBEROS</code> is specified for <code>AuthenticationType</code>, this parameter is required.</p> </note>
            agent_arns: <p>The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your HDFS cluster.</p>
            tags: <p>The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources. </p>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, which includes the Kerberos keytab that DataSync uses to access a specific Hadoop Distributed File System (HDFS) storage location, with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationHdfs</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with the <code>KerberosKeytab</code> you specify for to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>KerberosKeytab</code>) or <code>CustomSecretConfig</code> (without <code>KerberosKeytab</code>) to provide credentials for a <code>CreateLocationHdfs</code> request. Do not provide both parameters for the same request.</p> </note>
            custom_secret_config: <p>Specifies configuration information for a customer-managed Secrets Manager secret where the Kerberos keytab for the HDFS storage location is stored in binary, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>KerberosKeytab</code>) or <code>CustomSecretConfig</code> (without <code>KerberosKeytab</code>) to provide credentials for a <code>CreateLocationHdfs</code> request. Do not provide both parameters for the same request.</p> </note>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_hdfs_request.CreateLocationHdfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_hdfs_response.CreateLocationHdfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_hdfs

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_hdfs.create_location_hdfs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_hdfs_request.CreateLocationHdfsRequest = {
            "name_nodes": name_nodes,
            "authentication_type": authentication_type,
            "agent_arns": agent_arns,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if block_size is not None:
            input_["block_size"] = block_size
        if replication_factor is not None:
            input_["replication_factor"] = replication_factor
        if kms_key_provider_uri is not None:
            input_["kms_key_provider_uri"] = kms_key_provider_uri
        if qop_configuration is not None:
            input_["qop_configuration"] = qop_configuration
        if simple_user is not None:
            input_["simple_user"] = simple_user
        if kerberos_principal is not None:
            input_["kerberos_principal"] = kerberos_principal
        if kerberos_keytab is not None:
            input_["kerberos_keytab"] = kerberos_keytab
        if kerberos_krb5_conf is not None:
            input_["kerberos_krb5_conf"] = kerberos_krb5_conf
        if tags is not None:
            input_["tags"] = tags
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_nfs(
        self,
        subdirectory: "capo_datasync.types.nfs_subdirectory.NfsSubdirectory",
        server_hostname: "capo_datasync.types.server_hostname.ServerHostname",
        on_prem_config: "capo_datasync.types.on_prem_config.OnPremConfig",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        mount_options: Optional[
            "capo_datasync.types.nfs_mount_options.NfsMountOptions"
        ] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
    ) -> "capo_datasync.types.create_location_nfs_response.CreateLocationNfsResponse":
        """<p>Creates a transfer <i>location</i> for a Network File System (NFS) file server. DataSync can use this location as a source or destination for transferring data.</p> <p>Before you begin, make sure that you understand how DataSync <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs">accesses NFS file servers</a>.</p>

        Args:
            subdirectory: <p>Specifies the export path in your NFS file server that you want DataSync to mount.</p> <p>This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs">Accessing NFS file servers</a>.</p>
            server_hostname: <p>Specifies the DNS name or IP address (IPv4 or IPv6) of the NFS file server that your DataSync agent connects to.</p>
            on_prem_config: <p>Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect to your NFS file server.</p> <p>You can specify more than one agent. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html#multiple-agents">Using multiple DataSync agents</a>.</p>
            mount_options: <p>Specifies the options that DataSync can use to mount your NFS file server.</p>
            tags: <p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_nfs_request.CreateLocationNfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_nfs_response.CreateLocationNfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_nfs

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_nfs.create_location_nfs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_nfs_request.CreateLocationNfsRequest = {
            "subdirectory": subdirectory,
            "server_hostname": server_hostname,
            "on_prem_config": on_prem_config,
        }
        if mount_options is not None:
            input_["mount_options"] = mount_options
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_object_storage(
        self,
        server_hostname: "capo_datasync.types.server_hostname.ServerHostname",
        bucket_name: "capo_datasync.types.object_storage_bucket_name.ObjectStorageBucketName",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        server_port: Optional[
            "capo_datasync.types.object_storage_server_port.ObjectStorageServerPort"
        ] = None,
        server_protocol: Optional[
            "capo_datasync.types.object_storage_server_protocol.ObjectStorageServerProtocol"
        ] = None,
        subdirectory: Optional[
            "capo_datasync.types.s3_subdirectory.S3Subdirectory"
        ] = None,
        access_key: Optional[
            "capo_datasync.types.object_storage_access_key.ObjectStorageAccessKey"
        ] = None,
        secret_key: Optional[
            "capo_datasync.types.object_storage_secret_key.ObjectStorageSecretKey"
        ] = None,
        agent_arns: Optional["capo_datasync.types.agent_arn_list.AgentArnList"] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
        server_certificate: Optional[
            "capo_datasync.types.object_storage_certificate.ObjectStorageCertificate"
        ] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
    ) -> "capo_datasync.types.create_location_object_storage_response.CreateLocationObjectStorageResponse":
        """<p>Creates a transfer <i>location</i> for an object storage system. DataSync can use this location as a source or destination for transferring data. You can make transfers with or without a <a href="https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html#when-agent-required">DataSync agent</a>.</p> <p>Before you begin, make sure that you understand the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-object-location.html#create-object-location-prerequisites">prerequisites</a> for DataSync to work with object storage systems.</p>

        Args:
            server_hostname: <p>Specifies the domain name or IP address (IPv4 or IPv6) of the object storage server that your DataSync agent connects to.</p>
            server_port: <p>Specifies the port that your object storage server accepts inbound network traffic on (for example, port 443).</p>
            server_protocol: <p>Specifies the protocol that your object storage server uses to communicate. If not specified, the default value is <code>HTTPS</code>.</p>
            subdirectory: <p>Specifies the object prefix for your object storage server. If this is a source location, DataSync only copies objects with this prefix. If this is a destination location, DataSync writes all objects with this prefix. </p>
            bucket_name: <p>Specifies the name of the object storage bucket involved in the transfer.</p>
            access_key: <p>Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.</p>
            secret_key: <p>Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.</p> <note> <p>If you provide a secret using <code>SecretKey</code>, but do not provide secret configuration details using <code>CmkSecretConfig</code> or <code>CustomSecretConfig</code>, then DataSync stores the token using your Amazon Web Services account's Secrets Manager secret.</p> </note>
            agent_arns: <p>(Optional) Specifies the Amazon Resource Names (ARNs) of the DataSync agents that can connect with your object storage system. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.</p> <note> <p>Make sure you configure this parameter correctly when you first create your storage location. You cannot add or remove agents from a storage location after you create it.</p> </note>
            tags: <p>Specifies the key-value pair that represents a tag that you want to add to the resource. Tags can help you manage, filter, and search for your resources. We recommend creating a name tag for your location.</p>
            server_certificate: <p>Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA). You must specify a single <code>.pem</code> file with a full certificate chain (for example, <code>file:///home/user/.ssh/object_storage_certificates.pem</code>).</p> <p>The certificate chain might include:</p> <ul> <li> <p>The object storage system's certificate</p> </li> <li> <p>All intermediate certificates (if there are any)</p> </li> <li> <p>The root certificate of the signing CA</p> </li> </ul> <p>You can concatenate your certificates into a <code>.pem</code> file (which can be up to 32768 bytes before base64 encoding). The following example <code>cat</code> command creates an <code>object_storage_certificates.pem</code> file that includes three certificates:</p> <p> <code>cat object_server_certificate.pem intermediate_certificate.pem ca_root_certificate.pem > object_storage_certificates.pem</code> </p> <p>To use this parameter, configure <code>ServerProtocol</code> to <code>HTTPS</code>.</p>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, which includes the <code>SecretKey</code> that DataSync uses to access a specific object storage location, with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationObjectStorage</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with the value you specify for the <code>SecretKey</code> parameter to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>SecretKey</code>) or <code>CustomSecretConfig</code> (without <code>SecretKey</code>) to provide credentials for a <code>CreateLocationObjectStorage</code> request. Do not provide both parameters for the same request.</p> </note>
            custom_secret_config: <p>Specifies configuration information for a customer-managed Secrets Manager secret where the secret key for a specific object storage location is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>SecretKey</code>) or <code>CustomSecretConfig</code> (without <code>SecretKey</code>) to provide credentials for a <code>CreateLocationObjectStorage</code> request. Do not provide both parameters for the same request.</p> </note>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_object_storage_request.CreateLocationObjectStorageRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_object_storage_response.CreateLocationObjectStorageResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_object_storage

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_object_storage.create_location_object_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_object_storage_request.CreateLocationObjectStorageRequest = {
            "server_hostname": server_hostname,
            "bucket_name": bucket_name,
        }
        if server_port is not None:
            input_["server_port"] = server_port
        if server_protocol is not None:
            input_["server_protocol"] = server_protocol
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if access_key is not None:
            input_["access_key"] = access_key
        if secret_key is not None:
            input_["secret_key"] = secret_key
        if agent_arns is not None:
            input_["agent_arns"] = agent_arns
        if tags is not None:
            input_["tags"] = tags
        if server_certificate is not None:
            input_["server_certificate"] = server_certificate
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_s3(
        self,
        s3_bucket_arn: "capo_datasync.types.s3_bucket_arn.S3BucketArn",
        s3_config: "capo_datasync.types.s3_config.S3Config",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.s3_subdirectory.S3Subdirectory"
        ] = None,
        s3_storage_class: Optional[
            "capo_datasync.types.s3_storage_class.S3StorageClass"
        ] = None,
        agent_arns: Optional["capo_datasync.types.agent_arn_list.AgentArnList"] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
    ) -> "capo_datasync.types.create_location_s3_response.CreateLocationS3Response":
        """<p>Creates a transfer <i>location</i> for an Amazon S3 bucket. DataSync can use this location as a source or destination for transferring data.</p> <important> <p>Before you begin, make sure that you read the following topics:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Storage class considerations with Amazon S3 locations</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests">Evaluating S3 request costs when using DataSync</a> </p> </li> </ul> </important> <p> For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html">Configuring transfers with Amazon S3</a>.</p>

        Args:
            subdirectory: <p>Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location).</p> <note> <p>DataSync can't transfer objects with a prefix that begins with a slash (<code>/</code>) or includes <code>//</code>, <code>/./</code>, or <code>/../</code> patterns. For example:</p> <ul> <li> <p> <code>/photos</code> </p> </li> <li> <p> <code>photos//2006/January</code> </p> </li> <li> <p> <code>photos/./2006/February</code> </p> </li> <li> <p> <code>photos/../2006/March</code> </p> </li> </ul> </note>
            s3_bucket_arn: <p>Specifies the ARN of the S3 bucket that you want to use as a location. (When creating your DataSync task later, you specify whether this location is a transfer source or destination.) </p> <p>If your S3 bucket is located on an Outposts resource, you must specify an Amazon S3 access point. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html">Managing data access with Amazon S3 access points</a> in the <i>Amazon S3 User Guide</i>.</p>
            s3_storage_class: <p>Specifies the storage class that you want your objects to use when Amazon S3 is a transfer destination.</p> <p>For buckets in Amazon Web Services Regions, the storage class defaults to <code>STANDARD</code>. For buckets on Outposts, the storage class defaults to <code>OUTPOSTS</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Storage class considerations with Amazon S3 transfers</a>.</p>
            agent_arns: <p>(Amazon S3 on Outposts only) Specifies the Amazon Resource Name (ARN) of the DataSync agent on your Outpost.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/deploy-agents.html#outposts-agent">Deploy your DataSync agent on Outposts</a>.</p>
            tags: <p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your transfer location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_s3_request.CreateLocationS3Request]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_s3_response.CreateLocationS3Response"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_s3

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_s3.create_location_s3(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_s3_request.CreateLocationS3Request = {
            "s3_bucket_arn": s3_bucket_arn,
            "s3_config": s3_config,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if s3_storage_class is not None:
            input_["s3_storage_class"] = s3_storage_class
        if agent_arns is not None:
            input_["agent_arns"] = agent_arns
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location_smb(
        self,
        subdirectory: "capo_datasync.types.smb_subdirectory.SmbSubdirectory",
        server_hostname: "capo_datasync.types.server_hostname.ServerHostname",
        agent_arns: "capo_datasync.types.agent_arn_list.AgentArnList",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        user: Optional["capo_datasync.types.smb_user.SmbUser"] = None,
        domain: Optional["capo_datasync.types.smb_domain.SmbDomain"] = None,
        password: Optional["capo_datasync.types.smb_password.SmbPassword"] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
        mount_options: Optional[
            "capo_datasync.types.smb_mount_options.SmbMountOptions"
        ] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
        authentication_type: Optional[
            "capo_datasync.types.smb_authentication_type.SmbAuthenticationType"
        ] = None,
        dns_ip_addresses: Optional["capo_datasync.types.dns_ip_list.DnsIpList"] = None,
        kerberos_principal: Optional[
            "capo_datasync.types.kerberos_principal.KerberosPrincipal"
        ] = None,
        kerberos_keytab: Optional[
            "capo_datasync.types.kerberos_keytab_file.KerberosKeytabFile"
        ] = None,
        kerberos_krb5_conf: Optional[
            "capo_datasync.types.kerberos_krb5_conf_file.KerberosKrb5ConfFile"
        ] = None,
    ) -> "capo_datasync.types.create_location_smb_response.CreateLocationSmbResponse":
        """<p>Creates a transfer <i>location</i> for a Server Message Block (SMB) file server. DataSync can use this location as a source or destination for transferring data.</p> <p>Before you begin, make sure that you understand how DataSync accesses SMB file servers. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions">Providing DataSync access to SMB file servers</a>.</p>

        Args:
            subdirectory: <p>Specifies the name of the share exported by your SMB file server where DataSync will read or write data. You can include a subdirectory in the share path (for example, <code>/path/to/subdirectory</code>). Make sure that other SMB clients in your network can also mount this path.</p> <p>To copy all data in the subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions">Providing DataSync access to SMB file servers</a>.</p>
            server_hostname: <p>Specifies the domain name or IP address (IPv4 or IPv6) of the SMB file server that your DataSync agent connects to.</p> <note> <p>If you're using Kerberos authentication, you must specify a domain name.</p> </note>
            user: <p>Specifies the user that can mount and access the files, folders, and file metadata in your SMB file server. This parameter applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p> <p>For information about choosing a user with the right level of access for your transfer, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions">Providing DataSync access to SMB file servers</a>.</p>
            domain: <p>Specifies the Windows domain name that your SMB file server belongs to. This parameter applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p> <p>If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right file server.</p>
            password: <p>Specifies the password of the user who can mount your SMB file server and has permission to access the files and folders involved in your transfer. This parameter applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, either a <code>Password</code> or <code>KerberosKeytab</code> (for <code>NTLM</code> (default) and <code>KERBEROS</code> authentication types, respectively) that DataSync uses to access a specific SMB storage location, with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationSmbRequest</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with either the <code>Password</code> or <code>KerberosKeytab</code> you specify to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with either <code>Password</code> or <code>KerberosKeytab</code>) or <code>CustomSecretConfig</code> (without any <code>Password</code> and <code>KerberosKeytab</code>) to provide credentials for a <code>CreateLocationSmbRequest</code> request. Do not provide both <code>CmkSecretConfig</code> and <code>CustomSecretConfig</code> parameters for the same request.</p> </note>
            custom_secret_config: <p>Specifies configuration information for a customer-managed Secrets Manager secret where the SMB storage location credentials is stored in Secrets Manager as plain text (for <code>Password</code>) or binary (for <code>KerberosKeytab</code>). This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>SasConfiguration</code>) or <code>CustomSecretConfig</code> (without <code>SasConfiguration</code>) to provide credentials for a <code>CreateLocationSmbRequest</code> request. Do not provide both parameters for the same request.</p> </note>
            agent_arns: <p>Specifies the DataSync agent (or agents) that can connect to your SMB file server. You specify an agent by using its Amazon Resource Name (ARN).</p>
            mount_options: <p>Specifies the version of the SMB protocol that DataSync uses to access your SMB file server.</p>
            tags: <p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>
            authentication_type: <p>Specifies the authentication protocol that DataSync uses to connect to your SMB file server. DataSync supports <code>NTLM</code> (default) and <code>KERBEROS</code> authentication.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions">Providing DataSync access to SMB file servers</a>.</p>
            dns_ip_addresses: <p>Specifies the IPv4 or IPv6 addresses for the DNS servers that your SMB file server belongs to. This parameter applies only if <code>AuthenticationType</code> is set to <code>KERBEROS</code>.</p> <p>If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right SMB file server.</p>
            kerberos_principal: <p>Specifies a Kerberos principal, which is an identity in your Kerberos realm that has permission to access the files, folders, and file metadata in your SMB file server.</p> <p>A Kerberos principal might look like <code>HOST/kerberosuser@MYDOMAIN.ORG</code>.</p> <p>Principal names are case sensitive. Your DataSync task execution will fail if the principal that you specify for this parameter doesn’t exactly match the principal that you use to create the keytab file.</p>
            kerberos_keytab: <p>Specifies your Kerberos key table (keytab) file, which includes mappings between your Kerberos principal and encryption keys.</p> <p>To avoid task execution errors, make sure that the Kerberos principal that you use to create the keytab file matches exactly what you specify for <code>KerberosPrincipal</code>. </p>
            kerberos_krb5_conf: <p>Specifies a Kerberos configuration file (<code>krb5.conf</code>) that defines your Kerberos realm configuration.</p> <p>The file must be base64 encoded. If you're using the CLI, the encoding is done for you.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_location_smb_request.CreateLocationSmbRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_location_smb_response.CreateLocationSmbResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_location_smb

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_location_smb.create_location_smb(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_location_smb_request.CreateLocationSmbRequest = {
            "subdirectory": subdirectory,
            "server_hostname": server_hostname,
            "agent_arns": agent_arns,
        }
        if user is not None:
            input_["user"] = user
        if domain is not None:
            input_["domain"] = domain
        if password is not None:
            input_["password"] = password
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config
        if mount_options is not None:
            input_["mount_options"] = mount_options
        if tags is not None:
            input_["tags"] = tags
        if authentication_type is not None:
            input_["authentication_type"] = authentication_type
        if dns_ip_addresses is not None:
            input_["dns_ip_addresses"] = dns_ip_addresses
        if kerberos_principal is not None:
            input_["kerberos_principal"] = kerberos_principal
        if kerberos_keytab is not None:
            input_["kerberos_keytab"] = kerberos_keytab
        if kerberos_krb5_conf is not None:
            input_["kerberos_krb5_conf"] = kerberos_krb5_conf

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_task(
        self,
        source_location_arn: "capo_datasync.types.location_arn.LocationArn",
        destination_location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        cloud_watch_log_group_arn: Optional[
            "capo_datasync.types.log_group_arn.LogGroupArn"
        ] = None,
        name: Optional["capo_datasync.types.tag_value.TagValue"] = None,
        options: Optional["capo_datasync.types.options.Options"] = None,
        excludes: Optional["capo_datasync.types.filter_list.FilterList"] = None,
        schedule: Optional["capo_datasync.types.task_schedule.TaskSchedule"] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
        includes: Optional["capo_datasync.types.filter_list.FilterList"] = None,
        manifest_config: Optional[
            "capo_datasync.types.manifest_config.ManifestConfig"
        ] = None,
        task_report_config: Optional[
            "capo_datasync.types.task_report_config.TaskReportConfig"
        ] = None,
        task_mode: Optional["capo_datasync.types.task_mode.TaskMode"] = None,
    ) -> "capo_datasync.types.create_task_response.CreateTaskResponse":
        """<p>Configures a <i>task</i>, which defines where and how DataSync transfers your data.</p> <p>A task includes a source location, destination location, and transfer options (such as bandwidth limits, scheduling, and more).</p> <important> <p>If you're planning to transfer data to or from an Amazon S3 location, review <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests">how DataSync can affect your S3 request charges</a> and the <a href="http://aws.amazon.com/datasync/pricing/">DataSync pricing page</a> before you begin.</p> </important>

        Args:
            source_location_arn: <p>Specifies the ARN of your transfer's source location.</p>
            destination_location_arn: <p>Specifies the ARN of your transfer's destination location. </p>
            cloud_watch_log_group_arn: <p>Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.</p> <p>For Enhanced mode tasks, you don't need to specify anything. DataSync automatically sends logs to a CloudWatch log group named <code>/aws/datasync</code>.</p>
            name: <p>Specifies the name of your task.</p>
            options: <p>Specifies your task's settings, such as preserving file metadata, verifying data integrity, among other options.</p>
            excludes: <p>Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>
            schedule: <p>Specifies a schedule for when you want your task to run. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html">Scheduling your task</a>.</p>
            tags: <p>Specifies the tags that you want to apply to your task.</p> <p> <i>Tags</i> are key-value pairs that help you manage, filter, and search for your DataSync resources.</p>
            includes: <p>Specifies include filters that define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>
            manifest_config: <p>Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html">Specifying what DataSync transfers by using a manifest</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p>
            task_report_config: <p>Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html">Monitoring your DataSync transfers with task reports</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p>
            task_mode: <p>Specifies one of the following task modes for your data transfer:</p> <ul> <li> <p> <code>ENHANCED</code> - Transfer virtually unlimited numbers of objects with higher performance than Basic mode. Enhanced mode tasks optimize the data transfer process by listing, preparing, transferring, and verifying data in parallel. Enhanced mode is currently available for transfers between Amazon S3 locations, transfers between Azure Blob and Amazon S3 without an agent, and transfers between other clouds and Amazon S3 without an agent.</p> <note> <p>To create an Enhanced mode task, the IAM role that you use to call the <code>CreateTask</code> operation must have the <code>iam:CreateServiceLinkedRole</code> permission.</p> </note> </li> <li> <p> <code>BASIC</code> (default) - Transfer files or objects between Amazon Web Services storage and all other supported DataSync locations. Basic mode tasks are subject to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/datasync-limits.html">quotas</a> on the number of files, objects, and directories in a dataset. Basic mode sequentially prepares, transfers, and verifies data, making it slower than Enhanced mode for most workloads.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html#task-mode-differences">Understanding task mode differences</a>.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.create_task_request.CreateTaskRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.create_task_response.CreateTaskResponse"
        ]:
            import capo_datasync._operations.fmrs_service.create_task

            output, http_response = (
                capo_datasync._operations.fmrs_service.create_task.create_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.create_task_request.CreateTaskRequest = {
            "source_location_arn": source_location_arn,
            "destination_location_arn": destination_location_arn,
        }
        if cloud_watch_log_group_arn is not None:
            input_["cloud_watch_log_group_arn"] = cloud_watch_log_group_arn
        if name is not None:
            input_["name"] = name
        if options is not None:
            input_["options"] = options
        if excludes is not None:
            input_["excludes"] = excludes
        if schedule is not None:
            input_["schedule"] = schedule
        if tags is not None:
            input_["tags"] = tags
        if includes is not None:
            input_["includes"] = includes
        if manifest_config is not None:
            input_["manifest_config"] = manifest_config
        if task_report_config is not None:
            input_["task_report_config"] = task_report_config
        if task_mode is not None:
            input_["task_mode"] = task_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_agent(
        self,
        agent_arn: "capo_datasync.types.agent_arn.AgentArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.delete_agent_response.DeleteAgentResponse":
        """<p>Removes an DataSync agent resource from your Amazon Web Services account.</p> <p>Keep in mind that this operation (which can't be undone) doesn't remove the agent's virtual machine (VM) or Amazon EC2 instance from your storage environment. For next steps, you can delete the VM or instance from your storage environment or reuse it to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html">activate a new agent</a>.</p>

        Args:
            agent_arn: <p>The Amazon Resource Name (ARN) of the agent to delete. Use the <code>ListAgents</code> operation to return a list of agents for your account and Amazon Web Services Region.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.delete_agent_request.DeleteAgentRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.delete_agent_response.DeleteAgentResponse"
        ]:
            import capo_datasync._operations.fmrs_service.delete_agent

            output, http_response = (
                capo_datasync._operations.fmrs_service.delete_agent.delete_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.delete_agent_request.DeleteAgentRequest = {
            "agent_arn": agent_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_location(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.delete_location_response.DeleteLocationResponse":
        """<p>Deletes a transfer location resource from DataSync. </p>

        Args:
            location_arn: <p>The Amazon Resource Name (ARN) of the location to delete.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.delete_location_request.DeleteLocationRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.delete_location_response.DeleteLocationResponse"
        ]:
            import capo_datasync._operations.fmrs_service.delete_location

            output, http_response = (
                capo_datasync._operations.fmrs_service.delete_location.delete_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.delete_location_request.DeleteLocationRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_task(
        self,
        task_arn: "capo_datasync.types.task_arn.TaskArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.delete_task_response.DeleteTaskResponse":
        """<p>Deletes a transfer task resource from DataSync.</p>

        Args:
            task_arn: <p>Specifies the Amazon Resource Name (ARN) of the task that you want to delete.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.delete_task_request.DeleteTaskRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.delete_task_response.DeleteTaskResponse"
        ]:
            import capo_datasync._operations.fmrs_service.delete_task

            output, http_response = (
                capo_datasync._operations.fmrs_service.delete_task.delete_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.delete_task_request.DeleteTaskRequest = {
            "task_arn": task_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_agent(
        self,
        agent_arn: "capo_datasync.types.agent_arn.AgentArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_agent_response.DescribeAgentResponse":
        """<p>Returns information about an DataSync agent, such as its name, service endpoint type, and status.</p>

        Args:
            agent_arn: <p>Specifies the Amazon Resource Name (ARN) of the DataSync agent that you want information about.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_agent_request.DescribeAgentRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_agent_response.DescribeAgentResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_agent

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_agent.describe_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_agent_request.DescribeAgentRequest = {
            "agent_arn": agent_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_azure_blob(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_location_azure_blob_response.DescribeLocationAzureBlobResponse":
        """<p>Provides details about how an DataSync transfer location for Microsoft Azure Blob Storage is configured.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of your Azure Blob Storage transfer location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_azure_blob_request.DescribeLocationAzureBlobRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_azure_blob_response.DescribeLocationAzureBlobResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_azure_blob

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_azure_blob.describe_location_azure_blob(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_azure_blob_request.DescribeLocationAzureBlobRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_efs(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> (
        "capo_datasync.types.describe_location_efs_response.DescribeLocationEfsResponse"
    ):
        """<p>Provides details about how an DataSync transfer location for an Amazon EFS file system is configured.</p>

        Args:
            location_arn: <p>The Amazon Resource Name (ARN) of the Amazon EFS file system location that you want information about.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_efs_request.DescribeLocationEfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_efs_response.DescribeLocationEfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_efs

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_efs.describe_location_efs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_efs_request.DescribeLocationEfsRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_fsx_lustre(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_location_fsx_lustre_response.DescribeLocationFsxLustreResponse":
        """<p>Provides details about how an DataSync transfer location for an Amazon FSx for Lustre file system is configured.</p>

        Args:
            location_arn: <p>The Amazon Resource Name (ARN) of the FSx for Lustre location to describe. </p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_fsx_lustre_request.DescribeLocationFsxLustreRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_fsx_lustre_response.DescribeLocationFsxLustreResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_fsx_lustre

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_fsx_lustre.describe_location_fsx_lustre(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_fsx_lustre_request.DescribeLocationFsxLustreRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_fsx_ontap(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_location_fsx_ontap_response.DescribeLocationFsxOntapResponse":
        """<p>Provides details about how an DataSync transfer location for an Amazon FSx for NetApp ONTAP file system is configured.</p> <note> <p>If your location uses SMB, the <code>DescribeLocationFsxOntap</code> operation doesn't actually return a <code>Password</code>.</p> </note>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the FSx for ONTAP file system location that you want information about.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_fsx_ontap_request.DescribeLocationFsxOntapRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_fsx_ontap_response.DescribeLocationFsxOntapResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_fsx_ontap

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_fsx_ontap.describe_location_fsx_ontap(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_fsx_ontap_request.DescribeLocationFsxOntapRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_fsx_open_zfs(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_location_fsx_open_zfs_response.DescribeLocationFsxOpenZfsResponse":
        """<p>Provides details about how an DataSync transfer location for an Amazon FSx for OpenZFS file system is configured.</p> <note> <p>Response elements related to <code>SMB</code> aren't supported with the <code>DescribeLocationFsxOpenZfs</code> operation.</p> </note>

        Args:
            location_arn: <p>The Amazon Resource Name (ARN) of the FSx for OpenZFS location to describe.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_fsx_open_zfs_request.DescribeLocationFsxOpenZfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_fsx_open_zfs_response.DescribeLocationFsxOpenZfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_fsx_open_zfs

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_fsx_open_zfs.describe_location_fsx_open_zfs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_fsx_open_zfs_request.DescribeLocationFsxOpenZfsRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_fsx_windows(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_location_fsx_windows_response.DescribeLocationFsxWindowsResponse":
        """<p>Provides details about how an DataSync transfer location for an Amazon FSx for Windows File Server file system is configured.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the FSx for Windows File Server location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_fsx_windows_request.DescribeLocationFsxWindowsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_fsx_windows_response.DescribeLocationFsxWindowsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_fsx_windows

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_fsx_windows.describe_location_fsx_windows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_fsx_windows_request.DescribeLocationFsxWindowsRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_hdfs(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_location_hdfs_response.DescribeLocationHdfsResponse":
        """<p>Provides details about how an DataSync transfer location for a Hadoop Distributed File System (HDFS) is configured.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the HDFS location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_hdfs_request.DescribeLocationHdfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_hdfs_response.DescribeLocationHdfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_hdfs

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_hdfs.describe_location_hdfs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_hdfs_request.DescribeLocationHdfsRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_nfs(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> (
        "capo_datasync.types.describe_location_nfs_response.DescribeLocationNfsResponse"
    ):
        """<p>Provides details about how an DataSync transfer location for a Network File System (NFS) file server is configured.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the NFS location that you want information about.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_nfs_request.DescribeLocationNfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_nfs_response.DescribeLocationNfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_nfs

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_nfs.describe_location_nfs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_nfs_request.DescribeLocationNfsRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_object_storage(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_location_object_storage_response.DescribeLocationObjectStorageResponse":
        """<p>Provides details about how an DataSync transfer location for an object storage system is configured.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the object storage system location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_object_storage_request.DescribeLocationObjectStorageRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_object_storage_response.DescribeLocationObjectStorageResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_object_storage

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_object_storage.describe_location_object_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_object_storage_request.DescribeLocationObjectStorageRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_s3(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_location_s3_response.DescribeLocationS3Response":
        """<p>Provides details about how an DataSync transfer location for an S3 bucket is configured.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the Amazon S3 location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_s3_request.DescribeLocationS3Request]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_s3_response.DescribeLocationS3Response"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_s3

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_s3.describe_location_s3(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_s3_request.DescribeLocationS3Request = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_location_smb(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> (
        "capo_datasync.types.describe_location_smb_response.DescribeLocationSmbResponse"
    ):
        """<p>Provides details about how an DataSync transfer location for a Server Message Block (SMB) file server is configured.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the SMB location that you want information about.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_location_smb_request.DescribeLocationSmbRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_location_smb_response.DescribeLocationSmbResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_location_smb

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_location_smb.describe_location_smb(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_location_smb_request.DescribeLocationSmbRequest = {
            "location_arn": location_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_task(
        self,
        task_arn: "capo_datasync.types.task_arn.TaskArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_task_response.DescribeTaskResponse":
        """<p>Provides information about a <i>task</i>, which defines where and how DataSync transfers your data.</p>

        Args:
            task_arn: <p>Specifies the Amazon Resource Name (ARN) of the transfer task that you want information about.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_task_request.DescribeTaskRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_task_response.DescribeTaskResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_task

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_task.describe_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_task_request.DescribeTaskRequest = {
            "task_arn": task_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_task_execution(
        self,
        task_execution_arn: "capo_datasync.types.task_execution_arn.TaskExecutionArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.describe_task_execution_response.DescribeTaskExecutionResponse":
        """<p>Provides information about an execution of your DataSync task. You can use this operation to help monitor the progress of an ongoing data transfer or check the results of the transfer.</p> <note> <p>Some <code>DescribeTaskExecution</code> response elements are only relevant to a specific task mode. For information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html#task-mode-differences">Understanding task mode differences</a> and <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transfer-performance-counters.html">Understanding data transfer performance counters</a>.</p> </note>

        Args:
            task_execution_arn: <p>Specifies the Amazon Resource Name (ARN) of the task execution that you want information about.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.describe_task_execution_request.DescribeTaskExecutionRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.describe_task_execution_response.DescribeTaskExecutionResponse"
        ]:
            import capo_datasync._operations.fmrs_service.describe_task_execution

            output, http_response = (
                capo_datasync._operations.fmrs_service.describe_task_execution.describe_task_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.describe_task_execution_request.DescribeTaskExecutionRequest = {
            "task_execution_arn": task_execution_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agents(
        self,
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
    ) -> "capo_datasync.types.list_agents_response.ListAgentsResponse":
        """<p>Returns a list of DataSync agents that belong to an Amazon Web Services account in the Amazon Web Services Region specified in the request.</p> <p>With pagination, you can reduce the number of agents returned in a response. If you get a truncated list of agents in a response, the response contains a marker that you can specify in your next request to fetch the next page of agents.</p> <p> <code>ListAgents</code> is eventually consistent. This means the result of running the operation might not reflect that you just created or deleted an agent. For example, if you create an agent with <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateAgent.html">CreateAgent</a> and then immediately run <code>ListAgents</code>, that agent might not show up in the list right away. In situations like this, you can always confirm whether an agent has been created (or deleted) by using <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeAgent.html">DescribeAgent</a>.</p>

        Args:
            max_results: <p>Specifies the maximum number of DataSync agents to list in a response. By default, a response shows a maximum of 100 agents.</p>
            next_token: <p>Specifies an opaque string that indicates the position to begin the next list of results in the response.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.list_agents_request.ListAgentsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.list_agents_response.ListAgentsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.list_agents

            output, http_response = (
                capo_datasync._operations.fmrs_service.list_agents.list_agents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.list_agents_request.ListAgentsRequest = {}
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

    def iter_list_agents(
        self,
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_datasync.types.agent_list_entry.AgentListEntry]":
        _token = next_token
        while True:
            _response = self.list_agents(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agents",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_locations(
        self,
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_datasync.types.location_filters.LocationFilters"
        ] = None,
    ) -> "capo_datasync.types.list_locations_response.ListLocationsResponse":
        """<p>Returns a list of source and destination locations.</p> <p>If you have more locations than are returned in a response (that is, the response returns only a truncated list of your agents), the response contains a token that you can specify in your next request to fetch the next page of locations.</p>

        Args:
            max_results: <p>The maximum number of locations to return.</p>
            next_token: <p>An opaque string that indicates the position at which to begin the next list of locations.</p>
            filters: <p>You can use API filters to narrow down the list of resources returned by <code>ListLocations</code>. For example, to retrieve all tasks on a specific source location, you can use <code>ListLocations</code> with filter name <code>LocationType S3</code> and <code>Operator Equals</code>.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.list_locations_request.ListLocationsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.list_locations_response.ListLocationsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.list_locations

            output, http_response = (
                capo_datasync._operations.fmrs_service.list_locations.list_locations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.list_locations_request.ListLocationsRequest = {}
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

    def iter_list_locations(
        self,
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_datasync.types.location_filters.LocationFilters"
        ] = None,
    ) -> "Iterator[capo_datasync.types.location_list_entry.LocationListEntry]":
        _token = next_token
        while True:
            _response = self.list_locations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("locations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_datasync.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
    ) -> "capo_datasync.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns all the tags associated with an Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>Specifies the Amazon Resource Name (ARN) of the resource that you want tag information on.</p>
            max_results: <p>Specifies how many results that you want in the response.</p>
            next_token: <p>Specifies an opaque string that indicates the position to begin the next list of results in the response.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_datasync._operations.fmrs_service.list_tags_for_resource

            output, http_response = (
                capo_datasync._operations.fmrs_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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

    def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_datasync.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_datasync.types.tag_list_entry.TagListEntry]":
        _token = next_token
        while True:
            _response = self.list_tags_for_resource(
                resource_arn,
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

    def list_task_executions(
        self,
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        task_arn: Optional["capo_datasync.types.task_arn.TaskArn"] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
    ) -> "capo_datasync.types.list_task_executions_response.ListTaskExecutionsResponse":
        """<p>Returns a list of executions for an DataSync transfer task.</p>

        Args:
            task_arn: <p>Specifies the Amazon Resource Name (ARN) of the task that you want execution information about.</p>
            max_results: <p>Specifies how many results you want in the response.</p>
            next_token: <p>Specifies an opaque string that indicates the position at which to begin the next list of results in the response.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.list_task_executions_request.ListTaskExecutionsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.list_task_executions_response.ListTaskExecutionsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.list_task_executions

            output, http_response = (
                capo_datasync._operations.fmrs_service.list_task_executions.list_task_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.list_task_executions_request.ListTaskExecutionsRequest = {}
        if task_arn is not None:
            input_["task_arn"] = task_arn
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

    def iter_list_task_executions(
        self,
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        task_arn: Optional["capo_datasync.types.task_arn.TaskArn"] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
    ) -> (
        "Iterator[capo_datasync.types.task_execution_list_entry.TaskExecutionListEntry]"
    ):
        _token = next_token
        while True:
            _response = self.list_task_executions(
                config_overrides=config_overrides,
                task_arn=task_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("task_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tasks(
        self,
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
        filters: Optional["capo_datasync.types.task_filters.TaskFilters"] = None,
    ) -> "capo_datasync.types.list_tasks_response.ListTasksResponse":
        """<p>Returns a list of the DataSync tasks you created.</p>

        Args:
            max_results: <p>The maximum number of tasks to return.</p>
            next_token: <p>An opaque string that indicates the position at which to begin the next list of tasks.</p>
            filters: <p>You can use API filters to narrow down the list of resources returned by <code>ListTasks</code>. For example, to retrieve all tasks on a specific source location, you can use <code>ListTasks</code> with filter name <code>LocationId</code> and <code>Operator Equals</code> with the ARN for the location.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.list_tasks_request.ListTasksRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.list_tasks_response.ListTasksResponse"
        ]:
            import capo_datasync._operations.fmrs_service.list_tasks

            output, http_response = (
                capo_datasync._operations.fmrs_service.list_tasks.list_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.list_tasks_request.ListTasksRequest = {}
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

    def iter_list_tasks(
        self,
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        max_results: Optional["capo_datasync.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_datasync.types.next_token.NextToken"] = None,
        filters: Optional["capo_datasync.types.task_filters.TaskFilters"] = None,
    ) -> "Iterator[capo_datasync.types.task_list_entry.TaskListEntry]":
        _token = next_token
        while True:
            _response = self.list_tasks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_task_execution(
        self,
        task_arn: "capo_datasync.types.task_arn.TaskArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        override_options: Optional["capo_datasync.types.options.Options"] = None,
        includes: Optional["capo_datasync.types.filter_list.FilterList"] = None,
        excludes: Optional["capo_datasync.types.filter_list.FilterList"] = None,
        manifest_config: Optional[
            "capo_datasync.types.manifest_config.ManifestConfig"
        ] = None,
        task_report_config: Optional[
            "capo_datasync.types.task_report_config.TaskReportConfig"
        ] = None,
        tags: Optional["capo_datasync.types.input_tag_list.InputTagList"] = None,
    ) -> "capo_datasync.types.start_task_execution_response.StartTaskExecutionResponse":
        """<p>Starts an DataSync transfer task. For each task, you can only run one task execution at a time.</p> <p>There are several steps to a task execution. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/working-with-task-executions.html#understand-task-execution-statuses">Task execution statuses</a>.</p> <important> <p>If you're planning to transfer data to or from an Amazon S3 location, review <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests">how DataSync can affect your S3 request charges</a> and the <a href="http://aws.amazon.com/datasync/pricing/">DataSync pricing page</a> before you begin.</p> </important>

        Args:
            task_arn: <p>Specifies the Amazon Resource Name (ARN) of the task that you want to start.</p>
            includes: <p>Specifies a list of filter rules that determines which files to include when running a task. The pattern should contain a single filter string that consists of the patterns to include. The patterns are delimited by "|" (that is, a pipe), for example, <code>"/folder1|/folder2"</code>. </p>
            excludes: <p>Specifies a list of filter rules that determines which files to exclude from a task. The list contains a single filter string that consists of the patterns to exclude. The patterns are delimited by "|" (that is, a pipe), for example, <code>"/folder1|/folder2"</code>. </p>
            manifest_config: <p>Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html">Specifying what DataSync transfers by using a manifest</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a manifest configuration, specify this parameter with an empty value.</p>
            task_report_config: <p>Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html">Monitoring your DataSync transfers with task reports</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a task report configuration, specify this parameter as empty.</p>
            tags: <p>Specifies the tags that you want to apply to the Amazon Resource Name (ARN) representing the task execution.</p> <p> <i>Tags</i> are key-value pairs that help you manage, filter, and search for your DataSync resources.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.start_task_execution_request.StartTaskExecutionRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.start_task_execution_response.StartTaskExecutionResponse"
        ]:
            import capo_datasync._operations.fmrs_service.start_task_execution

            output, http_response = (
                capo_datasync._operations.fmrs_service.start_task_execution.start_task_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.start_task_execution_request.StartTaskExecutionRequest = {
            "task_arn": task_arn
        }
        if override_options is not None:
            input_["override_options"] = override_options
        if includes is not None:
            input_["includes"] = includes
        if excludes is not None:
            input_["excludes"] = excludes
        if manifest_config is not None:
            input_["manifest_config"] = manifest_config
        if task_report_config is not None:
            input_["task_report_config"] = task_report_config
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_datasync.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_datasync.types.input_tag_list.InputTagList",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.tag_resource_response.TagResourceResponse":
        """<p>Applies a <i>tag</i> to an Amazon Web Services resource. Tags are key-value pairs that can help you manage, filter, and search for your resources.</p> <p>These include DataSync resources, such as locations, tasks, and task executions.</p>

        Args:
            resource_arn: <p>Specifies the Amazon Resource Name (ARN) of the resource to apply the tag to.</p>
            tags: <p>Specifies the tags that you want to apply to the resource.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_datasync._operations.fmrs_service.tag_resource

            output, http_response = (
                capo_datasync._operations.fmrs_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_datasync.types.taggable_resource_arn.TaggableResourceArn",
        keys: "capo_datasync.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> "capo_datasync.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from an Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>Specifies the Amazon Resource Name (ARN) of the resource to remove the tags from.</p>
            keys: <p>Specifies the keys in the tags that you want to remove.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_datasync._operations.fmrs_service.untag_resource

            output, http_response = (
                capo_datasync._operations.fmrs_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "keys": keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_agent(
        self,
        agent_arn: "capo_datasync.types.agent_arn.AgentArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        name: Optional["capo_datasync.types.tag_value.TagValue"] = None,
    ) -> "capo_datasync.types.update_agent_response.UpdateAgentResponse":
        """<p>Updates the name of an DataSync agent.</p>

        Args:
            agent_arn: <p>The Amazon Resource Name (ARN) of the agent to update.</p>
            name: <p>The name that you want to use to configure the agent.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_agent_request.UpdateAgentRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_agent_response.UpdateAgentResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_agent

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_agent.update_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_agent_request.UpdateAgentRequest = {
            "agent_arn": agent_arn
        }
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_azure_blob(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.azure_blob_subdirectory.AzureBlobSubdirectory"
        ] = None,
        authentication_type: Optional[
            "capo_datasync.types.azure_blob_authentication_type.AzureBlobAuthenticationType"
        ] = None,
        sas_configuration: Optional[
            "capo_datasync.types.azure_blob_sas_configuration.AzureBlobSasConfiguration"
        ] = None,
        blob_type: Optional["capo_datasync.types.azure_blob_type.AzureBlobType"] = None,
        access_tier: Optional[
            "capo_datasync.types.azure_access_tier.AzureAccessTier"
        ] = None,
        agent_arns: Optional["capo_datasync.types.agent_arn_list.AgentArnList"] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
    ) -> "capo_datasync.types.update_location_azure_blob_response.UpdateLocationAzureBlobResponse":
        """<p>Modifies the following configurations of the Microsoft Azure Blob Storage transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html">Configuring DataSync transfers with Azure Blob Storage</a>.</p>

        Args:
            location_arn: <p>Specifies the ARN of the Azure Blob Storage transfer location that you're updating.</p>
            subdirectory: <p>Specifies path segments if you want to limit your transfer to a virtual directory in your container (for example, <code>/my/images</code>).</p>
            authentication_type: <p>Specifies the authentication method DataSync uses to access your Azure Blob Storage. DataSync can access blob storage using a shared access signature (SAS).</p>
            sas_configuration: <p>Specifies the SAS configuration that allows DataSync to access your Azure Blob Storage.</p>
            blob_type: <p>Specifies the type of blob that you want your objects or files to be when transferring them into Azure Blob Storage. Currently, DataSync only supports moving data into Azure Blob Storage as block blobs. For more information on blob types, see the <a href="https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs">Azure Blob Storage documentation</a>.</p>
            access_tier: <p>Specifies the access tier that you want your objects or files transferred into. This only applies when using the location as a transfer destination. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers">Access tiers</a>.</p>
            agent_arns: <p>(Optional) Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect with your Azure Blob Storage container. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.</p> <p>You can specify more than one agent. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html">Using multiple agents for your transfer</a>.</p> <note> <p>You cannot add or remove agents from a storage location after you initially create it.</p> </note>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>
            custom_secret_config: <p>Specifies configuration information for a customer-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_azure_blob_request.UpdateLocationAzureBlobRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_azure_blob_response.UpdateLocationAzureBlobResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_azure_blob

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_azure_blob.update_location_azure_blob(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_azure_blob_request.UpdateLocationAzureBlobRequest = {
            "location_arn": location_arn
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if authentication_type is not None:
            input_["authentication_type"] = authentication_type
        if sas_configuration is not None:
            input_["sas_configuration"] = sas_configuration
        if blob_type is not None:
            input_["blob_type"] = blob_type
        if access_tier is not None:
            input_["access_tier"] = access_tier
        if agent_arns is not None:
            input_["agent_arns"] = agent_arns
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_efs(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.efs_subdirectory.EfsSubdirectory"
        ] = None,
        access_point_arn: Optional[
            "capo_datasync.types.updated_efs_access_point_arn.UpdatedEfsAccessPointArn"
        ] = None,
        file_system_access_role_arn: Optional[
            "capo_datasync.types.updated_efs_iam_role_arn.UpdatedEfsIamRoleArn"
        ] = None,
        in_transit_encryption: Optional[
            "capo_datasync.types.efs_in_transit_encryption.EfsInTransitEncryption"
        ] = None,
    ) -> "capo_datasync.types.update_location_efs_response.UpdateLocationEfsResponse":
        """<p>Modifies the following configuration parameters of the Amazon EFS transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html">Configuring DataSync transfers with Amazon EFS</a>.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the Amazon EFS transfer location that you're updating.</p>
            subdirectory: <p>Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data on your file system (depending on if this is a source or destination location).</p> <p>By default, DataSync uses the root directory (or <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html">access point</a> if you provide one by using <code>AccessPointArn</code>). You can also include subdirectories using forward slashes (for example, <code>/path/to/folder</code>).</p>
            access_point_arn: <p>Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to mount your Amazon EFS file system.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam">Accessing restricted Amazon EFS file systems</a>.</p>
            file_system_access_role_arn: <p>Specifies an Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.</p> <p>For information on creating this role, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam-role">Creating a DataSync IAM role for Amazon EFS file system access</a>.</p>
            in_transit_encryption: <p>Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it transfers data to or from your Amazon EFS file system.</p> <p>If you specify an access point using <code>AccessPointArn</code> or an IAM role using <code>FileSystemAccessRoleArn</code>, you must set this parameter to <code>TLS1_2</code>.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_efs_request.UpdateLocationEfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_efs_response.UpdateLocationEfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_efs

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_efs.update_location_efs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_efs_request.UpdateLocationEfsRequest = {
            "location_arn": location_arn
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if access_point_arn is not None:
            input_["access_point_arn"] = access_point_arn
        if file_system_access_role_arn is not None:
            input_["file_system_access_role_arn"] = file_system_access_role_arn
        if in_transit_encryption is not None:
            input_["in_transit_encryption"] = in_transit_encryption

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_fsx_lustre(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.smb_subdirectory.SmbSubdirectory"
        ] = None,
    ) -> "capo_datasync.types.update_location_fsx_lustre_response.UpdateLocationFsxLustreResponse":
        """<p>Modifies the following configuration parameters of the Amazon FSx for Lustre transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-lustre-location.html">Configuring DataSync transfers with FSx for Lustre</a>.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the FSx for Lustre transfer location that you're updating.</p>
            subdirectory: <p>Specifies a mount path for your FSx for Lustre file system. The path can include subdirectories.</p> <p>When the location is used as a source, DataSync reads data from the mount path. When the location is used as a destination, DataSync writes data to the mount path. If you don't include this parameter, DataSync uses the file system's root directory (<code>/</code>).</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_fsx_lustre_request.UpdateLocationFsxLustreRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_fsx_lustre_response.UpdateLocationFsxLustreResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_fsx_lustre

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_fsx_lustre.update_location_fsx_lustre(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_fsx_lustre_request.UpdateLocationFsxLustreRequest = {
            "location_arn": location_arn
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_fsx_ontap(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        protocol: Optional[
            "capo_datasync.types.fsx_update_protocol.FsxUpdateProtocol"
        ] = None,
        subdirectory: Optional[
            "capo_datasync.types.fsx_ontap_subdirectory.FsxOntapSubdirectory"
        ] = None,
    ) -> "capo_datasync.types.update_location_fsx_ontap_response.UpdateLocationFsxOntapResponse":
        """<p>Modifies the following configuration parameters of the Amazon FSx for NetApp ONTAP transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html">Configuring DataSync transfers with FSx for ONTAP</a>.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the FSx for ONTAP transfer location that you're updating.</p>
            protocol: <p>Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.</p>
            subdirectory: <p>Specifies a path to the file share in the storage virtual machine (SVM) where you want to transfer data to or from.</p> <p>You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be <code>/vol1</code>, <code>/vol1/tree1</code>, or <code>/share1</code>.</p> <note> <p>Don't specify a junction path in the SVM's root volume. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html">Managing FSx for ONTAP storage virtual machines</a> in the <i>Amazon FSx for NetApp ONTAP User Guide</i>.</p> </note>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_fsx_ontap_request.UpdateLocationFsxOntapRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_fsx_ontap_response.UpdateLocationFsxOntapResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_fsx_ontap

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_fsx_ontap.update_location_fsx_ontap(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_fsx_ontap_request.UpdateLocationFsxOntapRequest = {
            "location_arn": location_arn
        }
        if protocol is not None:
            input_["protocol"] = protocol
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_fsx_open_zfs(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        protocol: Optional["capo_datasync.types.fsx_protocol.FsxProtocol"] = None,
        subdirectory: Optional[
            "capo_datasync.types.smb_subdirectory.SmbSubdirectory"
        ] = None,
    ) -> "capo_datasync.types.update_location_fsx_open_zfs_response.UpdateLocationFsxOpenZfsResponse":
        """<p>Modifies the following configuration parameters of the Amazon FSx for OpenZFS transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-openzfs-location.html">Configuring DataSync transfers with FSx for OpenZFS</a>.</p> <note> <p>Request parameters related to <code>SMB</code> aren't supported with the <code>UpdateLocationFsxOpenZfs</code> operation.</p> </note>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the FSx for OpenZFS transfer location that you're updating.</p>
            subdirectory: <p>Specifies a subdirectory in the location's path that must begin with <code>/fsx</code>. DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_fsx_open_zfs_request.UpdateLocationFsxOpenZfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_fsx_open_zfs_response.UpdateLocationFsxOpenZfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_fsx_open_zfs

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_fsx_open_zfs.update_location_fsx_open_zfs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_fsx_open_zfs_request.UpdateLocationFsxOpenZfsRequest = {
            "location_arn": location_arn
        }
        if protocol is not None:
            input_["protocol"] = protocol
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_fsx_windows(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.fsx_windows_subdirectory.FsxWindowsSubdirectory"
        ] = None,
        domain: Optional[
            "capo_datasync.types.update_smb_domain.UpdateSmbDomain"
        ] = None,
        user: Optional["capo_datasync.types.smb_user.SmbUser"] = None,
        password: Optional["capo_datasync.types.smb_password.SmbPassword"] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
    ) -> "capo_datasync.types.update_location_fsx_windows_response.UpdateLocationFsxWindowsResponse":
        """<p>Modifies the following configuration parameters of the Amazon FSx for Windows File Server transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html">Configuring DataSync transfers with FSx for Windows File Server</a>.</p>

        Args:
            location_arn: <p>Specifies the ARN of the FSx for Windows File Server transfer location that you're updating.</p>
            subdirectory: <p>Specifies a mount path for your file system using forward slashes. DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).</p>
            domain: <p>Specifies the name of the Windows domain that your FSx for Windows File Server file system belongs to.</p> <p>If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file system.</p>
            user: <p>Specifies the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.</p> <p>For information about choosing a user with the right level of access for your transfer, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#create-fsx-windows-location-permissions">required permissions</a> for FSx for Windows File Server locations.</p>
            password: <p>Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.</p>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, such as a <code>Password</code> or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>
            custom_secret_config: <p>Specifies configuration information for a customer-managed secret, such as a <code>Password</code> or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_fsx_windows_request.UpdateLocationFsxWindowsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_fsx_windows_response.UpdateLocationFsxWindowsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_fsx_windows

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_fsx_windows.update_location_fsx_windows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_fsx_windows_request.UpdateLocationFsxWindowsRequest = {
            "location_arn": location_arn
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if domain is not None:
            input_["domain"] = domain
        if user is not None:
            input_["user"] = user
        if password is not None:
            input_["password"] = password
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_hdfs(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.hdfs_subdirectory.HdfsSubdirectory"
        ] = None,
        name_nodes: Optional[
            "capo_datasync.types.hdfs_name_node_list.HdfsNameNodeList"
        ] = None,
        block_size: Optional[
            "capo_datasync.types.hdfs_block_size.HdfsBlockSize"
        ] = None,
        replication_factor: Optional[
            "capo_datasync.types.hdfs_replication_factor.HdfsReplicationFactor"
        ] = None,
        kms_key_provider_uri: Optional[
            "capo_datasync.types.kms_key_provider_uri.KmsKeyProviderUri"
        ] = None,
        qop_configuration: Optional[
            "capo_datasync.types.qop_configuration.QopConfiguration"
        ] = None,
        authentication_type: Optional[
            "capo_datasync.types.hdfs_authentication_type.HdfsAuthenticationType"
        ] = None,
        simple_user: Optional["capo_datasync.types.hdfs_user.HdfsUser"] = None,
        kerberos_principal: Optional[
            "capo_datasync.types.kerberos_principal.KerberosPrincipal"
        ] = None,
        kerberos_keytab: Optional[
            "capo_datasync.types.kerberos_keytab_file.KerberosKeytabFile"
        ] = None,
        kerberos_krb5_conf: Optional[
            "capo_datasync.types.kerberos_krb5_conf_file.KerberosKrb5ConfFile"
        ] = None,
        agent_arns: Optional["capo_datasync.types.agent_arn_list.AgentArnList"] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
    ) -> "capo_datasync.types.update_location_hdfs_response.UpdateLocationHdfsResponse":
        """<p>Modifies the following configuration parameters of the Hadoop Distributed File System (HDFS) transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-hdfs-location.html">Configuring DataSync transfers with an HDFS cluster</a>.</p>

        Args:
            location_arn: <p>The Amazon Resource Name (ARN) of the source HDFS cluster location.</p>
            subdirectory: <p>A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write data to the HDFS cluster.</p>
            name_nodes: <p>The NameNode that manages the HDFS namespace. The NameNode performs operations such as opening, closing, and renaming files and directories. The NameNode contains the information to map blocks of data to the DataNodes.</p> <p>The number of NameNodes you can specify depends on the task mode:</p> <ul> <li> <p>Enhanced mode – You can specify multiple NameNodes for HDFS High Availability (HA) configurations.</p> </li> <li> <p>Basic mode – You can specify only one NameNode.</p> </li> </ul>
            block_size: <p>The size of the data blocks to write into the HDFS cluster. </p>
            replication_factor: <p>The number of DataNodes to replicate the data to when writing to the HDFS cluster. </p>
            kms_key_provider_uri: <p>The URI of the HDFS cluster's Key Management Server (KMS). </p>
            qop_configuration: <p>The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer privacy settings configured on the Hadoop Distributed File System (HDFS) cluster. </p>
            authentication_type: <p>The type of authentication used to determine the identity of the user. </p>
            simple_user: <p>The user name used to identify the client on the host operating system.</p>
            kerberos_principal: <p>The Kerberos principal with access to the files and folders on the HDFS cluster. </p>
            kerberos_keytab: <p>The Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and the encrypted keys. You can load the keytab from a file by providing the file's address.</p>
            kerberos_krb5_conf: <p>The <code>krb5.conf</code> file that contains the Kerberos configuration information. You can load the <code>krb5.conf</code> file by providing the file's address. If you're using the CLI, it performs the base64 encoding for you. Otherwise, provide the base64-encoded text.</p>
            agent_arns: <p>The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your HDFS cluster.</p>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, such as a <code>KerberosKeytab</code> or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>
            custom_secret_config: <p>Specifies configuration information for a customer-managed secret, such as a <code>KerberosKeytab</code> or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_hdfs_request.UpdateLocationHdfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_hdfs_response.UpdateLocationHdfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_hdfs

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_hdfs.update_location_hdfs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_hdfs_request.UpdateLocationHdfsRequest = {
            "location_arn": location_arn
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if name_nodes is not None:
            input_["name_nodes"] = name_nodes
        if block_size is not None:
            input_["block_size"] = block_size
        if replication_factor is not None:
            input_["replication_factor"] = replication_factor
        if kms_key_provider_uri is not None:
            input_["kms_key_provider_uri"] = kms_key_provider_uri
        if qop_configuration is not None:
            input_["qop_configuration"] = qop_configuration
        if authentication_type is not None:
            input_["authentication_type"] = authentication_type
        if simple_user is not None:
            input_["simple_user"] = simple_user
        if kerberos_principal is not None:
            input_["kerberos_principal"] = kerberos_principal
        if kerberos_keytab is not None:
            input_["kerberos_keytab"] = kerberos_keytab
        if kerberos_krb5_conf is not None:
            input_["kerberos_krb5_conf"] = kerberos_krb5_conf
        if agent_arns is not None:
            input_["agent_arns"] = agent_arns
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_nfs(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.nfs_subdirectory.NfsSubdirectory"
        ] = None,
        server_hostname: Optional[
            "capo_datasync.types.server_hostname.ServerHostname"
        ] = None,
        on_prem_config: Optional[
            "capo_datasync.types.on_prem_config.OnPremConfig"
        ] = None,
        mount_options: Optional[
            "capo_datasync.types.nfs_mount_options.NfsMountOptions"
        ] = None,
    ) -> "capo_datasync.types.update_location_nfs_response.UpdateLocationNfsResponse":
        """<p>Modifies the following configuration parameters of the Network File System (NFS) transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html">Configuring transfers with an NFS file server</a>.</p>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the NFS transfer location that you want to update.</p>
            subdirectory: <p>Specifies the export path in your NFS file server that you want DataSync to mount.</p> <p>This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs">Accessing NFS file servers</a>.</p>
            server_hostname: <p>Specifies the DNS name or IP address (IPv4 or IPv6) of the NFS file server that your DataSync agent connects to.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_nfs_request.UpdateLocationNfsRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_nfs_response.UpdateLocationNfsResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_nfs

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_nfs.update_location_nfs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_nfs_request.UpdateLocationNfsRequest = {
            "location_arn": location_arn
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if server_hostname is not None:
            input_["server_hostname"] = server_hostname
        if on_prem_config is not None:
            input_["on_prem_config"] = on_prem_config
        if mount_options is not None:
            input_["mount_options"] = mount_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_object_storage(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        server_port: Optional[
            "capo_datasync.types.object_storage_server_port.ObjectStorageServerPort"
        ] = None,
        server_protocol: Optional[
            "capo_datasync.types.object_storage_server_protocol.ObjectStorageServerProtocol"
        ] = None,
        subdirectory: Optional[
            "capo_datasync.types.s3_subdirectory.S3Subdirectory"
        ] = None,
        server_hostname: Optional[
            "capo_datasync.types.server_hostname.ServerHostname"
        ] = None,
        access_key: Optional[
            "capo_datasync.types.object_storage_access_key.ObjectStorageAccessKey"
        ] = None,
        secret_key: Optional[
            "capo_datasync.types.object_storage_secret_key.ObjectStorageSecretKey"
        ] = None,
        agent_arns: Optional["capo_datasync.types.agent_arn_list.AgentArnList"] = None,
        server_certificate: Optional[
            "capo_datasync.types.object_storage_certificate.ObjectStorageCertificate"
        ] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
    ) -> "capo_datasync.types.update_location_object_storage_response.UpdateLocationObjectStorageResponse":
        """<p>Modifies the following configuration parameters of the object storage transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-object-location.html">Configuring DataSync transfers with an object storage system</a>.</p>

        Args:
            location_arn: <p>Specifies the ARN of the object storage system location that you're updating.</p>
            server_port: <p>Specifies the port that your object storage server accepts inbound network traffic on (for example, port 443).</p>
            server_protocol: <p>Specifies the protocol that your object storage server uses to communicate.</p>
            subdirectory: <p>Specifies the object prefix for your object storage server. If this is a source location, DataSync only copies objects with this prefix. If this is a destination location, DataSync writes all objects with this prefix.</p>
            server_hostname: <p>Specifies the domain name or IP address (IPv4 or IPv6) of the object storage server that your DataSync agent connects to.</p>
            access_key: <p>Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.</p>
            secret_key: <p>Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.</p> <note> <p>If you provide a secret using <code>SecretKey</code>, but do not provide secret configuration details using <code>CmkSecretConfig</code> or <code>CustomSecretConfig</code>, then DataSync stores the token using your Amazon Web Services account's Secrets Manager secret.</p> </note>
            agent_arns: <p>(Optional) Specifies the Amazon Resource Names (ARNs) of the DataSync agents that can connect with your object storage system. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.</p> <note> <p>You cannot add or remove agents from a storage location after you initially create it.</p> </note>
            server_certificate: <p>Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA). You must specify a single <code>.pem</code> file with a full certificate chain (for example, <code>file:///home/user/.ssh/object_storage_certificates.pem</code>).</p> <p>The certificate chain might include:</p> <ul> <li> <p>The object storage system's certificate</p> </li> <li> <p>All intermediate certificates (if there are any)</p> </li> <li> <p>The root certificate of the signing CA</p> </li> </ul> <p>You can concatenate your certificates into a <code>.pem</code> file (which can be up to 32768 bytes before base64 encoding). The following example <code>cat</code> command creates an <code>object_storage_certificates.pem</code> file that includes three certificates:</p> <p> <code>cat object_server_certificate.pem intermediate_certificate.pem ca_root_certificate.pem > object_storage_certificates.pem</code> </p> <p>To use this parameter, configure <code>ServerProtocol</code> to <code>HTTPS</code>.</p> <p>Updating this parameter doesn't interfere with tasks that you have in progress.</p>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>
            custom_secret_config: <p>Specifies configuration information for a customer-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_object_storage_request.UpdateLocationObjectStorageRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_object_storage_response.UpdateLocationObjectStorageResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_object_storage

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_object_storage.update_location_object_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_object_storage_request.UpdateLocationObjectStorageRequest = {
            "location_arn": location_arn
        }
        if server_port is not None:
            input_["server_port"] = server_port
        if server_protocol is not None:
            input_["server_protocol"] = server_protocol
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if server_hostname is not None:
            input_["server_hostname"] = server_hostname
        if access_key is not None:
            input_["access_key"] = access_key
        if secret_key is not None:
            input_["secret_key"] = secret_key
        if agent_arns is not None:
            input_["agent_arns"] = agent_arns
        if server_certificate is not None:
            input_["server_certificate"] = server_certificate
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_s3(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.s3_subdirectory.S3Subdirectory"
        ] = None,
        s3_storage_class: Optional[
            "capo_datasync.types.s3_storage_class.S3StorageClass"
        ] = None,
        s3_config: Optional["capo_datasync.types.s3_config.S3Config"] = None,
    ) -> "capo_datasync.types.update_location_s3_response.UpdateLocationS3Response":
        """<p>Modifies the following configuration parameters of the Amazon S3 transfer location that you're using with DataSync.</p> <important> <p>Before you begin, make sure that you read the following topics:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Storage class considerations with Amazon S3 locations</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests">Evaluating S3 request costs when using DataSync</a> </p> </li> </ul> </important>

        Args:
            location_arn: <p>Specifies the Amazon Resource Name (ARN) of the Amazon S3 transfer location that you're updating.</p>
            subdirectory: <p>Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location).</p> <note> <p>DataSync can't transfer objects with a prefix that begins with a slash (<code>/</code>) or includes <code>//</code>, <code>/./</code>, or <code>/../</code> patterns. For example:</p> <ul> <li> <p> <code>/photos</code> </p> </li> <li> <p> <code>photos//2006/January</code> </p> </li> <li> <p> <code>photos/./2006/February</code> </p> </li> <li> <p> <code>photos/../2006/March</code> </p> </li> </ul> </note>
            s3_storage_class: <p>Specifies the storage class that you want your objects to use when Amazon S3 is a transfer destination.</p> <p>For buckets in Amazon Web Services Regions, the storage class defaults to <code>STANDARD</code>. For buckets on Outposts, the storage class defaults to <code>OUTPOSTS</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Storage class considerations with Amazon S3 transfers</a>.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_s3_request.UpdateLocationS3Request]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_s3_response.UpdateLocationS3Response"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_s3

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_s3.update_location_s3(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_s3_request.UpdateLocationS3Request = {
            "location_arn": location_arn
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if s3_storage_class is not None:
            input_["s3_storage_class"] = s3_storage_class
        if s3_config is not None:
            input_["s3_config"] = s3_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_location_smb(
        self,
        location_arn: "capo_datasync.types.location_arn.LocationArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        subdirectory: Optional[
            "capo_datasync.types.smb_subdirectory.SmbSubdirectory"
        ] = None,
        server_hostname: Optional[
            "capo_datasync.types.server_hostname.ServerHostname"
        ] = None,
        user: Optional["capo_datasync.types.smb_user.SmbUser"] = None,
        domain: Optional["capo_datasync.types.smb_domain.SmbDomain"] = None,
        password: Optional["capo_datasync.types.smb_password.SmbPassword"] = None,
        cmk_secret_config: Optional[
            "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
        ] = None,
        custom_secret_config: Optional[
            "capo_datasync.types.custom_secret_config.CustomSecretConfig"
        ] = None,
        agent_arns: Optional["capo_datasync.types.agent_arn_list.AgentArnList"] = None,
        mount_options: Optional[
            "capo_datasync.types.smb_mount_options.SmbMountOptions"
        ] = None,
        authentication_type: Optional[
            "capo_datasync.types.smb_authentication_type.SmbAuthenticationType"
        ] = None,
        dns_ip_addresses: Optional["capo_datasync.types.dns_ip_list.DnsIpList"] = None,
        kerberos_principal: Optional[
            "capo_datasync.types.kerberos_principal.KerberosPrincipal"
        ] = None,
        kerberos_keytab: Optional[
            "capo_datasync.types.kerberos_keytab_file.KerberosKeytabFile"
        ] = None,
        kerberos_krb5_conf: Optional[
            "capo_datasync.types.kerberos_krb5_conf_file.KerberosKrb5ConfFile"
        ] = None,
    ) -> "capo_datasync.types.update_location_smb_response.UpdateLocationSmbResponse":
        """<p>Modifies the following configuration parameters of the Server Message Block (SMB) transfer location that you're using with DataSync.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html">Configuring DataSync transfers with an SMB file server</a>.</p>

        Args:
            location_arn: <p>Specifies the ARN of the SMB location that you want to update.</p>
            subdirectory: <p>Specifies the name of the share exported by your SMB file server where DataSync will read or write data. You can include a subdirectory in the share path (for example, <code>/path/to/subdirectory</code>). Make sure that other SMB clients in your network can also mount this path.</p> <p>To copy all data in the specified subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions">Providing DataSync access to SMB file servers</a>.</p>
            server_hostname: <p>Specifies the domain name or IP address (IPv4 or IPv6) of the SMB file server that your DataSync agent connects to.</p> <note> <p>If you're using Kerberos authentication, you must specify a domain name.</p> </note>
            user: <p>Specifies the user name that can mount your SMB file server and has permission to access the files and folders involved in your transfer. This parameter applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p> <p>For information about choosing a user with the right level of access for your transfer, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions">Providing DataSync access to SMB file servers</a>.</p>
            domain: <p>Specifies the Windows domain name that your SMB file server belongs to. This parameter applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p> <p>If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right file server.</p>
            password: <p>Specifies the password of the user who can mount your SMB file server and has permission to access the files and folders involved in your transfer. This parameter applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p>
            cmk_secret_config: <p>Specifies configuration information for a DataSync-managed secret, such as a <code>Password</code> or <code>KerberosKeytab</code> or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>
            custom_secret_config: <p>Specifies configuration information for a customer-managed secret, such as a <code>Password</code> or <code>KerberosKeytab</code> or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>
            agent_arns: <p>Specifies the DataSync agent (or agents) that can connect to your SMB file server. You specify an agent by using its Amazon Resource Name (ARN).</p>
            authentication_type: <p>Specifies the authentication protocol that DataSync uses to connect to your SMB file server. DataSync supports <code>NTLM</code> (default) and <code>KERBEROS</code> authentication.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions">Providing DataSync access to SMB file servers</a>.</p>
            dns_ip_addresses: <p>Specifies the IP addresses (IPv4 or IPv6) for the DNS servers that your SMB file server belongs to. This parameter applies only if <code>AuthenticationType</code> is set to <code>KERBEROS</code>.</p> <p>If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right SMB file server. </p>
            kerberos_principal: <p>Specifies a Kerberos prinicpal, which is an identity in your Kerberos realm that has permission to access the files, folders, and file metadata in your SMB file server.</p> <p>A Kerberos principal might look like <code>HOST/kerberosuser@MYDOMAIN.ORG</code>.</p> <p>Principal names are case sensitive. Your DataSync task execution will fail if the principal that you specify for this parameter doesn’t exactly match the principal that you use to create the keytab file.</p>
            kerberos_keytab: <p>Specifies your Kerberos key table (keytab) file, which includes mappings between your Kerberos principal and encryption keys.</p> <p>To avoid task execution errors, make sure that the Kerberos principal that you use to create the keytab file matches exactly what you specify for <code>KerberosPrincipal</code>.</p>
            kerberos_krb5_conf: <p>Specifies a Kerberos configuration file (<code>krb5.conf</code>) that defines your Kerberos realm configuration.</p> <p>The file must be base64 encoded. If you're using the CLI, the encoding is done for you.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_location_smb_request.UpdateLocationSmbRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_location_smb_response.UpdateLocationSmbResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_location_smb

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_location_smb.update_location_smb(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_location_smb_request.UpdateLocationSmbRequest = {
            "location_arn": location_arn
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory
        if server_hostname is not None:
            input_["server_hostname"] = server_hostname
        if user is not None:
            input_["user"] = user
        if domain is not None:
            input_["domain"] = domain
        if password is not None:
            input_["password"] = password
        if cmk_secret_config is not None:
            input_["cmk_secret_config"] = cmk_secret_config
        if custom_secret_config is not None:
            input_["custom_secret_config"] = custom_secret_config
        if agent_arns is not None:
            input_["agent_arns"] = agent_arns
        if mount_options is not None:
            input_["mount_options"] = mount_options
        if authentication_type is not None:
            input_["authentication_type"] = authentication_type
        if dns_ip_addresses is not None:
            input_["dns_ip_addresses"] = dns_ip_addresses
        if kerberos_principal is not None:
            input_["kerberos_principal"] = kerberos_principal
        if kerberos_keytab is not None:
            input_["kerberos_keytab"] = kerberos_keytab
        if kerberos_krb5_conf is not None:
            input_["kerberos_krb5_conf"] = kerberos_krb5_conf

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_task(
        self,
        task_arn: "capo_datasync.types.task_arn.TaskArn",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
        options: Optional["capo_datasync.types.options.Options"] = None,
        excludes: Optional["capo_datasync.types.filter_list.FilterList"] = None,
        schedule: Optional["capo_datasync.types.task_schedule.TaskSchedule"] = None,
        name: Optional["capo_datasync.types.tag_value.TagValue"] = None,
        cloud_watch_log_group_arn: Optional[
            "capo_datasync.types.log_group_arn.LogGroupArn"
        ] = None,
        includes: Optional["capo_datasync.types.filter_list.FilterList"] = None,
        manifest_config: Optional[
            "capo_datasync.types.manifest_config.ManifestConfig"
        ] = None,
        task_report_config: Optional[
            "capo_datasync.types.task_report_config.TaskReportConfig"
        ] = None,
    ) -> "capo_datasync.types.update_task_response.UpdateTaskResponse":
        """<p>Updates the configuration of a <i>task</i>, which defines where and how DataSync transfers your data.</p>

        Args:
            task_arn: <p>Specifies the ARN of the task that you want to update.</p>
            excludes: <p>Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>
            schedule: <p>Specifies a schedule for when you want your task to run. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html">Scheduling your task</a>.</p>
            name: <p>Specifies the name of your task.</p>
            cloud_watch_log_group_arn: <p>Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.</p> <p>For Enhanced mode tasks, you must use <code>/aws/datasync</code> as your log group name. For example:</p> <p> <code>arn:aws:logs:us-east-1:111222333444:log-group:/aws/datasync:*</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html">Monitoring data transfers with CloudWatch Logs</a>.</p>
            includes: <p>Specifies include filters define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>
            manifest_config: <p>Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html">Specifying what DataSync transfers by using a manifest</a>.</p> <p>When using this parameter, your caller identity (the IAM role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a manifest configuration, specify this parameter as empty.</p>
            task_report_config: <p>Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html">Monitoring your DataSync transfers with task reports</a>.</p> <p>When using this parameter, your caller identity (the IAM role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a task report configuration, specify this parameter as empty.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_task_request.UpdateTaskRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_task_response.UpdateTaskResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_task

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_task.update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_task_request.UpdateTaskRequest = {
            "task_arn": task_arn
        }
        if options is not None:
            input_["options"] = options
        if excludes is not None:
            input_["excludes"] = excludes
        if schedule is not None:
            input_["schedule"] = schedule
        if name is not None:
            input_["name"] = name
        if cloud_watch_log_group_arn is not None:
            input_["cloud_watch_log_group_arn"] = cloud_watch_log_group_arn
        if includes is not None:
            input_["includes"] = includes
        if manifest_config is not None:
            input_["manifest_config"] = manifest_config
        if task_report_config is not None:
            input_["task_report_config"] = task_report_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_task_execution(
        self,
        task_execution_arn: "capo_datasync.types.task_execution_arn.TaskExecutionArn",
        options: "capo_datasync.types.options.Options",
        *,
        config_overrides: Optional[DataSyncClientConfig] = None,
    ) -> (
        "capo_datasync.types.update_task_execution_response.UpdateTaskExecutionResponse"
    ):
        """<p>Updates the configuration of a running DataSync task execution.</p> <note> <p>Currently, the only <code>Option</code> that you can modify with <code>UpdateTaskExecution</code> is <code> <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-BytesPerSecond">BytesPerSecond</a> </code>, which throttles bandwidth for a running or queued task execution.</p> </note>

        Args:
            task_execution_arn: <p>Specifies the Amazon Resource Name (ARN) of the task execution that you're updating.</p>

        Raises:
            capo_datasync.errors.internal_exception.InternalException: <p>This exception is thrown when an error occurs in the DataSync service.</p>
            capo_datasync.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_datasync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datasync.types.update_task_execution_request.UpdateTaskExecutionRequest]",
        ) -> OperationResponse[
            "capo_datasync.types.update_task_execution_response.UpdateTaskExecutionResponse"
        ]:
            import capo_datasync._operations.fmrs_service.update_task_execution

            output, http_response = (
                capo_datasync._operations.fmrs_service.update_task_execution.update_task_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datasync.types.update_task_execution_request.UpdateTaskExecutionRequest = {
            "task_execution_arn": task_execution_arn,
            "options": options,
        }

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
