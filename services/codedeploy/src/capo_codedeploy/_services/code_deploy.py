"""Generated from Smithy shape ``com.amazonaws.codedeploy#CodeDeploy_20141006``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_codedeploy._auth._signers
import capo_codedeploy._auth._sigv4
from capo_codedeploy._auth._identity import Credentials
from capo_codedeploy._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_codedeploy._auth._zapros_handler import AuthMiddleware
from capo_codedeploy._pagination import resolve_path as _resolve_path
from capo_codedeploy._services._aws_config import aws_config
from capo_codedeploy._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_codedeploy.types.add_tags_to_on_premises_instances_input
    import capo_codedeploy.types.alarm_configuration
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.application_revision_sort_by
    import capo_codedeploy.types.applications_list
    import capo_codedeploy.types.arn
    import capo_codedeploy.types.auto_rollback_configuration
    import capo_codedeploy.types.auto_scaling_group_name_list
    import capo_codedeploy.types.batch_get_application_revisions_input
    import capo_codedeploy.types.batch_get_application_revisions_output
    import capo_codedeploy.types.batch_get_applications_input
    import capo_codedeploy.types.batch_get_applications_output
    import capo_codedeploy.types.batch_get_deployment_groups_input
    import capo_codedeploy.types.batch_get_deployment_groups_output
    import capo_codedeploy.types.batch_get_deployment_instances_input
    import capo_codedeploy.types.batch_get_deployment_instances_output
    import capo_codedeploy.types.batch_get_deployment_targets_input
    import capo_codedeploy.types.batch_get_deployment_targets_output
    import capo_codedeploy.types.batch_get_deployments_input
    import capo_codedeploy.types.batch_get_deployments_output
    import capo_codedeploy.types.batch_get_on_premises_instances_input
    import capo_codedeploy.types.batch_get_on_premises_instances_output
    import capo_codedeploy.types.blue_green_deployment_configuration
    import capo_codedeploy.types.boolean
    import capo_codedeploy.types.compute_platform
    import capo_codedeploy.types.continue_deployment_input
    import capo_codedeploy.types.create_application_input
    import capo_codedeploy.types.create_application_output
    import capo_codedeploy.types.create_deployment_config_input
    import capo_codedeploy.types.create_deployment_config_output
    import capo_codedeploy.types.create_deployment_group_input
    import capo_codedeploy.types.create_deployment_group_output
    import capo_codedeploy.types.create_deployment_input
    import capo_codedeploy.types.create_deployment_output
    import capo_codedeploy.types.delete_application_input
    import capo_codedeploy.types.delete_deployment_config_input
    import capo_codedeploy.types.delete_deployment_group_input
    import capo_codedeploy.types.delete_deployment_group_output
    import capo_codedeploy.types.delete_git_hub_account_token_input
    import capo_codedeploy.types.delete_git_hub_account_token_output
    import capo_codedeploy.types.delete_resources_by_external_id_input
    import capo_codedeploy.types.delete_resources_by_external_id_output
    import capo_codedeploy.types.deployment_config_name
    import capo_codedeploy.types.deployment_group_name
    import capo_codedeploy.types.deployment_groups_list
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.deployment_mode
    import capo_codedeploy.types.deployment_status_list
    import capo_codedeploy.types.deployment_style
    import capo_codedeploy.types.deployment_wait_type
    import capo_codedeploy.types.deployments_list
    import capo_codedeploy.types.deregister_on_premises_instance_input
    import capo_codedeploy.types.description
    import capo_codedeploy.types.ec2_tag_filter_list
    import capo_codedeploy.types.ec2_tag_set
    import capo_codedeploy.types.ecs_service_list
    import capo_codedeploy.types.external_id
    import capo_codedeploy.types.file_exists_behavior
    import capo_codedeploy.types.get_application_input
    import capo_codedeploy.types.get_application_output
    import capo_codedeploy.types.get_application_revision_input
    import capo_codedeploy.types.get_application_revision_output
    import capo_codedeploy.types.get_deployment_config_input
    import capo_codedeploy.types.get_deployment_config_output
    import capo_codedeploy.types.get_deployment_group_input
    import capo_codedeploy.types.get_deployment_group_output
    import capo_codedeploy.types.get_deployment_input
    import capo_codedeploy.types.get_deployment_instance_input
    import capo_codedeploy.types.get_deployment_instance_output
    import capo_codedeploy.types.get_deployment_output
    import capo_codedeploy.types.get_deployment_target_input
    import capo_codedeploy.types.get_deployment_target_output
    import capo_codedeploy.types.get_on_premises_instance_input
    import capo_codedeploy.types.get_on_premises_instance_output
    import capo_codedeploy.types.git_hub_account_token_name
    import capo_codedeploy.types.iam_session_arn
    import capo_codedeploy.types.iam_user_arn
    import capo_codedeploy.types.instance_id
    import capo_codedeploy.types.instance_name
    import capo_codedeploy.types.instance_name_list
    import capo_codedeploy.types.instance_status_list
    import capo_codedeploy.types.instance_type_list
    import capo_codedeploy.types.instances_list
    import capo_codedeploy.types.lifecycle_event_hook_execution_id
    import capo_codedeploy.types.lifecycle_event_status
    import capo_codedeploy.types.list_application_revisions_input
    import capo_codedeploy.types.list_application_revisions_output
    import capo_codedeploy.types.list_applications_input
    import capo_codedeploy.types.list_applications_output
    import capo_codedeploy.types.list_deployment_configs_input
    import capo_codedeploy.types.list_deployment_configs_output
    import capo_codedeploy.types.list_deployment_groups_input
    import capo_codedeploy.types.list_deployment_groups_output
    import capo_codedeploy.types.list_deployment_instances_input
    import capo_codedeploy.types.list_deployment_instances_output
    import capo_codedeploy.types.list_deployment_targets_input
    import capo_codedeploy.types.list_deployment_targets_output
    import capo_codedeploy.types.list_deployments_input
    import capo_codedeploy.types.list_deployments_output
    import capo_codedeploy.types.list_git_hub_account_token_names_input
    import capo_codedeploy.types.list_git_hub_account_token_names_output
    import capo_codedeploy.types.list_on_premises_instances_input
    import capo_codedeploy.types.list_on_premises_instances_output
    import capo_codedeploy.types.list_state_filter_action
    import capo_codedeploy.types.list_tags_for_resource_input
    import capo_codedeploy.types.list_tags_for_resource_output
    import capo_codedeploy.types.load_balancer_info
    import capo_codedeploy.types.minimum_healthy_hosts
    import capo_codedeploy.types.next_token
    import capo_codedeploy.types.nullable_boolean
    import capo_codedeploy.types.on_premises_tag_set
    import capo_codedeploy.types.outdated_instances_strategy
    import capo_codedeploy.types.put_lifecycle_event_hook_execution_status_input
    import capo_codedeploy.types.put_lifecycle_event_hook_execution_status_output
    import capo_codedeploy.types.register_application_revision_input
    import capo_codedeploy.types.register_on_premises_instance_input
    import capo_codedeploy.types.registration_status
    import capo_codedeploy.types.remove_tags_from_on_premises_instances_input
    import capo_codedeploy.types.revision_location
    import capo_codedeploy.types.revision_location_list
    import capo_codedeploy.types.role
    import capo_codedeploy.types.s3_bucket
    import capo_codedeploy.types.s3_key
    import capo_codedeploy.types.skip_wait_time_for_instance_termination_input
    import capo_codedeploy.types.sort_order
    import capo_codedeploy.types.stop_deployment_input
    import capo_codedeploy.types.stop_deployment_output
    import capo_codedeploy.types.tag_filter_list
    import capo_codedeploy.types.tag_key_list
    import capo_codedeploy.types.tag_list
    import capo_codedeploy.types.tag_resource_input
    import capo_codedeploy.types.tag_resource_output
    import capo_codedeploy.types.target_filters
    import capo_codedeploy.types.target_id
    import capo_codedeploy.types.target_id_list
    import capo_codedeploy.types.target_instances
    import capo_codedeploy.types.time_range
    import capo_codedeploy.types.traffic_routing_config
    import capo_codedeploy.types.trigger_config_list
    import capo_codedeploy.types.untag_resource_input
    import capo_codedeploy.types.untag_resource_output
    import capo_codedeploy.types.update_application_input
    import capo_codedeploy.types.update_deployment_group_input
    import capo_codedeploy.types.update_deployment_group_output
    import capo_codedeploy.types.zonal_config


class CodeDeployClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class CodeDeployClient:
    """A client for the ``CodeDeploy`` service.

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
        self._config = CodeDeployClientConfig(
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
        self, config_overrides: Optional[CodeDeployClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CodeDeployClientConfig = config_overrides or {}
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

    def add_tags_to_on_premises_instances(
        self,
        tags: "capo_codedeploy.types.tag_list.TagList",
        instance_names: "capo_codedeploy.types.instance_name_list.InstanceNameList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> None:
        """<p>Adds tags to on-premises instances.</p>

        Args:
            tags: <p>The tag key-value pairs to add to the on-premises instances.</p> <p>Keys and values are both required. Keys cannot be null or empty strings. Value-only tags are not allowed.</p>
            instance_names: <p>The names of the on-premises instances to which to add tags.</p>

        Raises:
            capo_codedeploy.errors.instance_limit_exceeded_exception.InstanceLimitExceededException: <p>The maximum number of allowed on-premises instances in a single call was exceeded.</p>
            capo_codedeploy.errors.instance_name_required_exception.InstanceNameRequiredException: <p>An on-premises instance name was not specified.</p>
            capo_codedeploy.errors.instance_not_registered_exception.InstanceNotRegisteredException: <p>The specified on-premises instance is not registered.</p>
            capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException: <p>The on-premises instance name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_tag_exception.InvalidTagException: <p>The tag was specified in an invalid format.</p>
            capo_codedeploy.errors.tag_limit_exceeded_exception.TagLimitExceededException: <p>The maximum allowed number of tags was exceeded.</p>
            capo_codedeploy.errors.tag_required_exception.TagRequiredException: <p>A tag was not specified.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.add_tags_to_on_premises_instances_input.AddTagsToOnPremisesInstancesInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.add_tags_to_on_premises_instances

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.add_tags_to_on_premises_instances.add_tags_to_on_premises_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.add_tags_to_on_premises_instances_input.AddTagsToOnPremisesInstancesInput = {
            "tags": tags,
            "instance_names": instance_names,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_application_revisions(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        revisions: "capo_codedeploy.types.revision_location_list.RevisionLocationList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.batch_get_application_revisions_output.BatchGetApplicationRevisionsOutput":
        """<p>Gets information about one or more application revisions. The maximum number of application revisions that can be returned is 25.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application about which to get revision information.</p>
            revisions: <p>An array of <code>RevisionLocation</code> objects that specify information to get about the application revisions, including type and location. The maximum number of <code>RevisionLocation</code> objects you can specify is 25.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.batch_limit_exceeded_exception.BatchLimitExceededException: <p>The maximum number of names or IDs allowed for this request (100) was exceeded.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_revision_exception.InvalidRevisionException: <p>The revision was specified in an invalid format.</p>
            capo_codedeploy.errors.revision_required_exception.RevisionRequiredException: <p>The revision ID was not specified.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.batch_get_application_revisions_input.BatchGetApplicationRevisionsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.batch_get_application_revisions_output.BatchGetApplicationRevisionsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.batch_get_application_revisions

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.batch_get_application_revisions.batch_get_application_revisions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.batch_get_application_revisions_input.BatchGetApplicationRevisionsInput = {
            "application_name": application_name,
            "revisions": revisions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_applications(
        self,
        application_names: "capo_codedeploy.types.applications_list.ApplicationsList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> (
        "capo_codedeploy.types.batch_get_applications_output.BatchGetApplicationsOutput"
    ):
        """<p>Gets information about one or more applications. The maximum number of applications that can be returned is 100.</p>

        Args:
            application_names: <p>A list of application names separated by spaces. The maximum number of application names you can specify is 100.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.batch_limit_exceeded_exception.BatchLimitExceededException: <p>The maximum number of names or IDs allowed for this request (100) was exceeded.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.batch_get_applications_input.BatchGetApplicationsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.batch_get_applications_output.BatchGetApplicationsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.batch_get_applications

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.batch_get_applications.batch_get_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.batch_get_applications_input.BatchGetApplicationsInput = {
            "application_names": application_names
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_deployment_groups(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        deployment_group_names: "capo_codedeploy.types.deployment_groups_list.DeploymentGroupsList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.batch_get_deployment_groups_output.BatchGetDeploymentGroupsOutput":
        """<p>Gets information about one or more deployment groups.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the applicable user or Amazon Web Services account.</p>
            deployment_group_names: <p>The names of the deployment groups.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.batch_limit_exceeded_exception.BatchLimitExceededException: <p>The maximum number of names or IDs allowed for this request (100) was exceeded.</p>
            capo_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException: <p>The deployment configuration does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException: <p>The deployment group name was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException: <p>The deployment group name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.batch_get_deployment_groups_input.BatchGetDeploymentGroupsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.batch_get_deployment_groups_output.BatchGetDeploymentGroupsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.batch_get_deployment_groups

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.batch_get_deployment_groups.batch_get_deployment_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.batch_get_deployment_groups_input.BatchGetDeploymentGroupsInput = {
            "application_name": application_name,
            "deployment_group_names": deployment_group_names,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_deployment_instances(
        self,
        deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId",
        instance_ids: "capo_codedeploy.types.instances_list.InstancesList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.batch_get_deployment_instances_output.BatchGetDeploymentInstancesOutput":
        """<note> <p> This method works, but is deprecated. Use <code>BatchGetDeploymentTargets</code> instead. </p> </note> <p> Returns an array of one or more instances associated with a deployment. This method works with EC2/On-premises and Lambda compute platforms. The newer <code>BatchGetDeploymentTargets</code> works with all compute platforms. The maximum number of instances that can be returned is 25.</p>

        Args:
            deployment_id: <p> The unique ID of a deployment. </p>
            instance_ids: <p>The unique IDs of instances used in the deployment. The maximum number of instance IDs you can specify is 25.</p>

        Raises:
            capo_codedeploy.errors.batch_limit_exceeded_exception.BatchLimitExceededException: <p>The maximum number of names or IDs allowed for this request (100) was exceeded.</p>
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.instance_id_required_exception.InstanceIdRequiredException: <p>The instance ID was not specified.</p>
            capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException: <p>The computePlatform is invalid. The computePlatform should be <code>Lambda</code>, <code>Server</code>, or <code>ECS</code>.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException: <p>The on-premises instance name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.batch_get_deployment_instances_input.BatchGetDeploymentInstancesInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.batch_get_deployment_instances_output.BatchGetDeploymentInstancesOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.batch_get_deployment_instances

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.batch_get_deployment_instances.batch_get_deployment_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.batch_get_deployment_instances_input.BatchGetDeploymentInstancesInput = {
            "deployment_id": deployment_id,
            "instance_ids": instance_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_deployments(
        self,
        deployment_ids: "capo_codedeploy.types.deployments_list.DeploymentsList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.batch_get_deployments_output.BatchGetDeploymentsOutput":
        """<p>Gets information about one or more deployments. The maximum number of deployments that can be returned is 25.</p>

        Args:
            deployment_ids: <p> A list of deployment IDs, separated by spaces. The maximum number of deployment IDs you can specify is 25.</p>

        Raises:
            capo_codedeploy.errors.batch_limit_exceeded_exception.BatchLimitExceededException: <p>The maximum number of names or IDs allowed for this request (100) was exceeded.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.batch_get_deployments_input.BatchGetDeploymentsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.batch_get_deployments_output.BatchGetDeploymentsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.batch_get_deployments

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.batch_get_deployments.batch_get_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.batch_get_deployments_input.BatchGetDeploymentsInput = {
            "deployment_ids": deployment_ids
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_deployment_targets(
        self,
        deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId",
        target_ids: "capo_codedeploy.types.target_id_list.TargetIdList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.batch_get_deployment_targets_output.BatchGetDeploymentTargetsOutput":
        """<p> Returns an array of one or more targets associated with a deployment. This method works with all compute types and should be used instead of the deprecated <code>BatchGetDeploymentInstances</code>. The maximum number of targets that can be returned is 25.</p> <p> The type of targets returned depends on the deployment's compute platform or deployment method: </p> <ul> <li> <p> <b>EC2/On-premises</b>: Information about Amazon EC2 instance targets. </p> </li> <li> <p> <b>Lambda</b>: Information about Lambda functions targets. </p> </li> <li> <p> <b>Amazon ECS</b>: Information about Amazon ECS service targets. </p> </li> <li> <p> <b>CloudFormation</b>: Information about targets of blue/green deployments initiated by a CloudFormation stack update.</p> </li> </ul>

        Args:
            deployment_id: <p> The unique ID of a deployment. </p>
            target_ids: <p> The unique IDs of the deployment targets. The compute platform of the deployment determines the type of the targets and their formats. The maximum number of deployment target IDs you can specify is 25.</p> <ul> <li> <p> For deployments that use the EC2/On-premises compute platform, the target IDs are Amazon EC2 or on-premises instances IDs, and their target type is <code>instanceTarget</code>. </p> </li> <li> <p> For deployments that use the Lambda compute platform, the target IDs are the names of Lambda functions, and their target type is <code>instanceTarget</code>. </p> </li> <li> <p> For deployments that use the Amazon ECS compute platform, the target IDs are pairs of Amazon ECS clusters and services specified using the format <code><clustername>:<servicename></code>. Their target type is <code>ecsTarget</code>. </p> </li> <li> <p> For deployments that are deployed with CloudFormation, the target IDs are CloudFormation stack IDs. Their target type is <code>cloudFormationTarget</code>. </p> </li> </ul>

        Raises:
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.deployment_not_started_exception.DeploymentNotStartedException: <p>The specified deployment has not started.</p>
            capo_codedeploy.errors.deployment_target_does_not_exist_exception.DeploymentTargetDoesNotExistException: <p> The provided target ID does not belong to the attempted deployment. </p>
            capo_codedeploy.errors.deployment_target_id_required_exception.DeploymentTargetIdRequiredException: <p> A deployment target ID was not provided. </p>
            capo_codedeploy.errors.deployment_target_list_size_exceeded_exception.DeploymentTargetListSizeExceededException: <p> The maximum number of targets that can be associated with an Amazon ECS or Lambda deployment was exceeded. The target list of both types of deployments must have exactly one item. This exception does not apply to EC2/On-premises deployments. </p>
            capo_codedeploy.errors.instance_does_not_exist_exception.InstanceDoesNotExistException: <p>The specified instance does not exist in the deployment group.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_target_id_exception.InvalidDeploymentTargetIdException: <p> The target ID provided was not valid. </p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.batch_get_deployment_targets_input.BatchGetDeploymentTargetsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.batch_get_deployment_targets_output.BatchGetDeploymentTargetsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.batch_get_deployment_targets

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.batch_get_deployment_targets.batch_get_deployment_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.batch_get_deployment_targets_input.BatchGetDeploymentTargetsInput = {
            "deployment_id": deployment_id,
            "target_ids": target_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_on_premises_instances(
        self,
        instance_names: "capo_codedeploy.types.instance_name_list.InstanceNameList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.batch_get_on_premises_instances_output.BatchGetOnPremisesInstancesOutput":
        """<p>Gets information about one or more on-premises instances. The maximum number of on-premises instances that can be returned is 25.</p>

        Args:
            instance_names: <p>The names of the on-premises instances about which to get information. The maximum number of instance names you can specify is 25.</p>

        Raises:
            capo_codedeploy.errors.batch_limit_exceeded_exception.BatchLimitExceededException: <p>The maximum number of names or IDs allowed for this request (100) was exceeded.</p>
            capo_codedeploy.errors.instance_name_required_exception.InstanceNameRequiredException: <p>An on-premises instance name was not specified.</p>
            capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException: <p>The on-premises instance name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.batch_get_on_premises_instances_input.BatchGetOnPremisesInstancesInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.batch_get_on_premises_instances_output.BatchGetOnPremisesInstancesOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.batch_get_on_premises_instances

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.batch_get_on_premises_instances.batch_get_on_premises_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.batch_get_on_premises_instances_input.BatchGetOnPremisesInstancesInput = {
            "instance_names": instance_names
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def continue_deployment(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        deployment_id: Optional[
            "capo_codedeploy.types.deployment_id.DeploymentId"
        ] = None,
        deployment_wait_type: Optional[
            "capo_codedeploy.types.deployment_wait_type.DeploymentWaitType"
        ] = None,
    ) -> None:
        """<p>For a blue/green deployment, starts the process of rerouting traffic from instances in the original environment to instances in the replacement environment without waiting for a specified wait time to elapse. (Traffic rerouting, which is achieved by registering instances in the replacement environment with the load balancer, can start as soon as all instances have a status of Ready.) </p>

        Args:
            deployment_id: <p> The unique ID of a blue/green deployment for which you want to start rerouting traffic to the replacement environment. </p>
            deployment_wait_type: <p> The status of the deployment's waiting period. <code>READY_WAIT</code> indicates that the deployment is ready to start shifting traffic. <code>TERMINATION_WAIT</code> indicates that the traffic is shifted, but the original target is not terminated. </p>

        Raises:
            capo_codedeploy.errors.deployment_already_completed_exception.DeploymentAlreadyCompletedException: <p>The deployment is already complete.</p>
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.deployment_is_not_in_ready_state_exception.DeploymentIsNotInReadyStateException: <p>The deployment does not have a status of Ready and can't continue yet.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_status_exception.InvalidDeploymentStatusException: <p>The specified deployment status doesn't exist or cannot be determined.</p>
            capo_codedeploy.errors.invalid_deployment_wait_type_exception.InvalidDeploymentWaitTypeException: <p> The wait type is invalid. </p>
            capo_codedeploy.errors.unsupported_action_for_deployment_type_exception.UnsupportedActionForDeploymentTypeException: <p>A call was submitted that is not supported for the specified deployment type.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.continue_deployment_input.ContinueDeploymentInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.continue_deployment

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.continue_deployment.continue_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.continue_deployment_input.ContinueDeploymentInput = {}
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id
        if deployment_wait_type is not None:
            input_["deployment_wait_type"] = deployment_wait_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_application(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        compute_platform: Optional[
            "capo_codedeploy.types.compute_platform.ComputePlatform"
        ] = None,
        tags: Optional["capo_codedeploy.types.tag_list.TagList"] = None,
    ) -> "capo_codedeploy.types.create_application_output.CreateApplicationOutput":
        """<p>Creates an application.</p>

        Args:
            application_name: <p>The name of the application. This name must be unique with the applicable user or Amazon Web Services account.</p>
            compute_platform: <p> The destination platform type for the deployment (<code>Lambda</code>, <code>Server</code>, or <code>ECS</code>).</p>
            tags: <p> The metadata that you apply to CodeDeploy applications to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define. </p>

        Raises:
            capo_codedeploy.errors.application_already_exists_exception.ApplicationAlreadyExistsException: <p>An application with the specified name with the user or Amazon Web Services account already exists.</p>
            capo_codedeploy.errors.application_limit_exceeded_exception.ApplicationLimitExceededException: <p>More applications were attempted to be created than are allowed.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException: <p>The computePlatform is invalid. The computePlatform should be <code>Lambda</code>, <code>Server</code>, or <code>ECS</code>.</p>
            capo_codedeploy.errors.invalid_tags_to_add_exception.InvalidTagsToAddException: <p> The specified tags are not valid. </p>
            capo_codedeploy.errors.throttling_exception.ThrottlingException: <p>An API function was called too frequently.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.create_application_input.CreateApplicationInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.create_application_output.CreateApplicationOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.create_application

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.create_application_input.CreateApplicationInput = {
            "application_name": application_name
        }
        if compute_platform is not None:
            input_["compute_platform"] = compute_platform
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_deployment(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        deployment_group_name: Optional[
            "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
        ] = None,
        revision: Optional[
            "capo_codedeploy.types.revision_location.RevisionLocation"
        ] = None,
        deployment_config_name: Optional[
            "capo_codedeploy.types.deployment_config_name.DeploymentConfigName"
        ] = None,
        description: Optional["capo_codedeploy.types.description.Description"] = None,
        ignore_application_stop_failures: Optional[
            "capo_codedeploy.types.boolean.Boolean"
        ] = None,
        target_instances: Optional[
            "capo_codedeploy.types.target_instances.TargetInstances"
        ] = None,
        auto_rollback_configuration: Optional[
            "capo_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
        ] = None,
        update_outdated_instances_only: Optional[
            "capo_codedeploy.types.boolean.Boolean"
        ] = None,
        file_exists_behavior: Optional[
            "capo_codedeploy.types.file_exists_behavior.FileExistsBehavior"
        ] = None,
        deployment_mode: Optional[
            "capo_codedeploy.types.deployment_mode.DeploymentMode"
        ] = None,
        override_alarm_configuration: Optional[
            "capo_codedeploy.types.alarm_configuration.AlarmConfiguration"
        ] = None,
    ) -> "capo_codedeploy.types.create_deployment_output.CreateDeploymentOutput":
        """<p>Deploys an application revision through the specified deployment group.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>
            deployment_group_name: <p>The name of the deployment group.</p>
            revision: <p> The type and location of the revision to deploy. </p>
            deployment_config_name: <p>The name of a deployment configuration associated with the user or Amazon Web Services account.</p> <p>If not specified, the value configured in the deployment group is used as the default. If the deployment group does not have a deployment configuration associated with it, <code>CodeDeployDefault</code>.<code>OneAtATime</code> is used by default.</p>
            description: <p>A comment about the deployment.</p>
            ignore_application_stop_failures: <p> If true, then if an <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, or <code>AfterBlockTraffic</code> deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if <code>ApplicationStop</code> fails, the deployment continues with <code>DownloadBundle</code>. If <code>BeforeBlockTraffic</code> fails, the deployment continues with <code>BlockTraffic</code>. If <code>AfterBlockTraffic</code> fails, the deployment continues with <code>ApplicationStop</code>. </p> <p> If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted. </p> <p> During a deployment, the CodeDeploy agent runs the scripts specified for <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, and <code>AfterBlockTraffic</code> in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail. </p> <p> If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use <code>ignoreApplicationStopFailures</code> to specify that the <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, and <code>AfterBlockTraffic</code> failures should be ignored. </p>
            target_instances: <p> Information about the instances that belong to the replacement environment in a blue/green deployment. </p>
            auto_rollback_configuration: <p>Configuration information for an automatic rollback that is added when a deployment is created.</p>
            update_outdated_instances_only: <p> Indicates whether to deploy to all instances or only to instances that are not running the latest application revision. </p>
            file_exists_behavior: <p>Information about how CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.</p> <p>The <code>fileExistsBehavior</code> parameter takes any of the following values:</p> <ul> <li> <p>DISALLOW: The deployment fails. This is also the default behavior if no option is specified.</p> </li> <li> <p>OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance.</p> </li> <li> <p>RETAIN: The version of the file already on the instance is kept and used as part of the new deployment.</p> </li> </ul>
            deployment_mode: <p>The type of deployment to create. Valid values are:</p> <ul> <li> <p> <code>STANDARD</code>: Deploys the specified revision. This is the default behavior if <code>deploymentMode</code> is not specified.</p> </li> <li> <p> <code>RESTART</code>: Restarts the application on the target instances using the revision from the deployment group's last successful deployment, without downloading a new revision. <code>RESTART</code> is supported only for EC2/On-premises in-place deployments.</p> <p>When <code>deploymentMode</code> is <code>RESTART</code>, the following apply:</p> <ul> <li> <p>The call is rejected for Amazon ECS and Lambda deployments.</p> </li> <li> <p>The <code>revision</code> parameter (including its <code>s3Location</code> and <code>gitHubLocation</code>) must not be specified, and is rejected if provided. The revision is resolved by the service from the deployment group's last successful deployment.</p> </li> <li> <p>The <code>updateOutdatedInstancesOnly</code> parameter must not be set to <code>true</code>, and is rejected if provided.</p> </li> </ul> </li> </ul>
            override_alarm_configuration: <p>Allows you to specify information about alarms associated with a deployment. The alarm configuration that you specify here will override the alarm configuration at the deployment group level. Consider overriding the alarm configuration if you have set up alarms at the deployment group level that are causing deployment failures. In this case, you would call <code>CreateDeployment</code> to create a new deployment that uses a previous application revision that is known to work, and set its alarm configuration to turn off alarm polling. Turning off alarm polling ensures that the new deployment proceeds without being blocked by the alarm that was generated by the previous, failed, deployment.</p> <note> <p>If you specify an <code>overrideAlarmConfiguration</code>, you need the <code>UpdateDeploymentGroup</code> IAM permission when calling <code>CreateDeployment</code>.</p> </note>

        Raises:
            capo_codedeploy.errors.alarms_limit_exceeded_exception.AlarmsLimitExceededException: <p>The maximum number of alarms for a deployment group (10) was exceeded.</p>
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException: <p>The deployment configuration does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException: <p>The named deployment group with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException: <p>The deployment group name was not specified.</p>
            capo_codedeploy.errors.deployment_limit_exceeded_exception.DeploymentLimitExceededException: <p>The number of allowed deployments was exceeded.</p>
            capo_codedeploy.errors.description_too_long_exception.DescriptionTooLongException: <p>The description is too long.</p>
            capo_codedeploy.errors.invalid_alarm_config_exception.InvalidAlarmConfigException: <p>The format of the alarm configuration is invalid. Possible causes include:</p> <ul> <li> <p>The alarm list is null.</p> </li> <li> <p>The alarm object is null.</p> </li> <li> <p>The alarm name is empty or null or exceeds the limit of 255 characters.</p> </li> <li> <p>Two alarms with the same name have been specified.</p> </li> <li> <p>The alarm configuration is enabled, but the alarm list is empty.</p> </li> </ul>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_auto_rollback_config_exception.InvalidAutoRollbackConfigException: <p>The automatic rollback configuration was specified in an invalid format. For example, automatic rollback is enabled, but an invalid triggering event type or no event types were listed.</p>
            capo_codedeploy.errors.invalid_auto_scaling_group_exception.InvalidAutoScalingGroupException: <p>The Auto Scaling group was specified in an invalid format or does not exist.</p>
            capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException: <p>The computePlatform is invalid. The computePlatform should be <code>Lambda</code>, <code>Server</code>, or <code>ECS</code>.</p>
            capo_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException: <p>The deployment configuration name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException: <p>The deployment group name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_ecs_service_exception.InvalidECSServiceException: <p> The Amazon ECS service identifier is not valid. </p>
            capo_codedeploy.errors.invalid_file_exists_behavior_exception.InvalidFileExistsBehaviorException: <p>An invalid fileExistsBehavior option was specified to determine how CodeDeploy handles files or directories that already exist in a deployment target location, but weren't part of the previous successful deployment. Valid values include "DISALLOW," "OVERWRITE," and "RETAIN."</p>
            capo_codedeploy.errors.invalid_git_hub_account_token_exception.InvalidGitHubAccountTokenException: <p>The GitHub token is not valid.</p>
            capo_codedeploy.errors.invalid_ignore_application_stop_failures_value_exception.InvalidIgnoreApplicationStopFailuresValueException: <p>The IgnoreApplicationStopFailures value is invalid. For Lambda deployments, <code>false</code> is expected. For EC2/On-premises deployments, <code>true</code> or <code>false</code> is expected.</p>
            capo_codedeploy.errors.invalid_input_exception.InvalidInputException: <p>The input was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_load_balancer_info_exception.InvalidLoadBalancerInfoException: <p>An invalid load balancer name, or no load balancer name, was specified.</p>
            capo_codedeploy.errors.invalid_revision_exception.InvalidRevisionException: <p>The revision was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_role_exception.InvalidRoleException: <p>The service role ARN was specified in an invalid format. Or, if an Auto Scaling group was specified, the specified service role does not grant the appropriate permissions to Amazon EC2 Auto Scaling.</p>
            capo_codedeploy.errors.invalid_target_instances_exception.InvalidTargetInstancesException: <p>The target instance configuration is invalid. Possible causes include:</p> <ul> <li> <p>Configuration data for target instances was entered for an in-place deployment.</p> </li> <li> <p>The limit of 10 tags for a tag type was exceeded.</p> </li> <li> <p>The combined length of the tag names exceeded the limit. </p> </li> <li> <p>A specified tag is not currently applied to any instances.</p> </li> </ul>
            capo_codedeploy.errors.invalid_traffic_routing_configuration_exception.InvalidTrafficRoutingConfigurationException: <p> The configuration that specifies how traffic is routed during a deployment is invalid.</p>
            capo_codedeploy.errors.invalid_update_outdated_instances_only_value_exception.InvalidUpdateOutdatedInstancesOnlyValueException: <p>The UpdateOutdatedInstancesOnly value is invalid. For Lambda deployments, <code>false</code> is expected. For EC2/On-premises deployments, <code>true</code> or <code>false</code> is expected.</p>
            capo_codedeploy.errors.revision_does_not_exist_exception.RevisionDoesNotExistException: <p>The named revision does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.revision_required_exception.RevisionRequiredException: <p>The revision ID was not specified.</p>
            capo_codedeploy.errors.throttling_exception.ThrottlingException: <p>An API function was called too frequently.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.create_deployment_input.CreateDeploymentInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.create_deployment_output.CreateDeploymentOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.create_deployment

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.create_deployment.create_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.create_deployment_input.CreateDeploymentInput = {
            "application_name": application_name
        }
        if deployment_group_name is not None:
            input_["deployment_group_name"] = deployment_group_name
        if revision is not None:
            input_["revision"] = revision
        if deployment_config_name is not None:
            input_["deployment_config_name"] = deployment_config_name
        if description is not None:
            input_["description"] = description
        if ignore_application_stop_failures is not None:
            input_["ignore_application_stop_failures"] = (
                ignore_application_stop_failures
            )
        if target_instances is not None:
            input_["target_instances"] = target_instances
        if auto_rollback_configuration is not None:
            input_["auto_rollback_configuration"] = auto_rollback_configuration
        if update_outdated_instances_only is not None:
            input_["update_outdated_instances_only"] = update_outdated_instances_only
        if file_exists_behavior is not None:
            input_["file_exists_behavior"] = file_exists_behavior
        if deployment_mode is not None:
            input_["deployment_mode"] = deployment_mode
        if override_alarm_configuration is not None:
            input_["override_alarm_configuration"] = override_alarm_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_deployment_config(
        self,
        deployment_config_name: "capo_codedeploy.types.deployment_config_name.DeploymentConfigName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        minimum_healthy_hosts: Optional[
            "capo_codedeploy.types.minimum_healthy_hosts.MinimumHealthyHosts"
        ] = None,
        traffic_routing_config: Optional[
            "capo_codedeploy.types.traffic_routing_config.TrafficRoutingConfig"
        ] = None,
        compute_platform: Optional[
            "capo_codedeploy.types.compute_platform.ComputePlatform"
        ] = None,
        zonal_config: Optional["capo_codedeploy.types.zonal_config.ZonalConfig"] = None,
    ) -> "capo_codedeploy.types.create_deployment_config_output.CreateDeploymentConfigOutput":
        """<p> Creates a deployment configuration. </p>

        Args:
            deployment_config_name: <p>The name of the deployment configuration to create.</p>
            minimum_healthy_hosts: <p>The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.</p> <p>The type parameter takes either of the following values:</p> <ul> <li> <p>HOST_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value.</p> </li> <li> <p>FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the deployment, CodeDeploy converts the percentage to the equivalent number of instances and rounds up fractional instances.</p> </li> </ul> <p>The value parameter takes an integer.</p> <p>For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a value of 95.</p>
            traffic_routing_config: <p>The configuration that specifies how the deployment traffic is routed.</p>
            compute_platform: <p>The destination platform type for the deployment (<code>Lambda</code>, <code>Server</code>, or <code>ECS</code>).</p>
            zonal_config: <p>Configure the <code>ZonalConfig</code> object if you want CodeDeploy to deploy your application to one <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones">Availability Zone</a> at a time, within an Amazon Web Services Region.</p> <p>For more information about the zonal configuration feature, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config">zonal configuration</a> in the <i>CodeDeploy User Guide</i>.</p>

        Raises:
            capo_codedeploy.errors.deployment_config_already_exists_exception.DeploymentConfigAlreadyExistsException: <p>A deployment configuration with the specified name with the user or Amazon Web Services account already exists.</p>
            capo_codedeploy.errors.deployment_config_limit_exceeded_exception.DeploymentConfigLimitExceededException: <p>The deployment configurations limit was exceeded.</p>
            capo_codedeploy.errors.deployment_config_name_required_exception.DeploymentConfigNameRequiredException: <p>The deployment configuration name was not specified.</p>
            capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException: <p>The computePlatform is invalid. The computePlatform should be <code>Lambda</code>, <code>Server</code>, or <code>ECS</code>.</p>
            capo_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException: <p>The deployment configuration name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_minimum_healthy_host_value_exception.InvalidMinimumHealthyHostValueException: <p>The minimum healthy instance value was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_traffic_routing_configuration_exception.InvalidTrafficRoutingConfigurationException: <p> The configuration that specifies how traffic is routed during a deployment is invalid.</p>
            capo_codedeploy.errors.invalid_zonal_deployment_configuration_exception.InvalidZonalDeploymentConfigurationException: <p>The <code>ZonalConfig</code> object is not valid.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.create_deployment_config_input.CreateDeploymentConfigInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.create_deployment_config_output.CreateDeploymentConfigOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.create_deployment_config

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.create_deployment_config.create_deployment_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.create_deployment_config_input.CreateDeploymentConfigInput = {
            "deployment_config_name": deployment_config_name
        }
        if minimum_healthy_hosts is not None:
            input_["minimum_healthy_hosts"] = minimum_healthy_hosts
        if traffic_routing_config is not None:
            input_["traffic_routing_config"] = traffic_routing_config
        if compute_platform is not None:
            input_["compute_platform"] = compute_platform
        if zonal_config is not None:
            input_["zonal_config"] = zonal_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_deployment_group(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        deployment_group_name: "capo_codedeploy.types.deployment_group_name.DeploymentGroupName",
        service_role_arn: "capo_codedeploy.types.role.Role",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        deployment_config_name: Optional[
            "capo_codedeploy.types.deployment_config_name.DeploymentConfigName"
        ] = None,
        ec2_tag_filters: Optional[
            "capo_codedeploy.types.ec2_tag_filter_list.EC2TagFilterList"
        ] = None,
        on_premises_instance_tag_filters: Optional[
            "capo_codedeploy.types.tag_filter_list.TagFilterList"
        ] = None,
        auto_scaling_groups: Optional[
            "capo_codedeploy.types.auto_scaling_group_name_list.AutoScalingGroupNameList"
        ] = None,
        trigger_configurations: Optional[
            "capo_codedeploy.types.trigger_config_list.TriggerConfigList"
        ] = None,
        alarm_configuration: Optional[
            "capo_codedeploy.types.alarm_configuration.AlarmConfiguration"
        ] = None,
        auto_rollback_configuration: Optional[
            "capo_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
        ] = None,
        outdated_instances_strategy: Optional[
            "capo_codedeploy.types.outdated_instances_strategy.OutdatedInstancesStrategy"
        ] = None,
        deployment_style: Optional[
            "capo_codedeploy.types.deployment_style.DeploymentStyle"
        ] = None,
        blue_green_deployment_configuration: Optional[
            "capo_codedeploy.types.blue_green_deployment_configuration.BlueGreenDeploymentConfiguration"
        ] = None,
        load_balancer_info: Optional[
            "capo_codedeploy.types.load_balancer_info.LoadBalancerInfo"
        ] = None,
        ec2_tag_set: Optional["capo_codedeploy.types.ec2_tag_set.EC2TagSet"] = None,
        ecs_services: Optional[
            "capo_codedeploy.types.ecs_service_list.ECSServiceList"
        ] = None,
        on_premises_tag_set: Optional[
            "capo_codedeploy.types.on_premises_tag_set.OnPremisesTagSet"
        ] = None,
        tags: Optional["capo_codedeploy.types.tag_list.TagList"] = None,
        termination_hook_enabled: Optional[
            "capo_codedeploy.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput":
        """<p>Creates a deployment group to which application revisions are deployed.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>
            deployment_group_name: <p>The name of a new deployment group for the specified application.</p>
            deployment_config_name: <p>If specified, the deployment configuration name can be either one of the predefined configurations provided with CodeDeploy or a custom deployment configuration that you create by calling the create deployment configuration operation.</p> <p> <code>CodeDeployDefault.OneAtATime</code> is the default deployment configuration. It is used if a configuration isn't specified for the deployment or deployment group.</p> <p>For more information about the predefined deployment configurations in CodeDeploy, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html">Working with Deployment Configurations in CodeDeploy</a> in the <i>CodeDeploy User Guide</i>.</p>
            ec2_tag_filters: <p>The Amazon EC2 tags on which to filter. The deployment group includes Amazon EC2 instances with any of the specified tags. Cannot be used in the same call as ec2TagSet.</p>
            on_premises_instance_tag_filters: <p>The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags. Cannot be used in the same call as <code>OnPremisesTagSet</code>.</p>
            auto_scaling_groups: <p>A list of associated Amazon EC2 Auto Scaling groups.</p>
            service_role_arn: <p>A service role Amazon Resource Name (ARN) that allows CodeDeploy to act on the user's behalf when interacting with Amazon Web Services services.</p>
            trigger_configurations: <p>Information about triggers to create when the deployment group is created. For examples, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-sns.html">Create a Trigger for an CodeDeploy Event</a> in the <i>CodeDeploy User Guide</i>.</p>
            alarm_configuration: <p>Information to add about Amazon CloudWatch alarms when the deployment group is created.</p>
            auto_rollback_configuration: <p>Configuration information for an automatic rollback that is added when a deployment group is created.</p>
            outdated_instances_strategy: <p>Indicates what happens when new Amazon EC2 instances are launched mid-deployment and do not receive the deployed application revision.</p> <p>If this option is set to <code>UPDATE</code> or is unspecified, CodeDeploy initiates one or more 'auto-update outdated instances' deployments to apply the deployed application revision to the new Amazon EC2 instances.</p> <p>If this option is set to <code>IGNORE</code>, CodeDeploy does not initiate a deployment to update the new Amazon EC2 instances. This may result in instances having different revisions.</p>
            deployment_style: <p>Information about the type of deployment, in-place or blue/green, that you want to run and whether to route deployment traffic behind a load balancer.</p>
            blue_green_deployment_configuration: <p>Information about blue/green deployment options for a deployment group.</p>
            load_balancer_info: <p>Information about the load balancer used in a deployment.</p>
            ec2_tag_set: <p>Information about groups of tags applied to Amazon EC2 instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups. Cannot be used in the same call as <code>ec2TagFilters</code>.</p>
            ecs_services: <p> The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <code><clustername>:<servicename></code>. </p>
            on_premises_tag_set: <p>Information about groups of tags applied to on-premises instances. The deployment group includes only on-premises instances identified by all of the tag groups. Cannot be used in the same call as <code>onPremisesInstanceTagFilters</code>.</p>
            tags: <p> The metadata that you apply to CodeDeploy deployment groups to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define. </p>
            termination_hook_enabled: <p>This parameter only applies if you are using CodeDeploy with Amazon EC2 Auto Scaling. For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html">Integrating CodeDeploy with Amazon EC2 Auto Scaling</a> in the <i>CodeDeploy User Guide</i>.</p> <p>Set <code>terminationHookEnabled</code> to <code>true</code> to have CodeDeploy install a termination hook into your Auto Scaling group when you create a deployment group. When this hook is installed, CodeDeploy will perform termination deployments.</p> <p>For information about termination deployments, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable">Enabling termination deployments during Auto Scaling scale-in events</a> in the <i>CodeDeploy User Guide</i>.</p> <p>For more information about Auto Scaling scale-in events, see the <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html#as-lifecycle-scale-in">Scale in</a> topic in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Raises:
            capo_codedeploy.errors.alarms_limit_exceeded_exception.AlarmsLimitExceededException: <p>The maximum number of alarms for a deployment group (10) was exceeded.</p>
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException: <p>The deployment configuration does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_group_already_exists_exception.DeploymentGroupAlreadyExistsException: <p>A deployment group with the specified name with the user or Amazon Web Services account already exists.</p>
            capo_codedeploy.errors.deployment_group_limit_exceeded_exception.DeploymentGroupLimitExceededException: <p> The deployment groups limit was exceeded.</p>
            capo_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException: <p>The deployment group name was not specified.</p>
            capo_codedeploy.errors.ecs_service_mapping_limit_exceeded_exception.ECSServiceMappingLimitExceededException: <p> The Amazon ECS service is associated with more than one deployment groups. An Amazon ECS service can be associated with only one deployment group. </p>
            capo_codedeploy.errors.invalid_alarm_config_exception.InvalidAlarmConfigException: <p>The format of the alarm configuration is invalid. Possible causes include:</p> <ul> <li> <p>The alarm list is null.</p> </li> <li> <p>The alarm object is null.</p> </li> <li> <p>The alarm name is empty or null or exceeds the limit of 255 characters.</p> </li> <li> <p>Two alarms with the same name have been specified.</p> </li> <li> <p>The alarm configuration is enabled, but the alarm list is empty.</p> </li> </ul>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_auto_rollback_config_exception.InvalidAutoRollbackConfigException: <p>The automatic rollback configuration was specified in an invalid format. For example, automatic rollback is enabled, but an invalid triggering event type or no event types were listed.</p>
            capo_codedeploy.errors.invalid_auto_scaling_group_exception.InvalidAutoScalingGroupException: <p>The Auto Scaling group was specified in an invalid format or does not exist.</p>
            capo_codedeploy.errors.invalid_blue_green_deployment_configuration_exception.InvalidBlueGreenDeploymentConfigurationException: <p>The configuration for the blue/green deployment group was provided in an invalid format. For information about deployment configuration format, see <a>CreateDeploymentConfig</a>.</p>
            capo_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException: <p>The deployment configuration name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException: <p>The deployment group name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_style_exception.InvalidDeploymentStyleException: <p>An invalid deployment style was specified. Valid deployment types include "IN_PLACE" and "BLUE_GREEN." Valid deployment options include "WITH_TRAFFIC_CONTROL" and "WITHOUT_TRAFFIC_CONTROL."</p>
            capo_codedeploy.errors.invalid_ec2_tag_combination_exception.InvalidEC2TagCombinationException: <p>A call was submitted that specified both Ec2TagFilters and Ec2TagSet, but only one of these data types can be used in a single call.</p>
            capo_codedeploy.errors.invalid_ec2_tag_exception.InvalidEC2TagException: <p>The tag was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_ecs_service_exception.InvalidECSServiceException: <p> The Amazon ECS service identifier is not valid. </p>
            capo_codedeploy.errors.invalid_input_exception.InvalidInputException: <p>The input was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_load_balancer_info_exception.InvalidLoadBalancerInfoException: <p>An invalid load balancer name, or no load balancer name, was specified.</p>
            capo_codedeploy.errors.invalid_on_premises_tag_combination_exception.InvalidOnPremisesTagCombinationException: <p>A call was submitted that specified both OnPremisesTagFilters and OnPremisesTagSet, but only one of these data types can be used in a single call.</p>
            capo_codedeploy.errors.invalid_role_exception.InvalidRoleException: <p>The service role ARN was specified in an invalid format. Or, if an Auto Scaling group was specified, the specified service role does not grant the appropriate permissions to Amazon EC2 Auto Scaling.</p>
            capo_codedeploy.errors.invalid_tag_exception.InvalidTagException: <p>The tag was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_tags_to_add_exception.InvalidTagsToAddException: <p> The specified tags are not valid. </p>
            capo_codedeploy.errors.invalid_target_group_pair_exception.InvalidTargetGroupPairException: <p> A target group pair associated with this deployment is not valid. </p>
            capo_codedeploy.errors.invalid_traffic_routing_configuration_exception.InvalidTrafficRoutingConfigurationException: <p> The configuration that specifies how traffic is routed during a deployment is invalid.</p>
            capo_codedeploy.errors.invalid_trigger_config_exception.InvalidTriggerConfigException: <p>The trigger was specified in an invalid format.</p>
            capo_codedeploy.errors.lifecycle_hook_limit_exceeded_exception.LifecycleHookLimitExceededException: <p>The limit for lifecycle hooks was exceeded.</p>
            capo_codedeploy.errors.role_required_exception.RoleRequiredException: <p>The role ID was not specified.</p>
            capo_codedeploy.errors.tag_set_list_limit_exceeded_exception.TagSetListLimitExceededException: <p>The number of tag groups included in the tag set list exceeded the maximum allowed limit of 3.</p>
            capo_codedeploy.errors.throttling_exception.ThrottlingException: <p>An API function was called too frequently.</p>
            capo_codedeploy.errors.trigger_targets_limit_exceeded_exception.TriggerTargetsLimitExceededException: <p>The maximum allowed number of triggers was exceeded.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.create_deployment_group_input.CreateDeploymentGroupInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.create_deployment_group

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.create_deployment_group.create_deployment_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.create_deployment_group_input.CreateDeploymentGroupInput = {
            "application_name": application_name,
            "deployment_group_name": deployment_group_name,
            "service_role_arn": service_role_arn,
        }
        if deployment_config_name is not None:
            input_["deployment_config_name"] = deployment_config_name
        if ec2_tag_filters is not None:
            input_["ec2_tag_filters"] = ec2_tag_filters
        if on_premises_instance_tag_filters is not None:
            input_["on_premises_instance_tag_filters"] = (
                on_premises_instance_tag_filters
            )
        if auto_scaling_groups is not None:
            input_["auto_scaling_groups"] = auto_scaling_groups
        if trigger_configurations is not None:
            input_["trigger_configurations"] = trigger_configurations
        if alarm_configuration is not None:
            input_["alarm_configuration"] = alarm_configuration
        if auto_rollback_configuration is not None:
            input_["auto_rollback_configuration"] = auto_rollback_configuration
        if outdated_instances_strategy is not None:
            input_["outdated_instances_strategy"] = outdated_instances_strategy
        if deployment_style is not None:
            input_["deployment_style"] = deployment_style
        if blue_green_deployment_configuration is not None:
            input_["blue_green_deployment_configuration"] = (
                blue_green_deployment_configuration
            )
        if load_balancer_info is not None:
            input_["load_balancer_info"] = load_balancer_info
        if ec2_tag_set is not None:
            input_["ec2_tag_set"] = ec2_tag_set
        if ecs_services is not None:
            input_["ecs_services"] = ecs_services
        if on_premises_tag_set is not None:
            input_["on_premises_tag_set"] = on_premises_tag_set
        if tags is not None:
            input_["tags"] = tags
        if termination_hook_enabled is not None:
            input_["termination_hook_enabled"] = termination_hook_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> None:
        """<p>Deletes an application.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>

        Raises:
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_role_exception.InvalidRoleException: <p>The service role ARN was specified in an invalid format. Or, if an Auto Scaling group was specified, the specified service role does not grant the appropriate permissions to Amazon EC2 Auto Scaling.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.delete_application_input.DeleteApplicationInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.delete_application

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.delete_application_input.DeleteApplicationInput = {
            "application_name": application_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_deployment_config(
        self,
        deployment_config_name: "capo_codedeploy.types.deployment_config_name.DeploymentConfigName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> None:
        """<p>Deletes a deployment configuration.</p> <note> <p>A deployment configuration cannot be deleted if it is currently in use. Predefined configurations cannot be deleted.</p> </note>

        Args:
            deployment_config_name: <p>The name of a deployment configuration associated with the user or Amazon Web Services account.</p>

        Raises:
            capo_codedeploy.errors.deployment_config_in_use_exception.DeploymentConfigInUseException: <p>The deployment configuration is still in use.</p>
            capo_codedeploy.errors.deployment_config_name_required_exception.DeploymentConfigNameRequiredException: <p>The deployment configuration name was not specified.</p>
            capo_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException: <p>The deployment configuration name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_operation_exception.InvalidOperationException: <p>An invalid operation was detected.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.delete_deployment_config_input.DeleteDeploymentConfigInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.delete_deployment_config

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.delete_deployment_config.delete_deployment_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.delete_deployment_config_input.DeleteDeploymentConfigInput = {
            "deployment_config_name": deployment_config_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_deployment_group(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        deployment_group_name: "capo_codedeploy.types.deployment_group_name.DeploymentGroupName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.delete_deployment_group_output.DeleteDeploymentGroupOutput":
        """<p>Deletes a deployment group.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>
            deployment_group_name: <p>The name of a deployment group for the specified application.</p>

        Raises:
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException: <p>The deployment group name was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException: <p>The deployment group name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_role_exception.InvalidRoleException: <p>The service role ARN was specified in an invalid format. Or, if an Auto Scaling group was specified, the specified service role does not grant the appropriate permissions to Amazon EC2 Auto Scaling.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.delete_deployment_group_input.DeleteDeploymentGroupInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.delete_deployment_group_output.DeleteDeploymentGroupOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.delete_deployment_group

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.delete_deployment_group.delete_deployment_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.delete_deployment_group_input.DeleteDeploymentGroupInput = {
            "application_name": application_name,
            "deployment_group_name": deployment_group_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_git_hub_account_token(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        token_name: Optional[
            "capo_codedeploy.types.git_hub_account_token_name.GitHubAccountTokenName"
        ] = None,
    ) -> "capo_codedeploy.types.delete_git_hub_account_token_output.DeleteGitHubAccountTokenOutput":
        """<p>Deletes a GitHub account connection.</p>

        Args:
            token_name: <p>The name of the GitHub account connection to delete.</p>

        Raises:
            capo_codedeploy.errors.git_hub_account_token_does_not_exist_exception.GitHubAccountTokenDoesNotExistException: <p>No GitHub account connection exists with the named specified in the call.</p>
            capo_codedeploy.errors.git_hub_account_token_name_required_exception.GitHubAccountTokenNameRequiredException: <p>The call is missing a required GitHub account connection name.</p>
            capo_codedeploy.errors.invalid_git_hub_account_token_name_exception.InvalidGitHubAccountTokenNameException: <p>The format of the specified GitHub account connection name is invalid.</p>
            capo_codedeploy.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The API used does not support the deployment.</p>
            capo_codedeploy.errors.resource_validation_exception.ResourceValidationException: <p>The specified resource could not be validated.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.delete_git_hub_account_token_input.DeleteGitHubAccountTokenInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.delete_git_hub_account_token_output.DeleteGitHubAccountTokenOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.delete_git_hub_account_token

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.delete_git_hub_account_token.delete_git_hub_account_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.delete_git_hub_account_token_input.DeleteGitHubAccountTokenInput = {}
        if token_name is not None:
            input_["token_name"] = token_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resources_by_external_id(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        external_id: Optional["capo_codedeploy.types.external_id.ExternalId"] = None,
    ) -> "capo_codedeploy.types.delete_resources_by_external_id_output.DeleteResourcesByExternalIdOutput":
        """<p>Deletes resources linked to an external ID. This action only applies if you have configured blue/green deployments through CloudFormation. </p> <note> <p>It is not necessary to call this action directly. CloudFormation calls it on your behalf when it needs to delete stack resources. This action is offered publicly in case you need to delete resources to comply with General Data Protection Regulation (GDPR) requirements.</p> </note>

        Args:
            external_id: <p>The unique ID of an external resource (for example, a CloudFormation stack ID) that is linked to one or more CodeDeploy resources.</p>

        Raises:
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.delete_resources_by_external_id_input.DeleteResourcesByExternalIdInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.delete_resources_by_external_id_output.DeleteResourcesByExternalIdOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.delete_resources_by_external_id

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.delete_resources_by_external_id.delete_resources_by_external_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.delete_resources_by_external_id_input.DeleteResourcesByExternalIdInput = {}
        if external_id is not None:
            input_["external_id"] = external_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_on_premises_instance(
        self,
        instance_name: "capo_codedeploy.types.instance_name.InstanceName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> None:
        """<p>Deregisters an on-premises instance.</p>

        Args:
            instance_name: <p>The name of the on-premises instance to deregister.</p>

        Raises:
            capo_codedeploy.errors.instance_name_required_exception.InstanceNameRequiredException: <p>An on-premises instance name was not specified.</p>
            capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException: <p>The on-premises instance name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.deregister_on_premises_instance_input.DeregisterOnPremisesInstanceInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.deregister_on_premises_instance

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.deregister_on_premises_instance.deregister_on_premises_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.deregister_on_premises_instance_input.DeregisterOnPremisesInstanceInput = {
            "instance_name": instance_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.get_application_output.GetApplicationOutput":
        """<p>Gets information about an application.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.get_application_input.GetApplicationInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.get_application_output.GetApplicationOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.get_application

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.get_application_input.GetApplicationInput = {
            "application_name": application_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application_revision(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        revision: "capo_codedeploy.types.revision_location.RevisionLocation",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.get_application_revision_output.GetApplicationRevisionOutput":
        """<p>Gets information about an application revision.</p>

        Args:
            application_name: <p>The name of the application that corresponds to the revision.</p>
            revision: <p>Information about the application revision to get, including type and location.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_revision_exception.InvalidRevisionException: <p>The revision was specified in an invalid format.</p>
            capo_codedeploy.errors.revision_does_not_exist_exception.RevisionDoesNotExistException: <p>The named revision does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.revision_required_exception.RevisionRequiredException: <p>The revision ID was not specified.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.get_application_revision_input.GetApplicationRevisionInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.get_application_revision_output.GetApplicationRevisionOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.get_application_revision

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.get_application_revision.get_application_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.get_application_revision_input.GetApplicationRevisionInput = {
            "application_name": application_name,
            "revision": revision,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment(
        self,
        deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.get_deployment_output.GetDeploymentOutput":
        """<p>Gets information about a deployment.</p> <note> <p> The <code>content</code> property of the <code>appSpecContent</code> object in the returned revision is always null. Use <code>GetApplicationRevision</code> and the <code>sha256</code> property of the returned <code>appSpecContent</code> object to get the content of the deployment’s AppSpec file. </p> </note>

        Args:
            deployment_id: <p> The unique ID of a deployment associated with the user or Amazon Web Services account. </p>

        Raises:
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.get_deployment_input.GetDeploymentInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.get_deployment

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.get_deployment_input.GetDeploymentInput = {
            "deployment_id": deployment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment_config(
        self,
        deployment_config_name: "capo_codedeploy.types.deployment_config_name.DeploymentConfigName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.get_deployment_config_output.GetDeploymentConfigOutput":
        """<p>Gets information about a deployment configuration.</p>

        Args:
            deployment_config_name: <p>The name of a deployment configuration associated with the user or Amazon Web Services account.</p>

        Raises:
            capo_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException: <p>The deployment configuration does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_config_name_required_exception.DeploymentConfigNameRequiredException: <p>The deployment configuration name was not specified.</p>
            capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException: <p>The computePlatform is invalid. The computePlatform should be <code>Lambda</code>, <code>Server</code>, or <code>ECS</code>.</p>
            capo_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException: <p>The deployment configuration name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.get_deployment_config_input.GetDeploymentConfigInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.get_deployment_config_output.GetDeploymentConfigOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.get_deployment_config

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.get_deployment_config.get_deployment_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.get_deployment_config_input.GetDeploymentConfigInput = {
            "deployment_config_name": deployment_config_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment_group(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        deployment_group_name: "capo_codedeploy.types.deployment_group_name.DeploymentGroupName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.get_deployment_group_output.GetDeploymentGroupOutput":
        """<p>Gets information about a deployment group.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>
            deployment_group_name: <p>The name of a deployment group for the specified application.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException: <p>The deployment configuration does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException: <p>The named deployment group with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException: <p>The deployment group name was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException: <p>The deployment group name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.get_deployment_group_input.GetDeploymentGroupInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.get_deployment_group_output.GetDeploymentGroupOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.get_deployment_group

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.get_deployment_group.get_deployment_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.get_deployment_group_input.GetDeploymentGroupInput = {
            "application_name": application_name,
            "deployment_group_name": deployment_group_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment_instance(
        self,
        deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId",
        instance_id: "capo_codedeploy.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.get_deployment_instance_output.GetDeploymentInstanceOutput":
        """<p>Gets information about an instance as part of a deployment.</p>

        Args:
            deployment_id: <p> The unique ID of a deployment. </p>
            instance_id: <p> The unique ID of an instance in the deployment group. </p>

        Raises:
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.instance_does_not_exist_exception.InstanceDoesNotExistException: <p>The specified instance does not exist in the deployment group.</p>
            capo_codedeploy.errors.instance_id_required_exception.InstanceIdRequiredException: <p>The instance ID was not specified.</p>
            capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException: <p>The computePlatform is invalid. The computePlatform should be <code>Lambda</code>, <code>Server</code>, or <code>ECS</code>.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException: <p>The on-premises instance name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.get_deployment_instance_input.GetDeploymentInstanceInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.get_deployment_instance_output.GetDeploymentInstanceOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.get_deployment_instance

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.get_deployment_instance.get_deployment_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.get_deployment_instance_input.GetDeploymentInstanceInput = {
            "deployment_id": deployment_id,
            "instance_id": instance_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment_target(
        self,
        deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId",
        target_id: "capo_codedeploy.types.target_id.TargetId",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.get_deployment_target_output.GetDeploymentTargetOutput":
        """<p> Returns information about a deployment target. </p>

        Args:
            deployment_id: <p> The unique ID of a deployment. </p>
            target_id: <p> The unique ID of a deployment target. </p>

        Raises:
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.deployment_not_started_exception.DeploymentNotStartedException: <p>The specified deployment has not started.</p>
            capo_codedeploy.errors.deployment_target_does_not_exist_exception.DeploymentTargetDoesNotExistException: <p> The provided target ID does not belong to the attempted deployment. </p>
            capo_codedeploy.errors.deployment_target_id_required_exception.DeploymentTargetIdRequiredException: <p> A deployment target ID was not provided. </p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_target_id_exception.InvalidDeploymentTargetIdException: <p> The target ID provided was not valid. </p>
            capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException: <p>The on-premises instance name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.get_deployment_target_input.GetDeploymentTargetInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.get_deployment_target_output.GetDeploymentTargetOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.get_deployment_target

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.get_deployment_target.get_deployment_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.get_deployment_target_input.GetDeploymentTargetInput = {
            "deployment_id": deployment_id,
            "target_id": target_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_on_premises_instance(
        self,
        instance_name: "capo_codedeploy.types.instance_name.InstanceName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.get_on_premises_instance_output.GetOnPremisesInstanceOutput":
        """<p> Gets information about an on-premises instance. </p>

        Args:
            instance_name: <p> The name of the on-premises instance about which to get information. </p>

        Raises:
            capo_codedeploy.errors.instance_name_required_exception.InstanceNameRequiredException: <p>An on-premises instance name was not specified.</p>
            capo_codedeploy.errors.instance_not_registered_exception.InstanceNotRegisteredException: <p>The specified on-premises instance is not registered.</p>
            capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException: <p>The on-premises instance name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.get_on_premises_instance_input.GetOnPremisesInstanceInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.get_on_premises_instance_output.GetOnPremisesInstanceOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.get_on_premises_instance

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.get_on_premises_instance.get_on_premises_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.get_on_premises_instance_input.GetOnPremisesInstanceInput = {
            "instance_name": instance_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_application_revisions(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        sort_by: Optional[
            "capo_codedeploy.types.application_revision_sort_by.ApplicationRevisionSortBy"
        ] = None,
        sort_order: Optional["capo_codedeploy.types.sort_order.SortOrder"] = None,
        s3_bucket: Optional["capo_codedeploy.types.s3_bucket.S3Bucket"] = None,
        s3_key_prefix: Optional["capo_codedeploy.types.s3_key.S3Key"] = None,
        deployed: Optional[
            "capo_codedeploy.types.list_state_filter_action.ListStateFilterAction"
        ] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "capo_codedeploy.types.list_application_revisions_output.ListApplicationRevisionsOutput":
        """<p>Lists information about revisions for an application.</p>

        Args:
            application_name: <p> The name of an CodeDeploy application associated with the user or Amazon Web Services account. </p>
            sort_by: <p>The column name to use to sort the list results:</p> <ul> <li> <p> <code>registerTime</code>: Sort by the time the revisions were registered with CodeDeploy.</p> </li> <li> <p> <code>firstUsedTime</code>: Sort by the time the revisions were first used in a deployment.</p> </li> <li> <p> <code>lastUsedTime</code>: Sort by the time the revisions were last used in a deployment.</p> </li> </ul> <p> If not specified or set to null, the results are returned in an arbitrary order. </p>
            sort_order: <p> The order in which to sort the list results: </p> <ul> <li> <p> <code>ascending</code>: ascending order.</p> </li> <li> <p> <code>descending</code>: descending order.</p> </li> </ul> <p>If not specified, the results are sorted in ascending order.</p> <p>If set to null, the results are sorted in an arbitrary order.</p>
            s3_bucket: <p> An Amazon S3 bucket name to limit the search for revisions. </p> <p> If set to null, all of the user's buckets are searched. </p>
            s3_key_prefix: <p> A key prefix for the set of Amazon S3 objects to limit the search for revisions. </p>
            deployed: <p> Whether to list revisions based on whether the revision is the target revision of a deployment group: </p> <ul> <li> <p> <code>include</code>: List revisions that are target revisions of a deployment group.</p> </li> <li> <p> <code>exclude</code>: Do not list revisions that are target revisions of a deployment group.</p> </li> <li> <p> <code>ignore</code>: List all revisions.</p> </li> </ul>
            next_token: <p>An identifier returned from the previous <code>ListApplicationRevisions</code> call. It can be used to return the next set of applications in the list.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.bucket_name_filter_required_exception.BucketNameFilterRequiredException: <p>A bucket name is required, but was not provided.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_bucket_name_filter_exception.InvalidBucketNameFilterException: <p>The bucket name either doesn't exist or was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployed_state_filter_exception.InvalidDeployedStateFilterException: <p>The deployed state filter was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_key_prefix_filter_exception.InvalidKeyPrefixFilterException: <p>The specified key prefix filter was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_sort_by_exception.InvalidSortByException: <p>The column name to sort by is either not present or was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_sort_order_exception.InvalidSortOrderException: <p>The sort order was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_application_revisions_input.ListApplicationRevisionsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_application_revisions_output.ListApplicationRevisionsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_application_revisions

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_application_revisions.list_application_revisions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_application_revisions_input.ListApplicationRevisionsInput = {
            "application_name": application_name
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if s3_bucket is not None:
            input_["s3_bucket"] = s3_bucket
        if s3_key_prefix is not None:
            input_["s3_key_prefix"] = s3_key_prefix
        if deployed is not None:
            input_["deployed"] = deployed
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_application_revisions(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        sort_by: Optional[
            "capo_codedeploy.types.application_revision_sort_by.ApplicationRevisionSortBy"
        ] = None,
        sort_order: Optional["capo_codedeploy.types.sort_order.SortOrder"] = None,
        s3_bucket: Optional["capo_codedeploy.types.s3_bucket.S3Bucket"] = None,
        s3_key_prefix: Optional["capo_codedeploy.types.s3_key.S3Key"] = None,
        deployed: Optional[
            "capo_codedeploy.types.list_state_filter_action.ListStateFilterAction"
        ] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_codedeploy.types.revision_location.RevisionLocation]":
        _token = next_token
        while True:
            _response = self.list_application_revisions(
                application_name,
                config_overrides=config_overrides,
                sort_by=sort_by,
                sort_order=sort_order,
                s3_bucket=s3_bucket,
                s3_key_prefix=s3_key_prefix,
                deployed=deployed,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("revisions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_applications(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "capo_codedeploy.types.list_applications_output.ListApplicationsOutput":
        """<p>Lists the applications registered with the user or Amazon Web Services account.</p>

        Args:
            next_token: <p>An identifier returned from the previous list applications call. It can be used to return the next set of applications in the list.</p>

        Raises:
            capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_applications_input.ListApplicationsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_applications_output.ListApplicationsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_applications

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_applications_input.ListApplicationsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_applications(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_codedeploy.types.application_name.ApplicationName]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_deployment_configs(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "capo_codedeploy.types.list_deployment_configs_output.ListDeploymentConfigsOutput":
        """<p>Lists the deployment configurations with the user or Amazon Web Services account.</p>

        Args:
            next_token: <p>An identifier returned from the previous <code>ListDeploymentConfigs</code> call. It can be used to return the next set of deployment configurations in the list. </p>

        Raises:
            capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_deployment_configs_input.ListDeploymentConfigsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_deployment_configs_output.ListDeploymentConfigsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_deployment_configs

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_deployment_configs.list_deployment_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_deployment_configs_input.ListDeploymentConfigsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_deployment_configs(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_codedeploy.types.deployment_config_name.DeploymentConfigName]":
        _token = next_token
        while True:
            _response = self.list_deployment_configs(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("deployment_configs_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_deployment_groups(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> (
        "capo_codedeploy.types.list_deployment_groups_output.ListDeploymentGroupsOutput"
    ):
        """<p>Lists the deployment groups for an application registered with the Amazon Web Services user or Amazon Web Services account.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>
            next_token: <p>An identifier returned from the previous list deployment groups call. It can be used to return the next set of deployment groups in the list.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_deployment_groups_input.ListDeploymentGroupsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_deployment_groups_output.ListDeploymentGroupsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_deployment_groups

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_deployment_groups.list_deployment_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_deployment_groups_input.ListDeploymentGroupsInput = {
            "application_name": application_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_deployment_groups(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_codedeploy.types.deployment_group_name.DeploymentGroupName]":
        _token = next_token
        while True:
            _response = self.list_deployment_groups(
                application_name,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("deployment_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_deployment_instances(
        self,
        deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
        instance_status_filter: Optional[
            "capo_codedeploy.types.instance_status_list.InstanceStatusList"
        ] = None,
        instance_type_filter: Optional[
            "capo_codedeploy.types.instance_type_list.InstanceTypeList"
        ] = None,
    ) -> "capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput":
        """<note> <p> The newer <code>BatchGetDeploymentTargets</code> should be used instead because it works with all compute types. <code>ListDeploymentInstances</code> throws an exception if it is used with a compute platform other than EC2/On-premises or Lambda. </p> </note> <p> Lists the instance for a deployment associated with the user or Amazon Web Services account. </p>

        Args:
            deployment_id: <p> The unique ID of a deployment. </p>
            next_token: <p>An identifier returned from the previous list deployment instances call. It can be used to return the next set of deployment instances in the list.</p>
            instance_status_filter: <p>A subset of instances to list by status:</p> <ul> <li> <p> <code>Pending</code>: Include those instances with pending deployments.</p> </li> <li> <p> <code>InProgress</code>: Include those instances where deployments are still in progress.</p> </li> <li> <p> <code>Succeeded</code>: Include those instances with successful deployments.</p> </li> <li> <p> <code>Failed</code>: Include those instances with failed deployments.</p> </li> <li> <p> <code>Skipped</code>: Include those instances with skipped deployments.</p> </li> <li> <p> <code>Unknown</code>: Include those instances with deployments in an unknown state.</p> </li> </ul>
            instance_type_filter: <p>The set of instances in a blue/green deployment, either those in the original environment ("BLUE") or those in the replacement environment ("GREEN"), for which you want to view instance information.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException: <p>The named deployment group with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.deployment_not_started_exception.DeploymentNotStartedException: <p>The specified deployment has not started.</p>
            capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException: <p>The computePlatform is invalid. The computePlatform should be <code>Lambda</code>, <code>Server</code>, or <code>ECS</code>.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_instance_type_exception.InvalidDeploymentInstanceTypeException: <p>An instance type was specified for an in-place deployment. Instance types are supported for blue/green deployments only.</p>
            capo_codedeploy.errors.invalid_instance_status_exception.InvalidInstanceStatusException: <p>The specified instance status does not exist.</p>
            capo_codedeploy.errors.invalid_instance_type_exception.InvalidInstanceTypeException: <p>An invalid instance type was specified for instances in a blue/green deployment. Valid values include "Blue" for an original environment and "Green" for a replacement environment.</p>
            capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_target_filter_name_exception.InvalidTargetFilterNameException: <p> The target filter name is invalid. </p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_deployment_instances_input.ListDeploymentInstancesInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_deployment_instances

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_deployment_instances.list_deployment_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_deployment_instances_input.ListDeploymentInstancesInput = {
            "deployment_id": deployment_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if instance_status_filter is not None:
            input_["instance_status_filter"] = instance_status_filter
        if instance_type_filter is not None:
            input_["instance_type_filter"] = instance_type_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_deployment_instances(
        self,
        deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
        instance_status_filter: Optional[
            "capo_codedeploy.types.instance_status_list.InstanceStatusList"
        ] = None,
        instance_type_filter: Optional[
            "capo_codedeploy.types.instance_type_list.InstanceTypeList"
        ] = None,
    ) -> "Iterator[capo_codedeploy.types.instance_id.InstanceId]":
        _token = next_token
        while True:
            _response = self.list_deployment_instances(
                deployment_id,
                config_overrides=config_overrides,
                next_token=_token,
                instance_status_filter=instance_status_filter,
                instance_type_filter=instance_type_filter,
            )
            _page = _resolve_path(_response, ("instances_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_deployments(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        application_name: Optional[
            "capo_codedeploy.types.application_name.ApplicationName"
        ] = None,
        deployment_group_name: Optional[
            "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
        ] = None,
        external_id: Optional["capo_codedeploy.types.external_id.ExternalId"] = None,
        include_only_statuses: Optional[
            "capo_codedeploy.types.deployment_status_list.DeploymentStatusList"
        ] = None,
        create_time_range: Optional[
            "capo_codedeploy.types.time_range.TimeRange"
        ] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "capo_codedeploy.types.list_deployments_output.ListDeploymentsOutput":
        """<p>Lists the deployments in a deployment group for an application registered with the user or Amazon Web Services account.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p> <note> <p>If <code>applicationName</code> is specified, then <code>deploymentGroupName</code> must be specified. If it is not specified, then <code>deploymentGroupName</code> must not be specified. </p> </note>
            deployment_group_name: <p>The name of a deployment group for the specified application.</p> <note> <p>If <code>deploymentGroupName</code> is specified, then <code>applicationName</code> must be specified. If it is not specified, then <code>applicationName</code> must not be specified. </p> </note>
            external_id: <p>The unique ID of an external resource for returning deployments linked to the external resource.</p>
            include_only_statuses: <p>A subset of deployments to list by status:</p> <ul> <li> <p> <code>Created</code>: Include created deployments in the resulting list.</p> </li> <li> <p> <code>Queued</code>: Include queued deployments in the resulting list.</p> </li> <li> <p> <code>In Progress</code>: Include in-progress deployments in the resulting list.</p> </li> <li> <p> <code>Succeeded</code>: Include successful deployments in the resulting list.</p> </li> <li> <p> <code>Failed</code>: Include failed deployments in the resulting list.</p> </li> <li> <p> <code>Stopped</code>: Include stopped deployments in the resulting list.</p> </li> </ul>
            create_time_range: <p>A time range (start and end) for returning a subset of the list of deployments.</p>
            next_token: <p>An identifier returned from the previous list deployments call. It can be used to return the next set of deployments in the list.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException: <p>The named deployment group with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException: <p>The deployment group name was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException: <p>The deployment group name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_status_exception.InvalidDeploymentStatusException: <p>The specified deployment status doesn't exist or cannot be determined.</p>
            capo_codedeploy.errors.invalid_external_id_exception.InvalidExternalIdException: <p>The external ID was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_input_exception.InvalidInputException: <p>The input was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_time_range_exception.InvalidTimeRangeException: <p>The specified time range was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_deployments_input.ListDeploymentsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_deployments

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_deployments.list_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_deployments_input.ListDeploymentsInput = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if deployment_group_name is not None:
            input_["deployment_group_name"] = deployment_group_name
        if external_id is not None:
            input_["external_id"] = external_id
        if include_only_statuses is not None:
            input_["include_only_statuses"] = include_only_statuses
        if create_time_range is not None:
            input_["create_time_range"] = create_time_range
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_deployments(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        application_name: Optional[
            "capo_codedeploy.types.application_name.ApplicationName"
        ] = None,
        deployment_group_name: Optional[
            "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
        ] = None,
        external_id: Optional["capo_codedeploy.types.external_id.ExternalId"] = None,
        include_only_statuses: Optional[
            "capo_codedeploy.types.deployment_status_list.DeploymentStatusList"
        ] = None,
        create_time_range: Optional[
            "capo_codedeploy.types.time_range.TimeRange"
        ] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_codedeploy.types.deployment_id.DeploymentId]":
        _token = next_token
        while True:
            _response = self.list_deployments(
                config_overrides=config_overrides,
                application_name=application_name,
                deployment_group_name=deployment_group_name,
                external_id=external_id,
                include_only_statuses=include_only_statuses,
                create_time_range=create_time_range,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("deployments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_deployment_targets(
        self,
        deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
        target_filters: Optional[
            "capo_codedeploy.types.target_filters.TargetFilters"
        ] = None,
    ) -> "capo_codedeploy.types.list_deployment_targets_output.ListDeploymentTargetsOutput":
        """<p> Returns an array of target IDs that are associated a deployment. </p>

        Args:
            deployment_id: <p> The unique ID of a deployment. </p>
            next_token: <p> A token identifier returned from the previous <code>ListDeploymentTargets</code> call. It can be used to return the next set of deployment targets in the list. </p>
            target_filters: <p> A key used to filter the returned targets. The two valid values are:</p> <ul> <li> <p> <code>TargetStatus</code> - A <code>TargetStatus</code> filter string can be <code>Failed</code>, <code>InProgress</code>, <code>Pending</code>, <code>Ready</code>, <code>Skipped</code>, <code>Succeeded</code>, or <code>Unknown</code>. </p> </li> <li> <p> <code>ServerInstanceLabel</code> - A <code>ServerInstanceLabel</code> filter string can be <code>Blue</code> or <code>Green</code>. </p> </li> </ul>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException: <p>The named deployment group with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.deployment_not_started_exception.DeploymentNotStartedException: <p>The specified deployment has not started.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_instance_type_exception.InvalidDeploymentInstanceTypeException: <p>An instance type was specified for an in-place deployment. Instance types are supported for blue/green deployments only.</p>
            capo_codedeploy.errors.invalid_instance_status_exception.InvalidInstanceStatusException: <p>The specified instance status does not exist.</p>
            capo_codedeploy.errors.invalid_instance_type_exception.InvalidInstanceTypeException: <p>An invalid instance type was specified for instances in a blue/green deployment. Valid values include "Blue" for an original environment and "Green" for a replacement environment.</p>
            capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_target_filter_name_exception.InvalidTargetFilterNameException: <p> The target filter name is invalid. </p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_deployment_targets_input.ListDeploymentTargetsInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_deployment_targets_output.ListDeploymentTargetsOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_deployment_targets

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_deployment_targets.list_deployment_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_deployment_targets_input.ListDeploymentTargetsInput = {
            "deployment_id": deployment_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if target_filters is not None:
            input_["target_filters"] = target_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_git_hub_account_token_names(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "capo_codedeploy.types.list_git_hub_account_token_names_output.ListGitHubAccountTokenNamesOutput":
        """<p>Lists the names of stored connections to GitHub accounts.</p>

        Args:
            next_token: <p>An identifier returned from the previous <code>ListGitHubAccountTokenNames</code> call. It can be used to return the next set of names in the list. </p>

        Raises:
            capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format.</p>
            capo_codedeploy.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The API used does not support the deployment.</p>
            capo_codedeploy.errors.resource_validation_exception.ResourceValidationException: <p>The specified resource could not be validated.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_git_hub_account_token_names_input.ListGitHubAccountTokenNamesInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_git_hub_account_token_names_output.ListGitHubAccountTokenNamesOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_git_hub_account_token_names

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_git_hub_account_token_names.list_git_hub_account_token_names(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_git_hub_account_token_names_input.ListGitHubAccountTokenNamesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_on_premises_instances(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        registration_status: Optional[
            "capo_codedeploy.types.registration_status.RegistrationStatus"
        ] = None,
        tag_filters: Optional[
            "capo_codedeploy.types.tag_filter_list.TagFilterList"
        ] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> "capo_codedeploy.types.list_on_premises_instances_output.ListOnPremisesInstancesOutput":
        """<p>Gets a list of names for one or more on-premises instances.</p> <p>Unless otherwise specified, both registered and deregistered on-premises instance names are listed. To list only registered or deregistered on-premises instance names, use the registration status parameter.</p>

        Args:
            registration_status: <p>The registration status of the on-premises instances:</p> <ul> <li> <p> <code>Deregistered</code>: Include deregistered on-premises instances in the resulting list.</p> </li> <li> <p> <code>Registered</code>: Include registered on-premises instances in the resulting list.</p> </li> </ul>
            tag_filters: <p>The on-premises instance tags that are used to restrict the on-premises instance names returned.</p>
            next_token: <p>An identifier returned from the previous list on-premises instances call. It can be used to return the next set of on-premises instances in the list.</p>

        Raises:
            capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_registration_status_exception.InvalidRegistrationStatusException: <p>The registration status was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_tag_filter_exception.InvalidTagFilterException: <p>The tag filter was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_on_premises_instances_input.ListOnPremisesInstancesInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_on_premises_instances_output.ListOnPremisesInstancesOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_on_premises_instances

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_on_premises_instances.list_on_premises_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_on_premises_instances_input.ListOnPremisesInstancesInput = {}
        if registration_status is not None:
            input_["registration_status"] = registration_status
        if tag_filters is not None:
            input_["tag_filters"] = tag_filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_codedeploy.types.arn.Arn",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        next_token: Optional["capo_codedeploy.types.next_token.NextToken"] = None,
    ) -> (
        "capo_codedeploy.types.list_tags_for_resource_output.ListTagsForResourceOutput"
    ):
        """<p> Returns a list of tags for the resource identified by a specified Amazon Resource Name (ARN). Tags are used to organize and categorize your CodeDeploy resources. </p>

        Args:
            resource_arn: <p> The ARN of a CodeDeploy resource. <code>ListTagsForResource</code> returns all the tags associated with the resource that is identified by the <code>ResourceArn</code>. </p>
            next_token: <p>An identifier returned from the previous <code>ListTagsForResource</code> call. It can be used to return the next set of applications in the list.</p>

        Raises:
            capo_codedeploy.errors.arn_not_supported_exception.ArnNotSupportedException: <p> The specified ARN is not supported. For example, it might be an ARN for a resource that is not expected. </p>
            capo_codedeploy.errors.invalid_arn_exception.InvalidArnException: <p> The specified ARN is not in a valid format. </p>
            capo_codedeploy.errors.resource_arn_required_exception.ResourceArnRequiredException: <p> The ARN of a resource is required, but was not found. </p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.list_tags_for_resource

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_lifecycle_event_hook_execution_status(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        deployment_id: Optional[
            "capo_codedeploy.types.deployment_id.DeploymentId"
        ] = None,
        lifecycle_event_hook_execution_id: Optional[
            "capo_codedeploy.types.lifecycle_event_hook_execution_id.LifecycleEventHookExecutionId"
        ] = None,
        status: Optional[
            "capo_codedeploy.types.lifecycle_event_status.LifecycleEventStatus"
        ] = None,
    ) -> "capo_codedeploy.types.put_lifecycle_event_hook_execution_status_output.PutLifecycleEventHookExecutionStatusOutput":
        """<p> Sets the result of a Lambda validation function. The function validates lifecycle hooks during a deployment that uses the Lambda or Amazon ECS compute platform. For Lambda deployments, the available lifecycle hooks are <code>BeforeAllowTraffic</code> and <code>AfterAllowTraffic</code>. For Amazon ECS deployments, the available lifecycle hooks are <code>BeforeInstall</code>, <code>AfterInstall</code>, <code>AfterAllowTestTraffic</code>, <code>BeforeAllowTraffic</code>, and <code>AfterAllowTraffic</code>. Lambda validation functions return <code>Succeeded</code> or <code>Failed</code>. For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#appspec-hooks-lambda">AppSpec 'hooks' Section for an Lambda Deployment </a> and <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#appspec-hooks-ecs">AppSpec 'hooks' Section for an Amazon ECS Deployment</a>.</p>

        Args:
            deployment_id: <p> The unique ID of a deployment. Pass this ID to a Lambda function that validates a deployment lifecycle event. </p>
            lifecycle_event_hook_execution_id: <p> The execution ID of a deployment's lifecycle hook. A deployment lifecycle hook is specified in the <code>hooks</code> section of the AppSpec file. </p>
            status: <p>The result of a Lambda function that validates a deployment lifecycle event. The values listed in <b>Valid Values</b> are valid for lifecycle statuses in general; however, only <code>Succeeded</code> and <code>Failed</code> can be passed successfully in your API call.</p>

        Raises:
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_lifecycle_event_hook_execution_id_exception.InvalidLifecycleEventHookExecutionIdException: <p>A lifecycle event hook is invalid. Review the <code>hooks</code> section in your AppSpec file to ensure the lifecycle events and <code>hooks</code> functions are valid.</p>
            capo_codedeploy.errors.invalid_lifecycle_event_hook_execution_status_exception.InvalidLifecycleEventHookExecutionStatusException: <p>The result of a Lambda validation function that verifies a lifecycle event is invalid. It should return <code>Succeeded</code> or <code>Failed</code>.</p>
            capo_codedeploy.errors.lifecycle_event_already_completed_exception.LifecycleEventAlreadyCompletedException: <p>An attempt to return the status of an already completed lifecycle event occurred.</p>
            capo_codedeploy.errors.unsupported_action_for_deployment_type_exception.UnsupportedActionForDeploymentTypeException: <p>A call was submitted that is not supported for the specified deployment type.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.put_lifecycle_event_hook_execution_status_input.PutLifecycleEventHookExecutionStatusInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.put_lifecycle_event_hook_execution_status_output.PutLifecycleEventHookExecutionStatusOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.put_lifecycle_event_hook_execution_status

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.put_lifecycle_event_hook_execution_status.put_lifecycle_event_hook_execution_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.put_lifecycle_event_hook_execution_status_input.PutLifecycleEventHookExecutionStatusInput = {}
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id
        if lifecycle_event_hook_execution_id is not None:
            input_["lifecycle_event_hook_execution_id"] = (
                lifecycle_event_hook_execution_id
            )
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_application_revision(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        revision: "capo_codedeploy.types.revision_location.RevisionLocation",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        description: Optional["capo_codedeploy.types.description.Description"] = None,
    ) -> None:
        """<p>Registers with CodeDeploy a revision for the specified application.</p>

        Args:
            application_name: <p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>
            description: <p>A comment about the revision.</p>
            revision: <p>Information about the application revision to register, including type and location.</p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.description_too_long_exception.DescriptionTooLongException: <p>The description is too long.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_revision_exception.InvalidRevisionException: <p>The revision was specified in an invalid format.</p>
            capo_codedeploy.errors.revision_required_exception.RevisionRequiredException: <p>The revision ID was not specified.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.register_application_revision_input.RegisterApplicationRevisionInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.register_application_revision

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.register_application_revision.register_application_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.register_application_revision_input.RegisterApplicationRevisionInput = {
            "application_name": application_name,
            "revision": revision,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_on_premises_instance(
        self,
        instance_name: "capo_codedeploy.types.instance_name.InstanceName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        iam_session_arn: Optional[
            "capo_codedeploy.types.iam_session_arn.IamSessionArn"
        ] = None,
        iam_user_arn: Optional["capo_codedeploy.types.iam_user_arn.IamUserArn"] = None,
    ) -> None:
        """<p>Registers an on-premises instance.</p> <note> <p>Only one IAM ARN (an IAM session ARN or IAM user ARN) is supported in the request. You cannot use both.</p> </note>

        Args:
            instance_name: <p>The name of the on-premises instance to register.</p>
            iam_session_arn: <p>The ARN of the IAM session to associate with the on-premises instance.</p>
            iam_user_arn: <p>The ARN of the user to associate with the on-premises instance.</p>

        Raises:
            capo_codedeploy.errors.iam_arn_required_exception.IamArnRequiredException: <p>No IAM ARN was included in the request. You must use an IAM session ARN or user ARN in the request.</p>
            capo_codedeploy.errors.iam_session_arn_already_registered_exception.IamSessionArnAlreadyRegisteredException: <p>The request included an IAM session ARN that has already been used to register a different instance.</p>
            capo_codedeploy.errors.iam_user_arn_already_registered_exception.IamUserArnAlreadyRegisteredException: <p>The specified user ARN is already registered with an on-premises instance.</p>
            capo_codedeploy.errors.iam_user_arn_required_exception.IamUserArnRequiredException: <p>An user ARN was not specified.</p>
            capo_codedeploy.errors.instance_name_already_registered_exception.InstanceNameAlreadyRegisteredException: <p>The specified on-premises instance name is already registered.</p>
            capo_codedeploy.errors.instance_name_required_exception.InstanceNameRequiredException: <p>An on-premises instance name was not specified.</p>
            capo_codedeploy.errors.invalid_iam_session_arn_exception.InvalidIamSessionArnException: <p>The IAM session ARN was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_iam_user_arn_exception.InvalidIamUserArnException: <p>The user ARN was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException: <p>The on-premises instance name was specified in an invalid format.</p>
            capo_codedeploy.errors.multiple_iam_arns_provided_exception.MultipleIamArnsProvidedException: <p>Both an user ARN and an IAM session ARN were included in the request. Use only one ARN type.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.register_on_premises_instance_input.RegisterOnPremisesInstanceInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.register_on_premises_instance

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.register_on_premises_instance.register_on_premises_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.register_on_premises_instance_input.RegisterOnPremisesInstanceInput = {
            "instance_name": instance_name
        }
        if iam_session_arn is not None:
            input_["iam_session_arn"] = iam_session_arn
        if iam_user_arn is not None:
            input_["iam_user_arn"] = iam_user_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_tags_from_on_premises_instances(
        self,
        tags: "capo_codedeploy.types.tag_list.TagList",
        instance_names: "capo_codedeploy.types.instance_name_list.InstanceNameList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> None:
        """<p>Removes one or more tags from one or more on-premises instances.</p>

        Args:
            tags: <p>The tag key-value pairs to remove from the on-premises instances.</p>
            instance_names: <p>The names of the on-premises instances from which to remove tags.</p>

        Raises:
            capo_codedeploy.errors.instance_limit_exceeded_exception.InstanceLimitExceededException: <p>The maximum number of allowed on-premises instances in a single call was exceeded.</p>
            capo_codedeploy.errors.instance_name_required_exception.InstanceNameRequiredException: <p>An on-premises instance name was not specified.</p>
            capo_codedeploy.errors.instance_not_registered_exception.InstanceNotRegisteredException: <p>The specified on-premises instance is not registered.</p>
            capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException: <p>The on-premises instance name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_tag_exception.InvalidTagException: <p>The tag was specified in an invalid format.</p>
            capo_codedeploy.errors.tag_limit_exceeded_exception.TagLimitExceededException: <p>The maximum allowed number of tags was exceeded.</p>
            capo_codedeploy.errors.tag_required_exception.TagRequiredException: <p>A tag was not specified.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.remove_tags_from_on_premises_instances_input.RemoveTagsFromOnPremisesInstancesInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.remove_tags_from_on_premises_instances

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.remove_tags_from_on_premises_instances.remove_tags_from_on_premises_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.remove_tags_from_on_premises_instances_input.RemoveTagsFromOnPremisesInstancesInput = {
            "tags": tags,
            "instance_names": instance_names,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def skip_wait_time_for_instance_termination(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        deployment_id: Optional[
            "capo_codedeploy.types.deployment_id.DeploymentId"
        ] = None,
    ) -> None:
        """<p>In a blue/green deployment, overrides any specified wait time and starts terminating instances immediately after the traffic routing is complete.</p>

        Args:
            deployment_id: <p> The unique ID of a blue/green deployment for which you want to skip the instance termination wait time. </p>

        Raises:
            capo_codedeploy.errors.deployment_already_completed_exception.DeploymentAlreadyCompletedException: <p>The deployment is already complete.</p>
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.deployment_not_started_exception.DeploymentNotStartedException: <p>The specified deployment has not started.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.unsupported_action_for_deployment_type_exception.UnsupportedActionForDeploymentTypeException: <p>A call was submitted that is not supported for the specified deployment type.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.skip_wait_time_for_instance_termination_input.SkipWaitTimeForInstanceTerminationInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.skip_wait_time_for_instance_termination

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.skip_wait_time_for_instance_termination.skip_wait_time_for_instance_termination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.skip_wait_time_for_instance_termination_input.SkipWaitTimeForInstanceTerminationInput = {}
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_deployment(
        self,
        deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        auto_rollback_enabled: Optional[
            "capo_codedeploy.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_codedeploy.types.stop_deployment_output.StopDeploymentOutput":
        """<p>Attempts to stop an ongoing deployment.</p>

        Args:
            deployment_id: <p> The unique ID of a deployment. </p>
            auto_rollback_enabled: <p> Indicates, when a deployment is stopped, whether instances that have been updated should be rolled back to the previous version of the application revision. </p>

        Raises:
            capo_codedeploy.errors.deployment_already_completed_exception.DeploymentAlreadyCompletedException: <p>The deployment is already complete.</p>
            capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException: <p>The deployment with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException: <p>The named deployment group with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException: <p>At least one deployment ID must be specified.</p>
            capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException: <p>At least one of the deployment IDs was specified in an invalid format.</p>
            capo_codedeploy.errors.unsupported_action_for_deployment_type_exception.UnsupportedActionForDeploymentTypeException: <p>A call was submitted that is not supported for the specified deployment type.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.stop_deployment_input.StopDeploymentInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.stop_deployment_output.StopDeploymentOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.stop_deployment

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.stop_deployment.stop_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.stop_deployment_input.StopDeploymentInput = {
            "deployment_id": deployment_id
        }
        if auto_rollback_enabled is not None:
            input_["auto_rollback_enabled"] = auto_rollback_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_codedeploy.types.arn.Arn",
        tags: "capo_codedeploy.types.tag_list.TagList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.tag_resource_output.TagResourceOutput":
        """<p> Associates the list of tags in the input <code>Tags</code> parameter with the resource identified by the <code>ResourceArn</code> input parameter. </p>

        Args:
            resource_arn: <p> The ARN of a resource, such as a CodeDeploy application or deployment group. </p>
            tags: <p> A list of tags that <code>TagResource</code> associates with a resource. The resource is identified by the <code>ResourceArn</code> input parameter. </p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.arn_not_supported_exception.ArnNotSupportedException: <p> The specified ARN is not supported. For example, it might be an ARN for a resource that is not expected. </p>
            capo_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException: <p>The deployment configuration does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException: <p>The named deployment group with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.invalid_arn_exception.InvalidArnException: <p> The specified ARN is not in a valid format. </p>
            capo_codedeploy.errors.invalid_tags_to_add_exception.InvalidTagsToAddException: <p> The specified tags are not valid. </p>
            capo_codedeploy.errors.resource_arn_required_exception.ResourceArnRequiredException: <p> The ARN of a resource is required, but was not found. </p>
            capo_codedeploy.errors.tag_required_exception.TagRequiredException: <p>A tag was not specified.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.tag_resource

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.tag_resource_input.TagResourceInput = {
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

    def untag_resource(
        self,
        resource_arn: "capo_codedeploy.types.arn.Arn",
        tag_keys: "capo_codedeploy.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
    ) -> "capo_codedeploy.types.untag_resource_output.UntagResourceOutput":
        """<p> Disassociates a resource from a list of tags. The resource is identified by the <code>ResourceArn</code> input parameter. The tags are identified by the list of keys in the <code>TagKeys</code> input parameter. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) that specifies from which resource to disassociate the tags with the keys in the <code>TagKeys</code> input parameter. </p>
            tag_keys: <p> A list of keys of <code>Tag</code> objects. The <code>Tag</code> objects identified by the keys are disassociated from the resource specified by the <code>ResourceArn</code> input parameter. </p>

        Raises:
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.arn_not_supported_exception.ArnNotSupportedException: <p> The specified ARN is not supported. For example, it might be an ARN for a resource that is not expected. </p>
            capo_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException: <p>The deployment configuration does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException: <p>The named deployment group with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.invalid_arn_exception.InvalidArnException: <p> The specified ARN is not in a valid format. </p>
            capo_codedeploy.errors.invalid_tags_to_add_exception.InvalidTagsToAddException: <p> The specified tags are not valid. </p>
            capo_codedeploy.errors.resource_arn_required_exception.ResourceArnRequiredException: <p> The ARN of a resource is required, but was not found. </p>
            capo_codedeploy.errors.tag_required_exception.TagRequiredException: <p>A tag was not specified.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.untag_resource

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.untag_resource_input.UntagResourceInput = {
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

    def update_application(
        self,
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        application_name: Optional[
            "capo_codedeploy.types.application_name.ApplicationName"
        ] = None,
        new_application_name: Optional[
            "capo_codedeploy.types.application_name.ApplicationName"
        ] = None,
    ) -> None:
        """<p>Changes the name of an application.</p>

        Args:
            application_name: <p>The current name of the application you want to change.</p>
            new_application_name: <p>The new name to give the application.</p>

        Raises:
            capo_codedeploy.errors.application_already_exists_exception.ApplicationAlreadyExistsException: <p>An application with the specified name with the user or Amazon Web Services account already exists.</p>
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.update_application_input.UpdateApplicationInput]",
        ) -> OperationResponse[None]:
            import capo_codedeploy._operations.code_deploy_20141006.update_application

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.update_application_input.UpdateApplicationInput = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if new_application_name is not None:
            input_["new_application_name"] = new_application_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_deployment_group(
        self,
        application_name: "capo_codedeploy.types.application_name.ApplicationName",
        current_deployment_group_name: "capo_codedeploy.types.deployment_group_name.DeploymentGroupName",
        *,
        config_overrides: Optional[CodeDeployClientConfig] = None,
        new_deployment_group_name: Optional[
            "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
        ] = None,
        deployment_config_name: Optional[
            "capo_codedeploy.types.deployment_config_name.DeploymentConfigName"
        ] = None,
        ec2_tag_filters: Optional[
            "capo_codedeploy.types.ec2_tag_filter_list.EC2TagFilterList"
        ] = None,
        on_premises_instance_tag_filters: Optional[
            "capo_codedeploy.types.tag_filter_list.TagFilterList"
        ] = None,
        auto_scaling_groups: Optional[
            "capo_codedeploy.types.auto_scaling_group_name_list.AutoScalingGroupNameList"
        ] = None,
        service_role_arn: Optional["capo_codedeploy.types.role.Role"] = None,
        trigger_configurations: Optional[
            "capo_codedeploy.types.trigger_config_list.TriggerConfigList"
        ] = None,
        alarm_configuration: Optional[
            "capo_codedeploy.types.alarm_configuration.AlarmConfiguration"
        ] = None,
        auto_rollback_configuration: Optional[
            "capo_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
        ] = None,
        outdated_instances_strategy: Optional[
            "capo_codedeploy.types.outdated_instances_strategy.OutdatedInstancesStrategy"
        ] = None,
        deployment_style: Optional[
            "capo_codedeploy.types.deployment_style.DeploymentStyle"
        ] = None,
        blue_green_deployment_configuration: Optional[
            "capo_codedeploy.types.blue_green_deployment_configuration.BlueGreenDeploymentConfiguration"
        ] = None,
        load_balancer_info: Optional[
            "capo_codedeploy.types.load_balancer_info.LoadBalancerInfo"
        ] = None,
        ec2_tag_set: Optional["capo_codedeploy.types.ec2_tag_set.EC2TagSet"] = None,
        ecs_services: Optional[
            "capo_codedeploy.types.ecs_service_list.ECSServiceList"
        ] = None,
        on_premises_tag_set: Optional[
            "capo_codedeploy.types.on_premises_tag_set.OnPremisesTagSet"
        ] = None,
        termination_hook_enabled: Optional[
            "capo_codedeploy.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_codedeploy.types.update_deployment_group_output.UpdateDeploymentGroupOutput":
        """<p>Changes information about a deployment group.</p>

        Args:
            application_name: <p>The application name that corresponds to the deployment group to update.</p>
            current_deployment_group_name: <p>The current name of the deployment group.</p>
            new_deployment_group_name: <p>The new name of the deployment group, if you want to change it.</p>
            deployment_config_name: <p>The replacement deployment configuration name to use, if you want to change it.</p>
            ec2_tag_filters: <p>The replacement set of Amazon EC2 tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.</p>
            on_premises_instance_tag_filters: <p>The replacement set of on-premises instance tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.</p>
            auto_scaling_groups: <p>The replacement list of Auto Scaling groups to be included in the deployment group, if you want to change them.</p> <ul> <li> <p>To keep the Auto Scaling groups, enter their names or do not specify this parameter. </p> </li> <li> <p>To remove Auto Scaling groups, specify a non-null empty list of Auto Scaling group names to detach all CodeDeploy-managed Auto Scaling lifecycle hooks. For examples, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-auto-scaling.html#troubleshooting-auto-scaling-heartbeat">Amazon EC2 instances in an Amazon EC2 Auto Scaling group fail to launch and receive the error "Heartbeat Timeout"</a> in the <i>CodeDeploy User Guide</i>.</p> </li> </ul>
            service_role_arn: <p>A replacement ARN for the service role, if you want to change it.</p>
            trigger_configurations: <p>Information about triggers to change when the deployment group is updated. For examples, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-edit.html">Edit a Trigger in a CodeDeploy Deployment Group</a> in the <i>CodeDeploy User Guide</i>.</p>
            alarm_configuration: <p>Information to add or change about Amazon CloudWatch alarms when the deployment group is updated.</p>
            auto_rollback_configuration: <p>Information for an automatic rollback configuration that is added or changed when a deployment group is updated.</p>
            outdated_instances_strategy: <p>Indicates what happens when new Amazon EC2 instances are launched mid-deployment and do not receive the deployed application revision.</p> <p>If this option is set to <code>UPDATE</code> or is unspecified, CodeDeploy initiates one or more 'auto-update outdated instances' deployments to apply the deployed application revision to the new Amazon EC2 instances.</p> <p>If this option is set to <code>IGNORE</code>, CodeDeploy does not initiate a deployment to update the new Amazon EC2 instances. This may result in instances having different revisions.</p>
            deployment_style: <p>Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.</p>
            blue_green_deployment_configuration: <p>Information about blue/green deployment options for a deployment group.</p>
            load_balancer_info: <p>Information about the load balancer used in a deployment.</p>
            ec2_tag_set: <p>Information about groups of tags applied to on-premises instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups.</p>
            ecs_services: <p> The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <code><clustername>:<servicename></code>. </p>
            on_premises_tag_set: <p>Information about an on-premises instance tag set. The deployment group includes only on-premises instances identified by all the tag groups.</p>
            termination_hook_enabled: <p>This parameter only applies if you are using CodeDeploy with Amazon EC2 Auto Scaling. For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html">Integrating CodeDeploy with Amazon EC2 Auto Scaling</a> in the <i>CodeDeploy User Guide</i>.</p> <p>Set <code>terminationHookEnabled</code> to <code>true</code> to have CodeDeploy install a termination hook into your Auto Scaling group when you update a deployment group. When this hook is installed, CodeDeploy will perform termination deployments.</p> <p>For information about termination deployments, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable">Enabling termination deployments during Auto Scaling scale-in events</a> in the <i>CodeDeploy User Guide</i>.</p> <p>For more information about Auto Scaling scale-in events, see the <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html#as-lifecycle-scale-in">Scale in</a> topic in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Raises:
            capo_codedeploy.errors.alarms_limit_exceeded_exception.AlarmsLimitExceededException: <p>The maximum number of alarms for a deployment group (10) was exceeded.</p>
            capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException: <p>The application does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException: <p>The minimum number of required application names was not specified.</p>
            capo_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException: <p>The deployment configuration does not exist with the user or Amazon Web Services account.</p>
            capo_codedeploy.errors.deployment_group_already_exists_exception.DeploymentGroupAlreadyExistsException: <p>A deployment group with the specified name with the user or Amazon Web Services account already exists.</p>
            capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException: <p>The named deployment group with the user or Amazon Web Services account does not exist.</p>
            capo_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException: <p>The deployment group name was not specified.</p>
            capo_codedeploy.errors.ecs_service_mapping_limit_exceeded_exception.ECSServiceMappingLimitExceededException: <p> The Amazon ECS service is associated with more than one deployment groups. An Amazon ECS service can be associated with only one deployment group. </p>
            capo_codedeploy.errors.invalid_alarm_config_exception.InvalidAlarmConfigException: <p>The format of the alarm configuration is invalid. Possible causes include:</p> <ul> <li> <p>The alarm list is null.</p> </li> <li> <p>The alarm object is null.</p> </li> <li> <p>The alarm name is empty or null or exceeds the limit of 255 characters.</p> </li> <li> <p>Two alarms with the same name have been specified.</p> </li> <li> <p>The alarm configuration is enabled, but the alarm list is empty.</p> </li> </ul>
            capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException: <p>The application name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_auto_rollback_config_exception.InvalidAutoRollbackConfigException: <p>The automatic rollback configuration was specified in an invalid format. For example, automatic rollback is enabled, but an invalid triggering event type or no event types were listed.</p>
            capo_codedeploy.errors.invalid_auto_scaling_group_exception.InvalidAutoScalingGroupException: <p>The Auto Scaling group was specified in an invalid format or does not exist.</p>
            capo_codedeploy.errors.invalid_blue_green_deployment_configuration_exception.InvalidBlueGreenDeploymentConfigurationException: <p>The configuration for the blue/green deployment group was provided in an invalid format. For information about deployment configuration format, see <a>CreateDeploymentConfig</a>.</p>
            capo_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException: <p>The deployment configuration name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException: <p>The deployment group name was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_deployment_style_exception.InvalidDeploymentStyleException: <p>An invalid deployment style was specified. Valid deployment types include "IN_PLACE" and "BLUE_GREEN." Valid deployment options include "WITH_TRAFFIC_CONTROL" and "WITHOUT_TRAFFIC_CONTROL."</p>
            capo_codedeploy.errors.invalid_ec2_tag_combination_exception.InvalidEC2TagCombinationException: <p>A call was submitted that specified both Ec2TagFilters and Ec2TagSet, but only one of these data types can be used in a single call.</p>
            capo_codedeploy.errors.invalid_ec2_tag_exception.InvalidEC2TagException: <p>The tag was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_ecs_service_exception.InvalidECSServiceException: <p> The Amazon ECS service identifier is not valid. </p>
            capo_codedeploy.errors.invalid_input_exception.InvalidInputException: <p>The input was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_load_balancer_info_exception.InvalidLoadBalancerInfoException: <p>An invalid load balancer name, or no load balancer name, was specified.</p>
            capo_codedeploy.errors.invalid_on_premises_tag_combination_exception.InvalidOnPremisesTagCombinationException: <p>A call was submitted that specified both OnPremisesTagFilters and OnPremisesTagSet, but only one of these data types can be used in a single call.</p>
            capo_codedeploy.errors.invalid_role_exception.InvalidRoleException: <p>The service role ARN was specified in an invalid format. Or, if an Auto Scaling group was specified, the specified service role does not grant the appropriate permissions to Amazon EC2 Auto Scaling.</p>
            capo_codedeploy.errors.invalid_tag_exception.InvalidTagException: <p>The tag was specified in an invalid format.</p>
            capo_codedeploy.errors.invalid_target_group_pair_exception.InvalidTargetGroupPairException: <p> A target group pair associated with this deployment is not valid. </p>
            capo_codedeploy.errors.invalid_traffic_routing_configuration_exception.InvalidTrafficRoutingConfigurationException: <p> The configuration that specifies how traffic is routed during a deployment is invalid.</p>
            capo_codedeploy.errors.invalid_trigger_config_exception.InvalidTriggerConfigException: <p>The trigger was specified in an invalid format.</p>
            capo_codedeploy.errors.lifecycle_hook_limit_exceeded_exception.LifecycleHookLimitExceededException: <p>The limit for lifecycle hooks was exceeded.</p>
            capo_codedeploy.errors.tag_set_list_limit_exceeded_exception.TagSetListLimitExceededException: <p>The number of tag groups included in the tag set list exceeded the maximum allowed limit of 3.</p>
            capo_codedeploy.errors.throttling_exception.ThrottlingException: <p>An API function was called too frequently.</p>
            capo_codedeploy.errors.trigger_targets_limit_exceeded_exception.TriggerTargetsLimitExceededException: <p>The maximum allowed number of triggers was exceeded.</p>
            capo_codedeploy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codedeploy.types.update_deployment_group_input.UpdateDeploymentGroupInput]",
        ) -> OperationResponse[
            "capo_codedeploy.types.update_deployment_group_output.UpdateDeploymentGroupOutput"
        ]:
            import capo_codedeploy._operations.code_deploy_20141006.update_deployment_group

            output, http_response = (
                capo_codedeploy._operations.code_deploy_20141006.update_deployment_group.update_deployment_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codedeploy.types.update_deployment_group_input.UpdateDeploymentGroupInput = {
            "application_name": application_name,
            "current_deployment_group_name": current_deployment_group_name,
        }
        if new_deployment_group_name is not None:
            input_["new_deployment_group_name"] = new_deployment_group_name
        if deployment_config_name is not None:
            input_["deployment_config_name"] = deployment_config_name
        if ec2_tag_filters is not None:
            input_["ec2_tag_filters"] = ec2_tag_filters
        if on_premises_instance_tag_filters is not None:
            input_["on_premises_instance_tag_filters"] = (
                on_premises_instance_tag_filters
            )
        if auto_scaling_groups is not None:
            input_["auto_scaling_groups"] = auto_scaling_groups
        if service_role_arn is not None:
            input_["service_role_arn"] = service_role_arn
        if trigger_configurations is not None:
            input_["trigger_configurations"] = trigger_configurations
        if alarm_configuration is not None:
            input_["alarm_configuration"] = alarm_configuration
        if auto_rollback_configuration is not None:
            input_["auto_rollback_configuration"] = auto_rollback_configuration
        if outdated_instances_strategy is not None:
            input_["outdated_instances_strategy"] = outdated_instances_strategy
        if deployment_style is not None:
            input_["deployment_style"] = deployment_style
        if blue_green_deployment_configuration is not None:
            input_["blue_green_deployment_configuration"] = (
                blue_green_deployment_configuration
            )
        if load_balancer_info is not None:
            input_["load_balancer_info"] = load_balancer_info
        if ec2_tag_set is not None:
            input_["ec2_tag_set"] = ec2_tag_set
        if ecs_services is not None:
            input_["ecs_services"] = ecs_services
        if on_premises_tag_set is not None:
            input_["on_premises_tag_set"] = on_premises_tag_set
        if termination_hook_enabled is not None:
            input_["termination_hook_enabled"] = termination_hook_enabled

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
