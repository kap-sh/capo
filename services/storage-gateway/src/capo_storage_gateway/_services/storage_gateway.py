"""Generated from Smithy shape ``com.amazonaws.storagegateway#StorageGateway_20130630``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_storage_gateway._auth._signers
import capo_storage_gateway._auth._sigv4
from capo_storage_gateway._auth._identity import Credentials
from capo_storage_gateway._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_storage_gateway._auth._zapros_handler import AuthMiddleware
from capo_storage_gateway._pagination import resolve_path as _resolve_path
from capo_storage_gateway._services._aws_config import aws_config
from capo_storage_gateway._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_storage_gateway.types.activate_gateway_input
    import capo_storage_gateway.types.activate_gateway_output
    import capo_storage_gateway.types.activation_key
    import capo_storage_gateway.types.add_cache_input
    import capo_storage_gateway.types.add_cache_output
    import capo_storage_gateway.types.add_tags_to_resource_input
    import capo_storage_gateway.types.add_tags_to_resource_output
    import capo_storage_gateway.types.add_upload_buffer_input
    import capo_storage_gateway.types.add_upload_buffer_output
    import capo_storage_gateway.types.add_working_storage_input
    import capo_storage_gateway.types.add_working_storage_output
    import capo_storage_gateway.types.assign_tape_pool_input
    import capo_storage_gateway.types.assign_tape_pool_output
    import capo_storage_gateway.types.associate_file_system_input
    import capo_storage_gateway.types.associate_file_system_output
    import capo_storage_gateway.types.attach_volume_input
    import capo_storage_gateway.types.attach_volume_output
    import capo_storage_gateway.types.audit_destination_arn
    import capo_storage_gateway.types.authentication
    import capo_storage_gateway.types.automatic_tape_creation_rules
    import capo_storage_gateway.types.bandwidth_download_rate_limit
    import capo_storage_gateway.types.bandwidth_rate_limit_intervals
    import capo_storage_gateway.types.bandwidth_type
    import capo_storage_gateway.types.bandwidth_upload_rate_limit
    import capo_storage_gateway.types.boolean
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.cache_attributes
    import capo_storage_gateway.types.cache_report_arn
    import capo_storage_gateway.types.cache_report_filter_list
    import capo_storage_gateway.types.cache_report_info
    import capo_storage_gateway.types.cancel_archival_input
    import capo_storage_gateway.types.cancel_archival_output
    import capo_storage_gateway.types.cancel_cache_report_input
    import capo_storage_gateway.types.cancel_cache_report_output
    import capo_storage_gateway.types.cancel_retrieval_input
    import capo_storage_gateway.types.cancel_retrieval_output
    import capo_storage_gateway.types.case_sensitivity
    import capo_storage_gateway.types.chap_secret
    import capo_storage_gateway.types.client_token
    import capo_storage_gateway.types.cloud_watch_log_group_arn
    import capo_storage_gateway.types.create_cachedi_scsi_volume_input
    import capo_storage_gateway.types.create_cachedi_scsi_volume_output
    import capo_storage_gateway.types.create_nfs_file_share_input
    import capo_storage_gateway.types.create_nfs_file_share_output
    import capo_storage_gateway.types.create_smb_file_share_input
    import capo_storage_gateway.types.create_smb_file_share_output
    import capo_storage_gateway.types.create_snapshot_from_volume_recovery_point_input
    import capo_storage_gateway.types.create_snapshot_from_volume_recovery_point_output
    import capo_storage_gateway.types.create_snapshot_input
    import capo_storage_gateway.types.create_snapshot_output
    import capo_storage_gateway.types.create_storedi_scsi_volume_input
    import capo_storage_gateway.types.create_storedi_scsi_volume_output
    import capo_storage_gateway.types.create_tape_pool_input
    import capo_storage_gateway.types.create_tape_pool_output
    import capo_storage_gateway.types.create_tape_with_barcode_input
    import capo_storage_gateway.types.create_tape_with_barcode_output
    import capo_storage_gateway.types.create_tapes_input
    import capo_storage_gateway.types.create_tapes_output
    import capo_storage_gateway.types.day_of_month
    import capo_storage_gateway.types.day_of_week
    import capo_storage_gateway.types.delete_automatic_tape_creation_policy_input
    import capo_storage_gateway.types.delete_automatic_tape_creation_policy_output
    import capo_storage_gateway.types.delete_bandwidth_rate_limit_input
    import capo_storage_gateway.types.delete_bandwidth_rate_limit_output
    import capo_storage_gateway.types.delete_cache_report_input
    import capo_storage_gateway.types.delete_cache_report_output
    import capo_storage_gateway.types.delete_chap_credentials_input
    import capo_storage_gateway.types.delete_chap_credentials_output
    import capo_storage_gateway.types.delete_file_share_input
    import capo_storage_gateway.types.delete_file_share_output
    import capo_storage_gateway.types.delete_gateway_input
    import capo_storage_gateway.types.delete_gateway_output
    import capo_storage_gateway.types.delete_snapshot_schedule_input
    import capo_storage_gateway.types.delete_snapshot_schedule_output
    import capo_storage_gateway.types.delete_tape_archive_input
    import capo_storage_gateway.types.delete_tape_archive_output
    import capo_storage_gateway.types.delete_tape_input
    import capo_storage_gateway.types.delete_tape_output
    import capo_storage_gateway.types.delete_tape_pool_input
    import capo_storage_gateway.types.delete_tape_pool_output
    import capo_storage_gateway.types.delete_volume_input
    import capo_storage_gateway.types.delete_volume_output
    import capo_storage_gateway.types.describe_availability_monitor_test_input
    import capo_storage_gateway.types.describe_availability_monitor_test_output
    import capo_storage_gateway.types.describe_bandwidth_rate_limit_input
    import capo_storage_gateway.types.describe_bandwidth_rate_limit_output
    import capo_storage_gateway.types.describe_bandwidth_rate_limit_schedule_input
    import capo_storage_gateway.types.describe_bandwidth_rate_limit_schedule_output
    import capo_storage_gateway.types.describe_cache_input
    import capo_storage_gateway.types.describe_cache_output
    import capo_storage_gateway.types.describe_cache_report_input
    import capo_storage_gateway.types.describe_cache_report_output
    import capo_storage_gateway.types.describe_cachedi_scsi_volumes_input
    import capo_storage_gateway.types.describe_cachedi_scsi_volumes_output
    import capo_storage_gateway.types.describe_chap_credentials_input
    import capo_storage_gateway.types.describe_chap_credentials_output
    import capo_storage_gateway.types.describe_file_system_associations_input
    import capo_storage_gateway.types.describe_file_system_associations_output
    import capo_storage_gateway.types.describe_gateway_information_input
    import capo_storage_gateway.types.describe_gateway_information_output
    import capo_storage_gateway.types.describe_maintenance_start_time_input
    import capo_storage_gateway.types.describe_maintenance_start_time_output
    import capo_storage_gateway.types.describe_nfs_file_shares_input
    import capo_storage_gateway.types.describe_nfs_file_shares_output
    import capo_storage_gateway.types.describe_smb_file_shares_input
    import capo_storage_gateway.types.describe_smb_file_shares_output
    import capo_storage_gateway.types.describe_smb_settings_input
    import capo_storage_gateway.types.describe_smb_settings_output
    import capo_storage_gateway.types.describe_snapshot_schedule_input
    import capo_storage_gateway.types.describe_snapshot_schedule_output
    import capo_storage_gateway.types.describe_storedi_scsi_volumes_input
    import capo_storage_gateway.types.describe_storedi_scsi_volumes_output
    import capo_storage_gateway.types.describe_tape_archives_input
    import capo_storage_gateway.types.describe_tape_archives_output
    import capo_storage_gateway.types.describe_tape_recovery_points_input
    import capo_storage_gateway.types.describe_tape_recovery_points_output
    import capo_storage_gateway.types.describe_tapes_input
    import capo_storage_gateway.types.describe_tapes_output
    import capo_storage_gateway.types.describe_upload_buffer_input
    import capo_storage_gateway.types.describe_upload_buffer_output
    import capo_storage_gateway.types.describe_vtl_devices_input
    import capo_storage_gateway.types.describe_vtl_devices_output
    import capo_storage_gateway.types.describe_working_storage_input
    import capo_storage_gateway.types.describe_working_storage_output
    import capo_storage_gateway.types.description
    import capo_storage_gateway.types.detach_volume_input
    import capo_storage_gateway.types.detach_volume_output
    import capo_storage_gateway.types.device_type
    import capo_storage_gateway.types.disable_gateway_input
    import capo_storage_gateway.types.disable_gateway_output
    import capo_storage_gateway.types.disassociate_file_system_input
    import capo_storage_gateway.types.disassociate_file_system_output
    import capo_storage_gateway.types.disk_id
    import capo_storage_gateway.types.disk_ids
    import capo_storage_gateway.types.dns_host_name
    import capo_storage_gateway.types.domain_name
    import capo_storage_gateway.types.domain_user_name
    import capo_storage_gateway.types.domain_user_password
    import capo_storage_gateway.types.encryption_type
    import capo_storage_gateway.types.endpoint_network_configuration
    import capo_storage_gateway.types.evict_files_failing_upload_input
    import capo_storage_gateway.types.evict_files_failing_upload_output
    import capo_storage_gateway.types.file_share_arn
    import capo_storage_gateway.types.file_share_arn_list
    import capo_storage_gateway.types.file_share_client_list
    import capo_storage_gateway.types.file_share_info
    import capo_storage_gateway.types.file_share_name
    import capo_storage_gateway.types.file_system_association_arn
    import capo_storage_gateway.types.file_system_association_arn_list
    import capo_storage_gateway.types.file_system_association_summary
    import capo_storage_gateway.types.file_system_location_arn
    import capo_storage_gateway.types.folder_list
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.gateway_capacity
    import capo_storage_gateway.types.gateway_info
    import capo_storage_gateway.types.gateway_name
    import capo_storage_gateway.types.gateway_timezone
    import capo_storage_gateway.types.gateway_type
    import capo_storage_gateway.types.hosts
    import capo_storage_gateway.types.hour_of_day
    import capo_storage_gateway.types.iqn_name
    import capo_storage_gateway.types.join_domain_input
    import capo_storage_gateway.types.join_domain_output
    import capo_storage_gateway.types.kms_key
    import capo_storage_gateway.types.list_automatic_tape_creation_policies_input
    import capo_storage_gateway.types.list_automatic_tape_creation_policies_output
    import capo_storage_gateway.types.list_cache_reports_input
    import capo_storage_gateway.types.list_cache_reports_output
    import capo_storage_gateway.types.list_file_shares_input
    import capo_storage_gateway.types.list_file_shares_output
    import capo_storage_gateway.types.list_file_system_associations_input
    import capo_storage_gateway.types.list_file_system_associations_output
    import capo_storage_gateway.types.list_gateways_input
    import capo_storage_gateway.types.list_gateways_output
    import capo_storage_gateway.types.list_local_disks_input
    import capo_storage_gateway.types.list_local_disks_output
    import capo_storage_gateway.types.list_tags_for_resource_input
    import capo_storage_gateway.types.list_tags_for_resource_output
    import capo_storage_gateway.types.list_tape_pools_input
    import capo_storage_gateway.types.list_tape_pools_output
    import capo_storage_gateway.types.list_tapes_input
    import capo_storage_gateway.types.list_tapes_output
    import capo_storage_gateway.types.list_volume_initiators_input
    import capo_storage_gateway.types.list_volume_initiators_output
    import capo_storage_gateway.types.list_volume_recovery_points_input
    import capo_storage_gateway.types.list_volume_recovery_points_output
    import capo_storage_gateway.types.list_volumes_input
    import capo_storage_gateway.types.list_volumes_output
    import capo_storage_gateway.types.local_console_password
    import capo_storage_gateway.types.location_arn
    import capo_storage_gateway.types.long
    import capo_storage_gateway.types.marker
    import capo_storage_gateway.types.medium_changer_type
    import capo_storage_gateway.types.minute_of_hour
    import capo_storage_gateway.types.network_interface_id
    import capo_storage_gateway.types.nfs_file_share_defaults
    import capo_storage_gateway.types.notification_policy
    import capo_storage_gateway.types.notify_when_uploaded_input
    import capo_storage_gateway.types.notify_when_uploaded_output
    import capo_storage_gateway.types.num_tapes_to_create
    import capo_storage_gateway.types.object_acl
    import capo_storage_gateway.types.organizational_unit
    import capo_storage_gateway.types.pool_ar_ns
    import capo_storage_gateway.types.pool_arn
    import capo_storage_gateway.types.pool_id
    import capo_storage_gateway.types.pool_info
    import capo_storage_gateway.types.pool_name
    import capo_storage_gateway.types.positive_int_object
    import capo_storage_gateway.types.recurrence_in_hours
    import capo_storage_gateway.types.refresh_cache_input
    import capo_storage_gateway.types.refresh_cache_output
    import capo_storage_gateway.types.region_id
    import capo_storage_gateway.types.remove_tags_from_resource_input
    import capo_storage_gateway.types.remove_tags_from_resource_output
    import capo_storage_gateway.types.reset_cache_input
    import capo_storage_gateway.types.reset_cache_output
    import capo_storage_gateway.types.resource_arn
    import capo_storage_gateway.types.retention_lock_time_in_days
    import capo_storage_gateway.types.retention_lock_type
    import capo_storage_gateway.types.retrieve_tape_archive_input
    import capo_storage_gateway.types.retrieve_tape_archive_output
    import capo_storage_gateway.types.retrieve_tape_recovery_point_input
    import capo_storage_gateway.types.retrieve_tape_recovery_point_output
    import capo_storage_gateway.types.role
    import capo_storage_gateway.types.set_local_console_password_input
    import capo_storage_gateway.types.set_local_console_password_output
    import capo_storage_gateway.types.set_smb_guest_password_input
    import capo_storage_gateway.types.set_smb_guest_password_output
    import capo_storage_gateway.types.shutdown_gateway_input
    import capo_storage_gateway.types.shutdown_gateway_output
    import capo_storage_gateway.types.smb_guest_password
    import capo_storage_gateway.types.smb_local_groups
    import capo_storage_gateway.types.smb_security_strategy
    import capo_storage_gateway.types.snapshot_description
    import capo_storage_gateway.types.snapshot_id
    import capo_storage_gateway.types.software_update_preferences
    import capo_storage_gateway.types.squash
    import capo_storage_gateway.types.start_availability_monitor_test_input
    import capo_storage_gateway.types.start_availability_monitor_test_output
    import capo_storage_gateway.types.start_cache_report_input
    import capo_storage_gateway.types.start_cache_report_output
    import capo_storage_gateway.types.start_gateway_input
    import capo_storage_gateway.types.start_gateway_output
    import capo_storage_gateway.types.storage_class
    import capo_storage_gateway.types.tag
    import capo_storage_gateway.types.tag_keys
    import capo_storage_gateway.types.tags
    import capo_storage_gateway.types.tape
    import capo_storage_gateway.types.tape_ar_ns
    import capo_storage_gateway.types.tape_archive
    import capo_storage_gateway.types.tape_arn
    import capo_storage_gateway.types.tape_barcode
    import capo_storage_gateway.types.tape_barcode_prefix
    import capo_storage_gateway.types.tape_drive_type
    import capo_storage_gateway.types.tape_info
    import capo_storage_gateway.types.tape_recovery_point_info
    import capo_storage_gateway.types.tape_size
    import capo_storage_gateway.types.tape_storage_class
    import capo_storage_gateway.types.target_arn
    import capo_storage_gateway.types.target_name
    import capo_storage_gateway.types.timeout_in_seconds
    import capo_storage_gateway.types.update_automatic_tape_creation_policy_input
    import capo_storage_gateway.types.update_automatic_tape_creation_policy_output
    import capo_storage_gateway.types.update_bandwidth_rate_limit_input
    import capo_storage_gateway.types.update_bandwidth_rate_limit_output
    import capo_storage_gateway.types.update_bandwidth_rate_limit_schedule_input
    import capo_storage_gateway.types.update_bandwidth_rate_limit_schedule_output
    import capo_storage_gateway.types.update_chap_credentials_input
    import capo_storage_gateway.types.update_chap_credentials_output
    import capo_storage_gateway.types.update_file_system_association_input
    import capo_storage_gateway.types.update_file_system_association_output
    import capo_storage_gateway.types.update_gateway_information_input
    import capo_storage_gateway.types.update_gateway_information_output
    import capo_storage_gateway.types.update_gateway_software_now_input
    import capo_storage_gateway.types.update_gateway_software_now_output
    import capo_storage_gateway.types.update_maintenance_start_time_input
    import capo_storage_gateway.types.update_maintenance_start_time_output
    import capo_storage_gateway.types.update_nfs_file_share_input
    import capo_storage_gateway.types.update_nfs_file_share_output
    import capo_storage_gateway.types.update_smb_file_share_input
    import capo_storage_gateway.types.update_smb_file_share_output
    import capo_storage_gateway.types.update_smb_file_share_visibility_input
    import capo_storage_gateway.types.update_smb_file_share_visibility_output
    import capo_storage_gateway.types.update_smb_local_groups_input
    import capo_storage_gateway.types.update_smb_local_groups_output
    import capo_storage_gateway.types.update_smb_security_strategy_input
    import capo_storage_gateway.types.update_smb_security_strategy_output
    import capo_storage_gateway.types.update_snapshot_schedule_input
    import capo_storage_gateway.types.update_snapshot_schedule_output
    import capo_storage_gateway.types.update_vtl_device_type_input
    import capo_storage_gateway.types.update_vtl_device_type_output
    import capo_storage_gateway.types.user_list
    import capo_storage_gateway.types.volume_ar_ns
    import capo_storage_gateway.types.volume_arn
    import capo_storage_gateway.types.volume_info
    import capo_storage_gateway.types.vtl_device
    import capo_storage_gateway.types.vtl_device_ar_ns
    import capo_storage_gateway.types.vtl_device_arn


class StorageGatewayClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class StorageGatewayClient:
    """A client for the ``StorageGateway`` service.

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
        self._config = StorageGatewayClientConfig(
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
        self, config_overrides: Optional[StorageGatewayClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: StorageGatewayClientConfig = config_overrides or {}
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

    def activate_gateway(
        self,
        activation_key: "capo_storage_gateway.types.activation_key.ActivationKey",
        gateway_name: "capo_storage_gateway.types.gateway_name.GatewayName",
        gateway_timezone: "capo_storage_gateway.types.gateway_timezone.GatewayTimezone",
        gateway_region: "capo_storage_gateway.types.region_id.RegionId",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        gateway_type: Optional[
            "capo_storage_gateway.types.gateway_type.GatewayType"
        ] = None,
        tape_drive_type: Optional[
            "capo_storage_gateway.types.tape_drive_type.TapeDriveType"
        ] = None,
        medium_changer_type: Optional[
            "capo_storage_gateway.types.medium_changer_type.MediumChangerType"
        ] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.activate_gateway_output.ActivateGatewayOutput":
        """<p>Activates the gateway you previously deployed on your host. In the activation process, you specify information such as the Amazon Web Services Region that you want to use for storing snapshots or tapes, the time zone for scheduled snapshots the gateway snapshot schedule window, an activation key, and a name for your gateway. The activation process also associates your gateway with your account. For more information, see <a>UpdateGatewayInformation</a>.</p> <note> <p>You must turn on the gateway VM before you can activate your gateway.</p> </note>

        Args:
            activation_key: <p>Your gateway activation key. You can obtain the activation key by sending an HTTP GET request with redirects enabled to the gateway IP address (port 80). The redirect URL returned in the response provides you the activation key for your gateway in the query string parameter <code>activationKey</code>. It may also include other activation-related parameters, however, these are merely defaults -- the arguments you pass to the <code>ActivateGateway</code> API call determine the actual configuration of your gateway.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Getting activation key</a> in the <i>Storage Gateway User Guide</i>.</p>
            gateway_name: <p>The name you configured for your gateway.</p>
            gateway_timezone: <p>A value that indicates the time zone you want to set for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, GMT indicates Greenwich Mean Time without any offset. GMT-4:00 indicates the time is 4 hours behind GMT. GMT+2:00 indicates the time is 2 hours ahead of GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.</p>
            gateway_region: <p>A value that indicates the Amazon Web Services Region where you want to store your data. The gateway Amazon Web Services Region specified must be the same Amazon Web Services Region as the Amazon Web Services Region in your <code>Host</code> header in the request. For more information about available Amazon Web Services Regions and endpoints for Storage Gateway, see <a href="https://docs.aws.amazon.com/general/latest/gr/sg.html"> Storage Gateway endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p> <p>Valid Values: See <a href="https://docs.aws.amazon.com/general/latest/gr/sg.html"> Storage Gateway endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>. </p>
            gateway_type: <p>A value that defines the type of gateway to activate. The type specified is critical to all later functions of the gateway and cannot be changed after activation. The default value is <code>CACHED</code>.</p> <important> <p>Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit <a href="https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/">this blog post</a>.</p> </important> <p>Valid Values: <code>STORED</code> | <code>CACHED</code> | <code>VTL</code> | <code>FILE_S3</code> | <code>FILE_FSX_SMB</code> </p>
            tape_drive_type: <p>The value that indicates the type of tape drive to use for tape gateway. This field is optional.</p> <p>Valid Values: <code>IBM-ULT3580-TD5</code> </p>
            medium_changer_type: <p>The value that indicates the type of medium changer to use for tape gateway. This field is optional.</p> <p>Valid Values: <code>STK-L700</code> | <code>AWS-Gateway-VTL</code> | <code>IBM-03584L32-0402</code> </p>
            tags: <p>A list of up to 50 tags that you can assign to the gateway. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers that can be represented in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256 characters.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To activate the gateway
            Activates the gateway you previously deployed on your host.

            >>> client.activate_gateway(activation_key='29AV1-3OFV9-VVIUB-NKT0I-LRO6V', gateway_name='My_Gateway', gateway_timezone='GMT-12:00', gateway_region='us-east-1', gateway_type='STORED', tape_drive_type='IBM-ULT3580-TD5', medium_changer_type='AWS-Gateway-VTL')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.activate_gateway_input.ActivateGatewayInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.activate_gateway_output.ActivateGatewayOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.activate_gateway

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.activate_gateway.activate_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.activate_gateway_input.ActivateGatewayInput = {
            "activation_key": activation_key,
            "gateway_name": gateway_name,
            "gateway_timezone": gateway_timezone,
            "gateway_region": gateway_region,
        }
        if gateway_type is not None:
            input_["gateway_type"] = gateway_type
        if tape_drive_type is not None:
            input_["tape_drive_type"] = tape_drive_type
        if medium_changer_type is not None:
            input_["medium_changer_type"] = medium_changer_type
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_cache(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        disk_ids: "capo_storage_gateway.types.disk_ids.DiskIds",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.add_cache_output.AddCacheOutput":
        """<p>Configures one or more gateway local disks as cache for a gateway. This operation is only supported in the cached volume, tape, and file gateway type (see <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html">How Storage Gateway works (architecture)</a>.</p> <p>In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add cache, and one or more disk IDs that you want to configure as cache.</p>

        Args:
            disk_ids: <p>An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the <a>ListLocalDisks</a> API.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a cache
            The following example shows a request that activates a gateway-stored volume.

            >>> client.add_cache(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', disk_ids=['pci-0000:03:00.0-scsi-0:0:0:0', 'pci-0000:03:00.0-scsi-0:0:1:0'])
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.add_cache_input.AddCacheInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.add_cache_output.AddCacheOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.add_cache

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.add_cache.add_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.add_cache_input.AddCacheInput = {
            "gateway_arn": gateway_arn,
            "disk_ids": disk_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_tags_to_resource(
        self,
        resource_arn: "capo_storage_gateway.types.resource_arn.ResourceARN",
        tags: "capo_storage_gateway.types.tags.Tags",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> (
        "capo_storage_gateway.types.add_tags_to_resource_output.AddTagsToResourceOutput"
    ):
        """<p>Adds one or more tags to the specified resource. You use tags to add metadata to resources, which you can use to categorize these resources. For example, you can categorize resources by purpose, owner, environment, or team. Each tag consists of a key and a value, which you define. You can add tags to the following Storage Gateway resources:</p> <ul> <li> <p>Storage gateways of all types</p> </li> <li> <p>Storage volumes</p> </li> <li> <p>Virtual tapes</p> </li> <li> <p>NFS and SMB file shares</p> </li> <li> <p>File System associations</p> </li> </ul> <p>You can create a maximum of 50 tags for each resource. Virtual tapes and storage volumes that are recovered to a new gateway maintain their tags.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to add tags to.</p>
            tags: <p>The key-value pair that represents the tag you want to add to the resource. The value can be an empty string.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add tags to resource
            Adds one or more tags to the specified resource.

            >>> client.add_tags_to_resource(resource_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B', tags=[{'Key': 'Dev Gatgeway Region', 'Value': 'East Coast'}])
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.add_tags_to_resource_input.AddTagsToResourceInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.add_tags_to_resource_output.AddTagsToResourceOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.add_tags_to_resource

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.add_tags_to_resource.add_tags_to_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.add_tags_to_resource_input.AddTagsToResourceInput = {
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

    def add_upload_buffer(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        disk_ids: "capo_storage_gateway.types.disk_ids.DiskIds",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.add_upload_buffer_output.AddUploadBufferOutput":
        """<p>Configures one or more gateway local disks as upload buffer for a specified gateway. This operation is supported for the stored volume, cached volume, and tape gateway types.</p> <p>In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add upload buffer, and one or more disk IDs that you want to configure as upload buffer.</p>

        Args:
            disk_ids: <p>An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the <a>ListLocalDisks</a> API.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add upload buffer on local disk
            Configures one or more gateway local disks as upload buffer for a specified gateway.

            >>> client.add_upload_buffer(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', disk_ids=['pci-0000:03:00.0-scsi-0:0:0:0', 'pci-0000:03:00.0-scsi-0:0:1:0'])
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.add_upload_buffer_input.AddUploadBufferInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.add_upload_buffer_output.AddUploadBufferOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.add_upload_buffer

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.add_upload_buffer.add_upload_buffer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.add_upload_buffer_input.AddUploadBufferInput = {
            "gateway_arn": gateway_arn,
            "disk_ids": disk_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_working_storage(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        disk_ids: "capo_storage_gateway.types.disk_ids.DiskIds",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> (
        "capo_storage_gateway.types.add_working_storage_output.AddWorkingStorageOutput"
    ):
        """<p>Configures one or more gateway local disks as working storage for a gateway. This operation is only supported in the stored volume gateway type. This operation is deprecated in cached volume API version 20120630. Use <a>AddUploadBuffer</a> instead.</p> <note> <p>Working storage is also referred to as upload buffer. You can also use the <a>AddUploadBuffer</a> operation to add upload buffer to a stored volume gateway.</p> </note> <p>In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add working storage, and one or more disk IDs that you want to configure as working storage.</p>

        Args:
            disk_ids: <p>An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the <a>ListLocalDisks</a> API.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add storage on local disk
            Configures one or more gateway local disks as working storage for a gateway. (Working storage is also referred to as upload buffer.)

            >>> client.add_working_storage(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', disk_ids=['pci-0000:03:00.0-scsi-0:0:0:0', 'pci-0000:03:00.0-scsi-0:0:1:0'])
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.add_working_storage_input.AddWorkingStorageInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.add_working_storage_output.AddWorkingStorageOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.add_working_storage

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.add_working_storage.add_working_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.add_working_storage_input.AddWorkingStorageInput = {
            "gateway_arn": gateway_arn,
            "disk_ids": disk_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def assign_tape_pool(
        self,
        tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN",
        pool_id: "capo_storage_gateway.types.pool_id.PoolId",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        bypass_governance_retention: Optional[
            "capo_storage_gateway.types.boolean2.Boolean2"
        ] = None,
    ) -> "capo_storage_gateway.types.assign_tape_pool_output.AssignTapePoolOutput":
        """<p>Assigns a tape to a tape pool for archiving. The tape assigned to a pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the S3 storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>

        Args:
            tape_arn: <p>The unique Amazon Resource Name (ARN) of the virtual tape that you want to add to the tape pool.</p>
            pool_id: <p>The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>
            bypass_governance_retention: <p>Set permissions to bypass governance retention. If the lock type of the archived tape is <code>Governance</code>, the tape's archived age is not older than <code>RetentionLockInDays</code>, and the user does not already have <code>BypassGovernanceRetention</code>, setting this to TRUE enables the user to bypass the retention lock. This parameter is set to true by default for calls from the console.</p> <p>Valid values: <code>TRUE</code> | <code>FALSE</code> </p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.assign_tape_pool_input.AssignTapePoolInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.assign_tape_pool_output.AssignTapePoolOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.assign_tape_pool

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.assign_tape_pool.assign_tape_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.assign_tape_pool_input.AssignTapePoolInput = {
            "tape_arn": tape_arn,
            "pool_id": pool_id,
        }
        if bypass_governance_retention is not None:
            input_["bypass_governance_retention"] = bypass_governance_retention

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_file_system(
        self,
        user_name: "capo_storage_gateway.types.domain_user_name.DomainUserName",
        password: "capo_storage_gateway.types.domain_user_password.DomainUserPassword",
        client_token: "capo_storage_gateway.types.client_token.ClientToken",
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        location_arn: "capo_storage_gateway.types.file_system_location_arn.FileSystemLocationARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
        audit_destination_arn: Optional[
            "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
        ] = None,
        cache_attributes: Optional[
            "capo_storage_gateway.types.cache_attributes.CacheAttributes"
        ] = None,
        endpoint_network_configuration: Optional[
            "capo_storage_gateway.types.endpoint_network_configuration.EndpointNetworkConfiguration"
        ] = None,
    ) -> "capo_storage_gateway.types.associate_file_system_output.AssociateFileSystemOutput":
        """<p>Associate an Amazon FSx file system with the FSx File Gateway. After the association process is complete, the file shares on the Amazon FSx file system are available for access through the gateway. This operation only supports the FSx File Gateway type.</p>

        Args:
            user_name: <p>The user name of the user credential that has permission to access the root share D$ of the Amazon FSx file system. The user account must belong to the Amazon FSx delegated admin user group.</p>
            password: <p>The password of the user credential.</p>
            client_token: <p>A unique string value that you supply that is used by the FSx File Gateway to ensure idempotent file system association creation.</p>
            location_arn: <p>The Amazon Resource Name (ARN) of the Amazon FSx file system to associate with the FSx File Gateway.</p>
            tags: <p>A list of up to 50 tags that can be assigned to the file system association. Each tag is a key-value pair.</p>
            audit_destination_arn: <p>The Amazon Resource Name (ARN) of the storage used for the audit logs.</p>
            endpoint_network_configuration: <p>Specifies the network configuration information for the gateway associated with the Amazon FSx file system.</p> <note> <p>If multiple file systems are associated with this gateway, this parameter's <code>IpAddresses</code> field is required.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.associate_file_system_input.AssociateFileSystemInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.associate_file_system_output.AssociateFileSystemOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.associate_file_system

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.associate_file_system.associate_file_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.associate_file_system_input.AssociateFileSystemInput = {
            "user_name": user_name,
            "password": password,
            "client_token": client_token,
            "gateway_arn": gateway_arn,
            "location_arn": location_arn,
        }
        if tags is not None:
            input_["tags"] = tags
        if audit_destination_arn is not None:
            input_["audit_destination_arn"] = audit_destination_arn
        if cache_attributes is not None:
            input_["cache_attributes"] = cache_attributes
        if endpoint_network_configuration is not None:
            input_["endpoint_network_configuration"] = endpoint_network_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def attach_volume(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN",
        network_interface_id: "capo_storage_gateway.types.network_interface_id.NetworkInterfaceId",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        target_name: Optional[
            "capo_storage_gateway.types.target_name.TargetName"
        ] = None,
        disk_id: Optional["capo_storage_gateway.types.disk_id.DiskId"] = None,
    ) -> "capo_storage_gateway.types.attach_volume_output.AttachVolumeOutput":
        """<p>Connects a volume to an iSCSI connection and then attaches the volume to the specified gateway. Detaching and attaching a volume enables you to recover your data from one gateway to a different gateway without creating a snapshot. It also makes it easier to move your volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway that you want to attach the volume to.</p>
            target_name: <p>The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying <code>TargetName</code> as <i>myvolume</i> results in the target ARN of <code>arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume</code>. The target name must be unique across all volumes on a gateway.</p> <p>If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.</p>
            volume_arn: <p>The Amazon Resource Name (ARN) of the volume to attach to the specified gateway.</p>
            network_interface_id: <p>The network interface of the gateway on which to expose the iSCSI target. Accepts IPv4 and IPv6 addresses. Use <a>DescribeGatewayInformation</a> to get a list of the network interfaces available on a gateway.</p> <p>Valid Values: A valid IP address.</p>
            disk_id: <p>The unique device ID or other distinguishing data that identifies the local disk used to create the volume. This value is only required when you are attaching a stored volume.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.attach_volume_input.AttachVolumeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.attach_volume_output.AttachVolumeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.attach_volume

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.attach_volume.attach_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.attach_volume_input.AttachVolumeInput = {
            "gateway_arn": gateway_arn,
            "volume_arn": volume_arn,
            "network_interface_id": network_interface_id,
        }
        if target_name is not None:
            input_["target_name"] = target_name
        if disk_id is not None:
            input_["disk_id"] = disk_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_archival(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.cancel_archival_output.CancelArchivalOutput":
        """<p>Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving process is initiated. This operation is only supported in the tape gateway type.</p>

        Args:
            tape_arn: <p>The Amazon Resource Name (ARN) of the virtual tape you want to cancel archiving for.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel virtual tape archiving
            Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving process is initiated.

            >>> client.cancel_archival(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', tape_arn='arn:aws:storagegateway:us-east-1:999999999999:tape/AMZN01A2A4')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.cancel_archival_input.CancelArchivalInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.cancel_archival_output.CancelArchivalOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.cancel_archival

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.cancel_archival.cancel_archival(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.cancel_archival_input.CancelArchivalInput = {
            "gateway_arn": gateway_arn,
            "tape_arn": tape_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_cache_report(
        self,
        cache_report_arn: "capo_storage_gateway.types.cache_report_arn.CacheReportARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> (
        "capo_storage_gateway.types.cancel_cache_report_output.CancelCacheReportOutput"
    ):
        """<p>Cancels generation of a specified cache report. You can use this operation to manually cancel an IN-PROGRESS report for any reason. This action changes the report status from IN-PROGRESS to CANCELLED. You can only cancel in-progress reports. If the the report you attempt to cancel is in FAILED, ERROR, or COMPLETED state, the cancel operation returns an error.</p>

        Args:
            cache_report_arn: <p>The Amazon Resource Name (ARN) of the cache report you want to cancel.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.cancel_cache_report_input.CancelCacheReportInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.cancel_cache_report_output.CancelCacheReportOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.cancel_cache_report

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.cancel_cache_report.cancel_cache_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.cancel_cache_report_input.CancelCacheReportInput = {
            "cache_report_arn": cache_report_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_retrieval(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.cancel_retrieval_output.CancelRetrievalOutput":
        """<p>Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated. The virtual tape is returned to the VTS. This operation is only supported in the tape gateway type.</p>

        Args:
            tape_arn: <p>The Amazon Resource Name (ARN) of the virtual tape you want to cancel retrieval for.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel virtual tape retrieval
            Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated.

            >>> client.cancel_retrieval(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', tape_arn='arn:aws:storagegateway:us-east-1:999999999999:tape/AMZN01A2A4')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.cancel_retrieval_input.CancelRetrievalInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.cancel_retrieval_output.CancelRetrievalOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.cancel_retrieval

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.cancel_retrieval.cancel_retrieval(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.cancel_retrieval_input.CancelRetrievalInput = {
            "gateway_arn": gateway_arn,
            "tape_arn": tape_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cachedi_scsi_volume(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        volume_size_in_bytes: "capo_storage_gateway.types.long.long",
        target_name: "capo_storage_gateway.types.target_name.TargetName",
        network_interface_id: "capo_storage_gateway.types.network_interface_id.NetworkInterfaceId",
        client_token: "capo_storage_gateway.types.client_token.ClientToken",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        snapshot_id: Optional[
            "capo_storage_gateway.types.snapshot_id.SnapshotId"
        ] = None,
        source_volume_arn: Optional[
            "capo_storage_gateway.types.volume_arn.VolumeARN"
        ] = None,
        kms_encrypted: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        kms_key: Optional["capo_storage_gateway.types.kms_key.KMSKey"] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.create_cachedi_scsi_volume_output.CreateCachediSCSIVolumeOutput":
        """<p>Creates a cached volume on a specified cached volume gateway. This operation is only supported in the cached volume gateway type.</p> <note> <p>Cache storage must be allocated to the gateway before you can create a cached volume. Use the <a>AddCache</a> operation to add cache storage to a gateway.</p> </note> <p>In the request, you must specify the gateway, size of the volume in bytes, the iSCSI target name, an IP address on which to expose the target, and a unique client token. In response, the gateway creates the volume and returns information about it. This information includes the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.</p> <p>Optionally, you can provide the ARN for an existing volume as the <code>SourceVolumeARN</code> for this cached volume, which creates an exact copy of the existing volume’s latest recovery point. The <code>VolumeSizeInBytes</code> value must be equal to or larger than the size of the copied volume, in bytes.</p>

        Args:
            volume_size_in_bytes: <p>The size of the volume in bytes.</p>
            snapshot_id: <p>The snapshot ID (e.g. "snap-1122aabb") of the snapshot to restore as the new cached volume. Specify this field if you want to create the iSCSI storage volume from a snapshot; otherwise, do not include this field. To list snapshots for your account use <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html">DescribeSnapshots</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p>
            target_name: <p>The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying <code>TargetName</code> as <i>myvolume</i> results in the target ARN of <code>arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume</code>. The target name must be unique across all volumes on a gateway.</p> <p>If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.</p>
            source_volume_arn: <p>The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The <code>VolumeSizeInBytes</code> value for this new volume must be equal to or larger than the size of the existing volume, in bytes.</p>
            network_interface_id: <p>The network interface of the gateway on which to expose the iSCSI target. Accepts IPv4 and IPv6 addresses. Use <a>DescribeGatewayInformation</a> to get a list of the network interfaces available on a gateway.</p> <p>Valid Values: A valid IP address.</p>
            client_token: <p>A unique identifier that you use to retry a request. If you retry a request, use the same <code>ClientToken</code> you specified in the initial request.</p>
            kms_encrypted: <p>Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key, or <code>false</code> to use a key managed by Amazon S3. Optional.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            kms_key: <p>The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when <code>KMSEncrypted</code> is <code>true</code>. Optional.</p>
            tags: <p>A list of up to 50 tags that you can assign to a cached volume. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers that you can represent in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256 characters.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a cached iSCSI volume
            Creates a cached volume on a specified cached gateway.

            >>> client.create_cachedi_scsi_volume(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', volume_size_in_bytes=536870912000, snapshot_id='snap-f47b7b94', target_name='my-volume', network_interface_id='10.1.1.1', client_token='cachedvol112233')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.create_cachedi_scsi_volume_input.CreateCachediSCSIVolumeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.create_cachedi_scsi_volume_output.CreateCachediSCSIVolumeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.create_cachedi_scsi_volume

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.create_cachedi_scsi_volume.create_cachedi_scsi_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.create_cachedi_scsi_volume_input.CreateCachediSCSIVolumeInput = {
            "gateway_arn": gateway_arn,
            "volume_size_in_bytes": volume_size_in_bytes,
            "target_name": target_name,
            "network_interface_id": network_interface_id,
            "client_token": client_token,
        }
        if snapshot_id is not None:
            input_["snapshot_id"] = snapshot_id
        if source_volume_arn is not None:
            input_["source_volume_arn"] = source_volume_arn
        if kms_encrypted is not None:
            input_["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_nfs_file_share(
        self,
        client_token: "capo_storage_gateway.types.client_token.ClientToken",
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        role: "capo_storage_gateway.types.role.Role",
        location_arn: "capo_storage_gateway.types.location_arn.LocationARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        nfs_file_share_defaults: Optional[
            "capo_storage_gateway.types.nfs_file_share_defaults.NFSFileShareDefaults"
        ] = None,
        encryption_type: Optional[
            "capo_storage_gateway.types.encryption_type.EncryptionType"
        ] = None,
        kms_encrypted: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        kms_key: Optional["capo_storage_gateway.types.kms_key.KMSKey"] = None,
        default_storage_class: Optional[
            "capo_storage_gateway.types.storage_class.StorageClass"
        ] = None,
        object_acl: Optional["capo_storage_gateway.types.object_acl.ObjectACL"] = None,
        client_list: Optional[
            "capo_storage_gateway.types.file_share_client_list.FileShareClientList"
        ] = None,
        squash: Optional["capo_storage_gateway.types.squash.Squash"] = None,
        read_only: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        guess_mime_type_enabled: Optional[
            "capo_storage_gateway.types.boolean.Boolean"
        ] = None,
        requester_pays: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
        file_share_name: Optional[
            "capo_storage_gateway.types.file_share_name.FileShareName"
        ] = None,
        cache_attributes: Optional[
            "capo_storage_gateway.types.cache_attributes.CacheAttributes"
        ] = None,
        notification_policy: Optional[
            "capo_storage_gateway.types.notification_policy.NotificationPolicy"
        ] = None,
        vpc_endpoint_dns_name: Optional[
            "capo_storage_gateway.types.dns_host_name.DNSHostName"
        ] = None,
        bucket_region: Optional["capo_storage_gateway.types.region_id.RegionId"] = None,
        audit_destination_arn: Optional[
            "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
        ] = None,
    ) -> "capo_storage_gateway.types.create_nfs_file_share_output.CreateNFSFileShareOutput":
        r"""<p>Creates a Network File System (NFS) file share on an existing S3 File Gateway. In Storage Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage. Storage Gateway exposes file shares using an NFS interface. This operation is only supported for S3 File Gateways.</p> <important> <p>S3 File gateway requires Security Token Service (Amazon Web Services STS) to be activated to enable you to create a file share. Make sure Amazon Web Services STS is activated in the Amazon Web Services Region you are creating your S3 File Gateway in. If Amazon Web Services STS is not activated in the Amazon Web Services Region, activate it. For information about how to activate Amazon Web Services STS, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html">Activating and deactivating Amazon Web Services STS in an Amazon Web Services Region</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>S3 File Gateways do not support creating hard or symbolic links on a file share.</p> </important>

        Args:
            client_token: <p>A unique string value that you supply that is used by S3 File Gateway to ensure idempotent file share creation.</p>
            nfs_file_share_defaults: <p>File share default values. Optional.</p>
            gateway_arn: <p>The Amazon Resource Name (ARN) of the S3 File Gateway on which you want to create a file share.</p>
            encryption_type: <p>A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note>
            kms_encrypted: <p>Optional. Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key (SSE-KMS), or <code>false</code> to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the <code>EncryptionType</code> parameter instead.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            kms_key: <p>Optional. The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value must be set if <code>KMSEncrypted</code> is <code>true</code>, or if <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>.</p>
            role: <p>The ARN of the Identity and Access Management (IAM) role that an S3 File Gateway assumes when it accesses the underlying storage.</p>
            location_arn: <p>A custom ARN for the backend storage used for storing data for file shares. It includes a resource ARN with an optional prefix concatenation. The prefix must end with a forward slash (/).</p> <note> <p>You can specify LocationARN as a bucket ARN, access point ARN or access point alias, as shown in the following examples.</p> <p>Bucket ARN:</p> <p> <code>arn:aws:s3:::amzn-s3-demo-bucket/prefix/</code> </p> <p>Access point ARN:</p> <p> <code>arn:aws:s3:region:account-id:accesspoint/access-point-name/prefix/</code> </p> <p>If you specify an access point, the bucket policy must be configured to delegate access control to the access point. For information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html#access-points-delegating-control">Delegating access control to access points</a> in the <i>Amazon S3 User Guide</i>.</p> <p>Access point alias:</p> <p> <code>test-ap-ab123cdef4gehijklmn5opqrstuvuse1a-s3alias</code> </p> </note>
            default_storage_class: <p>The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is <code>S3_STANDARD</code>. Optional.</p> <p>Valid Values: <code>S3_STANDARD</code> | <code>S3_INTELLIGENT_TIERING</code> | <code>S3_STANDARD_IA</code> | <code>S3_ONEZONE_IA</code> </p>
            object_acl: <p>A value that sets the access control list (ACL) permission for objects in the S3 bucket that a S3 File Gateway puts objects into. The default value is <code>private</code>.</p>
            client_list: <p>The list of clients that are allowed to access the S3 File Gateway. The list must contain either valid IPv4/IPv6 addresses or valid CIDR blocks.</p>
            squash: <p>A value that maps a user to anonymous user.</p> <p>Valid values are the following:</p> <ul> <li> <p> <code>RootSquash</code>: Only root is mapped to anonymous user.</p> </li> <li> <p> <code>NoSquash</code>: No one is mapped to anonymous user.</p> </li> <li> <p> <code>AllSquash</code>: Everyone is mapped to anonymous user.</p> </li> </ul>
            read_only: <p>A value that sets the write status of a file share. Set this value to <code>true</code> to set the write status to read-only, otherwise set to <code>false</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            guess_mime_type_enabled: <p>A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to <code>true</code> to enable MIME type guessing, otherwise set to <code>false</code>. The default value is <code>true</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            requester_pays: <p>A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to <code>true</code>, the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.</p> <note> <p> <code>RequesterPays</code> is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            tags: <p>A list of up to 50 tags that can be assigned to the NFS file share. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>
            file_share_name: <p>The name of the file share. Optional.</p> <note> <p> <code>FileShareName</code> must be set if an S3 prefix name is set in <code>LocationARN</code>, or if an access point or access point alias is used.</p> <p>A valid NFS file share name can only contain the following characters: <code>a</code>-<code>z</code>, <code>A</code>-<code>Z</code>, <code>0</code>-<code>9</code>, <code>-</code>, <code>.</code>, and <code>_</code>.</p> </note>
            cache_attributes: <p>Specifies refresh cache information for the file share.</p>
            notification_policy: <p>The notification policy of the file share. <code>SettlingTimeInSeconds</code> controls the number of seconds to wait after the last point in time a client wrote to a file before generating an <code>ObjectUploaded</code> notification. Because clients can make many small writes to files, it's best to set this parameter for as long as possible to avoid generating multiple notifications for the same file in a small time period.</p> <note> <p> <code>SettlingTimeInSeconds</code> has no effect on the timing of the object uploading to Amazon S3, only the timing of the notification.</p> <p>This setting is not meant to specify an exact time at which the notification will be sent. In some cases, the gateway might require more than the specified delay time to generate and send notifications.</p> </note> <p>The following example sets <code>NotificationPolicy</code> on with <code>SettlingTimeInSeconds</code> set to 60.</p> <p> <code>{\"Upload\": {\"SettlingTimeInSeconds\": 60}}</code> </p> <p>The following example sets <code>NotificationPolicy</code> off.</p> <p> <code>{}</code> </p>
            vpc_endpoint_dns_name: <p>Specifies the DNS name for the VPC endpoint that the NFS file share uses to connect to Amazon S3.</p> <note> <p>This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.</p> </note>
            bucket_region: <p>Specifies the Region of the S3 bucket where the NFS file share stores files.</p> <note> <p>This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.</p> </note>
            audit_destination_arn: <p>The Amazon Resource Name (ARN) of the storage used for audit logs.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.create_nfs_file_share_input.CreateNFSFileShareInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.create_nfs_file_share_output.CreateNFSFileShareOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.create_nfs_file_share

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.create_nfs_file_share.create_nfs_file_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.create_nfs_file_share_input.CreateNFSFileShareInput = {
            "client_token": client_token,
            "gateway_arn": gateway_arn,
            "role": role,
            "location_arn": location_arn,
        }
        if nfs_file_share_defaults is not None:
            input_["nfs_file_share_defaults"] = nfs_file_share_defaults
        if encryption_type is not None:
            input_["encryption_type"] = encryption_type
        if kms_encrypted is not None:
            input_["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if default_storage_class is not None:
            input_["default_storage_class"] = default_storage_class
        if object_acl is not None:
            input_["object_acl"] = object_acl
        if client_list is not None:
            input_["client_list"] = client_list
        if squash is not None:
            input_["squash"] = squash
        if read_only is not None:
            input_["read_only"] = read_only
        if guess_mime_type_enabled is not None:
            input_["guess_mime_type_enabled"] = guess_mime_type_enabled
        if requester_pays is not None:
            input_["requester_pays"] = requester_pays
        if tags is not None:
            input_["tags"] = tags
        if file_share_name is not None:
            input_["file_share_name"] = file_share_name
        if cache_attributes is not None:
            input_["cache_attributes"] = cache_attributes
        if notification_policy is not None:
            input_["notification_policy"] = notification_policy
        if vpc_endpoint_dns_name is not None:
            input_["vpc_endpoint_dns_name"] = vpc_endpoint_dns_name
        if bucket_region is not None:
            input_["bucket_region"] = bucket_region
        if audit_destination_arn is not None:
            input_["audit_destination_arn"] = audit_destination_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_smb_file_share(
        self,
        client_token: "capo_storage_gateway.types.client_token.ClientToken",
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        role: "capo_storage_gateway.types.role.Role",
        location_arn: "capo_storage_gateway.types.location_arn.LocationARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        encryption_type: Optional[
            "capo_storage_gateway.types.encryption_type.EncryptionType"
        ] = None,
        kms_encrypted: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        kms_key: Optional["capo_storage_gateway.types.kms_key.KMSKey"] = None,
        default_storage_class: Optional[
            "capo_storage_gateway.types.storage_class.StorageClass"
        ] = None,
        object_acl: Optional["capo_storage_gateway.types.object_acl.ObjectACL"] = None,
        read_only: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        guess_mime_type_enabled: Optional[
            "capo_storage_gateway.types.boolean.Boolean"
        ] = None,
        requester_pays: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        smbacl_enabled: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        access_based_enumeration: Optional[
            "capo_storage_gateway.types.boolean.Boolean"
        ] = None,
        admin_user_list: Optional[
            "capo_storage_gateway.types.user_list.UserList"
        ] = None,
        valid_user_list: Optional[
            "capo_storage_gateway.types.user_list.UserList"
        ] = None,
        invalid_user_list: Optional[
            "capo_storage_gateway.types.user_list.UserList"
        ] = None,
        audit_destination_arn: Optional[
            "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
        ] = None,
        authentication: Optional[
            "capo_storage_gateway.types.authentication.Authentication"
        ] = None,
        case_sensitivity: Optional[
            "capo_storage_gateway.types.case_sensitivity.CaseSensitivity"
        ] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
        file_share_name: Optional[
            "capo_storage_gateway.types.file_share_name.FileShareName"
        ] = None,
        cache_attributes: Optional[
            "capo_storage_gateway.types.cache_attributes.CacheAttributes"
        ] = None,
        notification_policy: Optional[
            "capo_storage_gateway.types.notification_policy.NotificationPolicy"
        ] = None,
        vpc_endpoint_dns_name: Optional[
            "capo_storage_gateway.types.dns_host_name.DNSHostName"
        ] = None,
        bucket_region: Optional["capo_storage_gateway.types.region_id.RegionId"] = None,
        oplocks_enabled: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
    ) -> "capo_storage_gateway.types.create_smb_file_share_output.CreateSMBFileShareOutput":
        r"""<p>Creates a Server Message Block (SMB) file share on an existing S3 File Gateway. In Storage Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage. Storage Gateway exposes file shares using an SMB interface. This operation is only supported for S3 File Gateways.</p> <important> <p>S3 File Gateways require Security Token Service (Amazon Web Services STS) to be activated to enable you to create a file share. Make sure that Amazon Web Services STS is activated in the Amazon Web Services Region you are creating your S3 File Gateway in. If Amazon Web Services STS is not activated in this Amazon Web Services Region, activate it. For information about how to activate Amazon Web Services STS, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html">Activating and deactivating Amazon Web Services STS in an Amazon Web Services Region</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>File gateways don't support creating hard or symbolic links on a file share.</p> </important>

        Args:
            client_token: <p>A unique string value that you supply that is used by S3 File Gateway to ensure idempotent file share creation.</p>
            gateway_arn: <p>The ARN of the S3 File Gateway on which you want to create a file share.</p>
            encryption_type: <p>A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note>
            kms_encrypted: <p>Optional. Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key (SSE-KMS), or <code>false</code> to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the <code>EncryptionType</code> parameter instead.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            kms_key: <p>Optional. The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value must be set if <code>KMSEncrypted</code> is <code>true</code>, or if <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>.</p>
            role: <p>The ARN of the Identity and Access Management (IAM) role that an S3 File Gateway assumes when it accesses the underlying storage.</p>
            location_arn: <p>A custom ARN for the backend storage used for storing data for file shares. It includes a resource ARN with an optional prefix concatenation. The prefix must end with a forward slash (/).</p> <note> <p>You can specify LocationARN as a bucket ARN, access point ARN or access point alias, as shown in the following examples.</p> <p>Bucket ARN:</p> <p> <code>arn:aws:s3:::amzn-s3-demo-bucket/prefix/</code> </p> <p>Access point ARN:</p> <p> <code>arn:aws:s3:region:account-id:accesspoint/access-point-name/prefix/</code> </p> <p>If you specify an access point, the bucket policy must be configured to delegate access control to the access point. For information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html#access-points-delegating-control">Delegating access control to access points</a> in the <i>Amazon S3 User Guide</i>.</p> <p>Access point alias:</p> <p> <code>test-ap-ab123cdef4gehijklmn5opqrstuvuse1a-s3alias</code> </p> </note>
            default_storage_class: <p>The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is <code>S3_STANDARD</code>. Optional.</p> <p>Valid Values: <code>S3_STANDARD</code> | <code>S3_INTELLIGENT_TIERING</code> | <code>S3_STANDARD_IA</code> | <code>S3_ONEZONE_IA</code> </p>
            object_acl: <p>A value that sets the access control list (ACL) permission for objects in the S3 bucket that a S3 File Gateway puts objects into. The default value is <code>private</code>.</p>
            read_only: <p>A value that sets the write status of a file share. Set this value to <code>true</code> to set the write status to read-only, otherwise set to <code>false</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            guess_mime_type_enabled: <p>A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to <code>true</code> to enable MIME type guessing, otherwise set to <code>false</code>. The default value is <code>true</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            requester_pays: <p>A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to <code>true</code>, the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.</p> <note> <p> <code>RequesterPays</code> is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            smbacl_enabled: <p>Set this value to <code>true</code> to enable access control list (ACL) on the SMB file share. Set it to <code>false</code> to map file and directory permissions to the POSIX permissions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/filegateway/latest/files3/smb-acl.html">Using Windows ACLs to limit SMB file share access</a> in the <i>Amazon S3 File Gateway User Guide</i>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            access_based_enumeration: <p>The files and folders on this share will only be visible to users with read access.</p>
            admin_user_list: <p>A list of users or groups in the Active Directory that will be granted administrator privileges on the file share. These users can do all file operations as the super-user. Acceptable formats include: <code>DOMAIN\User1</code>, <code>user1</code>, <code>@group1</code>, and <code>@DOMAIN\group1</code>.</p> <important> <p>Use this option very carefully, because any user in this list can do anything they like on the file share, regardless of file permissions.</p> </important>
            valid_user_list: <p>A list of users or groups in the Active Directory that are allowed to access the file <a href=""></a> share. A group must be prefixed with the @ character. Acceptable formats include: <code>DOMAIN\User1</code>, <code>user1</code>, <code>@group1</code>, and <code>@DOMAIN\group1</code>. Can only be set if Authentication is set to <code>ActiveDirectory</code>.</p>
            invalid_user_list: <p>A list of users or groups in the Active Directory that are not allowed to access the file share. A group must be prefixed with the @ character. Acceptable formats include: <code>DOMAIN\User1</code>, <code>user1</code>, <code>@group1</code>, and <code>@DOMAIN\group1</code>. Can only be set if Authentication is set to <code>ActiveDirectory</code>.</p>
            audit_destination_arn: <p>The Amazon Resource Name (ARN) of the storage used for audit logs.</p>
            authentication: <p>The authentication method that users use to access the file share. The default is <code>ActiveDirectory</code>.</p> <p>Valid Values: <code>ActiveDirectory</code> | <code>GuestAccess</code> </p>
            case_sensitivity: <p>The case of an object name in an Amazon S3 bucket. For <code>ClientSpecified</code>, the client determines the case sensitivity. For <code>CaseSensitive</code>, the gateway determines the case sensitivity. The default value is <code>ClientSpecified</code>.</p>
            tags: <p>A list of up to 50 tags that can be assigned to the NFS file share. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>
            file_share_name: <p>The name of the file share. Optional.</p> <note> <p> <code>FileShareName</code> must be set if an S3 prefix name is set in <code>LocationARN</code>, or if an access point or access point alias is used.</p> <p>A valid SMB file share name cannot contain the following characters: <code>[</code>,<code>]</code>,<code>#</code>,<code>;</code>,<code><</code>,<code>></code>,<code>:</code>,<code>"</code>,<code>\</code>,<code>/</code>,<code>|</code>,<code>?</code>,<code>*</code>,<code>+</code>, or ASCII control characters <code>1-31</code>.</p> </note>
            cache_attributes: <p>Specifies refresh cache information for the file share.</p>
            notification_policy: <p>The notification policy of the file share. <code>SettlingTimeInSeconds</code> controls the number of seconds to wait after the last point in time a client wrote to a file before generating an <code>ObjectUploaded</code> notification. Because clients can make many small writes to files, it's best to set this parameter for as long as possible to avoid generating multiple notifications for the same file in a small time period.</p> <note> <p> <code>SettlingTimeInSeconds</code> has no effect on the timing of the object uploading to Amazon S3, only the timing of the notification.</p> <p>This setting is not meant to specify an exact time at which the notification will be sent. In some cases, the gateway might require more than the specified delay time to generate and send notifications.</p> </note> <p>The following example sets <code>NotificationPolicy</code> on with <code>SettlingTimeInSeconds</code> set to 60.</p> <p> <code>{\"Upload\": {\"SettlingTimeInSeconds\": 60}}</code> </p> <p>The following example sets <code>NotificationPolicy</code> off.</p> <p> <code>{}</code> </p>
            vpc_endpoint_dns_name: <p>Specifies the DNS name for the VPC endpoint that the SMB file share uses to connect to Amazon S3.</p> <note> <p>This parameter is required for SMB file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.</p> </note>
            bucket_region: <p>Specifies the Region of the S3 bucket where the SMB file share stores files.</p> <note> <p>This parameter is required for SMB file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.</p> </note>
            oplocks_enabled: <p>Specifies whether opportunistic locking is enabled for the SMB file share.</p> <note> <p>Enabling opportunistic locking on case-sensitive shares is not recommended for workloads that involve access to files with the same name in different case.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.create_smb_file_share_input.CreateSMBFileShareInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.create_smb_file_share_output.CreateSMBFileShareOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.create_smb_file_share

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.create_smb_file_share.create_smb_file_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.create_smb_file_share_input.CreateSMBFileShareInput = {
            "client_token": client_token,
            "gateway_arn": gateway_arn,
            "role": role,
            "location_arn": location_arn,
        }
        if encryption_type is not None:
            input_["encryption_type"] = encryption_type
        if kms_encrypted is not None:
            input_["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if default_storage_class is not None:
            input_["default_storage_class"] = default_storage_class
        if object_acl is not None:
            input_["object_acl"] = object_acl
        if read_only is not None:
            input_["read_only"] = read_only
        if guess_mime_type_enabled is not None:
            input_["guess_mime_type_enabled"] = guess_mime_type_enabled
        if requester_pays is not None:
            input_["requester_pays"] = requester_pays
        if smbacl_enabled is not None:
            input_["smbacl_enabled"] = smbacl_enabled
        if access_based_enumeration is not None:
            input_["access_based_enumeration"] = access_based_enumeration
        if admin_user_list is not None:
            input_["admin_user_list"] = admin_user_list
        if valid_user_list is not None:
            input_["valid_user_list"] = valid_user_list
        if invalid_user_list is not None:
            input_["invalid_user_list"] = invalid_user_list
        if audit_destination_arn is not None:
            input_["audit_destination_arn"] = audit_destination_arn
        if authentication is not None:
            input_["authentication"] = authentication
        if case_sensitivity is not None:
            input_["case_sensitivity"] = case_sensitivity
        if tags is not None:
            input_["tags"] = tags
        if file_share_name is not None:
            input_["file_share_name"] = file_share_name
        if cache_attributes is not None:
            input_["cache_attributes"] = cache_attributes
        if notification_policy is not None:
            input_["notification_policy"] = notification_policy
        if vpc_endpoint_dns_name is not None:
            input_["vpc_endpoint_dns_name"] = vpc_endpoint_dns_name
        if bucket_region is not None:
            input_["bucket_region"] = bucket_region
        if oplocks_enabled is not None:
            input_["oplocks_enabled"] = oplocks_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_snapshot(
        self,
        volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN",
        snapshot_description: "capo_storage_gateway.types.snapshot_description.SnapshotDescription",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.create_snapshot_output.CreateSnapshotOutput":
        """<p>Initiates a snapshot of a volume.</p> <p>Storage Gateway provides the ability to back up point-in-time snapshots of your data to Amazon Simple Storage (Amazon S3) for durable off-site recovery, and also import the data to an Amazon Elastic Block Store (EBS) volume in Amazon Elastic Compute Cloud (EC2). You can take snapshots of your gateway volume on a scheduled or ad hoc basis. This API enables you to take an ad hoc snapshot. For more information, see <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#SchedulingSnapshot">Editing a snapshot schedule</a>.</p> <p>In the <code>CreateSnapshot</code> request, you identify the volume by providing its Amazon Resource Name (ARN). You must also provide description for the snapshot. When Storage Gateway takes the snapshot of specified volume, the snapshot and description appears in the Storage Gateway console. In response, Storage Gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot. This operation is only supported in stored and cached volume gateway type.</p> <note> <p>To list or delete a snapshot, you must use the Amazon EC2 API. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html">DescribeSnapshots</a> or <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html">DeleteSnapshot</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p> </note> <important> <p>Volume and snapshot IDs are changing to a longer length ID format. For more information, see the important note on the <a href="https://docs.aws.amazon.com/storagegateway/latest/APIReference/Welcome.html">Welcome</a> page.</p> </important>

        Args:
            volume_arn: <p>The Amazon Resource Name (ARN) of the volume. Use the <a>ListVolumes</a> operation to return a list of gateway volumes.</p>
            snapshot_description: <p>Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the <b>Description</b> field, and in the Storage Gateway snapshot <b>Details</b> pane, <b>Description</b> field.</p>
            tags: <p>A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.service_unavailable_error.ServiceUnavailableError: <p>An internal server error has occurred because the service is unavailable. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a snapshot of a gateway volume
            Initiates an ad-hoc snapshot of a gateway volume.

            >>> client.create_snapshot(volume_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB', snapshot_description='My root volume snapshot as of 10/03/2017')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.create_snapshot_input.CreateSnapshotInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.create_snapshot_output.CreateSnapshotOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.create_snapshot

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.create_snapshot.create_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.create_snapshot_input.CreateSnapshotInput = {
            "volume_arn": volume_arn,
            "snapshot_description": snapshot_description,
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

    def create_snapshot_from_volume_recovery_point(
        self,
        volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN",
        snapshot_description: "capo_storage_gateway.types.snapshot_description.SnapshotDescription",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.create_snapshot_from_volume_recovery_point_output.CreateSnapshotFromVolumeRecoveryPointOutput":
        """<p>Initiates a snapshot of a gateway from a volume recovery point. This operation is only supported in the cached volume gateway type.</p> <p>A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot. To get a list of volume recovery point for cached volume gateway, use <a>ListVolumeRecoveryPoints</a>.</p> <p>In the <code>CreateSnapshotFromVolumeRecoveryPoint</code> request, you identify the volume by providing its Amazon Resource Name (ARN). You must also provide a description for the snapshot. When the gateway takes a snapshot of the specified volume, the snapshot and its description appear in the Storage Gateway console. In response, the gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot.</p> <note> <p>To list or delete a snapshot, you must use the Amazon EC2 API. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html">DescribeSnapshots</a> or <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html">DeleteSnapshot</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p> </note>

        Args:
            volume_arn: <p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return to retrieve the TargetARN for specified VolumeARN.</p>
            snapshot_description: <p>Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the <b>Description</b> field, and in the Storage Gateway snapshot <b>Details</b> pane, <b>Description</b> field.</p>
            tags: <p>A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.service_unavailable_error.ServiceUnavailableError: <p>An internal server error has occurred because the service is unavailable. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a snapshot of a gateway volume
            Initiates a snapshot of a gateway from a volume recovery point.

            >>> client.create_snapshot_from_volume_recovery_point(volume_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB', snapshot_description='My root volume snapshot as of 2017-06-30T10:10:10.000Z')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.create_snapshot_from_volume_recovery_point_input.CreateSnapshotFromVolumeRecoveryPointInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.create_snapshot_from_volume_recovery_point_output.CreateSnapshotFromVolumeRecoveryPointOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.create_snapshot_from_volume_recovery_point

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.create_snapshot_from_volume_recovery_point.create_snapshot_from_volume_recovery_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.create_snapshot_from_volume_recovery_point_input.CreateSnapshotFromVolumeRecoveryPointInput = {
            "volume_arn": volume_arn,
            "snapshot_description": snapshot_description,
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

    def create_storedi_scsi_volume(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        disk_id: "capo_storage_gateway.types.disk_id.DiskId",
        preserve_existing_data: "capo_storage_gateway.types.boolean2.Boolean2",
        target_name: "capo_storage_gateway.types.target_name.TargetName",
        network_interface_id: "capo_storage_gateway.types.network_interface_id.NetworkInterfaceId",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        snapshot_id: Optional[
            "capo_storage_gateway.types.snapshot_id.SnapshotId"
        ] = None,
        kms_encrypted: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        kms_key: Optional["capo_storage_gateway.types.kms_key.KMSKey"] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.create_storedi_scsi_volume_output.CreateStorediSCSIVolumeOutput":
        """<p>Creates a volume on a specified gateway. This operation is only supported in the stored volume gateway type.</p> <p>The size of the volume to create is inferred from the disk size. You can choose to preserve existing data on the disk, create volume from an existing snapshot, or create an empty volume. If you choose to create an empty gateway volume, then any existing data on the disk is erased.</p> <p>In the request, you must specify the gateway and the disk information on which you are creating the volume. In response, the gateway creates the volume and returns volume information such as the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.</p>

        Args:
            disk_id: <p>The unique identifier for the gateway local disk that is configured as a stored volume. Use <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/API_ListLocalDisks.html">ListLocalDisks</a> to list disk IDs for a gateway.</p>
            snapshot_id: <p>The snapshot ID (e.g., "snap-1122aabb") of the snapshot to restore as the new stored volume. Specify this field if you want to create the iSCSI storage volume from a snapshot; otherwise, do not include this field. To list snapshots for your account use <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html">DescribeSnapshots</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p>
            preserve_existing_data: <p>Set to <code>true</code> if you want to preserve the data on the local disk. Otherwise, set to <code>false</code> to create an empty volume.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            target_name: <p>The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying <code>TargetName</code> as <i>myvolume</i> results in the target ARN of <code>arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume</code>. The target name must be unique across all volumes on a gateway.</p> <p>If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.</p>
            network_interface_id: <p>The network interface of the gateway on which to expose the iSCSI target. Accepts IPv4 and IPv6 addresses. Use <a>DescribeGatewayInformation</a> to get a list of the network interfaces available on a gateway.</p> <p>Valid Values: A valid IP address.</p>
            kms_encrypted: <p>Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key, or <code>false</code> to use a key managed by Amazon S3. Optional.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            kms_key: <p>The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when <code>KMSEncrypted</code> is <code>true</code>. Optional.</p>
            tags: <p>A list of up to 50 tags that can be assigned to a stored volume. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a stored iSCSI volume
            Creates a stored volume on a specified stored gateway.

            >>> client.create_storedi_scsi_volume(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', disk_id='pci-0000:03:00.0-scsi-0:0:0:0', snapshot_id='snap-f47b7b94', preserve_existing_data=True, target_name='my-volume', network_interface_id='10.1.1.1')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.create_storedi_scsi_volume_input.CreateStorediSCSIVolumeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.create_storedi_scsi_volume_output.CreateStorediSCSIVolumeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.create_storedi_scsi_volume

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.create_storedi_scsi_volume.create_storedi_scsi_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.create_storedi_scsi_volume_input.CreateStorediSCSIVolumeInput = {
            "gateway_arn": gateway_arn,
            "disk_id": disk_id,
            "preserve_existing_data": preserve_existing_data,
            "target_name": target_name,
            "network_interface_id": network_interface_id,
        }
        if snapshot_id is not None:
            input_["snapshot_id"] = snapshot_id
        if kms_encrypted is not None:
            input_["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_tape_pool(
        self,
        pool_name: "capo_storage_gateway.types.pool_name.PoolName",
        storage_class: "capo_storage_gateway.types.tape_storage_class.TapeStorageClass",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        retention_lock_type: Optional[
            "capo_storage_gateway.types.retention_lock_type.RetentionLockType"
        ] = None,
        retention_lock_time_in_days: Optional[
            "capo_storage_gateway.types.retention_lock_time_in_days.RetentionLockTimeInDays"
        ] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.create_tape_pool_output.CreateTapePoolOutput":
        """<p>Creates a new custom tape pool. You can use custom tape pool to enable tape retention lock on tapes that are archived in the custom pool.</p>

        Args:
            pool_name: <p>The name of the new custom tape pool.</p>
            storage_class: <p>The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>
            retention_lock_type: <p>Tape retention lock can be configured in two modes. When configured in governance mode, Amazon Web Services accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root Amazon Web Services account.</p>
            retention_lock_time_in_days: <p>Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days).</p>
            tags: <p>A list of up to 50 tags that can be assigned to tape pool. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.create_tape_pool_input.CreateTapePoolInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.create_tape_pool_output.CreateTapePoolOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.create_tape_pool

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.create_tape_pool.create_tape_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.create_tape_pool_input.CreateTapePoolInput = {
            "pool_name": pool_name,
            "storage_class": storage_class,
        }
        if retention_lock_type is not None:
            input_["retention_lock_type"] = retention_lock_type
        if retention_lock_time_in_days is not None:
            input_["retention_lock_time_in_days"] = retention_lock_time_in_days
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_tapes(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        tape_size_in_bytes: "capo_storage_gateway.types.tape_size.TapeSize",
        client_token: "capo_storage_gateway.types.client_token.ClientToken",
        num_tapes_to_create: "capo_storage_gateway.types.num_tapes_to_create.NumTapesToCreate",
        tape_barcode_prefix: "capo_storage_gateway.types.tape_barcode_prefix.TapeBarcodePrefix",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        kms_encrypted: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        kms_key: Optional["capo_storage_gateway.types.kms_key.KMSKey"] = None,
        pool_id: Optional["capo_storage_gateway.types.pool_id.PoolId"] = None,
        worm: Optional["capo_storage_gateway.types.boolean2.Boolean2"] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.create_tapes_output.CreateTapesOutput":
        """<p>Creates one or more virtual tapes. You write data to the virtual tapes and then archive the tapes. This operation is only supported in the tape gateway type.</p> <note> <p>Cache storage must be allocated to the gateway before you can create virtual tapes. Use the <a>AddCache</a> operation to add cache storage to a gateway.</p> </note>

        Args:
            gateway_arn: <p>The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tapes with. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            tape_size_in_bytes: <p>The size, in bytes, of the virtual tapes that you want to create.</p> <note> <p>The size must be aligned by gigabyte (1024*1024*1024 bytes).</p> </note>
            client_token: <p>A unique identifier that you use to retry a request. If you retry a request, use the same <code>ClientToken</code> you specified in the initial request.</p> <note> <p>Using the same <code>ClientToken</code> prevents creating the tape multiple times.</p> </note>
            num_tapes_to_create: <p>The number of virtual tapes that you want to create.</p>
            tape_barcode_prefix: <p>A prefix that you append to the barcode of the virtual tape you are creating. This prefix makes the barcode unique.</p> <note> <p>The prefix must be 1-4 characters in length and must be one of the uppercase letters from A to Z.</p> </note>
            kms_encrypted: <p>Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key, or <code>false</code> to use a key managed by Amazon S3. Optional.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            kms_key: <p>The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when <code>KMSEncrypted</code> is <code>true</code>. Optional.</p>
            pool_id: <p>The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>
            worm: <p>Set to <code>TRUE</code> if the tape you are creating is to be configured as a write-once-read-many (WORM) tape.</p>
            tags: <p>A list of up to 50 tags that can be assigned to a virtual tape. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a virtual tape
            Creates one or more virtual tapes.

            >>> client.create_tapes(gateway_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B', tape_size_in_bytes=107374182400, client_token='77777', num_tapes_to_create=3, tape_barcode_prefix='TEST')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.create_tapes_input.CreateTapesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.create_tapes_output.CreateTapesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.create_tapes

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.create_tapes.create_tapes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.create_tapes_input.CreateTapesInput = {
            "gateway_arn": gateway_arn,
            "tape_size_in_bytes": tape_size_in_bytes,
            "client_token": client_token,
            "num_tapes_to_create": num_tapes_to_create,
            "tape_barcode_prefix": tape_barcode_prefix,
        }
        if kms_encrypted is not None:
            input_["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if pool_id is not None:
            input_["pool_id"] = pool_id
        if worm is not None:
            input_["worm"] = worm
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_tape_with_barcode(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        tape_size_in_bytes: "capo_storage_gateway.types.tape_size.TapeSize",
        tape_barcode: "capo_storage_gateway.types.tape_barcode.TapeBarcode",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        kms_encrypted: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        kms_key: Optional["capo_storage_gateway.types.kms_key.KMSKey"] = None,
        pool_id: Optional["capo_storage_gateway.types.pool_id.PoolId"] = None,
        worm: Optional["capo_storage_gateway.types.boolean2.Boolean2"] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.create_tape_with_barcode_output.CreateTapeWithBarcodeOutput":
        """<p>Creates a virtual tape by using your own barcode. You write data to the virtual tape and then archive the tape. A barcode is unique and cannot be reused if it has already been used on a tape. This applies to barcodes used on deleted tapes. This operation is only supported in the tape gateway type.</p> <note> <p>Cache storage must be allocated to the gateway before you can create a virtual tape. Use the <a>AddCache</a> operation to add cache storage to a gateway.</p> </note>

        Args:
            gateway_arn: <p>The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tape with. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            tape_size_in_bytes: <p>The size, in bytes, of the virtual tape that you want to create.</p> <note> <p>The size must be aligned by gigabyte (1024*1024*1024 bytes).</p> </note>
            tape_barcode: <p>The barcode that you want to assign to the tape.</p> <note> <p>Barcodes cannot be reused. This includes barcodes used for tapes that have been deleted.</p> </note>
            kms_encrypted: <p>Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key, or <code>false</code> to use a key managed by Amazon S3. Optional.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            kms_key: <p>The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when <code>KMSEncrypted</code> is <code>true</code>. Optional.</p>
            pool_id: <p>The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Deep Archive) that corresponds to the pool.</p>
            worm: <p>Set to <code>TRUE</code> if the tape you are creating is to be configured as a write-once-read-many (WORM) tape.</p>
            tags: <p>A list of up to 50 tags that can be assigned to a virtual tape that has a barcode. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a virtual tape using a barcode
            Creates a virtual tape by using your own barcode.

            >>> client.create_tape_with_barcode(gateway_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B', tape_size_in_bytes=107374182400, tape_barcode='TEST12345')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.create_tape_with_barcode_input.CreateTapeWithBarcodeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.create_tape_with_barcode_output.CreateTapeWithBarcodeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.create_tape_with_barcode

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.create_tape_with_barcode.create_tape_with_barcode(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.create_tape_with_barcode_input.CreateTapeWithBarcodeInput = {
            "gateway_arn": gateway_arn,
            "tape_size_in_bytes": tape_size_in_bytes,
            "tape_barcode": tape_barcode,
        }
        if kms_encrypted is not None:
            input_["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if pool_id is not None:
            input_["pool_id"] = pool_id
        if worm is not None:
            input_["worm"] = worm
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_automatic_tape_creation_policy(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.delete_automatic_tape_creation_policy_output.DeleteAutomaticTapeCreationPolicyOutput":
        """<p>Deletes the automatic tape creation policy of a gateway. If you delete this policy, new virtual tapes must be created manually. Use the Amazon Resource Name (ARN) of the gateway in your request to remove the policy.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_automatic_tape_creation_policy_input.DeleteAutomaticTapeCreationPolicyInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_automatic_tape_creation_policy_output.DeleteAutomaticTapeCreationPolicyOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_automatic_tape_creation_policy

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_automatic_tape_creation_policy.delete_automatic_tape_creation_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_automatic_tape_creation_policy_input.DeleteAutomaticTapeCreationPolicyInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_bandwidth_rate_limit(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        bandwidth_type: "capo_storage_gateway.types.bandwidth_type.BandwidthType",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.delete_bandwidth_rate_limit_output.DeleteBandwidthRateLimitOutput":
        """<p>Deletes the bandwidth rate limits of a gateway. You can delete either the upload and download bandwidth rate limit, or you can delete both. If you delete only one of the limits, the other limit remains unchanged. To specify which gateway to work with, use the Amazon Resource Name (ARN) of the gateway in your request. This operation is supported only for the stored volume, cached volume, and tape gateway types.</p>

        Args:
            bandwidth_type: <p>One of the BandwidthType values that indicates the gateway bandwidth rate limit to delete.</p> <p>Valid Values: <code>UPLOAD</code> | <code>DOWNLOAD</code> | <code>ALL</code> </p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete bandwidth rate limits of gateway
            Deletes the bandwidth rate limits of a gateway; either the upload or download limit, or both.

            >>> client.delete_bandwidth_rate_limit(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', bandwidth_type='All')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_bandwidth_rate_limit_input.DeleteBandwidthRateLimitInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_bandwidth_rate_limit_output.DeleteBandwidthRateLimitOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_bandwidth_rate_limit

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_bandwidth_rate_limit.delete_bandwidth_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_bandwidth_rate_limit_input.DeleteBandwidthRateLimitInput = {
            "gateway_arn": gateway_arn,
            "bandwidth_type": bandwidth_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cache_report(
        self,
        cache_report_arn: "capo_storage_gateway.types.cache_report_arn.CacheReportARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> (
        "capo_storage_gateway.types.delete_cache_report_output.DeleteCacheReportOutput"
    ):
        """<p>Deletes the specified cache report and any associated tags from the Storage Gateway database. You can only delete completed reports. If the status of the report you attempt to delete still IN-PROGRESS, the delete operation returns an error. You can use <code>CancelCacheReport</code> to cancel an IN-PROGRESS report.</p> <note> <p> <code>DeleteCacheReport</code> does not delete the report object from your Amazon S3 bucket.</p> </note>

        Args:
            cache_report_arn: <p>The Amazon Resource Name (ARN) of the cache report you want to delete.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_cache_report_input.DeleteCacheReportInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_cache_report_output.DeleteCacheReportOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_cache_report

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_cache_report.delete_cache_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_cache_report_input.DeleteCacheReportInput = {
            "cache_report_arn": cache_report_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_chap_credentials(
        self,
        target_arn: "capo_storage_gateway.types.target_arn.TargetARN",
        initiator_name: "capo_storage_gateway.types.iqn_name.IqnName",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.delete_chap_credentials_output.DeleteChapCredentialsOutput":
        """<p>Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair. This operation is supported in volume and tape gateway types.</p>

        Args:
            target_arn: <p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return to retrieve the TargetARN for specified VolumeARN.</p>
            initiator_name: <p>The iSCSI initiator that connects to the target.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete CHAP credentials
            Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair.

            >>> client.delete_chap_credentials(target_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume', initiator_name='iqn.1991-05.com.microsoft:computername.domain.example.com')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_chap_credentials_input.DeleteChapCredentialsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_chap_credentials_output.DeleteChapCredentialsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_chap_credentials

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_chap_credentials.delete_chap_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_chap_credentials_input.DeleteChapCredentialsInput = {
            "target_arn": target_arn,
            "initiator_name": initiator_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_file_share(
        self,
        file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        force_delete: Optional["capo_storage_gateway.types.boolean2.Boolean2"] = None,
    ) -> "capo_storage_gateway.types.delete_file_share_output.DeleteFileShareOutput":
        """<p>Deletes a file share from an S3 File Gateway. This operation is only supported for S3 File Gateways.</p>

        Args:
            file_share_arn: <p>The Amazon Resource Name (ARN) of the file share to be deleted.</p>
            force_delete: <p>If this value is set to <code>true</code>, the operation deletes a file share immediately and aborts all data uploads to Amazon Web Services. Otherwise, the file share is not deleted until all data is uploaded to Amazon Web Services. This process aborts the data upload process, and the file share enters the <code>FORCE_DELETING</code> status.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_file_share_input.DeleteFileShareInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_file_share_output.DeleteFileShareOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_file_share

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_file_share.delete_file_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_file_share_input.DeleteFileShareInput = {
            "file_share_arn": file_share_arn
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.delete_gateway_output.DeleteGatewayOutput":
        """<p>Deletes a gateway. To specify which gateway to delete, use the Amazon Resource Name (ARN) of the gateway in your request. The operation deletes the gateway; however, it does not delete the gateway virtual machine (VM) from your host computer.</p> <p>After you delete a gateway, you cannot reactivate it. Completed snapshots of the gateway volumes are not deleted upon deleting the gateway, however, pending snapshots will not complete. After you delete a gateway, your next step is to remove it from your environment.</p> <important> <p>You no longer pay software charges after the gateway is deleted; however, your existing Amazon EBS snapshots persist and you will continue to be billed for these snapshots. You can choose to remove all remaining Amazon EBS snapshots by canceling your Amazon EC2 subscription. If you prefer not to cancel your Amazon EC2 subscription, you can delete your snapshots using the Amazon EC2 console. For more information, see the <a href="http://aws.amazon.com/storagegateway">Storage Gateway detail page</a>.</p> </important>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a gatgeway
            This operation deletes the gateway, but not the gateway's VM from the host computer.

            >>> client.delete_gateway(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_gateway_input.DeleteGatewayInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_gateway_output.DeleteGatewayOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_gateway

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_gateway_input.DeleteGatewayInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_snapshot_schedule(
        self,
        volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.delete_snapshot_schedule_output.DeleteSnapshotScheduleOutput":
        """<p>Deletes a snapshot of a volume.</p> <p>You can take snapshots of your gateway volumes on a scheduled or ad hoc basis. This API action enables you to delete a snapshot schedule for a volume. For more information, see <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/backing-up-volumes.html">Backing up your volumes</a>. In the <code>DeleteSnapshotSchedule</code> request, you identify the volume by providing its Amazon Resource Name (ARN). This operation is only supported for cached volume gateway types.</p> <note> <p>To list or delete a snapshot, you must use the Amazon EC2 API. For more information, go to <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html">DescribeSnapshots</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p> </note>

        Args:
            volume_arn: <p>The volume which snapshot schedule to delete.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a snapshot of a volume
            This action enables you to delete a snapshot schedule for a volume.

            >>> client.delete_snapshot_schedule(volume_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_snapshot_schedule_input.DeleteSnapshotScheduleInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_snapshot_schedule_output.DeleteSnapshotScheduleOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_snapshot_schedule

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_snapshot_schedule.delete_snapshot_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_snapshot_schedule_input.DeleteSnapshotScheduleInput = {
            "volume_arn": volume_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_tape(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        bypass_governance_retention: Optional[
            "capo_storage_gateway.types.boolean2.Boolean2"
        ] = None,
    ) -> "capo_storage_gateway.types.delete_tape_output.DeleteTapeOutput":
        """<p>Deletes the specified virtual tape. This operation is only supported in the tape gateway type.</p>

        Args:
            gateway_arn: <p>The unique Amazon Resource Name (ARN) of the gateway that the virtual tape to delete is associated with. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            tape_arn: <p>The Amazon Resource Name (ARN) of the virtual tape to delete.</p>
            bypass_governance_retention: <p>Set to <code>TRUE</code> to delete an archived tape that belongs to a custom pool with tape retention lock. Only archived tapes with tape retention lock set to <code>governance</code> can be deleted. Archived tapes with tape retention lock set to <code>compliance</code> can't be deleted.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a virtual tape
            This example deletes the specified virtual tape.

            >>> client.delete_tape(gateway_arn='arn:aws:storagegateway:us-east-1:204469490176:gateway/sgw-12A3456B', tape_arn='arn:aws:storagegateway:us-east-1:204469490176:tape/TEST05A2A0')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_tape_input.DeleteTapeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_tape_output.DeleteTapeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_tape

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_tape.delete_tape(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_tape_input.DeleteTapeInput = {
            "gateway_arn": gateway_arn,
            "tape_arn": tape_arn,
        }
        if bypass_governance_retention is not None:
            input_["bypass_governance_retention"] = bypass_governance_retention

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_tape_archive(
        self,
        tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        bypass_governance_retention: Optional[
            "capo_storage_gateway.types.boolean2.Boolean2"
        ] = None,
    ) -> (
        "capo_storage_gateway.types.delete_tape_archive_output.DeleteTapeArchiveOutput"
    ):
        """<p>Deletes the specified virtual tape from the virtual tape shelf (VTS). This operation is only supported in the tape gateway type.</p>

        Args:
            tape_arn: <p>The Amazon Resource Name (ARN) of the virtual tape to delete from the virtual tape shelf (VTS).</p>
            bypass_governance_retention: <p>Set to <code>TRUE</code> to delete an archived tape that belongs to a custom pool with tape retention lock. Only archived tapes with tape retention lock set to <code>governance</code> can be deleted. Archived tapes with tape retention lock set to <code>compliance</code> can't be deleted.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a virtual tape from the shelf (VTS)
            Deletes the specified virtual tape from the virtual tape shelf (VTS).

            >>> client.delete_tape_archive(tape_arn='arn:aws:storagegateway:us-east-1:204469490176:tape/TEST05A2A0')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_tape_archive_input.DeleteTapeArchiveInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_tape_archive_output.DeleteTapeArchiveOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_tape_archive

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_tape_archive.delete_tape_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_tape_archive_input.DeleteTapeArchiveInput = {
            "tape_arn": tape_arn
        }
        if bypass_governance_retention is not None:
            input_["bypass_governance_retention"] = bypass_governance_retention

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_tape_pool(
        self,
        pool_arn: "capo_storage_gateway.types.pool_arn.PoolARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.delete_tape_pool_output.DeleteTapePoolOutput":
        """<p>Delete a custom tape pool. A custom tape pool can only be deleted if there are no tapes in the pool and if there are no automatic tape creation policies that reference the custom tape pool.</p>

        Args:
            pool_arn: <p>The Amazon Resource Name (ARN) of the custom tape pool to delete.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_tape_pool_input.DeleteTapePoolInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_tape_pool_output.DeleteTapePoolOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_tape_pool

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_tape_pool.delete_tape_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_tape_pool_input.DeleteTapePoolInput = {
            "pool_arn": pool_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_volume(
        self,
        volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.delete_volume_output.DeleteVolumeOutput":
        """<p>Deletes the specified storage volume that you previously created using the <a>CreateCachediSCSIVolume</a> or <a>CreateStorediSCSIVolume</a> API. This operation is only supported in the cached volume and stored volume types. For stored volume gateways, the local disk that was configured as the storage volume is not deleted. You can reuse the local disk to create another storage volume.</p> <p>Before you delete a volume, make sure there are no iSCSI connections to the volume you are deleting. You should also make sure there is no snapshot in progress. You can use the Amazon Elastic Compute Cloud (Amazon EC2) API to query snapshots on the volume you are deleting and check the snapshot status. For more information, go to <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html">DescribeSnapshots</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p> <p>In the request, you must provide the Amazon Resource Name (ARN) of the storage volume you want to delete.</p>

        Args:
            volume_arn: <p>The Amazon Resource Name (ARN) of the volume. Use the <a>ListVolumes</a> operation to return a list of gateway volumes.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a gateway volume
            Deletes the specified gateway volume that you previously created using the CreateCachediSCSIVolume or CreateStorediSCSIVolume API.

            >>> client.delete_volume(volume_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.delete_volume_input.DeleteVolumeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.delete_volume_output.DeleteVolumeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.delete_volume

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.delete_volume.delete_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.delete_volume_input.DeleteVolumeInput = {
            "volume_arn": volume_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_availability_monitor_test(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_availability_monitor_test_output.DescribeAvailabilityMonitorTestOutput":
        """<p>Returns information about the most recent high availability monitoring test that was performed on the host in a cluster. If a test isn't performed, the status and start time in the response would be null.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_availability_monitor_test_input.DescribeAvailabilityMonitorTestInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_availability_monitor_test_output.DescribeAvailabilityMonitorTestOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_availability_monitor_test

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_availability_monitor_test.describe_availability_monitor_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_availability_monitor_test_input.DescribeAvailabilityMonitorTestInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_bandwidth_rate_limit(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_bandwidth_rate_limit_output.DescribeBandwidthRateLimitOutput":
        """<p>Returns the bandwidth rate limits of a gateway. By default, these limits are not set, which means no bandwidth rate limiting is in effect. This operation is supported only for the stored volume, cached volume, and tape gateway types. To describe bandwidth rate limits for S3 file gateways, use <a>DescribeBandwidthRateLimitSchedule</a>.</p> <p>This operation returns a value for a bandwidth rate limit only if the limit is set. If no limits are set for the gateway, then this operation returns only the gateway ARN in the response body. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the bandwidth rate limits of a gateway
            Returns a value for a bandwidth rate limit if set. If not set, then only the gateway ARN is returned.

            >>> client.describe_bandwidth_rate_limit(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_bandwidth_rate_limit_input.DescribeBandwidthRateLimitInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_bandwidth_rate_limit_output.DescribeBandwidthRateLimitOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_bandwidth_rate_limit

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_bandwidth_rate_limit.describe_bandwidth_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_bandwidth_rate_limit_input.DescribeBandwidthRateLimitInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_bandwidth_rate_limit_schedule(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_bandwidth_rate_limit_schedule_output.DescribeBandwidthRateLimitScheduleOutput":
        """<p> Returns information about the bandwidth rate limit schedule of a gateway. By default, gateways do not have bandwidth rate limit schedules, which means no bandwidth rate limiting is in effect. This operation is supported only for volume, tape and S3 file gateways. FSx file gateways do not support bandwidth rate limits.</p> <p>This operation returns information about a gateway's bandwidth rate limit schedule. A bandwidth rate limit schedule consists of one or more bandwidth rate limit intervals. A bandwidth rate limit interval defines a period of time on one or more days of the week, during which bandwidth rate limits are specified for uploading, downloading, or both. </p> <p> A bandwidth rate limit interval consists of one or more days of the week, a start hour and minute, an ending hour and minute, and bandwidth rate limits for uploading and downloading </p> <p> If no bandwidth rate limit schedule intervals are set for the gateway, this operation returns an empty response. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_bandwidth_rate_limit_schedule_input.DescribeBandwidthRateLimitScheduleInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_bandwidth_rate_limit_schedule_output.DescribeBandwidthRateLimitScheduleOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_bandwidth_rate_limit_schedule

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_bandwidth_rate_limit_schedule.describe_bandwidth_rate_limit_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_bandwidth_rate_limit_schedule_input.DescribeBandwidthRateLimitScheduleInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cache(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_cache_output.DescribeCacheOutput":
        """<p>Returns information about the cache of a gateway. This operation is only supported in the cached volume, tape, and file gateway types.</p> <p>The response includes disk IDs that are configured as cache, and it includes the amount of cache allocated and used.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe cache information
            Returns information about the cache of a gateway.

            >>> client.describe_cache(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_cache_input.DescribeCacheInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_cache_output.DescribeCacheOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_cache

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_cache.describe_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_cache_input.DescribeCacheInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cachedi_scsi_volumes(
        self,
        volume_ar_ns: "capo_storage_gateway.types.volume_ar_ns.VolumeARNs",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_cachedi_scsi_volumes_output.DescribeCachediSCSIVolumesOutput":
        """<p>Returns a description of the gateway volumes specified in the request. This operation is only supported in the cached volume gateway types.</p> <p>The list of gateway volumes in the request must be from one gateway. In the response, Storage Gateway returns volume information sorted by volume Amazon Resource Name (ARN).</p>

        Args:
            volume_ar_ns: <p>An array of strings where each string represents the Amazon Resource Name (ARN) of a cached volume. All of the specified cached volumes must be from the same gateway. Use <a>ListVolumes</a> to get volume ARNs for a gateway.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe gateway cached iSCSI volumes
            Returns a description of the gateway cached iSCSI volumes specified in the request.

            >>> client.describe_cachedi_scsi_volumes(volume_ar_ns=['arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB'])
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_cachedi_scsi_volumes_input.DescribeCachediSCSIVolumesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_cachedi_scsi_volumes_output.DescribeCachediSCSIVolumesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_cachedi_scsi_volumes

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_cachedi_scsi_volumes.describe_cachedi_scsi_volumes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_cachedi_scsi_volumes_input.DescribeCachediSCSIVolumesInput = {
            "volume_ar_ns": volume_ar_ns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cache_report(
        self,
        cache_report_arn: "capo_storage_gateway.types.cache_report_arn.CacheReportARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_cache_report_output.DescribeCacheReportOutput":
        """<p>Returns information about the specified cache report, including completion status and generation progress.</p>

        Args:
            cache_report_arn: <p>The Amazon Resource Name (ARN) of the cache report you want to describe.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_cache_report_input.DescribeCacheReportInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_cache_report_output.DescribeCacheReportOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_cache_report

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_cache_report.describe_cache_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_cache_report_input.DescribeCacheReportInput = {
            "cache_report_arn": cache_report_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_chap_credentials(
        self,
        target_arn: "capo_storage_gateway.types.target_arn.TargetARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_chap_credentials_output.DescribeChapCredentialsOutput":
        """<p>Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair. This operation is supported in the volume and tape gateway types.</p>

        Args:
            target_arn: <p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return to retrieve the TargetARN for specified VolumeARN.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe CHAP credetnitals for an iSCSI
            Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair.

            >>> client.describe_chap_credentials(target_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_chap_credentials_input.DescribeChapCredentialsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_chap_credentials_output.DescribeChapCredentialsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_chap_credentials

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_chap_credentials.describe_chap_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_chap_credentials_input.DescribeChapCredentialsInput = {
            "target_arn": target_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_file_system_associations(
        self,
        file_system_association_arn_list: "capo_storage_gateway.types.file_system_association_arn_list.FileSystemAssociationARNList",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_file_system_associations_output.DescribeFileSystemAssociationsOutput":
        """<p>Gets the file system association information. This operation is only supported for FSx File Gateways.</p>

        Args:
            file_system_association_arn_list: <p>An array containing the Amazon Resource Name (ARN) of each file system association to be described.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_file_system_associations_input.DescribeFileSystemAssociationsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_file_system_associations_output.DescribeFileSystemAssociationsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_file_system_associations

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_file_system_associations.describe_file_system_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_file_system_associations_input.DescribeFileSystemAssociationsInput = {
            "file_system_association_arn_list": file_system_association_arn_list
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_gateway_information(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_gateway_information_output.DescribeGatewayInformationOutput":
        """<p>Returns metadata about a gateway such as its name, network interfaces, time zone, status, and software version. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe metadata about the gateway
            Returns metadata about a gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not).

            >>> client.describe_gateway_information(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_gateway_information_input.DescribeGatewayInformationInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_gateway_information_output.DescribeGatewayInformationOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_gateway_information

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_gateway_information.describe_gateway_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_gateway_information_input.DescribeGatewayInformationInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_maintenance_start_time(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_maintenance_start_time_output.DescribeMaintenanceStartTimeOutput":
        """<p>Returns your gateway's maintenance window schedule information, with values for monthly or weekly cadence, specific day and time to begin maintenance, and which types of updates to apply. Time values returned are for the gateway's time zone.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe gateway's maintenance start time
            Returns your gateway's weekly maintenance start time including the day and time of the week.

            >>> client.describe_maintenance_start_time(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_maintenance_start_time_input.DescribeMaintenanceStartTimeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_maintenance_start_time_output.DescribeMaintenanceStartTimeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_maintenance_start_time

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_maintenance_start_time.describe_maintenance_start_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_maintenance_start_time_input.DescribeMaintenanceStartTimeInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_nfs_file_shares(
        self,
        file_share_arn_list: "capo_storage_gateway.types.file_share_arn_list.FileShareARNList",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_nfs_file_shares_output.DescribeNFSFileSharesOutput":
        """<p>Gets a description for one or more Network File System (NFS) file shares from an S3 File Gateway. This operation is only supported for S3 File Gateways.</p>

        Args:
            file_share_arn_list: <p>An array containing the Amazon Resource Name (ARN) of each file share to be described.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_nfs_file_shares_input.DescribeNFSFileSharesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_nfs_file_shares_output.DescribeNFSFileSharesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_nfs_file_shares

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_nfs_file_shares.describe_nfs_file_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_nfs_file_shares_input.DescribeNFSFileSharesInput = {
            "file_share_arn_list": file_share_arn_list
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_smb_file_shares(
        self,
        file_share_arn_list: "capo_storage_gateway.types.file_share_arn_list.FileShareARNList",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_smb_file_shares_output.DescribeSMBFileSharesOutput":
        """<p>Gets a description for one or more Server Message Block (SMB) file shares from a S3 File Gateway. This operation is only supported for S3 File Gateways.</p>

        Args:
            file_share_arn_list: <p>An array containing the Amazon Resource Name (ARN) of each file share to be described.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_smb_file_shares_input.DescribeSMBFileSharesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_smb_file_shares_output.DescribeSMBFileSharesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_smb_file_shares

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_smb_file_shares.describe_smb_file_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_smb_file_shares_input.DescribeSMBFileSharesInput = {
            "file_share_arn_list": file_share_arn_list
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_smb_settings(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_smb_settings_output.DescribeSMBSettingsOutput":
        """<p>Gets a description of a Server Message Block (SMB) file share settings from a file gateway. This operation is only supported for file gateways.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_smb_settings_input.DescribeSMBSettingsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_smb_settings_output.DescribeSMBSettingsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_smb_settings

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_smb_settings.describe_smb_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_smb_settings_input.DescribeSMBSettingsInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_snapshot_schedule(
        self,
        volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_snapshot_schedule_output.DescribeSnapshotScheduleOutput":
        """<p>Describes the snapshot schedule for the specified gateway volume. The snapshot schedule information includes intervals at which snapshots are automatically initiated on the volume. This operation is only supported in the cached volume and stored volume types.</p>

        Args:
            volume_arn: <p>The Amazon Resource Name (ARN) of the volume. Use the <a>ListVolumes</a> operation to return a list of gateway volumes.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe snapshot schedule for gateway volume
            Describes the snapshot schedule for the specified gateway volume including intervals at which snapshots are automatically initiated.

            >>> client.describe_snapshot_schedule(volume_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_snapshot_schedule_input.DescribeSnapshotScheduleInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_snapshot_schedule_output.DescribeSnapshotScheduleOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_snapshot_schedule

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_snapshot_schedule.describe_snapshot_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_snapshot_schedule_input.DescribeSnapshotScheduleInput = {
            "volume_arn": volume_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_storedi_scsi_volumes(
        self,
        volume_ar_ns: "capo_storage_gateway.types.volume_ar_ns.VolumeARNs",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_storedi_scsi_volumes_output.DescribeStorediSCSIVolumesOutput":
        """<p>Returns the description of the gateway volumes specified in the request. The list of gateway volumes in the request must be from one gateway. In the response, Storage Gateway returns volume information sorted by volume ARNs. This operation is only supported in stored volume gateway type.</p>

        Args:
            volume_ar_ns: <p>An array of strings where each string represents the Amazon Resource Name (ARN) of a stored volume. All of the specified stored volumes must be from the same gateway. Use <a>ListVolumes</a> to get volume ARNs for a gateway.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the volumes of a gateway
            Returns the description of the gateway volumes specified in the request belonging to the same gateway.

            >>> client.describe_storedi_scsi_volumes(volume_ar_ns=['arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB'])
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_storedi_scsi_volumes_input.DescribeStorediSCSIVolumesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_storedi_scsi_volumes_output.DescribeStorediSCSIVolumesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_storedi_scsi_volumes

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_storedi_scsi_volumes.describe_storedi_scsi_volumes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_storedi_scsi_volumes_input.DescribeStorediSCSIVolumesInput = {
            "volume_ar_ns": volume_ar_ns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_tape_archives(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        tape_ar_ns: Optional["capo_storage_gateway.types.tape_ar_ns.TapeARNs"] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "capo_storage_gateway.types.describe_tape_archives_output.DescribeTapeArchivesOutput":
        """<p>Returns a description of specified virtual tapes in the virtual tape shelf (VTS). This operation is only supported in the tape gateway type.</p> <p>If a specific <code>TapeARN</code> is not specified, Storage Gateway returns a description of all virtual tapes found in the VTS associated with your account.</p>

        Args:
            tape_ar_ns: <p>Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe.</p>
            marker: <p>An opaque string that indicates the position at which to begin describing virtual tapes.</p>
            limit: <p>Specifies that the number of virtual tapes described be limited to the specified number.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_tape_archives_input.DescribeTapeArchivesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_tape_archives_output.DescribeTapeArchivesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_tape_archives

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_tape_archives.describe_tape_archives(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_tape_archives_input.DescribeTapeArchivesInput = {}
        if tape_ar_ns is not None:
            input_["tape_ar_ns"] = tape_ar_ns
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_tape_archives(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        tape_ar_ns: Optional["capo_storage_gateway.types.tape_ar_ns.TapeARNs"] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "Iterator[capo_storage_gateway.types.tape_archive.TapeArchive]":
        _token = marker
        while True:
            _response = self.describe_tape_archives(
                config_overrides=config_overrides,
                tape_ar_ns=tape_ar_ns,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("tape_archives",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_tape_recovery_points(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "capo_storage_gateway.types.describe_tape_recovery_points_output.DescribeTapeRecoveryPointsOutput":
        """<p>Returns a list of virtual tape recovery points that are available for the specified tape gateway.</p> <p>A recovery point is a point-in-time view of a virtual tape at which all the data on the virtual tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway. This operation is only supported in the tape gateway type.</p>

        Args:
            marker: <p>An opaque string that indicates the position at which to begin describing the virtual tape recovery points.</p>
            limit: <p>Specifies that the number of virtual tape recovery points that are described be limited to the specified number.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_tape_recovery_points_input.DescribeTapeRecoveryPointsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_tape_recovery_points_output.DescribeTapeRecoveryPointsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_tape_recovery_points

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_tape_recovery_points.describe_tape_recovery_points(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_tape_recovery_points_input.DescribeTapeRecoveryPointsInput = {
            "gateway_arn": gateway_arn
        }
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_tape_recovery_points(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "Iterator[capo_storage_gateway.types.tape_recovery_point_info.TapeRecoveryPointInfo]":
        _token = marker
        while True:
            _response = self.describe_tape_recovery_points(
                gateway_arn,
                config_overrides=config_overrides,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("tape_recovery_point_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_tapes(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        tape_ar_ns: Optional["capo_storage_gateway.types.tape_ar_ns.TapeARNs"] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "capo_storage_gateway.types.describe_tapes_output.DescribeTapesOutput":
        """<p>Returns a description of virtual tapes that correspond to the specified Amazon Resource Names (ARNs). If <code>TapeARN</code> is not specified, returns a description of the virtual tapes associated with the specified gateway. This operation is only supported for the tape gateway type.</p> <p>The operation supports pagination. By default, the operation returns a maximum of up to 100 tapes. You can optionally specify the <code>Limit</code> field in the body to limit the number of tapes in the response. If the number of tapes returned in the response is truncated, the response includes a <code>Marker</code> field. You can use this <code>Marker</code> value in your subsequent request to retrieve the next set of tapes.</p>

        Args:
            tape_ar_ns: <p>Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe. If this parameter is not specified, Tape gateway returns a description of all virtual tapes associated with the specified gateway.</p>
            marker: <p>A marker value, obtained in a previous call to <code>DescribeTapes</code>. This marker indicates which page of results to retrieve.</p> <p>If not specified, the first page of results is retrieved.</p>
            limit: <p>Specifies that the number of virtual tapes described be limited to the specified number.</p> <note> <p>Amazon Web Services may impose its own limit, if this field is not set.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe virtual tape(s) associated with gateway
            Returns a description of the specified Amazon Resource Name (ARN) of virtual tapes. If a TapeARN is not specified, returns a description of all virtual tapes.

            >>> client.describe_tapes(gateway_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B', tape_ar_ns=['arn:aws:storagegateway:us-east-1:999999999999:tape/TEST04A2A1', 'arn:aws:storagegateway:us-east-1:999999999999:tape/TEST05A2A0'], marker='1', limit=2)
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_tapes_input.DescribeTapesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_tapes_output.DescribeTapesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_tapes

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_tapes.describe_tapes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_tapes_input.DescribeTapesInput = {
            "gateway_arn": gateway_arn
        }
        if tape_ar_ns is not None:
            input_["tape_ar_ns"] = tape_ar_ns
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_tapes(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        tape_ar_ns: Optional["capo_storage_gateway.types.tape_ar_ns.TapeARNs"] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "Iterator[capo_storage_gateway.types.tape.Tape]":
        _token = marker
        while True:
            _response = self.describe_tapes(
                gateway_arn,
                config_overrides=config_overrides,
                tape_ar_ns=tape_ar_ns,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("tapes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_upload_buffer(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_upload_buffer_output.DescribeUploadBufferOutput":
        """<p>Returns information about the upload buffer of a gateway. This operation is supported for the stored volume, cached volume, and tape gateway types.</p> <p>The response includes disk IDs that are configured as upload buffer space, and it includes the amount of upload buffer space allocated and used.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe upload buffer of a gateway
            Returns information about the upload buffer of a gateway including disk IDs and the amount of upload buffer space allocated and used.

            >>> client.describe_upload_buffer(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
            To describe upload buffer of gateway
            Returns information about the upload buffer of a gateway including disk IDs and the amount of upload buffer space allocated/used.

            >>> client.describe_upload_buffer(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_upload_buffer_input.DescribeUploadBufferInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_upload_buffer_output.DescribeUploadBufferOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_upload_buffer

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_upload_buffer.describe_upload_buffer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_upload_buffer_input.DescribeUploadBufferInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_vtl_devices(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        vtl_device_ar_ns: Optional[
            "capo_storage_gateway.types.vtl_device_ar_ns.VTLDeviceARNs"
        ] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "capo_storage_gateway.types.describe_vtl_devices_output.DescribeVTLDevicesOutput":
        """<p>Returns a description of virtual tape library (VTL) devices for the specified tape gateway. In the response, Storage Gateway returns VTL device information.</p> <p>This operation is only supported in the tape gateway type.</p>

        Args:
            vtl_device_ar_ns: <p>An array of strings, where each string represents the Amazon Resource Name (ARN) of a VTL device.</p> <note> <p>All of the specified VTL devices must be from the same gateway. If no VTL devices are specified, the result will contain all devices on the specified gateway.</p> </note>
            marker: <p>An opaque string that indicates the position at which to begin describing the VTL devices.</p>
            limit: <p>Specifies that the number of VTL devices described be limited to the specified number.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe virtual tape library (VTL) devices of a single gateway
            Returns a description of virtual tape library (VTL) devices for the specified gateway.

            >>> client.describe_vtl_devices(gateway_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B', vtl_device_ar_ns=[], marker='1', limit=123)
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_vtl_devices_input.DescribeVTLDevicesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_vtl_devices_output.DescribeVTLDevicesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_vtl_devices

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_vtl_devices.describe_vtl_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_vtl_devices_input.DescribeVTLDevicesInput = {
            "gateway_arn": gateway_arn
        }
        if vtl_device_ar_ns is not None:
            input_["vtl_device_ar_ns"] = vtl_device_ar_ns
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_vtl_devices(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        vtl_device_ar_ns: Optional[
            "capo_storage_gateway.types.vtl_device_ar_ns.VTLDeviceARNs"
        ] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "Iterator[capo_storage_gateway.types.vtl_device.VTLDevice]":
        _token = marker
        while True:
            _response = self.describe_vtl_devices(
                gateway_arn,
                config_overrides=config_overrides,
                vtl_device_ar_ns=vtl_device_ar_ns,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("vtl_devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_working_storage(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.describe_working_storage_output.DescribeWorkingStorageOutput":
        """<p>Returns information about the working storage of a gateway. This operation is only supported in the stored volumes gateway type. This operation is deprecated in cached volumes API version (20120630). Use DescribeUploadBuffer instead.</p> <note> <p>Working storage is also referred to as upload buffer. You can also use the DescribeUploadBuffer operation to add upload buffer to a stored volume gateway.</p> </note> <p>The response includes disk IDs that are configured as working storage, and it includes the amount of working storage allocated and used.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the working storage of a gateway [Depreciated]
            This operation is supported only for the gateway-stored volume architecture. This operation is deprecated in cached-volumes API version (20120630). Use DescribeUploadBuffer instead.

            >>> client.describe_working_storage(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.describe_working_storage_input.DescribeWorkingStorageInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.describe_working_storage_output.DescribeWorkingStorageOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.describe_working_storage

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.describe_working_storage.describe_working_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.describe_working_storage_input.DescribeWorkingStorageInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detach_volume(
        self,
        volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        force_detach: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
    ) -> "capo_storage_gateway.types.detach_volume_output.DetachVolumeOutput":
        """<p>Disconnects a volume from an iSCSI connection and then detaches the volume from the specified gateway. Detaching and attaching a volume enables you to recover your data from one gateway to a different gateway without creating a snapshot. It also makes it easier to move your volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance. This operation is only supported in the volume gateway type.</p>

        Args:
            volume_arn: <p>The Amazon Resource Name (ARN) of the volume to detach from the gateway.</p>
            force_detach: <p>Set to <code>true</code> to forcibly remove the iSCSI connection of the target volume and detach the volume. The default is <code>false</code>. If this value is set to <code>false</code>, you must manually disconnect the iSCSI connection from the target volume.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.detach_volume_input.DetachVolumeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.detach_volume_output.DetachVolumeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.detach_volume

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.detach_volume.detach_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.detach_volume_input.DetachVolumeInput = {
            "volume_arn": volume_arn
        }
        if force_detach is not None:
            input_["force_detach"] = force_detach

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_gateway(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.disable_gateway_output.DisableGatewayOutput":
        """<p>Disables a tape gateway when the gateway is no longer functioning. For example, if your gateway VM is damaged, you can disable the gateway so you can recover virtual tapes.</p> <p>Use this operation for a tape gateway that is not reachable or not functioning. This operation is only supported in the tape gateway type.</p> <important> <p>After a gateway is disabled, it cannot be enabled.</p> </important>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disable a gateway when it is no longer functioning
            Disables a gateway when the gateway is no longer functioning. Use this operation for a gateway-VTL that is not reachable or not functioning.

            >>> client.disable_gateway(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.disable_gateway_input.DisableGatewayInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.disable_gateway_output.DisableGatewayOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.disable_gateway

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.disable_gateway.disable_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.disable_gateway_input.DisableGatewayInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_file_system(
        self,
        file_system_association_arn: "capo_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        force_delete: Optional["capo_storage_gateway.types.boolean2.Boolean2"] = None,
    ) -> "capo_storage_gateway.types.disassociate_file_system_output.DisassociateFileSystemOutput":
        """<p>Disassociates an Amazon FSx file system from the specified gateway. After the disassociation process finishes, the gateway can no longer access the Amazon FSx file system. This operation is only supported in the FSx File Gateway type.</p>

        Args:
            file_system_association_arn: <p>The Amazon Resource Name (ARN) of the file system association to be deleted.</p>
            force_delete: <p>If this value is set to true, the operation disassociates an Amazon FSx file system immediately. It ends all data uploads to the file system, and the file system association enters the <code>FORCE_DELETING</code> status. If this value is set to false, the Amazon FSx file system does not disassociate until all data is uploaded.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.disassociate_file_system_input.DisassociateFileSystemInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.disassociate_file_system_output.DisassociateFileSystemOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.disassociate_file_system

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.disassociate_file_system.disassociate_file_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.disassociate_file_system_input.DisassociateFileSystemInput = {
            "file_system_association_arn": file_system_association_arn
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def evict_files_failing_upload(
        self,
        file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        force_remove: Optional["capo_storage_gateway.types.boolean2.Boolean2"] = None,
    ) -> "capo_storage_gateway.types.evict_files_failing_upload_output.EvictFilesFailingUploadOutput":
        """<p>Starts a process that cleans the specified file share's cache of file entries that are failing upload to Amazon S3. This API operation reports success if the request is received with valid arguments, and there are no other cache clean operations currently in-progress for the specified file share. After a successful request, the cache clean operation occurs asynchronously and reports progress using CloudWatch logs and notifications.</p> <important> <p>If <code>ForceRemove</code> is set to <code>True</code>, the cache clean operation will delete file data from the gateway which might otherwise be recoverable. We recommend using this operation only after all other methods to clear files failing upload have been exhausted, and if your business need outweighs the potential data loss.</p> </important>

        Args:
            file_share_arn: <p>The Amazon Resource Name (ARN) of the file share for which you want to start the cache clean operation.</p>
            force_remove: <p>Specifies whether cache entries with full or partial file data currently stored on the gateway will be forcibly removed by the cache clean operation.</p> <p>Valid arguments:</p> <ul> <li> <p> <code>False</code> - The cache clean operation skips cache entries failing upload if they are associated with data currently stored on the gateway. This preserves the cached data.</p> </li> <li> <p> <code>True</code> - The cache clean operation removes cache entries failing upload even if they are associated with data currently stored on the gateway. This deletes the cached data.</p> <important> <p>If <code>ForceRemove</code> is set to <code>True</code>, the cache clean operation will delete file data from the gateway which might otherwise be recoverable.</p> </important> </li> </ul>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.evict_files_failing_upload_input.EvictFilesFailingUploadInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.evict_files_failing_upload_output.EvictFilesFailingUploadOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.evict_files_failing_upload

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.evict_files_failing_upload.evict_files_failing_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.evict_files_failing_upload_input.EvictFilesFailingUploadInput = {
            "file_share_arn": file_share_arn
        }
        if force_remove is not None:
            input_["force_remove"] = force_remove

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def join_domain(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        domain_name: "capo_storage_gateway.types.domain_name.DomainName",
        user_name: "capo_storage_gateway.types.domain_user_name.DomainUserName",
        password: "capo_storage_gateway.types.domain_user_password.DomainUserPassword",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        organizational_unit: Optional[
            "capo_storage_gateway.types.organizational_unit.OrganizationalUnit"
        ] = None,
        domain_controllers: Optional["capo_storage_gateway.types.hosts.Hosts"] = None,
        timeout_in_seconds: Optional[
            "capo_storage_gateway.types.timeout_in_seconds.TimeoutInSeconds"
        ] = None,
    ) -> "capo_storage_gateway.types.join_domain_output.JoinDomainOutput":
        """<p>Adds a file gateway to an Active Directory domain. This operation is only supported for file gateways that support the SMB file protocol.</p> <note> <p>Joining a domain creates an Active Directory computer account in the default organizational unit, using the gateway's <b>Gateway ID</b> as the account name (for example, SGW-1234ADE). If your Active Directory environment requires that you pre-stage accounts to facilitate the join domain process, you will need to create this account ahead of time.</p> <p>To create the gateway's computer account in an organizational unit other than the default, you must specify the organizational unit when joining the domain.</p> </note>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            domain_name: <p>The name of the domain that you want the gateway to join.</p>
            organizational_unit: <p>The organizational unit (OU) is a container in an Active Directory that can hold users, groups, computers, and other OUs and this parameter specifies the OU that the gateway will join within the AD domain.</p>
            domain_controllers: <p>List of IP addresses, NetBIOS names, or host names of your domain server. If you need to specify the port number include it after the colon (“:”). For example, <code>mydc.mydomain.com:389</code>.</p> <note> <p>S3 File Gateway supports IPv6 addresses in addition to IPv4 and other existing formats.</p> <p>FSx File Gateway does not support IPv6.</p> </note>
            timeout_in_seconds: <p>Specifies the time in seconds, in which the <code>JoinDomain</code> operation must complete. The default is 20 seconds.</p>
            user_name: <p>Sets the user name of user who has permission to add the gateway to the Active Directory domain. The domain user account should be enabled to join computers to the domain. For example, you can use the domain administrator account or an account with delegated permissions to join computers to the domain.</p>
            password: <p>Sets the password of the user who has permission to add the gateway to the Active Directory domain.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.join_domain_input.JoinDomainInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.join_domain_output.JoinDomainOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.join_domain

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.join_domain.join_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.join_domain_input.JoinDomainInput = {
            "gateway_arn": gateway_arn,
            "domain_name": domain_name,
            "user_name": user_name,
            "password": password,
        }
        if organizational_unit is not None:
            input_["organizational_unit"] = organizational_unit
        if domain_controllers is not None:
            input_["domain_controllers"] = domain_controllers
        if timeout_in_seconds is not None:
            input_["timeout_in_seconds"] = timeout_in_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_automatic_tape_creation_policies(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        gateway_arn: Optional[
            "capo_storage_gateway.types.gateway_arn.GatewayARN"
        ] = None,
    ) -> "capo_storage_gateway.types.list_automatic_tape_creation_policies_output.ListAutomaticTapeCreationPoliciesOutput":
        """<p>Lists the automatic tape creation policies for a gateway. If there are no automatic tape creation policies for the gateway, it returns an empty list.</p> <p>This operation is only supported for tape gateways.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_automatic_tape_creation_policies_input.ListAutomaticTapeCreationPoliciesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_automatic_tape_creation_policies_output.ListAutomaticTapeCreationPoliciesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_automatic_tape_creation_policies

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_automatic_tape_creation_policies.list_automatic_tape_creation_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_automatic_tape_creation_policies_input.ListAutomaticTapeCreationPoliciesInput = {}
        if gateway_arn is not None:
            input_["gateway_arn"] = gateway_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_cache_reports(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
    ) -> "capo_storage_gateway.types.list_cache_reports_output.ListCacheReportsOutput":
        """<p>Returns a list of existing cache reports for all file shares associated with your Amazon Web Services account. This list includes all information provided by the <code>DescribeCacheReport</code> action, such as report name, status, completion progress, start time, end time, filters, and tags.</p>

        Args:
            marker: <p>Opaque pagination token returned from a previous <code>ListCacheReports</code> operation. If present, <code>Marker</code> specifies where to continue the list from after a previous call to <code>ListCacheReports</code>. Optional.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_cache_reports_input.ListCacheReportsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_cache_reports_output.ListCacheReportsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_cache_reports

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_cache_reports.list_cache_reports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_cache_reports_input.ListCacheReportsInput = {}
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_cache_reports(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
    ) -> "Iterator[capo_storage_gateway.types.cache_report_info.CacheReportInfo]":
        _token = marker
        while True:
            _response = self.list_cache_reports(
                config_overrides=config_overrides,
                marker=_token,
            )
            _page = _resolve_path(_response, ("cache_report_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_file_shares(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        gateway_arn: Optional[
            "capo_storage_gateway.types.gateway_arn.GatewayARN"
        ] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
    ) -> "capo_storage_gateway.types.list_file_shares_output.ListFileSharesOutput":
        """<p>Gets a list of the file shares for a specific S3 File Gateway, or the list of file shares that belong to the calling Amazon Web Services account. This operation is only supported for S3 File Gateways.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway whose file shares you want to list. If this field is not present, all file shares under your account are listed.</p>
            limit: <p>The maximum number of file shares to return in the response. The value must be an integer with a value greater than zero. Optional.</p>
            marker: <p>Opaque pagination token returned from a previous ListFileShares operation. If present, <code>Marker</code> specifies where to continue the list from after a previous call to ListFileShares. Optional.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_file_shares_input.ListFileSharesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_file_shares_output.ListFileSharesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_file_shares

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_file_shares.list_file_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_file_shares_input.ListFileSharesInput = {}
        if gateway_arn is not None:
            input_["gateway_arn"] = gateway_arn
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_file_shares(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        gateway_arn: Optional[
            "capo_storage_gateway.types.gateway_arn.GatewayARN"
        ] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
    ) -> "Iterator[capo_storage_gateway.types.file_share_info.FileShareInfo]":
        _token = marker
        while True:
            _response = self.list_file_shares(
                config_overrides=config_overrides,
                gateway_arn=gateway_arn,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("file_share_info_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_file_system_associations(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        gateway_arn: Optional[
            "capo_storage_gateway.types.gateway_arn.GatewayARN"
        ] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
    ) -> "capo_storage_gateway.types.list_file_system_associations_output.ListFileSystemAssociationsOutput":
        """<p>Gets a list of <code>FileSystemAssociationSummary</code> objects. Each object contains a summary of a file system association. This operation is only supported for FSx File Gateways.</p>

        Args:
            limit: <p>The maximum number of file system associations to return in the response. If present, <code>Limit</code> must be an integer with a value greater than zero. Optional.</p>
            marker: <p>Opaque pagination token returned from a previous <code>ListFileSystemAssociations</code> operation. If present, <code>Marker</code> specifies where to continue the list from after a previous call to <code>ListFileSystemAssociations</code>. Optional.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_file_system_associations_input.ListFileSystemAssociationsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_file_system_associations_output.ListFileSystemAssociationsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_file_system_associations

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_file_system_associations.list_file_system_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_file_system_associations_input.ListFileSystemAssociationsInput = {}
        if gateway_arn is not None:
            input_["gateway_arn"] = gateway_arn
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_file_system_associations(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        gateway_arn: Optional[
            "capo_storage_gateway.types.gateway_arn.GatewayARN"
        ] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
    ) -> "Iterator[capo_storage_gateway.types.file_system_association_summary.FileSystemAssociationSummary]":
        _token = marker
        while True:
            _response = self.list_file_system_associations(
                config_overrides=config_overrides,
                gateway_arn=gateway_arn,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("file_system_association_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_gateways(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "capo_storage_gateway.types.list_gateways_output.ListGatewaysOutput":
        """<p>Lists gateways owned by an Amazon Web Services account in an Amazon Web Services Region specified in the request. The returned list is ordered by gateway Amazon Resource Name (ARN).</p> <p>By default, the operation returns a maximum of 100 gateways. This operation supports pagination that allows you to optionally reduce the number of gateways returned in a response.</p> <p>If you have more gateways than are returned in a response (that is, the response returns only a truncated list of your gateways), the response contains a marker that you can specify in your next request to fetch the next page of gateways.</p>

        Args:
            marker: <p>An opaque string that indicates the position at which to begin the returned list of gateways.</p>
            limit: <p>Specifies that the list of gateways returned be limited to the specified number of items.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To lists region specific gateways per AWS account
            Lists gateways owned by an AWS account in a specified region as requested. Results are sorted by gateway ARN up to a maximum of 100 gateways.

            >>> client.list_gateways(marker='1', limit=2)
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_gateways_input.ListGatewaysInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_gateways_output.ListGatewaysOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_gateways

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_gateways_input.ListGatewaysInput = {}
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_gateways(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "Iterator[capo_storage_gateway.types.gateway_info.GatewayInfo]":
        _token = marker
        while True:
            _response = self.list_gateways(
                config_overrides=config_overrides,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("gateways",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_local_disks(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.list_local_disks_output.ListLocalDisksOutput":
        """<p>Returns a list of the gateway's local disks. To specify which gateway to describe, you use the Amazon Resource Name (ARN) of the gateway in the body of the request.</p> <p>The request returns a list of all disks, specifying which are configured as working storage, cache storage, or stored volume or not configured at all. The response includes a <code>DiskStatus</code> field. This field can have a value of present (the disk is available to use), missing (the disk is no longer connected to the gateway), or mismatch (the disk node is occupied by a disk that has incorrect metadata or the disk content is corrupted).</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the gateway's local disks
            The request returns a list of all disks, specifying which are configured as working storage, cache storage, or stored volume or not configured at all.

            >>> client.list_local_disks(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_local_disks_input.ListLocalDisksInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_local_disks_output.ListLocalDisksOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_local_disks

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_local_disks.list_local_disks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_local_disks_input.ListLocalDisksInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_storage_gateway.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "capo_storage_gateway.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags that have been added to the specified resource. This operation is supported in storage gateways of all types.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to list tags.</p>
            marker: <p>An opaque string that indicates the position at which to begin returning the list of tags.</p>
            limit: <p>Specifies that the list of tags returned be limited to the specified number of items.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list tags that have been added to a resource
            Lists the tags that have been added to the specified resource.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B', marker='1', limit=1)
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_tags_for_resource

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_storage_gateway.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "Iterator[capo_storage_gateway.types.tag.Tag]":
        _token = marker
        while True:
            _response = self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_tape_pools(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        pool_ar_ns: Optional["capo_storage_gateway.types.pool_ar_ns.PoolARNs"] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "capo_storage_gateway.types.list_tape_pools_output.ListTapePoolsOutput":
        """<p>Lists custom tape pools. You specify custom tape pools to list by specifying one or more custom tape pool Amazon Resource Names (ARNs). If you don't specify a custom tape pool ARN, the operation lists all custom tape pools.</p> <p>This operation supports pagination. You can optionally specify the <code>Limit</code> parameter in the body to limit the number of tape pools in the response. If the number of tape pools returned in the response is truncated, the response includes a <code>Marker</code> element that you can use in your subsequent request to retrieve the next set of tape pools.</p>

        Args:
            pool_ar_ns: <p>The Amazon Resource Name (ARN) of each of the custom tape pools you want to list. If you don't specify a custom tape pool ARN, the response lists all custom tape pools. </p>
            marker: <p>A string that indicates the position at which to begin the returned list of tape pools.</p>
            limit: <p>An optional number limit for the tape pools in the list returned by this call.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_tape_pools_input.ListTapePoolsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_tape_pools_output.ListTapePoolsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_tape_pools

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_tape_pools.list_tape_pools(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_tape_pools_input.ListTapePoolsInput = {}
        if pool_ar_ns is not None:
            input_["pool_ar_ns"] = pool_ar_ns
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_tape_pools(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        pool_ar_ns: Optional["capo_storage_gateway.types.pool_ar_ns.PoolARNs"] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "Iterator[capo_storage_gateway.types.pool_info.PoolInfo]":
        _token = marker
        while True:
            _response = self.list_tape_pools(
                config_overrides=config_overrides,
                pool_ar_ns=pool_ar_ns,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("pool_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_tapes(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        tape_ar_ns: Optional["capo_storage_gateway.types.tape_ar_ns.TapeARNs"] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "capo_storage_gateway.types.list_tapes_output.ListTapesOutput":
        """<p>Lists virtual tapes in your virtual tape library (VTL) and your virtual tape shelf (VTS). You specify the tapes to list by specifying one or more tape Amazon Resource Names (ARNs). If you don't specify a tape ARN, the operation lists all virtual tapes in both your VTL and VTS.</p> <p>This operation supports pagination. By default, the operation returns a maximum of up to 100 tapes. You can optionally specify the <code>Limit</code> parameter in the body to limit the number of tapes in the response. If the number of tapes returned in the response is truncated, the response includes a <code>Marker</code> element that you can use in your subsequent request to retrieve the next set of tapes. This operation is only supported in the tape gateway type.</p>

        Args:
            marker: <p>A string that indicates the position at which to begin the returned list of tapes.</p>
            limit: <p>An optional number limit for the tapes in the list returned by this call.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_tapes_input.ListTapesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_tapes_output.ListTapesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_tapes

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_tapes.list_tapes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_tapes_input.ListTapesInput = {}
        if tape_ar_ns is not None:
            input_["tape_ar_ns"] = tape_ar_ns
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_tapes(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        tape_ar_ns: Optional["capo_storage_gateway.types.tape_ar_ns.TapeARNs"] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "Iterator[capo_storage_gateway.types.tape_info.TapeInfo]":
        _token = marker
        while True:
            _response = self.list_tapes(
                config_overrides=config_overrides,
                tape_ar_ns=tape_ar_ns,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("tape_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_volume_initiators(
        self,
        volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.list_volume_initiators_output.ListVolumeInitiatorsOutput":
        """<p>Lists iSCSI initiators that are connected to a volume. You can use this operation to determine whether a volume is being used or not. This operation is only supported in the cached volume and stored volume gateway types.</p>

        Args:
            volume_arn: <p>The Amazon Resource Name (ARN) of the volume. Use the <a>ListVolumes</a> operation to return a list of gateway volumes for the gateway.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_volume_initiators_input.ListVolumeInitiatorsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_volume_initiators_output.ListVolumeInitiatorsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_volume_initiators

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_volume_initiators.list_volume_initiators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_volume_initiators_input.ListVolumeInitiatorsInput = {
            "volume_arn": volume_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_volume_recovery_points(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.list_volume_recovery_points_output.ListVolumeRecoveryPointsOutput":
        """<p>Lists the recovery points for a specified gateway. This operation is only supported in the cached volume gateway type.</p> <p>Each cache volume has one recovery point. A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot or clone a new cached volume from a source volume. To create a snapshot from a volume recovery point use the <a>CreateSnapshotFromVolumeRecoveryPoint</a> operation.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list recovery points for a gateway
            Lists the recovery points for a specified gateway in which all data of the volume is consistent and can be used to create a snapshot.

            >>> client.list_volume_recovery_points(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_volume_recovery_points_input.ListVolumeRecoveryPointsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_volume_recovery_points_output.ListVolumeRecoveryPointsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_volume_recovery_points

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_volume_recovery_points.list_volume_recovery_points(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_volume_recovery_points_input.ListVolumeRecoveryPointsInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_volumes(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        gateway_arn: Optional[
            "capo_storage_gateway.types.gateway_arn.GatewayARN"
        ] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "capo_storage_gateway.types.list_volumes_output.ListVolumesOutput":
        """<p>Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN. The response includes only the volume ARNs. If you want additional volume information, use the <a>DescribeStorediSCSIVolumes</a> or the <a>DescribeCachediSCSIVolumes</a> API.</p> <p>The operation supports pagination. By default, the operation returns a maximum of up to 100 volumes. You can optionally specify the <code>Limit</code> field in the body to limit the number of volumes in the response. If the number of volumes returned in the response is truncated, the response includes a Marker field. You can use this Marker value in your subsequent request to retrieve the next set of volumes. This operation is only supported in the cached volume and stored volume gateway types.</p>

        Args:
            marker: <p>A string that indicates the position at which to begin the returned list of volumes. Obtain the marker from the response of a previous List iSCSI Volumes request.</p>
            limit: <p>Specifies that the list of volumes returned be limited to the specified number of items.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the iSCSI stored volumes of a gateway
            Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN up to a maximum of 100 volumes.

            >>> client.list_volumes(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', marker='1', limit=2)
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.list_volumes_input.ListVolumesInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.list_volumes_output.ListVolumesOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.list_volumes

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.list_volumes.list_volumes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.list_volumes_input.ListVolumesInput = {}
        if gateway_arn is not None:
            input_["gateway_arn"] = gateway_arn
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_volumes(
        self,
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        gateway_arn: Optional[
            "capo_storage_gateway.types.gateway_arn.GatewayARN"
        ] = None,
        marker: Optional["capo_storage_gateway.types.marker.Marker"] = None,
        limit: Optional[
            "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
        ] = None,
    ) -> "Iterator[capo_storage_gateway.types.volume_info.VolumeInfo]":
        _token = marker
        while True:
            _response = self.list_volumes(
                config_overrides=config_overrides,
                gateway_arn=gateway_arn,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("volume_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def notify_when_uploaded(
        self,
        file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.notify_when_uploaded_output.NotifyWhenUploadedOutput":
        """<p>Sends you notification through Amazon EventBridge when all files written to your file share have been uploaded to Amazon S3.</p> <p>Storage Gateway can send a notification through Amazon EventBridge when all files written to your file share up to that point in time have been uploaded to Amazon S3. These files include files written to the file share up to the time that you make a request for notification. When the upload is done, Storage Gateway sends you notification through EventBridge. You can configure EventBridge to send the notification through event targets such as Amazon SNS or Lambda function. This operation is only supported for S3 File Gateways.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification">Getting file upload notification</a> in the <i>Amazon S3 File Gateway User Guide</i>.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.notify_when_uploaded_input.NotifyWhenUploadedInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.notify_when_uploaded_output.NotifyWhenUploadedOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.notify_when_uploaded

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.notify_when_uploaded.notify_when_uploaded(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.notify_when_uploaded_input.NotifyWhenUploadedInput = {
            "file_share_arn": file_share_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def refresh_cache(
        self,
        file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        folder_list: Optional[
            "capo_storage_gateway.types.folder_list.FolderList"
        ] = None,
        recursive: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
    ) -> "capo_storage_gateway.types.refresh_cache_output.RefreshCacheOutput":
        """<p>Refreshes the cached inventory of objects for the specified file share. This operation finds objects in the Amazon S3 bucket that were added, removed, or replaced since the gateway last listed the bucket's contents and cached the results. This operation does not import files into the S3 File Gateway cache storage. It only updates the cached inventory to reflect changes in the inventory of the objects in the S3 bucket. This operation is only supported in the S3 File Gateway types.</p> <p>You can subscribe to be notified through an Amazon CloudWatch event when your <code>RefreshCache</code> operation completes. For more information, see <a href="https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification">Getting notified about file operations</a> in the <i>Amazon S3 File Gateway User Guide</i>. This operation is Only supported for S3 File Gateways.</p> <p>When this API is called, it only initiates the refresh operation. When the API call completes and returns a success code, it doesn't necessarily mean that the file refresh has completed. You should use the refresh-complete notification to determine that the operation has completed before you check for new files on the gateway file share. You can subscribe to be notified through a CloudWatch event when your <code>RefreshCache</code> operation completes.</p> <p>Throttle limit: This API is asynchronous, so the gateway will accept no more than two refreshes at any time. We recommend using the refresh-complete CloudWatch event notification before issuing additional requests. For more information, see <a href="https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification">Getting notified about file operations</a> in the <i>Amazon S3 File Gateway User Guide</i>.</p> <important> <ul> <li> <p>Wait at least 60 seconds between consecutive RefreshCache API requests.</p> </li> <li> <p>If you invoke the RefreshCache API when two requests are already being processed, any new request will cause an <code>InvalidGatewayRequestException</code> error because too many requests were sent to the server.</p> </li> </ul> </important> <note> <p>The S3 bucket name does not need to be included when entering the list of folders in the FolderList parameter.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification">Getting notified about file operations</a> in the <i>Amazon S3 File Gateway User Guide</i>.</p>

        Args:
            file_share_arn: <p>The Amazon Resource Name (ARN) of the file share you want to refresh.</p>
            folder_list: <p>A comma-separated list of the paths of folders to refresh in the cache. The default is [<code>"/"</code>]. The default refreshes objects and folders at the root of the Amazon S3 bucket. If <code>Recursive</code> is set to <code>true</code>, the entire S3 bucket that the file share has access to is refreshed.</p> <p>Do not include <code>/</code> when specifying folder names. For example, you would specify <code>samplefolder</code> rather than <code>samplefolder/</code>.</p>
            recursive: <p>A value that specifies whether to recursively refresh folders in the cache. The refresh includes folders that were in the cache the last time the gateway listed the folder's contents. If this value set to <code>true</code>, each folder that is listed in <code>FolderList</code> is recursively updated. Otherwise, subfolders listed in <code>FolderList</code> are not refreshed. Only objects that are in folders listed directly under <code>FolderList</code> are found and used for the update. The default is <code>true</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.refresh_cache_input.RefreshCacheInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.refresh_cache_output.RefreshCacheOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.refresh_cache

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.refresh_cache.refresh_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.refresh_cache_input.RefreshCacheInput = {
            "file_share_arn": file_share_arn
        }
        if folder_list is not None:
            input_["folder_list"] = folder_list
        if recursive is not None:
            input_["recursive"] = recursive

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_tags_from_resource(
        self,
        resource_arn: "capo_storage_gateway.types.resource_arn.ResourceARN",
        tag_keys: "capo_storage_gateway.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.remove_tags_from_resource_output.RemoveTagsFromResourceOutput":
        """<p>Removes one or more tags from the specified resource. This operation is supported in storage gateways of all types.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to remove the tags from.</p>
            tag_keys: <p>The keys of the tags you want to remove from the specified resource. A tag is composed of a key-value pair.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove tags from a resource
            Lists the iSCSI stored volumes of a gateway. Removes one or more tags from the specified resource.

            >>> client.remove_tags_from_resource(resource_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B', tag_keys=['Dev Gatgeway Region', 'East Coast'])
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.remove_tags_from_resource_input.RemoveTagsFromResourceInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.remove_tags_from_resource_output.RemoveTagsFromResourceOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.remove_tags_from_resource

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.remove_tags_from_resource.remove_tags_from_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.remove_tags_from_resource_input.RemoveTagsFromResourceInput = {
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

    def reset_cache(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.reset_cache_output.ResetCacheOutput":
        """<p>Resets all cache disks that have encountered an error and makes the disks available for reconfiguration as cache storage. If your cache disk encounters an error, the gateway prevents read and write operations on virtual tapes in the gateway. For example, an error can occur when a disk is corrupted or removed from the gateway. When a cache is reset, the gateway loses its cache storage. At this point, you can reconfigure the disks as cache disks. This operation is only supported in the cached volume and tape types.</p> <important> <p>If the cache disk you are resetting contains data that has not been uploaded to Amazon S3 yet, that data can be lost. After you reset cache disks, there will be no configured cache disks left in the gateway, so you must configure at least one new cache disk for your gateway to function properly.</p> </important>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To reset cache disks in error status
            Resets all cache disks that have encountered a error and makes the disks available for reconfiguration as cache storage.

            >>> client.reset_cache(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-13B4567C')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.reset_cache_input.ResetCacheInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.reset_cache_output.ResetCacheOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.reset_cache

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.reset_cache.reset_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.reset_cache_input.ResetCacheInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def retrieve_tape_archive(
        self,
        tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN",
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.retrieve_tape_archive_output.RetrieveTapeArchiveOutput":
        """<p>Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a tape gateway. Virtual tapes archived in the VTS are not associated with any gateway. However after a tape is retrieved, it is associated with a gateway, even though it is also listed in the VTS, that is, archive. This operation is only supported in the tape gateway type.</p> <p>Once a tape is successfully retrieved to a gateway, it cannot be retrieved again to another gateway. You must archive the tape again before you can retrieve it to another gateway. This operation is only supported in the tape gateway type.</p>

        Args:
            tape_arn: <p>The Amazon Resource Name (ARN) of the virtual tape you want to retrieve from the virtual tape shelf (VTS).</p>
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway you want to retrieve the virtual tape to. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p> <p>You retrieve archived virtual tapes to only one gateway and the gateway must be a tape gateway.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve an archived tape from the VTS
            Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a gateway-VTL. Virtual tapes archived in the VTS are not associated with any gateway.

            >>> client.retrieve_tape_archive(tape_arn='arn:aws:storagegateway:us-east-1:999999999999:tape/TEST0AA2AF', gateway_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.retrieve_tape_archive_input.RetrieveTapeArchiveInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.retrieve_tape_archive_output.RetrieveTapeArchiveOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.retrieve_tape_archive

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.retrieve_tape_archive.retrieve_tape_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.retrieve_tape_archive_input.RetrieveTapeArchiveInput = {
            "tape_arn": tape_arn,
            "gateway_arn": gateway_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def retrieve_tape_recovery_point(
        self,
        tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN",
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.retrieve_tape_recovery_point_output.RetrieveTapeRecoveryPointOutput":
        """<p>Retrieves the recovery point for the specified virtual tape. This operation is only supported in the tape gateway type.</p> <p>A recovery point is a point in time view of a virtual tape at which all the data on the tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway.</p> <note> <p>The virtual tape can be retrieved to only one gateway. The retrieved tape is read-only. The virtual tape can be retrieved to only a tape gateway. There is no charge for retrieving recovery points.</p> </note>

        Args:
            tape_arn: <p>The Amazon Resource Name (ARN) of the virtual tape for which you want to retrieve the recovery point.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve the recovery point of a virtual tape
            Retrieves the recovery point for the specified virtual tape.

            >>> client.retrieve_tape_recovery_point(tape_arn='arn:aws:storagegateway:us-east-1:999999999999:tape/TEST0AA2AF', gateway_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.retrieve_tape_recovery_point_input.RetrieveTapeRecoveryPointInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.retrieve_tape_recovery_point_output.RetrieveTapeRecoveryPointOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.retrieve_tape_recovery_point

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.retrieve_tape_recovery_point.retrieve_tape_recovery_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.retrieve_tape_recovery_point_input.RetrieveTapeRecoveryPointInput = {
            "tape_arn": tape_arn,
            "gateway_arn": gateway_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_local_console_password(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        local_console_password: "capo_storage_gateway.types.local_console_password.LocalConsolePassword",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.set_local_console_password_output.SetLocalConsolePasswordOutput":
        """<p>Sets the password for your VM local console. When you log in to the local console for the first time, you log in to the VM with the default credentials. We recommend that you set a new password. You don't need to know the default password to set a new password.</p>

        Args:
            local_console_password: <p>The password you want to set for your VM local console.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set a password for your VM
            Sets the password for your VM local console.

            >>> client.set_local_console_password(gateway_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B', local_console_password='PassWordMustBeAtLeast6Chars.')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.set_local_console_password_input.SetLocalConsolePasswordInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.set_local_console_password_output.SetLocalConsolePasswordOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.set_local_console_password

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.set_local_console_password.set_local_console_password(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.set_local_console_password_input.SetLocalConsolePasswordInput = {
            "gateway_arn": gateway_arn,
            "local_console_password": local_console_password,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_smb_guest_password(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        password: "capo_storage_gateway.types.smb_guest_password.SMBGuestPassword",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.set_smb_guest_password_output.SetSMBGuestPasswordOutput":
        """<p>Sets the password for the guest user <code>smbguest</code>. The <code>smbguest</code> user is the user when the authentication method for the file share is set to <code>GuestAccess</code>. This operation only supported for S3 File Gateways</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the S3 File Gateway the SMB file share is associated with.</p>
            password: <p>The password that you want to set for your SMB server.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.set_smb_guest_password_input.SetSMBGuestPasswordInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.set_smb_guest_password_output.SetSMBGuestPasswordOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.set_smb_guest_password

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.set_smb_guest_password.set_smb_guest_password(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.set_smb_guest_password_input.SetSMBGuestPasswordInput = {
            "gateway_arn": gateway_arn,
            "password": password,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def shutdown_gateway(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.shutdown_gateway_output.ShutdownGatewayOutput":
        """<p>Shuts down a Tape Gateway or Volume Gateway. To specify which gateway to shut down, use the Amazon Resource Name (ARN) of the gateway in the body of your request.</p> <note> <p>This API action cannot be used to shut down S3 File Gateway or FSx File Gateway.</p> </note> <p>The operation shuts down the gateway service component running in the gateway's virtual machine (VM) and not the host VM.</p> <note> <p>If you want to shut down the VM, it is recommended that you first shut down the gateway component in the VM to avoid unpredictable conditions.</p> </note> <p>After the gateway is shutdown, you cannot call any other API except <a>StartGateway</a>, <a>DescribeGatewayInformation</a>, and <a>ListGateways</a>. For more information, see <a>ActivateGateway</a>. Your applications cannot read from or write to the gateway's storage volumes, and there are no snapshots taken.</p> <note> <p>When you make a shutdown request, you will get a <code>200 OK</code> success response immediately. However, it might take some time for the gateway to shut down. You can call the <a>DescribeGatewayInformation</a> API to check the status. For more information, see <a>ActivateGateway</a>.</p> </note> <p>If do not intend to use the gateway again, you must delete the gateway (using <a>DeleteGateway</a>) to no longer pay software charges associated with the gateway.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To shut down a gateway service
            This operation shuts down the gateway service component running in the storage gateway's virtual machine (VM) and not the VM.

            >>> client.shutdown_gateway(gateway_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.shutdown_gateway_input.ShutdownGatewayInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.shutdown_gateway_output.ShutdownGatewayOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.shutdown_gateway

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.shutdown_gateway.shutdown_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.shutdown_gateway_input.ShutdownGatewayInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_availability_monitor_test(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.start_availability_monitor_test_output.StartAvailabilityMonitorTestOutput":
        """<p>Start a test that verifies that the specified gateway is configured for High Availability monitoring in your host environment. This request only initiates the test and that a successful response only indicates that the test was started. It doesn't indicate that the test passed. For the status of the test, invoke the <code>DescribeAvailabilityMonitorTest</code> API.</p> <note> <p>Starting this test will cause your gateway to go offline for a brief period.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.start_availability_monitor_test_input.StartAvailabilityMonitorTestInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.start_availability_monitor_test_output.StartAvailabilityMonitorTestOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.start_availability_monitor_test

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.start_availability_monitor_test.start_availability_monitor_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.start_availability_monitor_test_input.StartAvailabilityMonitorTestInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_cache_report(
        self,
        file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN",
        role: "capo_storage_gateway.types.role.Role",
        location_arn: "capo_storage_gateway.types.location_arn.LocationARN",
        bucket_region: "capo_storage_gateway.types.region_id.RegionId",
        client_token: "capo_storage_gateway.types.client_token.ClientToken",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        vpc_endpoint_dns_name: Optional[
            "capo_storage_gateway.types.dns_host_name.DNSHostName"
        ] = None,
        inclusion_filters: Optional[
            "capo_storage_gateway.types.cache_report_filter_list.CacheReportFilterList"
        ] = None,
        exclusion_filters: Optional[
            "capo_storage_gateway.types.cache_report_filter_list.CacheReportFilterList"
        ] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.start_cache_report_output.StartCacheReportOutput":
        """<p>Starts generating a report of the file metadata currently cached by an S3 File Gateway for a specific file share. You can use this report to identify and resolve issues if you have files failing upload from your gateway to Amazon S3. The report is a CSV file containing a list of files which match the set of filter parameters you specify in the request.</p> <note> <p>The <b>Files Failing Upload</b> flag is reset every 24 hours and during gateway reboot. If this report captures the files after the reset, but before they become flagged again, they will not be reported as <b>Files Failing Upload</b>.</p> </note> <p>The following requirements must be met to successfully generate a cache report:</p> <ul> <li> <p>You must have <code>s3:PutObject</code> and <code>s3:AbortMultipartUpload</code> permissions for the Amazon S3 bucket where you want to store the cache report.</p> </li> <li> <p>No other cache reports can currently be in-progress for the specified file share.</p> </li> <li> <p>There must be fewer than 10 existing cache reports for the specified file share.</p> </li> <li> <p>The gateway must be online and connected to Amazon Web Services.</p> </li> <li> <p>The root disk must have at least 20GB of free space when report generation starts.</p> </li> <li> <p>You must specify at least one value for <code>InclusionFilters</code> or <code>ExclusionFilters</code> in the request.</p> </li> </ul>

        Args:
            role: <p>The ARN of the IAM role used when saving the cache report to Amazon S3.</p>
            location_arn: <p>The ARN of the Amazon S3 bucket where you want to save the cache report.</p> <note> <p>We do not recommend saving the cache report to the same Amazon S3 bucket for which you are generating the report.</p> <p>This field does not accept access point ARNs.</p> </note>
            bucket_region: <p>The Amazon Web Services Region of the Amazon S3 bucket where you want to save the cache report.</p>
            vpc_endpoint_dns_name: <p>The DNS name of the VPC endpoint associated with the Amazon S3 where you want to save the cache report. Optional.</p>
            inclusion_filters: <p>The list of filters and parameters that determine which files are included in the report. You must specify at least one value for <code>InclusionFilters</code> or <code>ExclusionFilters</code> in a <code>StartCacheReport</code> request.</p>
            exclusion_filters: <p>The list of filters and parameters that determine which files are excluded from the report. You must specify at least one value for <code>InclusionFilters</code> or <code>ExclusionFilters</code> in a <code>StartCacheReport</code> request.</p>
            client_token: <p>A unique identifier that you use to ensure idempotent report generation if you need to retry an unsuccessful <code>StartCacheReport</code> request. If you retry a request, use the same <code>ClientToken</code> you specified in the initial request.</p>
            tags: <p>A list of up to 50 key/value tags that you can assign to the cache report. Using tags can help you categorize your reports and more easily locate them in search results.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.start_cache_report_input.StartCacheReportInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.start_cache_report_output.StartCacheReportOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.start_cache_report

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.start_cache_report.start_cache_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.start_cache_report_input.StartCacheReportInput = {
            "file_share_arn": file_share_arn,
            "role": role,
            "location_arn": location_arn,
            "bucket_region": bucket_region,
            "client_token": client_token,
        }
        if vpc_endpoint_dns_name is not None:
            input_["vpc_endpoint_dns_name"] = vpc_endpoint_dns_name
        if inclusion_filters is not None:
            input_["inclusion_filters"] = inclusion_filters
        if exclusion_filters is not None:
            input_["exclusion_filters"] = exclusion_filters
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_gateway(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.start_gateway_output.StartGatewayOutput":
        """<p>Starts a gateway that you previously shut down (see <a>ShutdownGateway</a>). After the gateway starts, you can then make other API calls, your applications can read from or write to the gateway's storage volumes and you will be able to take snapshot backups.</p> <note> <p>When you make a request, you will get a 200 OK success response immediately. However, it might take some time for the gateway to be ready. You should call <a>DescribeGatewayInformation</a> and check the status before making any additional API calls. For more information, see <a>ActivateGateway</a>.</p> </note> <p>To specify which gateway to start, use the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To start a gateway service
            Starts a gateway service that was previously shut down.

            >>> client.start_gateway(gateway_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.start_gateway_input.StartGatewayInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.start_gateway_output.StartGatewayOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.start_gateway

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.start_gateway.start_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.start_gateway_input.StartGatewayInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_automatic_tape_creation_policy(
        self,
        automatic_tape_creation_rules: "capo_storage_gateway.types.automatic_tape_creation_rules.AutomaticTapeCreationRules",
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.update_automatic_tape_creation_policy_output.UpdateAutomaticTapeCreationPolicyOutput":
        """<p>Updates the automatic tape creation policy of a gateway. Use this to update the policy with a new set of automatic tape creation rules. This is only supported for tape gateways.</p> <p>By default, there is no automatic tape creation policy.</p> <note> <p>A gateway can have only one automatic tape creation policy.</p> </note>

        Args:
            automatic_tape_creation_rules: <p>An automatic tape creation policy consists of a list of automatic tape creation rules. The rules determine when and how to automatically create new tapes.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_automatic_tape_creation_policy_input.UpdateAutomaticTapeCreationPolicyInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_automatic_tape_creation_policy_output.UpdateAutomaticTapeCreationPolicyOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_automatic_tape_creation_policy

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_automatic_tape_creation_policy.update_automatic_tape_creation_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_automatic_tape_creation_policy_input.UpdateAutomaticTapeCreationPolicyInput = {
            "automatic_tape_creation_rules": automatic_tape_creation_rules,
            "gateway_arn": gateway_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bandwidth_rate_limit(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        average_upload_rate_limit_in_bits_per_sec: Optional[
            "capo_storage_gateway.types.bandwidth_upload_rate_limit.BandwidthUploadRateLimit"
        ] = None,
        average_download_rate_limit_in_bits_per_sec: Optional[
            "capo_storage_gateway.types.bandwidth_download_rate_limit.BandwidthDownloadRateLimit"
        ] = None,
    ) -> "capo_storage_gateway.types.update_bandwidth_rate_limit_output.UpdateBandwidthRateLimitOutput":
        """<p>Updates the bandwidth rate limits of a gateway. You can update both the upload and download bandwidth rate limit or specify only one of the two. If you don't set a bandwidth rate limit, the existing rate limit remains. This operation is supported only for the stored volume, cached volume, and tape gateway types. To update bandwidth rate limits for S3 file gateways, use <a>UpdateBandwidthRateLimitSchedule</a>.</p> <p>By default, a gateway's bandwidth rate limits are not set. If you don't set any limit, the gateway does not have any limitations on its bandwidth usage and could potentially use the maximum available bandwidth.</p> <p>To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Args:
            average_upload_rate_limit_in_bits_per_sec: <p>The average upload bandwidth rate limit in bits per second.</p>
            average_download_rate_limit_in_bits_per_sec: <p>The average download bandwidth rate limit in bits per second.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the bandwidth rate limits of a gateway
            Updates the bandwidth rate limits of a gateway. Both the upload and download bandwidth rate limit can be set, or either one of the two. If a new limit is not set, the existing rate limit remains.

            >>> client.update_bandwidth_rate_limit(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', average_upload_rate_limit_in_bits_per_sec=51200, average_download_rate_limit_in_bits_per_sec=102400)
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_bandwidth_rate_limit_input.UpdateBandwidthRateLimitInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_bandwidth_rate_limit_output.UpdateBandwidthRateLimitOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_bandwidth_rate_limit

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_bandwidth_rate_limit.update_bandwidth_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_bandwidth_rate_limit_input.UpdateBandwidthRateLimitInput = {
            "gateway_arn": gateway_arn
        }
        if average_upload_rate_limit_in_bits_per_sec is not None:
            input_["average_upload_rate_limit_in_bits_per_sec"] = (
                average_upload_rate_limit_in_bits_per_sec
            )
        if average_download_rate_limit_in_bits_per_sec is not None:
            input_["average_download_rate_limit_in_bits_per_sec"] = (
                average_download_rate_limit_in_bits_per_sec
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bandwidth_rate_limit_schedule(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        bandwidth_rate_limit_intervals: "capo_storage_gateway.types.bandwidth_rate_limit_intervals.BandwidthRateLimitIntervals",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.update_bandwidth_rate_limit_schedule_output.UpdateBandwidthRateLimitScheduleOutput":
        """<p> Updates the bandwidth rate limit schedule for a specified gateway. By default, gateways do not have bandwidth rate limit schedules, which means no bandwidth rate limiting is in effect. Use this to initiate or update a gateway's bandwidth rate limit schedule. This operation is supported for volume, tape, and S3 file gateways. S3 file gateways support bandwidth rate limits for upload only. FSx file gateways do not support bandwidth rate limits.</p>

        Args:
            bandwidth_rate_limit_intervals: <p> An array containing bandwidth rate limit schedule intervals for a gateway. When no bandwidth rate limit intervals have been scheduled, the array is empty. </p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_bandwidth_rate_limit_schedule_input.UpdateBandwidthRateLimitScheduleInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_bandwidth_rate_limit_schedule_output.UpdateBandwidthRateLimitScheduleOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_bandwidth_rate_limit_schedule

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_bandwidth_rate_limit_schedule.update_bandwidth_rate_limit_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_bandwidth_rate_limit_schedule_input.UpdateBandwidthRateLimitScheduleInput = {
            "gateway_arn": gateway_arn,
            "bandwidth_rate_limit_intervals": bandwidth_rate_limit_intervals,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_chap_credentials(
        self,
        target_arn: "capo_storage_gateway.types.target_arn.TargetARN",
        secret_to_authenticate_initiator: "capo_storage_gateway.types.chap_secret.ChapSecret",
        initiator_name: "capo_storage_gateway.types.iqn_name.IqnName",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        secret_to_authenticate_target: Optional[
            "capo_storage_gateway.types.chap_secret.ChapSecret"
        ] = None,
    ) -> "capo_storage_gateway.types.update_chap_credentials_output.UpdateChapCredentialsOutput":
        """<p>Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target. By default, a gateway does not have CHAP enabled; however, for added security, you might use it. This operation is supported in the volume and tape gateway types.</p> <important> <p>When you update CHAP credentials, all existing connections on the target are closed and initiators must reconnect with the new credentials.</p> </important>

        Args:
            target_arn: <p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return the TargetARN for specified VolumeARN.</p>
            secret_to_authenticate_initiator: <p>The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.</p> <note> <p>The secret key must be between 12 and 16 bytes when encoded in UTF-8.</p> </note>
            initiator_name: <p>The iSCSI initiator that connects to the target.</p>
            secret_to_authenticate_target: <p>The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).</p> <p>Byte constraints: Minimum bytes of 12. Maximum bytes of 16.</p> <note> <p>The secret key must be between 12 and 16 bytes when encoded in UTF-8.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update CHAP credentials for an iSCSI target
            Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target.

            >>> client.update_chap_credentials(target_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume', secret_to_authenticate_initiator='111111111111', initiator_name='iqn.1991-05.com.microsoft:computername.domain.example.com', secret_to_authenticate_target='222222222222')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_chap_credentials_input.UpdateChapCredentialsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_chap_credentials_output.UpdateChapCredentialsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_chap_credentials

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_chap_credentials.update_chap_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_chap_credentials_input.UpdateChapCredentialsInput = {
            "target_arn": target_arn,
            "secret_to_authenticate_initiator": secret_to_authenticate_initiator,
            "initiator_name": initiator_name,
        }
        if secret_to_authenticate_target is not None:
            input_["secret_to_authenticate_target"] = secret_to_authenticate_target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_file_system_association(
        self,
        file_system_association_arn: "capo_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        user_name: Optional[
            "capo_storage_gateway.types.domain_user_name.DomainUserName"
        ] = None,
        password: Optional[
            "capo_storage_gateway.types.domain_user_password.DomainUserPassword"
        ] = None,
        audit_destination_arn: Optional[
            "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
        ] = None,
        cache_attributes: Optional[
            "capo_storage_gateway.types.cache_attributes.CacheAttributes"
        ] = None,
    ) -> "capo_storage_gateway.types.update_file_system_association_output.UpdateFileSystemAssociationOutput":
        """<p>Updates a file system association. This operation is only supported in the FSx File Gateways.</p>

        Args:
            file_system_association_arn: <p>The Amazon Resource Name (ARN) of the file system association that you want to update.</p>
            user_name: <p>The user name of the user credential that has permission to access the root share D$ of the Amazon FSx file system. The user account must belong to the Amazon FSx delegated admin user group.</p>
            password: <p>The password of the user credential.</p>
            audit_destination_arn: <p>The Amazon Resource Name (ARN) of the storage used for the audit logs.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_file_system_association_input.UpdateFileSystemAssociationInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_file_system_association_output.UpdateFileSystemAssociationOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_file_system_association

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_file_system_association.update_file_system_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_file_system_association_input.UpdateFileSystemAssociationInput = {
            "file_system_association_arn": file_system_association_arn
        }
        if user_name is not None:
            input_["user_name"] = user_name
        if password is not None:
            input_["password"] = password
        if audit_destination_arn is not None:
            input_["audit_destination_arn"] = audit_destination_arn
        if cache_attributes is not None:
            input_["cache_attributes"] = cache_attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gateway_information(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        gateway_name: Optional[
            "capo_storage_gateway.types.gateway_name.GatewayName"
        ] = None,
        gateway_timezone: Optional[
            "capo_storage_gateway.types.gateway_timezone.GatewayTimezone"
        ] = None,
        cloud_watch_log_group_arn: Optional[
            "capo_storage_gateway.types.cloud_watch_log_group_arn.CloudWatchLogGroupARN"
        ] = None,
        gateway_capacity: Optional[
            "capo_storage_gateway.types.gateway_capacity.GatewayCapacity"
        ] = None,
    ) -> "capo_storage_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput":
        """<p>Updates a gateway's metadata, which includes the gateway's name, time zone, and metadata cache size. To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.</p> <note> <p>For gateways activated after September 2, 2015, the gateway's ARN contains the gateway ID rather than the gateway name. However, changing the name of the gateway has no effect on the gateway's ARN.</p> </note>

        Args:
            gateway_timezone: <p>A value that indicates the time zone of the gateway.</p>
            cloud_watch_log_group_arn: <p>The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that you want to use to monitor and log events in the gateway.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html">What is Amazon CloudWatch Logs?</a> </p>
            gateway_capacity: <p>Specifies the size of the gateway's metadata cache. This setting impacts gateway performance and hardware recommendations. For more information, see <a href="https://docs.aws.amazon.com/filegateway/latest/files3/performance-multiple-file-shares.html">Performance guidance for gateways with multiple file shares</a> in the <i>Amazon S3 File Gateway User Guide</i>.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a gateway's metadata
            Updates a gateway's metadata, which includes the gateway's name and time zone.

            >>> client.update_gateway_information(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', gateway_name='MyGateway2', gateway_timezone='GMT-12:00')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_gateway_information

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_gateway_information.update_gateway_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput = {
            "gateway_arn": gateway_arn
        }
        if gateway_name is not None:
            input_["gateway_name"] = gateway_name
        if gateway_timezone is not None:
            input_["gateway_timezone"] = gateway_timezone
        if cloud_watch_log_group_arn is not None:
            input_["cloud_watch_log_group_arn"] = cloud_watch_log_group_arn
        if gateway_capacity is not None:
            input_["gateway_capacity"] = gateway_capacity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gateway_software_now(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput":
        """<p>Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.</p> <note> <p>When you make this request, you get a <code>200 OK</code> success response immediately. However, it might take some time for the update to complete. You can call <a>DescribeGatewayInformation</a> to verify the gateway is in the <code>STATE_RUNNING</code> state.</p> </note> <important> <p>A software update forces a system restart of your gateway. You can minimize the chance of any disruption to your applications by increasing your iSCSI Initiators' timeouts. For more information about increasing iSCSI Initiator timeouts for Windows and Linux, see <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorWindowsClient.html#CustomizeWindowsiSCSISettings">Customizing your Windows iSCSI settings</a> and <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorRedHatClient.html#CustomizeLinuxiSCSISettings">Customizing your Linux iSCSI settings</a>, respectively.</p> </important>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a gateway's VM software
            Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.

            >>> client.update_gateway_software_now(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_gateway_software_now

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_gateway_software_now.update_gateway_software_now(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_maintenance_start_time(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        hour_of_day: Optional[
            "capo_storage_gateway.types.hour_of_day.HourOfDay"
        ] = None,
        minute_of_hour: Optional[
            "capo_storage_gateway.types.minute_of_hour.MinuteOfHour"
        ] = None,
        day_of_week: Optional[
            "capo_storage_gateway.types.day_of_week.DayOfWeek"
        ] = None,
        day_of_month: Optional[
            "capo_storage_gateway.types.day_of_month.DayOfMonth"
        ] = None,
        software_update_preferences: Optional[
            "capo_storage_gateway.types.software_update_preferences.SoftwareUpdatePreferences"
        ] = None,
    ) -> "capo_storage_gateway.types.update_maintenance_start_time_output.UpdateMaintenanceStartTimeOutput":
        """<p>Updates a gateway's maintenance window schedule, with settings for monthly or weekly cadence, specific day and time to begin maintenance, and which types of updates to apply. Time configuration uses the gateway's time zone. You can pass values for a complete maintenance schedule, or update policy, or both. Previous values will persist for whichever setting you choose not to modify. If an incomplete or invalid maintenance schedule is passed, the entire request will be rejected with an error and no changes will occur.</p> <p>A complete maintenance schedule must include values for <i>both</i> <code>MinuteOfHour</code> and <code>HourOfDay</code>, and <i>either</i> <code>DayOfMonth</code> <i>or</i> <code>DayOfWeek</code>.</p> <note> <p>We recommend keeping maintenance updates turned on, except in specific use cases where the brief disruptions caused by updating the gateway could critically impact your deployment.</p> </note>

        Args:
            hour_of_day: <p>The hour component of the maintenance start time represented as <i>hh</i>, where <i>hh</i> is the hour (00 to 23). The hour of the day is in the time zone of the gateway.</p>
            minute_of_hour: <p>The minute component of the maintenance start time represented as <i>mm</i>, where <i>mm</i> is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.</p>
            day_of_week: <p>The day of the week component of the maintenance start time week represented as an ordinal number from 0 to 6, where 0 represents Sunday and 6 represents Saturday.</p>
            day_of_month: <p>The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month. It is not possible to set the maintenance schedule to start on days 29 through 31.</p>
            software_update_preferences: <p>A set of variables indicating the software update preferences for the gateway.</p> <p>Includes <code>AutomaticUpdatePolicy</code> field with the following inputs:</p> <p> <code>ALL_VERSIONS</code> - Enables regular gateway maintenance updates.</p> <p> <code>EMERGENCY_VERSIONS_ONLY</code> - Disables regular gateway maintenance updates. The gateway will still receive emergency version updates on rare occasions if necessary to remedy highly critical security or durability issues. You will be notified before an emergency version update is applied. These updates are applied during your gateway's scheduled maintenance window.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a gateway's maintenance start time
            Updates a gateway's weekly maintenance start time information, including day and time of the week. The maintenance time is in your gateway's time zone.

            >>> client.update_maintenance_start_time(gateway_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B', hour_of_day=0, minute_of_hour=30, day_of_week=2)
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_maintenance_start_time_input.UpdateMaintenanceStartTimeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_maintenance_start_time_output.UpdateMaintenanceStartTimeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_maintenance_start_time

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_maintenance_start_time.update_maintenance_start_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_maintenance_start_time_input.UpdateMaintenanceStartTimeInput = {
            "gateway_arn": gateway_arn
        }
        if hour_of_day is not None:
            input_["hour_of_day"] = hour_of_day
        if minute_of_hour is not None:
            input_["minute_of_hour"] = minute_of_hour
        if day_of_week is not None:
            input_["day_of_week"] = day_of_week
        if day_of_month is not None:
            input_["day_of_month"] = day_of_month
        if software_update_preferences is not None:
            input_["software_update_preferences"] = software_update_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_nfs_file_share(
        self,
        file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        encryption_type: Optional[
            "capo_storage_gateway.types.encryption_type.EncryptionType"
        ] = None,
        kms_encrypted: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        kms_key: Optional["capo_storage_gateway.types.kms_key.KMSKey"] = None,
        nfs_file_share_defaults: Optional[
            "capo_storage_gateway.types.nfs_file_share_defaults.NFSFileShareDefaults"
        ] = None,
        default_storage_class: Optional[
            "capo_storage_gateway.types.storage_class.StorageClass"
        ] = None,
        object_acl: Optional["capo_storage_gateway.types.object_acl.ObjectACL"] = None,
        client_list: Optional[
            "capo_storage_gateway.types.file_share_client_list.FileShareClientList"
        ] = None,
        squash: Optional["capo_storage_gateway.types.squash.Squash"] = None,
        read_only: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        guess_mime_type_enabled: Optional[
            "capo_storage_gateway.types.boolean.Boolean"
        ] = None,
        requester_pays: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        file_share_name: Optional[
            "capo_storage_gateway.types.file_share_name.FileShareName"
        ] = None,
        cache_attributes: Optional[
            "capo_storage_gateway.types.cache_attributes.CacheAttributes"
        ] = None,
        notification_policy: Optional[
            "capo_storage_gateway.types.notification_policy.NotificationPolicy"
        ] = None,
        audit_destination_arn: Optional[
            "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
        ] = None,
    ) -> "capo_storage_gateway.types.update_nfs_file_share_output.UpdateNFSFileShareOutput":
        r"""<p>Updates a Network File System (NFS) file share. This operation is only supported in S3 File Gateways.</p> <note> <p>To leave a file share field unchanged, set the corresponding input field to null.</p> </note> <p>Updates the following file share settings:</p> <ul> <li> <p>Default storage class for your S3 bucket</p> </li> <li> <p>Metadata defaults for your S3 bucket</p> </li> <li> <p>Allowed NFS clients for your file share</p> </li> <li> <p>Squash settings</p> </li> <li> <p>Write status of your file share</p> </li> </ul>

        Args:
            file_share_arn: <p>The Amazon Resource Name (ARN) of the file share to be updated.</p>
            encryption_type: <p>A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note>
            kms_encrypted: <p>Optional. Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key (SSE-KMS), or <code>false</code> to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the <code>EncryptionType</code> parameter instead.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            kms_key: <p>Optional. The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value must be set if <code>KMSEncrypted</code> is <code>true</code>, or if <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>.</p>
            nfs_file_share_defaults: <p>The default values for the file share. Optional.</p>
            default_storage_class: <p>The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is <code>S3_STANDARD</code>. Optional.</p> <p>Valid Values: <code>S3_STANDARD</code> | <code>S3_INTELLIGENT_TIERING</code> | <code>S3_STANDARD_IA</code> | <code>S3_ONEZONE_IA</code> </p>
            object_acl: <p>A value that sets the access control list (ACL) permission for objects in the S3 bucket that a S3 File Gateway puts objects into. The default value is <code>private</code>.</p>
            client_list: <p>The list of clients that are allowed to access the S3 File Gateway. The list must contain either valid IPv4/IPv6 addresses or valid CIDR blocks.</p>
            squash: <p>The user mapped to anonymous user.</p> <p>Valid values are the following:</p> <ul> <li> <p> <code>RootSquash</code>: Only root is mapped to anonymous user.</p> </li> <li> <p> <code>NoSquash</code>: No one is mapped to anonymous user.</p> </li> <li> <p> <code>AllSquash</code>: Everyone is mapped to anonymous user.</p> </li> </ul>
            read_only: <p>A value that sets the write status of a file share. Set this value to <code>true</code> to set the write status to read-only, otherwise set to <code>false</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            guess_mime_type_enabled: <p>A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to <code>true</code> to enable MIME type guessing, otherwise set to <code>false</code>. The default value is <code>true</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            requester_pays: <p>A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to <code>true</code>, the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.</p> <note> <p> <code>RequesterPays</code> is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            file_share_name: <p>The name of the file share. Optional.</p> <note> <p> <code>FileShareName</code> must be set if an S3 prefix name is set in <code>LocationARN</code>, or if an access point or access point alias is used.</p> <p>A valid NFS file share name can only contain the following characters: <code>a</code>-<code>z</code>, <code>A</code>-<code>Z</code>, <code>0</code>-<code>9</code>, <code>-</code>, <code>.</code>, and <code>_</code>.</p> </note>
            cache_attributes: <p>Specifies refresh cache information for the file share.</p>
            notification_policy: <p>The notification policy of the file share. <code>SettlingTimeInSeconds</code> controls the number of seconds to wait after the last point in time a client wrote to a file before generating an <code>ObjectUploaded</code> notification. Because clients can make many small writes to files, it's best to set this parameter for as long as possible to avoid generating multiple notifications for the same file in a small time period.</p> <note> <p> <code>SettlingTimeInSeconds</code> has no effect on the timing of the object uploading to Amazon S3, only the timing of the notification.</p> <p>This setting is not meant to specify an exact time at which the notification will be sent. In some cases, the gateway might require more than the specified delay time to generate and send notifications.</p> </note> <p>The following example sets <code>NotificationPolicy</code> on with <code>SettlingTimeInSeconds</code> set to 60.</p> <p> <code>{\"Upload\": {\"SettlingTimeInSeconds\": 60}}</code> </p> <p>The following example sets <code>NotificationPolicy</code> off.</p> <p> <code>{}</code> </p>
            audit_destination_arn: <p>The Amazon Resource Name (ARN) of the storage used for audit logs.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_nfs_file_share_input.UpdateNFSFileShareInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_nfs_file_share_output.UpdateNFSFileShareOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_nfs_file_share

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_nfs_file_share.update_nfs_file_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_nfs_file_share_input.UpdateNFSFileShareInput = {
            "file_share_arn": file_share_arn
        }
        if encryption_type is not None:
            input_["encryption_type"] = encryption_type
        if kms_encrypted is not None:
            input_["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if nfs_file_share_defaults is not None:
            input_["nfs_file_share_defaults"] = nfs_file_share_defaults
        if default_storage_class is not None:
            input_["default_storage_class"] = default_storage_class
        if object_acl is not None:
            input_["object_acl"] = object_acl
        if client_list is not None:
            input_["client_list"] = client_list
        if squash is not None:
            input_["squash"] = squash
        if read_only is not None:
            input_["read_only"] = read_only
        if guess_mime_type_enabled is not None:
            input_["guess_mime_type_enabled"] = guess_mime_type_enabled
        if requester_pays is not None:
            input_["requester_pays"] = requester_pays
        if file_share_name is not None:
            input_["file_share_name"] = file_share_name
        if cache_attributes is not None:
            input_["cache_attributes"] = cache_attributes
        if notification_policy is not None:
            input_["notification_policy"] = notification_policy
        if audit_destination_arn is not None:
            input_["audit_destination_arn"] = audit_destination_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_smb_file_share(
        self,
        file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        encryption_type: Optional[
            "capo_storage_gateway.types.encryption_type.EncryptionType"
        ] = None,
        kms_encrypted: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        kms_key: Optional["capo_storage_gateway.types.kms_key.KMSKey"] = None,
        default_storage_class: Optional[
            "capo_storage_gateway.types.storage_class.StorageClass"
        ] = None,
        object_acl: Optional["capo_storage_gateway.types.object_acl.ObjectACL"] = None,
        read_only: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        guess_mime_type_enabled: Optional[
            "capo_storage_gateway.types.boolean.Boolean"
        ] = None,
        requester_pays: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        smbacl_enabled: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
        access_based_enumeration: Optional[
            "capo_storage_gateway.types.boolean.Boolean"
        ] = None,
        admin_user_list: Optional[
            "capo_storage_gateway.types.user_list.UserList"
        ] = None,
        valid_user_list: Optional[
            "capo_storage_gateway.types.user_list.UserList"
        ] = None,
        invalid_user_list: Optional[
            "capo_storage_gateway.types.user_list.UserList"
        ] = None,
        audit_destination_arn: Optional[
            "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
        ] = None,
        case_sensitivity: Optional[
            "capo_storage_gateway.types.case_sensitivity.CaseSensitivity"
        ] = None,
        file_share_name: Optional[
            "capo_storage_gateway.types.file_share_name.FileShareName"
        ] = None,
        cache_attributes: Optional[
            "capo_storage_gateway.types.cache_attributes.CacheAttributes"
        ] = None,
        notification_policy: Optional[
            "capo_storage_gateway.types.notification_policy.NotificationPolicy"
        ] = None,
        oplocks_enabled: Optional["capo_storage_gateway.types.boolean.Boolean"] = None,
    ) -> "capo_storage_gateway.types.update_smb_file_share_output.UpdateSMBFileShareOutput":
        r"""<p>Updates a Server Message Block (SMB) file share. This operation is only supported for S3 File Gateways.</p> <note> <p>To leave a file share field unchanged, set the corresponding input field to null.</p> </note> <important> <p>File gateways require Security Token Service (Amazon Web Services STS) to be activated to enable you to create a file share. Make sure that Amazon Web Services STS is activated in the Amazon Web Services Region you are creating your file gateway in. If Amazon Web Services STS is not activated in this Amazon Web Services Region, activate it. For information about how to activate Amazon Web Services STS, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html">Activating and deactivating Amazon Web Services STS in an Amazon Web Services Region</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>File gateways don't support creating hard or symbolic links on a file share.</p> </important>

        Args:
            file_share_arn: <p>The Amazon Resource Name (ARN) of the SMB file share that you want to update.</p>
            encryption_type: <p>A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note>
            kms_encrypted: <p>Optional. Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key (SSE-KMS), or <code>false</code> to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the <code>EncryptionType</code> parameter instead.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            kms_key: <p>Optional. The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value must be set if <code>KMSEncrypted</code> is <code>true</code>, or if <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>.</p>
            default_storage_class: <p>The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is <code>S3_STANDARD</code>. Optional.</p> <p>Valid Values: <code>S3_STANDARD</code> | <code>S3_INTELLIGENT_TIERING</code> | <code>S3_STANDARD_IA</code> | <code>S3_ONEZONE_IA</code> </p>
            object_acl: <p>A value that sets the access control list (ACL) permission for objects in the S3 bucket that a S3 File Gateway puts objects into. The default value is <code>private</code>.</p>
            read_only: <p>A value that sets the write status of a file share. Set this value to <code>true</code> to set write status to read-only, otherwise set to <code>false</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            guess_mime_type_enabled: <p>A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to <code>true</code> to enable MIME type guessing, otherwise set to <code>false</code>. The default value is <code>true</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            requester_pays: <p>A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to <code>true</code>, the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.</p> <note> <p> <code>RequesterPays</code> is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            smbacl_enabled: <p>Set this value to <code>true</code> to enable access control list (ACL) on the SMB file share. Set it to <code>false</code> to map file and directory permissions to the POSIX permissions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/filegateway/latest/files3/smb-acl.html">Using Windows ACLs to limit SMB file share access</a> in the <i>Amazon S3 File Gateway User Guide</i>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>
            access_based_enumeration: <p>The files and folders on this share will only be visible to users with read access.</p>
            admin_user_list: <p>A list of users or groups in the Active Directory that have administrator rights to the file share. A group must be prefixed with the @ character. Acceptable formats include: <code>DOMAIN\User1</code>, <code>user1</code>, <code>@group1</code>, and <code>@DOMAIN\group1</code>. Can only be set if Authentication is set to <code>ActiveDirectory</code>.</p>
            valid_user_list: <p>A list of users or groups in the Active Directory that are allowed to access the file share. A group must be prefixed with the @ character. Acceptable formats include: <code>DOMAIN\User1</code>, <code>user1</code>, <code>@group1</code>, and <code>@DOMAIN\group1</code>. Can only be set if Authentication is set to <code>ActiveDirectory</code>.</p>
            invalid_user_list: <p>A list of users or groups in the Active Directory that are not allowed to access the file share. A group must be prefixed with the @ character. Acceptable formats include: <code>DOMAIN\User1</code>, <code>user1</code>, <code>@group1</code>, and <code>@DOMAIN\group1</code>. Can only be set if Authentication is set to <code>ActiveDirectory</code>.</p>
            audit_destination_arn: <p>The Amazon Resource Name (ARN) of the storage used for audit logs.</p>
            case_sensitivity: <p>The case of an object name in an Amazon S3 bucket. For <code>ClientSpecified</code>, the client determines the case sensitivity. For <code>CaseSensitive</code>, the gateway determines the case sensitivity. The default value is <code>ClientSpecified</code>.</p>
            file_share_name: <p>The name of the file share. Optional.</p> <note> <p> <code>FileShareName</code> must be set if an S3 prefix name is set in <code>LocationARN</code>, or if an access point or access point alias is used.</p> <p>A valid SMB file share name cannot contain the following characters: <code>[</code>,<code>]</code>,<code>#</code>,<code>;</code>,<code><</code>,<code>></code>,<code>:</code>,<code>"</code>,<code>\</code>,<code>/</code>,<code>|</code>,<code>?</code>,<code>*</code>,<code>+</code>, or ASCII control characters <code>1-31</code>.</p> </note>
            cache_attributes: <p>Specifies refresh cache information for the file share.</p>
            notification_policy: <p>The notification policy of the file share. <code>SettlingTimeInSeconds</code> controls the number of seconds to wait after the last point in time a client wrote to a file before generating an <code>ObjectUploaded</code> notification. Because clients can make many small writes to files, it's best to set this parameter for as long as possible to avoid generating multiple notifications for the same file in a small time period.</p> <note> <p> <code>SettlingTimeInSeconds</code> has no effect on the timing of the object uploading to Amazon S3, only the timing of the notification.</p> <p>This setting is not meant to specify an exact time at which the notification will be sent. In some cases, the gateway might require more than the specified delay time to generate and send notifications.</p> </note> <p>The following example sets <code>NotificationPolicy</code> on with <code>SettlingTimeInSeconds</code> set to 60.</p> <p> <code>{\"Upload\": {\"SettlingTimeInSeconds\": 60}}</code> </p> <p>The following example sets <code>NotificationPolicy</code> off.</p> <p> <code>{}</code> </p>
            oplocks_enabled: <p>Specifies whether opportunistic locking is enabled for the SMB file share.</p> <note> <p>Enabling opportunistic locking on case-sensitive shares is not recommended for workloads that involve access to files with the same name in different case.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_smb_file_share_input.UpdateSMBFileShareInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_smb_file_share_output.UpdateSMBFileShareOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_smb_file_share

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_smb_file_share.update_smb_file_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_smb_file_share_input.UpdateSMBFileShareInput = {
            "file_share_arn": file_share_arn
        }
        if encryption_type is not None:
            input_["encryption_type"] = encryption_type
        if kms_encrypted is not None:
            input_["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if default_storage_class is not None:
            input_["default_storage_class"] = default_storage_class
        if object_acl is not None:
            input_["object_acl"] = object_acl
        if read_only is not None:
            input_["read_only"] = read_only
        if guess_mime_type_enabled is not None:
            input_["guess_mime_type_enabled"] = guess_mime_type_enabled
        if requester_pays is not None:
            input_["requester_pays"] = requester_pays
        if smbacl_enabled is not None:
            input_["smbacl_enabled"] = smbacl_enabled
        if access_based_enumeration is not None:
            input_["access_based_enumeration"] = access_based_enumeration
        if admin_user_list is not None:
            input_["admin_user_list"] = admin_user_list
        if valid_user_list is not None:
            input_["valid_user_list"] = valid_user_list
        if invalid_user_list is not None:
            input_["invalid_user_list"] = invalid_user_list
        if audit_destination_arn is not None:
            input_["audit_destination_arn"] = audit_destination_arn
        if case_sensitivity is not None:
            input_["case_sensitivity"] = case_sensitivity
        if file_share_name is not None:
            input_["file_share_name"] = file_share_name
        if cache_attributes is not None:
            input_["cache_attributes"] = cache_attributes
        if notification_policy is not None:
            input_["notification_policy"] = notification_policy
        if oplocks_enabled is not None:
            input_["oplocks_enabled"] = oplocks_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_smb_file_share_visibility(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        file_shares_visible: "capo_storage_gateway.types.boolean.Boolean",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.update_smb_file_share_visibility_output.UpdateSMBFileShareVisibilityOutput":
        """<p>Controls whether the shares on an S3 File Gateway are visible in a net view or browse list. The operation is only supported for S3 File Gateways.</p>

        Args:
            file_shares_visible: <p>The shares on this gateway appear when listing shares.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_smb_file_share_visibility_input.UpdateSMBFileShareVisibilityInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_smb_file_share_visibility_output.UpdateSMBFileShareVisibilityOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_smb_file_share_visibility

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_smb_file_share_visibility.update_smb_file_share_visibility(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_smb_file_share_visibility_input.UpdateSMBFileShareVisibilityInput = {
            "gateway_arn": gateway_arn,
            "file_shares_visible": file_shares_visible,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_smb_local_groups(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        smb_local_groups: "capo_storage_gateway.types.smb_local_groups.SMBLocalGroups",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.update_smb_local_groups_output.UpdateSMBLocalGroupsOutput":
        """<p>Updates the list of Active Directory users and groups that have special permissions for SMB file shares on the gateway.</p>

        Args:
            smb_local_groups: <p>A list of Active Directory users and groups that you want to grant special permissions for SMB file shares on the gateway.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_smb_local_groups_input.UpdateSMBLocalGroupsInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_smb_local_groups_output.UpdateSMBLocalGroupsOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_smb_local_groups

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_smb_local_groups.update_smb_local_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_smb_local_groups_input.UpdateSMBLocalGroupsInput = {
            "gateway_arn": gateway_arn,
            "smb_local_groups": smb_local_groups,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_smb_security_strategy(
        self,
        gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN",
        smb_security_strategy: "capo_storage_gateway.types.smb_security_strategy.SMBSecurityStrategy",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.update_smb_security_strategy_output.UpdateSMBSecurityStrategyOutput":
        """<p>Updates the SMB security strategy level for an Amazon S3 file gateway. This action is only supported for Amazon S3 file gateways.</p> <note> <p>For information about configuring this setting using the Amazon Web Services console, see <a href="https://docs.aws.amazon.com/filegateway/latest/files3/security-strategy.html">Setting a security level for your gateway</a> in the <i>Amazon S3 File Gateway User Guide</i>.</p> <p>A higher security strategy level can affect performance of the gateway.</p> </note>

        Args:
            smb_security_strategy: <p>Specifies the type of security strategy.</p> <p> <code>ClientSpecified</code>: If you choose this option, requests are established based on what is negotiated by the client. This option is recommended when you want to maximize compatibility across different clients in your environment. Supported only for S3 File Gateway.</p> <p> <code>MandatorySigning</code>: If you choose this option, File Gateway only allows connections from SMBv2 or SMBv3 clients that have signing enabled. This option works with SMB clients on Microsoft Windows Vista, Windows Server 2008 or newer.</p> <p> <code>MandatoryEncryption</code>: If you choose this option, File Gateway only allows connections from SMBv3 clients that have encryption enabled. This option is recommended for environments that handle sensitive data. This option works with SMB clients on Microsoft Windows 8, Windows Server 2012 or newer.</p> <p> <code>MandatoryEncryptionNoAes128</code>: If you choose this option, File Gateway only allows connections from SMBv3 clients that use 256-bit AES encryption algorithms. 128-bit algorithms are not allowed. This option is recommended for environments that handle sensitive data. It works with SMB clients on Microsoft Windows 8, Windows Server 2012, or later.</p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_smb_security_strategy_input.UpdateSMBSecurityStrategyInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_smb_security_strategy_output.UpdateSMBSecurityStrategyOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_smb_security_strategy

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_smb_security_strategy.update_smb_security_strategy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_smb_security_strategy_input.UpdateSMBSecurityStrategyInput = {
            "gateway_arn": gateway_arn,
            "smb_security_strategy": smb_security_strategy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_snapshot_schedule(
        self,
        volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN",
        start_at: "capo_storage_gateway.types.hour_of_day.HourOfDay",
        recurrence_in_hours: "capo_storage_gateway.types.recurrence_in_hours.RecurrenceInHours",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
        description: Optional[
            "capo_storage_gateway.types.description.Description"
        ] = None,
        tags: Optional["capo_storage_gateway.types.tags.Tags"] = None,
    ) -> "capo_storage_gateway.types.update_snapshot_schedule_output.UpdateSnapshotScheduleOutput":
        """<p>Updates a snapshot schedule configured for a gateway volume. This operation is only supported in the cached volume and stored volume gateway types.</p> <p>The default snapshot schedule for volume is once every 24 hours, starting at the creation time of the volume. You can use this API to change the snapshot schedule configured for the volume.</p> <p>In the request you must identify the gateway volume whose snapshot schedule you want to update, and the schedule information, including when you want the snapshot to begin on a day and the frequency (in hours) of snapshots.</p>

        Args:
            volume_arn: <p>The Amazon Resource Name (ARN) of the volume. Use the <a>ListVolumes</a> operation to return a list of gateway volumes.</p>
            start_at: <p>The hour of the day at which the snapshot schedule begins represented as <i>hh</i>, where <i>hh</i> is the hour (0 to 23). The hour of the day is in the time zone of the gateway.</p>
            recurrence_in_hours: <p>Frequency of snapshots. Specify the number of hours between snapshots.</p>
            description: <p>Optional description of the snapshot that overwrites the existing description.</p>
            tags: <p>A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a volume snapshot schedule
            Updates a snapshot schedule configured for a gateway volume.

            >>> client.update_snapshot_schedule(volume_arn='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB', start_at=0, recurrence_in_hours=1, description='Hourly snapshot')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_snapshot_schedule_input.UpdateSnapshotScheduleInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_snapshot_schedule_output.UpdateSnapshotScheduleOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_snapshot_schedule

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_snapshot_schedule.update_snapshot_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_snapshot_schedule_input.UpdateSnapshotScheduleInput = {
            "volume_arn": volume_arn,
            "start_at": start_at,
            "recurrence_in_hours": recurrence_in_hours,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_vtl_device_type(
        self,
        vtl_device_arn: "capo_storage_gateway.types.vtl_device_arn.VTLDeviceARN",
        device_type: "capo_storage_gateway.types.device_type.DeviceType",
        *,
        config_overrides: Optional[StorageGatewayClientConfig] = None,
    ) -> "capo_storage_gateway.types.update_vtl_device_type_output.UpdateVTLDeviceTypeOutput":
        """<p>Updates the type of medium changer in a tape gateway. When you activate a tape gateway, you select a medium changer type for the tape gateway. This operation enables you to select a different type of medium changer after a tape gateway is activated. This operation is only supported in the tape gateway type.</p>

        Args:
            vtl_device_arn: <p>The Amazon Resource Name (ARN) of the medium changer you want to select.</p>
            device_type: <p>The type of medium changer you want to select.</p> <p>Valid Values: <code>STK-L700</code> | <code>AWS-Gateway-VTL</code> | <code>IBM-03584L32-0402</code> </p>

        Raises:
            capo_storage_gateway.errors.internal_server_error.InternalServerError: <p>An internal server error has occurred during the request. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException: <p>An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.</p>
            capo_storage_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a VTL device type
            Updates the type of medium changer in a gateway-VTL after a gateway-VTL is activated.

            >>> client.update_vtl_device_type(vtl_device_arn='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B/device/AMZN_SGW-1FAD4876_MEDIACHANGER_00001', device_type='Medium Changer')
        """

        def _handler(
            req: "OperationRequest[capo_storage_gateway.types.update_vtl_device_type_input.UpdateVTLDeviceTypeInput]",
        ) -> OperationResponse[
            "capo_storage_gateway.types.update_vtl_device_type_output.UpdateVTLDeviceTypeOutput"
        ]:
            import capo_storage_gateway._operations.storage_gateway_20130630.update_vtl_device_type

            output, http_response = (
                capo_storage_gateway._operations.storage_gateway_20130630.update_vtl_device_type.update_vtl_device_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_storage_gateway.types.update_vtl_device_type_input.UpdateVTLDeviceTypeInput = {
            "vtl_device_arn": vtl_device_arn,
            "device_type": device_type,
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
