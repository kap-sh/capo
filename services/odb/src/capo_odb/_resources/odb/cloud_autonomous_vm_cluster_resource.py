from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_odb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_odb.types.autonomous_virtual_machine_summary
    import capo_odb.types.cloud_autonomous_vm_cluster_summary
    import capo_odb.types.create_cloud_autonomous_vm_cluster_input
    import capo_odb.types.create_cloud_autonomous_vm_cluster_output
    import capo_odb.types.delete_cloud_autonomous_vm_cluster_input
    import capo_odb.types.delete_cloud_autonomous_vm_cluster_output
    import capo_odb.types.general_input_string
    import capo_odb.types.get_cloud_autonomous_vm_cluster_input
    import capo_odb.types.get_cloud_autonomous_vm_cluster_output
    import capo_odb.types.license_model
    import capo_odb.types.list_autonomous_virtual_machines_input
    import capo_odb.types.list_autonomous_virtual_machines_output
    import capo_odb.types.list_cloud_autonomous_vm_clusters_input
    import capo_odb.types.list_cloud_autonomous_vm_clusters_output
    import capo_odb.types.maintenance_window
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.string_list
    from capo_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from capo_odb._services.odb import odbClient, odbClientConfig


class CloudAutonomousVmClusterResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def create(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        autonomous_data_storage_size_in_t_bs: float,
        cpu_core_count_per_node: int,
        memory_per_oracle_compute_unit_in_g_bs: int,
        total_container_databases: int,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        db_servers: Optional["capo_odb.types.string_list.StringList"] = None,
        description: Optional[str] = None,
        is_mtls_enabled_vm_cluster: Optional[bool] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        maintenance_window: Optional[
            "capo_odb.types.maintenance_window.MaintenanceWindow"
        ] = None,
        scan_listener_port_non_tls: Optional[int] = None,
        scan_listener_port_tls: Optional[int] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        time_zone: Optional[str] = None,
    ) -> "capo_odb.types.create_cloud_autonomous_vm_cluster_output.CreateCloudAutonomousVmClusterOutput":
        """<p>Creates a new Autonomous VM cluster in the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure where the VM cluster will be created.</p>
            odb_network_id: <p>The unique identifier of the ODB network to be used for the VM cluster.</p>
            display_name: <p>The display name for the Autonomous VM cluster. The name does not need to be unique.</p>
            client_token: <p>A client-provided token to ensure idempotency of the request.</p>
            autonomous_data_storage_size_in_t_bs: <p>The data disk group size to be allocated for Autonomous Databases, in terabytes (TB).</p>
            cpu_core_count_per_node: <p>The number of CPU cores to be enabled per VM cluster node.</p>
            db_servers: <p>The list of database servers to be used for the Autonomous VM cluster.</p>
            description: <p>A user-provided description of the Autonomous VM cluster.</p>
            is_mtls_enabled_vm_cluster: <p>Specifies whether to enable mutual TLS (mTLS) authentication for the Autonomous VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the Autonomous VM cluster.</p>
            maintenance_window: <p>The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.</p>
            memory_per_oracle_compute_unit_in_g_bs: <p>The amount of memory to be allocated per OCPU, in GB.</p>
            scan_listener_port_non_tls: <p>The SCAN listener port for non-TLS (TCP) protocol.</p>
            scan_listener_port_tls: <p>The SCAN listener port for TLS (TCP) protocol.</p>
            tags: <p>Free-form tags for this resource. Each tag is a key-value pair with no predefined name, type, or namespace.</p>
            time_zone: <p>The time zone to use for the Autonomous VM cluster.</p>
            total_container_databases: <p>The total number of Autonomous CDBs that you can create in the Autonomous VM cluster.</p>

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
            req: "OperationRequest[capo_odb.types.create_cloud_autonomous_vm_cluster_input.CreateCloudAutonomousVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.create_cloud_autonomous_vm_cluster_output.CreateCloudAutonomousVmClusterOutput"
        ]:
            import capo_odb._operations.odb.create_cloud_autonomous_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.create_cloud_autonomous_vm_cluster.create_cloud_autonomous_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCloudAutonomousVmCluster")
        )
        input_: capo_odb.types.create_cloud_autonomous_vm_cluster_input.CreateCloudAutonomousVmClusterInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id,
            "odb_network_id": odb_network_id,
            "display_name": display_name,
            "autonomous_data_storage_size_in_t_bs": autonomous_data_storage_size_in_t_bs,
            "cpu_core_count_per_node": cpu_core_count_per_node,
            "memory_per_oracle_compute_unit_in_g_bs": memory_per_oracle_compute_unit_in_g_bs,
            "total_container_databases": total_container_databases,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if db_servers is not None:
            input_["db_servers"] = db_servers
        if description is not None:
            input_["description"] = description
        if is_mtls_enabled_vm_cluster is not None:
            input_["is_mtls_enabled_vm_cluster"] = is_mtls_enabled_vm_cluster
        if license_model is not None:
            input_["license_model"] = license_model
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        if scan_listener_port_non_tls is not None:
            input_["scan_listener_port_non_tls"] = scan_listener_port_non_tls
        if scan_listener_port_tls is not None:
            input_["scan_listener_port_tls"] = scan_listener_port_tls
        if tags is not None:
            input_["tags"] = tags
        if time_zone is not None:
            input_["time_zone"] = time_zone

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.get_cloud_autonomous_vm_cluster_output.GetCloudAutonomousVmClusterOutput":
        """<p>Gets information about a specific Autonomous VM cluster.</p>

        Args:
            cloud_autonomous_vm_cluster_id: <p>The unique identifier of the Autonomous VM cluster to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.get_cloud_autonomous_vm_cluster_input.GetCloudAutonomousVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.get_cloud_autonomous_vm_cluster_output.GetCloudAutonomousVmClusterOutput"
        ]:
            import capo_odb._operations.odb.get_cloud_autonomous_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.get_cloud_autonomous_vm_cluster.get_cloud_autonomous_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCloudAutonomousVmCluster")
        )
        input_: capo_odb.types.get_cloud_autonomous_vm_cluster_input.GetCloudAutonomousVmClusterInput = {
            "cloud_autonomous_vm_cluster_id": cloud_autonomous_vm_cluster_id
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
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.delete_cloud_autonomous_vm_cluster_output.DeleteCloudAutonomousVmClusterOutput":
        """<p>Deletes an Autonomous VM cluster.</p>

        Args:
            cloud_autonomous_vm_cluster_id: <p>The unique identifier of the Autonomous VM cluster to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.delete_cloud_autonomous_vm_cluster_input.DeleteCloudAutonomousVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.delete_cloud_autonomous_vm_cluster_output.DeleteCloudAutonomousVmClusterOutput"
        ]:
            import capo_odb._operations.odb.delete_cloud_autonomous_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.delete_cloud_autonomous_vm_cluster.delete_cloud_autonomous_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCloudAutonomousVmCluster")
        )
        input_: capo_odb.types.delete_cloud_autonomous_vm_cluster_input.DeleteCloudAutonomousVmClusterInput = {
            "cloud_autonomous_vm_cluster_id": cloud_autonomous_vm_cluster_id
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
    ) -> "capo_odb.types.list_cloud_autonomous_vm_clusters_output.ListCloudAutonomousVmClustersOutput":
        """<p>Lists all Autonomous VM clusters in a specified Cloud Exadata infrastructure.</p>

        Args:
            max_results: <p>The maximum number of items to return per page.</p>
            next_token: <p>The pagination token to continue listing from.</p>
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Cloud Exadata Infrastructure that hosts the Autonomous VM clusters to be listed.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_cloud_autonomous_vm_clusters_input.ListCloudAutonomousVmClustersInput]",
        ) -> OperationResponse[
            "capo_odb.types.list_cloud_autonomous_vm_clusters_output.ListCloudAutonomousVmClustersOutput"
        ]:
            import capo_odb._operations.odb.list_cloud_autonomous_vm_clusters

            output, http_response = (
                capo_odb._operations.odb.list_cloud_autonomous_vm_clusters.list_cloud_autonomous_vm_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCloudAutonomousVmClusters")
        )
        input_: capo_odb.types.list_cloud_autonomous_vm_clusters_input.ListCloudAutonomousVmClustersInput = {}
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

    def list_autonomous_virtual_machines(
        self,
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_autonomous_virtual_machines_output.ListAutonomousVirtualMachinesOutput":
        """<p>Lists all Autonomous VMs in an Autonomous VM cluster.</p>

        Args:
            max_results: <p>The maximum number of items to return per page.</p>
            next_token: <p>The pagination token to continue listing from.</p>
            cloud_autonomous_vm_cluster_id: <p>The unique identifier of the Autonomous VM cluster whose virtual machines you're listing.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_autonomous_virtual_machines_input.ListAutonomousVirtualMachinesInput]",
        ) -> OperationResponse[
            "capo_odb.types.list_autonomous_virtual_machines_output.ListAutonomousVirtualMachinesOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_virtual_machines

            output, http_response = (
                capo_odb._operations.odb.list_autonomous_virtual_machines.list_autonomous_virtual_machines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAutonomousVirtualMachines")
        )
        input_: capo_odb.types.list_autonomous_virtual_machines_input.ListAutonomousVirtualMachinesInput = {
            "cloud_autonomous_vm_cluster_id": cloud_autonomous_vm_cluster_id
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


class AsyncCloudAutonomousVmClusterResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def create(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        autonomous_data_storage_size_in_t_bs: float,
        cpu_core_count_per_node: int,
        memory_per_oracle_compute_unit_in_g_bs: int,
        total_container_databases: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        db_servers: Optional["capo_odb.types.string_list.StringList"] = None,
        description: Optional[str] = None,
        is_mtls_enabled_vm_cluster: Optional[bool] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        maintenance_window: Optional[
            "capo_odb.types.maintenance_window.MaintenanceWindow"
        ] = None,
        scan_listener_port_non_tls: Optional[int] = None,
        scan_listener_port_tls: Optional[int] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        time_zone: Optional[str] = None,
    ) -> "capo_odb.types.create_cloud_autonomous_vm_cluster_output.CreateCloudAutonomousVmClusterOutput":
        """<p>Creates a new Autonomous VM cluster in the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure where the VM cluster will be created.</p>
            odb_network_id: <p>The unique identifier of the ODB network to be used for the VM cluster.</p>
            display_name: <p>The display name for the Autonomous VM cluster. The name does not need to be unique.</p>
            client_token: <p>A client-provided token to ensure idempotency of the request.</p>
            autonomous_data_storage_size_in_t_bs: <p>The data disk group size to be allocated for Autonomous Databases, in terabytes (TB).</p>
            cpu_core_count_per_node: <p>The number of CPU cores to be enabled per VM cluster node.</p>
            db_servers: <p>The list of database servers to be used for the Autonomous VM cluster.</p>
            description: <p>A user-provided description of the Autonomous VM cluster.</p>
            is_mtls_enabled_vm_cluster: <p>Specifies whether to enable mutual TLS (mTLS) authentication for the Autonomous VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the Autonomous VM cluster.</p>
            maintenance_window: <p>The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.</p>
            memory_per_oracle_compute_unit_in_g_bs: <p>The amount of memory to be allocated per OCPU, in GB.</p>
            scan_listener_port_non_tls: <p>The SCAN listener port for non-TLS (TCP) protocol.</p>
            scan_listener_port_tls: <p>The SCAN listener port for TLS (TCP) protocol.</p>
            tags: <p>Free-form tags for this resource. Each tag is a key-value pair with no predefined name, type, or namespace.</p>
            time_zone: <p>The time zone to use for the Autonomous VM cluster.</p>
            total_container_databases: <p>The total number of Autonomous CDBs that you can create in the Autonomous VM cluster.</p>

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
            req: "AsyncOperationRequest[capo_odb.types.create_cloud_autonomous_vm_cluster_input.CreateCloudAutonomousVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_cloud_autonomous_vm_cluster_output.CreateCloudAutonomousVmClusterOutput"
        ]:
            import capo_odb._operations.odb.create_cloud_autonomous_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_cloud_autonomous_vm_cluster.async_create_cloud_autonomous_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCloudAutonomousVmCluster")
        )
        input_: capo_odb.types.create_cloud_autonomous_vm_cluster_input.CreateCloudAutonomousVmClusterInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id,
            "odb_network_id": odb_network_id,
            "display_name": display_name,
            "autonomous_data_storage_size_in_t_bs": autonomous_data_storage_size_in_t_bs,
            "cpu_core_count_per_node": cpu_core_count_per_node,
            "memory_per_oracle_compute_unit_in_g_bs": memory_per_oracle_compute_unit_in_g_bs,
            "total_container_databases": total_container_databases,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if db_servers is not None:
            input_["db_servers"] = db_servers
        if description is not None:
            input_["description"] = description
        if is_mtls_enabled_vm_cluster is not None:
            input_["is_mtls_enabled_vm_cluster"] = is_mtls_enabled_vm_cluster
        if license_model is not None:
            input_["license_model"] = license_model
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        if scan_listener_port_non_tls is not None:
            input_["scan_listener_port_non_tls"] = scan_listener_port_non_tls
        if scan_listener_port_tls is not None:
            input_["scan_listener_port_tls"] = scan_listener_port_tls
        if tags is not None:
            input_["tags"] = tags
        if time_zone is not None:
            input_["time_zone"] = time_zone

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_cloud_autonomous_vm_cluster_output.GetCloudAutonomousVmClusterOutput":
        """<p>Gets information about a specific Autonomous VM cluster.</p>

        Args:
            cloud_autonomous_vm_cluster_id: <p>The unique identifier of the Autonomous VM cluster to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_cloud_autonomous_vm_cluster_input.GetCloudAutonomousVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_cloud_autonomous_vm_cluster_output.GetCloudAutonomousVmClusterOutput"
        ]:
            import capo_odb._operations.odb.get_cloud_autonomous_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_cloud_autonomous_vm_cluster.async_get_cloud_autonomous_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCloudAutonomousVmCluster")
        )
        input_: capo_odb.types.get_cloud_autonomous_vm_cluster_input.GetCloudAutonomousVmClusterInput = {
            "cloud_autonomous_vm_cluster_id": cloud_autonomous_vm_cluster_id
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
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_cloud_autonomous_vm_cluster_output.DeleteCloudAutonomousVmClusterOutput":
        """<p>Deletes an Autonomous VM cluster.</p>

        Args:
            cloud_autonomous_vm_cluster_id: <p>The unique identifier of the Autonomous VM cluster to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_cloud_autonomous_vm_cluster_input.DeleteCloudAutonomousVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_cloud_autonomous_vm_cluster_output.DeleteCloudAutonomousVmClusterOutput"
        ]:
            import capo_odb._operations.odb.delete_cloud_autonomous_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_cloud_autonomous_vm_cluster.async_delete_cloud_autonomous_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCloudAutonomousVmCluster")
        )
        input_: capo_odb.types.delete_cloud_autonomous_vm_cluster_input.DeleteCloudAutonomousVmClusterInput = {
            "cloud_autonomous_vm_cluster_id": cloud_autonomous_vm_cluster_id
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
    ) -> "capo_odb.types.list_cloud_autonomous_vm_clusters_output.ListCloudAutonomousVmClustersOutput":
        """<p>Lists all Autonomous VM clusters in a specified Cloud Exadata infrastructure.</p>

        Args:
            max_results: <p>The maximum number of items to return per page.</p>
            next_token: <p>The pagination token to continue listing from.</p>
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Cloud Exadata Infrastructure that hosts the Autonomous VM clusters to be listed.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_cloud_autonomous_vm_clusters_input.ListCloudAutonomousVmClustersInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_cloud_autonomous_vm_clusters_output.ListCloudAutonomousVmClustersOutput"
        ]:
            import capo_odb._operations.odb.list_cloud_autonomous_vm_clusters

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_cloud_autonomous_vm_clusters.async_list_cloud_autonomous_vm_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCloudAutonomousVmClusters")
        )
        input_: capo_odb.types.list_cloud_autonomous_vm_clusters_input.ListCloudAutonomousVmClustersInput = {}
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

    async def list_autonomous_virtual_machines(
        self,
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_autonomous_virtual_machines_output.ListAutonomousVirtualMachinesOutput":
        """<p>Lists all Autonomous VMs in an Autonomous VM cluster.</p>

        Args:
            max_results: <p>The maximum number of items to return per page.</p>
            next_token: <p>The pagination token to continue listing from.</p>
            cloud_autonomous_vm_cluster_id: <p>The unique identifier of the Autonomous VM cluster whose virtual machines you're listing.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_virtual_machines_input.ListAutonomousVirtualMachinesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_virtual_machines_output.ListAutonomousVirtualMachinesOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_virtual_machines

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_virtual_machines.async_list_autonomous_virtual_machines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAutonomousVirtualMachines")
        )
        input_: capo_odb.types.list_autonomous_virtual_machines_input.ListAutonomousVirtualMachinesInput = {
            "cloud_autonomous_vm_cluster_id": cloud_autonomous_vm_cluster_id
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
