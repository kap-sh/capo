from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_emr_serverless._auth._signers
import capo_emr_serverless._auth._sigv4
from capo_emr_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.application_name
    import capo_emr_serverless.types.application_state_set
    import capo_emr_serverless.types.application_summary
    import capo_emr_serverless.types.architecture
    import capo_emr_serverless.types.auto_start_config
    import capo_emr_serverless.types.auto_stop_config
    import capo_emr_serverless.types.client_token
    import capo_emr_serverless.types.configuration_list
    import capo_emr_serverless.types.create_application_request
    import capo_emr_serverless.types.create_application_response
    import capo_emr_serverless.types.delete_application_request
    import capo_emr_serverless.types.delete_application_response
    import capo_emr_serverless.types.disk_encryption_configuration
    import capo_emr_serverless.types.engine_type
    import capo_emr_serverless.types.get_application_request
    import capo_emr_serverless.types.get_application_response
    import capo_emr_serverless.types.get_resource_dashboard_request
    import capo_emr_serverless.types.get_resource_dashboard_response
    import capo_emr_serverless.types.identity_center_configuration_input
    import capo_emr_serverless.types.image_configuration_input
    import capo_emr_serverless.types.initial_capacity_config_map
    import capo_emr_serverless.types.interactive_configuration
    import capo_emr_serverless.types.job_level_cost_allocation_configuration
    import capo_emr_serverless.types.list_applications_request
    import capo_emr_serverless.types.list_applications_response
    import capo_emr_serverless.types.maximum_allowed_resources
    import capo_emr_serverless.types.monitoring_configuration
    import capo_emr_serverless.types.network_configuration
    import capo_emr_serverless.types.next_token
    import capo_emr_serverless.types.release_label
    import capo_emr_serverless.types.resource_id
    import capo_emr_serverless.types.resource_type
    import capo_emr_serverless.types.scheduler_configuration
    import capo_emr_serverless.types.start_application_request
    import capo_emr_serverless.types.start_application_response
    import capo_emr_serverless.types.stop_application_request
    import capo_emr_serverless.types.stop_application_response
    import capo_emr_serverless.types.tag_map
    import capo_emr_serverless.types.update_application_request
    import capo_emr_serverless.types.update_application_response
    import capo_emr_serverless.types.worker_type_specification_input_map
    from capo_emr_serverless._services.async_emr_serverless import (
        AsyncEMRServerlessClient,
        AsyncEMRServerlessClientConfig,
    )
    from capo_emr_serverless._services.emr_serverless import (
        EMRServerlessClient,
        EMRServerlessClientConfig,
    )


