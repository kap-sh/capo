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
    import capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_input
    import capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_output
    import capo_odb.types.cluster_name
    import capo_odb.types.create_exadb_vm_cluster_input
    import capo_odb.types.create_exadb_vm_cluster_output
    import capo_odb.types.data_collection_options
    import capo_odb.types.delete_exadb_vm_cluster_input
    import capo_odb.types.delete_exadb_vm_cluster_output
    import capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_input
    import capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_output
    import capo_odb.types.exadb_vm_cluster_summary
    import capo_odb.types.general_input_string
    import capo_odb.types.get_exadb_vm_cluster_input
    import capo_odb.types.get_exadb_vm_cluster_output
    import capo_odb.types.hostname
    import capo_odb.types.license_model
    import capo_odb.types.list_exadb_vm_clusters_input
    import capo_odb.types.list_exadb_vm_clusters_output
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_list
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.shape_attribute
    import capo_odb.types.string_list
    import capo_odb.types.update_action
    import capo_odb.types.update_exadb_vm_cluster_input
    import capo_odb.types.update_exadb_vm_cluster_output
    from capo_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from capo_odb._services.odb import odbClient, odbClientConfig


class ExadbVmClusterResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def create(
        self,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        enabled_ecpu_count: int,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        grid_image_id: str,
        hostname: "capo_odb.types.hostname.Hostname",
        node_count: int,
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        shape: str,
        ssh_public_keys: "capo_odb.types.string_list.StringList",
        total_ecpu_count: int,
        vm_file_system_storage_total_size_in_g_bs: int,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        cluster_name: Optional["capo_odb.types.cluster_name.ClusterName"] = None,
        data_collection_options: Optional[
            "capo_odb.types.data_collection_options.DataCollectionOptions"
        ] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        scan_listener_port_tcp: Optional[int] = None,
        scan_listener_port_tcp_ssl: Optional[int] = None,
        shape_attribute: Optional[
            "capo_odb.types.shape_attribute.ShapeAttribute"
        ] = None,
        system_version: Optional[str] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        time_zone: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_exadb_vm_cluster_output.CreateExadbVmClusterOutput":
        """<p>Creates an Exascale VM cluster.</p>

        Args:
            display_name: <p>A user-friendly name for the Exascale VM cluster.</p>
            enabled_ecpu_count: <p>The number of ECPUs to enable for the Exascale VM cluster.</p>
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault for this Exascale VM cluster.</p>
            grid_image_id: <p>The Grid Infrastructure software image ID for the Exascale VM cluster.</p>
            hostname: <p>The host name for the Exascale VM cluster.</p>
            node_count: <p>The number of nodes in the Exascale VM cluster.</p>
            odb_network_id: <p>The unique identifier of the ODB network for the Exascale VM cluster.</p>
            shape: <p>The shape of the Exascale VM cluster.</p>
            ssh_public_keys: <p>The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.</p>
            total_ecpu_count: <p>The total number of ECPUs for the Exascale VM cluster.</p>
            vm_file_system_storage_total_size_in_g_bs: <p>The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.</p>
            cluster_name: <p>A name for the Grid Infrastructure cluster. The name isn't case sensitive.</p>
            data_collection_options: <p>The set of preferences for the various diagnostic collection options for the Exascale VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the Exascale VM cluster.</p>
            scan_listener_port_tcp: <p>The port number for TCP connections to the Single Client Access Name (SCAN) listener.</p>
            scan_listener_port_tcp_ssl: <p>The port number for TCP connections with SSL to the Single Client Access Name (SCAN) listener.</p>
            shape_attribute: <p>The shape attribute for the Exascale VM cluster.</p>
            system_version: <p>The version of the operating system of the image for the Exascale VM cluster.</p>
            tags: <p>The list of resource tags to apply to the Exascale VM cluster.</p>
            time_zone: <p>The time zone for the Exascale VM cluster.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you submit the same request twice with the same client token, the service ignores the second request and returns the result of the first. If you don't specify a client token, the AWS SDK automatically generates one. The client token is valid for up to 24 hours after it's first used.</p>

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
            req: "OperationRequest[capo_odb.types.create_exadb_vm_cluster_input.CreateExadbVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.create_exadb_vm_cluster_output.CreateExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.create_exadb_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.create_exadb_vm_cluster.create_exadb_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateExadbVmCluster")
        )
        input_: capo_odb.types.create_exadb_vm_cluster_input.CreateExadbVmClusterInput = {
            "display_name": display_name,
            "enabled_ecpu_count": enabled_ecpu_count,
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id,
            "grid_image_id": grid_image_id,
            "hostname": hostname,
            "node_count": node_count,
            "odb_network_id": odb_network_id,
            "shape": shape,
            "ssh_public_keys": ssh_public_keys,
            "total_ecpu_count": total_ecpu_count,
            "vm_file_system_storage_total_size_in_g_bs": vm_file_system_storage_total_size_in_g_bs,
        }
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if data_collection_options is not None:
            input_["data_collection_options"] = data_collection_options
        if license_model is not None:
            input_["license_model"] = license_model
        if scan_listener_port_tcp is not None:
            input_["scan_listener_port_tcp"] = scan_listener_port_tcp
        if scan_listener_port_tcp_ssl is not None:
            input_["scan_listener_port_tcp_ssl"] = scan_listener_port_tcp_ssl
        if shape_attribute is not None:
            input_["shape_attribute"] = shape_attribute
        if system_version is not None:
            input_["system_version"] = system_version
        if tags is not None:
            input_["tags"] = tags
        if time_zone is not None:
            input_["time_zone"] = time_zone
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

    def read(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.get_exadb_vm_cluster_output.GetExadbVmClusterOutput":
        """<p>Returns information about the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.get_exadb_vm_cluster_input.GetExadbVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.get_exadb_vm_cluster_output.GetExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.get_exadb_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.get_exadb_vm_cluster.get_exadb_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetExadbVmCluster")
        )
        input_: capo_odb.types.get_exadb_vm_cluster_input.GetExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id
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
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        data_collection_options: Optional[
            "capo_odb.types.data_collection_options.DataCollectionOptions"
        ] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        enabled_ecpu_count: Optional[int] = None,
        grid_image_id: Optional[str] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        ssh_public_keys: Optional["capo_odb.types.string_list.StringList"] = None,
        system_version: Optional[str] = None,
        total_ecpu_count: Optional[int] = None,
        update_action: Optional["capo_odb.types.update_action.UpdateAction"] = None,
        vm_file_system_storage_total_size_in_g_bs: Optional[int] = None,
    ) -> "capo_odb.types.update_exadb_vm_cluster_output.UpdateExadbVmClusterOutput":
        """<p>Updates the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to update.</p>
            data_collection_options: <p>The set of preferences for the various diagnostic collection options for the Exascale VM cluster.</p>
            display_name: <p>A new user-friendly name for the Exascale VM cluster.</p>
            enabled_ecpu_count: <p>The number of ECPUs to enable for the Exascale VM cluster.</p>
            grid_image_id: <p>The Grid Infrastructure software image ID for the Exascale VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the Exascale VM cluster.</p>
            ssh_public_keys: <p>The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.</p>
            system_version: <p>The version of the operating system of the image for the Exascale VM cluster.</p>
            total_ecpu_count: <p>The total number of ECPUs for the Exascale VM cluster.</p>
            update_action: <p>The update action to perform on the Exascale VM cluster.</p>
            vm_file_system_storage_total_size_in_g_bs: <p>The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.update_exadb_vm_cluster_input.UpdateExadbVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.update_exadb_vm_cluster_output.UpdateExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.update_exadb_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.update_exadb_vm_cluster.update_exadb_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateExadbVmCluster")
        )
        input_: capo_odb.types.update_exadb_vm_cluster_input.UpdateExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id
        }
        if data_collection_options is not None:
            input_["data_collection_options"] = data_collection_options
        if display_name is not None:
            input_["display_name"] = display_name
        if enabled_ecpu_count is not None:
            input_["enabled_ecpu_count"] = enabled_ecpu_count
        if grid_image_id is not None:
            input_["grid_image_id"] = grid_image_id
        if license_model is not None:
            input_["license_model"] = license_model
        if ssh_public_keys is not None:
            input_["ssh_public_keys"] = ssh_public_keys
        if system_version is not None:
            input_["system_version"] = system_version
        if total_ecpu_count is not None:
            input_["total_ecpu_count"] = total_ecpu_count
        if update_action is not None:
            input_["update_action"] = update_action
        if vm_file_system_storage_total_size_in_g_bs is not None:
            input_["vm_file_system_storage_total_size_in_g_bs"] = (
                vm_file_system_storage_total_size_in_g_bs
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.delete_exadb_vm_cluster_output.DeleteExadbVmClusterOutput":
        """<p>Deletes the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.delete_exadb_vm_cluster_input.DeleteExadbVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.delete_exadb_vm_cluster_output.DeleteExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.delete_exadb_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.delete_exadb_vm_cluster.delete_exadb_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteExadbVmCluster")
        )
        input_: capo_odb.types.delete_exadb_vm_cluster_input.DeleteExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id
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
        exascale_db_storage_vault_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_exadb_vm_clusters_output.ListExadbVmClustersOutput":
        """<p>Returns information about the Exascale VM clusters owned by your Amazon Web Services account.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault to list the associated Exascale VM clusters.</p>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_exadb_vm_clusters_input.ListExadbVmClustersInput]",
        ) -> OperationResponse[
            "capo_odb.types.list_exadb_vm_clusters_output.ListExadbVmClustersOutput"
        ]:
            import capo_odb._operations.odb.list_exadb_vm_clusters

            output, http_response = (
                capo_odb._operations.odb.list_exadb_vm_clusters.list_exadb_vm_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListExadbVmClusters")
        )
        input_: capo_odb.types.list_exadb_vm_clusters_input.ListExadbVmClustersInput = {}
        if exascale_db_storage_vault_id is not None:
            input_["exascale_db_storage_vault_id"] = exascale_db_storage_vault_id
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

    def associate_virtual_machines_to_exadb_vm_cluster(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        desired_node_count: int,
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_output.AssociateVirtualMachinesToExadbVmClusterOutput":
        """<p>Adds virtual machines to the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to add virtual machines to.</p>
            desired_node_count: <p>The desired number of nodes in the Exascale VM cluster after the association.</p>

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
            req: "OperationRequest[capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_input.AssociateVirtualMachinesToExadbVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_output.AssociateVirtualMachinesToExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.associate_virtual_machines_to_exadb_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.associate_virtual_machines_to_exadb_vm_cluster.associate_virtual_machines_to_exadb_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("AssociateVirtualMachinesToExadbVmCluster"),
        )
        input_: capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_input.AssociateVirtualMachinesToExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id,
            "desired_node_count": desired_node_count,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_virtual_machines_from_exadb_vm_cluster(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        db_node_ids: "capo_odb.types.resource_id_list.ResourceIdList",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_output.DisassociateVirtualMachinesFromExadbVmClusterOutput":
        """<p>Removes virtual machines from the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to remove virtual machines from.</p>
            db_node_ids: <p>The list of DB node IDs to remove from the Exascale VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_input.DisassociateVirtualMachinesFromExadbVmClusterInput]",
        ) -> OperationResponse[
            "capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_output.DisassociateVirtualMachinesFromExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.disassociate_virtual_machines_from_exadb_vm_cluster

            output, http_response = (
                capo_odb._operations.odb.disassociate_virtual_machines_from_exadb_vm_cluster.disassociate_virtual_machines_from_exadb_vm_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisassociateVirtualMachinesFromExadbVmCluster"),
        )
        input_: capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_input.DisassociateVirtualMachinesFromExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id,
            "db_node_ids": db_node_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncExadbVmClusterResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def create(
        self,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        enabled_ecpu_count: int,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        grid_image_id: str,
        hostname: "capo_odb.types.hostname.Hostname",
        node_count: int,
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        shape: str,
        ssh_public_keys: "capo_odb.types.string_list.StringList",
        total_ecpu_count: int,
        vm_file_system_storage_total_size_in_g_bs: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cluster_name: Optional["capo_odb.types.cluster_name.ClusterName"] = None,
        data_collection_options: Optional[
            "capo_odb.types.data_collection_options.DataCollectionOptions"
        ] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        scan_listener_port_tcp: Optional[int] = None,
        scan_listener_port_tcp_ssl: Optional[int] = None,
        shape_attribute: Optional[
            "capo_odb.types.shape_attribute.ShapeAttribute"
        ] = None,
        system_version: Optional[str] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        time_zone: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_exadb_vm_cluster_output.CreateExadbVmClusterOutput":
        """<p>Creates an Exascale VM cluster.</p>

        Args:
            display_name: <p>A user-friendly name for the Exascale VM cluster.</p>
            enabled_ecpu_count: <p>The number of ECPUs to enable for the Exascale VM cluster.</p>
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault for this Exascale VM cluster.</p>
            grid_image_id: <p>The Grid Infrastructure software image ID for the Exascale VM cluster.</p>
            hostname: <p>The host name for the Exascale VM cluster.</p>
            node_count: <p>The number of nodes in the Exascale VM cluster.</p>
            odb_network_id: <p>The unique identifier of the ODB network for the Exascale VM cluster.</p>
            shape: <p>The shape of the Exascale VM cluster.</p>
            ssh_public_keys: <p>The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.</p>
            total_ecpu_count: <p>The total number of ECPUs for the Exascale VM cluster.</p>
            vm_file_system_storage_total_size_in_g_bs: <p>The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.</p>
            cluster_name: <p>A name for the Grid Infrastructure cluster. The name isn't case sensitive.</p>
            data_collection_options: <p>The set of preferences for the various diagnostic collection options for the Exascale VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the Exascale VM cluster.</p>
            scan_listener_port_tcp: <p>The port number for TCP connections to the Single Client Access Name (SCAN) listener.</p>
            scan_listener_port_tcp_ssl: <p>The port number for TCP connections with SSL to the Single Client Access Name (SCAN) listener.</p>
            shape_attribute: <p>The shape attribute for the Exascale VM cluster.</p>
            system_version: <p>The version of the operating system of the image for the Exascale VM cluster.</p>
            tags: <p>The list of resource tags to apply to the Exascale VM cluster.</p>
            time_zone: <p>The time zone for the Exascale VM cluster.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you submit the same request twice with the same client token, the service ignores the second request and returns the result of the first. If you don't specify a client token, the AWS SDK automatically generates one. The client token is valid for up to 24 hours after it's first used.</p>

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
            req: "AsyncOperationRequest[capo_odb.types.create_exadb_vm_cluster_input.CreateExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_exadb_vm_cluster_output.CreateExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.create_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_exadb_vm_cluster.async_create_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateExadbVmCluster")
        )
        input_: capo_odb.types.create_exadb_vm_cluster_input.CreateExadbVmClusterInput = {
            "display_name": display_name,
            "enabled_ecpu_count": enabled_ecpu_count,
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id,
            "grid_image_id": grid_image_id,
            "hostname": hostname,
            "node_count": node_count,
            "odb_network_id": odb_network_id,
            "shape": shape,
            "ssh_public_keys": ssh_public_keys,
            "total_ecpu_count": total_ecpu_count,
            "vm_file_system_storage_total_size_in_g_bs": vm_file_system_storage_total_size_in_g_bs,
        }
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if data_collection_options is not None:
            input_["data_collection_options"] = data_collection_options
        if license_model is not None:
            input_["license_model"] = license_model
        if scan_listener_port_tcp is not None:
            input_["scan_listener_port_tcp"] = scan_listener_port_tcp
        if scan_listener_port_tcp_ssl is not None:
            input_["scan_listener_port_tcp_ssl"] = scan_listener_port_tcp_ssl
        if shape_attribute is not None:
            input_["shape_attribute"] = shape_attribute
        if system_version is not None:
            input_["system_version"] = system_version
        if tags is not None:
            input_["tags"] = tags
        if time_zone is not None:
            input_["time_zone"] = time_zone
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_exadb_vm_cluster_output.GetExadbVmClusterOutput":
        """<p>Returns information about the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_exadb_vm_cluster_input.GetExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_exadb_vm_cluster_output.GetExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.get_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_exadb_vm_cluster.async_get_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetExadbVmCluster")
        )
        input_: capo_odb.types.get_exadb_vm_cluster_input.GetExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id
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
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        data_collection_options: Optional[
            "capo_odb.types.data_collection_options.DataCollectionOptions"
        ] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        enabled_ecpu_count: Optional[int] = None,
        grid_image_id: Optional[str] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        ssh_public_keys: Optional["capo_odb.types.string_list.StringList"] = None,
        system_version: Optional[str] = None,
        total_ecpu_count: Optional[int] = None,
        update_action: Optional["capo_odb.types.update_action.UpdateAction"] = None,
        vm_file_system_storage_total_size_in_g_bs: Optional[int] = None,
    ) -> "capo_odb.types.update_exadb_vm_cluster_output.UpdateExadbVmClusterOutput":
        """<p>Updates the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to update.</p>
            data_collection_options: <p>The set of preferences for the various diagnostic collection options for the Exascale VM cluster.</p>
            display_name: <p>A new user-friendly name for the Exascale VM cluster.</p>
            enabled_ecpu_count: <p>The number of ECPUs to enable for the Exascale VM cluster.</p>
            grid_image_id: <p>The Grid Infrastructure software image ID for the Exascale VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the Exascale VM cluster.</p>
            ssh_public_keys: <p>The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.</p>
            system_version: <p>The version of the operating system of the image for the Exascale VM cluster.</p>
            total_ecpu_count: <p>The total number of ECPUs for the Exascale VM cluster.</p>
            update_action: <p>The update action to perform on the Exascale VM cluster.</p>
            vm_file_system_storage_total_size_in_g_bs: <p>The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_exadb_vm_cluster_input.UpdateExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_exadb_vm_cluster_output.UpdateExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.update_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_exadb_vm_cluster.async_update_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateExadbVmCluster")
        )
        input_: capo_odb.types.update_exadb_vm_cluster_input.UpdateExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id
        }
        if data_collection_options is not None:
            input_["data_collection_options"] = data_collection_options
        if display_name is not None:
            input_["display_name"] = display_name
        if enabled_ecpu_count is not None:
            input_["enabled_ecpu_count"] = enabled_ecpu_count
        if grid_image_id is not None:
            input_["grid_image_id"] = grid_image_id
        if license_model is not None:
            input_["license_model"] = license_model
        if ssh_public_keys is not None:
            input_["ssh_public_keys"] = ssh_public_keys
        if system_version is not None:
            input_["system_version"] = system_version
        if total_ecpu_count is not None:
            input_["total_ecpu_count"] = total_ecpu_count
        if update_action is not None:
            input_["update_action"] = update_action
        if vm_file_system_storage_total_size_in_g_bs is not None:
            input_["vm_file_system_storage_total_size_in_g_bs"] = (
                vm_file_system_storage_total_size_in_g_bs
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_exadb_vm_cluster_output.DeleteExadbVmClusterOutput":
        """<p>Deletes the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_exadb_vm_cluster_input.DeleteExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_exadb_vm_cluster_output.DeleteExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.delete_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_exadb_vm_cluster.async_delete_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteExadbVmCluster")
        )
        input_: capo_odb.types.delete_exadb_vm_cluster_input.DeleteExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id
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
        exascale_db_storage_vault_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_exadb_vm_clusters_output.ListExadbVmClustersOutput":
        """<p>Returns information about the Exascale VM clusters owned by your Amazon Web Services account.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault to list the associated Exascale VM clusters.</p>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_exadb_vm_clusters_input.ListExadbVmClustersInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_exadb_vm_clusters_output.ListExadbVmClustersOutput"
        ]:
            import capo_odb._operations.odb.list_exadb_vm_clusters

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_exadb_vm_clusters.async_list_exadb_vm_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListExadbVmClusters")
        )
        input_: capo_odb.types.list_exadb_vm_clusters_input.ListExadbVmClustersInput = {}
        if exascale_db_storage_vault_id is not None:
            input_["exascale_db_storage_vault_id"] = exascale_db_storage_vault_id
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

    async def associate_virtual_machines_to_exadb_vm_cluster(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        desired_node_count: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_output.AssociateVirtualMachinesToExadbVmClusterOutput":
        """<p>Adds virtual machines to the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to add virtual machines to.</p>
            desired_node_count: <p>The desired number of nodes in the Exascale VM cluster after the association.</p>

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
            req: "AsyncOperationRequest[capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_input.AssociateVirtualMachinesToExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_output.AssociateVirtualMachinesToExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.associate_virtual_machines_to_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.associate_virtual_machines_to_exadb_vm_cluster.async_associate_virtual_machines_to_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("AssociateVirtualMachinesToExadbVmCluster"),
        )
        input_: capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_input.AssociateVirtualMachinesToExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id,
            "desired_node_count": desired_node_count,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_virtual_machines_from_exadb_vm_cluster(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        db_node_ids: "capo_odb.types.resource_id_list.ResourceIdList",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_output.DisassociateVirtualMachinesFromExadbVmClusterOutput":
        """<p>Removes virtual machines from the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to remove virtual machines from.</p>
            db_node_ids: <p>The list of DB node IDs to remove from the Exascale VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_input.DisassociateVirtualMachinesFromExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_output.DisassociateVirtualMachinesFromExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.disassociate_virtual_machines_from_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.disassociate_virtual_machines_from_exadb_vm_cluster.async_disassociate_virtual_machines_from_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisassociateVirtualMachinesFromExadbVmCluster"),
        )
        input_: capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_input.DisassociateVirtualMachinesFromExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id,
            "db_node_ids": db_node_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
