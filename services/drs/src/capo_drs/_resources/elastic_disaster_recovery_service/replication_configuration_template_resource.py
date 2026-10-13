from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_drs._auth._signers
import capo_drs._auth._sigv4
from capo_drs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_drs.types.arn
    import capo_drs.types.create_replication_configuration_template_request
    import capo_drs.types.delete_replication_configuration_template_request
    import capo_drs.types.delete_replication_configuration_template_response
    import capo_drs.types.describe_replication_configuration_templates_request
    import capo_drs.types.describe_replication_configuration_templates_response
    import capo_drs.types.ec2_instance_type
    import capo_drs.types.internet_protocol
    import capo_drs.types.pagination_token
    import capo_drs.types.pit_policy
    import capo_drs.types.positive_integer
    import capo_drs.types.replication_configuration_data_plane_routing
    import capo_drs.types.replication_configuration_default_large_staging_disk_type
    import capo_drs.types.replication_configuration_ebs_encryption
    import capo_drs.types.replication_configuration_template
    import capo_drs.types.replication_configuration_template_i_ds
    import capo_drs.types.replication_configuration_template_id
    import capo_drs.types.replication_servers_security_groups_i_ds
    import capo_drs.types.strictly_positive_integer
    import capo_drs.types.subnet_id
    import capo_drs.types.tags_map
    import capo_drs.types.update_replication_configuration_template_request
    from capo_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from capo_drs._services.drs import drsClient, drsClientConfig


class ReplicationConfigurationTemplateResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def create(
        self,
        staging_area_subnet_id: "capo_drs.types.subnet_id.SubnetID",
        replication_servers_security_groups_i_ds: "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs",
        ebs_encryption: "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption",
        bandwidth_throttling: "capo_drs.types.positive_integer.PositiveInteger",
        staging_area_tags: "capo_drs.types.tags_map.TagsMap",
        pit_policy: "capo_drs.types.pit_policy.PITPolicy",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_server_instance_type: Optional[
            "capo_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_drs.types.arn.ARN"] = None,
        data_plane_routing: Optional[
            "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Creates a new ReplicationConfigurationTemplate.</p>

        Args:
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            tags: <p>A set of tags to be associated with the Replication Configuration Template resource.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template.create_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.create_replication_configuration_template_request

            return capo_drs.types.create_replication_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_drs.types.replication_configuration_template

            return capo_drs.types.replication_configuration_template.redact_sensitive(
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
        input_: capo_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest = {
            "staging_area_subnet_id": staging_area_subnet_id,
            "replication_servers_security_groups_i_ds": replication_servers_security_groups_i_ds,
            "ebs_encryption": ebs_encryption,
            "bandwidth_throttling": bandwidth_throttling,
            "staging_area_tags": staging_area_tags,
            "pit_policy": pit_policy,
        }
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
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
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if tags is not None:
            input_["tags"] = tags
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        replication_configuration_template_id: "capo_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        arn: Optional["capo_drs.types.arn.ARN"] = None,
        staging_area_subnet_id: Optional["capo_drs.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption: Optional[
            "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_drs.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_drs.types.positive_integer.PositiveInteger"
        ] = None,
        data_plane_routing: Optional[
            "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        pit_policy: Optional["capo_drs.types.pit_policy.PITPolicy"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Updates a ReplicationConfigurationTemplate by ID.</p>

        Args:
            replication_configuration_template_id: <p>The Replication Configuration Template ID.</p>
            arn: <p>The Replication Configuration Template ARN.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template.update_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.update_replication_configuration_template_request

            return capo_drs.types.update_replication_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_drs.types.replication_configuration_template

            return capo_drs.types.replication_configuration_template.redact_sensitive(
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
        input_: capo_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest = {
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
        if pit_policy is not None:
            input_["pit_policy"] = pit_policy
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        replication_configuration_template_id: "capo_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse":
        """<p>Deletes a single Replication Configuration Template by ID</p>

        Args:
            replication_configuration_template_id: <p>The ID of the Replication Configuration Template to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template.delete_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteReplicationConfigurationTemplate")
        )
        input_: capo_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest = {
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
        config_overrides: Optional[drsClientConfig] = None,
        replication_configuration_template_i_ds: Optional[
            "capo_drs.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse":
        """<p>Lists all ReplicationConfigurationTemplates, filtered by Source Server IDs.</p>

        Args:
            replication_configuration_template_i_ds: <p>The IDs of the Replication Configuration Templates to retrieve. An empty list means all Replication Configuration Templates.</p>
            max_results: <p>Maximum number of Replication Configuration Templates to retrieve.</p>
            next_token: <p>The token of the next Replication Configuration Template to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest]",
        ) -> OperationResponse[
            "capo_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates.describe_replication_configuration_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_replication_configuration_templates_response

            return capo_drs.types.describe_replication_configuration_templates_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeReplicationConfigurationTemplates",
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest = {}
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
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def create(
        self,
        staging_area_subnet_id: "capo_drs.types.subnet_id.SubnetID",
        replication_servers_security_groups_i_ds: "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs",
        ebs_encryption: "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption",
        bandwidth_throttling: "capo_drs.types.positive_integer.PositiveInteger",
        staging_area_tags: "capo_drs.types.tags_map.TagsMap",
        pit_policy: "capo_drs.types.pit_policy.PITPolicy",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_server_instance_type: Optional[
            "capo_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_drs.types.arn.ARN"] = None,
        data_plane_routing: Optional[
            "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Creates a new ReplicationConfigurationTemplate.</p>

        Args:
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            tags: <p>A set of tags to be associated with the Replication Configuration Template resource.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template.async_create_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.create_replication_configuration_template_request

            return capo_drs.types.create_replication_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_drs.types.replication_configuration_template

            return capo_drs.types.replication_configuration_template.redact_sensitive(
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
        input_: capo_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest = {
            "staging_area_subnet_id": staging_area_subnet_id,
            "replication_servers_security_groups_i_ds": replication_servers_security_groups_i_ds,
            "ebs_encryption": ebs_encryption,
            "bandwidth_throttling": bandwidth_throttling,
            "staging_area_tags": staging_area_tags,
            "pit_policy": pit_policy,
        }
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
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
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if tags is not None:
            input_["tags"] = tags
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        replication_configuration_template_id: "capo_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        arn: Optional["capo_drs.types.arn.ARN"] = None,
        staging_area_subnet_id: Optional["capo_drs.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption: Optional[
            "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_drs.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_drs.types.positive_integer.PositiveInteger"
        ] = None,
        data_plane_routing: Optional[
            "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        pit_policy: Optional["capo_drs.types.pit_policy.PITPolicy"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Updates a ReplicationConfigurationTemplate by ID.</p>

        Args:
            replication_configuration_template_id: <p>The Replication Configuration Template ID.</p>
            arn: <p>The Replication Configuration Template ARN.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template.async_update_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.update_replication_configuration_template_request

            return capo_drs.types.update_replication_configuration_template_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate",
        ) -> dict[str, Any]:
            import capo_drs.types.replication_configuration_template

            return capo_drs.types.replication_configuration_template.redact_sensitive(
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
        input_: capo_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest = {
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
        if pit_policy is not None:
            input_["pit_policy"] = pit_policy
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        replication_configuration_template_id: "capo_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse":
        """<p>Deletes a single Replication Configuration Template by ID</p>

        Args:
            replication_configuration_template_id: <p>The ID of the Replication Configuration Template to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template.async_delete_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteReplicationConfigurationTemplate")
        )
        input_: capo_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest = {
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
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        replication_configuration_template_i_ds: Optional[
            "capo_drs.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse":
        """<p>Lists all ReplicationConfigurationTemplates, filtered by Source Server IDs.</p>

        Args:
            replication_configuration_template_i_ds: <p>The IDs of the Replication Configuration Templates to retrieve. An empty list means all Replication Configuration Templates.</p>
            max_results: <p>Maximum number of Replication Configuration Templates to retrieve.</p>
            next_token: <p>The token of the next Replication Configuration Template to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates.async_describe_replication_configuration_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_replication_configuration_templates_response

            return capo_drs.types.describe_replication_configuration_templates_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeReplicationConfigurationTemplates",
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest = {}
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
