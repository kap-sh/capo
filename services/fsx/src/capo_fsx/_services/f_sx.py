"""Generated from Smithy shape ``com.amazonaws.fsx#AWSSimbaAPIService_v20180301``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_fsx._auth._signers
import capo_fsx._auth._sigv4
from capo_fsx._auth._identity import Credentials
from capo_fsx._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_fsx._auth._zapros_handler import AuthMiddleware
from capo_fsx._pagination import resolve_path as _resolve_path
from capo_fsx._services._aws_config import aws_config
from capo_fsx._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_fsx.types.admin_password
    import capo_fsx.types.alternate_dns_names
    import capo_fsx.types.archive_path
    import capo_fsx.types.associate_file_system_aliases_request
    import capo_fsx.types.associate_file_system_aliases_response
    import capo_fsx.types.backup_id
    import capo_fsx.types.backup_ids
    import capo_fsx.types.batch_import_meta_data_on_create
    import capo_fsx.types.cancel_data_repository_task_request
    import capo_fsx.types.cancel_data_repository_task_response
    import capo_fsx.types.capacity_to_release
    import capo_fsx.types.client_request_token
    import capo_fsx.types.completion_report
    import capo_fsx.types.copy_backup_request
    import capo_fsx.types.copy_backup_response
    import capo_fsx.types.copy_snapshot_and_update_volume_request
    import capo_fsx.types.copy_snapshot_and_update_volume_response
    import capo_fsx.types.copy_tags_to_data_repository_associations
    import capo_fsx.types.create_and_attach_s3_access_point_ontap_configuration
    import capo_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration
    import capo_fsx.types.create_and_attach_s3_access_point_request
    import capo_fsx.types.create_and_attach_s3_access_point_response
    import capo_fsx.types.create_and_attach_s3_access_point_s3_configuration
    import capo_fsx.types.create_backup_request
    import capo_fsx.types.create_backup_response
    import capo_fsx.types.create_data_repository_association_request
    import capo_fsx.types.create_data_repository_association_response
    import capo_fsx.types.create_data_repository_task_request
    import capo_fsx.types.create_data_repository_task_response
    import capo_fsx.types.create_file_cache_data_repository_associations
    import capo_fsx.types.create_file_cache_lustre_configuration
    import capo_fsx.types.create_file_cache_request
    import capo_fsx.types.create_file_cache_response
    import capo_fsx.types.create_file_system_from_backup_request
    import capo_fsx.types.create_file_system_from_backup_response
    import capo_fsx.types.create_file_system_lustre_configuration
    import capo_fsx.types.create_file_system_ontap_configuration
    import capo_fsx.types.create_file_system_open_zfs_configuration
    import capo_fsx.types.create_file_system_request
    import capo_fsx.types.create_file_system_response
    import capo_fsx.types.create_file_system_windows_configuration
    import capo_fsx.types.create_ontap_volume_configuration
    import capo_fsx.types.create_open_zfs_volume_configuration
    import capo_fsx.types.create_snapshot_request
    import capo_fsx.types.create_snapshot_response
    import capo_fsx.types.create_storage_virtual_machine_request
    import capo_fsx.types.create_storage_virtual_machine_response
    import capo_fsx.types.create_svm_active_directory_configuration
    import capo_fsx.types.create_volume_from_backup_request
    import capo_fsx.types.create_volume_from_backup_response
    import capo_fsx.types.create_volume_request
    import capo_fsx.types.create_volume_response
    import capo_fsx.types.data_repository_association_id
    import capo_fsx.types.data_repository_association_ids
    import capo_fsx.types.data_repository_task_filters
    import capo_fsx.types.data_repository_task_paths
    import capo_fsx.types.data_repository_task_type
    import capo_fsx.types.delete_backup_request
    import capo_fsx.types.delete_backup_response
    import capo_fsx.types.delete_data_in_file_system
    import capo_fsx.types.delete_data_repository_association_request
    import capo_fsx.types.delete_data_repository_association_response
    import capo_fsx.types.delete_file_cache_request
    import capo_fsx.types.delete_file_cache_response
    import capo_fsx.types.delete_file_system_lustre_configuration
    import capo_fsx.types.delete_file_system_open_zfs_configuration
    import capo_fsx.types.delete_file_system_request
    import capo_fsx.types.delete_file_system_response
    import capo_fsx.types.delete_file_system_windows_configuration
    import capo_fsx.types.delete_snapshot_request
    import capo_fsx.types.delete_snapshot_response
    import capo_fsx.types.delete_storage_virtual_machine_request
    import capo_fsx.types.delete_storage_virtual_machine_response
    import capo_fsx.types.delete_volume_ontap_configuration
    import capo_fsx.types.delete_volume_open_zfs_configuration
    import capo_fsx.types.delete_volume_request
    import capo_fsx.types.delete_volume_response
    import capo_fsx.types.describe_backups_request
    import capo_fsx.types.describe_backups_response
    import capo_fsx.types.describe_data_repository_associations_request
    import capo_fsx.types.describe_data_repository_associations_response
    import capo_fsx.types.describe_data_repository_tasks_request
    import capo_fsx.types.describe_data_repository_tasks_response
    import capo_fsx.types.describe_file_caches_request
    import capo_fsx.types.describe_file_caches_response
    import capo_fsx.types.describe_file_system_aliases_request
    import capo_fsx.types.describe_file_system_aliases_response
    import capo_fsx.types.describe_file_systems_request
    import capo_fsx.types.describe_file_systems_response
    import capo_fsx.types.describe_s3_access_point_attachments_request
    import capo_fsx.types.describe_s3_access_point_attachments_response
    import capo_fsx.types.describe_shared_vpc_configuration_request
    import capo_fsx.types.describe_shared_vpc_configuration_response
    import capo_fsx.types.describe_snapshots_request
    import capo_fsx.types.describe_snapshots_response
    import capo_fsx.types.describe_storage_virtual_machines_request
    import capo_fsx.types.describe_storage_virtual_machines_response
    import capo_fsx.types.describe_volumes_request
    import capo_fsx.types.describe_volumes_response
    import capo_fsx.types.detach_and_delete_s3_access_point_request
    import capo_fsx.types.detach_and_delete_s3_access_point_response
    import capo_fsx.types.disassociate_file_system_aliases_request
    import capo_fsx.types.disassociate_file_system_aliases_response
    import capo_fsx.types.file_cache_id
    import capo_fsx.types.file_cache_ids
    import capo_fsx.types.file_cache_type
    import capo_fsx.types.file_system_id
    import capo_fsx.types.file_system_ids
    import capo_fsx.types.file_system_type
    import capo_fsx.types.file_system_type_version
    import capo_fsx.types.filters
    import capo_fsx.types.flag
    import capo_fsx.types.include_shared
    import capo_fsx.types.kms_key_id
    import capo_fsx.types.limited_max_results
    import capo_fsx.types.list_tags_for_resource_request
    import capo_fsx.types.list_tags_for_resource_response
    import capo_fsx.types.max_results
    import capo_fsx.types.megabytes
    import capo_fsx.types.namespace
    import capo_fsx.types.network_type
    import capo_fsx.types.next_token
    import capo_fsx.types.open_zfs_copy_strategy
    import capo_fsx.types.region
    import capo_fsx.types.release_configuration
    import capo_fsx.types.release_file_system_nfs_v3_locks_request
    import capo_fsx.types.release_file_system_nfs_v3_locks_response
    import capo_fsx.types.resource_arn
    import capo_fsx.types.restore_open_zfs_volume_options
    import capo_fsx.types.restore_volume_from_snapshot_request
    import capo_fsx.types.restore_volume_from_snapshot_response
    import capo_fsx.types.s3_access_point_attachment
    import capo_fsx.types.s3_access_point_attachment_name
    import capo_fsx.types.s3_access_point_attachment_names
    import capo_fsx.types.s3_access_point_attachment_type
    import capo_fsx.types.s3_access_point_attachments_filters
    import capo_fsx.types.s3_data_repository_configuration
    import capo_fsx.types.security_group_ids
    import capo_fsx.types.snapshot
    import capo_fsx.types.snapshot_filters
    import capo_fsx.types.snapshot_id
    import capo_fsx.types.snapshot_ids
    import capo_fsx.types.snapshot_name
    import capo_fsx.types.source_backup_id
    import capo_fsx.types.start_misconfigured_state_recovery_request
    import capo_fsx.types.start_misconfigured_state_recovery_response
    import capo_fsx.types.storage_capacity
    import capo_fsx.types.storage_type
    import capo_fsx.types.storage_virtual_machine
    import capo_fsx.types.storage_virtual_machine_filters
    import capo_fsx.types.storage_virtual_machine_id
    import capo_fsx.types.storage_virtual_machine_ids
    import capo_fsx.types.storage_virtual_machine_name
    import capo_fsx.types.storage_virtual_machine_root_volume_security_style
    import capo_fsx.types.subnet_ids
    import capo_fsx.types.tag_keys
    import capo_fsx.types.tag_resource_request
    import capo_fsx.types.tag_resource_response
    import capo_fsx.types.tags
    import capo_fsx.types.task_id
    import capo_fsx.types.task_ids
    import capo_fsx.types.untag_resource_request
    import capo_fsx.types.untag_resource_response
    import capo_fsx.types.update_data_repository_association_request
    import capo_fsx.types.update_data_repository_association_response
    import capo_fsx.types.update_file_cache_lustre_configuration
    import capo_fsx.types.update_file_cache_request
    import capo_fsx.types.update_file_cache_response
    import capo_fsx.types.update_file_system_lustre_configuration
    import capo_fsx.types.update_file_system_ontap_configuration
    import capo_fsx.types.update_file_system_open_zfs_configuration
    import capo_fsx.types.update_file_system_request
    import capo_fsx.types.update_file_system_response
    import capo_fsx.types.update_file_system_windows_configuration
    import capo_fsx.types.update_ontap_volume_configuration
    import capo_fsx.types.update_open_zfs_volume_configuration
    import capo_fsx.types.update_open_zfs_volume_options
    import capo_fsx.types.update_shared_vpc_configuration_request
    import capo_fsx.types.update_shared_vpc_configuration_response
    import capo_fsx.types.update_snapshot_request
    import capo_fsx.types.update_snapshot_response
    import capo_fsx.types.update_storage_virtual_machine_request
    import capo_fsx.types.update_storage_virtual_machine_response
    import capo_fsx.types.update_svm_active_directory_configuration
    import capo_fsx.types.update_volume_request
    import capo_fsx.types.update_volume_response
    import capo_fsx.types.verbose_flag
    import capo_fsx.types.volume
    import capo_fsx.types.volume_filters
    import capo_fsx.types.volume_id
    import capo_fsx.types.volume_ids
    import capo_fsx.types.volume_name
    import capo_fsx.types.volume_type


class FSxClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class FSxClient:
    """A client for the ``FSx`` service.

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
        self._config = FSxClientConfig(
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
        self, config_overrides: Optional[FSxClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: FSxClientConfig = config_overrides or {}
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

    def associate_file_system_aliases(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        aliases: Optional[
            "capo_fsx.types.alternate_dns_names.AlternateDNSNames"
        ] = None,
    ) -> "capo_fsx.types.associate_file_system_aliases_response.AssociateFileSystemAliasesResponse":
        """<p>Use this action to associate one or more Domain Name Server (DNS) aliases with an existing Amazon FSx for Windows File Server file system. A file system can have a maximum of 50 DNS aliases associated with it at any one time. If you try to associate a DNS alias that is already associated with the file system, FSx takes no action on that alias in the request. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html">Working with DNS Aliases</a> and <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/walkthrough05-file-system-custom-CNAME.html">Walkthrough 5: Using DNS aliases to access your file system</a>, including additional steps you must take to be able to access your file system using a DNS alias.</p> <p>The system response shows the DNS aliases that Amazon FSx is attempting to associate with the file system. Use the API operation to monitor the status of the aliases Amazon FSx is associating with the file system.</p>

        Args:
            file_system_id: <p>Specifies the file system with which you want to associate one or more DNS aliases.</p>
            aliases: <p>An array of one or more DNS alias names to associate with the file system. The alias name has to comply with the following formatting requirements:</p> <ul> <li> <p>Formatted as a fully-qualified domain name (FQDN), <i> <code>hostname.domain</code> </i>, for example, <code>accounting.corp.example.com</code>.</p> </li> <li> <p>Can contain alphanumeric characters and the hyphen (-).</p> </li> <li> <p>Cannot start or end with a hyphen.</p> </li> <li> <p>Can start with a numeric.</p> </li> </ul> <p>For DNS alias names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.associate_file_system_aliases_request.AssociateFileSystemAliasesRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.associate_file_system_aliases_response.AssociateFileSystemAliasesResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.associate_file_system_aliases

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.associate_file_system_aliases.associate_file_system_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.associate_file_system_aliases_request.AssociateFileSystemAliasesRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if aliases is not None:
            input_["aliases"] = aliases

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_data_repository_task(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        task_id: Optional["capo_fsx.types.task_id.TaskId"] = None,
    ) -> "capo_fsx.types.cancel_data_repository_task_response.CancelDataRepositoryTaskResponse":
        """<p>Cancels an existing Amazon FSx for Lustre data repository task if that task is in either the <code>PENDING</code> or <code>EXECUTING</code> state. When you cancel an export task, Amazon FSx does the following.</p> <ul> <li> <p>Any files that FSx has already exported are not reverted.</p> </li> <li> <p>FSx continues to export any files that are in-flight when the cancel operation is received.</p> </li> <li> <p>FSx does not export any files that have not yet been exported.</p> </li> </ul> <p>For a release task, Amazon FSx will stop releasing files upon cancellation. Any files that have already been released will remain in the released state.</p>

        Args:
            task_id: <p>Specifies the data repository task to cancel.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.data_repository_task_ended.DataRepositoryTaskEnded: <p>The data repository task could not be canceled because the task has already ended.</p>
            capo_fsx.errors.data_repository_task_not_found.DataRepositoryTaskNotFound: <p>The data repository task or tasks you specified could not be found.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.cancel_data_repository_task_request.CancelDataRepositoryTaskRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.cancel_data_repository_task_response.CancelDataRepositoryTaskResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.cancel_data_repository_task

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.cancel_data_repository_task.cancel_data_repository_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.cancel_data_repository_task_request.CancelDataRepositoryTaskRequest = {}
        if task_id is not None:
            input_["task_id"] = task_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def copy_backup(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        source_backup_id: Optional[
            "capo_fsx.types.source_backup_id.SourceBackupId"
        ] = None,
        source_region: Optional["capo_fsx.types.region.Region"] = None,
        kms_key_id: Optional["capo_fsx.types.kms_key_id.KmsKeyId"] = None,
        copy_tags: Optional["capo_fsx.types.flag.Flag"] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
    ) -> "capo_fsx.types.copy_backup_response.CopyBackupResponse":
        """<p>Copies an existing backup within the same Amazon Web Services account to another Amazon Web Services Region (cross-Region copy) or within the same Amazon Web Services Region (in-Region copy). You can have up to five backup copy requests in progress to a single destination Region per account.</p> <p>You can use cross-Region backup copies for cross-Region disaster recovery. You can periodically take backups and copy them to another Region so that in the event of a disaster in the primary Region, you can restore from backup and recover availability quickly in the other Region. You can make cross-Region copies only within your Amazon Web Services partition. A partition is a grouping of Regions. Amazon Web Services currently has three partitions: <code>aws</code> (Standard Regions), <code>aws-cn</code> (China Regions), and <code>aws-us-gov</code> (Amazon Web Services GovCloud [US] Regions).</p> <p>You can also use backup copies to clone your file dataset to another Region or within the same Region.</p> <p>You can use the <code>SourceRegion</code> parameter to specify the Amazon Web Services Region from which the backup will be copied. For example, if you make the call from the <code>us-west-1</code> Region and want to copy a backup from the <code>us-east-2</code> Region, you specify <code>us-east-2</code> in the <code>SourceRegion</code> parameter to make a cross-Region copy. If you don't specify a Region, the backup copy is created in the same Region where the request is sent from (in-Region copy).</p> <p>For more information about creating backup copies, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html#copy-backups"> Copying backups</a> in the <i>Amazon FSx for Windows User Guide</i>, <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html#copy-backups">Copying backups</a> in the <i>Amazon FSx for Lustre User Guide</i>, and <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-backups.html#copy-backups">Copying backups</a> in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>

        Args:
            source_backup_id: <p>The ID of the source backup. Specifies the ID of the backup that's being copied.</p>
            source_region: <p>The source Amazon Web Services Region of the backup. Specifies the Amazon Web Services Region from which the backup is being copied. The source and destination Regions must be in the same Amazon Web Services partition. If you don't specify a Region, <code>SourceRegion</code> defaults to the Region where the request is sent from (in-Region copy).</p>
            copy_tags: <p>A Boolean flag indicating whether tags from the source backup should be copied to the backup copy. This value defaults to <code>false</code>.</p> <p>If you set <code>CopyTags</code> to <code>true</code> and the source backup has existing tags, you can use the <code>Tags</code> parameter to create new tags, provided that the sum of the source backup tags and the new tags doesn't exceed 50. Both sets of tags are merged. If there are tag conflicts (for example, two tags with the same key but different values), the tags created with the <code>Tags</code> parameter take precedence.</p>

        Raises:
            capo_fsx.errors.backup_not_found.BackupNotFound: <p>No Amazon FSx backups were found based upon the supplied parameters.</p>
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.incompatible_region_for_multi_az.IncompatibleRegionForMultiAZ: <p>Amazon FSx doesn't support Multi-AZ Windows File Server copy backup in the destination Region, so the copied backup can't be restored.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.invalid_destination_kms_key.InvalidDestinationKmsKey: <p>The Key Management Service (KMS) key of the destination backup is not valid.</p>
            capo_fsx.errors.invalid_region.InvalidRegion: <p>The Region provided for <code>SourceRegion</code> is not valid or is in a different Amazon Web Services partition.</p>
            capo_fsx.errors.invalid_source_kms_key.InvalidSourceKmsKey: <p>The Key Management Service (KMS) key of the source backup is not valid.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.source_backup_unavailable.SourceBackupUnavailable: <p>The request was rejected because the lifecycle status of the source backup isn't <code>AVAILABLE</code>.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To copy a backup
            This operation copies an Amazon FSx backup.

            >>> client.copy_backup(source_backup_id='backup-03e3c82e0183b7b6b', source_region='us-east-2')
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.copy_backup_request.CopyBackupRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.copy_backup_response.CopyBackupResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.copy_backup

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.copy_backup.copy_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.copy_backup_request.CopyBackupRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if source_backup_id is not None:
            input_["source_backup_id"] = source_backup_id
        if source_region is not None:
            input_["source_region"] = source_region
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def copy_snapshot_and_update_volume(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        volume_id: Optional["capo_fsx.types.volume_id.VolumeId"] = None,
        source_snapshot_arn: Optional["capo_fsx.types.resource_arn.ResourceARN"] = None,
        copy_strategy: Optional[
            "capo_fsx.types.open_zfs_copy_strategy.OpenZFSCopyStrategy"
        ] = None,
        options: Optional[
            "capo_fsx.types.update_open_zfs_volume_options.UpdateOpenZFSVolumeOptions"
        ] = None,
    ) -> "capo_fsx.types.copy_snapshot_and_update_volume_response.CopySnapshotAndUpdateVolumeResponse":
        """<p>Updates an existing volume by using a snapshot from another Amazon FSx for OpenZFS file system. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/on-demand-replication.html">on-demand data replication</a> in the Amazon FSx for OpenZFS User Guide.</p>

        Args:
            volume_id: <p>Specifies the ID of the volume that you are copying the snapshot to.</p>
            copy_strategy: <p>Specifies the strategy to use when copying data from a snapshot to the volume. </p> <ul> <li> <p> <code>FULL_COPY</code> - Copies all data from the snapshot to the volume. </p> </li> <li> <p> <code>INCREMENTAL_COPY</code> - Copies only the snapshot data that's changed since the previous replication.</p> </li> </ul> <note> <p> <code>CLONE</code> isn't a valid copy strategy option for the <code>CopySnapshotAndUpdateVolume</code> operation.</p> </note>
            options: <p>Confirms that you want to delete data on the destination volume that wasn’t there during the previous snapshot replication.</p> <p>Your replication will fail if you don’t include an option for a specific type of data and that data is on your destination. For example, if you don’t include <code>DELETE_INTERMEDIATE_SNAPSHOTS</code> and there are intermediate snapshots on the destination, you can’t copy the snapshot.</p> <ul> <li> <p> <code>DELETE_INTERMEDIATE_SNAPSHOTS</code> - Deletes snapshots on the destination volume that aren’t on the source volume.</p> </li> <li> <p> <code>DELETE_CLONED_VOLUMES</code> - Deletes snapshot clones on the destination volume that aren't on the source volume.</p> </li> <li> <p> <code>DELETE_INTERMEDIATE_DATA</code> - Overwrites snapshots on the destination volume that don’t match the source snapshot that you’re copying.</p> </li> </ul>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.copy_snapshot_and_update_volume_request.CopySnapshotAndUpdateVolumeRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.copy_snapshot_and_update_volume_response.CopySnapshotAndUpdateVolumeResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.copy_snapshot_and_update_volume

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.copy_snapshot_and_update_volume.copy_snapshot_and_update_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.copy_snapshot_and_update_volume_request.CopySnapshotAndUpdateVolumeRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_id is not None:
            input_["volume_id"] = volume_id
        if source_snapshot_arn is not None:
            input_["source_snapshot_arn"] = source_snapshot_arn
        if copy_strategy is not None:
            input_["copy_strategy"] = copy_strategy
        if options is not None:
            input_["options"] = options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_and_attach_s3_access_point(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        name: Optional[
            "capo_fsx.types.s3_access_point_attachment_name.S3AccessPointAttachmentName"
        ] = None,
        type: Optional[
            "capo_fsx.types.s3_access_point_attachment_type.S3AccessPointAttachmentType"
        ] = None,
        open_zfs_configuration: Optional[
            "capo_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration.CreateAndAttachS3AccessPointOpenZFSConfiguration"
        ] = None,
        ontap_configuration: Optional[
            "capo_fsx.types.create_and_attach_s3_access_point_ontap_configuration.CreateAndAttachS3AccessPointOntapConfiguration"
        ] = None,
        s3_access_point: Optional[
            "capo_fsx.types.create_and_attach_s3_access_point_s3_configuration.CreateAndAttachS3AccessPointS3Configuration"
        ] = None,
    ) -> "capo_fsx.types.create_and_attach_s3_access_point_response.CreateAndAttachS3AccessPointResponse":
        """<p>Creates an S3 access point and attaches it to an Amazon FSx volume. For FSx for OpenZFS file systems, the volume must be hosted on a high-availability file system, either Single-AZ or Multi-AZ. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/s3accesspoints-for-FSx.html">Accessing your data using Amazon S3 access points</a>. in the Amazon FSx for OpenZFS User Guide. </p> <p>The requester requires the following permissions to perform these actions:</p> <ul> <li> <p> <code>fsx:CreateAndAttachS3AccessPoint</code> </p> </li> <li> <p> <code>s3:CreateAccessPoint</code> </p> </li> <li> <p> <code>s3:GetAccessPoint</code> </p> </li> <li> <p> <code>s3:PutAccessPointPolicy</code> </p> </li> <li> <p> <code>s3:DeleteAccessPoint</code> </p> </li> </ul> <p>The following actions are related to <code>CreateAndAttachS3AccessPoint</code>:</p> <ul> <li> <p> <a>DescribeS3AccessPointAttachments</a> </p> </li> <li> <p> <a>DetachAndDeleteS3AccessPoint</a> </p> </li> </ul>

        Args:
            name: <p>The name you want to assign to this S3 access point.</p>
            type: <p>The type of S3 access point you want to create. Only <code>OpenZFS</code> is supported.</p>
            open_zfs_configuration: <p>Specifies the configuration to use when creating and attaching an S3 access point to an FSx for OpenZFS volume.</p>
            s3_access_point: <p>Specifies the virtual private cloud (VPC) configuration if you're creating an access point that is restricted to a VPC. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-vpc.html">Creating access points restricted to a virtual private cloud</a>.</p>

        Raises:
            capo_fsx.errors.access_point_already_owned_by_you.AccessPointAlreadyOwnedByYou: <p>An access point with that name already exists in the Amazon Web Services Region in your Amazon Web Services account.</p>
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.invalid_access_point.InvalidAccessPoint: <p>The access point specified doesn't exist.</p>
            capo_fsx.errors.invalid_request.InvalidRequest: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_fsx.errors.too_many_access_points.TooManyAccessPoints: <p>You have reached the maximum number of S3 access points attachments allowed for your account in this Amazon Web Services Region, or for the file system. For more information, or to request an increase, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/limits.html">Service quotas on FSx resources</a> in the FSx for OpenZFS User Guide.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.volume_not_found.VolumeNotFound: <p>No Amazon FSx volumes were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_and_attach_s3_access_point_request.CreateAndAttachS3AccessPointRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_and_attach_s3_access_point_response.CreateAndAttachS3AccessPointResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_and_attach_s3_access_point

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_and_attach_s3_access_point.create_and_attach_s3_access_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_and_attach_s3_access_point_request.CreateAndAttachS3AccessPointRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if name is not None:
            input_["name"] = name
        if type is not None:
            input_["type"] = type
        if open_zfs_configuration is not None:
            input_["open_zfs_configuration"] = open_zfs_configuration
        if ontap_configuration is not None:
            input_["ontap_configuration"] = ontap_configuration
        if s3_access_point is not None:
            input_["s3_access_point"] = s3_access_point

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backup(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
        volume_id: Optional["capo_fsx.types.volume_id.VolumeId"] = None,
    ) -> "capo_fsx.types.create_backup_response.CreateBackupResponse":
        """<p>Creates a backup of an existing Amazon FSx for Windows File Server file system, Amazon FSx for Lustre file system, Amazon FSx for NetApp ONTAP volume, or Amazon FSx for OpenZFS file system. We recommend creating regular backups so that you can restore a file system or volume from a backup if an issue arises with the original file system or volume.</p> <p>For Amazon FSx for Lustre file systems, you can create a backup only for file systems that have the following configuration:</p> <ul> <li> <p>A Persistent deployment type</p> </li> <li> <p>Are <i>not</i> linked to a data repository</p> </li> </ul> <p>For more information about backups, see the following:</p> <ul> <li> <p>For Amazon FSx for Lustre, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html">Working with FSx for Lustre backups</a>.</p> </li> <li> <p>For Amazon FSx for Windows, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html">Working with FSx for Windows backups</a>.</p> </li> <li> <p>For Amazon FSx for NetApp ONTAP, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-backups.html">Working with FSx for NetApp ONTAP backups</a>.</p> </li> <li> <p>For Amazon FSx for OpenZFS, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-backups.html">Working with FSx for OpenZFS backups</a>.</p> </li> </ul> <p>If a backup with the specified client request token exists and the parameters match, this operation returns the description of the existing backup. If a backup with the specified client request token exists and the parameters don't match, this operation returns <code>IncompatibleParameterError</code>. If a backup with the specified client request token doesn't exist, <code>CreateBackup</code> does the following: </p> <ul> <li> <p>Creates a new Amazon FSx backup with an assigned ID, and an initial lifecycle state of <code>CREATING</code>.</p> </li> <li> <p>Returns the description of the backup.</p> </li> </ul> <p>By using the idempotent operation, you can retry a <code>CreateBackup</code> operation without the risk of creating an extra backup. This approach can be useful when an initial call fails in a way that makes it unclear whether a backup was created. If you use the same client request token and the initial call created a backup, the operation returns a successful result because all the parameters are the same.</p> <p>The <code>CreateBackup</code> operation returns while the backup's lifecycle state is still <code>CREATING</code>. You can check the backup creation status by calling the <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeBackups.html">DescribeBackups</a> operation, which returns the backup state along with other information.</p>

        Args:
            file_system_id: <p>The ID of the file system to back up.</p>
            client_request_token: <p>(Optional) A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>
            tags: <p>(Optional) The tags to apply to the backup at backup creation. The key value of the <code>Name</code> tag appears in the console as the backup name. If you have set <code>CopyTagsToBackups</code> to <code>true</code>, and you specify one or more tags using the <code>CreateBackup</code> operation, no existing file system tags are copied from the file system to the backup.</p>
            volume_id: <p>(Optional) The ID of the FSx for ONTAP volume to back up.</p>

        Raises:
            capo_fsx.errors.backup_in_progress.BackupInProgress: <p>Another backup is already under way. Wait for completion before initiating additional backups of this file system.</p>
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.volume_not_found.VolumeNotFound: <p>No Amazon FSx volumes were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_backup_request.CreateBackupRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_backup_response.CreateBackupResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_backup

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_backup.create_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_backup_request.CreateBackupRequest = {}
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if volume_id is not None:
            input_["volume_id"] = volume_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_repository_association(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        file_system_path: Optional["capo_fsx.types.namespace.Namespace"] = None,
        data_repository_path: Optional[
            "capo_fsx.types.archive_path.ArchivePath"
        ] = None,
        batch_import_meta_data_on_create: Optional[
            "capo_fsx.types.batch_import_meta_data_on_create.BatchImportMetaDataOnCreate"
        ] = None,
        imported_file_chunk_size: Optional["capo_fsx.types.megabytes.Megabytes"] = None,
        s3: Optional[
            "capo_fsx.types.s3_data_repository_configuration.S3DataRepositoryConfiguration"
        ] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
    ) -> "capo_fsx.types.create_data_repository_association_response.CreateDataRepositoryAssociationResponse":
        """<p>Creates an Amazon FSx for Lustre data repository association (DRA). A data repository association is a link between a directory on the file system and an Amazon S3 bucket or prefix. You can have a maximum of 8 data repository associations on a file system. Data repository associations are supported on all FSx for Lustre 2.12 and 2.15 file systems, excluding <code>scratch_1</code> deployment type.</p> <p>Each data repository association must have a unique Amazon FSx file system directory and a unique S3 bucket or prefix associated with it. You can configure a data repository association for automatic import only, for automatic export only, or for both. To learn more about linking a data repository to your file system, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html">Linking your file system to an S3 bucket</a>.</p> <note> <p> <code>CreateDataRepositoryAssociation</code> isn't supported on Amazon File Cache resources. To create a DRA on Amazon File Cache, use the <code>CreateFileCache</code> operation.</p> </note>

        Args:
            file_system_path: <p>A path on the file system that points to a high-level directory (such as <code>/ns1/</code>) or subdirectory (such as <code>/ns1/subdir/</code>) that will be mapped 1-1 with <code>DataRepositoryPath</code>. The leading forward slash in the name is required. Two data repository associations cannot have overlapping file system paths. For example, if a data repository is associated with file system path <code>/ns1/</code>, then you cannot link another data repository with file system path <code>/ns1/ns2</code>.</p> <p>This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.</p> <note> <p>If you specify only a forward slash (<code>/</code>) as the file system path, you can link only one data repository to the file system. You can only specify "/" as the file system path for the first data repository associated with a file system.</p> </note>
            data_repository_path: <p>The path to the Amazon S3 data repository that will be linked to the file system. The path can be an S3 bucket or prefix in the format <code>s3://bucket-name/prefix/</code> (where <code>prefix</code> is optional). This path specifies where in the S3 data repository files will be imported from or exported to.</p>
            batch_import_meta_data_on_create: <p>Set to <code>true</code> to run an import data repository task to import metadata from the data repository to the file system after the data repository association is created. Default is <code>false</code>.</p>
            imported_file_chunk_size: <p>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.</p> <p>The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.</p>
            s3: <p>The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_data_repository_association_request.CreateDataRepositoryAssociationRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_data_repository_association_response.CreateDataRepositoryAssociationResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_data_repository_association

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_data_repository_association.create_data_repository_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_data_repository_association_request.CreateDataRepositoryAssociationRequest = {}
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if file_system_path is not None:
            input_["file_system_path"] = file_system_path
        if data_repository_path is not None:
            input_["data_repository_path"] = data_repository_path
        if batch_import_meta_data_on_create is not None:
            input_["batch_import_meta_data_on_create"] = (
                batch_import_meta_data_on_create
            )
        if imported_file_chunk_size is not None:
            input_["imported_file_chunk_size"] = imported_file_chunk_size
        if s3 is not None:
            input_["s3"] = s3
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_repository_task(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        type: Optional[
            "capo_fsx.types.data_repository_task_type.DataRepositoryTaskType"
        ] = None,
        paths: Optional[
            "capo_fsx.types.data_repository_task_paths.DataRepositoryTaskPaths"
        ] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        report: Optional["capo_fsx.types.completion_report.CompletionReport"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
        capacity_to_release: Optional[
            "capo_fsx.types.capacity_to_release.CapacityToRelease"
        ] = None,
        release_configuration: Optional[
            "capo_fsx.types.release_configuration.ReleaseConfiguration"
        ] = None,
    ) -> "capo_fsx.types.create_data_repository_task_response.CreateDataRepositoryTaskResponse":
        """<p>Creates an Amazon FSx for Lustre data repository task. A <code>CreateDataRepositoryTask</code> operation will fail if a data repository is not linked to the FSx file system.</p> <p>You use import and export data repository tasks to perform bulk operations between your FSx for Lustre file system and its linked data repositories. An example of a data repository task is exporting any data and metadata changes, including POSIX metadata, to files, directories, and symbolic links (symlinks) from your FSx file system to a linked data repository.</p> <p>You use release data repository tasks to release data from your file system for files that are exported to S3. The metadata of released files remains on the file system so users or applications can still access released files by reading the files again, which will restore data from Amazon S3 to the FSx for Lustre file system.</p> <p>To learn more about data repository tasks, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-repository-tasks.html">Data Repository Tasks</a>. To learn more about linking a data repository to your file system, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html">Linking your file system to an S3 bucket</a>.</p>

        Args:
            type: <p>Specifies the type of data repository task to create.</p> <ul> <li> <p> <code>EXPORT_TO_REPOSITORY</code> tasks export from your Amazon FSx for Lustre file system to a linked data repository.</p> </li> <li> <p> <code>IMPORT_METADATA_FROM_REPOSITORY</code> tasks import metadata changes from a linked S3 bucket to your Amazon FSx for Lustre file system.</p> </li> <li> <p> <code>RELEASE_DATA_FROM_FILESYSTEM</code> tasks release files in your Amazon FSx for Lustre file system that have been exported to a linked S3 bucket and that meet your specified release criteria.</p> </li> <li> <p> <code>AUTO_RELEASE_DATA</code> tasks automatically release files from an Amazon File Cache resource.</p> </li> </ul>
            paths: <p>A list of paths for the data repository task to use when the task is processed. If a path that you provide isn't valid, the task fails. If you don't provide paths, the default behavior is to export all files to S3 (for export tasks), import all files from S3 (for import tasks), or release all exported files that meet the last accessed time criteria (for release tasks).</p> <ul> <li> <p>For export tasks, the list contains paths on the FSx for Lustre file system from which the files are exported to the Amazon S3 bucket. The default path is the file system root directory. The paths you provide need to be relative to the mount point of the file system. If the mount point is <code>/mnt/fsx</code> and <code>/mnt/fsx/path1</code> is a directory or file on the file system you want to export, then the path to provide is <code>path1</code>.</p> </li> <li> <p>For import tasks, the list contains paths in the Amazon S3 bucket from which POSIX metadata changes are imported to the FSx for Lustre file system. The path can be an S3 bucket or prefix in the format <code>s3://bucket-name/prefix</code> (where <code>prefix</code> is optional).</p> </li> <li> <p>For release tasks, the list contains directory or file paths on the FSx for Lustre file system from which to release exported files. If a directory is specified, files within the directory are released. If a file path is specified, only that file is released. To release all exported files in the file system, specify a forward slash (/) as the path.</p> <note> <p>A file must also meet the last accessed time criteria specified in for the file to be released.</p> </note> </li> </ul>
            report: <p>Defines whether or not Amazon FSx provides a CompletionReport once the task has completed. A CompletionReport provides a detailed report on the files that Amazon FSx processed that meet the criteria specified by the <code>Scope</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/task-completion-report.html">Working with Task Completion Reports</a>.</p>
            capacity_to_release: <p>Specifies the amount of data to release, in GiB, by an Amazon File Cache <code>AUTO_RELEASE_DATA</code> task that automatically releases files from the cache.</p>
            release_configuration: <p>The configuration that specifies the last accessed time criteria for files that will be released from an Amazon FSx for Lustre file system.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.data_repository_task_executing.DataRepositoryTaskExecuting: <p>An existing data repository task is currently executing on the file system. Wait until the existing task has completed, then create the new task.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_data_repository_task_request.CreateDataRepositoryTaskRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_data_repository_task_response.CreateDataRepositoryTaskResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_data_repository_task

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_data_repository_task.create_data_repository_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_data_repository_task_request.CreateDataRepositoryTaskRequest = {}
        if type is not None:
            input_["type"] = type
        if paths is not None:
            input_["paths"] = paths
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if report is not None:
            input_["report"] = report
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if capacity_to_release is not None:
            input_["capacity_to_release"] = capacity_to_release
        if release_configuration is not None:
            input_["release_configuration"] = release_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_file_cache(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        file_cache_type: Optional[
            "capo_fsx.types.file_cache_type.FileCacheType"
        ] = None,
        file_cache_type_version: Optional[
            "capo_fsx.types.file_system_type_version.FileSystemTypeVersion"
        ] = None,
        storage_capacity: Optional[
            "capo_fsx.types.storage_capacity.StorageCapacity"
        ] = None,
        subnet_ids: Optional["capo_fsx.types.subnet_ids.SubnetIds"] = None,
        security_group_ids: Optional[
            "capo_fsx.types.security_group_ids.SecurityGroupIds"
        ] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
        copy_tags_to_data_repository_associations: Optional[
            "capo_fsx.types.copy_tags_to_data_repository_associations.CopyTagsToDataRepositoryAssociations"
        ] = None,
        kms_key_id: Optional["capo_fsx.types.kms_key_id.KmsKeyId"] = None,
        lustre_configuration: Optional[
            "capo_fsx.types.create_file_cache_lustre_configuration.CreateFileCacheLustreConfiguration"
        ] = None,
        data_repository_associations: Optional[
            "capo_fsx.types.create_file_cache_data_repository_associations.CreateFileCacheDataRepositoryAssociations"
        ] = None,
    ) -> "capo_fsx.types.create_file_cache_response.CreateFileCacheResponse":
        """<p>Creates a new Amazon File Cache resource.</p> <p>You can use this operation with a client request token in the request that Amazon File Cache uses to ensure idempotent creation. If a cache with the specified client request token exists and the parameters match, <code>CreateFileCache</code> returns the description of the existing cache. If a cache with the specified client request token exists and the parameters don't match, this call returns <code>IncompatibleParameterError</code>. If a file cache with the specified client request token doesn't exist, <code>CreateFileCache</code> does the following: </p> <ul> <li> <p>Creates a new, empty Amazon File Cache resource with an assigned ID, and an initial lifecycle state of <code>CREATING</code>.</p> </li> <li> <p>Returns the description of the cache in JSON format.</p> </li> </ul> <note> <p>The <code>CreateFileCache</code> call returns while the cache's lifecycle state is still <code>CREATING</code>. You can check the cache creation status by calling the <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileCaches.html">DescribeFileCaches</a> operation, which returns the cache state along with other information.</p> </note>

        Args:
            client_request_token: <p>An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p> <p>By using the idempotent operation, you can retry a <code>CreateFileCache</code> operation without the risk of creating an extra cache. This approach can be useful when an initial call fails in a way that makes it unclear whether a cache was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a cache, the client receives success as long as the parameters are the same.</p>
            file_cache_type: <p>The type of cache that you're creating, which must be <code>LUSTRE</code>.</p>
            file_cache_type_version: <p>Sets the Lustre version for the cache that you're creating, which must be <code>2.12</code>.</p>
            storage_capacity: <p>The storage capacity of the cache in gibibytes (GiB). Valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB.</p>
            security_group_ids: <p>A list of IDs specifying the security groups to apply to all network interfaces created for Amazon File Cache access. This list isn't returned in later requests to describe the cache.</p>
            copy_tags_to_data_repository_associations: <p>A boolean flag indicating whether tags for the cache should be copied to data repository associations. This value defaults to false.</p>
            kms_key_id: <p>Specifies the ID of the Key Management Service (KMS) key to use for encrypting data on an Amazon File Cache. If a <code>KmsKeyId</code> isn't specified, the Amazon FSx-managed KMS key for your account is used. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html">Encrypt</a> in the <i>Key Management Service API Reference</i>.</p>
            lustre_configuration: <p>The configuration for the Amazon File Cache resource being created.</p>
            data_repository_associations: <p>A list of up to 8 configurations for data repository associations (DRAs) to be created during the cache creation. The DRAs link the cache to either an Amazon S3 data repository or a Network File System (NFS) data repository that supports the NFSv3 protocol.</p> <p>The DRA configurations must meet the following requirements:</p> <ul> <li> <p>All configurations on the list must be of the same data repository type, either all S3 or all NFS. A cache can't link to different data repository types at the same time.</p> </li> <li> <p>An NFS DRA must link to an NFS file system that supports the NFSv3 protocol.</p> </li> </ul> <p>DRA automatic import and automatic export is not supported.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.invalid_network_settings.InvalidNetworkSettings: <p>One or more network settings specified in the request are invalid.</p>
            capo_fsx.errors.invalid_per_unit_storage_throughput.InvalidPerUnitStorageThroughput: <p>An invalid value for <code>PerUnitStorageThroughput</code> was provided. Please create your file system again, using a valid value.</p>
            capo_fsx.errors.missing_file_cache_configuration.MissingFileCacheConfiguration: <p>A cache configuration is required for this operation.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_file_cache_request.CreateFileCacheRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_file_cache_response.CreateFileCacheResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_file_cache

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_file_cache.create_file_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_file_cache_request.CreateFileCacheRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if file_cache_type is not None:
            input_["file_cache_type"] = file_cache_type
        if file_cache_type_version is not None:
            input_["file_cache_type_version"] = file_cache_type_version
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if copy_tags_to_data_repository_associations is not None:
            input_["copy_tags_to_data_repository_associations"] = (
                copy_tags_to_data_repository_associations
            )
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if lustre_configuration is not None:
            input_["lustre_configuration"] = lustre_configuration
        if data_repository_associations is not None:
            input_["data_repository_associations"] = data_repository_associations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_file_system(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        file_system_type: Optional[
            "capo_fsx.types.file_system_type.FileSystemType"
        ] = None,
        storage_capacity: Optional[
            "capo_fsx.types.storage_capacity.StorageCapacity"
        ] = None,
        storage_type: Optional["capo_fsx.types.storage_type.StorageType"] = None,
        subnet_ids: Optional["capo_fsx.types.subnet_ids.SubnetIds"] = None,
        security_group_ids: Optional[
            "capo_fsx.types.security_group_ids.SecurityGroupIds"
        ] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
        kms_key_id: Optional["capo_fsx.types.kms_key_id.KmsKeyId"] = None,
        windows_configuration: Optional[
            "capo_fsx.types.create_file_system_windows_configuration.CreateFileSystemWindowsConfiguration"
        ] = None,
        lustre_configuration: Optional[
            "capo_fsx.types.create_file_system_lustre_configuration.CreateFileSystemLustreConfiguration"
        ] = None,
        ontap_configuration: Optional[
            "capo_fsx.types.create_file_system_ontap_configuration.CreateFileSystemOntapConfiguration"
        ] = None,
        file_system_type_version: Optional[
            "capo_fsx.types.file_system_type_version.FileSystemTypeVersion"
        ] = None,
        open_zfs_configuration: Optional[
            "capo_fsx.types.create_file_system_open_zfs_configuration.CreateFileSystemOpenZFSConfiguration"
        ] = None,
        network_type: Optional["capo_fsx.types.network_type.NetworkType"] = None,
    ) -> "capo_fsx.types.create_file_system_response.CreateFileSystemResponse":
        """<p>Creates a new, empty Amazon FSx file system. You can create the following supported Amazon FSx file systems using the <code>CreateFileSystem</code> API operation:</p> <ul> <li> <p>Amazon FSx for Lustre</p> </li> <li> <p>Amazon FSx for NetApp ONTAP</p> </li> <li> <p>Amazon FSx for OpenZFS</p> </li> <li> <p>Amazon FSx for Windows File Server</p> </li> </ul> <p>This operation requires a client request token in the request that Amazon FSx uses to ensure idempotent creation. This means that calling the operation multiple times with the same client request token has no effect. By using the idempotent operation, you can retry a <code>CreateFileSystem</code> operation without the risk of creating an extra file system. This approach can be useful when an initial call fails in a way that makes it unclear whether a file system was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a file system, the client receives success as long as the parameters are the same.</p> <p>If a file system with the specified client request token exists and the parameters match, <code>CreateFileSystem</code> returns the description of the existing file system. If a file system with the specified client request token exists and the parameters don't match, this call returns <code>IncompatibleParameterError</code>. If a file system with the specified client request token doesn't exist, <code>CreateFileSystem</code> does the following:</p> <ul> <li> <p>Creates a new, empty Amazon FSx file system with an assigned ID, and an initial lifecycle state of <code>CREATING</code>.</p> </li> <li> <p>Returns the description of the file system in JSON format.</p> </li> </ul> <note> <p>The <code>CreateFileSystem</code> call returns while the file system's lifecycle state is still <code>CREATING</code>. You can check the file-system creation status by calling the <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html">DescribeFileSystems</a> operation, which returns the file system state along with other information.</p> </note>

        Args:
            client_request_token: <p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>
            file_system_type: <p>The type of Amazon FSx file system to create. Valid values are <code>WINDOWS</code>, <code>LUSTRE</code>, <code>ONTAP</code>, and <code>OPENZFS</code>.</p>
            storage_capacity: <p>Sets the storage capacity of the file system that you're creating, in gibibytes (GiB).</p> <p> <b>FSx for Lustre file systems</b> - The amount of storage capacity that you can configure depends on the value that you set for <code>StorageType</code> and the Lustre <code>DeploymentType</code>, as follows:</p> <ul> <li> <p>For <code>SCRATCH_2</code>, <code>PERSISTENT_2</code>, and <code>PERSISTENT_1</code> deployment types using SSD storage type, the valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB.</p> </li> <li> <p>For <code>PERSISTENT_1</code> HDD file systems, valid values are increments of 6000 GiB for 12 MB/s/TiB file systems and increments of 1800 GiB for 40 MB/s/TiB file systems.</p> </li> <li> <p>For <code>SCRATCH_1</code> deployment type, valid values are 1200 GiB, 2400 GiB, and increments of 3600 GiB.</p> </li> </ul> <p> <b>FSx for ONTAP file systems</b> - The amount of storage capacity that you can configure depends on the value of the <code>HAPairs</code> property. The minimum value is calculated as 1,024 * <code>HAPairs</code> and the maximum is calculated as 524,288 * <code>HAPairs</code>. </p> <p> <b>FSx for OpenZFS file systems</b> - The amount of storage capacity that you can configure is from 64 GiB up to 524,288 GiB (512 TiB).</p> <p> <b>FSx for Windows File Server file systems</b> - The amount of storage capacity that you can configure depends on the value that you set for <code>StorageType</code> as follows:</p> <ul> <li> <p>For SSD storage, valid values are 32 GiB-65,536 GiB (64 TiB).</p> </li> <li> <p>For HDD storage, valid values are 2000 GiB-65,536 GiB (64 TiB).</p> </li> </ul>
            storage_type: <p>Sets the storage class for the file system that you're creating. Valid values are <code>SSD</code>, <code>HDD</code>, and <code>INTELLIGENT_TIERING</code>.</p> <ul> <li> <p>Set to <code>SSD</code> to use solid state drive storage. SSD is supported on all Windows, Lustre, ONTAP, and OpenZFS deployment types.</p> </li> <li> <p>Set to <code>HDD</code> to use hard disk drive storage, which is supported on <code>SINGLE_AZ_2</code> and <code>MULTI_AZ_1</code> Windows file system deployment types, and on <code>PERSISTENT_1</code> Lustre file system deployment types.</p> </li> <li> <p>Set to <code>INTELLIGENT_TIERING</code> to use fully elastic, intelligently-tiered storage. Intelligent-Tiering is only available for OpenZFS file systems with the Multi-AZ deployment type and for Lustre file systems with the Persistent_2 deployment type.</p> </li> </ul> <p>Default value is <code>SSD</code>. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/optimize-fsx-costs.html#storage-type-options"> Storage type options</a> in the <i>FSx for Windows File Server User Guide</i>, <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html#lustre-storage-classes">FSx for Lustre storage classes</a> in the <i>FSx for Lustre User Guide</i>, and <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance-intelligent-tiering">Working with Intelligent-Tiering</a> in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>
            subnet_ids: <p>Specifies the IDs of the subnets that the file system will be accessible from. For Windows and ONTAP <code>MULTI_AZ_1</code> deployment types,provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the <code>WindowsConfiguration > PreferredSubnetID</code> or <code>OntapConfiguration > PreferredSubnetID</code> properties. For more information about Multi-AZ file system configuration, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html"> Availability and durability: Single-AZ and Multi-AZ file systems</a> in the <i>Amazon FSx for Windows User Guide</i> and <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html"> Availability and durability</a> in the <i>Amazon FSx for ONTAP User Guide</i>.</p> <p>For Windows <code>SINGLE_AZ_1</code> and <code>SINGLE_AZ_2</code> and all Lustre deployment types, provide exactly one subnet ID. The file server is launched in that subnet's Availability Zone.</p>
            security_group_ids: <p>A list of IDs specifying the security groups to apply to all network interfaces created for file system access. This list isn't returned in later requests to describe the file system.</p> <important> <p>You must specify a security group if you are creating a Multi-AZ FSx for ONTAP file system in a VPC subnet that has been shared with you.</p> </important>
            tags: <p>The tags to apply to the file system that's being created. The key value of the <code>Name</code> tag appears in the console as the file system name.</p>
            windows_configuration: <p>The Microsoft Windows configuration for the file system that's being created.</p>
            file_system_type_version: <p>For FSx for Lustre file systems, sets the Lustre version for the file system that you're creating. Valid values are <code>2.10</code>, <code>2.12</code>, and <code>2.15</code>:</p> <ul> <li> <p> <code>2.10</code> is supported by the Scratch and Persistent_1 Lustre deployment types.</p> </li> <li> <p> <code>2.12</code> is supported by all Lustre deployment types, except for <code>PERSISTENT_2</code> with a metadata configuration mode.</p> </li> <li> <p> <code>2.15</code> is supported by all Lustre deployment types and is recommended for all new file systems.</p> </li> </ul> <p>Default value is <code>2.10</code>, except for the following deployments:</p> <ul> <li> <p>Default value is <code>2.12</code> when <code>DeploymentType</code> is set to <code>PERSISTENT_2</code> without a metadata configuration mode.</p> </li> <li> <p>Default value is <code>2.15</code> when <code>DeploymentType</code> is set to <code>PERSISTENT_2</code> with a metadata configuration mode.</p> </li> </ul>
            open_zfs_configuration: <p>The OpenZFS configuration for the file system that's being created.</p>
            network_type: <p>The network type of the Amazon FSx file system that you are creating. Valid values are <code>IPV4</code> (which supports IPv4 only) and <code>DUAL</code> (for dual-stack mode, which supports both IPv4 and IPv6). The default is <code>IPV4</code>. Supported for FSx for OpenZFS, FSx for ONTAP, and FSx for Windows File Server file systems.</p>

        Raises:
            capo_fsx.errors.active_directory_error.ActiveDirectoryError: <p>An Active Directory error.</p>
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.invalid_export_path.InvalidExportPath: <p>The path provided for data repository export isn't valid.</p>
            capo_fsx.errors.invalid_import_path.InvalidImportPath: <p>The path provided for data repository import isn't valid.</p>
            capo_fsx.errors.invalid_network_settings.InvalidNetworkSettings: <p>One or more network settings specified in the request are invalid.</p>
            capo_fsx.errors.invalid_per_unit_storage_throughput.InvalidPerUnitStorageThroughput: <p>An invalid value for <code>PerUnitStorageThroughput</code> was provided. Please create your file system again, using a valid value.</p>
            capo_fsx.errors.missing_file_system_configuration.MissingFileSystemConfiguration: <p>A file system configuration is required for this operation.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_file_system_request.CreateFileSystemRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_file_system_response.CreateFileSystemResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_file_system

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_file_system.create_file_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_file_system_request.CreateFileSystemRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if file_system_type is not None:
            input_["file_system_type"] = file_system_type
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if windows_configuration is not None:
            input_["windows_configuration"] = windows_configuration
        if lustre_configuration is not None:
            input_["lustre_configuration"] = lustre_configuration
        if ontap_configuration is not None:
            input_["ontap_configuration"] = ontap_configuration
        if file_system_type_version is not None:
            input_["file_system_type_version"] = file_system_type_version
        if open_zfs_configuration is not None:
            input_["open_zfs_configuration"] = open_zfs_configuration
        if network_type is not None:
            input_["network_type"] = network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_file_system_from_backup(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        backup_id: Optional["capo_fsx.types.backup_id.BackupId"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        subnet_ids: Optional["capo_fsx.types.subnet_ids.SubnetIds"] = None,
        security_group_ids: Optional[
            "capo_fsx.types.security_group_ids.SecurityGroupIds"
        ] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
        windows_configuration: Optional[
            "capo_fsx.types.create_file_system_windows_configuration.CreateFileSystemWindowsConfiguration"
        ] = None,
        lustre_configuration: Optional[
            "capo_fsx.types.create_file_system_lustre_configuration.CreateFileSystemLustreConfiguration"
        ] = None,
        storage_type: Optional["capo_fsx.types.storage_type.StorageType"] = None,
        kms_key_id: Optional["capo_fsx.types.kms_key_id.KmsKeyId"] = None,
        file_system_type_version: Optional[
            "capo_fsx.types.file_system_type_version.FileSystemTypeVersion"
        ] = None,
        open_zfs_configuration: Optional[
            "capo_fsx.types.create_file_system_open_zfs_configuration.CreateFileSystemOpenZFSConfiguration"
        ] = None,
        storage_capacity: Optional[
            "capo_fsx.types.storage_capacity.StorageCapacity"
        ] = None,
        network_type: Optional["capo_fsx.types.network_type.NetworkType"] = None,
    ) -> "capo_fsx.types.create_file_system_from_backup_response.CreateFileSystemFromBackupResponse":
        """<p>Creates a new Amazon FSx for Lustre, Amazon FSx for Windows File Server, or Amazon FSx for OpenZFS file system from an existing Amazon FSx backup.</p> <p>If a file system with the specified client request token exists and the parameters match, this operation returns the description of the file system. If a file system with the specified client request token exists but the parameters don't match, this call returns <code>IncompatibleParameterError</code>. If a file system with the specified client request token doesn't exist, this operation does the following:</p> <ul> <li> <p>Creates a new Amazon FSx file system from backup with an assigned ID, and an initial lifecycle state of <code>CREATING</code>.</p> </li> <li> <p>Returns the description of the file system.</p> </li> </ul> <p>Parameters like the Active Directory, default share name, automatic backup, and backup settings default to the parameters of the file system that was backed up, unless overridden. You can explicitly supply other settings.</p> <p>By using the idempotent operation, you can retry a <code>CreateFileSystemFromBackup</code> call without the risk of creating an extra file system. This approach can be useful when an initial call fails in a way that makes it unclear whether a file system was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a file system, the client receives a success message as long as the parameters are the same.</p> <note> <p>The <code>CreateFileSystemFromBackup</code> call returns while the file system's lifecycle state is still <code>CREATING</code>. You can check the file-system creation status by calling the <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html"> DescribeFileSystems</a> operation, which returns the file system state along with other information.</p> </note>

        Args:
            client_request_token: <p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>
            subnet_ids: <p>Specifies the IDs of the subnets that the file system will be accessible from. For Windows <code>MULTI_AZ_1</code> file system deployment types, provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the <code>WindowsConfiguration > PreferredSubnetID</code> property.</p> <p>Windows <code>SINGLE_AZ_1</code> and <code>SINGLE_AZ_2</code> file system deployment types, Lustre file systems, and OpenZFS file systems provide exactly one subnet ID. The file server is launched in that subnet's Availability Zone.</p>
            security_group_ids: <p>A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups apply to all network interfaces. This value isn't returned in later <code>DescribeFileSystem</code> requests.</p>
            tags: <p>The tags to be applied to the file system at file system creation. The key value of the <code>Name</code> tag appears in the console as the file system name.</p>
            windows_configuration: <p>The configuration for this Microsoft Windows file system.</p>
            storage_type: <p>Sets the storage type for the Windows, OpenZFS, or Lustre file system that you're creating from a backup. Valid values are <code>SSD</code>, <code>HDD</code>, and <code>INTELLIGENT_TIERING</code>.</p> <ul> <li> <p>Set to <code>SSD</code> to use solid state drive storage. SSD is supported on all Windows and OpenZFS deployment types.</p> </li> <li> <p>Set to <code>HDD</code> to use hard disk drive storage. HDD is supported on <code>SINGLE_AZ_2</code> and <code>MULTI_AZ_1</code> FSx for Windows File Server file system deployment types.</p> </li> <li> <p>Set to <code>INTELLIGENT_TIERING</code> to use fully elastic, intelligently-tiered storage. Intelligent-Tiering is only available for OpenZFS file systems with the Multi-AZ deployment type and for Lustre file systems with the Persistent_2 deployment type.</p> </li> </ul> <p> The default value is <code>SSD</code>. </p> <note> <p>HDD and SSD storage types have different minimum storage capacity requirements. A restored file system's storage capacity is tied to the file system that was backed up. You can create a file system that uses HDD storage from a backup of a file system that used SSD storage if the original SSD file system had a storage capacity of at least 2000 GiB.</p> </note>
            file_system_type_version: <p>Sets the version for the Amazon FSx for Lustre file system that you're creating from a backup. Valid values are <code>2.10</code>, <code>2.12</code>, and <code>2.15</code>.</p> <p>You can enter a Lustre version that is newer than the backup's <code>FileSystemTypeVersion</code> setting. If you don't enter a newer Lustre version, it defaults to the backup's setting.</p>
            open_zfs_configuration: <p>The OpenZFS configuration for the file system that's being created. </p>
            storage_capacity: <p>Sets the storage capacity of the OpenZFS file system that you're creating from a backup, in gibibytes (GiB). Valid values are from 64 GiB up to 524,288 GiB (512 TiB). However, the value that you specify must be equal to or greater than the backup's storage capacity value. If you don't use the <code>StorageCapacity</code> parameter, the default is the backup's <code>StorageCapacity</code> value.</p> <p>If used to create a file system other than OpenZFS, you must provide a value that matches the backup's <code>StorageCapacity</code> value. If you provide any other value, Amazon FSx responds with an HTTP status code 400 Bad Request. </p>
            network_type: <p>Sets the network type for the Amazon FSx for OpenZFS file system that you're creating from a backup.</p>

        Raises:
            capo_fsx.errors.active_directory_error.ActiveDirectoryError: <p>An Active Directory error.</p>
            capo_fsx.errors.backup_not_found.BackupNotFound: <p>No Amazon FSx backups were found based upon the supplied parameters.</p>
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.invalid_network_settings.InvalidNetworkSettings: <p>One or more network settings specified in the request are invalid.</p>
            capo_fsx.errors.invalid_per_unit_storage_throughput.InvalidPerUnitStorageThroughput: <p>An invalid value for <code>PerUnitStorageThroughput</code> was provided. Please create your file system again, using a valid value.</p>
            capo_fsx.errors.missing_file_system_configuration.MissingFileSystemConfiguration: <p>A file system configuration is required for this operation.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_file_system_from_backup_request.CreateFileSystemFromBackupRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_file_system_from_backup_response.CreateFileSystemFromBackupResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_file_system_from_backup

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_file_system_from_backup.create_file_system_from_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_file_system_from_backup_request.CreateFileSystemFromBackupRequest = {}
        if backup_id is not None:
            input_["backup_id"] = backup_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if windows_configuration is not None:
            input_["windows_configuration"] = windows_configuration
        if lustre_configuration is not None:
            input_["lustre_configuration"] = lustre_configuration
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if file_system_type_version is not None:
            input_["file_system_type_version"] = file_system_type_version
        if open_zfs_configuration is not None:
            input_["open_zfs_configuration"] = open_zfs_configuration
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if network_type is not None:
            input_["network_type"] = network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_snapshot(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        name: Optional["capo_fsx.types.snapshot_name.SnapshotName"] = None,
        volume_id: Optional["capo_fsx.types.volume_id.VolumeId"] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
    ) -> "capo_fsx.types.create_snapshot_response.CreateSnapshotResponse":
        """<p>Creates a snapshot of an existing Amazon FSx for OpenZFS volume. With snapshots, you can easily undo file changes and compare file versions by restoring the volume to a previous version.</p> <p>If a snapshot with the specified client request token exists, and the parameters match, this operation returns the description of the existing snapshot. If a snapshot with the specified client request token exists, and the parameters don't match, this operation returns <code>IncompatibleParameterError</code>. If a snapshot with the specified client request token doesn't exist, <code>CreateSnapshot</code> does the following:</p> <ul> <li> <p>Creates a new OpenZFS snapshot with an assigned ID, and an initial lifecycle state of <code>CREATING</code>.</p> </li> <li> <p>Returns the description of the snapshot.</p> </li> </ul> <p>By using the idempotent operation, you can retry a <code>CreateSnapshot</code> operation without the risk of creating an extra snapshot. This approach can be useful when an initial call fails in a way that makes it unclear whether a snapshot was created. If you use the same client request token and the initial call created a snapshot, the operation returns a successful result because all the parameters are the same.</p> <p>The <code>CreateSnapshot</code> operation returns while the snapshot's lifecycle state is still <code>CREATING</code>. You can check the snapshot creation status by calling the <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeSnapshots.html">DescribeSnapshots</a> operation, which returns the snapshot state along with other information.</p>

        Args:
            name: <p>The name of the snapshot. </p>
            volume_id: <p>The ID of the volume that you are taking a snapshot of.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.volume_not_found.VolumeNotFound: <p>No Amazon FSx volumes were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_snapshot_request.CreateSnapshotRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_snapshot_response.CreateSnapshotResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_snapshot

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_snapshot.create_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_snapshot_request.CreateSnapshotRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if name is not None:
            input_["name"] = name
        if volume_id is not None:
            input_["volume_id"] = volume_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_storage_virtual_machine(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        active_directory_configuration: Optional[
            "capo_fsx.types.create_svm_active_directory_configuration.CreateSvmActiveDirectoryConfiguration"
        ] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        name: Optional[
            "capo_fsx.types.storage_virtual_machine_name.StorageVirtualMachineName"
        ] = None,
        svm_admin_password: Optional[
            "capo_fsx.types.admin_password.AdminPassword"
        ] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
        root_volume_security_style: Optional[
            "capo_fsx.types.storage_virtual_machine_root_volume_security_style.StorageVirtualMachineRootVolumeSecurityStyle"
        ] = None,
    ) -> "capo_fsx.types.create_storage_virtual_machine_response.CreateStorageVirtualMachineResponse":
        """<p>Creates a storage virtual machine (SVM) for an Amazon FSx for ONTAP file system.</p>

        Args:
            active_directory_configuration: <p>Describes the self-managed Microsoft Active Directory to which you want to join the SVM. Joining an Active Directory provides user authentication and access control for SMB clients, including Microsoft Windows and macOS clients accessing the file system.</p>
            name: <p>The name of the SVM.</p>
            svm_admin_password: <p>The password to use when managing the SVM using the NetApp ONTAP CLI or REST API. If you do not specify a password, you can still use the file system's <code>fsxadmin</code> user to manage the SVM.</p>
            root_volume_security_style: <p>The security style of the root volume of the SVM. Specify one of the following values:</p> <ul> <li> <p> <code>UNIX</code> if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account.</p> </li> <li> <p> <code>NTFS</code> if the file system is managed by a Microsoft Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Microsoft Windows user as the service account.</p> </li> <li> <p> <code>MIXED</code> This is an advanced setting. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-security-style.html">Volume security style</a> in the Amazon FSx for NetApp ONTAP User Guide.</p> </li> </ul> <p></p>

        Raises:
            capo_fsx.errors.active_directory_error.ActiveDirectoryError: <p>An Active Directory error.</p>
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_storage_virtual_machine_request.CreateStorageVirtualMachineRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_storage_virtual_machine_response.CreateStorageVirtualMachineResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_storage_virtual_machine

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_storage_virtual_machine.create_storage_virtual_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_storage_virtual_machine_request.CreateStorageVirtualMachineRequest = {}
        if active_directory_configuration is not None:
            input_["active_directory_configuration"] = active_directory_configuration
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if name is not None:
            input_["name"] = name
        if svm_admin_password is not None:
            input_["svm_admin_password"] = svm_admin_password
        if tags is not None:
            input_["tags"] = tags
        if root_volume_security_style is not None:
            input_["root_volume_security_style"] = root_volume_security_style

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_volume(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        volume_type: Optional["capo_fsx.types.volume_type.VolumeType"] = None,
        name: Optional["capo_fsx.types.volume_name.VolumeName"] = None,
        ontap_configuration: Optional[
            "capo_fsx.types.create_ontap_volume_configuration.CreateOntapVolumeConfiguration"
        ] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
        open_zfs_configuration: Optional[
            "capo_fsx.types.create_open_zfs_volume_configuration.CreateOpenZFSVolumeConfiguration"
        ] = None,
    ) -> "capo_fsx.types.create_volume_response.CreateVolumeResponse":
        """<p>Creates an FSx for ONTAP or Amazon FSx for OpenZFS storage volume.</p>

        Args:
            volume_type: <p>Specifies the type of volume to create; <code>ONTAP</code> and <code>OPENZFS</code> are the only valid volume types.</p>
            name: <p>Specifies the name of the volume that you're creating.</p>
            ontap_configuration: <p>Specifies the configuration to use when creating the ONTAP volume.</p>
            open_zfs_configuration: <p>Specifies the configuration to use when creating the OpenZFS volume.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.missing_volume_configuration.MissingVolumeConfiguration: <p>A volume configuration is required for this operation.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.storage_virtual_machine_not_found.StorageVirtualMachineNotFound: <p>No FSx for ONTAP SVMs were found based upon the supplied parameters.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_volume_request.CreateVolumeRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_volume_response.CreateVolumeResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_volume

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_volume.create_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_volume_request.CreateVolumeRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_type is not None:
            input_["volume_type"] = volume_type
        if name is not None:
            input_["name"] = name
        if ontap_configuration is not None:
            input_["ontap_configuration"] = ontap_configuration
        if tags is not None:
            input_["tags"] = tags
        if open_zfs_configuration is not None:
            input_["open_zfs_configuration"] = open_zfs_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_volume_from_backup(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        backup_id: Optional["capo_fsx.types.backup_id.BackupId"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        name: Optional["capo_fsx.types.volume_name.VolumeName"] = None,
        ontap_configuration: Optional[
            "capo_fsx.types.create_ontap_volume_configuration.CreateOntapVolumeConfiguration"
        ] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
    ) -> "capo_fsx.types.create_volume_from_backup_response.CreateVolumeFromBackupResponse":
        """<p>Creates a new Amazon FSx for NetApp ONTAP volume from an existing Amazon FSx volume backup.</p>

        Args:
            name: <p>The name of the new volume you're creating.</p>
            ontap_configuration: <p>Specifies the configuration of the ONTAP volume that you are creating.</p>

        Raises:
            capo_fsx.errors.backup_not_found.BackupNotFound: <p>No Amazon FSx backups were found based upon the supplied parameters.</p>
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.missing_volume_configuration.MissingVolumeConfiguration: <p>A volume configuration is required for this operation.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.storage_virtual_machine_not_found.StorageVirtualMachineNotFound: <p>No FSx for ONTAP SVMs were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.create_volume_from_backup_request.CreateVolumeFromBackupRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.create_volume_from_backup_response.CreateVolumeFromBackupResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.create_volume_from_backup

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.create_volume_from_backup.create_volume_from_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.create_volume_from_backup_request.CreateVolumeFromBackupRequest = {}
        if backup_id is not None:
            input_["backup_id"] = backup_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if name is not None:
            input_["name"] = name
        if ontap_configuration is not None:
            input_["ontap_configuration"] = ontap_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backup(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        backup_id: Optional["capo_fsx.types.backup_id.BackupId"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_fsx.types.delete_backup_response.DeleteBackupResponse":
        """<p>Deletes an Amazon FSx backup. After deletion, the backup no longer exists, and its data is gone.</p> <p>The <code>DeleteBackup</code> call returns instantly. The backup won't show up in later <code>DescribeBackups</code> calls.</p> <important> <p>The data in a deleted backup is also deleted and can't be recovered by any means.</p> </important>

        Args:
            backup_id: <p>The ID of the backup that you want to delete.</p>
            client_request_token: <p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent deletion. This parameter is automatically filled on your behalf when using the CLI or SDK.</p>

        Raises:
            capo_fsx.errors.backup_being_copied.BackupBeingCopied: <p>You can't delete a backup while it's being copied.</p>
            capo_fsx.errors.backup_in_progress.BackupInProgress: <p>Another backup is already under way. Wait for completion before initiating additional backups of this file system.</p>
            capo_fsx.errors.backup_not_found.BackupNotFound: <p>No Amazon FSx backups were found based upon the supplied parameters.</p>
            capo_fsx.errors.backup_restoring.BackupRestoring: <p>You can't delete a backup while it's being used to restore a file system.</p>
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a backup
            This operation deletes an Amazon FSx file system backup.

            >>> client.delete_backup(backup_id='backup-03e3c82e0183b7b6b')
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.delete_backup_request.DeleteBackupRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.delete_backup_response.DeleteBackupResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.delete_backup

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.delete_backup.delete_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.delete_backup_request.DeleteBackupRequest = {}
        if backup_id is not None:
            input_["backup_id"] = backup_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_repository_association(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        association_id: Optional[
            "capo_fsx.types.data_repository_association_id.DataRepositoryAssociationId"
        ] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        delete_data_in_file_system: Optional[
            "capo_fsx.types.delete_data_in_file_system.DeleteDataInFileSystem"
        ] = None,
    ) -> "capo_fsx.types.delete_data_repository_association_response.DeleteDataRepositoryAssociationResponse":
        """<p>Deletes a data repository association on an Amazon FSx for Lustre file system. Deleting the data repository association unlinks the file system from the Amazon S3 bucket. When deleting a data repository association, you have the option of deleting the data in the file system that corresponds to the data repository association. Data repository associations are supported on all FSx for Lustre 2.12 and 2.15 file systems, excluding <code>scratch_1</code> deployment type.</p>

        Args:
            association_id: <p>The ID of the data repository association that you want to delete.</p>
            delete_data_in_file_system: <p>Set to <code>true</code> to delete the data in the file system that corresponds to the data repository association.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.data_repository_association_not_found.DataRepositoryAssociationNotFound: <p>No data repository associations were found based upon the supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.delete_data_repository_association_request.DeleteDataRepositoryAssociationRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.delete_data_repository_association_response.DeleteDataRepositoryAssociationResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.delete_data_repository_association

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.delete_data_repository_association.delete_data_repository_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.delete_data_repository_association_request.DeleteDataRepositoryAssociationRequest = {}
        if association_id is not None:
            input_["association_id"] = association_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if delete_data_in_file_system is not None:
            input_["delete_data_in_file_system"] = delete_data_in_file_system

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_file_cache(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_cache_id: Optional["capo_fsx.types.file_cache_id.FileCacheId"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_fsx.types.delete_file_cache_response.DeleteFileCacheResponse":
        """<p>Deletes an Amazon File Cache resource. After deletion, the cache no longer exists, and its data is gone.</p> <p>The <code>DeleteFileCache</code> operation returns while the cache has the <code>DELETING</code> status. You can check the cache deletion status by calling the <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileCaches.html">DescribeFileCaches</a> operation, which returns a list of caches in your account. If you pass the cache ID for a deleted cache, the <code>DescribeFileCaches</code> operation returns a <code>FileCacheNotFound</code> error.</p> <important> <p>The data in a deleted cache is also deleted and can't be recovered by any means.</p> </important>

        Args:
            file_cache_id: <p>The ID of the cache that's being deleted.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_cache_not_found.FileCacheNotFound: <p>No caches were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.delete_file_cache_request.DeleteFileCacheRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.delete_file_cache_response.DeleteFileCacheResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.delete_file_cache

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.delete_file_cache.delete_file_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.delete_file_cache_request.DeleteFileCacheRequest = {}
        if file_cache_id is not None:
            input_["file_cache_id"] = file_cache_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_file_system(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        windows_configuration: Optional[
            "capo_fsx.types.delete_file_system_windows_configuration.DeleteFileSystemWindowsConfiguration"
        ] = None,
        lustre_configuration: Optional[
            "capo_fsx.types.delete_file_system_lustre_configuration.DeleteFileSystemLustreConfiguration"
        ] = None,
        open_zfs_configuration: Optional[
            "capo_fsx.types.delete_file_system_open_zfs_configuration.DeleteFileSystemOpenZFSConfiguration"
        ] = None,
    ) -> "capo_fsx.types.delete_file_system_response.DeleteFileSystemResponse":
        """<p>Deletes a file system. After deletion, the file system no longer exists, and its data is gone. Any existing automatic backups and snapshots are also deleted.</p> <p>To delete an Amazon FSx for NetApp ONTAP file system, first delete all the volumes and storage virtual machines (SVMs) on the file system. Then provide a <code>FileSystemId</code> value to the <code>DeleteFileSystem</code> operation.</p> <p>Before deleting an Amazon FSx for OpenZFS file system, make sure that there aren't any Amazon S3 access points attached to any volume. For more information on how to list S3 access points that are attached to volumes, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-list.html">Listing S3 access point attachments</a>. For more information on how to delete S3 access points, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/delete-access-point.html">Deleting an S3 access point attachment</a>.</p> <p>By default, when you delete an Amazon FSx for Windows File Server file system, a final backup is created upon deletion. This final backup isn't subject to the file system's retention policy, and must be manually deleted.</p> <p>To delete an Amazon FSx for Lustre file system, first <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/unmounting-fs.html">unmount</a> it from every connected Amazon EC2 instance, then provide a <code>FileSystemId</code> value to the <code>DeleteFileSystem</code> operation. By default, Amazon FSx will not take a final backup when the <code>DeleteFileSystem</code> operation is invoked. On file systems not linked to an Amazon S3 bucket, set <code>SkipFinalBackup</code> to <code>false</code> to take a final backup of the file system you are deleting. Backups cannot be enabled on S3-linked file systems. To ensure all of your data is written back to S3 before deleting your file system, you can either monitor for the <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-cloudwatch.html#auto-import-export-metrics">AgeOfOldestQueuedMessage</a> metric to be zero (if using automatic export) or you can run an <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/export-data-repo-task-dra.html">export data repository task</a>. If you have automatic export enabled and want to use an export data repository task, you have to disable automatic export before executing the export data repository task.</p> <p>The <code>DeleteFileSystem</code> operation returns while the file system has the <code>DELETING</code> status. You can check the file system deletion status by calling the <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html">DescribeFileSystems</a> operation, which returns a list of file systems in your account. If you pass the file system ID for a deleted file system, the <code>DescribeFileSystems</code> operation returns a <code>FileSystemNotFound</code> error.</p> <note> <p>If a data repository task is in a <code>PENDING</code> or <code>EXECUTING</code> state, deleting an Amazon FSx for Lustre file system will fail with an HTTP status code 400 (Bad Request).</p> </note> <important> <p>The data in a deleted file system is also deleted and can't be recovered by any means.</p> </important>

        Args:
            file_system_id: <p>The ID of the file system that you want to delete.</p>
            client_request_token: <p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent deletion. This token is automatically filled on your behalf when using the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>
            open_zfs_configuration: <p>The configuration object for the OpenZFS file system used in the <code>DeleteFileSystem</code> operation.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a file system
            This operation deletes an Amazon FSx file system.

            >>> client.delete_file_system(file_system_id='fs-0498eed5fe91001ec')
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.delete_file_system_request.DeleteFileSystemRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.delete_file_system_response.DeleteFileSystemResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.delete_file_system

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.delete_file_system.delete_file_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.delete_file_system_request.DeleteFileSystemRequest = {}
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if windows_configuration is not None:
            input_["windows_configuration"] = windows_configuration
        if lustre_configuration is not None:
            input_["lustre_configuration"] = lustre_configuration
        if open_zfs_configuration is not None:
            input_["open_zfs_configuration"] = open_zfs_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_snapshot(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        snapshot_id: Optional["capo_fsx.types.snapshot_id.SnapshotId"] = None,
    ) -> "capo_fsx.types.delete_snapshot_response.DeleteSnapshotResponse":
        """<p>Deletes an Amazon FSx for OpenZFS snapshot. After deletion, the snapshot no longer exists, and its data is gone. Deleting a snapshot doesn't affect snapshots stored in a file system backup. </p> <p>The <code>DeleteSnapshot</code> operation returns instantly. The snapshot appears with the lifecycle status of <code>DELETING</code> until the deletion is complete.</p>

        Args:
            snapshot_id: <p>The ID of the snapshot that you want to delete.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.snapshot_not_found.SnapshotNotFound: <p>No Amazon FSx snapshots were found based on the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.delete_snapshot_request.DeleteSnapshotRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.delete_snapshot_response.DeleteSnapshotResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.delete_snapshot

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.delete_snapshot.delete_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.delete_snapshot_request.DeleteSnapshotRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if snapshot_id is not None:
            input_["snapshot_id"] = snapshot_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_storage_virtual_machine(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        storage_virtual_machine_id: Optional[
            "capo_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
        ] = None,
    ) -> "capo_fsx.types.delete_storage_virtual_machine_response.DeleteStorageVirtualMachineResponse":
        """<p>Deletes an existing Amazon FSx for ONTAP storage virtual machine (SVM). Prior to deleting an SVM, you must delete all non-root volumes in the SVM, otherwise the operation will fail.</p>

        Args:
            storage_virtual_machine_id: <p>The ID of the SVM that you want to delete.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.storage_virtual_machine_not_found.StorageVirtualMachineNotFound: <p>No FSx for ONTAP SVMs were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.delete_storage_virtual_machine_request.DeleteStorageVirtualMachineRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.delete_storage_virtual_machine_response.DeleteStorageVirtualMachineResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.delete_storage_virtual_machine

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.delete_storage_virtual_machine.delete_storage_virtual_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.delete_storage_virtual_machine_request.DeleteStorageVirtualMachineRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if storage_virtual_machine_id is not None:
            input_["storage_virtual_machine_id"] = storage_virtual_machine_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_volume(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        volume_id: Optional["capo_fsx.types.volume_id.VolumeId"] = None,
        ontap_configuration: Optional[
            "capo_fsx.types.delete_volume_ontap_configuration.DeleteVolumeOntapConfiguration"
        ] = None,
        open_zfs_configuration: Optional[
            "capo_fsx.types.delete_volume_open_zfs_configuration.DeleteVolumeOpenZFSConfiguration"
        ] = None,
    ) -> "capo_fsx.types.delete_volume_response.DeleteVolumeResponse":
        """<p>Deletes an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volume.</p>

        Args:
            volume_id: <p>The ID of the volume that you are deleting.</p>
            ontap_configuration: <p>For Amazon FSx for ONTAP volumes, specify whether to take a final backup of the volume and apply tags to the backup. To apply tags to the backup, you must have the <code>fsx:TagResource</code> permission.</p>
            open_zfs_configuration: <p>For Amazon FSx for OpenZFS volumes, specify whether to delete all child volumes and snapshots.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.volume_not_found.VolumeNotFound: <p>No Amazon FSx volumes were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.delete_volume_request.DeleteVolumeRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.delete_volume_response.DeleteVolumeResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.delete_volume

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.delete_volume.delete_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.delete_volume_request.DeleteVolumeRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_id is not None:
            input_["volume_id"] = volume_id
        if ontap_configuration is not None:
            input_["ontap_configuration"] = ontap_configuration
        if open_zfs_configuration is not None:
            input_["open_zfs_configuration"] = open_zfs_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_backups(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        backup_ids: Optional["capo_fsx.types.backup_ids.BackupIds"] = None,
        filters: Optional["capo_fsx.types.filters.Filters"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.describe_backups_response.DescribeBackupsResponse":
        """<p>Returns the description of a specific Amazon FSx backup, if a <code>BackupIds</code> value is provided for that backup. Otherwise, it returns all backups owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you're calling.</p> <p>When retrieving all backups, you can optionally specify the <code>MaxResults</code> parameter to limit the number of backups in a response. If more backups remain, Amazon FSx returns a <code>NextToken</code> value in the response. In this case, send a later request with the <code>NextToken</code> request parameter set to the value of the <code>NextToken</code> value from the last response.</p> <p>This operation is used in an iterative process to retrieve a list of your backups. <code>DescribeBackups</code> is called first without a <code>NextToken</code> value. Then the operation continues to be called with the <code>NextToken</code> parameter set to the value of the last <code>NextToken</code> value until a response has no <code>NextToken</code> value.</p> <p>When using this operation, keep the following in mind:</p> <ul> <li> <p>The operation might return fewer than the <code>MaxResults</code> value of backup descriptions while still including a <code>NextToken</code> value.</p> </li> <li> <p>The order of the backups returned in the response of one <code>DescribeBackups</code> call and the order of the backups returned across the responses of a multi-call iteration is unspecified.</p> </li> </ul>

        Args:
            backup_ids: <p>The IDs of the backups that you want to retrieve. This parameter value overrides any filters. If any IDs aren't found, a <code>BackupNotFound</code> error occurs.</p>
            filters: <p>The filters structure. The supported names are <code>file-system-id</code>, <code>backup-type</code>, <code>file-system-type</code>, and <code>volume-id</code>.</p>
            max_results: <p>Maximum number of backups to return in the response. This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the <code>MaxResults</code> parameter specified in the request and the service's internal maximum number of items per page.</p>
            next_token: <p>An opaque pagination token returned from a previous <code>DescribeBackups</code> operation. If a token is present, the operation continues the list from where the returning call left off.</p>

        Raises:
            capo_fsx.errors.backup_not_found.BackupNotFound: <p>No Amazon FSx backups were found based upon the supplied parameters.</p>
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.volume_not_found.VolumeNotFound: <p>No Amazon FSx volumes were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_backups_request.DescribeBackupsRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_backups_response.DescribeBackupsResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_backups

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_backups.describe_backups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_backups_request.DescribeBackupsRequest = {}
        if backup_ids is not None:
            input_["backup_ids"] = backup_ids
        if filters is not None:
            input_["filters"] = filters
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

    def iter_describe_backups(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        backup_ids: Optional["capo_fsx.types.backup_ids.BackupIds"] = None,
        filters: Optional["capo_fsx.types.filters.Filters"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.describe_backups_response.DescribeBackupsResponse]":
        _token = next_token
        while True:
            _response = self.describe_backups(
                config_overrides=config_overrides,
                backup_ids=backup_ids,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_data_repository_associations(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        association_ids: Optional[
            "capo_fsx.types.data_repository_association_ids.DataRepositoryAssociationIds"
        ] = None,
        filters: Optional["capo_fsx.types.filters.Filters"] = None,
        max_results: Optional[
            "capo_fsx.types.limited_max_results.LimitedMaxResults"
        ] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.describe_data_repository_associations_response.DescribeDataRepositoryAssociationsResponse":
        """<p>Returns the description of specific Amazon FSx for Lustre or Amazon File Cache data repository associations, if one or more <code>AssociationIds</code> values are provided in the request, or if filters are used in the request. Data repository associations are supported on Amazon File Cache resources and all FSx for Lustre 2.12 and 2,15 file systems, excluding <code>scratch_1</code> deployment type.</p> <p>You can use filters to narrow the response to include just data repository associations for specific file systems (use the <code>file-system-id</code> filter with the ID of the file system) or caches (use the <code>file-cache-id</code> filter with the ID of the cache), or data repository associations for a specific repository type (use the <code>data-repository-type</code> filter with a value of <code>S3</code> or <code>NFS</code>). If you don't use filters, the response returns all data repository associations owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you're calling.</p> <p>When retrieving all data repository associations, you can paginate the response by using the optional <code>MaxResults</code> parameter to limit the number of data repository associations returned in a response. If more data repository associations remain, a <code>NextToken</code> value is returned in the response. In this case, send a later request with the <code>NextToken</code> request parameter set to the value of <code>NextToken</code> from the last response.</p>

        Args:
            association_ids: <p>IDs of the data repository associations whose descriptions you want to retrieve (String).</p>
            max_results: <p>The maximum number of resources to return in the response. This value must be an integer greater than zero.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.data_repository_association_not_found.DataRepositoryAssociationNotFound: <p>No data repository associations were found based upon the supplied parameters.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.invalid_data_repository_type.InvalidDataRepositoryType: <p>You have filtered the response to a data repository type that is not supported.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_data_repository_associations_request.DescribeDataRepositoryAssociationsRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_data_repository_associations_response.DescribeDataRepositoryAssociationsResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_data_repository_associations

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_data_repository_associations.describe_data_repository_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_data_repository_associations_request.DescribeDataRepositoryAssociationsRequest = {}
        if association_ids is not None:
            input_["association_ids"] = association_ids
        if filters is not None:
            input_["filters"] = filters
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

    def iter_describe_data_repository_associations(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        association_ids: Optional[
            "capo_fsx.types.data_repository_association_ids.DataRepositoryAssociationIds"
        ] = None,
        filters: Optional["capo_fsx.types.filters.Filters"] = None,
        max_results: Optional[
            "capo_fsx.types.limited_max_results.LimitedMaxResults"
        ] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.describe_data_repository_associations_response.DescribeDataRepositoryAssociationsResponse]":
        _token = next_token
        while True:
            _response = self.describe_data_repository_associations(
                config_overrides=config_overrides,
                association_ids=association_ids,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_data_repository_tasks(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        task_ids: Optional["capo_fsx.types.task_ids.TaskIds"] = None,
        filters: Optional[
            "capo_fsx.types.data_repository_task_filters.DataRepositoryTaskFilters"
        ] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.describe_data_repository_tasks_response.DescribeDataRepositoryTasksResponse":
        """<p>Returns the description of specific Amazon FSx for Lustre or Amazon File Cache data repository tasks, if one or more <code>TaskIds</code> values are provided in the request, or if filters are used in the request. You can use filters to narrow the response to include just tasks for specific file systems or caches, or tasks in a specific lifecycle state. Otherwise, it returns all data repository tasks owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you're calling.</p> <p>When retrieving all tasks, you can paginate the response by using the optional <code>MaxResults</code> parameter to limit the number of tasks returned in a response. If more tasks remain, a <code>NextToken</code> value is returned in the response. In this case, send a later request with the <code>NextToken</code> request parameter set to the value of <code>NextToken</code> from the last response.</p>

        Args:
            task_ids: <p>(Optional) IDs of the tasks whose descriptions you want to retrieve (String).</p>
            filters: <p>(Optional) You can use filters to narrow the <code>DescribeDataRepositoryTasks</code> response to include just tasks for specific file systems, or tasks in a specific lifecycle state.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.data_repository_task_not_found.DataRepositoryTaskNotFound: <p>The data repository task or tasks you specified could not be found.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_data_repository_tasks_request.DescribeDataRepositoryTasksRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_data_repository_tasks_response.DescribeDataRepositoryTasksResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_data_repository_tasks

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_data_repository_tasks.describe_data_repository_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_data_repository_tasks_request.DescribeDataRepositoryTasksRequest = {}
        if task_ids is not None:
            input_["task_ids"] = task_ids
        if filters is not None:
            input_["filters"] = filters
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

    def iter_describe_data_repository_tasks(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        task_ids: Optional["capo_fsx.types.task_ids.TaskIds"] = None,
        filters: Optional[
            "capo_fsx.types.data_repository_task_filters.DataRepositoryTaskFilters"
        ] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.describe_data_repository_tasks_response.DescribeDataRepositoryTasksResponse]":
        _token = next_token
        while True:
            _response = self.describe_data_repository_tasks(
                config_overrides=config_overrides,
                task_ids=task_ids,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_file_caches(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_cache_ids: Optional["capo_fsx.types.file_cache_ids.FileCacheIds"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.describe_file_caches_response.DescribeFileCachesResponse":
        """<p>Returns the description of a specific Amazon File Cache resource, if a <code>FileCacheIds</code> value is provided for that cache. Otherwise, it returns descriptions of all caches owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you're calling.</p> <p>When retrieving all cache descriptions, you can optionally specify the <code>MaxResults</code> parameter to limit the number of descriptions in a response. If more cache descriptions remain, the operation returns a <code>NextToken</code> value in the response. In this case, send a later request with the <code>NextToken</code> request parameter set to the value of <code>NextToken</code> from the last response.</p> <p>This operation is used in an iterative process to retrieve a list of your cache descriptions. <code>DescribeFileCaches</code> is called first without a <code>NextToken</code>value. Then the operation continues to be called with the <code>NextToken</code> parameter set to the value of the last <code>NextToken</code> value until a response has no <code>NextToken</code>.</p> <p>When using this operation, keep the following in mind:</p> <ul> <li> <p>The implementation might return fewer than <code>MaxResults</code> cache descriptions while still including a <code>NextToken</code> value.</p> </li> <li> <p>The order of caches returned in the response of one <code>DescribeFileCaches</code> call and the order of caches returned across the responses of a multicall iteration is unspecified.</p> </li> </ul>

        Args:
            file_cache_ids: <p>IDs of the caches whose descriptions you want to retrieve (String).</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_cache_not_found.FileCacheNotFound: <p>No caches were found based upon supplied parameters.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_file_caches_request.DescribeFileCachesRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_file_caches_response.DescribeFileCachesResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_file_caches

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_file_caches.describe_file_caches(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_file_caches_request.DescribeFileCachesRequest = {}
        if file_cache_ids is not None:
            input_["file_cache_ids"] = file_cache_ids
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

    def iter_describe_file_caches(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_cache_ids: Optional["capo_fsx.types.file_cache_ids.FileCacheIds"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.describe_file_caches_response.DescribeFileCachesResponse]":
        _token = next_token
        while True:
            _response = self.describe_file_caches(
                config_overrides=config_overrides,
                file_cache_ids=file_cache_ids,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_file_system_aliases(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.describe_file_system_aliases_response.DescribeFileSystemAliasesResponse":
        """<p>Returns the DNS aliases that are associated with the specified Amazon FSx for Windows File Server file system. A history of all DNS aliases that have been associated with and disassociated from the file system is available in the list of <a>AdministrativeAction</a> provided in the <a>DescribeFileSystems</a> operation response.</p>

        Args:
            file_system_id: <p>The ID of the file system to return the associated DNS aliases for (String).</p>
            max_results: <p>Maximum number of DNS aliases to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the <code>MaxResults</code> parameter specified in the request and the service's internal maximum number of items per page.</p>
            next_token: <p>Opaque pagination token returned from a previous <code>DescribeFileSystemAliases</code> operation (String). If a token is included in the request, the action continues the list from where the previous returning call left off.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_file_system_aliases_request.DescribeFileSystemAliasesRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_file_system_aliases_response.DescribeFileSystemAliasesResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_file_system_aliases

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_file_system_aliases.describe_file_system_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_file_system_aliases_request.DescribeFileSystemAliasesRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
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

    def iter_describe_file_system_aliases(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.describe_file_system_aliases_response.DescribeFileSystemAliasesResponse]":
        _token = next_token
        while True:
            _response = self.describe_file_system_aliases(
                config_overrides=config_overrides,
                client_request_token=client_request_token,
                file_system_id=file_system_id,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_file_systems(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_system_ids: Optional[
            "capo_fsx.types.file_system_ids.FileSystemIds"
        ] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.describe_file_systems_response.DescribeFileSystemsResponse":
        """<p>Returns the description of specific Amazon FSx file systems, if a <code>FileSystemIds</code> value is provided for that file system. Otherwise, it returns descriptions of all file systems owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you're calling.</p> <p>When retrieving all file system descriptions, you can optionally specify the <code>MaxResults</code> parameter to limit the number of descriptions in a response. If more file system descriptions remain, Amazon FSx returns a <code>NextToken</code> value in the response. In this case, send a later request with the <code>NextToken</code> request parameter set to the value of <code>NextToken</code> from the last response.</p> <p>This operation is used in an iterative process to retrieve a list of your file system descriptions. <code>DescribeFileSystems</code> is called first without a <code>NextToken</code>value. Then the operation continues to be called with the <code>NextToken</code> parameter set to the value of the last <code>NextToken</code> value until a response has no <code>NextToken</code>.</p> <p>When using this operation, keep the following in mind:</p> <ul> <li> <p>The implementation might return fewer than <code>MaxResults</code> file system descriptions while still including a <code>NextToken</code> value.</p> </li> <li> <p>The order of file systems returned in the response of one <code>DescribeFileSystems</code> call and the order of file systems returned across the responses of a multicall iteration is unspecified.</p> </li> </ul>

        Args:
            file_system_ids: <p>IDs of the file systems whose descriptions you want to retrieve (String).</p>
            max_results: <p>Maximum number of file systems to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the <code>MaxResults</code> parameter specified in the request and the service's internal maximum number of items per page.</p>
            next_token: <p>Opaque pagination token returned from a previous <code>DescribeFileSystems</code> operation (String). If a token present, the operation continues the list from where the returning call left off.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_file_systems_request.DescribeFileSystemsRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_file_systems_response.DescribeFileSystemsResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_file_systems

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_file_systems.describe_file_systems(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_file_systems_request.DescribeFileSystemsRequest = {}
        if file_system_ids is not None:
            input_["file_system_ids"] = file_system_ids
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

    def iter_describe_file_systems(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_system_ids: Optional[
            "capo_fsx.types.file_system_ids.FileSystemIds"
        ] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.describe_file_systems_response.DescribeFileSystemsResponse]":
        _token = next_token
        while True:
            _response = self.describe_file_systems(
                config_overrides=config_overrides,
                file_system_ids=file_system_ids,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_s3_access_point_attachments(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        names: Optional[
            "capo_fsx.types.s3_access_point_attachment_names.S3AccessPointAttachmentNames"
        ] = None,
        filters: Optional[
            "capo_fsx.types.s3_access_point_attachments_filters.S3AccessPointAttachmentsFilters"
        ] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.describe_s3_access_point_attachments_response.DescribeS3AccessPointAttachmentsResponse":
        """<p>Describes one or more S3 access points attached to Amazon FSx volumes.</p> <p>The requester requires the following permission to perform this action:</p> <ul> <li> <p> <code>fsx:DescribeS3AccessPointAttachments</code> </p> </li> </ul>

        Args:
            names: <p>The names of the S3 access point attachments whose descriptions you want to retrieve.</p>
            filters: <p>Enter a filter Name and Values pair to view a select set of S3 access point attachments.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.s3_access_point_attachment_not_found.S3AccessPointAttachmentNotFound: <p>The access point specified was not found.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_s3_access_point_attachments_request.DescribeS3AccessPointAttachmentsRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_s3_access_point_attachments_response.DescribeS3AccessPointAttachmentsResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_s3_access_point_attachments

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_s3_access_point_attachments.describe_s3_access_point_attachments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_s3_access_point_attachments_request.DescribeS3AccessPointAttachmentsRequest = {}
        if names is not None:
            input_["names"] = names
        if filters is not None:
            input_["filters"] = filters
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

    def iter_describe_s3_access_point_attachments(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        names: Optional[
            "capo_fsx.types.s3_access_point_attachment_names.S3AccessPointAttachmentNames"
        ] = None,
        filters: Optional[
            "capo_fsx.types.s3_access_point_attachments_filters.S3AccessPointAttachmentsFilters"
        ] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.s3_access_point_attachment.S3AccessPointAttachment]":
        _token = next_token
        while True:
            _response = self.describe_s3_access_point_attachments(
                config_overrides=config_overrides,
                names=names,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("s3_access_point_attachments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_shared_vpc_configuration(
        self, *, config_overrides: Optional[FSxClientConfig] = None
    ) -> "capo_fsx.types.describe_shared_vpc_configuration_response.DescribeSharedVpcConfigurationResponse":
        """<p>Indicates whether participant accounts in your organization can create Amazon FSx for NetApp ONTAP Multi-AZ file systems in subnets that are shared by a virtual private cloud (VPC) owner. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-file-systems.html#fsxn-vpc-shared-subnets">Creating FSx for ONTAP file systems in shared subnets</a>. </p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_shared_vpc_configuration_request.DescribeSharedVpcConfigurationRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_shared_vpc_configuration_response.DescribeSharedVpcConfigurationResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_shared_vpc_configuration

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_shared_vpc_configuration.describe_shared_vpc_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_shared_vpc_configuration_request.DescribeSharedVpcConfigurationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_snapshots(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        snapshot_ids: Optional["capo_fsx.types.snapshot_ids.SnapshotIds"] = None,
        filters: Optional["capo_fsx.types.snapshot_filters.SnapshotFilters"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
        include_shared: Optional["capo_fsx.types.include_shared.IncludeShared"] = None,
    ) -> "capo_fsx.types.describe_snapshots_response.DescribeSnapshotsResponse":
        """<p>Returns the description of specific Amazon FSx for OpenZFS snapshots, if a <code>SnapshotIds</code> value is provided. Otherwise, this operation returns all snapshots owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you're calling.</p> <p>When retrieving all snapshots, you can optionally specify the <code>MaxResults</code> parameter to limit the number of snapshots in a response. If more backups remain, Amazon FSx returns a <code>NextToken</code> value in the response. In this case, send a later request with the <code>NextToken</code> request parameter set to the value of <code>NextToken</code> from the last response. </p> <p>Use this operation in an iterative process to retrieve a list of your snapshots. <code>DescribeSnapshots</code> is called first without a <code>NextToken</code> value. Then the operation continues to be called with the <code>NextToken</code> parameter set to the value of the last <code>NextToken</code> value until a response has no <code>NextToken</code> value.</p> <p>When using this operation, keep the following in mind:</p> <ul> <li> <p>The operation might return fewer than the <code>MaxResults</code> value of snapshot descriptions while still including a <code>NextToken</code> value.</p> </li> <li> <p>The order of snapshots returned in the response of one <code>DescribeSnapshots</code> call and the order of backups returned across the responses of a multi-call iteration is unspecified. </p> </li> </ul>

        Args:
            snapshot_ids: <p>The IDs of the snapshots that you want to retrieve. This parameter value overrides any filters. If any IDs aren't found, a <code>SnapshotNotFound</code> error occurs.</p>
            filters: <p>The filters structure. The supported names are <code>file-system-id</code> or <code>volume-id</code>.</p>
            include_shared: <p>Set to <code>false</code> (default) if you want to only see the snapshots owned by your Amazon Web Services account. Set to <code>true</code> if you want to see the snapshots in your account and the ones shared with you from another account.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.snapshot_not_found.SnapshotNotFound: <p>No Amazon FSx snapshots were found based on the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_snapshots_request.DescribeSnapshotsRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_snapshots_response.DescribeSnapshotsResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_snapshots

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_snapshots.describe_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_snapshots_request.DescribeSnapshotsRequest = {}
        if snapshot_ids is not None:
            input_["snapshot_ids"] = snapshot_ids
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_shared is not None:
            input_["include_shared"] = include_shared

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_snapshots(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        snapshot_ids: Optional["capo_fsx.types.snapshot_ids.SnapshotIds"] = None,
        filters: Optional["capo_fsx.types.snapshot_filters.SnapshotFilters"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
        include_shared: Optional["capo_fsx.types.include_shared.IncludeShared"] = None,
    ) -> "Iterator[capo_fsx.types.snapshot.Snapshot]":
        _token = next_token
        while True:
            _response = self.describe_snapshots(
                config_overrides=config_overrides,
                snapshot_ids=snapshot_ids,
                filters=filters,
                max_results=max_results,
                next_token=_token,
                include_shared=include_shared,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_storage_virtual_machines(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        storage_virtual_machine_ids: Optional[
            "capo_fsx.types.storage_virtual_machine_ids.StorageVirtualMachineIds"
        ] = None,
        filters: Optional[
            "capo_fsx.types.storage_virtual_machine_filters.StorageVirtualMachineFilters"
        ] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.describe_storage_virtual_machines_response.DescribeStorageVirtualMachinesResponse":
        """<p>Describes one or more Amazon FSx for NetApp ONTAP storage virtual machines (SVMs).</p>

        Args:
            storage_virtual_machine_ids: <p>Enter the ID of one or more SVMs that you want to view.</p>
            filters: <p>Enter a filter name:value pair to view a select set of SVMs.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.storage_virtual_machine_not_found.StorageVirtualMachineNotFound: <p>No FSx for ONTAP SVMs were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_storage_virtual_machines_request.DescribeStorageVirtualMachinesRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_storage_virtual_machines_response.DescribeStorageVirtualMachinesResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_storage_virtual_machines

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_storage_virtual_machines.describe_storage_virtual_machines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_storage_virtual_machines_request.DescribeStorageVirtualMachinesRequest = {}
        if storage_virtual_machine_ids is not None:
            input_["storage_virtual_machine_ids"] = storage_virtual_machine_ids
        if filters is not None:
            input_["filters"] = filters
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

    def iter_describe_storage_virtual_machines(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        storage_virtual_machine_ids: Optional[
            "capo_fsx.types.storage_virtual_machine_ids.StorageVirtualMachineIds"
        ] = None,
        filters: Optional[
            "capo_fsx.types.storage_virtual_machine_filters.StorageVirtualMachineFilters"
        ] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.storage_virtual_machine.StorageVirtualMachine]":
        _token = next_token
        while True:
            _response = self.describe_storage_virtual_machines(
                config_overrides=config_overrides,
                storage_virtual_machine_ids=storage_virtual_machine_ids,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("storage_virtual_machines",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_volumes(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        volume_ids: Optional["capo_fsx.types.volume_ids.VolumeIds"] = None,
        filters: Optional["capo_fsx.types.volume_filters.VolumeFilters"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.describe_volumes_response.DescribeVolumesResponse":
        """<p>Describes one or more Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volumes.</p>

        Args:
            volume_ids: <p>The IDs of the volumes whose descriptions you want to retrieve.</p>
            filters: <p>Enter a filter <code>Name</code> and <code>Values</code> pair to view a select set of volumes.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.volume_not_found.VolumeNotFound: <p>No Amazon FSx volumes were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.describe_volumes_request.DescribeVolumesRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.describe_volumes_response.DescribeVolumesResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.describe_volumes

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.describe_volumes.describe_volumes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.describe_volumes_request.DescribeVolumesRequest = {}
        if volume_ids is not None:
            input_["volume_ids"] = volume_ids
        if filters is not None:
            input_["filters"] = filters
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

    def iter_describe_volumes(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        volume_ids: Optional["capo_fsx.types.volume_ids.VolumeIds"] = None,
        filters: Optional["capo_fsx.types.volume_filters.VolumeFilters"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.volume.Volume]":
        _token = next_token
        while True:
            _response = self.describe_volumes(
                config_overrides=config_overrides,
                volume_ids=volume_ids,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("volumes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def detach_and_delete_s3_access_point(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        name: Optional[
            "capo_fsx.types.s3_access_point_attachment_name.S3AccessPointAttachmentName"
        ] = None,
    ) -> "capo_fsx.types.detach_and_delete_s3_access_point_response.DetachAndDeleteS3AccessPointResponse":
        """<p>Detaches an S3 access point from an Amazon FSx volume and deletes the S3 access point.</p> <p>The requester requires the following permission to perform this action:</p> <ul> <li> <p> <code>fsx:DetachAndDeleteS3AccessPoint</code> </p> </li> <li> <p> <code>s3:DeleteAccessPoint</code> </p> </li> </ul>

        Args:
            name: <p>The name of the S3 access point attachment that you want to delete.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.s3_access_point_attachment_not_found.S3AccessPointAttachmentNotFound: <p>The access point specified was not found.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.detach_and_delete_s3_access_point_request.DetachAndDeleteS3AccessPointRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.detach_and_delete_s3_access_point_response.DetachAndDeleteS3AccessPointResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.detach_and_delete_s3_access_point

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.detach_and_delete_s3_access_point.detach_and_delete_s3_access_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.detach_and_delete_s3_access_point_request.DetachAndDeleteS3AccessPointRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_file_system_aliases(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        aliases: Optional[
            "capo_fsx.types.alternate_dns_names.AlternateDNSNames"
        ] = None,
    ) -> "capo_fsx.types.disassociate_file_system_aliases_response.DisassociateFileSystemAliasesResponse":
        """<p>Use this action to disassociate, or remove, one or more Domain Name Service (DNS) aliases from an Amazon FSx for Windows File Server file system. If you attempt to disassociate a DNS alias that is not associated with the file system, Amazon FSx responds with an HTTP status code 400 (Bad Request). For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html">Working with DNS Aliases</a>.</p> <p>The system generated response showing the DNS aliases that Amazon FSx is attempting to disassociate from the file system. Use the API operation to monitor the status of the aliases Amazon FSx is disassociating with the file system.</p>

        Args:
            file_system_id: <p>Specifies the file system from which to disassociate the DNS aliases.</p>
            aliases: <p>An array of one or more DNS alias names to disassociate, or remove, from the file system.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.disassociate_file_system_aliases_request.DisassociateFileSystemAliasesRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.disassociate_file_system_aliases_response.DisassociateFileSystemAliasesResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.disassociate_file_system_aliases

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.disassociate_file_system_aliases.disassociate_file_system_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.disassociate_file_system_aliases_request.DisassociateFileSystemAliasesRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if aliases is not None:
            input_["aliases"] = aliases

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        resource_arn: Optional["capo_fsx.types.resource_arn.ResourceARN"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "capo_fsx.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for Amazon FSx resources.</p> <p>When retrieving all tags, you can optionally specify the <code>MaxResults</code> parameter to limit the number of tags in a response. If more tags remain, Amazon FSx returns a <code>NextToken</code> value in the response. In this case, send a later request with the <code>NextToken</code> request parameter set to the value of <code>NextToken</code> from the last response.</p> <p>This action is used in an iterative process to retrieve a list of your tags. <code>ListTagsForResource</code> is called first without a <code>NextToken</code>value. Then the action continues to be called with the <code>NextToken</code> parameter set to the value of the last <code>NextToken</code> value until a response has no <code>NextToken</code>.</p> <p>When using this action, keep the following in mind:</p> <ul> <li> <p>The implementation might return fewer than <code>MaxResults</code> file system descriptions while still including a <code>NextToken</code> value.</p> </li> <li> <p>The order of tags returned in the response of one <code>ListTagsForResource</code> call and the order of tags returned across the responses of a multi-call iteration is unspecified.</p> </li> </ul>

        Args:
            resource_arn: <p>The ARN of the Amazon FSx resource that will have its tags listed.</p>
            max_results: <p>Maximum number of tags to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the <code>MaxResults</code> parameter specified in the request and the service's internal maximum number of items per page.</p>
            next_token: <p>Opaque pagination token returned from a previous <code>ListTagsForResource</code> operation (String). If a token present, the action continues the list from where the returning call left off.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.not_service_resource_error.NotServiceResourceError: <p>The resource specified for the tagging operation is not a resource type owned by Amazon FSx. Use the API of the relevant service to perform the operation. </p>
            capo_fsx.errors.resource_does_not_support_tagging.ResourceDoesNotSupportTagging: <p>The resource specified does not support tagging. </p>
            capo_fsx.errors.resource_not_found.ResourceNotFound: <p>The resource specified by the Amazon Resource Name (ARN) can't be found.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list tags for a resource
            This operation lists tags for an Amazon FSx resource.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:fsx:us-east-1:012345678912:file-system/fs-0498eed5fe91001ec')
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.list_tags_for_resource

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
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
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        resource_arn: Optional["capo_fsx.types.resource_arn.ResourceARN"] = None,
        max_results: Optional["capo_fsx.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_fsx.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_fsx.types.list_tags_for_resource_response.ListTagsForResourceResponse]":
        _token = next_token
        while True:
            _response = self.list_tags_for_resource(
                config_overrides=config_overrides,
                resource_arn=resource_arn,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def release_file_system_nfs_v3_locks(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_fsx.types.release_file_system_nfs_v3_locks_response.ReleaseFileSystemNfsV3LocksResponse":
        """<p>Releases the file system lock from an Amazon FSx for OpenZFS file system.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.release_file_system_nfs_v3_locks_request.ReleaseFileSystemNfsV3LocksRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.release_file_system_nfs_v3_locks_response.ReleaseFileSystemNfsV3LocksResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.release_file_system_nfs_v3_locks

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.release_file_system_nfs_v3_locks.release_file_system_nfs_v3_locks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.release_file_system_nfs_v3_locks_request.ReleaseFileSystemNfsV3LocksRequest = {}
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_volume_from_snapshot(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        volume_id: Optional["capo_fsx.types.volume_id.VolumeId"] = None,
        snapshot_id: Optional["capo_fsx.types.snapshot_id.SnapshotId"] = None,
        options: Optional[
            "capo_fsx.types.restore_open_zfs_volume_options.RestoreOpenZFSVolumeOptions"
        ] = None,
    ) -> "capo_fsx.types.restore_volume_from_snapshot_response.RestoreVolumeFromSnapshotResponse":
        """<p>Returns an Amazon FSx for OpenZFS volume to the state saved by the specified snapshot.</p>

        Args:
            volume_id: <p>The ID of the volume that you are restoring.</p>
            snapshot_id: <p>The ID of the source snapshot. Specifies the snapshot that you are restoring from.</p>
            options: <p>The settings used when restoring the specified volume from snapshot.</p> <ul> <li> <p> <code>DELETE_INTERMEDIATE_SNAPSHOTS</code> - Deletes snapshots between the current state and the specified snapshot. If there are intermediate snapshots and this option isn't used, <code>RestoreVolumeFromSnapshot</code> fails.</p> </li> <li> <p> <code>DELETE_CLONED_VOLUMES</code> - Deletes any dependent clone volumes created from intermediate snapshots. If there are any dependent clone volumes and this option isn't used, <code>RestoreVolumeFromSnapshot</code> fails.</p> </li> </ul>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.volume_not_found.VolumeNotFound: <p>No Amazon FSx volumes were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.restore_volume_from_snapshot_request.RestoreVolumeFromSnapshotRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.restore_volume_from_snapshot_response.RestoreVolumeFromSnapshotResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.restore_volume_from_snapshot

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.restore_volume_from_snapshot.restore_volume_from_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.restore_volume_from_snapshot_request.RestoreVolumeFromSnapshotRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_id is not None:
            input_["volume_id"] = volume_id
        if snapshot_id is not None:
            input_["snapshot_id"] = snapshot_id
        if options is not None:
            input_["options"] = options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_misconfigured_state_recovery(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
    ) -> "capo_fsx.types.start_misconfigured_state_recovery_response.StartMisconfiguredStateRecoveryResponse":
        """<p>After performing steps to repair the Active Directory configuration of an FSx for Windows File Server file system, use this action to initiate the process of Amazon FSx attempting to reconnect to the file system.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.start_misconfigured_state_recovery_request.StartMisconfiguredStateRecoveryRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.start_misconfigured_state_recovery_response.StartMisconfiguredStateRecoveryResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.start_misconfigured_state_recovery

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.start_misconfigured_state_recovery.start_misconfigured_state_recovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.start_misconfigured_state_recovery_request.StartMisconfiguredStateRecoveryRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        resource_arn: Optional["capo_fsx.types.resource_arn.ResourceARN"] = None,
        tags: Optional["capo_fsx.types.tags.Tags"] = None,
    ) -> "capo_fsx.types.tag_resource_response.TagResourceResponse":
        """<p>Tags an Amazon FSx resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon FSx resource that you want to tag.</p>
            tags: <p>A list of tags for the resource. If a tag with a given key already exists, the value is replaced by the one specified in this parameter.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.not_service_resource_error.NotServiceResourceError: <p>The resource specified for the tagging operation is not a resource type owned by Amazon FSx. Use the API of the relevant service to perform the operation. </p>
            capo_fsx.errors.resource_does_not_support_tagging.ResourceDoesNotSupportTagging: <p>The resource specified does not support tagging. </p>
            capo_fsx.errors.resource_not_found.ResourceNotFound: <p>The resource specified by the Amazon Resource Name (ARN) can't be found.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To tag a resource
            This operation tags an Amazon FSx resource.

            >>> client.tag_resource(resource_arn='arn:aws:fsx:us-east-1:012345678912:file-system/fs-0498eed5fe91001ec', tags=[{'Key': 'Name', 'Value': 'MyFileSystem'}])
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.tag_resource

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.tag_resource_request.TagResourceRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        resource_arn: Optional["capo_fsx.types.resource_arn.ResourceARN"] = None,
        tag_keys: Optional["capo_fsx.types.tag_keys.TagKeys"] = None,
    ) -> "capo_fsx.types.untag_resource_response.UntagResourceResponse":
        """<p>This action removes a tag from an Amazon FSx resource.</p>

        Args:
            resource_arn: <p>The ARN of the Amazon FSx resource to untag.</p>
            tag_keys: <p>A list of keys of tags on the resource to untag. In case the tag key doesn't exist, the call will still succeed to be idempotent.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.not_service_resource_error.NotServiceResourceError: <p>The resource specified for the tagging operation is not a resource type owned by Amazon FSx. Use the API of the relevant service to perform the operation. </p>
            capo_fsx.errors.resource_does_not_support_tagging.ResourceDoesNotSupportTagging: <p>The resource specified does not support tagging. </p>
            capo_fsx.errors.resource_not_found.ResourceNotFound: <p>The resource specified by the Amazon Resource Name (ARN) can't be found.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To untag a resource
            This operation untags an Amazon FSx resource.

            >>> client.untag_resource(resource_arn='arn:aws:fsx:us-east-1:012345678912:file-system/fs-0498eed5fe91001ec', tag_keys=['Name'])
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.untag_resource

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.untag_resource_request.UntagResourceRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_repository_association(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        association_id: Optional[
            "capo_fsx.types.data_repository_association_id.DataRepositoryAssociationId"
        ] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        imported_file_chunk_size: Optional["capo_fsx.types.megabytes.Megabytes"] = None,
        s3: Optional[
            "capo_fsx.types.s3_data_repository_configuration.S3DataRepositoryConfiguration"
        ] = None,
    ) -> "capo_fsx.types.update_data_repository_association_response.UpdateDataRepositoryAssociationResponse":
        """<p>Updates the configuration of an existing data repository association on an Amazon FSx for Lustre file system. Data repository associations are supported on all FSx for Lustre 2.12 and 2.15 file systems, excluding <code>scratch_1</code> deployment type.</p>

        Args:
            association_id: <p>The ID of the data repository association that you are updating.</p>
            imported_file_chunk_size: <p>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.</p> <p>The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.</p>
            s3: <p>The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.data_repository_association_not_found.DataRepositoryAssociationNotFound: <p>No data repository associations were found based upon the supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.update_data_repository_association_request.UpdateDataRepositoryAssociationRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.update_data_repository_association_response.UpdateDataRepositoryAssociationResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.update_data_repository_association

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.update_data_repository_association.update_data_repository_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.update_data_repository_association_request.UpdateDataRepositoryAssociationRequest = {}
        if association_id is not None:
            input_["association_id"] = association_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if imported_file_chunk_size is not None:
            input_["imported_file_chunk_size"] = imported_file_chunk_size
        if s3 is not None:
            input_["s3"] = s3

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_file_cache(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_cache_id: Optional["capo_fsx.types.file_cache_id.FileCacheId"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        lustre_configuration: Optional[
            "capo_fsx.types.update_file_cache_lustre_configuration.UpdateFileCacheLustreConfiguration"
        ] = None,
    ) -> "capo_fsx.types.update_file_cache_response.UpdateFileCacheResponse":
        """<p>Updates the configuration of an existing Amazon File Cache resource. You can update multiple properties in a single request.</p>

        Args:
            file_cache_id: <p>The ID of the cache that you are updating.</p>
            lustre_configuration: <p>The configuration updates for an Amazon File Cache resource.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_cache_not_found.FileCacheNotFound: <p>No caches were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.missing_file_cache_configuration.MissingFileCacheConfiguration: <p>A cache configuration is required for this operation.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.update_file_cache_request.UpdateFileCacheRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.update_file_cache_response.UpdateFileCacheResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.update_file_cache

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.update_file_cache.update_file_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.update_file_cache_request.UpdateFileCacheRequest = {}
        if file_cache_id is not None:
            input_["file_cache_id"] = file_cache_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if lustre_configuration is not None:
            input_["lustre_configuration"] = lustre_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_file_system(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        file_system_id: Optional["capo_fsx.types.file_system_id.FileSystemId"] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        storage_capacity: Optional[
            "capo_fsx.types.storage_capacity.StorageCapacity"
        ] = None,
        windows_configuration: Optional[
            "capo_fsx.types.update_file_system_windows_configuration.UpdateFileSystemWindowsConfiguration"
        ] = None,
        lustre_configuration: Optional[
            "capo_fsx.types.update_file_system_lustre_configuration.UpdateFileSystemLustreConfiguration"
        ] = None,
        ontap_configuration: Optional[
            "capo_fsx.types.update_file_system_ontap_configuration.UpdateFileSystemOntapConfiguration"
        ] = None,
        open_zfs_configuration: Optional[
            "capo_fsx.types.update_file_system_open_zfs_configuration.UpdateFileSystemOpenZFSConfiguration"
        ] = None,
        storage_type: Optional["capo_fsx.types.storage_type.StorageType"] = None,
        file_system_type_version: Optional[
            "capo_fsx.types.file_system_type_version.FileSystemTypeVersion"
        ] = None,
        network_type: Optional["capo_fsx.types.network_type.NetworkType"] = None,
    ) -> "capo_fsx.types.update_file_system_response.UpdateFileSystemResponse":
        """<p>Use this operation to update the configuration of an existing Amazon FSx file system. You can update multiple properties in a single request.</p> <p>For FSx for Windows File Server file systems, you can update the following properties:</p> <ul> <li> <p> <code>AuditLogConfiguration</code> </p> </li> <li> <p> <code>AutomaticBackupRetentionDays</code> </p> </li> <li> <p> <code>DailyAutomaticBackupStartTime</code> </p> </li> <li> <p> <code>DiskIopsConfiguration</code> </p> </li> <li> <p> <code>SelfManagedActiveDirectoryConfiguration</code> </p> </li> <li> <p> <code>StorageCapacity</code> </p> </li> <li> <p> <code>StorageType</code> </p> </li> <li> <p> <code>ThroughputCapacity</code> </p> </li> <li> <p> <code>WeeklyMaintenanceStartTime</code> </p> </li> </ul> <p>For FSx for Lustre file systems, you can update the following properties:</p> <ul> <li> <p> <code>AutoImportPolicy</code> </p> </li> <li> <p> <code>AutomaticBackupRetentionDays</code> </p> </li> <li> <p> <code>DailyAutomaticBackupStartTime</code> </p> </li> <li> <p> <code>DataCompressionType</code> </p> </li> <li> <p> <code>FileSystemTypeVersion</code> </p> </li> <li> <p> <code>LogConfiguration</code> </p> </li> <li> <p> <code>LustreReadCacheConfiguration</code> </p> </li> <li> <p> <code>LustreRootSquashConfiguration</code> </p> </li> <li> <p> <code>MetadataConfiguration</code> </p> </li> <li> <p> <code>PerUnitStorageThroughput</code> </p> </li> <li> <p> <code>StorageCapacity</code> </p> </li> <li> <p> <code>ThroughputCapacity</code> </p> </li> <li> <p> <code>WeeklyMaintenanceStartTime</code> </p> </li> </ul> <p>For FSx for ONTAP file systems, you can update the following properties:</p> <ul> <li> <p> <code>AddRouteTableIds</code> </p> </li> <li> <p> <code>AutomaticBackupRetentionDays</code> </p> </li> <li> <p> <code>DailyAutomaticBackupStartTime</code> </p> </li> <li> <p> <code>DiskIopsConfiguration</code> </p> </li> <li> <p> <code>EndpointIpv6AddressRange</code> </p> </li> <li> <p> <code>FsxAdminPassword</code> </p> </li> <li> <p> <code>HAPairs</code> </p> </li> <li> <p> <code>RemoveRouteTableIds</code> </p> </li> <li> <p> <code>StorageCapacity</code> </p> </li> <li> <p> <code>ThroughputCapacity</code> </p> </li> <li> <p> <code>ThroughputCapacityPerHAPair</code> </p> </li> <li> <p> <code>WeeklyMaintenanceStartTime</code> </p> </li> </ul> <p>For FSx for OpenZFS file systems, you can update the following properties:</p> <ul> <li> <p> <code>AddRouteTableIds</code> </p> </li> <li> <p> <code>AutomaticBackupRetentionDays</code> </p> </li> <li> <p> <code>CopyTagsToBackups</code> </p> </li> <li> <p> <code>CopyTagsToVolumes</code> </p> </li> <li> <p> <code>DailyAutomaticBackupStartTime</code> </p> </li> <li> <p> <code>DiskIopsConfiguration</code> </p> </li> <li> <p> <code>EndpointIpv6AddressRange</code> </p> </li> <li> <p> <code>ReadCacheConfiguration</code> </p> </li> <li> <p> <code>RemoveRouteTableIds</code> </p> </li> <li> <p> <code>StorageCapacity</code> </p> </li> <li> <p> <code>ThroughputCapacity</code> </p> </li> <li> <p> <code>WeeklyMaintenanceStartTime</code> </p> </li> </ul>

        Args:
            file_system_id: <p>The ID of the file system that you are updating.</p>
            client_request_token: <p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent updates. This string is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>
            storage_capacity: <p>Use this parameter to increase the storage capacity of an FSx for Windows File Server, FSx for Lustre, FSx for OpenZFS, or FSx for ONTAP file system. For second-generation FSx for ONTAP file systems, you can also decrease the storage capacity. Specifies the storage capacity target value, in GiB, for the file system that you're updating. </p> <note> <p>You can't make a storage capacity increase request if there is an existing storage capacity increase request in progress.</p> </note> <p>For Lustre file systems, the storage capacity target value can be the following:</p> <ul> <li> <p>For <code>SCRATCH_2</code>, <code>PERSISTENT_1</code>, and <code>PERSISTENT_2 SSD</code> deployment types, valid values are in multiples of 2400 GiB. The value must be greater than the current storage capacity.</p> </li> <li> <p>For <code>PERSISTENT HDD</code> file systems, valid values are multiples of 6000 GiB for 12-MBps throughput per TiB file systems and multiples of 1800 GiB for 40-MBps throughput per TiB file systems. The values must be greater than the current storage capacity.</p> </li> <li> <p>For <code>SCRATCH_1</code> file systems, you can't increase the storage capacity.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html">Managing storage and throughput capacity</a> in the <i>FSx for Lustre User Guide</i>.</p> <p>For FSx for OpenZFS file systems, the storage capacity target value must be at least 10 percent greater than the current storage capacity value. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-storage-capacity.html">Managing storage capacity</a> in the <i>FSx for OpenZFS User Guide</i>.</p> <p>For Windows file systems, the storage capacity target value must be at least 10 percent greater than the current storage capacity value. To increase storage capacity, the file system must have at least 16 MBps of throughput capacity. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html">Managing storage capacity</a> in the <i>Amazon FSxfor Windows File Server User Guide</i>.</p> <p>For ONTAP file systems, when increasing storage capacity, the storage capacity target value must be at least 10 percent greater than the current storage capacity value. When decreasing storage capacity on second-generation file systems, the target value must be at least 9 percent smaller than the current SSD storage capacity. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html">File system storage capacity and IOPS</a> in the Amazon FSx for NetApp ONTAP User Guide.</p>
            windows_configuration: <p>The configuration updates for an Amazon FSx for Windows File Server file system.</p>
            open_zfs_configuration: <p>The configuration updates for an FSx for OpenZFS file system.</p>
            file_system_type_version: <p>The Lustre version you are updating an FSx for Lustre file system to. Valid values are <code>2.12</code> and <code>2.15</code>. The value you choose must be newer than the file system's current Lustre version.</p>
            network_type: <p>Changes the network type of an FSx for OpenZFS file system.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.file_system_not_found.FileSystemNotFound: <p>No Amazon FSx file systems were found based upon supplied parameters.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.invalid_network_settings.InvalidNetworkSettings: <p>One or more network settings specified in the request are invalid.</p>
            capo_fsx.errors.missing_file_system_configuration.MissingFileSystemConfiguration: <p>A file system configuration is required for this operation.</p>
            capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded: <p>An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting Amazon Web Services Support.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.update_file_system_request.UpdateFileSystemRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.update_file_system_response.UpdateFileSystemResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.update_file_system

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.update_file_system.update_file_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.update_file_system_request.UpdateFileSystemRequest = {}
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if windows_configuration is not None:
            input_["windows_configuration"] = windows_configuration
        if lustre_configuration is not None:
            input_["lustre_configuration"] = lustre_configuration
        if ontap_configuration is not None:
            input_["ontap_configuration"] = ontap_configuration
        if open_zfs_configuration is not None:
            input_["open_zfs_configuration"] = open_zfs_configuration
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if file_system_type_version is not None:
            input_["file_system_type_version"] = file_system_type_version
        if network_type is not None:
            input_["network_type"] = network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_shared_vpc_configuration(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        enable_fsx_route_table_updates_from_participant_accounts: Optional[
            "capo_fsx.types.verbose_flag.VerboseFlag"
        ] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_fsx.types.update_shared_vpc_configuration_response.UpdateSharedVpcConfigurationResponse":
        """<p>Configures whether participant accounts in your organization can create Amazon FSx for NetApp ONTAP Multi-AZ file systems in subnets that are shared by a virtual private cloud (VPC) owner. For more information, see the <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/maz-shared-vpc.html">Amazon FSx for NetApp ONTAP User Guide</a>.</p> <note> <p>We strongly recommend that participant-created Multi-AZ file systems in the shared VPC are deleted before you disable this feature. Once the feature is disabled, these file systems will enter a <code>MISCONFIGURED</code> state and behave like Single-AZ file systems. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/maz-shared-vpc.html#disabling-maz-vpc-sharing">Important considerations before disabling shared VPC support for Multi-AZ file systems</a>.</p> </note>

        Args:
            enable_fsx_route_table_updates_from_participant_accounts: <p>Specifies whether participant accounts can create FSx for ONTAP Multi-AZ file systems in shared subnets. Set to <code>true</code> to enable or <code>false</code> to disable.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.update_shared_vpc_configuration_request.UpdateSharedVpcConfigurationRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.update_shared_vpc_configuration_response.UpdateSharedVpcConfigurationResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.update_shared_vpc_configuration

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.update_shared_vpc_configuration.update_shared_vpc_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.update_shared_vpc_configuration_request.UpdateSharedVpcConfigurationRequest = {}
        if enable_fsx_route_table_updates_from_participant_accounts is not None:
            input_["enable_fsx_route_table_updates_from_participant_accounts"] = (
                enable_fsx_route_table_updates_from_participant_accounts
            )
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_snapshot(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        name: Optional["capo_fsx.types.snapshot_name.SnapshotName"] = None,
        snapshot_id: Optional["capo_fsx.types.snapshot_id.SnapshotId"] = None,
    ) -> "capo_fsx.types.update_snapshot_response.UpdateSnapshotResponse":
        """<p>Updates the name of an Amazon FSx for OpenZFS snapshot.</p>

        Args:
            name: <p>The name of the snapshot to update.</p>
            snapshot_id: <p>The ID of the snapshot that you want to update, in the format <code>fsvolsnap-0123456789abcdef0</code>.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.snapshot_not_found.SnapshotNotFound: <p>No Amazon FSx snapshots were found based on the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.update_snapshot_request.UpdateSnapshotRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.update_snapshot_response.UpdateSnapshotResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.update_snapshot

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.update_snapshot.update_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.update_snapshot_request.UpdateSnapshotRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if name is not None:
            input_["name"] = name
        if snapshot_id is not None:
            input_["snapshot_id"] = snapshot_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_storage_virtual_machine(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        active_directory_configuration: Optional[
            "capo_fsx.types.update_svm_active_directory_configuration.UpdateSvmActiveDirectoryConfiguration"
        ] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        storage_virtual_machine_id: Optional[
            "capo_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
        ] = None,
        svm_admin_password: Optional[
            "capo_fsx.types.admin_password.AdminPassword"
        ] = None,
    ) -> "capo_fsx.types.update_storage_virtual_machine_response.UpdateStorageVirtualMachineResponse":
        """<p>Updates an FSx for ONTAP storage virtual machine (SVM).</p>

        Args:
            active_directory_configuration: <p>Specifies updates to an SVM's Microsoft Active Directory (AD) configuration.</p>
            storage_virtual_machine_id: <p>The ID of the SVM that you want to update, in the format <code>svm-0123456789abcdef0</code>.</p>
            svm_admin_password: <p>Specifies a new SvmAdminPassword.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.storage_virtual_machine_not_found.StorageVirtualMachineNotFound: <p>No FSx for ONTAP SVMs were found based upon the supplied parameters.</p>
            capo_fsx.errors.unsupported_operation.UnsupportedOperation: <p>The requested operation is not supported for this resource or API.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.update_storage_virtual_machine_request.UpdateStorageVirtualMachineRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.update_storage_virtual_machine_response.UpdateStorageVirtualMachineResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.update_storage_virtual_machine

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.update_storage_virtual_machine.update_storage_virtual_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.update_storage_virtual_machine_request.UpdateStorageVirtualMachineRequest = {}
        if active_directory_configuration is not None:
            input_["active_directory_configuration"] = active_directory_configuration
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if storage_virtual_machine_id is not None:
            input_["storage_virtual_machine_id"] = storage_virtual_machine_id
        if svm_admin_password is not None:
            input_["svm_admin_password"] = svm_admin_password

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_volume(
        self,
        *,
        config_overrides: Optional[FSxClientConfig] = None,
        client_request_token: Optional[
            "capo_fsx.types.client_request_token.ClientRequestToken"
        ] = None,
        volume_id: Optional["capo_fsx.types.volume_id.VolumeId"] = None,
        ontap_configuration: Optional[
            "capo_fsx.types.update_ontap_volume_configuration.UpdateOntapVolumeConfiguration"
        ] = None,
        name: Optional["capo_fsx.types.volume_name.VolumeName"] = None,
        open_zfs_configuration: Optional[
            "capo_fsx.types.update_open_zfs_volume_configuration.UpdateOpenZFSVolumeConfiguration"
        ] = None,
    ) -> "capo_fsx.types.update_volume_response.UpdateVolumeResponse":
        """<p>Updates the configuration of an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volume.</p>

        Args:
            volume_id: <p>The ID of the volume that you want to update, in the format <code>fsvol-0123456789abcdef0</code>.</p>
            ontap_configuration: <p>The configuration of the ONTAP volume that you are updating.</p>
            name: <p>The name of the OpenZFS volume. OpenZFS root volumes are automatically named <code>FSX</code>. Child volume names must be unique among their parent volume's children. The name of the volume is part of the mount string for the OpenZFS volume. </p>
            open_zfs_configuration: <p>The configuration of the OpenZFS volume that you are updating.</p>

        Raises:
            capo_fsx.errors.bad_request.BadRequest: <p>A generic error indicating a failure with a client request.</p>
            capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError: <p>The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.</p>
            capo_fsx.errors.internal_server_error.InternalServerError: <p>A generic error indicating a server-side failure.</p>
            capo_fsx.errors.missing_volume_configuration.MissingVolumeConfiguration: <p>A volume configuration is required for this operation.</p>
            capo_fsx.errors.volume_not_found.VolumeNotFound: <p>No Amazon FSx volumes were found based upon the supplied parameters.</p>
            capo_fsx.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_fsx.types.update_volume_request.UpdateVolumeRequest]",
        ) -> OperationResponse[
            "capo_fsx.types.update_volume_response.UpdateVolumeResponse"
        ]:
            import capo_fsx._operations.aws_simba_api_service_v20180301.update_volume

            output, http_response = (
                capo_fsx._operations.aws_simba_api_service_v20180301.update_volume.update_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fsx.types.update_volume_request.UpdateVolumeRequest = {}
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_id is not None:
            input_["volume_id"] = volume_id
        if ontap_configuration is not None:
            input_["ontap_configuration"] = ontap_configuration
        if name is not None:
            input_["name"] = name
        if open_zfs_configuration is not None:
            input_["open_zfs_configuration"] = open_zfs_configuration

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
