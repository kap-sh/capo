from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_mgn._auth._signers
import capo_mgn._auth._sigv4
from capo_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.bandwidth_throttling
    import capo_mgn.types.create_replication_configuration_template_request
    import capo_mgn.types.delete_replication_configuration_template_request
    import capo_mgn.types.delete_replication_configuration_template_response
    import capo_mgn.types.describe_replication_configuration_templates_request
    import capo_mgn.types.describe_replication_configuration_templates_response
    import capo_mgn.types.ec2_instance_type
    import capo_mgn.types.internet_protocol
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.replication_configuration_data_plane_routing
    import capo_mgn.types.replication_configuration_default_large_staging_disk_type
    import capo_mgn.types.replication_configuration_ebs_encryption
    import capo_mgn.types.replication_configuration_template
    import capo_mgn.types.replication_configuration_template_i_ds
    import capo_mgn.types.replication_configuration_template_id
    import capo_mgn.types.replication_servers_security_groups_i_ds
    import capo_mgn.types.storage_configuration
    import capo_mgn.types.subnet_id
    import capo_mgn.types.tags_map
    import capo_mgn.types.update_replication_configuration_template_request
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class ReplicationConfigurationTemplateResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        staging_area_subnet_id: "capo_mgn.types.subnet_id.SubnetID",
        associate_default_security_group: bool,
        replication_servers_security_groups_i_ds: "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs",
        replication_server_instance_type: "capo_mgn.types.ec2_instance_type.EC2InstanceType",
        use_dedicated_replication_server: bool,
        default_large_staging_disk_type: "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType",
        ebs_encryption: "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption",
        bandwidth_throttling: "capo_mgn.types.bandwidth_throttling.BandwidthThrottling",
        data_plane_routing: "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting",
        create_public_ip: bool,
        staging_area_tags: "capo_mgn.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        ebs_encryption_key_arn: Optional["capo_mgn.types.arn.ARN"] = None,
        use_fips_endpoint: Optional[bool] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        internet_protocol: Optional[
            "capo_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
        storage_configuration: Optional[
            "capo_mgn.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Creates a new ReplicationConfigurationTemplate.</p>

        Args:
            staging_area_subnet_id: <p>Request to configure the Staging Area subnet ID during Replication Settings template creation.</p>
            associate_default_security_group: <p>Request to associate the default Application Migration Service Security group with the Replication Settings template.</p>
            replication_servers_security_groups_i_ds: <p>Request to configure the Replication Server Security group ID during Replication Settings template creation.</p>
            replication_server_instance_type: <p>Request to configure the Replication Server instance type during Replication Settings template creation.</p>
            use_dedicated_replication_server: <p>Request to use Dedicated Replication Servers during Replication Settings template creation.</p>
            default_large_staging_disk_type: <p>Request to configure the default large staging disk EBS volume type during Replication Settings template creation.</p>
            ebs_encryption: <p>Request to configure EBS encryption during Replication Settings template creation.</p>
            ebs_encryption_key_arn: <p>Request to configure an EBS encryption key during Replication Settings template creation.</p>
            bandwidth_throttling: <p>Request to configure bandwidth throttling during Replication Settings template creation.</p>
            data_plane_routing: <p>Request to configure data plane routing during Replication Settings template creation.</p>
            create_public_ip: <p>Request to create Public IP during Replication Settings template creation.</p>
            staging_area_tags: <p>Request to configure Staging Area tags during Replication Settings template creation.</p>
            use_fips_endpoint: <p>Request to use Fips Endpoint during Replication Settings template creation.</p>
            tags: <p>Request to configure tags during Replication Settings template creation.</p>
            internet_protocol: <p>Request to configure the internet protocol to IPv4 or IPv6.</p>
            store_snapshot_on_local_zone: <p>Request to store snapshot on local zone during Replication Settings template creation.</p>
            storage_configuration: <p>Request to configure storage during Replication Settings template creation.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.create_replication_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_replication_configuration_template.create_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_replication_configuration_template_request

            return capo_mgn.types.create_replication_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_mgn.types.replication_configuration_template

            return capo_mgn.types.replication_configuration_template.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateReplicationConfigurationTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest = {
            "staging_area_subnet_id": staging_area_subnet_id,
            "associate_default_security_group": associate_default_security_group,
            "replication_servers_security_groups_i_ds": replication_servers_security_groups_i_ds,
            "replication_server_instance_type": replication_server_instance_type,
            "use_dedicated_replication_server": use_dedicated_replication_server,
            "default_large_staging_disk_type": default_large_staging_disk_type,
            "ebs_encryption": ebs_encryption,
            "bandwidth_throttling": bandwidth_throttling,
            "data_plane_routing": data_plane_routing,
            "create_public_ip": create_public_ip,
            "staging_area_tags": staging_area_tags,
        }
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if use_fips_endpoint is not None:
            input_["use_fips_endpoint"] = use_fips_endpoint
        if tags is not None:
            input_["tags"] = tags
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input_["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        replication_configuration_template_id: "capo_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        arn: Optional["capo_mgn.types.arn.ARN"] = None,
        staging_area_subnet_id: Optional["capo_mgn.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_mgn.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption: Optional[
            "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_mgn.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_mgn.types.bandwidth_throttling.BandwidthThrottling"
        ] = None,
        data_plane_routing: Optional[
            "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        use_fips_endpoint: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
        storage_configuration: Optional[
            "capo_mgn.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Updates a ReplicationConfigurationTemplate by ID.</p>

        Args:
            replication_configuration_template_id: <p>Update replication configuration template template ID request.</p>
            arn: <p>Update replication configuration template ARN request.</p>
            staging_area_subnet_id: <p>Update replication configuration template Staging Area subnet ID request.</p>
            associate_default_security_group: <p>Update replication configuration template associate default Application Migration Service Security group request.</p>
            replication_servers_security_groups_i_ds: <p>Update replication configuration template Replication Server Security groups IDs request.</p>
            replication_server_instance_type: <p>Update replication configuration template Replication Server instance type request.</p>
            use_dedicated_replication_server: <p>Update replication configuration template use dedicated Replication Server request.</p>
            default_large_staging_disk_type: <p>Update replication configuration template use default large Staging Disk type request.</p>
            ebs_encryption: <p>Update replication configuration template EBS encryption request.</p>
            ebs_encryption_key_arn: <p>Update replication configuration template EBS encryption key ARN request.</p>
            bandwidth_throttling: <p>Update replication configuration template bandwidth throttling request.</p>
            data_plane_routing: <p>Update replication configuration template data plane routing request.</p>
            create_public_ip: <p>Update replication configuration template create Public IP request.</p>
            staging_area_tags: <p>Update replication configuration template Staging Area Tags request.</p>
            use_fips_endpoint: <p>Update replication configuration template use Fips Endpoint request.</p>
            internet_protocol: <p>Update replication configuration template internet protocol request.</p>
            store_snapshot_on_local_zone: <p>Update replication configuration template store snapshot on local zone request.</p>
            storage_configuration: <p>Update replication configuration template storage configuration request.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.update_replication_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_replication_configuration_template.update_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.update_replication_configuration_template_request

            return capo_mgn.types.update_replication_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_mgn.types.replication_configuration_template

            return capo_mgn.types.replication_configuration_template.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateReplicationConfigurationTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest = {
            "replication_configuration_template_id": replication_configuration_template_id
        }
        if arn is not None:
            input_["arn"] = arn
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if use_fips_endpoint is not None:
            input_["use_fips_endpoint"] = use_fips_endpoint
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input_["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        replication_configuration_template_id: "capo_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse":
        """<p>Deletes a single Replication Configuration Template by ID</p>

        Args:
            replication_configuration_template_id: <p>Request to delete Replication Configuration Template from service by Replication Configuration Template ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_replication_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_replication_configuration_template.delete_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteReplicationConfigurationTemplate")
        )
        input_: capo_mgn.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest = {
            "replication_configuration_template_id": replication_configuration_template_id
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
        config_overrides: Optional[mgnClientConfig] = None,
        replication_configuration_template_i_ds: Optional[
            "capo_mgn.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse":
        """<p>Lists all ReplicationConfigurationTemplates, filtered by replication configuration template IDs.</p>

        Args:
            replication_configuration_template_i_ds: <p>Request to describe Replication Configuration template by template IDs.</p>
            max_results: <p>Request to describe Replication Configuration template by max results.</p>
            next_token: <p>Request to describe Replication Configuration template by next token.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_replication_configuration_templates

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_replication_configuration_templates.describe_replication_configuration_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_replication_configuration_templates_response

            return capo_mgn.types.describe_replication_configuration_templates_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeReplicationConfigurationTemplates",
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest = {}
        if replication_configuration_template_i_ds is not None:
            input_["replication_configuration_template_i_ds"] = (
                replication_configuration_template_i_ds
            )
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


class AsyncReplicationConfigurationTemplateResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        staging_area_subnet_id: "capo_mgn.types.subnet_id.SubnetID",
        associate_default_security_group: bool,
        replication_servers_security_groups_i_ds: "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs",
        replication_server_instance_type: "capo_mgn.types.ec2_instance_type.EC2InstanceType",
        use_dedicated_replication_server: bool,
        default_large_staging_disk_type: "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType",
        ebs_encryption: "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption",
        bandwidth_throttling: "capo_mgn.types.bandwidth_throttling.BandwidthThrottling",
        data_plane_routing: "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting",
        create_public_ip: bool,
        staging_area_tags: "capo_mgn.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        ebs_encryption_key_arn: Optional["capo_mgn.types.arn.ARN"] = None,
        use_fips_endpoint: Optional[bool] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        internet_protocol: Optional[
            "capo_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
        storage_configuration: Optional[
            "capo_mgn.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Creates a new ReplicationConfigurationTemplate.</p>

        Args:
            staging_area_subnet_id: <p>Request to configure the Staging Area subnet ID during Replication Settings template creation.</p>
            associate_default_security_group: <p>Request to associate the default Application Migration Service Security group with the Replication Settings template.</p>
            replication_servers_security_groups_i_ds: <p>Request to configure the Replication Server Security group ID during Replication Settings template creation.</p>
            replication_server_instance_type: <p>Request to configure the Replication Server instance type during Replication Settings template creation.</p>
            use_dedicated_replication_server: <p>Request to use Dedicated Replication Servers during Replication Settings template creation.</p>
            default_large_staging_disk_type: <p>Request to configure the default large staging disk EBS volume type during Replication Settings template creation.</p>
            ebs_encryption: <p>Request to configure EBS encryption during Replication Settings template creation.</p>
            ebs_encryption_key_arn: <p>Request to configure an EBS encryption key during Replication Settings template creation.</p>
            bandwidth_throttling: <p>Request to configure bandwidth throttling during Replication Settings template creation.</p>
            data_plane_routing: <p>Request to configure data plane routing during Replication Settings template creation.</p>
            create_public_ip: <p>Request to create Public IP during Replication Settings template creation.</p>
            staging_area_tags: <p>Request to configure Staging Area tags during Replication Settings template creation.</p>
            use_fips_endpoint: <p>Request to use Fips Endpoint during Replication Settings template creation.</p>
            tags: <p>Request to configure tags during Replication Settings template creation.</p>
            internet_protocol: <p>Request to configure the internet protocol to IPv4 or IPv6.</p>
            store_snapshot_on_local_zone: <p>Request to store snapshot on local zone during Replication Settings template creation.</p>
            storage_configuration: <p>Request to configure storage during Replication Settings template creation.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.create_replication_configuration_template

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.create_replication_configuration_template.async_create_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_replication_configuration_template_request

            return capo_mgn.types.create_replication_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_mgn.types.replication_configuration_template

            return capo_mgn.types.replication_configuration_template.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateReplicationConfigurationTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest = {
            "staging_area_subnet_id": staging_area_subnet_id,
            "associate_default_security_group": associate_default_security_group,
            "replication_servers_security_groups_i_ds": replication_servers_security_groups_i_ds,
            "replication_server_instance_type": replication_server_instance_type,
            "use_dedicated_replication_server": use_dedicated_replication_server,
            "default_large_staging_disk_type": default_large_staging_disk_type,
            "ebs_encryption": ebs_encryption,
            "bandwidth_throttling": bandwidth_throttling,
            "data_plane_routing": data_plane_routing,
            "create_public_ip": create_public_ip,
            "staging_area_tags": staging_area_tags,
        }
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if use_fips_endpoint is not None:
            input_["use_fips_endpoint"] = use_fips_endpoint
        if tags is not None:
            input_["tags"] = tags
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input_["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        replication_configuration_template_id: "capo_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        arn: Optional["capo_mgn.types.arn.ARN"] = None,
        staging_area_subnet_id: Optional["capo_mgn.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_mgn.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption: Optional[
            "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_mgn.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_mgn.types.bandwidth_throttling.BandwidthThrottling"
        ] = None,
        data_plane_routing: Optional[
            "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        use_fips_endpoint: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
        storage_configuration: Optional[
            "capo_mgn.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Updates a ReplicationConfigurationTemplate by ID.</p>

        Args:
            replication_configuration_template_id: <p>Update replication configuration template template ID request.</p>
            arn: <p>Update replication configuration template ARN request.</p>
            staging_area_subnet_id: <p>Update replication configuration template Staging Area subnet ID request.</p>
            associate_default_security_group: <p>Update replication configuration template associate default Application Migration Service Security group request.</p>
            replication_servers_security_groups_i_ds: <p>Update replication configuration template Replication Server Security groups IDs request.</p>
            replication_server_instance_type: <p>Update replication configuration template Replication Server instance type request.</p>
            use_dedicated_replication_server: <p>Update replication configuration template use dedicated Replication Server request.</p>
            default_large_staging_disk_type: <p>Update replication configuration template use default large Staging Disk type request.</p>
            ebs_encryption: <p>Update replication configuration template EBS encryption request.</p>
            ebs_encryption_key_arn: <p>Update replication configuration template EBS encryption key ARN request.</p>
            bandwidth_throttling: <p>Update replication configuration template bandwidth throttling request.</p>
            data_plane_routing: <p>Update replication configuration template data plane routing request.</p>
            create_public_ip: <p>Update replication configuration template create Public IP request.</p>
            staging_area_tags: <p>Update replication configuration template Staging Area Tags request.</p>
            use_fips_endpoint: <p>Update replication configuration template use Fips Endpoint request.</p>
            internet_protocol: <p>Update replication configuration template internet protocol request.</p>
            store_snapshot_on_local_zone: <p>Update replication configuration template store snapshot on local zone request.</p>
            storage_configuration: <p>Update replication configuration template storage configuration request.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.update_replication_configuration_template

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_replication_configuration_template.async_update_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.update_replication_configuration_template_request

            return capo_mgn.types.update_replication_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_mgn.types.replication_configuration_template

            return capo_mgn.types.replication_configuration_template.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateReplicationConfigurationTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest = {
            "replication_configuration_template_id": replication_configuration_template_id
        }
        if arn is not None:
            input_["arn"] = arn
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if use_fips_endpoint is not None:
            input_["use_fips_endpoint"] = use_fips_endpoint
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input_["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        replication_configuration_template_id: "capo_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> "capo_mgn.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse":
        """<p>Deletes a single Replication Configuration Template by ID</p>

        Args:
            replication_configuration_template_id: <p>Request to delete Replication Configuration Template from service by Replication Configuration Template ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_replication_configuration_template

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.delete_replication_configuration_template.async_delete_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteReplicationConfigurationTemplate")
        )
        input_: capo_mgn.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest = {
            "replication_configuration_template_id": replication_configuration_template_id
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
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        replication_configuration_template_i_ds: Optional[
            "capo_mgn.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse":
        """<p>Lists all ReplicationConfigurationTemplates, filtered by replication configuration template IDs.</p>

        Args:
            replication_configuration_template_i_ds: <p>Request to describe Replication Configuration template by template IDs.</p>
            max_results: <p>Request to describe Replication Configuration template by max results.</p>
            next_token: <p>Request to describe Replication Configuration template by next token.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_replication_configuration_templates

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.describe_replication_configuration_templates.async_describe_replication_configuration_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_replication_configuration_templates_response

            return capo_mgn.types.describe_replication_configuration_templates_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeReplicationConfigurationTemplates",
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest = {}
        if replication_configuration_template_i_ds is not None:
            input_["replication_configuration_template_i_ds"] = (
                replication_configuration_template_i_ds
            )
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
