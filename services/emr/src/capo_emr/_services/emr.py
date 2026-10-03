"""Generated from Smithy shape ``com.amazonaws.emr#ElasticMapReduce``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_emr._auth._signers
import capo_emr._auth._sigv4
from capo_emr._auth._identity import Credentials
from capo_emr._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_emr._auth._zapros_handler import AuthMiddleware
from capo_emr._pagination import resolve_path as _resolve_path
from capo_emr._services._aws_config import aws_config
from capo_emr._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_emr.types.add_instance_fleet_input
    import capo_emr.types.add_instance_fleet_output
    import capo_emr.types.add_instance_groups_input
    import capo_emr.types.add_instance_groups_output
    import capo_emr.types.add_job_flow_steps_input
    import capo_emr.types.add_job_flow_steps_output
    import capo_emr.types.add_tags_input
    import capo_emr.types.add_tags_output
    import capo_emr.types.application_list
    import capo_emr.types.arn_type
    import capo_emr.types.auth_mode
    import capo_emr.types.auto_scaling_policy
    import capo_emr.types.auto_termination_policy
    import capo_emr.types.block_public_access_configuration
    import capo_emr.types.boolean
    import capo_emr.types.boolean_object
    import capo_emr.types.bootstrap_action_config_list
    import capo_emr.types.cancel_steps_input
    import capo_emr.types.cancel_steps_output
    import capo_emr.types.client_request_token
    import capo_emr.types.cluster_id
    import capo_emr.types.cluster_state_list
    import capo_emr.types.cluster_summary
    import capo_emr.types.command
    import capo_emr.types.configuration_list
    import capo_emr.types.create_persistent_app_ui_input
    import capo_emr.types.create_persistent_app_ui_output
    import capo_emr.types.create_security_configuration_input
    import capo_emr.types.create_security_configuration_output
    import capo_emr.types.create_studio_input
    import capo_emr.types.create_studio_output
    import capo_emr.types.create_studio_session_mapping_input
    import capo_emr.types.date
    import capo_emr.types.delete_security_configuration_input
    import capo_emr.types.delete_security_configuration_output
    import capo_emr.types.delete_studio_input
    import capo_emr.types.delete_studio_session_mapping_input
    import capo_emr.types.describe_cluster_input
    import capo_emr.types.describe_cluster_output
    import capo_emr.types.describe_job_flows_input
    import capo_emr.types.describe_job_flows_output
    import capo_emr.types.describe_notebook_execution_input
    import capo_emr.types.describe_notebook_execution_output
    import capo_emr.types.describe_persistent_app_ui_input
    import capo_emr.types.describe_persistent_app_ui_output
    import capo_emr.types.describe_release_label_input
    import capo_emr.types.describe_release_label_output
    import capo_emr.types.describe_security_configuration_input
    import capo_emr.types.describe_security_configuration_output
    import capo_emr.types.describe_step_input
    import capo_emr.types.describe_step_output
    import capo_emr.types.describe_studio_input
    import capo_emr.types.describe_studio_output
    import capo_emr.types.emr_containers_config
    import capo_emr.types.environment_variables_map
    import capo_emr.types.execution_engine_config
    import capo_emr.types.get_auto_termination_policy_input
    import capo_emr.types.get_auto_termination_policy_output
    import capo_emr.types.get_block_public_access_configuration_input
    import capo_emr.types.get_block_public_access_configuration_output
    import capo_emr.types.get_cluster_session_credentials_input
    import capo_emr.types.get_cluster_session_credentials_output
    import capo_emr.types.get_managed_scaling_policy_input
    import capo_emr.types.get_managed_scaling_policy_output
    import capo_emr.types.get_on_cluster_app_ui_presigned_url_input
    import capo_emr.types.get_on_cluster_app_ui_presigned_url_output
    import capo_emr.types.get_persistent_app_ui_presigned_url_input
    import capo_emr.types.get_persistent_app_ui_presigned_url_output
    import capo_emr.types.get_session_endpoint_input
    import capo_emr.types.get_session_endpoint_output
    import capo_emr.types.get_session_input
    import capo_emr.types.get_session_output
    import capo_emr.types.get_studio_session_mapping_input
    import capo_emr.types.get_studio_session_mapping_output
    import capo_emr.types.iam_role_arn
    import capo_emr.types.idc_user_assignment
    import capo_emr.types.identity_type
    import capo_emr.types.instance
    import capo_emr.types.instance_fleet
    import capo_emr.types.instance_fleet_config
    import capo_emr.types.instance_fleet_id
    import capo_emr.types.instance_fleet_modify_config
    import capo_emr.types.instance_fleet_type
    import capo_emr.types.instance_group
    import capo_emr.types.instance_group_config_list
    import capo_emr.types.instance_group_id
    import capo_emr.types.instance_group_modify_config_list
    import capo_emr.types.instance_group_type_list
    import capo_emr.types.instance_state_list
    import capo_emr.types.integer
    import capo_emr.types.job_flow_execution_state_list
    import capo_emr.types.job_flow_instances_config
    import capo_emr.types.kerberos_attributes
    import capo_emr.types.list_bootstrap_actions_input
    import capo_emr.types.list_bootstrap_actions_output
    import capo_emr.types.list_clusters_input
    import capo_emr.types.list_clusters_output
    import capo_emr.types.list_instance_fleets_input
    import capo_emr.types.list_instance_fleets_output
    import capo_emr.types.list_instance_groups_input
    import capo_emr.types.list_instance_groups_output
    import capo_emr.types.list_instances_input
    import capo_emr.types.list_instances_output
    import capo_emr.types.list_notebook_executions_input
    import capo_emr.types.list_notebook_executions_output
    import capo_emr.types.list_release_labels_input
    import capo_emr.types.list_release_labels_output
    import capo_emr.types.list_security_configurations_input
    import capo_emr.types.list_security_configurations_output
    import capo_emr.types.list_sessions_input
    import capo_emr.types.list_sessions_output
    import capo_emr.types.list_steps_input
    import capo_emr.types.list_steps_output
    import capo_emr.types.list_studio_session_mappings_input
    import capo_emr.types.list_studio_session_mappings_output
    import capo_emr.types.list_studios_input
    import capo_emr.types.list_studios_output
    import capo_emr.types.list_supported_instance_types_input
    import capo_emr.types.list_supported_instance_types_output
    import capo_emr.types.long
    import capo_emr.types.managed_scaling_policy
    import capo_emr.types.marker
    import capo_emr.types.max_results_number
    import capo_emr.types.modify_cluster_input
    import capo_emr.types.modify_cluster_output
    import capo_emr.types.modify_instance_fleet_input
    import capo_emr.types.modify_instance_groups_input
    import capo_emr.types.monitoring_configuration
    import capo_emr.types.new_supported_products_list
    import capo_emr.types.notebook_execution_status
    import capo_emr.types.notebook_execution_summary
    import capo_emr.types.notebook_s3_location_from_input
    import capo_emr.types.on_cluster_app_ui_type
    import capo_emr.types.output_notebook_format
    import capo_emr.types.output_notebook_s3_location_from_input
    import capo_emr.types.persistent_app_ui_type
    import capo_emr.types.placement_group_config_list
    import capo_emr.types.profiler_type
    import capo_emr.types.put_auto_scaling_policy_input
    import capo_emr.types.put_auto_scaling_policy_output
    import capo_emr.types.put_auto_termination_policy_input
    import capo_emr.types.put_auto_termination_policy_output
    import capo_emr.types.put_block_public_access_configuration_input
    import capo_emr.types.put_block_public_access_configuration_output
    import capo_emr.types.put_managed_scaling_policy_input
    import capo_emr.types.put_managed_scaling_policy_output
    import capo_emr.types.release_label_filter
    import capo_emr.types.remove_auto_scaling_policy_input
    import capo_emr.types.remove_auto_scaling_policy_output
    import capo_emr.types.remove_auto_termination_policy_input
    import capo_emr.types.remove_auto_termination_policy_output
    import capo_emr.types.remove_managed_scaling_policy_input
    import capo_emr.types.remove_managed_scaling_policy_output
    import capo_emr.types.remove_tags_input
    import capo_emr.types.remove_tags_output
    import capo_emr.types.repo_upgrade_on_boot
    import capo_emr.types.resource_id
    import capo_emr.types.run_job_flow_input
    import capo_emr.types.run_job_flow_output
    import capo_emr.types.scale_down_behavior
    import capo_emr.types.security_configuration_summary
    import capo_emr.types.session
    import capo_emr.types.session_id
    import capo_emr.types.session_mapping_summary
    import capo_emr.types.session_monitoring_configuration
    import capo_emr.types.session_state_list
    import capo_emr.types.set_keep_job_flow_alive_when_no_steps_input
    import capo_emr.types.set_termination_protection_input
    import capo_emr.types.set_unhealthy_node_replacement_input
    import capo_emr.types.set_visible_to_all_users_input
    import capo_emr.types.start_notebook_execution_input
    import capo_emr.types.start_notebook_execution_output
    import capo_emr.types.start_session_input
    import capo_emr.types.start_session_output
    import capo_emr.types.step_cancellation_option
    import capo_emr.types.step_config_list
    import capo_emr.types.step_id
    import capo_emr.types.step_ids_list
    import capo_emr.types.step_state_list
    import capo_emr.types.step_summary
    import capo_emr.types.stop_notebook_execution_input
    import capo_emr.types.string
    import capo_emr.types.string_list
    import capo_emr.types.studio_summary
    import capo_emr.types.subnet_id_list
    import capo_emr.types.supported_products_list
    import capo_emr.types.tag_list
    import capo_emr.types.terminate_job_flows_input
    import capo_emr.types.terminate_session_input
    import capo_emr.types.terminate_session_output
    import capo_emr.types.update_studio_input
    import capo_emr.types.update_studio_session_mapping_input
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_list
    import capo_emr.types.xml_string_max_len256


class EMRClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class EMRClient:
    """A client for the ``EMR`` service.

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
        self._config = EMRClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[EMRClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EMRClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def add_instance_fleet(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        instance_fleet: Optional[
            "capo_emr.types.instance_fleet_config.InstanceFleetConfig"
        ] = None,
    ) -> "capo_emr.types.add_instance_fleet_output.AddInstanceFleetOutput":
        """<p>Adds an instance fleet to a running cluster.</p> <note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x.</p> </note>

        Args:
            cluster_id: <p>The unique identifier of the cluster.</p>
            instance_fleet: <p>Specifies the configuration of the instance fleet.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.add_instance_fleet_input.AddInstanceFleetInput]",
        ) -> OperationResponse[
            "capo_emr.types.add_instance_fleet_output.AddInstanceFleetOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.add_instance_fleet

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.add_instance_fleet.add_instance_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.add_instance_fleet_input.AddInstanceFleetInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if instance_fleet is not None:
            input_["instance_fleet"] = instance_fleet

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_instance_groups(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        instance_groups: Optional[
            "capo_emr.types.instance_group_config_list.InstanceGroupConfigList"
        ] = None,
        job_flow_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
    ) -> "capo_emr.types.add_instance_groups_output.AddInstanceGroupsOutput":
        """<p>Adds one or more instance groups to a running cluster.</p>

        Args:
            instance_groups: <p>Instance groups to add.</p>
            job_flow_id: <p>Job flow in which to add the instance groups.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.add_instance_groups_input.AddInstanceGroupsInput]",
        ) -> OperationResponse[
            "capo_emr.types.add_instance_groups_output.AddInstanceGroupsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.add_instance_groups

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.add_instance_groups.add_instance_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.add_instance_groups_input.AddInstanceGroupsInput = {}
        if instance_groups is not None:
            input_["instance_groups"] = instance_groups
        if job_flow_id is not None:
            input_["job_flow_id"] = job_flow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_job_flow_steps(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        job_flow_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        steps: Optional["capo_emr.types.step_config_list.StepConfigList"] = None,
        execution_role_arn: Optional["capo_emr.types.arn_type.ArnType"] = None,
    ) -> "capo_emr.types.add_job_flow_steps_output.AddJobFlowStepsOutput":
        """<p>AddJobFlowSteps adds new steps to a running cluster. A maximum of 256 steps are allowed in each job flow.</p> <p>If your cluster is long-running (such as a Hive data warehouse) or complex, you may require more than 256 steps to process your data. You can bypass the 256-step limitation in various ways, including using SSH to connect to the master node and submitting queries directly to the software running on the master node, such as Hive and Hadoop.</p> <p>A step specifies the location of a JAR file stored either on the master node of the cluster or in Amazon S3. Each step is performed by the main function of the main class of the JAR file. The main class can be specified either in the manifest of the JAR or by using the MainFunction parameter of the step.</p> <p>Amazon EMR executes each step in the order listed. For a step to be considered complete, the main function must exit with a zero exit code and all Hadoop jobs started while the step was running must have completed and run successfully.</p> <p>You can only add steps to a cluster that is in one of the following states: STARTING, BOOTSTRAPPING, RUNNING, or WAITING.</p> <note> <p>The string values passed into <code>HadoopJarStep</code> object cannot exceed a total of 10240 characters.</p> </note>

        Args:
            job_flow_id: <p>A string that uniquely identifies the job flow. This identifier is returned by <a>RunJobFlow</a> and can also be obtained from <a>ListClusters</a>. </p>
            steps: <p> A list of <a>StepConfig</a> to be executed by the job flow. </p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the runtime role for a step on the cluster. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: <code>arn:partition:service:region:account:resource</code>. </p> <p>For example, <code>arn:aws:IAM::1234567890:role/ReadOnly</code> is a correctly formatted runtime role ARN.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.add_job_flow_steps_input.AddJobFlowStepsInput]",
        ) -> OperationResponse[
            "capo_emr.types.add_job_flow_steps_output.AddJobFlowStepsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.add_job_flow_steps

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.add_job_flow_steps.add_job_flow_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.add_job_flow_steps_input.AddJobFlowStepsInput = {}
        if job_flow_id is not None:
            input_["job_flow_id"] = job_flow_id
        if steps is not None:
            input_["steps"] = steps
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_tags(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        resource_id: Optional["capo_emr.types.resource_id.ResourceId"] = None,
        tags: Optional["capo_emr.types.tag_list.TagList"] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
    ) -> "capo_emr.types.add_tags_output.AddTagsOutput":
        """<p>Adds tags to an Amazon EMR resource, such as a cluster or an Amazon EMR Studio. Tags make it easier to associate resources in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html">Tag Clusters</a>. </p>

        Args:
            resource_id: <p>The Amazon EMR resource identifier to which tags will be added. For example, a cluster identifier or an Amazon EMR Studio ID.</p>
            tags: <p>A list of tags to associate with a resource. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.</p>
            cluster_id: <p>The ID of the cluster that scopes the tag operation. Required when the resource being tagged is a session-scoped resource.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.add_tags_input.AddTagsInput]",
        ) -> OperationResponse["capo_emr.types.add_tags_output.AddTagsOutput"]:
            import capo_emr._operations.elastic_map_reduce.add_tags

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.add_tags.add_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.add_tags_input.AddTagsInput = {}
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if tags is not None:
            input_["tags"] = tags
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_steps(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        step_ids: Optional["capo_emr.types.step_ids_list.StepIdsList"] = None,
        step_cancellation_option: Optional[
            "capo_emr.types.step_cancellation_option.StepCancellationOption"
        ] = None,
    ) -> "capo_emr.types.cancel_steps_output.CancelStepsOutput":
        """<p>Cancels a pending step or steps in a running cluster. Available only in Amazon EMR versions 4.8.0 and later, excluding version 5.0.0. A maximum of 256 steps are allowed in each CancelSteps request. CancelSteps is idempotent but asynchronous; it does not guarantee that a step will be canceled, even if the request is successfully submitted. When you use Amazon EMR releases 5.28.0 and later, you can cancel steps that are in a <code>PENDING</code> or <code>RUNNING</code> state. In earlier versions of Amazon EMR, you can only cancel steps that are in a <code>PENDING</code> state. </p>

        Args:
            cluster_id: <p>The <code>ClusterID</code> for the specified steps that will be canceled. Use <a>RunJobFlow</a> and <a>ListClusters</a> to get ClusterIDs. </p>
            step_ids: <p>The list of <code>StepIDs</code> to cancel. Use <a>ListSteps</a> to get steps and their states for the specified cluster.</p>
            step_cancellation_option: <p>The option to choose to cancel <code>RUNNING</code> steps. By default, the value is <code>SEND_INTERRUPT</code>.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.cancel_steps_input.CancelStepsInput]",
        ) -> OperationResponse["capo_emr.types.cancel_steps_output.CancelStepsOutput"]:
            import capo_emr._operations.elastic_map_reduce.cancel_steps

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.cancel_steps.cancel_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.cancel_steps_input.CancelStepsInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if step_ids is not None:
            input_["step_ids"] = step_ids
        if step_cancellation_option is not None:
            input_["step_cancellation_option"] = step_cancellation_option

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_persistent_app_ui(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        target_resource_arn: Optional["capo_emr.types.arn_type.ArnType"] = None,
        emr_containers_config: Optional[
            "capo_emr.types.emr_containers_config.EMRContainersConfig"
        ] = None,
        tags: Optional["capo_emr.types.tag_list.TagList"] = None,
        x_referer: Optional["capo_emr.types.string.String"] = None,
        profiler_type: Optional["capo_emr.types.profiler_type.ProfilerType"] = None,
    ) -> "capo_emr.types.create_persistent_app_ui_output.CreatePersistentAppUIOutput":
        """<p>Creates a persistent application user interface.</p>

        Args:
            target_resource_arn: <p>The unique Amazon Resource Name (ARN) of the target resource.</p>
            emr_containers_config: <p>The EMR containers configuration.</p>
            tags: <p>Tags for the persistent application user interface.</p>
            x_referer: <p>The cross reference for the persistent application user interface.</p>
            profiler_type: <p>The profiler type for the persistent application user interface.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.create_persistent_app_ui_input.CreatePersistentAppUIInput]",
        ) -> OperationResponse[
            "capo_emr.types.create_persistent_app_ui_output.CreatePersistentAppUIOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.create_persistent_app_ui

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.create_persistent_app_ui.create_persistent_app_ui(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.create_persistent_app_ui_input.CreatePersistentAppUIInput = {}
        if target_resource_arn is not None:
            input_["target_resource_arn"] = target_resource_arn
        if emr_containers_config is not None:
            input_["emr_containers_config"] = emr_containers_config
        if tags is not None:
            input_["tags"] = tags
        if x_referer is not None:
            input_["x_referer"] = x_referer
        if profiler_type is not None:
            input_["profiler_type"] = profiler_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_security_configuration(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        name: Optional["capo_emr.types.xml_string.XmlString"] = None,
        security_configuration: Optional["capo_emr.types.string.String"] = None,
    ) -> "capo_emr.types.create_security_configuration_output.CreateSecurityConfigurationOutput":
        """<p>Creates a security configuration, which is stored in the service and can be specified when a cluster is created.</p>

        Args:
            name: <p>The name of the security configuration.</p>
            security_configuration: <p>The security configuration details in JSON format. For JSON parameters and examples, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-security-configurations.html">Use Security Configurations to Set Up Cluster Security</a> in the <i>Amazon EMR Management Guide</i>.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.create_security_configuration_input.CreateSecurityConfigurationInput]",
        ) -> OperationResponse[
            "capo_emr.types.create_security_configuration_output.CreateSecurityConfigurationOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.create_security_configuration

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.create_security_configuration.create_security_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.create_security_configuration_input.CreateSecurityConfigurationInput = {}
        if name is not None:
            input_["name"] = name
        if security_configuration is not None:
            input_["security_configuration"] = security_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_studio(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        description: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        auth_mode: Optional["capo_emr.types.auth_mode.AuthMode"] = None,
        vpc_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        subnet_ids: Optional["capo_emr.types.subnet_id_list.SubnetIdList"] = None,
        service_role: Optional["capo_emr.types.xml_string.XmlString"] = None,
        user_role: Optional["capo_emr.types.xml_string.XmlString"] = None,
        workspace_security_group_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        engine_security_group_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        default_s3_location: Optional["capo_emr.types.xml_string.XmlString"] = None,
        idp_auth_url: Optional["capo_emr.types.xml_string.XmlString"] = None,
        idp_relay_state_parameter_name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        tags: Optional["capo_emr.types.tag_list.TagList"] = None,
        trusted_identity_propagation_enabled: Optional[
            "capo_emr.types.boolean_object.BooleanObject"
        ] = None,
        idc_user_assignment: Optional[
            "capo_emr.types.idc_user_assignment.IdcUserAssignment"
        ] = None,
        idc_instance_arn: Optional["capo_emr.types.arn_type.ArnType"] = None,
        encryption_key_arn: Optional["capo_emr.types.xml_string.XmlString"] = None,
    ) -> "capo_emr.types.create_studio_output.CreateStudioOutput":
        """<p>Creates a new Amazon EMR Studio.</p>

        Args:
            name: <p>A descriptive name for the Amazon EMR Studio.</p>
            description: <p>A detailed description of the Amazon EMR Studio.</p>
            auth_mode: <p>Specifies whether the Studio authenticates users using IAM or IAM Identity Center.</p>
            vpc_id: <p>The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.</p>
            subnet_ids: <p>A list of subnet IDs to associate with the Amazon EMR Studio. A Studio can have a maximum of 5 subnets. The subnets must belong to the VPC specified by <code>VpcId</code>. Studio users can create a Workspace in any of the specified subnets.</p>
            service_role: <p>The IAM role that the Amazon EMR Studio assumes. The service role provides a way for Amazon EMR Studio to interoperate with other Amazon Web Services services.</p>
            user_role: <p>The IAM user role that users and groups assume when logged in to an Amazon EMR Studio. Only specify a <code>UserRole</code> when you use IAM Identity Center authentication. The permissions attached to the <code>UserRole</code> can be scoped down for each user or group using session policies.</p>
            workspace_security_group_id: <p>The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by <code>VpcId</code>.</p>
            engine_security_group_id: <p>The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by <code>VpcId</code>.</p>
            default_s3_location: <p>The Amazon S3 location to back up Amazon EMR Studio Workspaces and notebook files.</p>
            idp_auth_url: <p>The authentication endpoint of your identity provider (IdP). Specify this value when you use IAM authentication and want to let federated users log in to a Studio with the Studio URL and credentials from your IdP. Amazon EMR Studio redirects users to this endpoint to enter credentials.</p>
            idp_relay_state_parameter_name: <p>The name that your identity provider (IdP) uses for its <code>RelayState</code> parameter. For example, <code>RelayState</code> or <code>TargetSource</code>. Specify this value when you use IAM authentication and want to let federated users log in to a Studio using the Studio URL. The <code>RelayState</code> parameter differs by IdP.</p>
            tags: <p>A list of tags to associate with the Amazon EMR Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.</p>
            trusted_identity_propagation_enabled: <p> A Boolean indicating whether to enable Trusted identity propagation for the Studio. The default value is <code>false</code>. </p>
            idc_user_assignment: <p> Specifies whether IAM Identity Center user assignment is <code>REQUIRED</code> or <code>OPTIONAL</code>. If the value is set to <code>REQUIRED</code>, users must be explicitly assigned to the Studio application to access the Studio. </p>
            idc_instance_arn: <p> The ARN of the IAM Identity Center instance to create the Studio application. </p>
            encryption_key_arn: <p>The KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.create_studio_input.CreateStudioInput]",
        ) -> OperationResponse[
            "capo_emr.types.create_studio_output.CreateStudioOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.create_studio

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.create_studio.create_studio(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.create_studio_input.CreateStudioInput = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if auth_mode is not None:
            input_["auth_mode"] = auth_mode
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if service_role is not None:
            input_["service_role"] = service_role
        if user_role is not None:
            input_["user_role"] = user_role
        if workspace_security_group_id is not None:
            input_["workspace_security_group_id"] = workspace_security_group_id
        if engine_security_group_id is not None:
            input_["engine_security_group_id"] = engine_security_group_id
        if default_s3_location is not None:
            input_["default_s3_location"] = default_s3_location
        if idp_auth_url is not None:
            input_["idp_auth_url"] = idp_auth_url
        if idp_relay_state_parameter_name is not None:
            input_["idp_relay_state_parameter_name"] = idp_relay_state_parameter_name
        if tags is not None:
            input_["tags"] = tags
        if trusted_identity_propagation_enabled is not None:
            input_["trusted_identity_propagation_enabled"] = (
                trusted_identity_propagation_enabled
            )
        if idc_user_assignment is not None:
            input_["idc_user_assignment"] = idc_user_assignment
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_studio_session_mapping(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        studio_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_type: Optional["capo_emr.types.identity_type.IdentityType"] = None,
        session_policy_arn: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
    ) -> None:
        """<p>Maps a user or group to the Amazon EMR Studio specified by <code>StudioId</code>, and applies a session policy to refine Studio permissions for that user or group. Use <code>CreateStudioSessionMapping</code> to assign users to a Studio when you use IAM Identity Center authentication. For instructions on how to assign users to a Studio when you use IAM authentication, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-manage-users.html#emr-studio-assign-users-groups">Assign a user or group to your EMR Studio</a>.</p>

        Args:
            studio_id: <p>The ID of the Amazon EMR Studio to which the user or group will be mapped.</p>
            identity_id: <p>The globally unique identifier (GUID) of the user or group from the IAM Identity Center Identity Store. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserId">UserId</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-GroupId">GroupId</a> in the <i>IAM Identity Center Identity Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified, but not both.</p>
            identity_name: <p>The name of the user or group. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName">UserName</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName">DisplayName</a> in the <i>IAM Identity Center Identity Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified, but not both.</p>
            identity_type: <p>Specifies whether the identity to map to the Amazon EMR Studio is a user or a group.</p>
            session_policy_arn: <p>The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group. You should specify the ARN for the session policy that you want to apply, not the ARN of your user role. For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-user-role.html">Create an Amazon EMR Studio User Role with Session Policies</a>.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.create_studio_session_mapping_input.CreateStudioSessionMappingInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.create_studio_session_mapping

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.create_studio_session_mapping.create_studio_session_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.create_studio_session_mapping_input.CreateStudioSessionMappingInput = {}
        if studio_id is not None:
            input_["studio_id"] = studio_id
        if identity_id is not None:
            input_["identity_id"] = identity_id
        if identity_name is not None:
            input_["identity_name"] = identity_name
        if identity_type is not None:
            input_["identity_type"] = identity_type
        if session_policy_arn is not None:
            input_["session_policy_arn"] = session_policy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_security_configuration(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        name: Optional["capo_emr.types.xml_string.XmlString"] = None,
    ) -> "capo_emr.types.delete_security_configuration_output.DeleteSecurityConfigurationOutput":
        """<p>Deletes a security configuration.</p>

        Args:
            name: <p>The name of the security configuration.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.delete_security_configuration_input.DeleteSecurityConfigurationInput]",
        ) -> OperationResponse[
            "capo_emr.types.delete_security_configuration_output.DeleteSecurityConfigurationOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.delete_security_configuration

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.delete_security_configuration.delete_security_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.delete_security_configuration_input.DeleteSecurityConfigurationInput = {}
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_studio(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        studio_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
    ) -> None:
        """<p>Removes an Amazon EMR Studio from the Studio metadata store.</p>

        Args:
            studio_id: <p>The ID of the Amazon EMR Studio.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.delete_studio_input.DeleteStudioInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.delete_studio

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.delete_studio.delete_studio(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.delete_studio_input.DeleteStudioInput = {}
        if studio_id is not None:
            input_["studio_id"] = studio_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_studio_session_mapping(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        studio_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_type: Optional["capo_emr.types.identity_type.IdentityType"] = None,
    ) -> None:
        """<p>Removes a user or group from an Amazon EMR Studio.</p>

        Args:
            studio_id: <p>The ID of the Amazon EMR Studio.</p>
            identity_id: <p>The globally unique identifier (GUID) of the user or group to remove from the Amazon EMR Studio. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserId">UserId</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-GroupId">GroupId</a> in the <i>IAM Identity Center Identity Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified.</p>
            identity_name: <p>The name of the user name or group to remove from the Amazon EMR Studio. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName">UserName</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName">DisplayName</a> in the <i>IAM Identity Center Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified.</p>
            identity_type: <p>Specifies whether the identity to delete from the Amazon EMR Studio is a user or a group.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.delete_studio_session_mapping_input.DeleteStudioSessionMappingInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.delete_studio_session_mapping

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.delete_studio_session_mapping.delete_studio_session_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.delete_studio_session_mapping_input.DeleteStudioSessionMappingInput = {}
        if studio_id is not None:
            input_["studio_id"] = studio_id
        if identity_id is not None:
            input_["identity_id"] = identity_id
        if identity_name is not None:
            input_["identity_name"] = identity_name
        if identity_type is not None:
            input_["identity_type"] = identity_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cluster(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
    ) -> "capo_emr.types.describe_cluster_output.DescribeClusterOutput":
        """<p>Provides cluster-level details including status, hardware and software configuration, VPC settings, and so on.</p>

        Args:
            cluster_id: <p>The identifier of the cluster to describe.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.describe_cluster_input.DescribeClusterInput]",
        ) -> OperationResponse[
            "capo_emr.types.describe_cluster_output.DescribeClusterOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.describe_cluster

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.describe_cluster.describe_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.describe_cluster_input.DescribeClusterInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_job_flows(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        created_after: Optional["capo_emr.types.date.Date"] = None,
        created_before: Optional["capo_emr.types.date.Date"] = None,
        job_flow_ids: Optional["capo_emr.types.xml_string_list.XmlStringList"] = None,
        job_flow_states: Optional[
            "capo_emr.types.job_flow_execution_state_list.JobFlowExecutionStateList"
        ] = None,
    ) -> "capo_emr.types.describe_job_flows_output.DescribeJobFlowsOutput":
        """<p>This API is no longer supported and will eventually be removed. We recommend you use <a>ListClusters</a>, <a>DescribeCluster</a>, <a>ListSteps</a>, <a>ListInstanceGroups</a> and <a>ListBootstrapActions</a> instead.</p> <p>DescribeJobFlows returns a list of job flows that match all of the supplied parameters. The parameters can include a list of job flow IDs, job flow states, and restrictions on job flow creation date and time.</p> <p>Regardless of supplied parameters, only job flows created within the last two months are returned.</p> <p>If no parameters are supplied, then job flows matching either of the following criteria are returned:</p> <ul> <li> <p>Job flows created and completed in the last two weeks</p> </li> <li> <p> Job flows created within the last two months that are in one of the following states: <code>RUNNING</code>, <code>WAITING</code>, <code>SHUTTING_DOWN</code>, <code>STARTING</code> </p> </li> </ul> <p>Amazon EMR can return a maximum of 512 job flow descriptions.</p>

        Args:
            created_after: <p>Return only job flows created after this date and time.</p>
            created_before: <p>Return only job flows created before this date and time.</p>
            job_flow_ids: <p>Return only job flows whose job flow ID is contained in this list.</p>
            job_flow_states: <p>Return only job flows whose state is contained in this list.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.describe_job_flows_input.DescribeJobFlowsInput]",
        ) -> OperationResponse[
            "capo_emr.types.describe_job_flows_output.DescribeJobFlowsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.describe_job_flows

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.describe_job_flows.describe_job_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.describe_job_flows_input.DescribeJobFlowsInput = {}
        if created_after is not None:
            input_["created_after"] = created_after
        if created_before is not None:
            input_["created_before"] = created_before
        if job_flow_ids is not None:
            input_["job_flow_ids"] = job_flow_ids
        if job_flow_states is not None:
            input_["job_flow_states"] = job_flow_states

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_notebook_execution(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        notebook_execution_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
    ) -> "capo_emr.types.describe_notebook_execution_output.DescribeNotebookExecutionOutput":
        """<p>Provides details of a notebook execution.</p>

        Args:
            notebook_execution_id: <p>The unique identifier of the notebook execution.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.describe_notebook_execution_input.DescribeNotebookExecutionInput]",
        ) -> OperationResponse[
            "capo_emr.types.describe_notebook_execution_output.DescribeNotebookExecutionOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.describe_notebook_execution

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.describe_notebook_execution.describe_notebook_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.describe_notebook_execution_input.DescribeNotebookExecutionInput = {}
        if notebook_execution_id is not None:
            input_["notebook_execution_id"] = notebook_execution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_persistent_app_ui(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        persistent_app_ui_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
    ) -> (
        "capo_emr.types.describe_persistent_app_ui_output.DescribePersistentAppUIOutput"
    ):
        """<p>Describes a persistent application user interface.</p>

        Args:
            persistent_app_ui_id: <p>The identifier for the persistent application user interface.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.describe_persistent_app_ui_input.DescribePersistentAppUIInput]",
        ) -> OperationResponse[
            "capo_emr.types.describe_persistent_app_ui_output.DescribePersistentAppUIOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.describe_persistent_app_ui

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.describe_persistent_app_ui.describe_persistent_app_ui(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.describe_persistent_app_ui_input.DescribePersistentAppUIInput = {}
        if persistent_app_ui_id is not None:
            input_["persistent_app_ui_id"] = persistent_app_ui_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_release_label(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        release_label: Optional["capo_emr.types.string.String"] = None,
        next_token: Optional["capo_emr.types.string.String"] = None,
        max_results: Optional[
            "capo_emr.types.max_results_number.MaxResultsNumber"
        ] = None,
    ) -> "capo_emr.types.describe_release_label_output.DescribeReleaseLabelOutput":
        """<p>Provides Amazon EMR release label details, such as the releases available the Region where the API request is run, and the available applications for a specific Amazon EMR release label. Can also list Amazon EMR releases that support a specified version of Spark.</p>

        Args:
            release_label: <p>The target release label to be described.</p>
            next_token: <p>The pagination token. Reserved for future use. Currently set to null.</p>
            max_results: <p>Reserved for future use. Currently set to null.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.describe_release_label_input.DescribeReleaseLabelInput]",
        ) -> OperationResponse[
            "capo_emr.types.describe_release_label_output.DescribeReleaseLabelOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.describe_release_label

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.describe_release_label.describe_release_label(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.describe_release_label_input.DescribeReleaseLabelInput = {}
        if release_label is not None:
            input_["release_label"] = release_label
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_security_configuration(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        name: Optional["capo_emr.types.xml_string.XmlString"] = None,
    ) -> "capo_emr.types.describe_security_configuration_output.DescribeSecurityConfigurationOutput":
        """<p>Provides the details of a security configuration by returning the configuration JSON.</p>

        Args:
            name: <p>The name of the security configuration.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.describe_security_configuration_input.DescribeSecurityConfigurationInput]",
        ) -> OperationResponse[
            "capo_emr.types.describe_security_configuration_output.DescribeSecurityConfigurationOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.describe_security_configuration

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.describe_security_configuration.describe_security_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.describe_security_configuration_input.DescribeSecurityConfigurationInput = {}
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_step(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        step_id: Optional["capo_emr.types.step_id.StepId"] = None,
    ) -> "capo_emr.types.describe_step_output.DescribeStepOutput":
        """<p>Provides more detail about the cluster step.</p>

        Args:
            cluster_id: <p>The identifier of the cluster with steps to describe.</p>
            step_id: <p>The identifier of the step to describe.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.describe_step_input.DescribeStepInput]",
        ) -> OperationResponse[
            "capo_emr.types.describe_step_output.DescribeStepOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.describe_step

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.describe_step.describe_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.describe_step_input.DescribeStepInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if step_id is not None:
            input_["step_id"] = step_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_studio(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        studio_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
    ) -> "capo_emr.types.describe_studio_output.DescribeStudioOutput":
        """<p>Returns details for the specified Amazon EMR Studio including ID, Name, VPC, Studio access URL, and so on.</p>

        Args:
            studio_id: <p>The Amazon EMR Studio ID.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.describe_studio_input.DescribeStudioInput]",
        ) -> OperationResponse[
            "capo_emr.types.describe_studio_output.DescribeStudioOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.describe_studio

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.describe_studio.describe_studio(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.describe_studio_input.DescribeStudioInput = {}
        if studio_id is not None:
            input_["studio_id"] = studio_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_auto_termination_policy(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
    ) -> "capo_emr.types.get_auto_termination_policy_output.GetAutoTerminationPolicyOutput":
        """<p>Returns the auto-termination policy for an Amazon EMR cluster.</p>

        Args:
            cluster_id: <p>Specifies the ID of the Amazon EMR cluster for which the auto-termination policy will be fetched.</p>

        Raises:
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.get_auto_termination_policy_input.GetAutoTerminationPolicyInput]",
        ) -> OperationResponse[
            "capo_emr.types.get_auto_termination_policy_output.GetAutoTerminationPolicyOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.get_auto_termination_policy

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.get_auto_termination_policy.get_auto_termination_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.get_auto_termination_policy_input.GetAutoTerminationPolicyInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_block_public_access_configuration(
        self, *, config_overrides: Optional[EMRClientConfig] = None
    ) -> "capo_emr.types.get_block_public_access_configuration_output.GetBlockPublicAccessConfigurationOutput":
        """<p>Returns the Amazon EMR block public access configuration for your Amazon Web Services account in the current Region. For more information see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/configure-block-public-access.html">Configure Block Public Access for Amazon EMR</a> in the <i>Amazon EMR Management Guide</i>.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.get_block_public_access_configuration_input.GetBlockPublicAccessConfigurationInput]",
        ) -> OperationResponse[
            "capo_emr.types.get_block_public_access_configuration_output.GetBlockPublicAccessConfigurationOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.get_block_public_access_configuration

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.get_block_public_access_configuration.get_block_public_access_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.get_block_public_access_configuration_input.GetBlockPublicAccessConfigurationInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cluster_session_credentials(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        execution_role_arn: Optional["capo_emr.types.arn_type.ArnType"] = None,
    ) -> "capo_emr.types.get_cluster_session_credentials_output.GetClusterSessionCredentialsOutput":
        """<p>Provides temporary, HTTP basic credentials that are associated with a given runtime IAM role and used by a cluster with fine-grained access control activated. You can use these credentials to connect to cluster endpoints that support username and password authentication.</p>

        Args:
            cluster_id: <p>The unique identifier of the cluster.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the runtime role for interactive workload submission on the cluster. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: <code>arn:partition:service:region:account:resource</code>.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.get_cluster_session_credentials_input.GetClusterSessionCredentialsInput]",
        ) -> OperationResponse[
            "capo_emr.types.get_cluster_session_credentials_output.GetClusterSessionCredentialsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.get_cluster_session_credentials

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.get_cluster_session_credentials.get_cluster_session_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.get_cluster_session_credentials_input.GetClusterSessionCredentialsInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_managed_scaling_policy(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
    ) -> (
        "capo_emr.types.get_managed_scaling_policy_output.GetManagedScalingPolicyOutput"
    ):
        """<p>Fetches the attached managed scaling policy for an Amazon EMR cluster. </p>

        Args:
            cluster_id: <p>Specifies the ID of the cluster for which the managed scaling policy will be fetched. </p>

        Raises:
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.get_managed_scaling_policy_input.GetManagedScalingPolicyInput]",
        ) -> OperationResponse[
            "capo_emr.types.get_managed_scaling_policy_output.GetManagedScalingPolicyOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.get_managed_scaling_policy

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.get_managed_scaling_policy.get_managed_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.get_managed_scaling_policy_input.GetManagedScalingPolicyInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_on_cluster_app_ui_presigned_url(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        on_cluster_app_ui_type: Optional[
            "capo_emr.types.on_cluster_app_ui_type.OnClusterAppUIType"
        ] = None,
        application_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        dry_run: Optional["capo_emr.types.boolean_object.BooleanObject"] = None,
        execution_role_arn: Optional["capo_emr.types.arn_type.ArnType"] = None,
    ) -> "capo_emr.types.get_on_cluster_app_ui_presigned_url_output.GetOnClusterAppUIPresignedURLOutput":
        """<p>The presigned URL properties for the cluster's application user interface.</p>

        Args:
            cluster_id: <p>The cluster ID associated with the cluster's application user interface presigned URL.</p>
            on_cluster_app_ui_type: <p>The application UI type associated with the cluster's application user interface presigned URL.</p>
            application_id: <p>The application ID associated with the cluster's application user interface presigned URL.</p>
            dry_run: <p>Determines if the user interface presigned URL is for a dry run.</p>
            execution_role_arn: <p>The execution role ARN associated with the cluster's application user interface presigned URL.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.get_on_cluster_app_ui_presigned_url_input.GetOnClusterAppUIPresignedURLInput]",
        ) -> OperationResponse[
            "capo_emr.types.get_on_cluster_app_ui_presigned_url_output.GetOnClusterAppUIPresignedURLOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.get_on_cluster_app_ui_presigned_url

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.get_on_cluster_app_ui_presigned_url.get_on_cluster_app_ui_presigned_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.get_on_cluster_app_ui_presigned_url_input.GetOnClusterAppUIPresignedURLInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if on_cluster_app_ui_type is not None:
            input_["on_cluster_app_ui_type"] = on_cluster_app_ui_type
        if application_id is not None:
            input_["application_id"] = application_id
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_persistent_app_ui_presigned_url(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        persistent_app_ui_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        persistent_app_ui_type: Optional[
            "capo_emr.types.persistent_app_ui_type.PersistentAppUIType"
        ] = None,
        application_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        auth_proxy_call: Optional["capo_emr.types.boolean_object.BooleanObject"] = None,
        execution_role_arn: Optional["capo_emr.types.arn_type.ArnType"] = None,
    ) -> "capo_emr.types.get_persistent_app_ui_presigned_url_output.GetPersistentAppUIPresignedURLOutput":
        """<p>The presigned URL properties for the cluster's application user interface.</p>

        Args:
            persistent_app_ui_id: <p>The persistent application user interface ID associated with the presigned URL.</p>
            persistent_app_ui_type: <p>The persistent application user interface type associated with the presigned URL.</p>
            application_id: <p>The application ID associated with the presigned URL.</p>
            auth_proxy_call: <p>A boolean that represents if the caller is an authentication proxy call.</p>
            execution_role_arn: <p>The execution role ARN associated with the presigned URL.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.get_persistent_app_ui_presigned_url_input.GetPersistentAppUIPresignedURLInput]",
        ) -> OperationResponse[
            "capo_emr.types.get_persistent_app_ui_presigned_url_output.GetPersistentAppUIPresignedURLOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.get_persistent_app_ui_presigned_url

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.get_persistent_app_ui_presigned_url.get_persistent_app_ui_presigned_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.get_persistent_app_ui_presigned_url_input.GetPersistentAppUIPresignedURLInput = {}
        if persistent_app_ui_id is not None:
            input_["persistent_app_ui_id"] = persistent_app_ui_id
        if persistent_app_ui_type is not None:
            input_["persistent_app_ui_type"] = persistent_app_ui_type
        if application_id is not None:
            input_["application_id"] = application_id
        if auth_proxy_call is not None:
            input_["auth_proxy_call"] = auth_proxy_call
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_session(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        session_id: Optional["capo_emr.types.session_id.SessionId"] = None,
    ) -> "capo_emr.types.get_session_output.GetSessionOutput":
        """<p>Returns detailed information about a session.</p>

        Args:
            cluster_id: <p>The ID of the cluster that the session belongs to.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.get_session_input.GetSessionInput]",
        ) -> OperationResponse["capo_emr.types.get_session_output.GetSessionOutput"]:
            import capo_emr._operations.elastic_map_reduce.get_session

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.get_session.get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.get_session_input.GetSessionInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_session_endpoint(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        session_id: Optional["capo_emr.types.session_id.SessionId"] = None,
    ) -> "capo_emr.types.get_session_endpoint_output.GetSessionEndpointOutput":
        """<p>Returns the Spark Connect endpoint URL and a time-limited authentication token for the specified session. Use the endpoint and token to connect a PySpark client to the session. Call this operation again when the token expires to obtain a new one.</p>

        Args:
            cluster_id: <p>The ID of the cluster that the session belongs to.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.get_session_endpoint_input.GetSessionEndpointInput]",
        ) -> OperationResponse[
            "capo_emr.types.get_session_endpoint_output.GetSessionEndpointOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.get_session_endpoint

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.get_session_endpoint.get_session_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.get_session_endpoint_input.GetSessionEndpointInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_studio_session_mapping(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        studio_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_type: Optional["capo_emr.types.identity_type.IdentityType"] = None,
    ) -> (
        "capo_emr.types.get_studio_session_mapping_output.GetStudioSessionMappingOutput"
    ):
        """<p>Fetches mapping details for the specified Amazon EMR Studio and identity (user or group).</p>

        Args:
            studio_id: <p>The ID of the Amazon EMR Studio.</p>
            identity_id: <p>The globally unique identifier (GUID) of the user or group. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserId">UserId</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-GroupId">GroupId</a> in the <i>IAM Identity Center Identity Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified.</p>
            identity_name: <p>The name of the user or group to fetch. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName">UserName</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName">DisplayName</a> in the <i>IAM Identity Center Identity Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified.</p>
            identity_type: <p>Specifies whether the identity to fetch is a user or a group.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.get_studio_session_mapping_input.GetStudioSessionMappingInput]",
        ) -> OperationResponse[
            "capo_emr.types.get_studio_session_mapping_output.GetStudioSessionMappingOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.get_studio_session_mapping

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.get_studio_session_mapping.get_studio_session_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.get_studio_session_mapping_input.GetStudioSessionMappingInput = {}
        if studio_id is not None:
            input_["studio_id"] = studio_id
        if identity_id is not None:
            input_["identity_id"] = identity_id
        if identity_name is not None:
            input_["identity_name"] = identity_name
        if identity_type is not None:
            input_["identity_type"] = identity_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_bootstrap_actions(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "capo_emr.types.list_bootstrap_actions_output.ListBootstrapActionsOutput":
        """<p>Provides information about the bootstrap actions associated with a cluster.</p>

        Args:
            cluster_id: <p>The cluster identifier for the bootstrap actions to list.</p>
            marker: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_bootstrap_actions_input.ListBootstrapActionsInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_bootstrap_actions_output.ListBootstrapActionsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_bootstrap_actions

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_bootstrap_actions.list_bootstrap_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_bootstrap_actions_input.ListBootstrapActionsInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_bootstrap_actions(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "Iterator[capo_emr.types.command.Command]":
        _token = marker
        while True:
            _response = self.list_bootstrap_actions(
                config_overrides=config_overrides,
                cluster_id=cluster_id,
                marker=_token,
            )
            _page = _resolve_path(_response, ("bootstrap_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_clusters(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        created_after: Optional["capo_emr.types.date.Date"] = None,
        created_before: Optional["capo_emr.types.date.Date"] = None,
        cluster_states: Optional[
            "capo_emr.types.cluster_state_list.ClusterStateList"
        ] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "capo_emr.types.list_clusters_output.ListClustersOutput":
        """<p>Provides the status of all clusters visible to this Amazon Web Services account. Allows you to filter the list of clusters based on certain criteria; for example, filtering by cluster creation date and time or by status. This call returns a maximum of 50 clusters in unsorted order per call, but returns a marker to track the paging of the cluster list across multiple ListClusters calls.</p>

        Args:
            created_after: <p>The creation date and time beginning value filter for listing clusters.</p>
            created_before: <p>The creation date and time end value filter for listing clusters.</p>
            cluster_states: <p>The cluster state filters to apply when listing clusters. Clusters that change state while this action runs may be not be returned as expected in the list of clusters.</p>
            marker: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_clusters_input.ListClustersInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_clusters_output.ListClustersOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_clusters

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_clusters_input.ListClustersInput = {}
        if created_after is not None:
            input_["created_after"] = created_after
        if created_before is not None:
            input_["created_before"] = created_before
        if cluster_states is not None:
            input_["cluster_states"] = cluster_states
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        created_after: Optional["capo_emr.types.date.Date"] = None,
        created_before: Optional["capo_emr.types.date.Date"] = None,
        cluster_states: Optional[
            "capo_emr.types.cluster_state_list.ClusterStateList"
        ] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "Iterator[capo_emr.types.cluster_summary.ClusterSummary]":
        _token = marker
        while True:
            _response = self.list_clusters(
                config_overrides=config_overrides,
                created_after=created_after,
                created_before=created_before,
                cluster_states=cluster_states,
                marker=_token,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_instance_fleets(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "capo_emr.types.list_instance_fleets_output.ListInstanceFleetsOutput":
        """<p>Lists all available details about the instance fleets in a cluster.</p> <note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.</p> </note>

        Args:
            cluster_id: <p>The unique identifier of the cluster.</p>
            marker: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_instance_fleets_input.ListInstanceFleetsInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_instance_fleets_output.ListInstanceFleetsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_instance_fleets

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_instance_fleets.list_instance_fleets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_instance_fleets_input.ListInstanceFleetsInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_instance_fleets(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "Iterator[capo_emr.types.instance_fleet.InstanceFleet]":
        _token = marker
        while True:
            _response = self.list_instance_fleets(
                config_overrides=config_overrides,
                cluster_id=cluster_id,
                marker=_token,
            )
            _page = _resolve_path(_response, ("instance_fleets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_instance_groups(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "capo_emr.types.list_instance_groups_output.ListInstanceGroupsOutput":
        """<p>Provides all available details about the instance groups in a cluster.</p>

        Args:
            cluster_id: <p>The identifier of the cluster for which to list the instance groups.</p>
            marker: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_instance_groups_input.ListInstanceGroupsInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_instance_groups_output.ListInstanceGroupsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_instance_groups

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_instance_groups.list_instance_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_instance_groups_input.ListInstanceGroupsInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_instance_groups(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "Iterator[capo_emr.types.instance_group.InstanceGroup]":
        _token = marker
        while True:
            _response = self.list_instance_groups(
                config_overrides=config_overrides,
                cluster_id=cluster_id,
                marker=_token,
            )
            _page = _resolve_path(_response, ("instance_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_instances(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        instance_group_id: Optional[
            "capo_emr.types.instance_group_id.InstanceGroupId"
        ] = None,
        instance_group_types: Optional[
            "capo_emr.types.instance_group_type_list.InstanceGroupTypeList"
        ] = None,
        instance_fleet_id: Optional[
            "capo_emr.types.instance_fleet_id.InstanceFleetId"
        ] = None,
        instance_fleet_type: Optional[
            "capo_emr.types.instance_fleet_type.InstanceFleetType"
        ] = None,
        instance_states: Optional[
            "capo_emr.types.instance_state_list.InstanceStateList"
        ] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "capo_emr.types.list_instances_output.ListInstancesOutput":
        """<p>Provides information for all active Amazon EC2 instances and Amazon EC2 instances terminated in the last 30 days, up to a maximum of 2,000. Amazon EC2 instances in any of the following states are considered active: AWAITING_FULFILLMENT, PROVISIONING, BOOTSTRAPPING, RUNNING.</p>

        Args:
            cluster_id: <p>The identifier of the cluster for which to list the instances.</p>
            instance_group_id: <p>The identifier of the instance group for which to list the instances.</p>
            instance_group_types: <p>The type of instance group for which to list the instances.</p>
            instance_fleet_id: <p>The unique identifier of the instance fleet.</p>
            instance_fleet_type: <p>The node type of the instance fleet. For example MASTER, CORE, or TASK.</p>
            instance_states: <p>A list of instance states that will filter the instances returned with this request.</p>
            marker: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_instances_input.ListInstancesInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_instances_output.ListInstancesOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_instances

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_instances.list_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_instances_input.ListInstancesInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if instance_group_id is not None:
            input_["instance_group_id"] = instance_group_id
        if instance_group_types is not None:
            input_["instance_group_types"] = instance_group_types
        if instance_fleet_id is not None:
            input_["instance_fleet_id"] = instance_fleet_id
        if instance_fleet_type is not None:
            input_["instance_fleet_type"] = instance_fleet_type
        if instance_states is not None:
            input_["instance_states"] = instance_states
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_instances(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        instance_group_id: Optional[
            "capo_emr.types.instance_group_id.InstanceGroupId"
        ] = None,
        instance_group_types: Optional[
            "capo_emr.types.instance_group_type_list.InstanceGroupTypeList"
        ] = None,
        instance_fleet_id: Optional[
            "capo_emr.types.instance_fleet_id.InstanceFleetId"
        ] = None,
        instance_fleet_type: Optional[
            "capo_emr.types.instance_fleet_type.InstanceFleetType"
        ] = None,
        instance_states: Optional[
            "capo_emr.types.instance_state_list.InstanceStateList"
        ] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "Iterator[capo_emr.types.instance.Instance]":
        _token = marker
        while True:
            _response = self.list_instances(
                config_overrides=config_overrides,
                cluster_id=cluster_id,
                instance_group_id=instance_group_id,
                instance_group_types=instance_group_types,
                instance_fleet_id=instance_fleet_id,
                instance_fleet_type=instance_fleet_type,
                instance_states=instance_states,
                marker=_token,
            )
            _page = _resolve_path(_response, ("instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_notebook_executions(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        editor_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        status: Optional[
            "capo_emr.types.notebook_execution_status.NotebookExecutionStatus"
        ] = None,
        from_: Optional["capo_emr.types.date.Date"] = None,
        to: Optional["capo_emr.types.date.Date"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
        execution_engine_id: Optional["capo_emr.types.xml_string.XmlString"] = None,
    ) -> "capo_emr.types.list_notebook_executions_output.ListNotebookExecutionsOutput":
        """<p>Provides summaries of all notebook executions. You can filter the list based on multiple criteria such as status, time range, and editor id. Returns a maximum of 50 notebook executions and a marker to track the paging of a longer notebook execution list across multiple <code>ListNotebookExecutions</code> calls.</p>

        Args:
            editor_id: <p>The unique ID of the editor associated with the notebook execution.</p>
            status: <p>The status filter for listing notebook executions.</p> <ul> <li> <p> <code>START_PENDING</code> indicates that the cluster has received the execution request but execution has not begun.</p> </li> <li> <p> <code>STARTING</code> indicates that the execution is starting on the cluster.</p> </li> <li> <p> <code>RUNNING</code> indicates that the execution is being processed by the cluster.</p> </li> <li> <p> <code>FINISHING</code> indicates that execution processing is in the final stages.</p> </li> <li> <p> <code>FINISHED</code> indicates that the execution has completed without error.</p> </li> <li> <p> <code>FAILING</code> indicates that the execution is failing and will not finish successfully.</p> </li> <li> <p> <code>FAILED</code> indicates that the execution failed.</p> </li> <li> <p> <code>STOP_PENDING</code> indicates that the cluster has received a <code>StopNotebookExecution</code> request and the stop is pending.</p> </li> <li> <p> <code>STOPPING</code> indicates that the cluster is in the process of stopping the execution as a result of a <code>StopNotebookExecution</code> request.</p> </li> <li> <p> <code>STOPPED</code> indicates that the execution stopped because of a <code>StopNotebookExecution</code> request.</p> </li> </ul>
            from_: <p>The beginning of time range filter for listing notebook executions. The default is the timestamp of 30 days ago.</p>
            to: <p>The end of time range filter for listing notebook executions. The default is the current timestamp.</p>
            marker: <p>The pagination token, returned by a previous <code>ListNotebookExecutions</code> call, that indicates the start of the list for this <code>ListNotebookExecutions</code> call.</p>
            execution_engine_id: <p>The unique ID of the execution engine.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_notebook_executions_input.ListNotebookExecutionsInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_notebook_executions_output.ListNotebookExecutionsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_notebook_executions

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_notebook_executions.list_notebook_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_notebook_executions_input.ListNotebookExecutionsInput = {}
        if editor_id is not None:
            input_["editor_id"] = editor_id
        if status is not None:
            input_["status"] = status
        if from_ is not None:
            input_["from"] = from_
        if to is not None:
            input_["to"] = to
        if marker is not None:
            input_["marker"] = marker
        if execution_engine_id is not None:
            input_["execution_engine_id"] = execution_engine_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_notebook_executions(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        editor_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        status: Optional[
            "capo_emr.types.notebook_execution_status.NotebookExecutionStatus"
        ] = None,
        from_: Optional["capo_emr.types.date.Date"] = None,
        to: Optional["capo_emr.types.date.Date"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
        execution_engine_id: Optional["capo_emr.types.xml_string.XmlString"] = None,
    ) -> "Iterator[capo_emr.types.notebook_execution_summary.NotebookExecutionSummary]":
        _token = marker
        while True:
            _response = self.list_notebook_executions(
                config_overrides=config_overrides,
                editor_id=editor_id,
                status=status,
                from_=from_,
                to=to,
                marker=_token,
                execution_engine_id=execution_engine_id,
            )
            _page = _resolve_path(_response, ("notebook_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_release_labels(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        filters: Optional[
            "capo_emr.types.release_label_filter.ReleaseLabelFilter"
        ] = None,
        next_token: Optional["capo_emr.types.string.String"] = None,
        max_results: Optional[
            "capo_emr.types.max_results_number.MaxResultsNumber"
        ] = None,
    ) -> "capo_emr.types.list_release_labels_output.ListReleaseLabelsOutput":
        """<p>Retrieves release labels of Amazon EMR services in the Region where the API is called.</p>

        Args:
            filters: <p>Filters the results of the request. <code>Prefix</code> specifies the prefix of release labels to return. <code>Application</code> specifies the application (with/without version) of release labels to return.</p>
            next_token: <p>Specifies the next page of results. If <code>NextToken</code> is not specified, which is usually the case for the first request of ListReleaseLabels, the first page of results are determined by other filtering parameters or by the latest version. The <code>ListReleaseLabels</code> request fails if the identity (Amazon Web Services account ID) and all filtering parameters are different from the original request, or if the <code>NextToken</code> is expired or tampered with.</p>
            max_results: <p>Defines the maximum number of release labels to return in a single response. The default is <code>100</code>.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_release_labels_input.ListReleaseLabelsInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_release_labels_output.ListReleaseLabelsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_release_labels

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_release_labels.list_release_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_release_labels_input.ListReleaseLabelsInput = {}
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_release_labels(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        filters: Optional[
            "capo_emr.types.release_label_filter.ReleaseLabelFilter"
        ] = None,
        next_token: Optional["capo_emr.types.string.String"] = None,
        max_results: Optional[
            "capo_emr.types.max_results_number.MaxResultsNumber"
        ] = None,
    ) -> "Iterator[capo_emr.types.list_release_labels_output.ListReleaseLabelsOutput]":
        _token = next_token
        while True:
            _response = self.list_release_labels(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_security_configurations(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "capo_emr.types.list_security_configurations_output.ListSecurityConfigurationsOutput":
        """<p>Lists all the security configurations visible to this account, providing their creation dates and times, and their names. This call returns a maximum of 50 clusters per call, but returns a marker to track the paging of the cluster list across multiple ListSecurityConfigurations calls.</p>

        Args:
            marker: <p>The pagination token that indicates the set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_security_configurations_input.ListSecurityConfigurationsInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_security_configurations_output.ListSecurityConfigurationsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_security_configurations

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_security_configurations.list_security_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_security_configurations_input.ListSecurityConfigurationsInput = {}
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_security_configurations(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "Iterator[capo_emr.types.security_configuration_summary.SecurityConfigurationSummary]":
        _token = marker
        while True:
            _response = self.list_security_configurations(
                config_overrides=config_overrides,
                marker=_token,
            )
            _page = _resolve_path(_response, ("security_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_sessions(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        session_states: Optional[
            "capo_emr.types.session_state_list.SessionStateList"
        ] = None,
        next_token: Optional["capo_emr.types.string.String"] = None,
        max_results: Optional[
            "capo_emr.types.max_results_number.MaxResultsNumber"
        ] = None,
    ) -> "capo_emr.types.list_sessions_output.ListSessionsOutput":
        """<p>Lists the sessions on a cluster. You can filter the results by session state. Newer sessions are returned first.</p>

        Args:
            cluster_id: <p>The ID of the cluster to list sessions for.</p>
            session_states: <p>An optional filter that limits the results to sessions in the specified states.</p>
            next_token: <p>The pagination token returned by a previous <code>ListSessions</code> call. Use it to retrieve the next page of results.</p>
            max_results: <p>The maximum number of sessions to return in each page of results.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_sessions_input.ListSessionsInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_sessions_output.ListSessionsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_sessions

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_sessions_input.ListSessionsInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if session_states is not None:
            input_["session_states"] = session_states
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_sessions(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        session_states: Optional[
            "capo_emr.types.session_state_list.SessionStateList"
        ] = None,
        next_token: Optional["capo_emr.types.string.String"] = None,
        max_results: Optional[
            "capo_emr.types.max_results_number.MaxResultsNumber"
        ] = None,
    ) -> "Iterator[capo_emr.types.session.Session]":
        _token = next_token
        while True:
            _response = self.list_sessions(
                config_overrides=config_overrides,
                cluster_id=cluster_id,
                session_states=session_states,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_steps(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        step_states: Optional["capo_emr.types.step_state_list.StepStateList"] = None,
        step_ids: Optional["capo_emr.types.xml_string_list.XmlStringList"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "capo_emr.types.list_steps_output.ListStepsOutput":
        """<p>Provides a list of steps for the cluster in reverse order unless you specify <code>stepIds</code> with the request or filter by <code>StepStates</code>. You can specify a maximum of 10 <code>stepIDs</code>. The CLI automatically paginates results to return a list greater than 50 steps. To return more than 50 steps using the CLI, specify a <code>Marker</code>, which is a pagination token that indicates the next set of steps to retrieve.</p>

        Args:
            cluster_id: <p>The identifier of the cluster for which to list the steps.</p>
            step_states: <p>The filter to limit the step list based on certain states.</p>
            step_ids: <p>The filter to limit the step list based on the identifier of the steps. You can specify a maximum of ten Step IDs. The character constraint applies to the overall length of the array.</p>
            marker: <p>The maximum number of steps that a single <code>ListSteps</code> action returns is 50. To return a longer list of steps, use multiple <code>ListSteps</code> actions along with the <code>Marker</code> parameter, which is a pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_steps_input.ListStepsInput]",
        ) -> OperationResponse["capo_emr.types.list_steps_output.ListStepsOutput"]:
            import capo_emr._operations.elastic_map_reduce.list_steps

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_steps.list_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_steps_input.ListStepsInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if step_states is not None:
            input_["step_states"] = step_states
        if step_ids is not None:
            input_["step_ids"] = step_ids
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_steps(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        step_states: Optional["capo_emr.types.step_state_list.StepStateList"] = None,
        step_ids: Optional["capo_emr.types.xml_string_list.XmlStringList"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "Iterator[capo_emr.types.step_summary.StepSummary]":
        _token = marker
        while True:
            _response = self.list_steps(
                config_overrides=config_overrides,
                cluster_id=cluster_id,
                step_states=step_states,
                step_ids=step_ids,
                marker=_token,
            )
            _page = _resolve_path(_response, ("steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_studios(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "capo_emr.types.list_studios_output.ListStudiosOutput":
        """<p>Returns a list of all Amazon EMR Studios associated with the Amazon Web Services account. The list includes details such as ID, Studio Access URL, and creation time for each Studio.</p>

        Args:
            marker: <p>The pagination token that indicates the set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_studios_input.ListStudiosInput]",
        ) -> OperationResponse["capo_emr.types.list_studios_output.ListStudiosOutput"]:
            import capo_emr._operations.elastic_map_reduce.list_studios

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_studios.list_studios(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_studios_input.ListStudiosInput = {}
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_studios(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "Iterator[capo_emr.types.studio_summary.StudioSummary]":
        _token = marker
        while True:
            _response = self.list_studios(
                config_overrides=config_overrides,
                marker=_token,
            )
            _page = _resolve_path(_response, ("studios",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_studio_session_mappings(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        studio_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_type: Optional["capo_emr.types.identity_type.IdentityType"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "capo_emr.types.list_studio_session_mappings_output.ListStudioSessionMappingsOutput":
        """<p>Returns a list of all user or group session mappings for the Amazon EMR Studio specified by <code>StudioId</code>.</p>

        Args:
            studio_id: <p>The ID of the Amazon EMR Studio.</p>
            identity_type: <p>Specifies whether to return session mappings for users or groups. If not specified, the results include session mapping details for both users and groups.</p>
            marker: <p>The pagination token that indicates the set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_studio_session_mappings_input.ListStudioSessionMappingsInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_studio_session_mappings_output.ListStudioSessionMappingsOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_studio_session_mappings

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_studio_session_mappings.list_studio_session_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_studio_session_mappings_input.ListStudioSessionMappingsInput = {}
        if studio_id is not None:
            input_["studio_id"] = studio_id
        if identity_type is not None:
            input_["identity_type"] = identity_type
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_studio_session_mappings(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        studio_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_type: Optional["capo_emr.types.identity_type.IdentityType"] = None,
        marker: Optional["capo_emr.types.marker.Marker"] = None,
    ) -> "Iterator[capo_emr.types.session_mapping_summary.SessionMappingSummary]":
        _token = marker
        while True:
            _response = self.list_studio_session_mappings(
                config_overrides=config_overrides,
                studio_id=studio_id,
                identity_type=identity_type,
                marker=_token,
            )
            _page = _resolve_path(_response, ("session_mappings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def list_supported_instance_types(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        release_label: Optional["capo_emr.types.string.String"] = None,
        marker: Optional["capo_emr.types.string.String"] = None,
    ) -> "capo_emr.types.list_supported_instance_types_output.ListSupportedInstanceTypesOutput":
        """<p>A list of the instance types that Amazon EMR supports. You can filter the list by Amazon Web Services Region and Amazon EMR release. </p>

        Args:
            release_label: <p>The Amazon EMR release label determines the <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-app-versions-6.x.html">versions of open-source application packages</a> that Amazon EMR has installed on the cluster. Release labels are in the format <code>emr-x.x.x</code>, where x.x.x is an Amazon EMR release number such as <code>emr-6.10.0</code>. For more information about Amazon EMR releases and their included application versions and features, see the <i> <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html">Amazon EMR Release Guide</a> </i>.</p>
            marker: <p>The pagination token that marks the next set of results to retrieve.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.list_supported_instance_types_input.ListSupportedInstanceTypesInput]",
        ) -> OperationResponse[
            "capo_emr.types.list_supported_instance_types_output.ListSupportedInstanceTypesOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.list_supported_instance_types

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.list_supported_instance_types.list_supported_instance_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.list_supported_instance_types_input.ListSupportedInstanceTypesInput = {}
        if release_label is not None:
            input_["release_label"] = release_label
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_supported_instance_types(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        release_label: Optional["capo_emr.types.string.String"] = None,
        marker: Optional["capo_emr.types.string.String"] = None,
    ) -> "Iterator[capo_emr.types.list_supported_instance_types_output.ListSupportedInstanceTypesOutput]":
        _token = marker
        while True:
            _response = self.list_supported_instance_types(
                config_overrides=config_overrides,
                release_label=release_label,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def modify_cluster(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.string.String"] = None,
        step_concurrency_level: Optional["capo_emr.types.integer.Integer"] = None,
        extended_support: Optional[
            "capo_emr.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "capo_emr.types.modify_cluster_output.ModifyClusterOutput":
        """<p>Modifies the number of steps that can be executed concurrently for the cluster specified using ClusterID.</p>

        Args:
            cluster_id: <p>The unique identifier of the cluster.</p>
            step_concurrency_level: <p>The number of steps that can be executed concurrently. You can specify a minimum of 1 step and a maximum of 256 steps. We recommend that you do not change this parameter while steps are running or the <code>ActionOnFailure</code> setting may not behave as expected. For more information see <a>Step$ActionOnFailure</a>.</p>
            extended_support: <p>Reserved.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.modify_cluster_input.ModifyClusterInput]",
        ) -> OperationResponse[
            "capo_emr.types.modify_cluster_output.ModifyClusterOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.modify_cluster

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.modify_cluster.modify_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.modify_cluster_input.ModifyClusterInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if step_concurrency_level is not None:
            input_["step_concurrency_level"] = step_concurrency_level
        if extended_support is not None:
            input_["extended_support"] = extended_support

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_instance_fleet(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        instance_fleet: Optional[
            "capo_emr.types.instance_fleet_modify_config.InstanceFleetModifyConfig"
        ] = None,
    ) -> None:
        """<p>Modifies the target On-Demand and target Spot capacities for the instance fleet with the specified InstanceFleetID within the cluster specified using ClusterID. The call either succeeds or fails atomically.</p> <note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.</p> </note>

        Args:
            cluster_id: <p>The unique identifier of the cluster.</p>
            instance_fleet: <p>The configuration parameters of the instance fleet.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.modify_instance_fleet_input.ModifyInstanceFleetInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.modify_instance_fleet

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.modify_instance_fleet.modify_instance_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.modify_instance_fleet_input.ModifyInstanceFleetInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if instance_fleet is not None:
            input_["instance_fleet"] = instance_fleet

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_instance_groups(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        instance_groups: Optional[
            "capo_emr.types.instance_group_modify_config_list.InstanceGroupModifyConfigList"
        ] = None,
    ) -> None:
        """<p>ModifyInstanceGroups modifies the number of nodes and configuration settings of an instance group. The input parameters include the new target instance count for the group and the instance group ID. The call will either succeed or fail atomically.</p>

        Args:
            cluster_id: <p>The ID of the cluster to which the instance group belongs.</p>
            instance_groups: <p>Instance groups to change.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.modify_instance_groups_input.ModifyInstanceGroupsInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.modify_instance_groups

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.modify_instance_groups.modify_instance_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.modify_instance_groups_input.ModifyInstanceGroupsInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if instance_groups is not None:
            input_["instance_groups"] = instance_groups

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_auto_scaling_policy(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        instance_group_id: Optional[
            "capo_emr.types.instance_group_id.InstanceGroupId"
        ] = None,
        auto_scaling_policy: Optional[
            "capo_emr.types.auto_scaling_policy.AutoScalingPolicy"
        ] = None,
    ) -> "capo_emr.types.put_auto_scaling_policy_output.PutAutoScalingPolicyOutput":
        """<p>Creates or updates an automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric.</p>

        Args:
            cluster_id: <p>Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.</p>
            instance_group_id: <p>Specifies the ID of the instance group to which the automatic scaling policy is applied.</p>
            auto_scaling_policy: <p>Specifies the definition of the automatic scaling policy.</p>

        Raises:
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.put_auto_scaling_policy_input.PutAutoScalingPolicyInput]",
        ) -> OperationResponse[
            "capo_emr.types.put_auto_scaling_policy_output.PutAutoScalingPolicyOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.put_auto_scaling_policy

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.put_auto_scaling_policy.put_auto_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.put_auto_scaling_policy_input.PutAutoScalingPolicyInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if instance_group_id is not None:
            input_["instance_group_id"] = instance_group_id
        if auto_scaling_policy is not None:
            input_["auto_scaling_policy"] = auto_scaling_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_auto_termination_policy(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        auto_termination_policy: Optional[
            "capo_emr.types.auto_termination_policy.AutoTerminationPolicy"
        ] = None,
    ) -> "capo_emr.types.put_auto_termination_policy_output.PutAutoTerminationPolicyOutput":
        """<note> <p>Auto-termination is supported in Amazon EMR releases 5.30.0 and 6.1.0 and later. For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-auto-termination-policy.html">Using an auto-termination policy</a>.</p> </note> <p>Creates or updates an auto-termination policy for an Amazon EMR cluster. An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates. For alternative cluster termination options, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html">Control cluster termination</a>.</p>

        Args:
            cluster_id: <p>Specifies the ID of the Amazon EMR cluster to which the auto-termination policy will be attached.</p>
            auto_termination_policy: <p>Specifies the auto-termination policy to attach to the cluster.</p>

        Raises:
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.put_auto_termination_policy_input.PutAutoTerminationPolicyInput]",
        ) -> OperationResponse[
            "capo_emr.types.put_auto_termination_policy_output.PutAutoTerminationPolicyOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.put_auto_termination_policy

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.put_auto_termination_policy.put_auto_termination_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.put_auto_termination_policy_input.PutAutoTerminationPolicyInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if auto_termination_policy is not None:
            input_["auto_termination_policy"] = auto_termination_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_block_public_access_configuration(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        block_public_access_configuration: Optional[
            "capo_emr.types.block_public_access_configuration.BlockPublicAccessConfiguration"
        ] = None,
    ) -> "capo_emr.types.put_block_public_access_configuration_output.PutBlockPublicAccessConfigurationOutput":
        """<p>Creates or updates an Amazon EMR block public access configuration for your Amazon Web Services account in the current Region. For more information see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/configure-block-public-access.html">Configure Block Public Access for Amazon EMR</a> in the <i>Amazon EMR Management Guide</i>.</p>

        Args:
            block_public_access_configuration: <p>A configuration for Amazon EMR block public access. The configuration applies to all clusters created in your account for the current Region. The configuration specifies whether block public access is enabled. If block public access is enabled, security groups associated with the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port, unless the port is specified as an exception using <code>PermittedPublicSecurityGroupRuleRanges</code> in the <code>BlockPublicAccessConfiguration</code>. By default, Port 22 (SSH) is an exception, and public access is allowed on this port. You can change this by updating <code>BlockPublicSecurityGroupRules</code> to remove the exception.</p> <note> <p>For accounts that created clusters in a Region before November 25, 2019, block public access is disabled by default in that Region. To use this feature, you must manually enable and configure it. For accounts that did not create an Amazon EMR cluster in a Region before this date, block public access is enabled by default in that Region.</p> </note>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.put_block_public_access_configuration_input.PutBlockPublicAccessConfigurationInput]",
        ) -> OperationResponse[
            "capo_emr.types.put_block_public_access_configuration_output.PutBlockPublicAccessConfigurationOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.put_block_public_access_configuration

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.put_block_public_access_configuration.put_block_public_access_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.put_block_public_access_configuration_input.PutBlockPublicAccessConfigurationInput = {}
        if block_public_access_configuration is not None:
            input_["block_public_access_configuration"] = (
                block_public_access_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_managed_scaling_policy(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        managed_scaling_policy: Optional[
            "capo_emr.types.managed_scaling_policy.ManagedScalingPolicy"
        ] = None,
    ) -> (
        "capo_emr.types.put_managed_scaling_policy_output.PutManagedScalingPolicyOutput"
    ):
        """<p>Creates or updates a managed scaling policy for an Amazon EMR cluster. The managed scaling policy defines the limits for resources, such as Amazon EC2 instances that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration. </p>

        Args:
            cluster_id: <p>Specifies the ID of an Amazon EMR cluster where the managed scaling policy is attached. </p>
            managed_scaling_policy: <p>Specifies the constraints for the managed scaling policy. </p>

        Raises:
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.put_managed_scaling_policy_input.PutManagedScalingPolicyInput]",
        ) -> OperationResponse[
            "capo_emr.types.put_managed_scaling_policy_output.PutManagedScalingPolicyOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.put_managed_scaling_policy

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.put_managed_scaling_policy.put_managed_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.put_managed_scaling_policy_input.PutManagedScalingPolicyInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if managed_scaling_policy is not None:
            input_["managed_scaling_policy"] = managed_scaling_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_auto_scaling_policy(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        instance_group_id: Optional[
            "capo_emr.types.instance_group_id.InstanceGroupId"
        ] = None,
    ) -> (
        "capo_emr.types.remove_auto_scaling_policy_output.RemoveAutoScalingPolicyOutput"
    ):
        """<p>Removes an automatic scaling policy from a specified instance group within an Amazon EMR cluster.</p>

        Args:
            cluster_id: <p>Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.</p>
            instance_group_id: <p>Specifies the ID of the instance group to which the scaling policy is applied.</p>

        Raises:
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.remove_auto_scaling_policy_input.RemoveAutoScalingPolicyInput]",
        ) -> OperationResponse[
            "capo_emr.types.remove_auto_scaling_policy_output.RemoveAutoScalingPolicyOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.remove_auto_scaling_policy

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.remove_auto_scaling_policy.remove_auto_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.remove_auto_scaling_policy_input.RemoveAutoScalingPolicyInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if instance_group_id is not None:
            input_["instance_group_id"] = instance_group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_auto_termination_policy(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
    ) -> "capo_emr.types.remove_auto_termination_policy_output.RemoveAutoTerminationPolicyOutput":
        """<p>Removes an auto-termination policy from an Amazon EMR cluster.</p>

        Args:
            cluster_id: <p>Specifies the ID of the Amazon EMR cluster from which the auto-termination policy will be removed.</p>

        Raises:
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.remove_auto_termination_policy_input.RemoveAutoTerminationPolicyInput]",
        ) -> OperationResponse[
            "capo_emr.types.remove_auto_termination_policy_output.RemoveAutoTerminationPolicyOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.remove_auto_termination_policy

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.remove_auto_termination_policy.remove_auto_termination_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.remove_auto_termination_policy_input.RemoveAutoTerminationPolicyInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_managed_scaling_policy(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
    ) -> "capo_emr.types.remove_managed_scaling_policy_output.RemoveManagedScalingPolicyOutput":
        """<p> Removes a managed scaling policy from a specified Amazon EMR cluster. </p>

        Args:
            cluster_id: <p> Specifies the ID of the cluster from which the managed scaling policy will be removed. </p>

        Raises:
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.remove_managed_scaling_policy_input.RemoveManagedScalingPolicyInput]",
        ) -> OperationResponse[
            "capo_emr.types.remove_managed_scaling_policy_output.RemoveManagedScalingPolicyOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.remove_managed_scaling_policy

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.remove_managed_scaling_policy.remove_managed_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.remove_managed_scaling_policy_input.RemoveManagedScalingPolicyInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_tags(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        resource_id: Optional["capo_emr.types.resource_id.ResourceId"] = None,
        tag_keys: Optional["capo_emr.types.string_list.StringList"] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
    ) -> "capo_emr.types.remove_tags_output.RemoveTagsOutput":
        """<p>Removes tags from an Amazon EMR resource, such as a cluster or Amazon EMR Studio. Tags make it easier to associate resources in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html">Tag Clusters</a>. </p> <p>The following example removes the stack tag with value Prod from a cluster:</p>

        Args:
            resource_id: <p>The Amazon EMR resource identifier from which tags will be removed. For example, a cluster identifier or an Amazon EMR Studio ID.</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>
            cluster_id: <p>The ID of the cluster that scopes the tag operation. Required when the resource being untagged is a session-scoped resource.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.remove_tags_input.RemoveTagsInput]",
        ) -> OperationResponse["capo_emr.types.remove_tags_output.RemoveTagsOutput"]:
            import capo_emr._operations.elastic_map_reduce.remove_tags

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.remove_tags.remove_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.remove_tags_input.RemoveTagsInput = {}
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def run_job_flow(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        log_uri: Optional["capo_emr.types.xml_string.XmlString"] = None,
        log_encryption_kms_key_id: Optional[
            "capo_emr.types.xml_string.XmlString"
        ] = None,
        additional_info: Optional["capo_emr.types.xml_string.XmlString"] = None,
        ami_version: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        release_label: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        instances: Optional[
            "capo_emr.types.job_flow_instances_config.JobFlowInstancesConfig"
        ] = None,
        steps: Optional["capo_emr.types.step_config_list.StepConfigList"] = None,
        step_execution_role_arn: Optional["capo_emr.types.arn_type.ArnType"] = None,
        bootstrap_actions: Optional[
            "capo_emr.types.bootstrap_action_config_list.BootstrapActionConfigList"
        ] = None,
        supported_products: Optional[
            "capo_emr.types.supported_products_list.SupportedProductsList"
        ] = None,
        new_supported_products: Optional[
            "capo_emr.types.new_supported_products_list.NewSupportedProductsList"
        ] = None,
        applications: Optional[
            "capo_emr.types.application_list.ApplicationList"
        ] = None,
        configurations: Optional[
            "capo_emr.types.configuration_list.ConfigurationList"
        ] = None,
        visible_to_all_users: Optional["capo_emr.types.boolean.Boolean"] = None,
        job_flow_role: Optional["capo_emr.types.xml_string.XmlString"] = None,
        service_role: Optional["capo_emr.types.xml_string.XmlString"] = None,
        tags: Optional["capo_emr.types.tag_list.TagList"] = None,
        security_configuration: Optional["capo_emr.types.xml_string.XmlString"] = None,
        auto_scaling_role: Optional["capo_emr.types.xml_string.XmlString"] = None,
        scale_down_behavior: Optional[
            "capo_emr.types.scale_down_behavior.ScaleDownBehavior"
        ] = None,
        custom_ami_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        ebs_root_volume_size: Optional["capo_emr.types.integer.Integer"] = None,
        repo_upgrade_on_boot: Optional[
            "capo_emr.types.repo_upgrade_on_boot.RepoUpgradeOnBoot"
        ] = None,
        kerberos_attributes: Optional[
            "capo_emr.types.kerberos_attributes.KerberosAttributes"
        ] = None,
        step_concurrency_level: Optional["capo_emr.types.integer.Integer"] = None,
        managed_scaling_policy: Optional[
            "capo_emr.types.managed_scaling_policy.ManagedScalingPolicy"
        ] = None,
        placement_group_configs: Optional[
            "capo_emr.types.placement_group_config_list.PlacementGroupConfigList"
        ] = None,
        auto_termination_policy: Optional[
            "capo_emr.types.auto_termination_policy.AutoTerminationPolicy"
        ] = None,
        os_release_label: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        ebs_root_volume_iops: Optional["capo_emr.types.integer.Integer"] = None,
        ebs_root_volume_throughput: Optional["capo_emr.types.integer.Integer"] = None,
        extended_support: Optional[
            "capo_emr.types.boolean_object.BooleanObject"
        ] = None,
        monitoring_configuration: Optional[
            "capo_emr.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
        session_enabled: Optional["capo_emr.types.boolean_object.BooleanObject"] = None,
    ) -> "capo_emr.types.run_job_flow_output.RunJobFlowOutput":
        """<p>RunJobFlow creates and starts running a new cluster (job flow). The cluster runs the steps specified. After the steps complete, the cluster stops and the HDFS partition is lost. To prevent loss of data, configure the last step of the job flow to store results in Amazon S3. If the <a>JobFlowInstancesConfig</a> <code>KeepJobFlowAliveWhenNoSteps</code> parameter is set to <code>TRUE</code>, the cluster transitions to the WAITING state rather than shutting down after the steps have completed. </p> <p>For additional protection, you can set the <a>JobFlowInstancesConfig</a> <code>TerminationProtected</code> parameter to <code>TRUE</code> to lock the cluster and prevent it from being terminated by API call, user intervention, or in the event of a job flow error.</p> <p>A maximum of 256 steps are allowed in each job flow.</p> <p>If your cluster is long-running (such as a Hive data warehouse) or complex, you may require more than 256 steps to process your data. You can bypass the 256-step limitation in various ways, including using the SSH shell to connect to the master node and submitting queries directly to the software running on the master node, such as Hive and Hadoop.</p> <p>For long-running clusters, we recommend that you periodically store your results.</p> <note> <p>The instance fleets configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. The RunJobFlow request can contain InstanceFleets parameters or InstanceGroups parameters, but not both.</p> </note>

        Args:
            name: <p>The name of the job flow.</p>
            log_uri: <p>The location in Amazon S3 to write the log files of the job flow. If a value is not provided, logs are not created.</p>
            log_encryption_kms_key_id: <p>The KMS key used for encrypting log files. If a value is not provided, the logs remain encrypted by AES-256. This attribute is only available with Amazon EMR releases 5.30.0 and later, excluding Amazon EMR 6.0.0.</p>
            additional_info: <p>A JSON string for selecting additional features.</p>
            ami_version: <p>Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR releases 4.0 and later, <code>ReleaseLabel</code> is used. To specify a custom AMI, use <code>CustomAmiID</code>.</p>
            release_label: <p>The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form <code>emr-x.x.x</code>, where x.x.x is an Amazon EMR release version such as <code>emr-5.14.0</code>. For more information about Amazon EMR release versions and included application versions and features, see <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/">https://docs.aws.amazon.com/emr/latest/ReleaseGuide/</a>. The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use <code>AmiVersion</code>.</p>
            instances: <p>A specification of the number and type of Amazon EC2 instances.</p>
            steps: <p>A list of steps to run.</p>
            step_execution_role_arn: <p>The Amazon Resource Name (ARN) of the runtime role for steps specified in the RunJobFlow request. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: <code>arn:partition:iam::account-id:role/role-name</code>.</p> <p>For example, <code>arn:aws:iam::1234567890:role/ReadOnly</code> is a correctly formatted runtime role ARN.</p> <p>This parameter applies only to steps included in the <code>Steps</code> parameter of this RunJobFlow request. It does not apply to steps added later to the cluster.</p>
            bootstrap_actions: <p>A list of bootstrap actions to run before Hadoop starts on the cluster nodes.</p>
            supported_products: <note> <p>For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later, use Applications.</p> </note> <p>A list of strings that indicates third-party software to use. For more information, see the <a href="https://docs.aws.amazon.com/emr/latest/DeveloperGuide/emr-dg.pdf">Amazon EMR Developer Guide</a>. Currently supported values are:</p> <ul> <li> <p>"mapr-m3" - launch the job flow using MapR M3 Edition.</p> </li> <li> <p>"mapr-m5" - launch the job flow using MapR M5 Edition.</p> </li> </ul>
            new_supported_products: <note> <p>For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later, use Applications.</p> </note> <p>A list of strings that indicates third-party software to use with the job flow that accepts a user argument list. Amazon EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action arguments. For more information, see "Launch a Job Flow on the MapR Distribution for Hadoop" in the <a href="https://docs.aws.amazon.com/emr/latest/DeveloperGuide/emr-dg.pdf">Amazon EMR Developer Guide</a>. Supported values are:</p> <ul> <li> <p>"mapr-m3" - launch the cluster using MapR M3 Edition.</p> </li> <li> <p>"mapr-m5" - launch the cluster using MapR M5 Edition.</p> </li> <li> <p>"mapr" with the user arguments specifying "--edition,m3" or "--edition,m5" - launch the job flow using MapR M3 or M5 Edition respectively.</p> </li> <li> <p>"mapr-m7" - launch the cluster using MapR M7 Edition.</p> </li> <li> <p>"hunk" - launch the cluster with the Hunk Big Data Analytics Platform.</p> </li> <li> <p>"hue"- launch the cluster with Hue installed.</p> </li> <li> <p>"spark" - launch the cluster with Apache Spark installed.</p> </li> <li> <p>"ganglia" - launch the cluster with the Ganglia Monitoring System installed.</p> </li> </ul>
            applications: <p>Applies to Amazon EMR releases 4.0 and later. A case-insensitive list of applications for Amazon EMR to install and configure when launching the cluster. For a list of applications available for each Amazon EMR release version, see the <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/">Amazon EMRRelease Guide</a>.</p>
            configurations: <p>For Amazon EMR releases 4.0 and later. The list of configurations supplied for the Amazon EMR cluster that you are creating.</p>
            visible_to_all_users: <important> <p>The VisibleToAllUsers parameter is no longer supported. By default, the value is set to <code>true</code>. Setting it to <code>false</code> now has no effect.</p> </important> <p>Set this value to <code>true</code> so that IAM principals in the Amazon Web Services account associated with the cluster can perform Amazon EMR actions on the cluster that their IAM policies allow. This value defaults to <code>true</code> for clusters created using the Amazon EMR API or the CLI <a href="https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html">create-cluster</a> command.</p> <p>When set to <code>false</code>, only the IAM principal that created the cluster and the Amazon Web Services account root user can perform Amazon EMR actions for the cluster, regardless of the IAM permissions policies attached to other IAM principals. For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_IAM_emr-with-IAM.html#security_set_visible_to_all_users">Understanding the Amazon EMR cluster VisibleToAllUsers setting</a> in the <i>Amazon EMR Management Guide</i>.</p>
            job_flow_role: <p>Also called instance profile and Amazon EC2 role. An IAM role for an Amazon EMR cluster. The Amazon EC2 instances of the cluster assume this role. The default role is <code>EMR_EC2_DefaultRole</code>. In order to use the default role, you must have already created it using the CLI or console.</p>
            service_role: <p>The IAM role that Amazon EMR assumes in order to access Amazon Web Services resources on your behalf. If you've created a custom service role path, you must specify it for the service role when you launch your cluster.</p>
            tags: <p>A list of tags to associate with a cluster and propagate to Amazon EC2 instances.</p>
            security_configuration: <p>The name of a security configuration to apply to the cluster.</p>
            auto_scaling_role: <p>An IAM role for automatic scaling policies. The default role is <code>EMR_AutoScaling_DefaultRole</code>. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.</p>
            scale_down_behavior: <p>Specifies the way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. <code>TERMINATE_AT_INSTANCE_HOUR</code> indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. <code>TERMINATE_AT_TASK_COMPLETION</code> indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. <code>TERMINATE_AT_TASK_COMPLETION</code> available only in Amazon EMR releases 4.1.0 and later, and is the default for releases of Amazon EMR earlier than 5.1.0.</p>
            custom_ami_id: <p>Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI. If specified, Amazon EMR uses this AMI when it launches cluster Amazon EC2 instances. For more information about custom AMIs in Amazon EMR, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-ami.html">Using a Custom AMI</a> in the <i>Amazon EMR Management Guide</i>. If omitted, the cluster uses the base Linux AMI for the <code>ReleaseLabel</code> specified. For Amazon EMR releases 2.x and 3.x, use <code>AmiVersion</code> instead.</p> <p>For information about creating a custom AMI, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html">Creating an Amazon EBS-Backed Linux AMI</a> in the <i>Amazon Elastic Compute Cloud User Guide for Linux Instances</i>. For information about finding an AMI ID, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html">Finding a Linux AMI</a>. </p>
            ebs_root_volume_size: <p>The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 4.x and later.</p>
            repo_upgrade_on_boot: <p>Applies only when <code>CustomAmiID</code> is used. Specifies which updates from the Amazon Linux AMI package repositories to apply automatically when the instance boots using the AMI. If omitted, the default is <code>SECURITY</code>, which indicates that only security updates are applied. If <code>NONE</code> is specified, no updates are applied, and all updates must be applied manually.</p>
            kerberos_attributes: <p>Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html">Use Kerberos Authentication</a> in the <i>Amazon EMR Management Guide</i>.</p>
            step_concurrency_level: <p>Specifies the number of steps that can be executed concurrently. The default value is <code>1</code>. The maximum value is <code>256</code>.</p>
            managed_scaling_policy: <p> The specified managed scaling policy for an Amazon EMR cluster. </p>
            placement_group_configs: <p>The specified placement group configuration for an Amazon EMR cluster.</p>
            os_release_label: <p>Specifies a particular Amazon Linux release for all nodes in a cluster launch RunJobFlow request. If a release is not specified, Amazon EMR uses the latest validated Amazon Linux release for cluster launch.</p>
            ebs_root_volume_iops: <p>The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.</p>
            ebs_root_volume_throughput: <p>The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.</p>
            extended_support: <p>Reserved.</p>
            monitoring_configuration: <p>Contains CloudWatch log configuration metadata and settings.</p>
            session_enabled: <p>Indicates whether Spark Connect sessions are enabled on the cluster. When set to <code>true</code>, you can start Spark Connect sessions using the <code>StartSession</code> operation.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.run_job_flow_input.RunJobFlowInput]",
        ) -> OperationResponse["capo_emr.types.run_job_flow_output.RunJobFlowOutput"]:
            import capo_emr._operations.elastic_map_reduce.run_job_flow

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.run_job_flow.run_job_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.run_job_flow_input.RunJobFlowInput = {}
        if name is not None:
            input_["name"] = name
        if log_uri is not None:
            input_["log_uri"] = log_uri
        if log_encryption_kms_key_id is not None:
            input_["log_encryption_kms_key_id"] = log_encryption_kms_key_id
        if additional_info is not None:
            input_["additional_info"] = additional_info
        if ami_version is not None:
            input_["ami_version"] = ami_version
        if release_label is not None:
            input_["release_label"] = release_label
        if instances is not None:
            input_["instances"] = instances
        if steps is not None:
            input_["steps"] = steps
        if step_execution_role_arn is not None:
            input_["step_execution_role_arn"] = step_execution_role_arn
        if bootstrap_actions is not None:
            input_["bootstrap_actions"] = bootstrap_actions
        if supported_products is not None:
            input_["supported_products"] = supported_products
        if new_supported_products is not None:
            input_["new_supported_products"] = new_supported_products
        if applications is not None:
            input_["applications"] = applications
        if configurations is not None:
            input_["configurations"] = configurations
        if visible_to_all_users is not None:
            input_["visible_to_all_users"] = visible_to_all_users
        if job_flow_role is not None:
            input_["job_flow_role"] = job_flow_role
        if service_role is not None:
            input_["service_role"] = service_role
        if tags is not None:
            input_["tags"] = tags
        if security_configuration is not None:
            input_["security_configuration"] = security_configuration
        if auto_scaling_role is not None:
            input_["auto_scaling_role"] = auto_scaling_role
        if scale_down_behavior is not None:
            input_["scale_down_behavior"] = scale_down_behavior
        if custom_ami_id is not None:
            input_["custom_ami_id"] = custom_ami_id
        if ebs_root_volume_size is not None:
            input_["ebs_root_volume_size"] = ebs_root_volume_size
        if repo_upgrade_on_boot is not None:
            input_["repo_upgrade_on_boot"] = repo_upgrade_on_boot
        if kerberos_attributes is not None:
            input_["kerberos_attributes"] = kerberos_attributes
        if step_concurrency_level is not None:
            input_["step_concurrency_level"] = step_concurrency_level
        if managed_scaling_policy is not None:
            input_["managed_scaling_policy"] = managed_scaling_policy
        if placement_group_configs is not None:
            input_["placement_group_configs"] = placement_group_configs
        if auto_termination_policy is not None:
            input_["auto_termination_policy"] = auto_termination_policy
        if os_release_label is not None:
            input_["os_release_label"] = os_release_label
        if ebs_root_volume_iops is not None:
            input_["ebs_root_volume_iops"] = ebs_root_volume_iops
        if ebs_root_volume_throughput is not None:
            input_["ebs_root_volume_throughput"] = ebs_root_volume_throughput
        if extended_support is not None:
            input_["extended_support"] = extended_support
        if monitoring_configuration is not None:
            input_["monitoring_configuration"] = monitoring_configuration
        if session_enabled is not None:
            input_["session_enabled"] = session_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_keep_job_flow_alive_when_no_steps(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        job_flow_ids: Optional["capo_emr.types.xml_string_list.XmlStringList"] = None,
        keep_job_flow_alive_when_no_steps: Optional[
            "capo_emr.types.boolean.Boolean"
        ] = None,
    ) -> None:
        """<p>You can use the <code>SetKeepJobFlowAliveWhenNoSteps</code> to configure a cluster (job flow) to terminate after the step execution, i.e., all your steps are executed. If you want a transient cluster that shuts down after the last of the current executing steps are completed, you can configure <code>SetKeepJobFlowAliveWhenNoSteps</code> to false. If you want a long running cluster, configure <code>SetKeepJobFlowAliveWhenNoSteps</code> to true.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_TerminationProtection.html">Managing Cluster Termination</a> in the <i>Amazon EMR Management Guide</i>.</p>

        Args:
            job_flow_ids: <p>A list of strings that uniquely identify the clusters to protect. This identifier is returned by <a href="https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html">RunJobFlow</a> and can also be obtained from <a href="https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeJobFlows.html">DescribeJobFlows</a>.</p>
            keep_job_flow_alive_when_no_steps: <p>A Boolean that indicates whether to terminate the cluster after all steps are executed.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.set_keep_job_flow_alive_when_no_steps_input.SetKeepJobFlowAliveWhenNoStepsInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.set_keep_job_flow_alive_when_no_steps

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.set_keep_job_flow_alive_when_no_steps.set_keep_job_flow_alive_when_no_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.set_keep_job_flow_alive_when_no_steps_input.SetKeepJobFlowAliveWhenNoStepsInput = {}
        if job_flow_ids is not None:
            input_["job_flow_ids"] = job_flow_ids
        if keep_job_flow_alive_when_no_steps is not None:
            input_["keep_job_flow_alive_when_no_steps"] = (
                keep_job_flow_alive_when_no_steps
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_termination_protection(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        job_flow_ids: Optional["capo_emr.types.xml_string_list.XmlStringList"] = None,
        termination_protected: Optional["capo_emr.types.boolean.Boolean"] = None,
    ) -> None:
        """<p>SetTerminationProtection locks a cluster (job flow) so the Amazon EC2 instances in the cluster cannot be terminated by user intervention, an API call, or in the event of a job-flow error. The cluster still terminates upon successful completion of the job flow. Calling <code>SetTerminationProtection</code> on a cluster is similar to calling the Amazon EC2 <code>DisableAPITermination</code> API on all Amazon EC2 instances in a cluster.</p> <p> <code>SetTerminationProtection</code> is used to prevent accidental termination of a cluster and to ensure that in the event of an error, the instances persist so that you can recover any data stored in their ephemeral instance storage.</p> <p> To terminate a cluster that has been locked by setting <code>SetTerminationProtection</code> to <code>true</code>, you must first unlock the job flow by a subsequent call to <code>SetTerminationProtection</code> in which you set the value to <code>false</code>. </p> <p> For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_TerminationProtection.html">Managing Cluster Termination</a> in the <i>Amazon EMR Management Guide</i>. </p>

        Args:
            job_flow_ids: <p> A list of strings that uniquely identify the clusters to protect. This identifier is returned by <a>RunJobFlow</a> and can also be obtained from <a>DescribeJobFlows</a> . </p>
            termination_protected: <p>A Boolean that indicates whether to protect the cluster and prevent the Amazon EC2 instances in the cluster from shutting down due to API calls, user intervention, or job-flow error.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.set_termination_protection_input.SetTerminationProtectionInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.set_termination_protection

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.set_termination_protection.set_termination_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.set_termination_protection_input.SetTerminationProtectionInput = {}
        if job_flow_ids is not None:
            input_["job_flow_ids"] = job_flow_ids
        if termination_protected is not None:
            input_["termination_protected"] = termination_protected

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_unhealthy_node_replacement(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        job_flow_ids: Optional["capo_emr.types.xml_string_list.XmlStringList"] = None,
        unhealthy_node_replacement: Optional[
            "capo_emr.types.boolean_object.BooleanObject"
        ] = None,
    ) -> None:
        """<p>Specify whether to enable unhealthy node replacement, which lets Amazon EMR gracefully replace core nodes on a cluster if any nodes become unhealthy. For example, a node becomes unhealthy if disk usage is above 90%. If unhealthy node replacement is on and <code>TerminationProtected</code> are off, Amazon EMR immediately terminates the unhealthy core nodes. To use unhealthy node replacement and retain unhealthy core nodes, use to turn on termination protection. In such cases, Amazon EMR adds the unhealthy nodes to a denylist, reducing job interruptions and failures.</p> <p>If unhealthy node replacement is on, Amazon EMR notifies YARN and other applications on the cluster to stop scheduling tasks with these nodes, moves the data, and then terminates the nodes.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-node-replacement.html">graceful node replacement</a> in the <i>Amazon EMR Management Guide</i>.</p>

        Args:
            job_flow_ids: <p>The list of strings that uniquely identify the clusters for which to turn on unhealthy node replacement. You can get these identifiers by running the <a>RunJobFlow</a> or the <a>DescribeJobFlows</a> operations.</p>
            unhealthy_node_replacement: <p>Indicates whether to turn on or turn off graceful unhealthy node replacement.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.set_unhealthy_node_replacement_input.SetUnhealthyNodeReplacementInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.set_unhealthy_node_replacement

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.set_unhealthy_node_replacement.set_unhealthy_node_replacement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.set_unhealthy_node_replacement_input.SetUnhealthyNodeReplacementInput = {}
        if job_flow_ids is not None:
            input_["job_flow_ids"] = job_flow_ids
        if unhealthy_node_replacement is not None:
            input_["unhealthy_node_replacement"] = unhealthy_node_replacement

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_visible_to_all_users(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        job_flow_ids: Optional["capo_emr.types.xml_string_list.XmlStringList"] = None,
        visible_to_all_users: Optional["capo_emr.types.boolean.Boolean"] = None,
    ) -> None:
        """<important> <p>The SetVisibleToAllUsers parameter is no longer supported. Your cluster may be visible to all users in your account. To restrict cluster access using an IAM policy, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-IAM.html">Identity and Access Management for Amazon EMR</a>. </p> </important> <p>Sets the <a>Cluster$VisibleToAllUsers</a> value for an Amazon EMR cluster. When <code>true</code>, IAM principals in the Amazon Web Services account can perform Amazon EMR cluster actions that their IAM policies allow. When <code>false</code>, only the IAM principal that created the cluster and the Amazon Web Services account root user can perform Amazon EMR actions on the cluster, regardless of IAM permissions policies attached to other IAM principals.</p> <p>This action works on running clusters. When you create a cluster, use the <a>RunJobFlowInput$VisibleToAllUsers</a> parameter.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_IAM_emr-with-IAM.html#security_set_visible_to_all_users">Understanding the Amazon EMR Cluster VisibleToAllUsers Setting</a> in the <i>Amazon EMR Management Guide</i>.</p>

        Args:
            job_flow_ids: <p>The unique identifier of the job flow (cluster).</p>
            visible_to_all_users: <p>A value of <code>true</code> indicates that an IAM principal in the Amazon Web Services account can perform Amazon EMR actions on the cluster that the IAM policies attached to the principal allow. A value of <code>false</code> indicates that only the IAM principal that created the cluster and the Amazon Web Services root user can perform Amazon EMR actions on the cluster.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.set_visible_to_all_users_input.SetVisibleToAllUsersInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.set_visible_to_all_users

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.set_visible_to_all_users.set_visible_to_all_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.set_visible_to_all_users_input.SetVisibleToAllUsersInput = {}
        if job_flow_ids is not None:
            input_["job_flow_ids"] = job_flow_ids
        if visible_to_all_users is not None:
            input_["visible_to_all_users"] = visible_to_all_users

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_notebook_execution(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        editor_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        relative_path: Optional["capo_emr.types.xml_string.XmlString"] = None,
        notebook_execution_name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        notebook_params: Optional["capo_emr.types.xml_string.XmlString"] = None,
        execution_engine: Optional[
            "capo_emr.types.execution_engine_config.ExecutionEngineConfig"
        ] = None,
        service_role: Optional["capo_emr.types.xml_string.XmlString"] = None,
        notebook_instance_security_group_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        tags: Optional["capo_emr.types.tag_list.TagList"] = None,
        notebook_s3_location: Optional[
            "capo_emr.types.notebook_s3_location_from_input.NotebookS3LocationFromInput"
        ] = None,
        output_notebook_s3_location: Optional[
            "capo_emr.types.output_notebook_s3_location_from_input.OutputNotebookS3LocationFromInput"
        ] = None,
        output_notebook_format: Optional[
            "capo_emr.types.output_notebook_format.OutputNotebookFormat"
        ] = None,
        environment_variables: Optional[
            "capo_emr.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
    ) -> "capo_emr.types.start_notebook_execution_output.StartNotebookExecutionOutput":
        """<p>Starts a notebook execution.</p>

        Args:
            editor_id: <p>The unique identifier of the Amazon EMR Notebook to use for notebook execution.</p>
            relative_path: <p>The path and file name of the notebook file for this execution, relative to the path specified for the Amazon EMR Notebook. For example, if you specify a path of <code>s3://MyBucket/MyNotebooks</code> when you create an Amazon EMR Notebook for a notebook with an ID of <code>e-ABCDEFGHIJK1234567890ABCD</code> (the <code>EditorID</code> of this request), and you specify a <code>RelativePath</code> of <code>my_notebook_executions/notebook_execution.ipynb</code>, the location of the file for the notebook execution is <code>s3://MyBucket/MyNotebooks/e-ABCDEFGHIJK1234567890ABCD/my_notebook_executions/notebook_execution.ipynb</code>.</p>
            notebook_execution_name: <p>An optional name for the notebook execution.</p>
            notebook_params: <p>Input parameters in JSON format passed to the Amazon EMR Notebook at runtime for execution.</p>
            execution_engine: <p>Specifies the execution engine (cluster) that runs the notebook execution.</p>
            service_role: <p>The name or ARN of the IAM role that is used as the service role for Amazon EMR (the Amazon EMR role) for the notebook execution.</p>
            notebook_instance_security_group_id: <p>The unique identifier of the Amazon EC2 security group to associate with the Amazon EMR Notebook for this notebook execution.</p>
            tags: <p>A list of tags associated with a notebook execution. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters and an optional value string with a maximum of 256 characters.</p>
            notebook_s3_location: <p>The Amazon S3 location for the notebook execution input.</p>
            output_notebook_s3_location: <p>The Amazon S3 location for the notebook execution output.</p>
            output_notebook_format: <p>The output format for the notebook execution.</p>
            environment_variables: <p>The environment variables associated with the notebook execution.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.start_notebook_execution_input.StartNotebookExecutionInput]",
        ) -> OperationResponse[
            "capo_emr.types.start_notebook_execution_output.StartNotebookExecutionOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.start_notebook_execution

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.start_notebook_execution.start_notebook_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.start_notebook_execution_input.StartNotebookExecutionInput = {}
        if editor_id is not None:
            input_["editor_id"] = editor_id
        if relative_path is not None:
            input_["relative_path"] = relative_path
        if notebook_execution_name is not None:
            input_["notebook_execution_name"] = notebook_execution_name
        if notebook_params is not None:
            input_["notebook_params"] = notebook_params
        if execution_engine is not None:
            input_["execution_engine"] = execution_engine
        if service_role is not None:
            input_["service_role"] = service_role
        if notebook_instance_security_group_id is not None:
            input_["notebook_instance_security_group_id"] = (
                notebook_instance_security_group_id
            )
        if tags is not None:
            input_["tags"] = tags
        if notebook_s3_location is not None:
            input_["notebook_s3_location"] = notebook_s3_location
        if output_notebook_s3_location is not None:
            input_["output_notebook_s3_location"] = output_notebook_s3_location
        if output_notebook_format is not None:
            input_["output_notebook_format"] = output_notebook_format
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_session(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        execution_role_arn: Optional["capo_emr.types.iam_role_arn.IAMRoleArn"] = None,
        engine_configurations: Optional[
            "capo_emr.types.configuration_list.ConfigurationList"
        ] = None,
        monitoring_configuration: Optional[
            "capo_emr.types.session_monitoring_configuration.SessionMonitoringConfiguration"
        ] = None,
        session_idle_timeout_in_minutes: Optional["capo_emr.types.long.Long"] = None,
        client_request_token: Optional[
            "capo_emr.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_emr.types.tag_list.TagList"] = None,
    ) -> "capo_emr.types.start_session_output.StartSessionOutput":
        """<p>Creates and starts a new Spark Connect session on the specified cluster. The cluster must be in the <code>RUNNING</code> or <code>WAITING</code> state and have sessions enabled. This operation is supported in Amazon EMR Spark 8.0.0 and later.</p>

        Args:
            name: <p>An optional name for the session.</p>
            cluster_id: <p>The ID of the cluster on which to start the session.</p>
            execution_role_arn: <p>The execution role ARN for the session. Amazon EMR uses this role to access Amazon Web Services resources on your behalf during session execution.</p>
            engine_configurations: <p>The configuration overrides for the session. Only runtime configuration overrides are supported.</p>
            monitoring_configuration: <p>The monitoring configuration that controls where session logs are published, such as Amazon S3, CloudWatch, or managed logging.</p>
            session_idle_timeout_in_minutes: <p>The idle timeout, in minutes. If the session is idle for this duration, Amazon EMR EC2 automatically terminates it.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client request token, the service returns the original response without performing the operation again.</p>
            tags: <p>The tags to assign to the session.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.start_session_input.StartSessionInput]",
        ) -> OperationResponse[
            "capo_emr.types.start_session_output.StartSessionOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.start_session

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.start_session.start_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.start_session_input.StartSessionInput = {}
        if name is not None:
            input_["name"] = name
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if engine_configurations is not None:
            input_["engine_configurations"] = engine_configurations
        if monitoring_configuration is not None:
            input_["monitoring_configuration"] = monitoring_configuration
        if session_idle_timeout_in_minutes is not None:
            input_["session_idle_timeout_in_minutes"] = session_idle_timeout_in_minutes
        if client_request_token is not None:
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

    def stop_notebook_execution(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        notebook_execution_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
    ) -> None:
        """<p>Stops a notebook execution.</p>

        Args:
            notebook_execution_id: <p>The unique identifier of the notebook execution.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.stop_notebook_execution_input.StopNotebookExecutionInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.stop_notebook_execution

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.stop_notebook_execution.stop_notebook_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.stop_notebook_execution_input.StopNotebookExecutionInput = {}
        if notebook_execution_id is not None:
            input_["notebook_execution_id"] = notebook_execution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_job_flows(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        job_flow_ids: Optional["capo_emr.types.xml_string_list.XmlStringList"] = None,
    ) -> None:
        """<p>TerminateJobFlows shuts a list of clusters (job flows) down. When a job flow is shut down, any step not yet completed is canceled and the Amazon EC2 instances on which the cluster is running are stopped. Any log files not already saved are uploaded to Amazon S3 if a LogUri was specified when the cluster was created.</p> <p>The maximum number of clusters allowed is 10. The call to <code>TerminateJobFlows</code> is asynchronous. Depending on the configuration of the cluster, it may take up to 1-5 minutes for the cluster to completely terminate and release allocated resources, such as Amazon EC2 instances.</p>

        Args:
            job_flow_ids: <p>A list of job flows to be shut down.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.terminate_job_flows_input.TerminateJobFlowsInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.terminate_job_flows

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.terminate_job_flows.terminate_job_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.terminate_job_flows_input.TerminateJobFlowsInput = {}
        if job_flow_ids is not None:
            input_["job_flow_ids"] = job_flow_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_session(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        cluster_id: Optional["capo_emr.types.cluster_id.ClusterId"] = None,
        session_id: Optional["capo_emr.types.session_id.SessionId"] = None,
    ) -> "capo_emr.types.terminate_session_output.TerminateSessionOutput":
        """<p>Terminates an active session. After you call this operation, the session enters the <code>TERMINATING</code> state and then transitions to <code>TERMINATED</code>.</p>

        Args:
            cluster_id: <p>The ID of the cluster that the session belongs to.</p>
            session_id: <p>The ID of the session to terminate.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.terminate_session_input.TerminateSessionInput]",
        ) -> OperationResponse[
            "capo_emr.types.terminate_session_output.TerminateSessionOutput"
        ]:
            import capo_emr._operations.elastic_map_reduce.terminate_session

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.terminate_session.terminate_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.terminate_session_input.TerminateSessionInput = {}
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_studio(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        studio_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        description: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        subnet_ids: Optional["capo_emr.types.subnet_id_list.SubnetIdList"] = None,
        default_s3_location: Optional["capo_emr.types.xml_string.XmlString"] = None,
        encryption_key_arn: Optional["capo_emr.types.xml_string.XmlString"] = None,
    ) -> None:
        """<p>Updates an Amazon EMR Studio configuration, including attributes such as name, description, and subnets.</p>

        Args:
            studio_id: <p>The ID of the Amazon EMR Studio to update.</p>
            name: <p>A descriptive name for the Amazon EMR Studio.</p>
            description: <p>A detailed description to assign to the Amazon EMR Studio.</p>
            subnet_ids: <p>A list of subnet IDs to associate with the Amazon EMR Studio. The list can include new subnet IDs, but must also include all of the subnet IDs previously associated with the Studio. The list order does not matter. A Studio can have a maximum of 5 subnets. The subnets must belong to the same VPC as the Studio. </p>
            default_s3_location: <p>The Amazon S3 location to back up Workspaces and notebook files for the Amazon EMR Studio.</p>
            encryption_key_arn: <p>The KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.</p>

        Raises:
            capo_emr.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon EMR service.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.update_studio_input.UpdateStudioInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.update_studio

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.update_studio.update_studio(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.update_studio_input.UpdateStudioInput = {}
        if studio_id is not None:
            input_["studio_id"] = studio_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if default_s3_location is not None:
            input_["default_s3_location"] = default_s3_location
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_studio_session_mapping(
        self,
        *,
        config_overrides: Optional[EMRClientConfig] = None,
        studio_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_id: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_name: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
        identity_type: Optional["capo_emr.types.identity_type.IdentityType"] = None,
        session_policy_arn: Optional[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ] = None,
    ) -> None:
        """<p>Updates the session policy attached to the user or group for the specified Amazon EMR Studio.</p>

        Args:
            studio_id: <p>The ID of the Amazon EMR Studio.</p>
            identity_id: <p>The globally unique identifier (GUID) of the user or group. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserId">UserId</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-GroupId">GroupId</a> in the <i>IAM Identity Center Identity Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified.</p>
            identity_name: <p>The name of the user or group to update. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName">UserName</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName">DisplayName</a> in the <i>IAM Identity Center Identity Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified.</p>
            identity_type: <p>Specifies whether the identity to update is a user or a group.</p>
            session_policy_arn: <p>The Amazon Resource Name (ARN) of the session policy to associate with the specified user or group.</p>

        Raises:
            capo_emr.errors.internal_server_error.InternalServerError: <p>Indicates that an error occurred while processing the request and that the request was not completed.</p>
            capo_emr.errors.invalid_request_exception.InvalidRequestException: <p>This exception occurs when there is something wrong with user input.</p>
            capo_emr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr.types.update_studio_session_mapping_input.UpdateStudioSessionMappingInput]",
        ) -> OperationResponse[None]:
            import capo_emr._operations.elastic_map_reduce.update_studio_session_mapping

            output, http_response = (
                capo_emr._operations.elastic_map_reduce.update_studio_session_mapping.update_studio_session_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr.types.update_studio_session_mapping_input.UpdateStudioSessionMappingInput = {}
        if studio_id is not None:
            input_["studio_id"] = studio_id
        if identity_id is not None:
            input_["identity_id"] = identity_id
        if identity_name is not None:
            input_["identity_name"] = identity_name
        if identity_type is not None:
            input_["identity_type"] = identity_type
        if session_policy_arn is not None:
            input_["session_policy_arn"] = session_policy_arn

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