class ApplicationResource:
    def __init__(self, service: EMRServerlessClient) -> None:
        self._service = service

    def create(
        self,
        release_label: "capo_emr_serverless.types.release_label.ReleaseLabel",
        type: "capo_emr_serverless.types.engine_type.EngineType",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        name: Optional[
            "capo_emr_serverless.types.application_name.ApplicationName"
        ] = None,
        initial_capacity: Optional[
            "capo_emr_serverless.types.initial_capacity_config_map.InitialCapacityConfigMap"
        ] = None,
        maximum_capacity: Optional[
            "capo_emr_serverless.types.maximum_allowed_resources.MaximumAllowedResources"
        ] = None,
        tags: Optional["capo_emr_serverless.types.tag_map.TagMap"] = None,
        auto_start_configuration: Optional[
            "capo_emr_serverless.types.auto_start_config.AutoStartConfig"
        ] = None,
        auto_stop_configuration: Optional[
            "capo_emr_serverless.types.auto_stop_config.AutoStopConfig"
        ] = None,
        network_configuration: Optional[
            "capo_emr_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        architecture: Optional[
            "capo_emr_serverless.types.architecture.Architecture"
        ] = None,
        image_configuration: Optional[
            "capo_emr_serverless.types.image_configuration_input.ImageConfigurationInput"
        ] = None,
        worker_type_specifications: Optional[
            "capo_emr_serverless.types.worker_type_specification_input_map.WorkerTypeSpecificationInputMap"
        ] = None,
        runtime_configuration: Optional[
            "capo_emr_serverless.types.configuration_list.ConfigurationList"
        ] = None,
        monitoring_configuration: Optional[
            "capo_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
        disk_encryption_configuration: Optional[
            "capo_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
        ] = None,
        interactive_configuration: Optional[
            "capo_emr_serverless.types.interactive_configuration.InteractiveConfiguration"
        ] = None,
        scheduler_configuration: Optional[
            "capo_emr_serverless.types.scheduler_configuration.SchedulerConfiguration"
        ] = None,
        identity_center_configuration: Optional[
            "capo_emr_serverless.types.identity_center_configuration_input.IdentityCenterConfigurationInput"
        ] = None,
        job_level_cost_allocation_configuration: Optional[
            "capo_emr_serverless.types.job_level_cost_allocation_configuration.JobLevelCostAllocationConfiguration"
        ] = None,
    ) -> "capo_emr_serverless.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an application.</p>

        Args:
            name: <p>The name of the application.</p>
            release_label: <p>The Amazon EMR release associated with the application.</p>
            type: <p>The type of application you want to start, such as Spark or Hive.</p>
            client_token: <p>The client idempotency token of the application to create. Its value must be unique for each request.</p>
            initial_capacity: <p>The capacity to initialize when the application is created.</p>
            maximum_capacity: <p>The maximum capacity to allocate when the application is created. This is cumulative across all workers at any given point in time, not just when an application is created. No new resources will be created once any one of the defined limits is hit.</p>
            tags: <p>The tags assigned to the application.</p>
            auto_start_configuration: <p>The configuration for an application to automatically start on job submission.</p>
            auto_stop_configuration: <p>The configuration for an application to automatically stop after a certain amount of time being idle.</p>
            network_configuration: <p>The network configuration for customer VPC connectivity.</p>
            architecture: <p>The CPU architecture of an application.</p>
            image_configuration: <p>The image configuration for all worker types. You can either set this parameter or <code>imageConfiguration</code> for each worker type in <code>workerTypeSpecifications</code>.</p>
            worker_type_specifications: <p>The key-value pairs that specify worker type to <code>WorkerTypeSpecificationInput</code>. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include <code>Driver</code> and <code>Executor</code> for Spark applications and <code>HiveDriver</code> and <code>TezTask</code> for Hive applications. You can either set image details in this parameter for each worker type, or in <code>imageConfiguration</code> for all worker types.</p>
            runtime_configuration: <p>The <a href="https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html">Configuration</a> specifications to use when creating an application. Each configuration consists of a classification and properties. This configuration is applied to all the job runs submitted under the application.</p>
            monitoring_configuration: <p>The configuration setting for monitoring.</p>
            disk_encryption_configuration: <p>The configuration object that allows encrypting local disks.</p>
            interactive_configuration: <p>The interactive configuration object that enables the interactive use cases to use when running an application.</p>
            scheduler_configuration: <p>The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.</p>
            identity_center_configuration: <p>The IAM Identity Center Configuration accepts the Identity Center instance parameter required to enable trusted identity propagation. This configuration allows identity propagation between integrated services and the Identity Center instance.</p>
            job_level_cost_allocation_configuration: <p>The configuration object that enables job level cost allocation.</p>

        Raises:
            capo_emr_serverless.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.create_application

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.create_application_request.CreateApplicationRequest = {
            "release_label": release_label,
            "type": type,
            "client_token": client_token,
        }
        if name is not None:
            input_["name"] = name
        if initial_capacity is not None:
            input_["initial_capacity"] = initial_capacity
        if maximum_capacity is not None:
            input_["maximum_capacity"] = maximum_capacity
        if tags is not None:
            input_["tags"] = tags
        if auto_start_configuration is not None:
            input_["auto_start_configuration"] = auto_start_configuration
        if auto_stop_configuration is not None:
            input_["auto_stop_configuration"] = auto_stop_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if architecture is not None:
            input_["architecture"] = architecture
        if image_configuration is not None:
            input_["image_configuration"] = image_configuration
        if worker_type_specifications is not None:
            input_["worker_type_specifications"] = worker_type_specifications
        if runtime_configuration is not None:
            input_["runtime_configuration"] = runtime_configuration
        if monitoring_configuration is not None:
            input_["monitoring_configuration"] = monitoring_configuration
        if disk_encryption_configuration is not None:
            input_["disk_encryption_configuration"] = disk_encryption_configuration
        if interactive_configuration is not None:
            input_["interactive_configuration"] = interactive_configuration
        if scheduler_configuration is not None:
            input_["scheduler_configuration"] = scheduler_configuration
        if identity_center_configuration is not None:
            input_["identity_center_configuration"] = identity_center_configuration
        if job_level_cost_allocation_configuration is not None:
            input_["job_level_cost_allocation_configuration"] = (
                job_level_cost_allocation_configuration
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_application_response.GetApplicationResponse":
        """<p>Displays detailed information about a specified application.</p>

        Args:
            application_id: <p>The ID of the application that will be described.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_application

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        initial_capacity: Optional[
            "capo_emr_serverless.types.initial_capacity_config_map.InitialCapacityConfigMap"
        ] = None,
        maximum_capacity: Optional[
            "capo_emr_serverless.types.maximum_allowed_resources.MaximumAllowedResources"
        ] = None,
        auto_start_configuration: Optional[
            "capo_emr_serverless.types.auto_start_config.AutoStartConfig"
        ] = None,
        auto_stop_configuration: Optional[
            "capo_emr_serverless.types.auto_stop_config.AutoStopConfig"
        ] = None,
        network_configuration: Optional[
            "capo_emr_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        architecture: Optional[
            "capo_emr_serverless.types.architecture.Architecture"
        ] = None,
        image_configuration: Optional[
            "capo_emr_serverless.types.image_configuration_input.ImageConfigurationInput"
        ] = None,
        worker_type_specifications: Optional[
            "capo_emr_serverless.types.worker_type_specification_input_map.WorkerTypeSpecificationInputMap"
        ] = None,
        interactive_configuration: Optional[
            "capo_emr_serverless.types.interactive_configuration.InteractiveConfiguration"
        ] = None,
        release_label: Optional[
            "capo_emr_serverless.types.release_label.ReleaseLabel"
        ] = None,
        runtime_configuration: Optional[
            "capo_emr_serverless.types.configuration_list.ConfigurationList"
        ] = None,
        monitoring_configuration: Optional[
            "capo_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
        disk_encryption_configuration: Optional[
            "capo_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
        ] = None,
        scheduler_configuration: Optional[
            "capo_emr_serverless.types.scheduler_configuration.SchedulerConfiguration"
        ] = None,
        identity_center_configuration: Optional[
            "capo_emr_serverless.types.identity_center_configuration_input.IdentityCenterConfigurationInput"
        ] = None,
        job_level_cost_allocation_configuration: Optional[
            "capo_emr_serverless.types.job_level_cost_allocation_configuration.JobLevelCostAllocationConfiguration"
        ] = None,
    ) -> "capo_emr_serverless.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates a specified application. An application has to be in a stopped or created state in order to be updated.</p>

        Args:
            application_id: <p>The ID of the application to update.</p>
            client_token: <p>The client idempotency token of the application to update. Its value must be unique for each request.</p>
            initial_capacity: <p>The capacity to initialize when the application is updated.</p>
            maximum_capacity: <p>The maximum capacity to allocate when the application is updated. This is cumulative across all workers at any given point in time during the lifespan of the application. No new resources will be created once any one of the defined limits is hit.</p>
            auto_start_configuration: <p>The configuration for an application to automatically start on job submission.</p>
            auto_stop_configuration: <p>The configuration for an application to automatically stop after a certain amount of time being idle.</p>
            architecture: <p>The CPU architecture of an application.</p>
            image_configuration: <p>The image configuration to be used for all worker types. You can either set this parameter or <code>imageConfiguration</code> for each worker type in <code>WorkerTypeSpecificationInput</code>.</p>
            worker_type_specifications: <p>The key-value pairs that specify worker type to <code>WorkerTypeSpecificationInput</code>. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include <code>Driver</code> and <code>Executor</code> for Spark applications and <code>HiveDriver</code> and <code>TezTask</code> for Hive applications. You can either set image details in this parameter for each worker type, or in <code>imageConfiguration</code> for all worker types.</p>
            interactive_configuration: <p>The interactive configuration object that contains new interactive use cases when the application is updated.</p>
            release_label: <p>The Amazon EMR release label for the application. You can change the release label to use a different release of Amazon EMR.</p>
            runtime_configuration: <p>The <a href="https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html">Configuration</a> specifications to use when updating an application. Each configuration consists of a classification and properties. This configuration is applied across all the job runs submitted under the application.</p>
            monitoring_configuration: <p>The configuration setting for monitoring.</p>
            disk_encryption_configuration: <p>The configuration object that allows encrypting local disks.</p>
            scheduler_configuration: <p>The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.</p>
            identity_center_configuration: <p>Specifies the IAM Identity Center configuration used to enable or disable trusted identity propagation. When provided, this configuration determines how the application interacts with IAM Identity Center for user authentication and access control.</p>
            job_level_cost_allocation_configuration: <p>The configuration object that enables job level cost allocation.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.update_application

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id,
            "client_token": client_token,
        }
        if initial_capacity is not None:
            input_["initial_capacity"] = initial_capacity
        if maximum_capacity is not None:
            input_["maximum_capacity"] = maximum_capacity
        if auto_start_configuration is not None:
            input_["auto_start_configuration"] = auto_start_configuration
        if auto_stop_configuration is not None:
            input_["auto_stop_configuration"] = auto_stop_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if architecture is not None:
            input_["architecture"] = architecture
        if image_configuration is not None:
            input_["image_configuration"] = image_configuration
        if worker_type_specifications is not None:
            input_["worker_type_specifications"] = worker_type_specifications
        if interactive_configuration is not None:
            input_["interactive_configuration"] = interactive_configuration
        if release_label is not None:
            input_["release_label"] = release_label
        if runtime_configuration is not None:
            input_["runtime_configuration"] = runtime_configuration
        if monitoring_configuration is not None:
            input_["monitoring_configuration"] = monitoring_configuration
        if disk_encryption_configuration is not None:
            input_["disk_encryption_configuration"] = disk_encryption_configuration
        if scheduler_configuration is not None:
            input_["scheduler_configuration"] = scheduler_configuration
        if identity_center_configuration is not None:
            input_["identity_center_configuration"] = identity_center_configuration
        if job_level_cost_allocation_configuration is not None:
            input_["job_level_cost_allocation_configuration"] = (
                job_level_cost_allocation_configuration
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an application. An application has to be in a stopped or created state in order to be deleted.</p>

        Args:
            application_id: <p>The ID of the application that will be deleted.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.delete_application

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
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
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        states: Optional[
            "capo_emr_serverless.types.application_state_set.ApplicationStateSet"
        ] = None,
    ) -> (
        "capo_emr_serverless.types.list_applications_response.ListApplicationsResponse"
    ):
        """<p>Lists applications based on a set of parameters.</p>

        Args:
            next_token: <p>The token for the next set of application results.</p>
            max_results: <p>The maximum number of applications that can be listed.</p>
            states: <p>An optional filter for application states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_applications

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if states is not None:
            input_["states"] = states

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_dashboard(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        resource_id: "capo_emr_serverless.types.resource_id.ResourceId",
        resource_type: "capo_emr_serverless.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        access_system_profile_logs: Optional[bool] = None,
    ) -> "capo_emr_serverless.types.get_resource_dashboard_response.GetResourceDashboardResponse":
        """<p>Returns a URL that you can use to access the application UIs for a specified resource, such as a session.</p> <p>For resources in a running state, the application UI is a live user interface such as the Spark web UI. For terminated resources, the application UI is a persistent application user interface such as the Spark History Server.</p> <note> <p>The URL is valid for one hour after you generate it. To access the application UI after that hour elapses, you must invoke the API again to generate a new URL.</p> </note>

        Args:
            application_id: <p>The ID of the application that the resource belongs to.</p>
            resource_id: <p>The ID of the resource.</p>
            resource_type: <p>The type of resource to access the dashboard for. Currently, only <code>Session</code> is supported.</p>
            access_system_profile_logs: <p>Allows access to system profile logs for Lake Formation-enabled sessions. Default is false.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.get_resource_dashboard_request.GetResourceDashboardRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.get_resource_dashboard_response.GetResourceDashboardResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_resource_dashboard

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.get_resource_dashboard.get_resource_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_resource_dashboard_request.GetResourceDashboardRequest = {
            "application_id": application_id,
            "resource_id": resource_id,
            "resource_type": resource_type,
        }
        if access_system_profile_logs is not None:
            input_["access_system_profile_logs"] = access_system_profile_logs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_application(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> (
        "capo_emr_serverless.types.start_application_response.StartApplicationResponse"
    ):
        """<p>Starts a specified application and initializes initial capacity if configured.</p>

        Args:
            application_id: <p>The ID of the application to start.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The maximum number of resources per account has been reached.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.start_application_request.StartApplicationRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.start_application_response.StartApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.start_application

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.start_application.start_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.start_application_request.StartApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_application(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.stop_application_response.StopApplicationResponse":
        """<p>Stops a specified application and releases initial capacity if configured. All scheduled and running jobs must be completed or cancelled before stopping an application.</p>

        Args:
            application_id: <p>The ID of the application to stop.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.stop_application_request.StopApplicationRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.stop_application_response.StopApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.stop_application

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.stop_application.stop_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.stop_application_request.StopApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncApplicationResource:
    def __init__(self, service: AsyncEMRServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        release_label: "capo_emr_serverless.types.release_label.ReleaseLabel",
        type: "capo_emr_serverless.types.engine_type.EngineType",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        name: Optional[
            "capo_emr_serverless.types.application_name.ApplicationName"
        ] = None,
        initial_capacity: Optional[
            "capo_emr_serverless.types.initial_capacity_config_map.InitialCapacityConfigMap"
        ] = None,
        maximum_capacity: Optional[
            "capo_emr_serverless.types.maximum_allowed_resources.MaximumAllowedResources"
        ] = None,
        tags: Optional["capo_emr_serverless.types.tag_map.TagMap"] = None,
        auto_start_configuration: Optional[
            "capo_emr_serverless.types.auto_start_config.AutoStartConfig"
        ] = None,
        auto_stop_configuration: Optional[
            "capo_emr_serverless.types.auto_stop_config.AutoStopConfig"
        ] = None,
        network_configuration: Optional[
            "capo_emr_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        architecture: Optional[
            "capo_emr_serverless.types.architecture.Architecture"
        ] = None,
        image_configuration: Optional[
            "capo_emr_serverless.types.image_configuration_input.ImageConfigurationInput"
        ] = None,
        worker_type_specifications: Optional[
            "capo_emr_serverless.types.worker_type_specification_input_map.WorkerTypeSpecificationInputMap"
        ] = None,
        runtime_configuration: Optional[
            "capo_emr_serverless.types.configuration_list.ConfigurationList"
        ] = None,
        monitoring_configuration: Optional[
            "capo_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
        disk_encryption_configuration: Optional[
            "capo_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
        ] = None,
        interactive_configuration: Optional[
            "capo_emr_serverless.types.interactive_configuration.InteractiveConfiguration"
        ] = None,
        scheduler_configuration: Optional[
            "capo_emr_serverless.types.scheduler_configuration.SchedulerConfiguration"
        ] = None,
        identity_center_configuration: Optional[
            "capo_emr_serverless.types.identity_center_configuration_input.IdentityCenterConfigurationInput"
        ] = None,
        job_level_cost_allocation_configuration: Optional[
            "capo_emr_serverless.types.job_level_cost_allocation_configuration.JobLevelCostAllocationConfiguration"
        ] = None,
    ) -> "capo_emr_serverless.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an application.</p>

        Args:
            name: <p>The name of the application.</p>
            release_label: <p>The Amazon EMR release associated with the application.</p>
            type: <p>The type of application you want to start, such as Spark or Hive.</p>
            client_token: <p>The client idempotency token of the application to create. Its value must be unique for each request.</p>
            initial_capacity: <p>The capacity to initialize when the application is created.</p>
            maximum_capacity: <p>The maximum capacity to allocate when the application is created. This is cumulative across all workers at any given point in time, not just when an application is created. No new resources will be created once any one of the defined limits is hit.</p>
            tags: <p>The tags assigned to the application.</p>
            auto_start_configuration: <p>The configuration for an application to automatically start on job submission.</p>
            auto_stop_configuration: <p>The configuration for an application to automatically stop after a certain amount of time being idle.</p>
            network_configuration: <p>The network configuration for customer VPC connectivity.</p>
            architecture: <p>The CPU architecture of an application.</p>
            image_configuration: <p>The image configuration for all worker types. You can either set this parameter or <code>imageConfiguration</code> for each worker type in <code>workerTypeSpecifications</code>.</p>
            worker_type_specifications: <p>The key-value pairs that specify worker type to <code>WorkerTypeSpecificationInput</code>. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include <code>Driver</code> and <code>Executor</code> for Spark applications and <code>HiveDriver</code> and <code>TezTask</code> for Hive applications. You can either set image details in this parameter for each worker type, or in <code>imageConfiguration</code> for all worker types.</p>
            runtime_configuration: <p>The <a href="https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html">Configuration</a> specifications to use when creating an application. Each configuration consists of a classification and properties. This configuration is applied to all the job runs submitted under the application.</p>
            monitoring_configuration: <p>The configuration setting for monitoring.</p>
            disk_encryption_configuration: <p>The configuration object that allows encrypting local disks.</p>
            interactive_configuration: <p>The interactive configuration object that enables the interactive use cases to use when running an application.</p>
            scheduler_configuration: <p>The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.</p>
            identity_center_configuration: <p>The IAM Identity Center Configuration accepts the Identity Center instance parameter required to enable trusted identity propagation. This configuration allows identity propagation between integrated services and the Identity Center instance.</p>
            job_level_cost_allocation_configuration: <p>The configuration object that enables job level cost allocation.</p>

        Raises:
            capo_emr_serverless.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.create_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.create_application_request.CreateApplicationRequest = {
            "release_label": release_label,
            "type": type,
            "client_token": client_token,
        }
        if name is not None:
            input_["name"] = name
        if initial_capacity is not None:
            input_["initial_capacity"] = initial_capacity
        if maximum_capacity is not None:
            input_["maximum_capacity"] = maximum_capacity
        if tags is not None:
            input_["tags"] = tags
        if auto_start_configuration is not None:
            input_["auto_start_configuration"] = auto_start_configuration
        if auto_stop_configuration is not None:
            input_["auto_stop_configuration"] = auto_stop_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if architecture is not None:
            input_["architecture"] = architecture
        if image_configuration is not None:
            input_["image_configuration"] = image_configuration
        if worker_type_specifications is not None:
            input_["worker_type_specifications"] = worker_type_specifications
        if runtime_configuration is not None:
            input_["runtime_configuration"] = runtime_configuration
        if monitoring_configuration is not None:
            input_["monitoring_configuration"] = monitoring_configuration
        if disk_encryption_configuration is not None:
            input_["disk_encryption_configuration"] = disk_encryption_configuration
        if interactive_configuration is not None:
            input_["interactive_configuration"] = interactive_configuration
        if scheduler_configuration is not None:
            input_["scheduler_configuration"] = scheduler_configuration
        if identity_center_configuration is not None:
            input_["identity_center_configuration"] = identity_center_configuration
        if job_level_cost_allocation_configuration is not None:
            input_["job_level_cost_allocation_configuration"] = (
                job_level_cost_allocation_configuration
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_application_response.GetApplicationResponse":
        """<p>Displays detailed information about a specified application.</p>

        Args:
            application_id: <p>The ID of the application that will be described.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        initial_capacity: Optional[
            "capo_emr_serverless.types.initial_capacity_config_map.InitialCapacityConfigMap"
        ] = None,
        maximum_capacity: Optional[
            "capo_emr_serverless.types.maximum_allowed_resources.MaximumAllowedResources"
        ] = None,
        auto_start_configuration: Optional[
            "capo_emr_serverless.types.auto_start_config.AutoStartConfig"
        ] = None,
        auto_stop_configuration: Optional[
            "capo_emr_serverless.types.auto_stop_config.AutoStopConfig"
        ] = None,
        network_configuration: Optional[
            "capo_emr_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        architecture: Optional[
            "capo_emr_serverless.types.architecture.Architecture"
        ] = None,
        image_configuration: Optional[
            "capo_emr_serverless.types.image_configuration_input.ImageConfigurationInput"
        ] = None,
        worker_type_specifications: Optional[
            "capo_emr_serverless.types.worker_type_specification_input_map.WorkerTypeSpecificationInputMap"
        ] = None,
        interactive_configuration: Optional[
            "capo_emr_serverless.types.interactive_configuration.InteractiveConfiguration"
        ] = None,
        release_label: Optional[
            "capo_emr_serverless.types.release_label.ReleaseLabel"
        ] = None,
        runtime_configuration: Optional[
            "capo_emr_serverless.types.configuration_list.ConfigurationList"
        ] = None,
        monitoring_configuration: Optional[
            "capo_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
        disk_encryption_configuration: Optional[
            "capo_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
        ] = None,
        scheduler_configuration: Optional[
            "capo_emr_serverless.types.scheduler_configuration.SchedulerConfiguration"
        ] = None,
        identity_center_configuration: Optional[
            "capo_emr_serverless.types.identity_center_configuration_input.IdentityCenterConfigurationInput"
        ] = None,
        job_level_cost_allocation_configuration: Optional[
            "capo_emr_serverless.types.job_level_cost_allocation_configuration.JobLevelCostAllocationConfiguration"
        ] = None,
    ) -> "capo_emr_serverless.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates a specified application. An application has to be in a stopped or created state in order to be updated.</p>

        Args:
            application_id: <p>The ID of the application to update.</p>
            client_token: <p>The client idempotency token of the application to update. Its value must be unique for each request.</p>
            initial_capacity: <p>The capacity to initialize when the application is updated.</p>
            maximum_capacity: <p>The maximum capacity to allocate when the application is updated. This is cumulative across all workers at any given point in time during the lifespan of the application. No new resources will be created once any one of the defined limits is hit.</p>
            auto_start_configuration: <p>The configuration for an application to automatically start on job submission.</p>
            auto_stop_configuration: <p>The configuration for an application to automatically stop after a certain amount of time being idle.</p>
            architecture: <p>The CPU architecture of an application.</p>
            image_configuration: <p>The image configuration to be used for all worker types. You can either set this parameter or <code>imageConfiguration</code> for each worker type in <code>WorkerTypeSpecificationInput</code>.</p>
            worker_type_specifications: <p>The key-value pairs that specify worker type to <code>WorkerTypeSpecificationInput</code>. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include <code>Driver</code> and <code>Executor</code> for Spark applications and <code>HiveDriver</code> and <code>TezTask</code> for Hive applications. You can either set image details in this parameter for each worker type, or in <code>imageConfiguration</code> for all worker types.</p>
            interactive_configuration: <p>The interactive configuration object that contains new interactive use cases when the application is updated.</p>
            release_label: <p>The Amazon EMR release label for the application. You can change the release label to use a different release of Amazon EMR.</p>
            runtime_configuration: <p>The <a href="https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html">Configuration</a> specifications to use when updating an application. Each configuration consists of a classification and properties. This configuration is applied across all the job runs submitted under the application.</p>
            monitoring_configuration: <p>The configuration setting for monitoring.</p>
            disk_encryption_configuration: <p>The configuration object that allows encrypting local disks.</p>
            scheduler_configuration: <p>The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.</p>
            identity_center_configuration: <p>Specifies the IAM Identity Center configuration used to enable or disable trusted identity propagation. When provided, this configuration determines how the application interacts with IAM Identity Center for user authentication and access control.</p>
            job_level_cost_allocation_configuration: <p>The configuration object that enables job level cost allocation.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.update_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id,
            "client_token": client_token,
        }
        if initial_capacity is not None:
            input_["initial_capacity"] = initial_capacity
        if maximum_capacity is not None:
            input_["maximum_capacity"] = maximum_capacity
        if auto_start_configuration is not None:
            input_["auto_start_configuration"] = auto_start_configuration
        if auto_stop_configuration is not None:
            input_["auto_stop_configuration"] = auto_stop_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if architecture is not None:
            input_["architecture"] = architecture
        if image_configuration is not None:
            input_["image_configuration"] = image_configuration
        if worker_type_specifications is not None:
            input_["worker_type_specifications"] = worker_type_specifications
        if interactive_configuration is not None:
            input_["interactive_configuration"] = interactive_configuration
        if release_label is not None:
            input_["release_label"] = release_label
        if runtime_configuration is not None:
            input_["runtime_configuration"] = runtime_configuration
        if monitoring_configuration is not None:
            input_["monitoring_configuration"] = monitoring_configuration
        if disk_encryption_configuration is not None:
            input_["disk_encryption_configuration"] = disk_encryption_configuration
        if scheduler_configuration is not None:
            input_["scheduler_configuration"] = scheduler_configuration
        if identity_center_configuration is not None:
            input_["identity_center_configuration"] = identity_center_configuration
        if job_level_cost_allocation_configuration is not None:
            input_["job_level_cost_allocation_configuration"] = (
                job_level_cost_allocation_configuration
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an application. An application has to be in a stopped or created state in order to be deleted.</p>

        Args:
            application_id: <p>The ID of the application that will be deleted.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.delete_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
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
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        states: Optional[
            "capo_emr_serverless.types.application_state_set.ApplicationStateSet"
        ] = None,
    ) -> (
        "capo_emr_serverless.types.list_applications_response.ListApplicationsResponse"
    ):
        """<p>Lists applications based on a set of parameters.</p>

        Args:
            next_token: <p>The token for the next set of application results.</p>
            max_results: <p>The maximum number of applications that can be listed.</p>
            states: <p>An optional filter for application states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_applications

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if states is not None:
            input_["states"] = states

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_dashboard(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        resource_id: "capo_emr_serverless.types.resource_id.ResourceId",
        resource_type: "capo_emr_serverless.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        access_system_profile_logs: Optional[bool] = None,
    ) -> "capo_emr_serverless.types.get_resource_dashboard_response.GetResourceDashboardResponse":
        """<p>Returns a URL that you can use to access the application UIs for a specified resource, such as a session.</p> <p>For resources in a running state, the application UI is a live user interface such as the Spark web UI. For terminated resources, the application UI is a persistent application user interface such as the Spark History Server.</p> <note> <p>The URL is valid for one hour after you generate it. To access the application UI after that hour elapses, you must invoke the API again to generate a new URL.</p> </note>

        Args:
            application_id: <p>The ID of the application that the resource belongs to.</p>
            resource_id: <p>The ID of the resource.</p>
            resource_type: <p>The type of resource to access the dashboard for. Currently, only <code>Session</code> is supported.</p>
            access_system_profile_logs: <p>Allows access to system profile logs for Lake Formation-enabled sessions. Default is false.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_resource_dashboard_request.GetResourceDashboardRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_resource_dashboard_response.GetResourceDashboardResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_resource_dashboard

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_resource_dashboard.async_get_resource_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_resource_dashboard_request.GetResourceDashboardRequest = {
            "application_id": application_id,
            "resource_id": resource_id,
            "resource_type": resource_type,
        }
        if access_system_profile_logs is not None:
            input_["access_system_profile_logs"] = access_system_profile_logs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_application(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> (
        "capo_emr_serverless.types.start_application_response.StartApplicationResponse"
    ):
        """<p>Starts a specified application and initializes initial capacity if configured.</p>

        Args:
            application_id: <p>The ID of the application to start.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The maximum number of resources per account has been reached.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.start_application_request.StartApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.start_application_response.StartApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.start_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.start_application.async_start_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.start_application_request.StartApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_application(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.stop_application_response.StopApplicationResponse":
        """<p>Stops a specified application and releases initial capacity if configured. All scheduled and running jobs must be completed or cancelled before stopping an application.</p>

        Args:
            application_id: <p>The ID of the application to stop.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.stop_application_request.StopApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.stop_application_response.StopApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.stop_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.stop_application.async_stop_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.stop_application_request.StopApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
