from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_odb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_odb.types.cloud_vm_cluster_summary
    import capo_odb.types.cluster_name
    import capo_odb.types.create_cloud_vm_cluster_input
    import capo_odb.types.create_cloud_vm_cluster_output
    import capo_odb.types.data_collection_options
    import capo_odb.types.delete_cloud_vm_cluster_input
    import capo_odb.types.delete_cloud_vm_cluster_output
    import capo_odb.types.general_input_string
    import capo_odb.types.get_cloud_vm_cluster_input
    import capo_odb.types.get_cloud_vm_cluster_output
    import capo_odb.types.hostname
    import capo_odb.types.license_model
    import capo_odb.types.list_cloud_vm_clusters_input
    import capo_odb.types.list_cloud_vm_clusters_output
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.string_list
    from capo_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from capo_odb._services.odb import odbClient, odbClientConfig


class CloudVmClusterResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def create(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        cpu_core_count: int,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        gi_version: str,
        hostname: "capo_odb.types.hostname.Hostname",
        ssh_public_keys: "capo_odb.types.string_list.StringList",
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        cluster_name: Optional["capo_odb.types.cluster_name.ClusterName"] = None,
        data_collection_options: Optional[
            "capo_odb.types.data_collection_options.DataCollectionOptions"
        ] = None,
        data_storage_size_in_t_bs: Optional[float] = None,
        db_node_storage_size_in_g_bs: Optional[int] = None,
        db_servers: Optional["capo_odb.types.string_list.StringList"] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        is_local_backup_enabled: Optional[bool] = None,
        is_sparse_diskgroup_enabled: Optional[bool] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        memory_size_in_g_bs: Optional[int] = None,
        system_version: Optional[str] = None,
        time_zone: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        scan_listener_port_tcp: Optional[int] = None,
    ) -> "capo_odb.types.create_cloud_vm_cluster_output.CreateCloudVmClusterOutput":
        """<p>Creates a VM cluster on the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure for this VM cluster.</p>
            cpu_core_count: <p>The number of CPU cores to enable on the VM cluster.</p>
            display_name: <p>A user-friendly name for the VM cluster.</p>
            gi_version: <p>A valid software version of Oracle Grid Infrastructure (GI). To get the list of valid values, use the <code>ListGiVersions</code> operation and specify the shape of the Exadata infrastructure.</p> <p>Example: <code>19.0.0.0</code> </p>
            hostname: <p>The host name for the VM cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be "localhost" or "hostname".</p> </li> <li> <p>Can't contain "-version".</p> </li> <li> <p>The maximum length of the combined hostname and domain is 63 characters.</p> </li> <li> <p>The hostname must be unique within the subnet.</p> </li> </ul>
            ssh_public_keys: <p>The public key portion of one or more key pairs used for SSH access to the VM cluster.</p>
            odb_network_id: <p>The unique identifier of the ODB network for the VM cluster.</p>
            cluster_name: <p>A name for the Grid Infrastructure cluster. The name isn't case sensitive.</p>
            data_collection_options: <p>The set of preferences for the various diagnostic collection options for the VM cluster.</p>
            data_storage_size_in_t_bs: <p>The size of the data disk group, in terabytes (TBs), to allocate for the VM cluster.</p>
            db_node_storage_size_in_g_bs: <p>The amount of local node storage, in gigabytes (GB), to allocate for the VM cluster.</p>
            db_servers: <p>The list of database servers for the VM cluster.</p>
            tags: <p>The list of resource tags to apply to the VM cluster.</p>
            is_local_backup_enabled: <p>Specifies whether to enable database backups to local Exadata storage for the VM cluster.</p>
            is_sparse_diskgroup_enabled: <p>Specifies whether to create a sparse disk group for the VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the VM cluster.</p> <p>Default: <code>LICENSE_INCLUDED</code> </p>
            memory_size_in_g_bs: <p>The amount of memory, in gigabytes (GB), to allocate for the VM cluster.</p>
            system_version: <p>The version of the operating system of the image for the VM cluster.</p>
            time_zone: <p>The time zone for the VM cluster. For a list of valid values for time zone, you can check the options in the console.</p> <p>Default: UTC</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>
            scan_listener_port_tcp: <p>The port number for TCP connections to the single client access name (SCAN) listener. </p> <p>Valid values: <code>1024–8999</code> with the following exceptions: <code>2484</code>, <code>6100</code>, <code>6200</code>, <code>7060</code>, <code>7070</code>, <code>7085</code>, and <code>7879</code> </p> <p>Default: <code>1521</code> </p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.create_cloud_vm_cluster_input.CreateCloudVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.create_cloud_vm_cluster_output.CreateCloudVmClusterOutput"
        ]:
            import capo_odb._operations.odb.create_cloud_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.create_cloud_vm_cluster.create_cloud_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_odb.types.create_cloud_vm_cluster_input.CreateCloudVmClusterInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id,
            "cpu_core_count": cpu_core_count,
            "display_name": display_name,
            "gi_version": gi_version,
            "hostname": hostname,
            "ssh_public_keys": ssh_public_keys,
            "odb_network_id": odb_network_id,
        }
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if data_collection_options is not None:
            input_["data_collection_options"] = data_collection_options
        if data_storage_size_in_t_bs is not None:
            input_["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if db_node_storage_size_in_g_bs is not None:
            input_["db_node_storage_size_in_g_bs"] = db_node_storage_size_in_g_bs
        if db_servers is not None:
            input_["db_servers"] = db_servers
        if tags is not None:
            input_["tags"] = tags
        if is_local_backup_enabled is not None:
            input_["is_local_backup_enabled"] = is_local_backup_enabled
        if is_sparse_diskgroup_enabled is not None:
            input_["is_sparse_diskgroup_enabled"] = is_sparse_diskgroup_enabled
        if license_model is not None:
            input_["license_model"] = license_model
        if memory_size_in_g_bs is not None:
            input_["memory_size_in_g_bs"] = memory_size_in_g_bs
        if system_version is not None:
            input_["system_version"] = system_version
        if time_zone is not None:
            input_["time_zone"] = time_zone
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if scan_listener_port_tcp is not None:
            input_["scan_listener_port_tcp"] = scan_listener_port_tcp

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.get_cloud_vm_cluster_output.GetCloudVmClusterOutput":
        """<p>Returns information about the specified VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.get_cloud_vm_cluster_input.GetCloudVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.get_cloud_vm_cluster_output.GetCloudVmClusterOutput"
        ]:
            import capo_odb._operations.odb.get_cloud_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.get_cloud_vm_cluster.get_cloud_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_odb.types.get_cloud_vm_cluster_input.GetCloudVmClusterInput = {
            "cloud_vm_cluster_id": cloud_vm_cluster_id
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
        cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.delete_cloud_vm_cluster_output.DeleteCloudVmClusterOutput":
        """<p>Deletes the specified VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.delete_cloud_vm_cluster_input.DeleteCloudVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.delete_cloud_vm_cluster_output.DeleteCloudVmClusterOutput"
        ]:
            import capo_odb._operations.odb.delete_cloud_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.delete_cloud_vm_cluster.delete_cloud_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_odb.types.delete_cloud_vm_cluster_input.DeleteCloudVmClusterInput = {
            "cloud_vm_cluster_id": cloud_vm_cluster_id
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
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_exadata_infrastructure_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "capo_odb.types.list_cloud_vm_clusters_output.ListCloudVmClustersOutput":
        """<p>Returns information about the VM clusters owned by your Amazon Web Services account or only the ones on the specified Exadata infrastructure.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Oracle Exadata infrastructure.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_cloud_vm_clusters_input.ListCloudVmClustersInput]",
        ) -> OperationResponse[
            "capo_odb.types.list_cloud_vm_clusters_output.ListCloudVmClustersOutput"
        ]:
            import capo_odb._operations.odb.list_cloud_vm_clusters

            output, http_response = (
                capo_odb._operations.odb.list_cloud_vm_clusters.list_cloud_vm_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_odb.types.list_cloud_vm_clusters_input.ListCloudVmClustersInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if cloud_exadata_infrastructure_id is not None:
            input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCloudVmClusterResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def create(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        cpu_core_count: int,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        gi_version: str,
        hostname: "capo_odb.types.hostname.Hostname",
        ssh_public_keys: "capo_odb.types.string_list.StringList",
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cluster_name: Optional["capo_odb.types.cluster_name.ClusterName"] = None,
        data_collection_options: Optional[
            "capo_odb.types.data_collection_options.DataCollectionOptions"
        ] = None,
        data_storage_size_in_t_bs: Optional[float] = None,
        db_node_storage_size_in_g_bs: Optional[int] = None,
        db_servers: Optional["capo_odb.types.string_list.StringList"] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        is_local_backup_enabled: Optional[bool] = None,
        is_sparse_diskgroup_enabled: Optional[bool] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        memory_size_in_g_bs: Optional[int] = None,
        system_version: Optional[str] = None,
        time_zone: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        scan_listener_port_tcp: Optional[int] = None,
    ) -> "capo_odb.types.create_cloud_vm_cluster_output.CreateCloudVmClusterOutput":
        """<p>Creates a VM cluster on the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure for this VM cluster.</p>
            cpu_core_count: <p>The number of CPU cores to enable on the VM cluster.</p>
            display_name: <p>A user-friendly name for the VM cluster.</p>
            gi_version: <p>A valid software version of Oracle Grid Infrastructure (GI). To get the list of valid values, use the <code>ListGiVersions</code> operation and specify the shape of the Exadata infrastructure.</p> <p>Example: <code>19.0.0.0</code> </p>
            hostname: <p>The host name for the VM cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be "localhost" or "hostname".</p> </li> <li> <p>Can't contain "-version".</p> </li> <li> <p>The maximum length of the combined hostname and domain is 63 characters.</p> </li> <li> <p>The hostname must be unique within the subnet.</p> </li> </ul>
            ssh_public_keys: <p>The public key portion of one or more key pairs used for SSH access to the VM cluster.</p>
            odb_network_id: <p>The unique identifier of the ODB network for the VM cluster.</p>
            cluster_name: <p>A name for the Grid Infrastructure cluster. The name isn't case sensitive.</p>
            data_collection_options: <p>The set of preferences for the various diagnostic collection options for the VM cluster.</p>
            data_storage_size_in_t_bs: <p>The size of the data disk group, in terabytes (TBs), to allocate for the VM cluster.</p>
            db_node_storage_size_in_g_bs: <p>The amount of local node storage, in gigabytes (GB), to allocate for the VM cluster.</p>
            db_servers: <p>The list of database servers for the VM cluster.</p>
            tags: <p>The list of resource tags to apply to the VM cluster.</p>
            is_local_backup_enabled: <p>Specifies whether to enable database backups to local Exadata storage for the VM cluster.</p>
            is_sparse_diskgroup_enabled: <p>Specifies whether to create a sparse disk group for the VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the VM cluster.</p> <p>Default: <code>LICENSE_INCLUDED</code> </p>
            memory_size_in_g_bs: <p>The amount of memory, in gigabytes (GB), to allocate for the VM cluster.</p>
            system_version: <p>The version of the operating system of the image for the VM cluster.</p>
            time_zone: <p>The time zone for the VM cluster. For a list of valid values for time zone, you can check the options in the console.</p> <p>Default: UTC</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>
            scan_listener_port_tcp: <p>The port number for TCP connections to the single client access name (SCAN) listener. </p> <p>Valid values: <code>1024–8999</code> with the following exceptions: <code>2484</code>, <code>6100</code>, <code>6200</code>, <code>7060</code>, <code>7070</code>, <code>7085</code>, and <code>7879</code> </p> <p>Default: <code>1521</code> </p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_cloud_vm_cluster_input.CreateCloudVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_cloud_vm_cluster_output.CreateCloudVmClusterOutput"
        ]:
            import capo_odb._operations.odb.create_cloud_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_cloud_vm_cluster.async_create_cloud_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_odb.types.create_cloud_vm_cluster_input.CreateCloudVmClusterInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id,
            "cpu_core_count": cpu_core_count,
            "display_name": display_name,
            "gi_version": gi_version,
            "hostname": hostname,
            "ssh_public_keys": ssh_public_keys,
            "odb_network_id": odb_network_id,
        }
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if data_collection_options is not None:
            input_["data_collection_options"] = data_collection_options
        if data_storage_size_in_t_bs is not None:
            input_["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if db_node_storage_size_in_g_bs is not None:
            input_["db_node_storage_size_in_g_bs"] = db_node_storage_size_in_g_bs
        if db_servers is not None:
            input_["db_servers"] = db_servers
        if tags is not None:
            input_["tags"] = tags
        if is_local_backup_enabled is not None:
            input_["is_local_backup_enabled"] = is_local_backup_enabled
        if is_sparse_diskgroup_enabled is not None:
            input_["is_sparse_diskgroup_enabled"] = is_sparse_diskgroup_enabled
        if license_model is not None:
            input_["license_model"] = license_model
        if memory_size_in_g_bs is not None:
            input_["memory_size_in_g_bs"] = memory_size_in_g_bs
        if system_version is not None:
            input_["system_version"] = system_version
        if time_zone is not None:
            input_["time_zone"] = time_zone
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if scan_listener_port_tcp is not None:
            input_["scan_listener_port_tcp"] = scan_listener_port_tcp

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_cloud_vm_cluster_output.GetCloudVmClusterOutput":
        """<p>Returns information about the specified VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_cloud_vm_cluster_input.GetCloudVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_cloud_vm_cluster_output.GetCloudVmClusterOutput"
        ]:
            import capo_odb._operations.odb.get_cloud_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_cloud_vm_cluster.async_get_cloud_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_odb.types.get_cloud_vm_cluster_input.GetCloudVmClusterInput = {
            "cloud_vm_cluster_id": cloud_vm_cluster_id
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
        cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_cloud_vm_cluster_output.DeleteCloudVmClusterOutput":
        """<p>Deletes the specified VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_cloud_vm_cluster_input.DeleteCloudVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_cloud_vm_cluster_output.DeleteCloudVmClusterOutput"
        ]:
            import capo_odb._operations.odb.delete_cloud_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_cloud_vm_cluster.async_delete_cloud_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_odb.types.delete_cloud_vm_cluster_input.DeleteCloudVmClusterInput = {
            "cloud_vm_cluster_id": cloud_vm_cluster_id
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
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_exadata_infrastructure_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "capo_odb.types.list_cloud_vm_clusters_output.ListCloudVmClustersOutput":
        """<p>Returns information about the VM clusters owned by your Amazon Web Services account or only the ones on the specified Exadata infrastructure.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Oracle Exadata infrastructure.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_cloud_vm_clusters_input.ListCloudVmClustersInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_cloud_vm_clusters_output.ListCloudVmClustersOutput"
        ]:
            import capo_odb._operations.odb.list_cloud_vm_clusters

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_cloud_vm_clusters.async_list_cloud_vm_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_odb.types.list_cloud_vm_clusters_input.ListCloudVmClustersInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if cloud_exadata_infrastructure_id is not None:
            input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
