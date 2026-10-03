from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_redshift_serverless.types.config_parameter_list
    import capo_redshift_serverless.types.create_workgroup_request
    import capo_redshift_serverless.types.create_workgroup_response
    import capo_redshift_serverless.types.delete_workgroup_request
    import capo_redshift_serverless.types.delete_workgroup_response
    import capo_redshift_serverless.types.get_workgroup_request
    import capo_redshift_serverless.types.get_workgroup_response
    import capo_redshift_serverless.types.ip_address_type
    import capo_redshift_serverless.types.list_workgroups_request
    import capo_redshift_serverless.types.list_workgroups_response
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.owner_account
    import capo_redshift_serverless.types.performance_target
    import capo_redshift_serverless.types.security_group_id_list
    import capo_redshift_serverless.types.subnet_id_list
    import capo_redshift_serverless.types.tag_list
    import capo_redshift_serverless.types.track_name
    import capo_redshift_serverless.types.update_workgroup_request
    import capo_redshift_serverless.types.update_workgroup_response
    import capo_redshift_serverless.types.workgroup
    import capo_redshift_serverless.types.workgroup_name
    from capo_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from capo_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class WorkgroupResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def put(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        base_capacity: Optional[int] = None,
        enhanced_vpc_routing: Optional[bool] = None,
        config_parameters: Optional[
            "capo_redshift_serverless.types.config_parameter_list.ConfigParameterList"
        ] = None,
        security_group_ids: Optional[
            "capo_redshift_serverless.types.security_group_id_list.SecurityGroupIdList"
        ] = None,
        subnet_ids: Optional[
            "capo_redshift_serverless.types.subnet_id_list.SubnetIdList"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
        port: Optional[int] = None,
        max_capacity: Optional[int] = None,
        price_performance_target: Optional[
            "capo_redshift_serverless.types.performance_target.PerformanceTarget"
        ] = None,
        ip_address_type: Optional[
            "capo_redshift_serverless.types.ip_address_type.IpAddressType"
        ] = None,
        track_name: Optional[
            "capo_redshift_serverless.types.track_name.TrackName"
        ] = None,
        extra_compute_for_automatic_optimization: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.create_workgroup_response.CreateWorkgroupResponse":
        """<p>Creates an workgroup in Amazon Redshift Serverless.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a workgroup is in an account with VPC BPA turned on, the following capabilities are blocked: </p> <ul> <li> <p>Creating a public access workgroup</p> </li> <li> <p>Modifying a private workgroup to public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the workgroup when the workgroup is public</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            workgroup_name: <p>The name of the created workgroup.</p>
            namespace_name: <p>The name of the namespace to associate with the workgroup.</p>
            base_capacity: <p>The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).</p>
            enhanced_vpc_routing: <p>The value that specifies whether to turn on enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC instead of over the internet.</p>
            config_parameters: <p>An array of parameters to set for advanced control over a database. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. If you're using <code>wlm_json_configuration</code>, the maximum size of <code>parameterValue</code> is 8000 characters. For more information about query monitoring rules and available metrics, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless"> Query monitoring metrics for Amazon Redshift Serverless</a>.</p>
            security_group_ids: <p>An array of security group IDs to associate with the workgroup.</p>
            subnet_ids: <p>An array of VPC subnet IDs to associate with the workgroup.</p>
            publicly_accessible: <p>A value that specifies whether the workgroup can be accessed from a public network.</p>
            tags: <p>A array of tag instances.</p>
            port: <p>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</p>
            max_capacity: <p>The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.</p>
            price_performance_target: <p>An object that represents the price performance target settings for the workgroup.</p>
            ip_address_type: <p>The IP address type that the workgroup supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>
            track_name: <p>An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the <code>current</code> track.</p>
            extra_compute_for_automatic_optimization: <p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is an insufficient capacity to perform the action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.ipv6_cidr_block_not_found_exception.Ipv6CidrBlockNotFoundException: <p>There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.create_workgroup_request.CreateWorkgroupRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.create_workgroup_response.CreateWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_workgroup

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.create_workgroup.create_workgroup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_workgroup_request.CreateWorkgroupRequest = {
            "workgroup_name": workgroup_name,
            "namespace_name": namespace_name,
        }
        if base_capacity is not None:
            input_["base_capacity"] = base_capacity
        if enhanced_vpc_routing is not None:
            input_["enhanced_vpc_routing"] = enhanced_vpc_routing
        if config_parameters is not None:
            input_["config_parameters"] = config_parameters
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if tags is not None:
            input_["tags"] = tags
        if port is not None:
            input_["port"] = port
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if price_performance_target is not None:
            input_["price_performance_target"] = price_performance_target
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if track_name is not None:
            input_["track_name"] = track_name
        if extra_compute_for_automatic_optimization is not None:
            input_["extra_compute_for_automatic_optimization"] = (
                extra_compute_for_automatic_optimization
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_workgroup_response.GetWorkgroupResponse":
        """<p>Returns information about a specific workgroup.</p>

        Args:
            workgroup_name: <p>The name of the workgroup to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.get_workgroup_request.GetWorkgroupRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.get_workgroup_response.GetWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_workgroup

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.get_workgroup.get_workgroup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_workgroup_request.GetWorkgroupRequest = {
            "workgroup_name": workgroup_name
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
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        base_capacity: Optional[int] = None,
        enhanced_vpc_routing: Optional[bool] = None,
        config_parameters: Optional[
            "capo_redshift_serverless.types.config_parameter_list.ConfigParameterList"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        subnet_ids: Optional[
            "capo_redshift_serverless.types.subnet_id_list.SubnetIdList"
        ] = None,
        security_group_ids: Optional[
            "capo_redshift_serverless.types.security_group_id_list.SecurityGroupIdList"
        ] = None,
        port: Optional[int] = None,
        max_capacity: Optional[int] = None,
        ip_address_type: Optional[
            "capo_redshift_serverless.types.ip_address_type.IpAddressType"
        ] = None,
        price_performance_target: Optional[
            "capo_redshift_serverless.types.performance_target.PerformanceTarget"
        ] = None,
        track_name: Optional[
            "capo_redshift_serverless.types.track_name.TrackName"
        ] = None,
        extra_compute_for_automatic_optimization: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.update_workgroup_response.UpdateWorkgroupResponse":
        """<p>Updates a workgroup with the specified configuration settings. You can't update multiple parameters in one request. For example, you can update <code>baseCapacity</code> or <code>port</code> in a single request, but you can't update both in the same request.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a workgroup is in an account with VPC BPA turned on, the following capabilities are blocked: </p> <ul> <li> <p>Creating a public access workgroup</p> </li> <li> <p>Modifying a private workgroup to public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the workgroup when the workgroup is public</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            workgroup_name: <p>The name of the workgroup to update. You can't update the name of a workgroup once it is created.</p>
            base_capacity: <p>The new base data warehouse capacity in Redshift Processing Units (RPUs).</p>
            enhanced_vpc_routing: <p>The value that specifies whether to turn on enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.</p>
            config_parameters: <p>An array of parameters to set for advanced control over a database. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. If you're using <code>wlm_json_configuration</code>, the maximum size of <code>parameterValue</code> is 8000 characters. For more information about query monitoring rules and available metrics, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless"> Query monitoring metrics for Amazon Redshift Serverless</a>.</p>
            publicly_accessible: <p>A value that specifies whether the workgroup can be accessible from a public network.</p>
            subnet_ids: <p>An array of VPC subnet IDs to associate with the workgroup.</p>
            security_group_ids: <p>An array of security group IDs to associate with the workgroup.</p>
            port: <p>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</p>
            max_capacity: <p>The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.</p>
            ip_address_type: <p>The IP address type that the workgroup supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>
            price_performance_target: <p>An object that represents the price performance target settings for the workgroup.</p>
            track_name: <p>An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the <code>current</code> track.</p>
            extra_compute_for_automatic_optimization: <p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is an insufficient capacity to perform the action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.ipv6_cidr_block_not_found_exception.Ipv6CidrBlockNotFoundException: <p>There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.update_workgroup_request.UpdateWorkgroupRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.update_workgroup_response.UpdateWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_workgroup

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.update_workgroup.update_workgroup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_workgroup_request.UpdateWorkgroupRequest = {
            "workgroup_name": workgroup_name
        }
        if base_capacity is not None:
            input_["base_capacity"] = base_capacity
        if enhanced_vpc_routing is not None:
            input_["enhanced_vpc_routing"] = enhanced_vpc_routing
        if config_parameters is not None:
            input_["config_parameters"] = config_parameters
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if port is not None:
            input_["port"] = port
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if price_performance_target is not None:
            input_["price_performance_target"] = price_performance_target
        if track_name is not None:
            input_["track_name"] = track_name
        if extra_compute_for_automatic_optimization is not None:
            input_["extra_compute_for_automatic_optimization"] = (
                extra_compute_for_automatic_optimization
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
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_workgroup_response.DeleteWorkgroupResponse":
        """<p>Deletes a workgroup.</p>

        Args:
            workgroup_name: <p>The name of the workgroup to be deleted.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.delete_workgroup_request.DeleteWorkgroupRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.delete_workgroup_response.DeleteWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_workgroup

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.delete_workgroup.delete_workgroup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_workgroup_request.DeleteWorkgroupRequest = {
            "workgroup_name": workgroup_name
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
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> (
        "capo_redshift_serverless.types.list_workgroups_response.ListWorkgroupsResponse"
    ):
        """<p>Returns information about a list of specified workgroups.</p>

        Args:
            next_token: <p>If your initial ListWorkgroups operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following ListNamespaces operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.list_workgroups_request.ListWorkgroupsRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.list_workgroups_response.ListWorkgroupsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_workgroups

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.list_workgroups.list_workgroups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_workgroups_request.ListWorkgroupsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWorkgroupResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def put(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        base_capacity: Optional[int] = None,
        enhanced_vpc_routing: Optional[bool] = None,
        config_parameters: Optional[
            "capo_redshift_serverless.types.config_parameter_list.ConfigParameterList"
        ] = None,
        security_group_ids: Optional[
            "capo_redshift_serverless.types.security_group_id_list.SecurityGroupIdList"
        ] = None,
        subnet_ids: Optional[
            "capo_redshift_serverless.types.subnet_id_list.SubnetIdList"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
        port: Optional[int] = None,
        max_capacity: Optional[int] = None,
        price_performance_target: Optional[
            "capo_redshift_serverless.types.performance_target.PerformanceTarget"
        ] = None,
        ip_address_type: Optional[
            "capo_redshift_serverless.types.ip_address_type.IpAddressType"
        ] = None,
        track_name: Optional[
            "capo_redshift_serverless.types.track_name.TrackName"
        ] = None,
        extra_compute_for_automatic_optimization: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.create_workgroup_response.CreateWorkgroupResponse":
        """<p>Creates an workgroup in Amazon Redshift Serverless.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a workgroup is in an account with VPC BPA turned on, the following capabilities are blocked: </p> <ul> <li> <p>Creating a public access workgroup</p> </li> <li> <p>Modifying a private workgroup to public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the workgroup when the workgroup is public</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            workgroup_name: <p>The name of the created workgroup.</p>
            namespace_name: <p>The name of the namespace to associate with the workgroup.</p>
            base_capacity: <p>The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).</p>
            enhanced_vpc_routing: <p>The value that specifies whether to turn on enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC instead of over the internet.</p>
            config_parameters: <p>An array of parameters to set for advanced control over a database. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. If you're using <code>wlm_json_configuration</code>, the maximum size of <code>parameterValue</code> is 8000 characters. For more information about query monitoring rules and available metrics, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless"> Query monitoring metrics for Amazon Redshift Serverless</a>.</p>
            security_group_ids: <p>An array of security group IDs to associate with the workgroup.</p>
            subnet_ids: <p>An array of VPC subnet IDs to associate with the workgroup.</p>
            publicly_accessible: <p>A value that specifies whether the workgroup can be accessed from a public network.</p>
            tags: <p>A array of tag instances.</p>
            port: <p>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</p>
            max_capacity: <p>The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.</p>
            price_performance_target: <p>An object that represents the price performance target settings for the workgroup.</p>
            ip_address_type: <p>The IP address type that the workgroup supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>
            track_name: <p>An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the <code>current</code> track.</p>
            extra_compute_for_automatic_optimization: <p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is an insufficient capacity to perform the action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.ipv6_cidr_block_not_found_exception.Ipv6CidrBlockNotFoundException: <p>There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_workgroup_request.CreateWorkgroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_workgroup_response.CreateWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_workgroup

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_workgroup.async_create_workgroup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_workgroup_request.CreateWorkgroupRequest = {
            "workgroup_name": workgroup_name,
            "namespace_name": namespace_name,
        }
        if base_capacity is not None:
            input_["base_capacity"] = base_capacity
        if enhanced_vpc_routing is not None:
            input_["enhanced_vpc_routing"] = enhanced_vpc_routing
        if config_parameters is not None:
            input_["config_parameters"] = config_parameters
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if tags is not None:
            input_["tags"] = tags
        if port is not None:
            input_["port"] = port
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if price_performance_target is not None:
            input_["price_performance_target"] = price_performance_target
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if track_name is not None:
            input_["track_name"] = track_name
        if extra_compute_for_automatic_optimization is not None:
            input_["extra_compute_for_automatic_optimization"] = (
                extra_compute_for_automatic_optimization
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_workgroup_response.GetWorkgroupResponse":
        """<p>Returns information about a specific workgroup.</p>

        Args:
            workgroup_name: <p>The name of the workgroup to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_workgroup_request.GetWorkgroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_workgroup_response.GetWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_workgroup

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_workgroup.async_get_workgroup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_workgroup_request.GetWorkgroupRequest = {
            "workgroup_name": workgroup_name
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
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        base_capacity: Optional[int] = None,
        enhanced_vpc_routing: Optional[bool] = None,
        config_parameters: Optional[
            "capo_redshift_serverless.types.config_parameter_list.ConfigParameterList"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        subnet_ids: Optional[
            "capo_redshift_serverless.types.subnet_id_list.SubnetIdList"
        ] = None,
        security_group_ids: Optional[
            "capo_redshift_serverless.types.security_group_id_list.SecurityGroupIdList"
        ] = None,
        port: Optional[int] = None,
        max_capacity: Optional[int] = None,
        ip_address_type: Optional[
            "capo_redshift_serverless.types.ip_address_type.IpAddressType"
        ] = None,
        price_performance_target: Optional[
            "capo_redshift_serverless.types.performance_target.PerformanceTarget"
        ] = None,
        track_name: Optional[
            "capo_redshift_serverless.types.track_name.TrackName"
        ] = None,
        extra_compute_for_automatic_optimization: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.update_workgroup_response.UpdateWorkgroupResponse":
        """<p>Updates a workgroup with the specified configuration settings. You can't update multiple parameters in one request. For example, you can update <code>baseCapacity</code> or <code>port</code> in a single request, but you can't update both in the same request.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a workgroup is in an account with VPC BPA turned on, the following capabilities are blocked: </p> <ul> <li> <p>Creating a public access workgroup</p> </li> <li> <p>Modifying a private workgroup to public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the workgroup when the workgroup is public</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            workgroup_name: <p>The name of the workgroup to update. You can't update the name of a workgroup once it is created.</p>
            base_capacity: <p>The new base data warehouse capacity in Redshift Processing Units (RPUs).</p>
            enhanced_vpc_routing: <p>The value that specifies whether to turn on enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.</p>
            config_parameters: <p>An array of parameters to set for advanced control over a database. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. If you're using <code>wlm_json_configuration</code>, the maximum size of <code>parameterValue</code> is 8000 characters. For more information about query monitoring rules and available metrics, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless"> Query monitoring metrics for Amazon Redshift Serverless</a>.</p>
            publicly_accessible: <p>A value that specifies whether the workgroup can be accessible from a public network.</p>
            subnet_ids: <p>An array of VPC subnet IDs to associate with the workgroup.</p>
            security_group_ids: <p>An array of security group IDs to associate with the workgroup.</p>
            port: <p>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</p>
            max_capacity: <p>The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.</p>
            ip_address_type: <p>The IP address type that the workgroup supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>
            price_performance_target: <p>An object that represents the price performance target settings for the workgroup.</p>
            track_name: <p>An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the <code>current</code> track.</p>
            extra_compute_for_automatic_optimization: <p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is an insufficient capacity to perform the action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.ipv6_cidr_block_not_found_exception.Ipv6CidrBlockNotFoundException: <p>There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_workgroup_request.UpdateWorkgroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_workgroup_response.UpdateWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_workgroup

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_workgroup.async_update_workgroup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_workgroup_request.UpdateWorkgroupRequest = {
            "workgroup_name": workgroup_name
        }
        if base_capacity is not None:
            input_["base_capacity"] = base_capacity
        if enhanced_vpc_routing is not None:
            input_["enhanced_vpc_routing"] = enhanced_vpc_routing
        if config_parameters is not None:
            input_["config_parameters"] = config_parameters
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if port is not None:
            input_["port"] = port
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if price_performance_target is not None:
            input_["price_performance_target"] = price_performance_target
        if track_name is not None:
            input_["track_name"] = track_name
        if extra_compute_for_automatic_optimization is not None:
            input_["extra_compute_for_automatic_optimization"] = (
                extra_compute_for_automatic_optimization
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
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_workgroup_response.DeleteWorkgroupResponse":
        """<p>Deletes a workgroup.</p>

        Args:
            workgroup_name: <p>The name of the workgroup to be deleted.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_workgroup_request.DeleteWorkgroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_workgroup_response.DeleteWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_workgroup

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_workgroup.async_delete_workgroup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_workgroup_request.DeleteWorkgroupRequest = {
            "workgroup_name": workgroup_name
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
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> (
        "capo_redshift_serverless.types.list_workgroups_response.ListWorkgroupsResponse"
    ):
        """<p>Returns information about a list of specified workgroups.</p>

        Args:
            next_token: <p>If your initial ListWorkgroups operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following ListNamespaces operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_workgroups_request.ListWorkgroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_workgroups_response.ListWorkgroupsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_workgroups

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_workgroups.async_list_workgroups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_workgroups_request.ListWorkgroupsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
