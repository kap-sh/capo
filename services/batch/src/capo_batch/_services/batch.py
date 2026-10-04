"""Generated from Smithy shape ``com.amazonaws.batch#AWSBatchV20160810``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_batch._auth._signers
import capo_batch._auth._sigv4
from capo_batch._auth._identity import Credentials
from capo_batch._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_batch._auth._zapros_handler import AuthMiddleware
from capo_batch._pagination import resolve_path as _resolve_path
from capo_batch._services._aws_config import aws_config
from capo_batch._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_batch.types.array_properties
    import capo_batch.types.boolean
    import capo_batch.types.cancel_job_request
    import capo_batch.types.cancel_job_response
    import capo_batch.types.cancel_jobs_request
    import capo_batch.types.cancel_jobs_response
    import capo_batch.types.capacity_limits
    import capo_batch.types.ce_state
    import capo_batch.types.ce_type
    import capo_batch.types.client_request_token
    import capo_batch.types.compute_environment_detail
    import capo_batch.types.compute_environment_orders
    import capo_batch.types.compute_resource
    import capo_batch.types.compute_resource_update
    import capo_batch.types.consumable_resource_properties
    import capo_batch.types.consumable_resource_summary
    import capo_batch.types.container_overrides
    import capo_batch.types.container_properties
    import capo_batch.types.create_compute_environment_request
    import capo_batch.types.create_compute_environment_response
    import capo_batch.types.create_consumable_resource_request
    import capo_batch.types.create_consumable_resource_response
    import capo_batch.types.create_job_queue_request
    import capo_batch.types.create_job_queue_response
    import capo_batch.types.create_quota_share_request
    import capo_batch.types.create_quota_share_response
    import capo_batch.types.create_scheduling_policy_request
    import capo_batch.types.create_scheduling_policy_response
    import capo_batch.types.create_service_environment_request
    import capo_batch.types.create_service_environment_response
    import capo_batch.types.delete_compute_environment_request
    import capo_batch.types.delete_compute_environment_response
    import capo_batch.types.delete_consumable_resource_request
    import capo_batch.types.delete_consumable_resource_response
    import capo_batch.types.delete_job_queue_request
    import capo_batch.types.delete_job_queue_response
    import capo_batch.types.delete_quota_share_request
    import capo_batch.types.delete_quota_share_response
    import capo_batch.types.delete_scheduling_policy_request
    import capo_batch.types.delete_scheduling_policy_response
    import capo_batch.types.delete_service_environment_request
    import capo_batch.types.delete_service_environment_response
    import capo_batch.types.deregister_job_definition_request
    import capo_batch.types.deregister_job_definition_response
    import capo_batch.types.describe_compute_environments_request
    import capo_batch.types.describe_compute_environments_response
    import capo_batch.types.describe_consumable_resource_request
    import capo_batch.types.describe_consumable_resource_response
    import capo_batch.types.describe_job_definitions_request
    import capo_batch.types.describe_job_definitions_response
    import capo_batch.types.describe_job_queues_request
    import capo_batch.types.describe_job_queues_response
    import capo_batch.types.describe_jobs_request
    import capo_batch.types.describe_jobs_response
    import capo_batch.types.describe_quota_share_request
    import capo_batch.types.describe_quota_share_response
    import capo_batch.types.describe_scheduling_policies_request
    import capo_batch.types.describe_scheduling_policies_response
    import capo_batch.types.describe_service_environments_request
    import capo_batch.types.describe_service_environments_response
    import capo_batch.types.describe_service_job_request
    import capo_batch.types.describe_service_job_response
    import capo_batch.types.ecs_properties
    import capo_batch.types.ecs_properties_override
    import capo_batch.types.ecs_settings
    import capo_batch.types.eks_configuration
    import capo_batch.types.eks_configuration_update
    import capo_batch.types.eks_properties
    import capo_batch.types.eks_properties_override
    import capo_batch.types.fairshare_policy
    import capo_batch.types.get_job_queue_snapshot_request
    import capo_batch.types.get_job_queue_snapshot_response
    import capo_batch.types.integer
    import capo_batch.types.job_definition
    import capo_batch.types.job_definition_type
    import capo_batch.types.job_dependency_list
    import capo_batch.types.job_queue_detail
    import capo_batch.types.job_queue_type
    import capo_batch.types.job_state_time_limit_actions
    import capo_batch.types.job_status
    import capo_batch.types.job_summary
    import capo_batch.types.job_timeout
    import capo_batch.types.jq_state
    import capo_batch.types.list_consumable_resources_filter_list
    import capo_batch.types.list_consumable_resources_request
    import capo_batch.types.list_consumable_resources_response
    import capo_batch.types.list_jobs_by_consumable_resource_filter_list
    import capo_batch.types.list_jobs_by_consumable_resource_request
    import capo_batch.types.list_jobs_by_consumable_resource_response
    import capo_batch.types.list_jobs_by_consumable_resource_summary
    import capo_batch.types.list_jobs_filter_list
    import capo_batch.types.list_jobs_request
    import capo_batch.types.list_jobs_response
    import capo_batch.types.list_quota_shares_request
    import capo_batch.types.list_quota_shares_response
    import capo_batch.types.list_scheduling_policies_request
    import capo_batch.types.list_scheduling_policies_response
    import capo_batch.types.list_service_jobs_request
    import capo_batch.types.list_service_jobs_response
    import capo_batch.types.list_tags_for_resource_request
    import capo_batch.types.list_tags_for_resource_response
    import capo_batch.types.long
    import capo_batch.types.node_overrides
    import capo_batch.types.node_properties
    import capo_batch.types.parameters_map
    import capo_batch.types.platform_capability_list
    import capo_batch.types.quota_share_capacity_limits
    import capo_batch.types.quota_share_detail
    import capo_batch.types.quota_share_policy
    import capo_batch.types.quota_share_preemption_configuration
    import capo_batch.types.quota_share_resource_sharing_configuration
    import capo_batch.types.quota_share_state
    import capo_batch.types.register_job_definition_request
    import capo_batch.types.register_job_definition_response
    import capo_batch.types.retry_strategy
    import capo_batch.types.scheduling_policy_listing_detail
    import capo_batch.types.service_environment_detail
    import capo_batch.types.service_environment_orders
    import capo_batch.types.service_environment_state
    import capo_batch.types.service_environment_type
    import capo_batch.types.service_job_preemption_configuration
    import capo_batch.types.service_job_retry_strategy
    import capo_batch.types.service_job_status
    import capo_batch.types.service_job_summary
    import capo_batch.types.service_job_timeout
    import capo_batch.types.service_job_type
    import capo_batch.types.string
    import capo_batch.types.string_list
    import capo_batch.types.submit_job_request
    import capo_batch.types.submit_job_response
    import capo_batch.types.submit_service_job_request
    import capo_batch.types.submit_service_job_response
    import capo_batch.types.tag_keys_list
    import capo_batch.types.tag_resource_request
    import capo_batch.types.tag_resource_response
    import capo_batch.types.tagris_tags_map
    import capo_batch.types.terminate_job_request
    import capo_batch.types.terminate_job_response
    import capo_batch.types.terminate_jobs_request
    import capo_batch.types.terminate_jobs_response
    import capo_batch.types.terminate_service_job_request
    import capo_batch.types.terminate_service_job_response
    import capo_batch.types.terminate_service_jobs_request
    import capo_batch.types.terminate_service_jobs_response
    import capo_batch.types.untag_resource_request
    import capo_batch.types.untag_resource_response
    import capo_batch.types.update_compute_environment_request
    import capo_batch.types.update_compute_environment_response
    import capo_batch.types.update_consumable_resource_request
    import capo_batch.types.update_consumable_resource_response
    import capo_batch.types.update_job_queue_request
    import capo_batch.types.update_job_queue_response
    import capo_batch.types.update_policy
    import capo_batch.types.update_quota_share_request
    import capo_batch.types.update_quota_share_response
    import capo_batch.types.update_scheduling_policy_request
    import capo_batch.types.update_scheduling_policy_response
    import capo_batch.types.update_service_environment_request
    import capo_batch.types.update_service_environment_response
    import capo_batch.types.update_service_job_request
    import capo_batch.types.update_service_job_response


class BatchClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class BatchClient:
    """A client for the ``Batch`` service.

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
        self._config = BatchClientConfig(
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
        self, config_overrides: Optional[BatchClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BatchClientConfig = config_overrides or {}
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

    def cancel_job(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_id: Optional["capo_batch.types.string.String"] = None,
        reason: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.cancel_job_response.CancelJobResponse":
        """<p>Cancels a job in an Batch job queue. Jobs that are in a <code>SUBMITTED</code>, <code>PENDING</code>, or <code>RUNNABLE</code> state are cancelled and the job status is updated to <code>FAILED</code>.</p> <note> <p>A <code>PENDING</code> job is cancelled after all dependency jobs are completed. Therefore, it might take longer than expected to cancel a job in <code>PENDING</code> status.</p> <p>When you try to cancel an array parent job in <code>PENDING</code>, Batch attempts to cancel all child jobs. The array parent job is cancelled when all child jobs are completed.</p> </note> <p>Jobs that progressed to the <code>STARTING</code> or <code>RUNNING</code> state aren't cancelled. However, the API operation still succeeds, even if no job is cancelled. These jobs must be terminated with the <a>TerminateJob</a> or <a>TerminateJobs</a> operation.</p>

        Args:
            job_id: <p>The Batch job ID of the job to cancel.</p>
            reason: <p>A message to attach to the job that explains the reason for cancelling it. This message is returned by future <a>DescribeJobs</a> operations on the job. It is also recorded in the Batch activity logs.</p> <p>This parameter has a limit of 1024 characters.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel a job
            This example cancels a job with the specified job ID.

            >>> client.cancel_job(reason='Cancelling job.', job_id='1d828f65-7a4d-42e8-996d-3b900ed59dc4')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.cancel_job_request.CancelJobRequest]",
        ) -> OperationResponse[
            "capo_batch.types.cancel_job_response.CancelJobResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.cancel_job

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.cancel_job.cancel_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.cancel_job_request.CancelJobRequest = {}
        if job_id is not None:
            input_["job_id"] = job_id
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_jobs(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        jobs: Optional["capo_batch.types.string_list.StringList"] = None,
        reason: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.cancel_jobs_response.CancelJobsResponse":
        """<p>Cancels up to 50 jobs in an Batch job queue. This is a bulk version of <a>CancelJob</a>. Jobs that are in a <code>SUBMITTED</code>, <code>PENDING</code>, or <code>RUNNABLE</code> state are cancelled and the job status is updated to <code>FAILED</code>.</p> <note> <p>A <code>PENDING</code> job is cancelled after all dependency jobs are completed. Therefore, it might take longer than expected to cancel a job in <code>PENDING</code> status.</p> <p>When you try to cancel an array parent job in <code>PENDING</code>, Batch attempts to cancel all child jobs. The array parent job is cancelled when all child jobs are completed.</p> </note> <p>Jobs that progressed to the <code>STARTING</code> or <code>RUNNING</code> state aren't cancelled. These jobs must be terminated with the <a>TerminateJob</a> or <a>TerminateJobs</a> operation.</p> <p>Batch reports the result for each job individually in the response. Jobs that were processed successfully are reported in the <code>successful</code> list. Jobs that encountered errors are reported in the <code>errors</code> list. The response returns an HTTP status code of <code>200</code> even when some jobs encountered errors, so check the <code>errors</code> list. Jobs that can't be found are treated as successfully processed.</p> <important> <p>This operation requires <code>batch:CancelJob</code> permission for each job in the request. There is no separate <code>batch:CancelJobs</code> IAM action. If a caller's IAM policy grants <code>batch:CancelJob</code>, they can use both the singular <a>CancelJob</a> and bulk <code>CancelJobs</code> operations.</p> </important>

        Args:
            jobs: <p>An array of up to 50 Batch job IDs of the jobs to cancel.</p>
            reason: <p>A message to attach to the job that explains the reason for cancelling it. This message is returned by future <a>DescribeJobs</a> operations on the job. It is also recorded in the Batch activity logs.</p> <p>This parameter has a limit of 1024 characters.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel multiple jobs
            This example cancels the jobs with the specified job IDs.

            >>> client.cancel_jobs(jobs=['1d828f65-7a4d-42e8-996d-3b900ed59dc4', 'b3d0f26e-6d3a-4a5b-9c2e-7f4a1b2c3d4e'], reason='Cancelling jobs.')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.cancel_jobs_request.CancelJobsRequest]",
        ) -> OperationResponse[
            "capo_batch.types.cancel_jobs_response.CancelJobsResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.cancel_jobs

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.cancel_jobs.cancel_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.cancel_jobs_request.CancelJobsRequest = {}
        if jobs is not None:
            input_["jobs"] = jobs
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_compute_environment(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        compute_environment_name: Optional["capo_batch.types.string.String"] = None,
        type: Optional["capo_batch.types.ce_type.CEType"] = None,
        state: Optional["capo_batch.types.ce_state.CEState"] = None,
        unmanagedv_cpus: Optional["capo_batch.types.integer.Integer"] = None,
        compute_resources: Optional[
            "capo_batch.types.compute_resource.ComputeResource"
        ] = None,
        service_role: Optional["capo_batch.types.string.String"] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
        eks_configuration: Optional[
            "capo_batch.types.eks_configuration.EksConfiguration"
        ] = None,
        context: Optional["capo_batch.types.string.String"] = None,
        ecs_settings: Optional["capo_batch.types.ecs_settings.EcsSettings"] = None,
    ) -> "capo_batch.types.create_compute_environment_response.CreateComputeEnvironmentResponse":
        """<p>Creates an Batch compute environment. You can create <code>MANAGED</code> or <code>UNMANAGED</code> compute environments. <code>MANAGED</code> compute environments can use Amazon EC2 or Fargate resources. <code>UNMANAGED</code> compute environments can only use EC2 resources.</p> <p>In a managed compute environment, Batch manages the capacity and instance types of the compute resources within the environment. This is based on the compute resource specification that you define or the <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html">launch template</a> that you specify when you create the compute environment. Either, you can choose to use EC2 On-Demand Instances and EC2 Spot Instances. Or, you can use Fargate and Fargate Spot capacity in your managed compute environment. You can optionally set a maximum price so that Spot Instances only launch when the Spot Instance price is less than a specified percentage of the On-Demand price.</p> <p>In an unmanaged compute environment, you can manage your own EC2 compute resources and have flexibility with how you configure your compute resources. For example, you can use custom AMIs. However, you must verify that each of your AMIs meet the Amazon ECS container instance AMI specification. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container_instance_AMIs.html">container instance AMIs</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. After you created your unmanaged compute environment, you can use the <a>DescribeComputeEnvironments</a> operation to find the Amazon ECS cluster that's associated with it. Then, launch your container instances into that Amazon ECS cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html">Launching an Amazon ECS container instance</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>Batch doesn't automatically upgrade the AMIs in a compute environment after it's created. For more information on how to update a compute environment's AMI, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> </note>

        Args:
            compute_environment_name: <p>The name for your compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>
            type: <p>The type of the compute environment: <code>MANAGED</code> or <code>UNMANAGED</code>. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">Compute Environments</a> in the <i>Batch User Guide</i>.</p>
            state: <p>The state of the compute environment. A compute environment must be created in the <code>ENABLED</code> state.</p> <p>If the state is <code>ENABLED</code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.</p> <p>If the state is <code>ENABLED</code>, then the Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.</p> <p>If the state is <code>DISABLED</code>, then the Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a <code>STARTING</code> or <code>RUNNING</code> state continue to progress normally. Managed compute environments in the <code>DISABLED</code> state don't scale out. </p> <note> <p>Compute environments in a <code>DISABLED</code> state may continue to incur billing charges, for example, if they have running instances due to jobs that are still executing or a non-zero <code>minvCpus</code> setting. To prevent additional charges, disable and delete the compute environment.</p> </note> <p>When an instance is idle, the instance scales down to the <code>minvCpus</code> value. However, the instance size doesn't change. For example, consider a <code>c5.8xlarge</code> instance with a <code>minvCpus</code> value of <code>4</code> and a <code>desiredvCpus</code> value of <code>36</code>. This instance doesn't scale down to a <code>c5.large</code> instance.</p>
            unmanagedv_cpus: <p>The maximum number of vCPUs for an unmanaged compute environment. This parameter is only used for fair-share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair-share job queue, no vCPU capacity is reserved.</p> <note> <p>This parameter is only supported when the <code>type</code> parameter is set to <code>UNMANAGED</code>.</p> </note>
            compute_resources: <p>Details about the compute resources managed by the compute environment. This parameter is required for managed compute environments. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">Compute Environments</a> in the <i>Batch User Guide</i>.</p>
            service_role: <p>The full Amazon Resource Name (ARN) of the IAM role that allows Batch to make calls to other Amazon Web Services services on your behalf. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html">Batch service IAM role</a> in the <i>Batch User Guide</i>.</p> <important> <p>If your account already created the Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the Batch service-linked role in your account.</p> <p>This automatic service-linked role creation only applies to <code>MANAGED</code> compute environments. For <code>UNMANAGED</code> compute environments, you must explicitly specify a <code>serviceRole</code>.</p> </important> <p>If your specified role has a path other than <code>/</code>, then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name <code>bar</code> has a path of <code>/foo/</code>, specify <code>/foo/bar</code> as the role name. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names">Friendly names and paths</a> in the <i>IAM User Guide</i>.</p> <note> <p>Depending on how you created your Batch service role, its ARN might contain the <code>service-role</code> path prefix. When you only specify the name of the service role, Batch assumes that your ARN doesn't use the <code>service-role</code> path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.</p> </note>
            tags: <p>The tags that you apply to the compute environment to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in <i>Amazon Web Services General Reference</i>.</p> <p>These tags can be updated or removed using the <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html">UntagResource</a> API operations. These tags don't propagate to the underlying compute resources.</p>
            eks_configuration: <p>The details for the Amazon EKS cluster that supports the compute environment.</p> <note> <p>To create a compute environment that uses EKS resources, the caller must have permissions to call <code>eks:DescribeCluster</code>. Additional Amazon EKS permissions are required for Batch to manage an access entry on the cluster; see <a href="https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html">Amazon EKS access entry authentication</a> in the <i>Batch User Guide</i>.</p> </note>
            context: <p>Reserved.</p>
            ecs_settings: <p>The Amazon ECS settings for the compute environment. These settings control CloudWatch Container Insights collection for the compute environment.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a managed EC2 compute environment
            This example creates a managed compute environment with specific C4 instance types that are launched on demand. The compute environment is called C4OnDemand.

            >>> client.create_compute_environment(compute_environment_name='C4OnDemand', state='ENABLED', type='MANAGED', compute_resources={'subnets': ['subnet-220c0e0a', 'subnet-1a95556d', 'subnet-978f6dce'], 'tags': {'Name': 'Batch Instance - C4OnDemand'}, 'desiredvCpus': 48, 'minvCpus': 0, 'instanceTypes': ['c4.large', 'c4.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge'], 'securityGroupIds': ['sg-cf5093b2'], 'instanceRole': 'ecsInstanceRole', 'maxvCpus': 128, 'type': 'EC2', 'ec2KeyPair': 'id_rsa'}, service_role='arn:aws:iam::012345678910:role/AWSBatchServiceRole')
            To create a managed EC2 Spot compute environment
            This example creates a managed compute environment with the M4 instance type that is launched when the Spot bid price is at or below 20% of the On-Demand price for the instance type. The compute environment is called M4Spot.

            >>> client.create_compute_environment(compute_environment_name='M4Spot', state='ENABLED', type='MANAGED', compute_resources={'subnets': ['subnet-220c0e0a', 'subnet-1a95556d', 'subnet-978f6dce'], 'type': 'SPOT', 'spotIamFleetRole': 'arn:aws:iam::012345678910:role/aws-ec2-spot-fleet-role', 'tags': {'Name': 'Batch Instance - M4Spot'}, 'desiredvCpus': 4, 'minvCpus': 0, 'instanceTypes': ['m4'], 'securityGroupIds': ['sg-cf5093b2'], 'instanceRole': 'ecsInstanceRole', 'maxvCpus': 128, 'bidPercentage': 20, 'ec2KeyPair': 'id_rsa'}, service_role='arn:aws:iam::012345678910:role/AWSBatchServiceRole')
            To create an ECS Managed Instances compute environment with capacity reservations
            This example creates an ECS Managed Instances compute environment that targets On-Demand Capacity Reservations for predictable capacity.

            >>> client.create_compute_environment(compute_environment_name='my-reserved-managed-instances-ce', state='ENABLED', type='MANAGED', compute_resources={'type': 'ECS_MANAGED_INSTANCES', 'maxvCpus': 512, 'managedInstancesProvider': {'infrastructureRoleArn': 'arn:aws:iam::123456789012:role/ecsInfrastructureRole', 'instanceLaunchTemplate': {'ec2InstanceProfileArn': 'arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile', 'networkConfiguration': {'subnets': ['subnet-abcde012', 'subnet-bcde012a'], 'securityGroups': ['sg-abcde012']}, 'instanceRequirements': {'allowedInstanceTypes': ['m5.xlarge', 'm5.2xlarge']}, 'capacityReservations': {'reservationGroupArn': 'arn:aws:ec2:us-east-1:123456789012:capacity-reservation-group/my-reservation-group', 'reservationPreference': 'RESERVATIONS_FIRST'}}}})
            To create an ECS Managed Instances compute environment
            This example creates a managed compute environment that uses ECS Managed Instances.

            >>> client.create_compute_environment(compute_environment_name='my-managed-instances-ce', state='ENABLED', type='MANAGED', compute_resources={'type': 'ECS_MANAGED_INSTANCES', 'maxvCpus': 256, 'managedInstancesProvider': {'infrastructureRoleArn': 'arn:aws:iam::123456789012:role/ecsInfrastructureRole', 'instanceLaunchTemplate': {'ec2InstanceProfileArn': 'arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile', 'networkConfiguration': {'subnets': ['subnet-abcde012', 'subnet-bcde012a'], 'securityGroups': ['sg-abcde012']}}}})
            To create an ECS Managed Instances Spot compute environment
            This example creates a Spot-backed ECS Managed Instances compute environment constrained to specific instance types.

            >>> client.create_compute_environment(compute_environment_name='my-spot-managed-instances-ce', state='ENABLED', type='MANAGED', compute_resources={'type': 'ECS_MANAGED_INSTANCES', 'maxvCpus': 1000, 'managedInstancesProvider': {'infrastructureRoleArn': 'arn:aws:iam::123456789012:role/ecsInfrastructureRole', 'instanceLaunchTemplate': {'ec2InstanceProfileArn': 'arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile', 'networkConfiguration': {'subnets': ['subnet-abcde012', 'subnet-bcde012a'], 'securityGroups': ['sg-abcde012']}, 'instanceRequirements': {'allowedInstanceTypes': ['m5.large', 'm5.xlarge', 'm6i.large', 'm6i.xlarge']}, 'capacityOptionType': 'SPOT'}}})
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.create_compute_environment_request.CreateComputeEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_batch.types.create_compute_environment_response.CreateComputeEnvironmentResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.create_compute_environment

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.create_compute_environment.create_compute_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.create_compute_environment_request.CreateComputeEnvironmentRequest = {}
        if compute_environment_name is not None:
            input_["compute_environment_name"] = compute_environment_name
        if type is not None:
            input_["type"] = type
        if state is not None:
            input_["state"] = state
        if unmanagedv_cpus is not None:
            input_["unmanagedv_cpus"] = unmanagedv_cpus
        if compute_resources is not None:
            input_["compute_resources"] = compute_resources
        if service_role is not None:
            input_["service_role"] = service_role
        if tags is not None:
            input_["tags"] = tags
        if eks_configuration is not None:
            input_["eks_configuration"] = eks_configuration
        if context is not None:
            input_["context"] = context
        if ecs_settings is not None:
            input_["ecs_settings"] = ecs_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_consumable_resource(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        consumable_resource_name: Optional["capo_batch.types.string.String"] = None,
        total_quantity: Optional["capo_batch.types.long.Long"] = None,
        resource_type: Optional["capo_batch.types.string.String"] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
    ) -> "capo_batch.types.create_consumable_resource_response.CreateConsumableResourceResponse":
        """<p>Creates an Batch consumable resource.</p>

        Args:
            consumable_resource_name: <p>The name of the consumable resource. Must be unique.</p>
            total_quantity: <p>The total amount of the consumable resource that is available. Must be non-negative.</p>
            resource_type: <p>Indicates whether the resource is available to be re-used after a job completes. Can be one of: </p> <ul> <li> <p> <code>REPLENISHABLE</code> (default)</p> </li> <li> <p> <code>NON_REPLENISHABLE</code> </p> </li> </ul>
            tags: <p>The tags that you apply to the consumable resource to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging your Batch resources</a>.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a consumable resource
            Creates a Batch consumable resource.

            >>> client.create_consumable_resource(consumable_resource_name='myConsumableResource', total_quantity=123, resource_type='REPLENISHABLE', tags={'Department': 'Engineering', 'User': 'JaneDoe'})
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.create_consumable_resource_request.CreateConsumableResourceRequest]",
        ) -> OperationResponse[
            "capo_batch.types.create_consumable_resource_response.CreateConsumableResourceResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.create_consumable_resource

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.create_consumable_resource.create_consumable_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.create_consumable_resource_request.CreateConsumableResourceRequest = {}
        if consumable_resource_name is not None:
            input_["consumable_resource_name"] = consumable_resource_name
        if total_quantity is not None:
            input_["total_quantity"] = total_quantity
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_job_queue(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue_name: Optional["capo_batch.types.string.String"] = None,
        state: Optional["capo_batch.types.jq_state.JQState"] = None,
        scheduling_policy_arn: Optional["capo_batch.types.string.String"] = None,
        priority: Optional["capo_batch.types.integer.Integer"] = None,
        compute_environment_order: Optional[
            "capo_batch.types.compute_environment_orders.ComputeEnvironmentOrders"
        ] = None,
        service_environment_order: Optional[
            "capo_batch.types.service_environment_orders.ServiceEnvironmentOrders"
        ] = None,
        job_queue_type: Optional["capo_batch.types.job_queue_type.JobQueueType"] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
        job_state_time_limit_actions: Optional[
            "capo_batch.types.job_state_time_limit_actions.JobStateTimeLimitActions"
        ] = None,
    ) -> "capo_batch.types.create_job_queue_response.CreateJobQueueResponse":
        """<p>Creates an Batch job queue. When you create a job queue, you associate one or more compute environments to the queue and assign an order of preference for the compute environments.</p> <p>You also set a priority to the job queue that determines the order that the Batch scheduler places jobs onto its associated compute environments. For example, if a compute environment is associated with more than one job queue, the job queue with a higher priority is given preference for scheduling jobs to that compute environment.</p>

        Args:
            job_queue_name: <p>The name of the job queue. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>
            state: <p>The state of the job queue. If the job queue state is <code>ENABLED</code>, it is able to accept jobs. If the job queue state is <code>DISABLED</code>, new jobs can't be added to the queue, but jobs already in the queue can finish.</p>
            scheduling_policy_arn: <p>The Amazon Resource Name (ARN) of the fair-share scheduling policy. Job queues that don't have a fair-share scheduling policy are scheduled in a first-in, first-out (FIFO) model. After a job queue has a fair-share scheduling policy, it can be replaced but can't be removed.</p> <p>The format is <code>aws:<i>Partition</i>:batch:<i>Region</i>:<i>Account</i>:scheduling-policy/<i>Name</i> </code>.</p> <p>An example is <code>aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy</code>.</p> <p>A job queue without a fair-share scheduling policy is scheduled as a FIFO job queue and can't have a fair-share scheduling policy added. Jobs queues with a fair-share scheduling policy can have a maximum of 500 active share identifiers. When the limit has been reached, submissions of any jobs that add a new share identifier fail.</p>
            priority: <p>The priority of the job queue. Job queues with a higher priority (or a higher integer value for the <code>priority</code> parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of <code>10</code> is given scheduling preference over a job queue with a priority value of <code>1</code>. All of the compute environments must be either EC2 (<code>EC2</code> or <code>SPOT</code>) or Fargate (<code>FARGATE</code> or <code>FARGATE_SPOT</code>); EC2 and Fargate compute environments can't be mixed.</p>
            compute_environment_order: <p>The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the <code>VALID</code> state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 (<code>EC2</code> or <code>SPOT</code>) or Fargate (<code>FARGATE</code> or <code>FARGATE_SPOT</code>); EC2 and Fargate compute environments can't be mixed.</p> <note> <p>All compute environments that are associated with a job queue must share the same architecture. Batch doesn't support mixing compute environment architecture types in a single job queue.</p> </note>
            service_environment_order: <p>A list of service environments that this job queue can use to allocate jobs. All serviceEnvironments must have the same type. A job queue can't have both a serviceEnvironmentOrder and a computeEnvironmentOrder field.</p>
            job_queue_type: <p>The type of job queue. For service jobs that run on SageMaker Training, this value is <code>SAGEMAKER_TRAINING</code>. For regular container jobs, this value is <code>EKS</code>, <code>ECS</code>, or <code>ECS_FARGATE</code> depending on the compute environment.</p>
            tags: <p>The tags that you apply to the job queue to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging your Batch resources</a> in <i>Batch User Guide</i>.</p>
            job_state_time_limit_actions: <p>The set of actions that Batch performs on jobs that remain at the head of the job queue in the specified state longer than specified times. Batch will perform each action after <code>maxTimeSeconds</code> has passed. (<b>Note</b>: The minimum value for maxTimeSeconds is 600 (10 minutes) and its maximum value is 86,400 (24 hours).)</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a job queue with a single compute environment
            This example creates a job queue called LowPriority that uses the M4Spot compute environment.

            >>> client.create_job_queue(priority=1, state='ENABLED', compute_environment_order=[{'computeEnvironment': 'M4Spot', 'order': 1}], job_queue_name='LowPriority')
            To create a job queue with an ECS Managed Instances compute environment
            This example creates a job queue called ManagedInstancesQueue that uses an ECS Managed Instances compute environment.

            >>> client.create_job_queue(priority=10, state='ENABLED', compute_environment_order=[{'computeEnvironment': 'my-managed-instances-ce', 'order': 1}], job_queue_name='ManagedInstancesQueue')
            To create a job queue with multiple compute environments
            This example creates a job queue called HighPriority that uses the C4OnDemand compute environment with an order of 1 and the M4Spot compute environment with an order of 2.

            >>> client.create_job_queue(priority=10, state='ENABLED', compute_environment_order=[{'computeEnvironment': 'C4OnDemand', 'order': 1}, {'computeEnvironment': 'M4Spot', 'order': 2}], job_queue_name='HighPriority')
            To create a job queue with On-Demand and Spot ECS Managed Instances compute environments
            This example creates a job queue that uses both On-Demand and Spot ECS Managed Instances compute environments. On-Demand environments must be ordered before Spot environments.

            >>> client.create_job_queue(priority=5, state='ENABLED', compute_environment_order=[{'computeEnvironment': 'my-managed-instances-ce', 'order': 1}, {'computeEnvironment': 'my-spot-managed-instances-ce', 'order': 2}], job_queue_name='ManagedInstancesMixedQueue')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.create_job_queue_request.CreateJobQueueRequest]",
        ) -> OperationResponse[
            "capo_batch.types.create_job_queue_response.CreateJobQueueResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.create_job_queue

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.create_job_queue.create_job_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.create_job_queue_request.CreateJobQueueRequest = {}
        if job_queue_name is not None:
            input_["job_queue_name"] = job_queue_name
        if state is not None:
            input_["state"] = state
        if scheduling_policy_arn is not None:
            input_["scheduling_policy_arn"] = scheduling_policy_arn
        if priority is not None:
            input_["priority"] = priority
        if compute_environment_order is not None:
            input_["compute_environment_order"] = compute_environment_order
        if service_environment_order is not None:
            input_["service_environment_order"] = service_environment_order
        if job_queue_type is not None:
            input_["job_queue_type"] = job_queue_type
        if tags is not None:
            input_["tags"] = tags
        if job_state_time_limit_actions is not None:
            input_["job_state_time_limit_actions"] = job_state_time_limit_actions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_quota_share(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        quota_share_name: Optional["capo_batch.types.string.String"] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        capacity_limits: Optional[
            "capo_batch.types.quota_share_capacity_limits.QuotaShareCapacityLimits"
        ] = None,
        resource_sharing_configuration: Optional[
            "capo_batch.types.quota_share_resource_sharing_configuration.QuotaShareResourceSharingConfiguration"
        ] = None,
        preemption_configuration: Optional[
            "capo_batch.types.quota_share_preemption_configuration.QuotaSharePreemptionConfiguration"
        ] = None,
        state: Optional["capo_batch.types.quota_share_state.QuotaShareState"] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
    ) -> "capo_batch.types.create_quota_share_response.CreateQuotaShareResponse":
        """<p>Creates an Batch quota share. Each quota share operates as a virtual queue with a configured compute capacity, resource sharing strategy, and borrow limits. </p>

        Args:
            quota_share_name: <p>The name of the quota share. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>
            job_queue: <p>The Batch job queue associated with the quota share. This can be the job queue name or ARN. A job queue must be in the <code>VALID</code> state before you can associate it with a quota share.</p>
            capacity_limits: <p>A list that specifies the quantity and type of compute capacity allocated to the quota share. </p>
            resource_sharing_configuration: <p>Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.</p>
            preemption_configuration: <p>Specifies the preemption behavior for jobs in a quota share.</p>
            state: <p>The state of the quota share. If the quota share is <code>ENABLED</code>, it is able to accept jobs. If the quota share is <code>DISABLED</code>, new jobs won't be accepted but jobs already submitted can finish. The default state is <code>ENABLED</code>.</p>
            tags: <p>The tags that you apply to the quota share to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging your Batch resources</a> in <i>Batch User Guide</i>.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.create_quota_share_request.CreateQuotaShareRequest]",
        ) -> OperationResponse[
            "capo_batch.types.create_quota_share_response.CreateQuotaShareResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.create_quota_share

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.create_quota_share.create_quota_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.create_quota_share_request.CreateQuotaShareRequest = {}
        if quota_share_name is not None:
            input_["quota_share_name"] = quota_share_name
        if job_queue is not None:
            input_["job_queue"] = job_queue
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits
        if resource_sharing_configuration is not None:
            input_["resource_sharing_configuration"] = resource_sharing_configuration
        if preemption_configuration is not None:
            input_["preemption_configuration"] = preemption_configuration
        if state is not None:
            input_["state"] = state
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_scheduling_policy(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        name: Optional["capo_batch.types.string.String"] = None,
        quota_share_policy: Optional[
            "capo_batch.types.quota_share_policy.QuotaSharePolicy"
        ] = None,
        fairshare_policy: Optional[
            "capo_batch.types.fairshare_policy.FairsharePolicy"
        ] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
    ) -> "capo_batch.types.create_scheduling_policy_response.CreateSchedulingPolicyResponse":
        """<p>Creates an Batch scheduling policy.</p>

        Args:
            name: <p>The name of the fair-share scheduling policy. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>
            quota_share_policy: <p>The quota share scheduling policy details. Only one of fairsharePolicy or quotaSharePolicy can be set. Once set, this policy type cannot be removed or changed to a fairSharePolicy.</p>
            fairshare_policy: <p>The fair-share scheduling policy details. Only one of fairsharePolicy or quotaSharePolicy can be set. Once set, this policy type cannot be removed or changed to a quotaSharePolicy.</p>
            tags: <p>The tags that you apply to the scheduling policy to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in <i>Amazon Web Services General Reference</i>.</p> <p>These tags can be updated or removed using the <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html">UntagResource</a> API operations.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.create_scheduling_policy_request.CreateSchedulingPolicyRequest]",
        ) -> OperationResponse[
            "capo_batch.types.create_scheduling_policy_response.CreateSchedulingPolicyResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.create_scheduling_policy

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.create_scheduling_policy.create_scheduling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.create_scheduling_policy_request.CreateSchedulingPolicyRequest = {}
        if name is not None:
            input_["name"] = name
        if quota_share_policy is not None:
            input_["quota_share_policy"] = quota_share_policy
        if fairshare_policy is not None:
            input_["fairshare_policy"] = fairshare_policy
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_service_environment(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        service_environment_name: Optional["capo_batch.types.string.String"] = None,
        service_environment_type: Optional[
            "capo_batch.types.service_environment_type.ServiceEnvironmentType"
        ] = None,
        state: Optional[
            "capo_batch.types.service_environment_state.ServiceEnvironmentState"
        ] = None,
        capacity_limits: Optional[
            "capo_batch.types.capacity_limits.CapacityLimits"
        ] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
    ) -> "capo_batch.types.create_service_environment_response.CreateServiceEnvironmentResponse":
        """<p>Creates a service environment for running service jobs. Service environments define capacity limits for specific service types such as SageMaker Training jobs.</p>

        Args:
            service_environment_name: <p>The name for the service environment. It can be up to 128 characters long and can contain letters, numbers, hyphens (-), and underscores (_).</p>
            service_environment_type: <p>The type of service environment. For SageMaker Training jobs, specify <code>SAGEMAKER_TRAINING</code>.</p>
            state: <p>The state of the service environment. Valid values are <code>ENABLED</code> and <code>DISABLED</code>. The default value is <code>ENABLED</code>.</p>
            capacity_limits: <p>The capacity limits for the service environment. The number of instances a job consumes is the total number of instances requested in the submit training job request resource configuration.</p>
            tags: <p>The tags that you apply to the service environment to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging your Batch resources</a>.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.create_service_environment_request.CreateServiceEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_batch.types.create_service_environment_response.CreateServiceEnvironmentResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.create_service_environment

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.create_service_environment.create_service_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.create_service_environment_request.CreateServiceEnvironmentRequest = {}
        if service_environment_name is not None:
            input_["service_environment_name"] = service_environment_name
        if service_environment_type is not None:
            input_["service_environment_type"] = service_environment_type
        if state is not None:
            input_["state"] = state
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_compute_environment(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        compute_environment: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.delete_compute_environment_response.DeleteComputeEnvironmentResponse":
        """<p>Deletes an Batch compute environment.</p> <p>Before you can delete a compute environment, you must set its state to <code>DISABLED</code> with the <a>UpdateComputeEnvironment</a> API operation and disassociate it from any job queues with the <a>UpdateJobQueue</a> API operation. Compute environments that use Fargate resources must terminate all active jobs on that compute environment before deleting the compute environment. If this isn't done, the compute environment enters an invalid state.</p>

        Args:
            compute_environment: <p>The name or Amazon Resource Name (ARN) of the compute environment to delete.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a compute environment
            This example deletes the P2OnDemand compute environment.

            >>> client.delete_compute_environment(compute_environment='P2OnDemand')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.delete_compute_environment_request.DeleteComputeEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_batch.types.delete_compute_environment_response.DeleteComputeEnvironmentResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.delete_compute_environment

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.delete_compute_environment.delete_compute_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.delete_compute_environment_request.DeleteComputeEnvironmentRequest = {}
        if compute_environment is not None:
            input_["compute_environment"] = compute_environment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_consumable_resource(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        consumable_resource: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.delete_consumable_resource_response.DeleteConsumableResourceResponse":
        """<p>Deletes the specified consumable resource.</p>

        Args:
            consumable_resource: <p>The name or ARN of the consumable resource that will be deleted.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a consumable resource
            Deletes the specified consumable resource.

            >>> client.delete_consumable_resource(consumable_resource='myConsumableResource')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.delete_consumable_resource_request.DeleteConsumableResourceRequest]",
        ) -> OperationResponse[
            "capo_batch.types.delete_consumable_resource_response.DeleteConsumableResourceResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.delete_consumable_resource

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.delete_consumable_resource.delete_consumable_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.delete_consumable_resource_request.DeleteConsumableResourceRequest = {}
        if consumable_resource is not None:
            input_["consumable_resource"] = consumable_resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_job_queue(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.delete_job_queue_response.DeleteJobQueueResponse":
        """<p>Deletes the specified job queue. You must first disable submissions for a queue with the <a>UpdateJobQueue</a> operation. All jobs in the queue are eventually terminated when you delete a job queue.</p> <p>It's not necessary to disassociate compute environments from a queue before submitting a <code>DeleteJobQueue</code> request.</p>

        Args:
            job_queue: <p>The short name or full Amazon Resource Name (ARN) of the queue to delete.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a job queue
            This example deletes the GPGPU job queue.

            >>> client.delete_job_queue(job_queue='GPGPU')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.delete_job_queue_request.DeleteJobQueueRequest]",
        ) -> OperationResponse[
            "capo_batch.types.delete_job_queue_response.DeleteJobQueueResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.delete_job_queue

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.delete_job_queue.delete_job_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.delete_job_queue_request.DeleteJobQueueRequest = {}
        if job_queue is not None:
            input_["job_queue"] = job_queue

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_quota_share(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        quota_share_arn: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.delete_quota_share_response.DeleteQuotaShareResponse":
        """<p>Deletes the specified quota share. You must first disable submissions for the share by updating the state to <code>DISABLED</code> using the <a>UpdateQuotaShare</a> operation. All jobs in the share are eventually terminated when you delete a quota share.</p>

        Args:
            quota_share_arn: <p>The Amazon Resource Name (ARN) of the quota share.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.delete_quota_share_request.DeleteQuotaShareRequest]",
        ) -> OperationResponse[
            "capo_batch.types.delete_quota_share_response.DeleteQuotaShareResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.delete_quota_share

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.delete_quota_share.delete_quota_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.delete_quota_share_request.DeleteQuotaShareRequest = {}
        if quota_share_arn is not None:
            input_["quota_share_arn"] = quota_share_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_scheduling_policy(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        arn: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.delete_scheduling_policy_response.DeleteSchedulingPolicyResponse":
        """<p>Deletes the specified scheduling policy.</p> <p>You can't delete a scheduling policy that's used in any job queues.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the scheduling policy to delete.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.delete_scheduling_policy_request.DeleteSchedulingPolicyRequest]",
        ) -> OperationResponse[
            "capo_batch.types.delete_scheduling_policy_response.DeleteSchedulingPolicyResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.delete_scheduling_policy

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.delete_scheduling_policy.delete_scheduling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.delete_scheduling_policy_request.DeleteSchedulingPolicyRequest = {}
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_environment(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        service_environment: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.delete_service_environment_response.DeleteServiceEnvironmentResponse":
        """<p>Deletes a Service environment. Before you can delete a service environment, you must first set its state to <code>DISABLED</code> with the <code>UpdateServiceEnvironment</code> API operation and disassociate it from any job queues with the <code>UpdateJobQueue</code> API operation.</p>

        Args:
            service_environment: <p>The name or ARN of the service environment to delete.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.delete_service_environment_request.DeleteServiceEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_batch.types.delete_service_environment_response.DeleteServiceEnvironmentResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.delete_service_environment

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.delete_service_environment.delete_service_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.delete_service_environment_request.DeleteServiceEnvironmentRequest = {}
        if service_environment is not None:
            input_["service_environment"] = service_environment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_job_definition(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_definition: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.deregister_job_definition_response.DeregisterJobDefinitionResponse":
        """<p>Deregisters an Batch job definition. Job definitions are permanently deleted after 180 days.</p>

        Args:
            job_definition: <p>The name and revision (<code>name:revision</code>) or full Amazon Resource Name (ARN) of the job definition to deregister.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deregister a job definition
            This example deregisters a job definition called sleep10.

            >>> client.deregister_job_definition(job_definition='sleep10')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.deregister_job_definition_request.DeregisterJobDefinitionRequest]",
        ) -> OperationResponse[
            "capo_batch.types.deregister_job_definition_response.DeregisterJobDefinitionResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.deregister_job_definition

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.deregister_job_definition.deregister_job_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.deregister_job_definition_request.DeregisterJobDefinitionRequest = {}
        if job_definition is not None:
            input_["job_definition"] = job_definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_compute_environments(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        compute_environments: Optional[
            "capo_batch.types.string_list.StringList"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.describe_compute_environments_response.DescribeComputeEnvironmentsResponse":
        """<p>Describes one or more of your compute environments.</p> <p>If you're using an unmanaged compute environment, you can use the <code>DescribeComputeEnvironment</code> operation to determine the <code>ecsClusterArn</code> that you launch your Amazon ECS container instances into.</p>

        Args:
            compute_environments: <p>A list of up to 100 compute environment names or full Amazon Resource Name (ARN) entries.</p>
            max_results: <p>The maximum number of cluster results returned by <code>DescribeComputeEnvironments</code> in paginated output. When this parameter is used, <code>DescribeComputeEnvironments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeComputeEnvironments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>DescribeComputeEnvironments</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeComputeEnvironments</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a compute environment
            This example describes the P2OnDemand compute environment.

            >>> client.describe_compute_environments(compute_environments=['P2OnDemand'])
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.describe_compute_environments_request.DescribeComputeEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_batch.types.describe_compute_environments_response.DescribeComputeEnvironmentsResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.describe_compute_environments

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.describe_compute_environments.describe_compute_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.describe_compute_environments_request.DescribeComputeEnvironmentsRequest = {}
        if compute_environments is not None:
            input_["compute_environments"] = compute_environments
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

    def iter_describe_compute_environments(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        compute_environments: Optional[
            "capo_batch.types.string_list.StringList"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> (
        "Iterator[capo_batch.types.compute_environment_detail.ComputeEnvironmentDetail]"
    ):
        _token = next_token
        while True:
            _response = self.describe_compute_environments(
                config_overrides=config_overrides,
                compute_environments=compute_environments,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("compute_environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_consumable_resource(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        consumable_resource: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.describe_consumable_resource_response.DescribeConsumableResourceResponse":
        """<p>Returns a description of the specified consumable resource.</p>

        Args:
            consumable_resource: <p>The name or ARN of the consumable resource whose description will be returned.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a description of a consumable resource
            Returns a description of the specified consumable resource.

            >>> client.describe_consumable_resource(consumable_resource='myConsumableResource')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.describe_consumable_resource_request.DescribeConsumableResourceRequest]",
        ) -> OperationResponse[
            "capo_batch.types.describe_consumable_resource_response.DescribeConsumableResourceResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.describe_consumable_resource

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.describe_consumable_resource.describe_consumable_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.describe_consumable_resource_request.DescribeConsumableResourceRequest = {}
        if consumable_resource is not None:
            input_["consumable_resource"] = consumable_resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_job_definitions(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_definitions: Optional["capo_batch.types.string_list.StringList"] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        job_definition_name: Optional["capo_batch.types.string.String"] = None,
        status: Optional["capo_batch.types.string.String"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.describe_job_definitions_response.DescribeJobDefinitionsResponse":
        """<p>Describes a list of job definitions. You can specify a <code>status</code> (such as <code>ACTIVE</code>) to only return job definitions that match that status.</p>

        Args:
            job_definitions: <p>A list of up to 100 job definitions. Each entry in the list can either be an ARN in the format <code>arn:aws:batch:${Region}:${Account}:job-definition/${JobDefinitionName}:${Revision}</code> or a short version using the form <code>${JobDefinitionName}:${Revision}</code>. This parameter can't be used with other parameters.</p>
            max_results: <p>The maximum number of results returned by <code>DescribeJobDefinitions</code> in paginated output. When this parameter is used, <code>DescribeJobDefinitions</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeJobDefinitions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>DescribeJobDefinitions</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            job_definition_name: <p>The name of the job definition to describe.</p>
            status: <p>The status used to filter job definitions.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeJobDefinitions</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe active job definitions
            This example describes all of your active job definitions.

            >>> client.describe_job_definitions(status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.describe_job_definitions_request.DescribeJobDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_batch.types.describe_job_definitions_response.DescribeJobDefinitionsResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.describe_job_definitions

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.describe_job_definitions.describe_job_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.describe_job_definitions_request.DescribeJobDefinitionsRequest = {}
        if job_definitions is not None:
            input_["job_definitions"] = job_definitions
        if max_results is not None:
            input_["max_results"] = max_results
        if job_definition_name is not None:
            input_["job_definition_name"] = job_definition_name
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_job_definitions(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_definitions: Optional["capo_batch.types.string_list.StringList"] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        job_definition_name: Optional["capo_batch.types.string.String"] = None,
        status: Optional["capo_batch.types.string.String"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "Iterator[capo_batch.types.job_definition.JobDefinition]":
        _token = next_token
        while True:
            _response = self.describe_job_definitions(
                config_overrides=config_overrides,
                job_definitions=job_definitions,
                max_results=max_results,
                job_definition_name=job_definition_name,
                status=status,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_job_queues(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queues: Optional["capo_batch.types.string_list.StringList"] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.describe_job_queues_response.DescribeJobQueuesResponse":
        """<p>Describes one or more of your job queues.</p>

        Args:
            job_queues: <p>A list of up to 100 queue names or full queue Amazon Resource Name (ARN) entries.</p>
            max_results: <p>The maximum number of results returned by <code>DescribeJobQueues</code> in paginated output. When this parameter is used, <code>DescribeJobQueues</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeJobQueues</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>DescribeJobQueues</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeJobQueues</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a job queue
            This example describes the HighPriority job queue.

            >>> client.describe_job_queues(job_queues=['HighPriority'])
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.describe_job_queues_request.DescribeJobQueuesRequest]",
        ) -> OperationResponse[
            "capo_batch.types.describe_job_queues_response.DescribeJobQueuesResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.describe_job_queues

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.describe_job_queues.describe_job_queues(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.describe_job_queues_request.DescribeJobQueuesRequest = {}
        if job_queues is not None:
            input_["job_queues"] = job_queues
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

    def iter_describe_job_queues(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queues: Optional["capo_batch.types.string_list.StringList"] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "Iterator[capo_batch.types.job_queue_detail.JobQueueDetail]":
        _token = next_token
        while True:
            _response = self.describe_job_queues(
                config_overrides=config_overrides,
                job_queues=job_queues,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_queues",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_jobs(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        jobs: Optional["capo_batch.types.string_list.StringList"] = None,
    ) -> "capo_batch.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Describes a list of Batch jobs.</p>

        Args:
            jobs: <p>A list of up to 100 job IDs.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a specific job
            This example describes a job with the specified job ID.

            >>> client.describe_jobs(jobs=['24fa2d7a-64c4-49d2-8b47-f8da4fbde8e9'])
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> OperationResponse[
            "capo_batch.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.describe_jobs

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.describe_jobs.describe_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.describe_jobs_request.DescribeJobsRequest = {}
        if jobs is not None:
            input_["jobs"] = jobs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_quota_share(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        quota_share_arn: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.describe_quota_share_response.DescribeQuotaShareResponse":
        """<p>Returns a description of the specified quota share.</p>

        Args:
            quota_share_arn: <p>The Amazon Resource Name (ARN) of the quota share.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.describe_quota_share_request.DescribeQuotaShareRequest]",
        ) -> OperationResponse[
            "capo_batch.types.describe_quota_share_response.DescribeQuotaShareResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.describe_quota_share

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.describe_quota_share.describe_quota_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.describe_quota_share_request.DescribeQuotaShareRequest = {}
        if quota_share_arn is not None:
            input_["quota_share_arn"] = quota_share_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_scheduling_policies(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        arns: Optional["capo_batch.types.string_list.StringList"] = None,
    ) -> "capo_batch.types.describe_scheduling_policies_response.DescribeSchedulingPoliciesResponse":
        """<p>Describes one or more of your scheduling policies.</p>

        Args:
            arns: <p>A list of up to 100 scheduling policy Amazon Resource Name (ARN) entries.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.describe_scheduling_policies_request.DescribeSchedulingPoliciesRequest]",
        ) -> OperationResponse[
            "capo_batch.types.describe_scheduling_policies_response.DescribeSchedulingPoliciesResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.describe_scheduling_policies

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.describe_scheduling_policies.describe_scheduling_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.describe_scheduling_policies_request.DescribeSchedulingPoliciesRequest = {}
        if arns is not None:
            input_["arns"] = arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_service_environments(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        service_environments: Optional[
            "capo_batch.types.string_list.StringList"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.describe_service_environments_response.DescribeServiceEnvironmentsResponse":
        """<p>Describes one or more of your service environments.</p>

        Args:
            service_environments: <p>An array of service environment names or ARN entries.</p>
            max_results: <p>The maximum number of results returned by <code>DescribeServiceEnvironments</code> in paginated output. When this parameter is used, <code>DescribeServiceEnvironments</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeServiceEnvironments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>DescribeServiceEnvironments</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeServiceEnvironments</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.describe_service_environments_request.DescribeServiceEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_batch.types.describe_service_environments_response.DescribeServiceEnvironmentsResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.describe_service_environments

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.describe_service_environments.describe_service_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.describe_service_environments_request.DescribeServiceEnvironmentsRequest = {}
        if service_environments is not None:
            input_["service_environments"] = service_environments
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

    def iter_describe_service_environments(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        service_environments: Optional[
            "capo_batch.types.string_list.StringList"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> (
        "Iterator[capo_batch.types.service_environment_detail.ServiceEnvironmentDetail]"
    ):
        _token = next_token
        while True:
            _response = self.describe_service_environments(
                config_overrides=config_overrides,
                service_environments=service_environments,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_service_job(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_id: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.describe_service_job_response.DescribeServiceJobResponse":
        """<p>The details of a service job.</p>

        Args:
            job_id: <p>The job ID for the service job to describe.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.describe_service_job_request.DescribeServiceJobRequest]",
        ) -> OperationResponse[
            "capo_batch.types.describe_service_job_response.DescribeServiceJobResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.describe_service_job

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.describe_service_job.describe_service_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.describe_service_job_request.DescribeServiceJobRequest = {}
        if job_id is not None:
            input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_job_queue_snapshot(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.get_job_queue_snapshot_response.GetJobQueueSnapshotResponse":
        """<p>Provides a snapshot of job queue state, including ordering of <code>RUNNABLE</code> jobs, as well as capacity utilization for already dispatched jobs. The first 100 <code>RUNNABLE</code> jobs in the job queue are listed in order of dispatch. For job queues with an attached quota-share policy, the first <code>RUNNABLE</code> job in each quota share is also listed. Capacity utilization for the job queue is provided, as well as break downs by share for job queues with attached fair-share or quota-share scheduling policies.</p>

        Args:
            job_queue: <p>The job queue’s name or full queue Amazon Resource Name (ARN).</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.get_job_queue_snapshot_request.GetJobQueueSnapshotRequest]",
        ) -> OperationResponse[
            "capo_batch.types.get_job_queue_snapshot_response.GetJobQueueSnapshotResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.get_job_queue_snapshot

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.get_job_queue_snapshot.get_job_queue_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.get_job_queue_snapshot_request.GetJobQueueSnapshotRequest = {}
        if job_queue is not None:
            input_["job_queue"] = job_queue

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_consumable_resources(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        filters: Optional[
            "capo_batch.types.list_consumable_resources_filter_list.ListConsumableResourcesFilterList"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.list_consumable_resources_response.ListConsumableResourcesResponse":
        """<p>Returns a list of Batch consumable resources.</p>

        Args:
            filters: <p>The filters to apply to the consumable resource list query. If used, only those consumable resources that match the filter are listed. Filter names and values can be:</p> <ul> <li> <p>name: <code>CONSUMABLE_RESOURCE_NAME </code> </p> <p>values: case-insensitive matches for the consumable resource name. If a filter value ends with an asterisk (*), it matches any consumable resource name that begins with the string before the '*'.</p> </li> </ul>
            max_results: <p>The maximum number of results returned by <code>ListConsumableResources</code> in paginated output. When this parameter is used, <code>ListConsumableResources</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListConsumableResources</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListConsumableResources</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListConsumableResources</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of a consumable resources
            Returns a list of the consumable resources for your account.

            >>> client.list_consumable_resources(filters=[{'name': 'CONSUMABLE_RESOURCE_NAME', 'values': ['my*']}], max_results=123)
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.list_consumable_resources_request.ListConsumableResourcesRequest]",
        ) -> OperationResponse[
            "capo_batch.types.list_consumable_resources_response.ListConsumableResourcesResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.list_consumable_resources

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.list_consumable_resources.list_consumable_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.list_consumable_resources_request.ListConsumableResourcesRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_consumable_resources(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        filters: Optional[
            "capo_batch.types.list_consumable_resources_filter_list.ListConsumableResourcesFilterList"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "Iterator[capo_batch.types.consumable_resource_summary.ConsumableResourceSummary]":
        _token = next_token
        while True:
            _response = self.list_consumable_resources(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("consumable_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_jobs(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        array_job_id: Optional["capo_batch.types.string.String"] = None,
        multi_node_job_id: Optional["capo_batch.types.string.String"] = None,
        job_status: Optional["capo_batch.types.job_status.JobStatus"] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
        filters: Optional[
            "capo_batch.types.list_jobs_filter_list.ListJobsFilterList"
        ] = None,
    ) -> "capo_batch.types.list_jobs_response.ListJobsResponse":
        """<p>Returns a list of Batch jobs.</p> <p>You must specify only one of the following items:</p> <ul> <li> <p>A job queue ID to return a list of jobs in that job queue</p> </li> <li> <p>A multi-node parallel job ID to return a list of nodes for that job</p> </li> <li> <p>An array job ID to return a list of the children for that job</p> </li> </ul>

        Args:
            job_queue: <p>The name or full Amazon Resource Name (ARN) of the job queue used to list jobs.</p>
            array_job_id: <p>The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.</p>
            multi_node_job_id: <p>The job ID for a multi-node parallel job. Specifying a multi-node parallel job ID with this parameter lists all nodes that are associated with the specified job.</p>
            job_status: <p>The job status used to filter jobs in the specified queue. If the <code>filters</code> parameter is specified, the <code>jobStatus</code> parameter is ignored and jobs with any status are returned. The exception is the <code>SHARE_IDENTIFIER</code> filter and <code>jobStatus</code> can be used together. If you don't specify a status, only <code>RUNNING</code> jobs are returned.</p> <note> <p>Array job parents are updated to <code>PENDING</code> when any child job is updated to <code>RUNNABLE</code> and remain in <code>PENDING</code> status while child jobs are running. To view these jobs, filter by <code>PENDING</code> status until all child jobs reach a terminal state.</p> </note>
            max_results: <p>The maximum number of results returned by <code>ListJobs</code> in a paginated output. When this parameter is used, <code>ListJobs</code> returns up to <code>maxResults</code> results in a single page and a <code>nextToken</code> response element, if applicable. The remaining results of the initial request can be seen by sending another <code>ListJobs</code> request with the returned <code>nextToken</code> value.</p> <p>The following outlines key parameters and limitations:</p> <ul> <li> <p>The minimum value is 1. </p> </li> <li> <p>When <code>--job-status</code> is used, Batch returns up to 1000 values. </p> </li> <li> <p>When <code>--filters</code> is used, Batch returns up to 100 values.</p> </li> <li> <p>If neither parameter is used, then <code>ListJobs</code> returns up to 1000 results (jobs that are in the <code>RUNNING</code> status) and a <code>nextToken</code> value, if applicable.</p> </li> </ul>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListJobs</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            filters: <p>The filter to apply to the query. Only one filter can be used at a time. When the filter is used, <code>jobStatus</code> is ignored with the exception that <code>SHARE_IDENTIFIER</code> and <code>jobStatus</code> can be used together. The filter doesn't apply to child jobs in an array or multi-node parallel (MNP) jobs. The results are sorted by the <code>createdAt</code> field, with the most recent jobs being first.</p> <note> <p>The <code>SHARE_IDENTIFIER</code> filter and the <code>jobStatus</code> field can be used together to filter results.</p> </note> <dl> <dt>JOB_NAME</dt> <dd> <p>The value of the filter is a case-insensitive match for the job name. If the value ends with an asterisk (*), the filter matches any job name that begins with the string before the '*'. This corresponds to the <code>jobName</code> value. For example, <code>test1</code> matches both <code>Test1</code> and <code>test1</code>, and <code>test1*</code> matches both <code>test1</code> and <code>Test10</code>. When the <code>JOB_NAME</code> filter is used, the results are grouped by the job name and version.</p> </dd> <dt>JOB_DEFINITION</dt> <dd> <p>The value for the filter is the name or Amazon Resource Name (ARN) of the job definition. This corresponds to the <code>jobDefinition</code> value. The value is case sensitive. When the value for the filter is the job definition name, the results include all the jobs that used any revision of that job definition name. If the value ends with an asterisk (*), the filter matches any job definition name that begins with the string before the '*'. For example, <code>jd1</code> matches only <code>jd1</code>, and <code>jd1*</code> matches both <code>jd1</code> and <code>jd1A</code>. The version of the job definition that's used doesn't affect the sort order. When the <code>JOB_DEFINITION</code> filter is used and the ARN is used (which is in the form <code>arn:${Partition}:batch:${Region}:${Account}:job-definition/${JobDefinitionName}:${Revision}</code>), the results include jobs that used the specified revision of the job definition. Asterisk (*) isn't supported when the ARN is used.</p> </dd> <dt>BEFORE_CREATED_AT</dt> <dd> <p>The value for the filter is the time that's before the job was created. This corresponds to the <code>createdAt</code> value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.</p> </dd> <dt>AFTER_CREATED_AT</dt> <dd> <p>The value for the filter is the time that's after the job was created. This corresponds to the <code>createdAt</code> value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.</p> </dd> <dt>SHARE_IDENTIFIER</dt> <dd> <p>The value for the filter is the fairshare scheduling share identifier.</p> </dd> </dl>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list running jobs
            This example lists the running jobs in the HighPriority job queue.

            >>> client.list_jobs(job_queue='HighPriority')
            To list submitted jobs
            This example lists jobs in the HighPriority job queue that are in the SUBMITTED job status.

            >>> client.list_jobs(job_queue='HighPriority', job_status='SUBMITTED')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.list_jobs_request.ListJobsRequest]",
        ) -> OperationResponse["capo_batch.types.list_jobs_response.ListJobsResponse"]:
            import capo_batch._operations.aws_batch_v20160810.list_jobs

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.list_jobs.list_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.list_jobs_request.ListJobsRequest = {}
        if job_queue is not None:
            input_["job_queue"] = job_queue
        if array_job_id is not None:
            input_["array_job_id"] = array_job_id
        if multi_node_job_id is not None:
            input_["multi_node_job_id"] = multi_node_job_id
        if job_status is not None:
            input_["job_status"] = job_status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_jobs(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        array_job_id: Optional["capo_batch.types.string.String"] = None,
        multi_node_job_id: Optional["capo_batch.types.string.String"] = None,
        job_status: Optional["capo_batch.types.job_status.JobStatus"] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
        filters: Optional[
            "capo_batch.types.list_jobs_filter_list.ListJobsFilterList"
        ] = None,
    ) -> "Iterator[capo_batch.types.job_summary.JobSummary]":
        _token = next_token
        while True:
            _response = self.list_jobs(
                config_overrides=config_overrides,
                job_queue=job_queue,
                array_job_id=array_job_id,
                multi_node_job_id=multi_node_job_id,
                job_status=job_status,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("job_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_jobs_by_consumable_resource(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        consumable_resource: Optional["capo_batch.types.string.String"] = None,
        filters: Optional[
            "capo_batch.types.list_jobs_by_consumable_resource_filter_list.ListJobsByConsumableResourceFilterList"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.list_jobs_by_consumable_resource_response.ListJobsByConsumableResourceResponse":
        """<p>Returns a list of Batch jobs that require a specific consumable resource.</p>

        Args:
            consumable_resource: <p>The name or ARN of the consumable resource.</p>
            filters: <p>The filters to apply to the job list query. If used, only those jobs requiring the specified consumable resource (<code>consumableResource</code>) and that match the value of the filters are listed. The filter names and values can be:</p> <ul> <li> <p>name: <code>JOB_STATUS</code> </p> <p>values: <code>SUBMITTED | PENDING | RUNNABLE | STARTING | RUNNING | SUCCEEDED | FAILED</code> </p> </li> <li> <p>name: <code>JOB_NAME </code> </p> <p>The values are case-insensitive matches for the job name. If a filter value ends with an asterisk (*), it matches any job name that begins with the string before the '*'.</p> </li> </ul>
            max_results: <p>The maximum number of results returned by <code>ListJobsByConsumableResource</code> in paginated output. When this parameter is used, <code>ListJobsByConsumableResource</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListJobsByConsumableResource</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListJobsByConsumableResource</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListJobsByConsumableResource</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of Batch jobs by consumable resource
            Returns a list of Batch jobs that require a specific consumable resource.

            >>> client.list_jobs_by_consumable_resource(consumable_resource='myConsumableResource', filters=[{'name': 'CONSUMABLE_RESOURCE_NAME', 'values': ['my*']}], max_results=123)
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.list_jobs_by_consumable_resource_request.ListJobsByConsumableResourceRequest]",
        ) -> OperationResponse[
            "capo_batch.types.list_jobs_by_consumable_resource_response.ListJobsByConsumableResourceResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.list_jobs_by_consumable_resource

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.list_jobs_by_consumable_resource.list_jobs_by_consumable_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.list_jobs_by_consumable_resource_request.ListJobsByConsumableResourceRequest = {}
        if consumable_resource is not None:
            input_["consumable_resource"] = consumable_resource
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_jobs_by_consumable_resource(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        consumable_resource: Optional["capo_batch.types.string.String"] = None,
        filters: Optional[
            "capo_batch.types.list_jobs_by_consumable_resource_filter_list.ListJobsByConsumableResourceFilterList"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "Iterator[capo_batch.types.list_jobs_by_consumable_resource_summary.ListJobsByConsumableResourceSummary]":
        _token = next_token
        while True:
            _response = self.list_jobs_by_consumable_resource(
                config_overrides=config_overrides,
                consumable_resource=consumable_resource,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_quota_shares(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.list_quota_shares_response.ListQuotaSharesResponse":
        """<p>Returns a list of Batch quota shares associated with a job queue.</p>

        Args:
            job_queue: <p>The name or full Amazon Resource Name (ARN) of the job queue used to list quota shares.</p>
            max_results: <p>The maximum number of results returned by <code>ListQuotaShares</code> in paginated output. When this parameter is used, <code>ListQuotaShares</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListQuotaShares</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, <code>ListQuotaShares</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value that's returned from a previous paginated <code>ListQuotaShares</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.list_quota_shares_request.ListQuotaSharesRequest]",
        ) -> OperationResponse[
            "capo_batch.types.list_quota_shares_response.ListQuotaSharesResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.list_quota_shares

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.list_quota_shares.list_quota_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.list_quota_shares_request.ListQuotaSharesRequest = {}
        if job_queue is not None:
            input_["job_queue"] = job_queue
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

    def iter_list_quota_shares(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "Iterator[capo_batch.types.quota_share_detail.QuotaShareDetail]":
        _token = next_token
        while True:
            _response = self.list_quota_shares(
                config_overrides=config_overrides,
                job_queue=job_queue,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("quota_shares",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_scheduling_policies(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.list_scheduling_policies_response.ListSchedulingPoliciesResponse":
        """<p>Returns a list of Batch scheduling policies.</p>

        Args:
            max_results: <p>The maximum number of results that's returned by <code>ListSchedulingPolicies</code> in paginated output. When this parameter is used, <code>ListSchedulingPolicies</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListSchedulingPolicies</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, <code>ListSchedulingPolicies</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value that's returned from a previous paginated <code>ListSchedulingPolicies</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.list_scheduling_policies_request.ListSchedulingPoliciesRequest]",
        ) -> OperationResponse[
            "capo_batch.types.list_scheduling_policies_response.ListSchedulingPoliciesResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.list_scheduling_policies

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.list_scheduling_policies.list_scheduling_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.list_scheduling_policies_request.ListSchedulingPoliciesRequest = {}
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

    def iter_list_scheduling_policies(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
    ) -> "Iterator[capo_batch.types.scheduling_policy_listing_detail.SchedulingPolicyListingDetail]":
        _token = next_token
        while True:
            _response = self.list_scheduling_policies(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scheduling_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_jobs(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        job_status: Optional[
            "capo_batch.types.service_job_status.ServiceJobStatus"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
        filters: Optional[
            "capo_batch.types.list_jobs_filter_list.ListJobsFilterList"
        ] = None,
    ) -> "capo_batch.types.list_service_jobs_response.ListServiceJobsResponse":
        """<p>Returns a list of service jobs for a specified job queue.</p>

        Args:
            job_queue: <p>The name or ARN of the job queue with which to list service jobs.</p>
            job_status: <p>The job status used to filter service jobs in the specified queue. If the <code>filters</code> parameter is specified, the <code>jobStatus</code> parameter is ignored and jobs with any status are returned. The exceptions are the <code>SHARE_IDENTIFIER</code> filter and <code>QUOTA_SHARE_NAME</code> filter, which can be used with <code>jobStatus</code>. If you don't specify a status, only <code>RUNNING</code> jobs are returned.</p> <note> <p>The <code>SHARE_IDENTIFIER</code> filter or <code>QUOTA_SHARE_NAME</code> filter can be used with the <code>jobStatus</code> field to filter results.</p> </note>
            max_results: <p>The maximum number of results returned by <code>ListServiceJobs</code> in paginated output. When this parameter is used, <code>ListServiceJobs</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServiceJobs</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServiceJobs</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListServiceJobs</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            filters: <p>The filter to apply to the query. Only one filter can be used at a time. When the filter is used, <code>jobStatus</code> is ignored with the exception that <code>SHARE_IDENTIFIER</code> or <code>QUOTA_SHARE_NAME</code> and <code>jobStatus</code> can be used together. The results are sorted by the <code>createdAt</code> field, with the most recent jobs being first.</p> <note> <p>The <code>SHARE_IDENTIFIER</code> or <code>QUOTA_SHARE_NAME</code> filter and the <code>jobStatus</code> field can be used together to filter results.</p> </note> <dl> <dt>JOB_NAME</dt> <dd> <p>The value of the filter is a case-insensitive match for the job name. If the value ends with an asterisk (*), the filter matches any job name that begins with the string before the '*'. This corresponds to the <code>jobName</code> value. For example, <code>test1</code> matches both <code>Test1</code> and <code>test1</code>, and <code>test1*</code> matches both <code>test1</code> and <code>Test10</code>. When the <code>JOB_NAME</code> filter is used, the results are grouped by the job name and version.</p> </dd> <dt>BEFORE_CREATED_AT</dt> <dd> <p>The value for the filter is the time that's before the job was created. This corresponds to the <code>createdAt</code> value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.</p> </dd> <dt>AFTER_CREATED_AT</dt> <dd> <p>The value for the filter is the time that's after the job was created. This corresponds to the <code>createdAt</code> value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.</p> </dd> <dt>SHARE_IDENTIFIER</dt> <dd> <p>The value for the filter is the fairshare scheduling share identifier.</p> </dd> <dt>QUOTA_SHARE_NAME</dt> <dd> <p>The value for the filter is the quota management share name.</p> </dd> </dl>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.list_service_jobs_request.ListServiceJobsRequest]",
        ) -> OperationResponse[
            "capo_batch.types.list_service_jobs_response.ListServiceJobsResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.list_service_jobs

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.list_service_jobs.list_service_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.list_service_jobs_request.ListServiceJobsRequest = {}
        if job_queue is not None:
            input_["job_queue"] = job_queue
        if job_status is not None:
            input_["job_status"] = job_status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_service_jobs(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        job_status: Optional[
            "capo_batch.types.service_job_status.ServiceJobStatus"
        ] = None,
        max_results: Optional["capo_batch.types.integer.Integer"] = None,
        next_token: Optional["capo_batch.types.string.String"] = None,
        filters: Optional[
            "capo_batch.types.list_jobs_filter_list.ListJobsFilterList"
        ] = None,
    ) -> "Iterator[capo_batch.types.service_job_summary.ServiceJobSummary]":
        _token = next_token
        while True:
            _response = self.list_service_jobs(
                config_overrides=config_overrides,
                job_queue=job_queue,
                job_status=job_status,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("job_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_batch.types.string.String",
        *,
        config_overrides: Optional[BatchClientConfig] = None,
    ) -> "capo_batch.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for an Batch resource. Batch resources that support tags are compute environments, jobs, job definitions, job queues, and scheduling policies. ARNs for child jobs of array and multi-node parallel (MNP) jobs aren't supported.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource that tags are listed for. Batch resources that support tags are compute environments, jobs, job definitions, job queues, and scheduling policies. ARNs for child jobs of array and multi-node parallel (MNP) jobs aren't supported.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListTagsForResource Example
            This demonstrates calling the ListTagsForResource action.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:batch:us-east-1:123456789012:job-definition/sleep30:1')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_batch.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.list_tags_for_resource

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_job_definition(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_definition_name: Optional["capo_batch.types.string.String"] = None,
        type: Optional["capo_batch.types.job_definition_type.JobDefinitionType"] = None,
        parameters: Optional["capo_batch.types.parameters_map.ParametersMap"] = None,
        scheduling_priority: Optional["capo_batch.types.integer.Integer"] = None,
        container_properties: Optional[
            "capo_batch.types.container_properties.ContainerProperties"
        ] = None,
        node_properties: Optional[
            "capo_batch.types.node_properties.NodeProperties"
        ] = None,
        retry_strategy: Optional[
            "capo_batch.types.retry_strategy.RetryStrategy"
        ] = None,
        propagate_tags: Optional["capo_batch.types.boolean.Boolean"] = None,
        timeout: Optional["capo_batch.types.job_timeout.JobTimeout"] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
        platform_capabilities: Optional[
            "capo_batch.types.platform_capability_list.PlatformCapabilityList"
        ] = None,
        eks_properties: Optional[
            "capo_batch.types.eks_properties.EksProperties"
        ] = None,
        ecs_properties: Optional[
            "capo_batch.types.ecs_properties.EcsProperties"
        ] = None,
        consumable_resource_properties: Optional[
            "capo_batch.types.consumable_resource_properties.ConsumableResourceProperties"
        ] = None,
    ) -> "capo_batch.types.register_job_definition_response.RegisterJobDefinitionResponse":
        """<p>Registers an Batch job definition.</p>

        Args:
            job_definition_name: <p>The name of the job definition to register. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>
            type: <p>The type of job definition. For more information about multi-node parallel jobs, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html">Creating a multi-node parallel job definition</a> in the <i>Batch User Guide</i>.</p> <ul> <li> <p>If the value is <code>container</code>, then one of the following is required: <code>containerProperties</code>, <code>ecsProperties</code>, or <code>eksProperties</code>.</p> </li> <li> <p>If the value is <code>multinode</code>, then <code>nodeProperties</code> is required.</p> </li> </ul> <note> <p>If the job is run on Fargate resources, then <code>multinode</code> isn't supported.</p> </note>
            parameters: <p>Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a <code>SubmitJob</code> request override any corresponding parameter defaults from the job definition.</p>
            scheduling_priority: <p>The scheduling priority for jobs that are submitted with this job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.</p> <p>The minimum supported value is 0 and the maximum supported value is 9999.</p>
            container_properties: <p>An object with properties specific to Amazon ECS-based single-node container-based jobs. If the job definition's <code>type</code> parameter is <code>container</code>, then you must specify either <code>containerProperties</code> or <code>nodeProperties</code>. This must not be specified for Amazon EKS-based job definitions.</p> <note> <p>If the job runs on Fargate resources, then you must not specify <code>nodeProperties</code>; use only <code>containerProperties</code>.</p> </note>
            node_properties: <p>An object with properties specific to multi-node parallel jobs. If you specify node properties for a job, it becomes a multi-node parallel job. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/multi-node-parallel-jobs.html">Multi-node Parallel Jobs</a> in the <i>Batch User Guide</i>.</p> <note> <p>If the job runs on Fargate resources, then you must not specify <code>nodeProperties</code>; use <code>containerProperties</code> instead.</p> </note> <note> <p>If the job runs on Amazon EKS resources, then you must not specify <code>nodeProperties</code>.</p> </note>
            retry_strategy: <p>The retry strategy to use for failed jobs that are submitted with this job definition. Any retry strategy that's specified during a <a>SubmitJob</a> operation overrides the retry strategy defined here. If a job is terminated due to a timeout, it isn't retried.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags are not propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the <code>FAILED</code> state.</p> <note> <p>If the job runs on Amazon EKS resources, then you must not specify <code>propagateTags</code>.</p> </note>
            timeout: <p>The timeout configuration for jobs that are submitted with this job definition, after which Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it isn't retried. The minimum value for the timeout is 60 seconds. Any timeout configuration that's specified during a <a>SubmitJob</a> operation overrides the timeout configuration defined here. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/job_timeouts.html">Job Timeouts</a> in the <i>Batch User Guide</i>.</p>
            tags: <p>The tags that you apply to the job definition to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging Amazon Web Services Resources</a> in <i>Batch User Guide</i>.</p>
            platform_capabilities: <p>The platform capabilities required by the job definition. If no value is specified, it defaults to <code>EC2</code>. To run the job on Fargate resources, specify <code>FARGATE</code>. To run the job on Amazon ECS Managed Instances, specify <code>MANAGED_INSTANCES</code>.</p> <p>Jobs with the <code>MANAGED_INSTANCES</code> platform capability must use <code>ecsProperties</code> (not <code>containerProperties</code>) and do not support multi-node parallel jobs.</p> <note> <p>If the job runs on Amazon EKS resources, then you must not specify <code>platformCapabilities</code>.</p> </note>
            eks_properties: <p>An object with properties that are specific to Amazon EKS-based jobs. This must not be specified for Amazon ECS based job definitions.</p>
            ecs_properties: <p>An object with properties that are specific to Amazon ECS-based jobs. This must not be specified for Amazon EKS-based job definitions.</p>
            consumable_resource_properties: <p>Contains a list of consumable resources required by the job.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            RegisterJobDefinition with tags
            This demonstrates calling the RegisterJobDefinition action, including tags.

            >>> client.register_job_definition(job_definition_name='sleep30', type='container', container_properties={'image': 'busybox', 'command': ['sleep', '30'], 'resourceRequirements': [{'type': 'MEMORY', 'value': '128'}, {'type': 'VCPU', 'value': '1'}]}, tags={'Department': 'Engineering', 'User': 'JaneDoe'})
            To register a GPU job definition on ECS Managed Instances
            This example registers a job definition that requests GPU resources on ECS Managed Instances.

            >>> client.register_job_definition(job_definition_name='my-gpu-managed-instances-job-def', type='container', platform_capabilities=['MANAGED_INSTANCES'], ecs_properties={'taskProperties': [{'containers': [{'image': '123456789012.dkr.ecr.us-east-1.amazonaws.com/my-gpu-image:latest', 'name': 'main', 'command': ['nvidia-smi'], 'resourceRequirements': [{'type': 'VCPU', 'value': '4'}, {'type': 'MEMORY', 'value': '16384'}, {'type': 'GPU', 'value': '1'}]}], 'executionRoleArn': 'arn:aws:iam::123456789012:role/ecsTaskExecutionRole'}]})
            To register a job definition
            This example registers a job definition for a simple container job.

            >>> client.register_job_definition(container_properties={'image': 'busybox', 'command': ['sleep', '10'], 'resourceRequirements': [{'type': 'MEMORY', 'value': '128'}, {'type': 'VCPU', 'value': '1'}]}, type='container', job_definition_name='sleep10')
            To register a job definition on ECS Managed Instances
            This example registers a job definition that runs on ECS Managed Instances using ecsProperties with the MANAGED_INSTANCES platform capability.

            >>> client.register_job_definition(job_definition_name='my-managed-instances-job-def', type='container', platform_capabilities=['MANAGED_INSTANCES'], ecs_properties={'taskProperties': [{'containers': [{'image': 'public.ecr.aws/amazonlinux/amazonlinux:2023', 'name': 'main', 'command': ['echo', 'hello managed instances'], 'resourceRequirements': [{'type': 'VCPU', 'value': '1'}, {'type': 'MEMORY', 'value': '1024'}]}], 'executionRoleArn': 'arn:aws:iam::123456789012:role/ecsTaskExecutionRole'}]})
            To register a multi-container job definition on ECS Managed Instances
            This example registers a job definition with a main container and a sidecar logging container on ECS Managed Instances.

            >>> client.register_job_definition(job_definition_name='my-sidecar-managed-instances-job-def', type='container', platform_capabilities=['MANAGED_INSTANCES'], ecs_properties={'taskProperties': [{'containers': [{'image': 'public.ecr.aws/amazonlinux/amazonlinux:2023', 'name': 'main', 'command': ['echo', 'processing data'], 'essential': True, 'resourceRequirements': [{'type': 'VCPU', 'value': '2'}, {'type': 'MEMORY', 'value': '4096'}]}, {'image': 'public.ecr.aws/amazonlinux/amazonlinux:2023', 'name': 'sidecar', 'command': ['echo', 'logging sidecar'], 'essential': False, 'resourceRequirements': [{'type': 'VCPU', 'value': '1'}, {'type': 'MEMORY', 'value': '512'}]}], 'executionRoleArn': 'arn:aws:iam::123456789012:role/ecsTaskExecutionRole'}]})
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.register_job_definition_request.RegisterJobDefinitionRequest]",
        ) -> OperationResponse[
            "capo_batch.types.register_job_definition_response.RegisterJobDefinitionResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.register_job_definition

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.register_job_definition.register_job_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.register_job_definition_request.RegisterJobDefinitionRequest = {}
        if job_definition_name is not None:
            input_["job_definition_name"] = job_definition_name
        if type is not None:
            input_["type"] = type
        if parameters is not None:
            input_["parameters"] = parameters
        if scheduling_priority is not None:
            input_["scheduling_priority"] = scheduling_priority
        if container_properties is not None:
            input_["container_properties"] = container_properties
        if node_properties is not None:
            input_["node_properties"] = node_properties
        if retry_strategy is not None:
            input_["retry_strategy"] = retry_strategy
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if timeout is not None:
            input_["timeout"] = timeout
        if tags is not None:
            input_["tags"] = tags
        if platform_capabilities is not None:
            input_["platform_capabilities"] = platform_capabilities
        if eks_properties is not None:
            input_["eks_properties"] = eks_properties
        if ecs_properties is not None:
            input_["ecs_properties"] = ecs_properties
        if consumable_resource_properties is not None:
            input_["consumable_resource_properties"] = consumable_resource_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def submit_job(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_name: Optional["capo_batch.types.string.String"] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        share_identifier: Optional["capo_batch.types.string.String"] = None,
        scheduling_priority_override: Optional[
            "capo_batch.types.integer.Integer"
        ] = None,
        array_properties: Optional[
            "capo_batch.types.array_properties.ArrayProperties"
        ] = None,
        depends_on: Optional[
            "capo_batch.types.job_dependency_list.JobDependencyList"
        ] = None,
        job_definition: Optional["capo_batch.types.string.String"] = None,
        parameters: Optional["capo_batch.types.parameters_map.ParametersMap"] = None,
        container_overrides: Optional[
            "capo_batch.types.container_overrides.ContainerOverrides"
        ] = None,
        node_overrides: Optional[
            "capo_batch.types.node_overrides.NodeOverrides"
        ] = None,
        retry_strategy: Optional[
            "capo_batch.types.retry_strategy.RetryStrategy"
        ] = None,
        propagate_tags: Optional["capo_batch.types.boolean.Boolean"] = None,
        timeout: Optional["capo_batch.types.job_timeout.JobTimeout"] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
        eks_properties_override: Optional[
            "capo_batch.types.eks_properties_override.EksPropertiesOverride"
        ] = None,
        ecs_properties_override: Optional[
            "capo_batch.types.ecs_properties_override.EcsPropertiesOverride"
        ] = None,
        consumable_resource_properties_override: Optional[
            "capo_batch.types.consumable_resource_properties.ConsumableResourceProperties"
        ] = None,
    ) -> "capo_batch.types.submit_job_response.SubmitJobResponse":
        """<p>Submits an Batch job from a job definition. Parameters that are specified during <a>SubmitJob</a> override parameters defined in the job definition. vCPU and memory requirements that are specified in the <code>resourceRequirements</code> objects in the job definition are the exception. They can't be overridden this way using the <code>memory</code> and <code>vcpus</code> parameters. Rather, you must specify updates to job definition parameters in a <code>resourceRequirements</code> object that's included in the <code>containerOverrides</code> parameter.</p> <note> <p>Job queues with a scheduling policy are limited to 500 active share identifiers at a time. </p> </note> <important> <p>Jobs that run on Fargate resources can't be guaranteed to run for more than 14 days. This is because, after 14 days, Fargate resources might become unavailable and job might be terminated.</p> </important>

        Args:
            job_name: <p>The name of the job. It can be up to 128 letters long. The first character must be alphanumeric, can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>
            job_queue: <p>The job queue where the job is submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue.</p>
            share_identifier: <p>The share identifier for the job. Don't specify this parameter if the job queue doesn't have a fair-share scheduling policy. If the job queue has a fair-share scheduling policy, then this parameter must be specified.</p> <p>This string is limited to 255 alphanumeric characters, and can be followed by an asterisk (*).</p>
            scheduling_priority_override: <p>The scheduling priority for the job. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority. This overrides any scheduling priority in the job definition and works only within a single share identifier.</p> <p>The minimum supported value is 0 and the maximum supported value is 9999.</p>
            array_properties: <p>The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html">Array Jobs</a> in the <i>Batch User Guide</i>.</p>
            depends_on: <p>A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a <code>SEQUENTIAL</code> type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an <code>N_TO_N</code> type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.</p>
            job_definition: <p>The job definition used by this job. This value can be one of <code>definition-name</code>, <code>definition-name:revision</code>, or the Amazon Resource Name (ARN) for the job definition, with or without the revision (<code>arn:aws:batch:<i>region</i>:<i>account</i>:job-definition/<i>definition-name</i>:<i>revision</i> </code>, or <code>arn:aws:batch:<i>region</i>:<i>account</i>:job-definition/<i>definition-name</i> </code>).</p> <p>If the revision is not specified, then the latest active revision is used.</p>
            parameters: <p>Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters in a <code>SubmitJob</code> request override any corresponding parameter defaults from the job definition.</p>
            container_overrides: <p>An object with properties that override the defaults for the job definition that specify the name of a container in the specified job definition and the overrides it should receive. You can override the default command for a container, which is specified in the job definition or the Docker image, with a <code>command</code> override. You can also override existing environment variables on a container or add new environment variables to it with an <code>environment</code> override.</p>
            node_overrides: <p>A list of node overrides in JSON format that specify the node range to target and the container overrides for that node range.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources; use <code>containerOverrides</code> instead.</p> </note>
            retry_strategy: <p>The retry strategy to use for failed jobs from this <a>SubmitJob</a> operation. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the <code>FAILED</code> state. When specified, this overrides the tag propagation setting in the job definition.</p>
            timeout: <p>The timeout configuration for this <a>SubmitJob</a> operation. You can specify a timeout duration after which Batch terminates your jobs if they haven't finished. If a job is terminated due to a timeout, it isn't retried. The minimum value for the timeout is 60 seconds. This configuration overrides any timeout configuration specified in the job definition. For array jobs, child jobs have the same timeout configuration as the parent job. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html">Job Timeouts</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            tags: <p>The tags that you apply to the job request to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in <i>Amazon Web Services General Reference</i>.</p>
            eks_properties_override: <p>An object, with properties that override defaults for the job definition, can only be specified for jobs that are run on Amazon EKS resources.</p>
            ecs_properties_override: <p>An object, with properties that override defaults for the job definition, can only be specified for jobs that are run on Amazon ECS resources.</p>
            consumable_resource_properties_override: <p>An object that contains overrides for the consumable resources of a job.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To submit a job to a queue
            This example submits a simple container job called example to the HighPriority job queue.

            >>> client.submit_job(job_name='example', job_queue='HighPriority', job_definition='sleep60')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.submit_job_request.SubmitJobRequest]",
        ) -> OperationResponse[
            "capo_batch.types.submit_job_response.SubmitJobResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.submit_job

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.submit_job.submit_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.submit_job_request.SubmitJobRequest = {}
        if job_name is not None:
            input_["job_name"] = job_name
        if job_queue is not None:
            input_["job_queue"] = job_queue
        if share_identifier is not None:
            input_["share_identifier"] = share_identifier
        if scheduling_priority_override is not None:
            input_["scheduling_priority_override"] = scheduling_priority_override
        if array_properties is not None:
            input_["array_properties"] = array_properties
        if depends_on is not None:
            input_["depends_on"] = depends_on
        if job_definition is not None:
            input_["job_definition"] = job_definition
        if parameters is not None:
            input_["parameters"] = parameters
        if container_overrides is not None:
            input_["container_overrides"] = container_overrides
        if node_overrides is not None:
            input_["node_overrides"] = node_overrides
        if retry_strategy is not None:
            input_["retry_strategy"] = retry_strategy
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if timeout is not None:
            input_["timeout"] = timeout
        if tags is not None:
            input_["tags"] = tags
        if eks_properties_override is not None:
            input_["eks_properties_override"] = eks_properties_override
        if ecs_properties_override is not None:
            input_["ecs_properties_override"] = ecs_properties_override
        if consumable_resource_properties_override is not None:
            input_["consumable_resource_properties_override"] = (
                consumable_resource_properties_override
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def submit_service_job(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_name: Optional["capo_batch.types.string.String"] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        retry_strategy: Optional[
            "capo_batch.types.service_job_retry_strategy.ServiceJobRetryStrategy"
        ] = None,
        scheduling_priority: Optional["capo_batch.types.integer.Integer"] = None,
        service_request_payload: Optional["capo_batch.types.string.String"] = None,
        service_job_type: Optional[
            "capo_batch.types.service_job_type.ServiceJobType"
        ] = None,
        share_identifier: Optional["capo_batch.types.string.String"] = None,
        quota_share_name: Optional["capo_batch.types.string.String"] = None,
        preemption_configuration: Optional[
            "capo_batch.types.service_job_preemption_configuration.ServiceJobPreemptionConfiguration"
        ] = None,
        timeout_config: Optional[
            "capo_batch.types.service_job_timeout.ServiceJobTimeout"
        ] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
        client_token: Optional[
            "capo_batch.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_batch.types.submit_service_job_response.SubmitServiceJobResponse":
        """<p>Submits a service job to a specified job queue to run on SageMaker AI. A service job is a unit of work that you submit to Batch for execution on SageMaker AI.</p>

        Args:
            job_name: <p>The name of the service job. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>
            job_queue: <p>The job queue into which the service job is submitted. You can specify either the name or the ARN of the queue. The job queue must have the type <code>SAGEMAKER_TRAINING</code>.</p>
            retry_strategy: <p>The retry strategy to use for failed service jobs that are submitted with this service job request. </p>
            scheduling_priority: <p>The scheduling priority of the service job. Valid values are integers between 0 and 9999.</p>
            service_request_payload: <p>The request, in JSON, for the service that the SubmitServiceJob operation is queueing. </p>
            service_job_type: <p>The type of service job. For SageMaker Training jobs, specify <code>SAGEMAKER_TRAINING</code>.</p>
            share_identifier: <p>The share identifier for the service job. Don't specify this parameter if the job queue doesn't have a fair-share scheduling policy. If the job queue has a fair-share scheduling policy, then this parameter must be specified.</p>
            quota_share_name: <p>The quota share for the service job. Don't specify this parameter if the job queue doesn't have a quota share scheduling policy. If the job queue has a quota share scheduling policy, then this parameter must be specified.</p>
            preemption_configuration: <p>Specifies the service job behavior when preempted.</p>
            timeout_config: <p>The timeout configuration for the service job. If none is specified, Batch defers to the default timeout of the underlying service handling the job.</p>
            tags: <p>The tags that you apply to the service job request. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging your Batch resources</a>.</p>
            client_token: <p>A unique identifier for the request. This token is used to ensure idempotency of requests. If this parameter is specified and two submit requests with identical payloads and <code>clientToken</code>s are received, these requests are considered the same request and the second request is rejected.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.submit_service_job_request.SubmitServiceJobRequest]",
        ) -> OperationResponse[
            "capo_batch.types.submit_service_job_response.SubmitServiceJobResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.submit_service_job

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.submit_service_job.submit_service_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.submit_service_job_request.SubmitServiceJobRequest = {}
        if job_name is not None:
            input_["job_name"] = job_name
        if job_queue is not None:
            input_["job_queue"] = job_queue
        if retry_strategy is not None:
            input_["retry_strategy"] = retry_strategy
        if scheduling_priority is not None:
            input_["scheduling_priority"] = scheduling_priority
        if service_request_payload is not None:
            input_["service_request_payload"] = service_request_payload
        if service_job_type is not None:
            input_["service_job_type"] = service_job_type
        if share_identifier is not None:
            input_["share_identifier"] = share_identifier
        if quota_share_name is not None:
            input_["quota_share_name"] = quota_share_name
        if preemption_configuration is not None:
            input_["preemption_configuration"] = preemption_configuration
        if timeout_config is not None:
            input_["timeout_config"] = timeout_config
        if tags is not None:
            input_["tags"] = tags
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

    def tag_resource(
        self,
        resource_arn: "capo_batch.types.string.String",
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        tags: Optional["capo_batch.types.tagris_tags_map.TagrisTagsMap"] = None,
    ) -> "capo_batch.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource aren't specified in the request parameters, they aren't changed. When a resource is deleted, the tags that are associated with that resource are deleted as well. Batch resources that support tags are compute environments, jobs, job definitions, job queues, and scheduling policies. ARNs for child jobs of array and multi-node parallel (MNP) jobs aren't supported.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that tags are added to. Batch resources that support tags are compute environments, jobs, job definitions, job queues, and scheduling policies. ARNs for child jobs of array and multi-node parallel (MNP) jobs aren't supported.</p>
            tags: <p>The tags that you apply to the resource to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            TagResource Example
            This demonstrates calling the TagResource action.

            >>> client.tag_resource(resource_arn='arn:aws:batch:us-east-1:123456789012:job-definition/sleep30:1', tags={'Stage': 'Alpha'})
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_batch.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.tag_resource

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
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

    def terminate_job(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_id: Optional["capo_batch.types.string.String"] = None,
        reason: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.terminate_job_response.TerminateJobResponse":
        """<p>Terminates a job in a job queue. Jobs that are in the <code>STARTING</code> or <code>RUNNING</code> state are terminated, which causes them to transition to <code>FAILED</code>. Jobs that have not progressed to the <code>STARTING</code> state are cancelled.</p>

        Args:
            job_id: <p>The Batch job ID of the job to terminate.</p>
            reason: <p>A message to attach to the job that explains the reason for terminating it. This message is returned by future <a>DescribeJobs</a> operations on the job. It is also recorded in the Batch activity logs.</p> <p>This parameter has a limit of 1024 characters.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To terminate a job
            This example terminates a job with the specified job ID.

            >>> client.terminate_job(reason='Terminating job.', job_id='61e743ed-35e4-48da-b2de-5c8333821c84')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.terminate_job_request.TerminateJobRequest]",
        ) -> OperationResponse[
            "capo_batch.types.terminate_job_response.TerminateJobResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.terminate_job

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.terminate_job.terminate_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.terminate_job_request.TerminateJobRequest = {}
        if job_id is not None:
            input_["job_id"] = job_id
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_jobs(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        jobs: Optional["capo_batch.types.string_list.StringList"] = None,
        reason: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.terminate_jobs_response.TerminateJobsResponse":
        """<p>Terminates up to 50 jobs in a job queue. This is a bulk version of <a>TerminateJob</a>. Jobs that are in the <code>STARTING</code> or <code>RUNNING</code> state are terminated, which causes them to transition to <code>FAILED</code>. Jobs that have not progressed to the <code>STARTING</code> state are cancelled.</p> <p>Batch reports the result for each job individually in the response. Jobs that were processed successfully are reported in the <code>successful</code> list. Jobs that encountered errors are reported in the <code>errors</code> list. The response returns an HTTP status code of <code>200</code> even when some jobs encountered errors, so check the <code>errors</code> list. Jobs that can't be found are treated as successfully processed.</p> <important> <p>This operation requires <code>batch:TerminateJob</code> permission for each job in the request. There is no separate <code>batch:TerminateJobs</code> IAM action. If a caller's IAM policy grants <code>batch:TerminateJob</code>, they can use both the singular <a>TerminateJob</a> and bulk <code>TerminateJobs</code> operations.</p> </important>

        Args:
            jobs: <p>An array of up to 50 Batch job IDs of the jobs to terminate.</p>
            reason: <p>A message to attach to the job that explains the reason for terminating it. This message is returned by future <a>DescribeJobs</a> operations on the job. It is also recorded in the Batch activity logs.</p> <p>This parameter has a limit of 1024 characters.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To terminate multiple jobs
            This example terminates the jobs with the specified job IDs.

            >>> client.terminate_jobs(jobs=['61e743ed-35e4-48da-b2de-5c8333821c84', 'b3d0f26e-6d3a-4a5b-9c2e-7f4a1b2c3d4e'], reason='Terminating jobs.')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.terminate_jobs_request.TerminateJobsRequest]",
        ) -> OperationResponse[
            "capo_batch.types.terminate_jobs_response.TerminateJobsResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.terminate_jobs

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.terminate_jobs.terminate_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.terminate_jobs_request.TerminateJobsRequest = {}
        if jobs is not None:
            input_["jobs"] = jobs
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_service_job(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_id: Optional["capo_batch.types.string.String"] = None,
        reason: Optional["capo_batch.types.string.String"] = None,
    ) -> "capo_batch.types.terminate_service_job_response.TerminateServiceJobResponse":
        """<p>Terminates a service job in a job queue. </p>

        Args:
            job_id: <p>The service job ID of the service job to terminate.</p>
            reason: <p>A message to attach to the service job that explains the reason for terminating it. This message is returned by <code>DescribeServiceJob</code> operations on the service job.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.terminate_service_job_request.TerminateServiceJobRequest]",
        ) -> OperationResponse[
            "capo_batch.types.terminate_service_job_response.TerminateServiceJobResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.terminate_service_job

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.terminate_service_job.terminate_service_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.terminate_service_job_request.TerminateServiceJobRequest = {}
        if job_id is not None:
            input_["job_id"] = job_id
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_service_jobs(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        jobs: Optional["capo_batch.types.string_list.StringList"] = None,
        reason: Optional["capo_batch.types.string.String"] = None,
    ) -> (
        "capo_batch.types.terminate_service_jobs_response.TerminateServiceJobsResponse"
    ):
        """<p>Terminates up to 50 service jobs in a job queue. This is a bulk version of <a>TerminateServiceJob</a>.</p> <p>Batch reports the result for each service job individually in the response. Service jobs that were processed successfully are reported in the <code>successful</code> list. Service jobs that encountered errors are reported in the <code>errors</code> list. The response returns an HTTP status code of <code>200</code> even when some service jobs encountered errors, so check the <code>errors</code> list. Service jobs that can't be found are treated as successfully processed.</p> <important> <p>This operation requires <code>batch:TerminateServiceJob</code> permission for each service job in the request. There is no separate <code>batch:TerminateServiceJobs</code> IAM action. If a caller's IAM policy grants <code>batch:TerminateServiceJob</code>, they can use both the singular <code>TerminateServiceJob</code> and bulk <code>TerminateServiceJobs</code> operations.</p> </important>

        Args:
            jobs: <p>An array of up to 50 service job IDs of the service jobs to terminate.</p>
            reason: <p>A message to attach to the service job that explains the reason for terminating it. This message is returned by <code>DescribeServiceJob</code> operations on the service job.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To terminate multiple service jobs
            This example terminates the specified service jobs with a reason.

            >>> client.terminate_service_jobs(jobs=['a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d', 'b3d0f26e-6d3a-4a5b-9c2e-7f4a1b2c3d4e'], reason='Job terminated by user request')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.terminate_service_jobs_request.TerminateServiceJobsRequest]",
        ) -> OperationResponse[
            "capo_batch.types.terminate_service_jobs_response.TerminateServiceJobsResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.terminate_service_jobs

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.terminate_service_jobs.terminate_service_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.terminate_service_jobs_request.TerminateServiceJobsRequest = {}
        if jobs is not None:
            input_["jobs"] = jobs
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_batch.types.string.String",
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        tag_keys: Optional["capo_batch.types.tag_keys_list.TagKeysList"] = None,
    ) -> "capo_batch.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes specified tags from an Batch resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to delete tags. Batch resources that support tags are compute environments, jobs, job definitions, job queues, and scheduling policies. ARNs for child jobs of array and multi-node parallel (MNP) jobs aren't supported.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UntagResource Example
            This demonstrates calling the UntagResource action.

            >>> client.untag_resource(resource_arn='arn:aws:batch:us-east-1:123456789012:job-definition/sleep30:1', tag_keys=['Stage'])
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_batch.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.untag_resource

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_compute_environment(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        compute_environment: Optional["capo_batch.types.string.String"] = None,
        state: Optional["capo_batch.types.ce_state.CEState"] = None,
        unmanagedv_cpus: Optional["capo_batch.types.integer.Integer"] = None,
        compute_resources: Optional[
            "capo_batch.types.compute_resource_update.ComputeResourceUpdate"
        ] = None,
        service_role: Optional["capo_batch.types.string.String"] = None,
        update_policy: Optional["capo_batch.types.update_policy.UpdatePolicy"] = None,
        context: Optional["capo_batch.types.string.String"] = None,
        ecs_settings: Optional["capo_batch.types.ecs_settings.EcsSettings"] = None,
        eks_configuration: Optional[
            "capo_batch.types.eks_configuration_update.EksConfigurationUpdate"
        ] = None,
    ) -> "capo_batch.types.update_compute_environment_response.UpdateComputeEnvironmentResponse":
        """<p>Updates an Batch compute environment.</p>

        Args:
            compute_environment: <p>The name or full Amazon Resource Name (ARN) of the compute environment to update.</p>
            state: <p>The state of the compute environment. Compute environments in the <code>ENABLED</code> state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.</p> <p>If the state is <code>ENABLED</code>, then the Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.</p> <p>If the state is <code>DISABLED</code>, then the Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a <code>STARTING</code> or <code>RUNNING</code> state continue to progress normally. Managed compute environments in the <code>DISABLED</code> state don't scale out. </p> <note> <p>Compute environments in a <code>DISABLED</code> state may continue to incur billing charges, for example, if they have running instances due to jobs that are still executing or a non-zero <code>minvCpus</code> setting. To prevent additional charges, disable and delete the compute environment.</p> </note> <p>When an instance is idle, the instance scales down to the <code>minvCpus</code> value. However, the instance size doesn't change. For example, consider a <code>c5.8xlarge</code> instance with a <code>minvCpus</code> value of <code>4</code> and a <code>desiredvCpus</code> value of <code>36</code>. This instance doesn't scale down to a <code>c5.large</code> instance.</p>
            unmanagedv_cpus: <p>The maximum number of vCPUs expected to be used for an unmanaged compute environment. Don't specify this parameter for a managed compute environment. This parameter is only used for fair-share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair-share job queue, no vCPU capacity is reserved.</p>
            compute_resources: <p>Details of the compute resources managed by the compute environment. Required for a managed compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">Compute Environments</a> in the <i>Batch User Guide</i>.</p>
            service_role: <p>The full Amazon Resource Name (ARN) of the IAM role that allows Batch to make calls to other Amazon Web Services services on your behalf. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html">Batch service IAM role</a> in the <i>Batch User Guide</i>.</p> <important> <p>If the compute environment has a service-linked role, it can't be changed to use a regular IAM role. Likewise, if the compute environment has a regular IAM role, it can't be changed to use a service-linked role. To update the parameters for the compute environment that require an infrastructure update to change, the <b>AWSServiceRoleForBatch</b> service-linked role must be used. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> </important> <p>If your specified role has a path other than <code>/</code>, then you must either specify the full role ARN (recommended) or prefix the role name with the path.</p> <note> <p>Depending on how you created your Batch service role, its ARN might contain the <code>service-role</code> path prefix. When you only specify the name of the service role, Batch assumes that your ARN doesn't use the <code>service-role</code> path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.</p> </note>
            update_policy: <p>Specifies the updated infrastructure update policy for the compute environment. For more information about infrastructure updates, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p>
            context: <p>Reserved.</p>
            ecs_settings: <p>The Amazon ECS settings for the compute environment. These settings control CloudWatch Container Insights collection for the compute environment.</p>
            eks_configuration: <p>Updates the Amazon EKS configuration for the compute environment. Only specify this parameter if the compute environment's <code>containerOrchestrationType</code> is <code>EKS</code>. Currently, the <code>accessEntry</code> setting is the only Amazon EKS configuration that you can change after the compute environment is created. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html">Amazon EKS access entry authentication</a> in the <i>Batch User Guide</i>.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a compute environment
            This example disables the P2OnDemand compute environment so it can be deleted.

            >>> client.update_compute_environment(compute_environment='P2OnDemand', state='DISABLED')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.update_compute_environment_request.UpdateComputeEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_batch.types.update_compute_environment_response.UpdateComputeEnvironmentResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.update_compute_environment

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.update_compute_environment.update_compute_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.update_compute_environment_request.UpdateComputeEnvironmentRequest = {}
        if compute_environment is not None:
            input_["compute_environment"] = compute_environment
        if state is not None:
            input_["state"] = state
        if unmanagedv_cpus is not None:
            input_["unmanagedv_cpus"] = unmanagedv_cpus
        if compute_resources is not None:
            input_["compute_resources"] = compute_resources
        if service_role is not None:
            input_["service_role"] = service_role
        if update_policy is not None:
            input_["update_policy"] = update_policy
        if context is not None:
            input_["context"] = context
        if ecs_settings is not None:
            input_["ecs_settings"] = ecs_settings
        if eks_configuration is not None:
            input_["eks_configuration"] = eks_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_consumable_resource(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        consumable_resource: Optional["capo_batch.types.string.String"] = None,
        operation: Optional["capo_batch.types.string.String"] = None,
        quantity: Optional["capo_batch.types.long.Long"] = None,
        client_token: Optional[
            "capo_batch.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_batch.types.update_consumable_resource_response.UpdateConsumableResourceResponse":
        """<p>Updates a consumable resource.</p>

        Args:
            consumable_resource: <p>The name or ARN of the consumable resource to be updated.</p>
            operation: <p>Indicates how the quantity of the consumable resource will be updated. Must be one of:</p> <ul> <li> <p> <code>SET</code> </p> <p>Sets the quantity of the resource to the value specified by the <code>quantity</code> parameter.</p> </li> <li> <p> <code>ADD</code> </p> <p>Increases the quantity of the resource by the value specified by the <code>quantity</code> parameter.</p> </li> <li> <p> <code>REMOVE</code> </p> <p>Reduces the quantity of the resource by the value specified by the <code>quantity</code> parameter.</p> </li> </ul>
            quantity: <p>The change in the total quantity of the consumable resource. The <code>operation</code> parameter determines whether the value specified here will be the new total quantity, or the amount by which the total quantity will be increased or reduced. Must be a non-negative value.</p>
            client_token: <p>If this parameter is specified and two update requests with identical payloads and <code>clientToken</code>s are received, these requests are considered the same request. Both requests will succeed, but the update will only happen once. A <code>clientToken</code> is valid for 8 hours.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a consumable resource
            Updates a consumable resource.

            >>> client.update_consumable_resource(consumable_resource='myConsumableResource', operation='ADD', quantity=12)
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.update_consumable_resource_request.UpdateConsumableResourceRequest]",
        ) -> OperationResponse[
            "capo_batch.types.update_consumable_resource_response.UpdateConsumableResourceResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.update_consumable_resource

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.update_consumable_resource.update_consumable_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.update_consumable_resource_request.UpdateConsumableResourceRequest = {}
        if consumable_resource is not None:
            input_["consumable_resource"] = consumable_resource
        if operation is not None:
            input_["operation"] = operation
        if quantity is not None:
            input_["quantity"] = quantity
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

    def update_job_queue(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_queue: Optional["capo_batch.types.string.String"] = None,
        state: Optional["capo_batch.types.jq_state.JQState"] = None,
        scheduling_policy_arn: Optional["capo_batch.types.string.String"] = None,
        priority: Optional["capo_batch.types.integer.Integer"] = None,
        compute_environment_order: Optional[
            "capo_batch.types.compute_environment_orders.ComputeEnvironmentOrders"
        ] = None,
        service_environment_order: Optional[
            "capo_batch.types.service_environment_orders.ServiceEnvironmentOrders"
        ] = None,
        job_state_time_limit_actions: Optional[
            "capo_batch.types.job_state_time_limit_actions.JobStateTimeLimitActions"
        ] = None,
    ) -> "capo_batch.types.update_job_queue_response.UpdateJobQueueResponse":
        """<p>Updates a job queue.</p>

        Args:
            job_queue: <p>The name or the Amazon Resource Name (ARN) of the job queue.</p>
            state: <p>Describes the queue's ability to accept new jobs. If the job queue state is <code>ENABLED</code>, it can accept jobs. If the job queue state is <code>DISABLED</code>, new jobs can't be added to the queue, but jobs already in the queue can finish.</p>
            scheduling_policy_arn: <p>Amazon Resource Name (ARN) of the fair-share scheduling policy. Once a job queue is created, the fair-share scheduling policy can be replaced but not removed. The format is <code>aws:<i>Partition</i>:batch:<i>Region</i>:<i>Account</i>:scheduling-policy/<i>Name</i> </code>. For example, <code>aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy</code>.</p>
            priority: <p>The priority of the job queue. Job queues with a higher priority (or a higher integer value for the <code>priority</code> parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of <code>10</code> is given scheduling preference over a job queue with a priority value of <code>1</code>. All of the compute environments must be either EC2 (<code>EC2</code> or <code>SPOT</code>) or Fargate (<code>FARGATE</code> or <code>FARGATE_SPOT</code>). EC2 and Fargate compute environments can't be mixed.</p>
            compute_environment_order: <p>Details the set of compute environments mapped to a job queue and their order relative to each other. This is one of the parameters used by the job scheduler to determine which compute environment runs a given job. Compute environments must be in the <code>VALID</code> state before you can associate them with a job queue. All of the compute environments must be either EC2 (<code>EC2</code> or <code>SPOT</code>) or Fargate (<code>FARGATE</code> or <code>FARGATE_SPOT</code>). EC2 and Fargate compute environments can't be mixed.</p> <note> <p>All compute environments that are associated with a job queue must share the same architecture. Batch doesn't support mixing compute environment architecture types in a single job queue.</p> </note>
            service_environment_order: <p>The order of the service environment associated with the job queue. Job queues with a higher priority are evaluated first when associated with the same service environment.</p>
            job_state_time_limit_actions: <p>The set of actions that Batch perform on jobs that remain at the head of the job queue in the specified state longer than specified times. Batch will perform each action after <code>maxTimeSeconds</code> has passed. (<b>Note</b>: The minimum value for maxTimeSeconds is 600 (10 minutes) and its maximum value is 86,400 (24 hours).)</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a job queue
            This example disables a job queue so that it can be deleted.

            >>> client.update_job_queue(state='DISABLED', job_queue='GPGPU')
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.update_job_queue_request.UpdateJobQueueRequest]",
        ) -> OperationResponse[
            "capo_batch.types.update_job_queue_response.UpdateJobQueueResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.update_job_queue

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.update_job_queue.update_job_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.update_job_queue_request.UpdateJobQueueRequest = {}
        if job_queue is not None:
            input_["job_queue"] = job_queue
        if state is not None:
            input_["state"] = state
        if scheduling_policy_arn is not None:
            input_["scheduling_policy_arn"] = scheduling_policy_arn
        if priority is not None:
            input_["priority"] = priority
        if compute_environment_order is not None:
            input_["compute_environment_order"] = compute_environment_order
        if service_environment_order is not None:
            input_["service_environment_order"] = service_environment_order
        if job_state_time_limit_actions is not None:
            input_["job_state_time_limit_actions"] = job_state_time_limit_actions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_quota_share(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        quota_share_arn: Optional["capo_batch.types.string.String"] = None,
        capacity_limits: Optional[
            "capo_batch.types.quota_share_capacity_limits.QuotaShareCapacityLimits"
        ] = None,
        resource_sharing_configuration: Optional[
            "capo_batch.types.quota_share_resource_sharing_configuration.QuotaShareResourceSharingConfiguration"
        ] = None,
        preemption_configuration: Optional[
            "capo_batch.types.quota_share_preemption_configuration.QuotaSharePreemptionConfiguration"
        ] = None,
        state: Optional["capo_batch.types.quota_share_state.QuotaShareState"] = None,
    ) -> "capo_batch.types.update_quota_share_response.UpdateQuotaShareResponse":
        """<p>Updates a quota share.</p>

        Args:
            quota_share_arn: <p>The Amazon Resource Name (ARN) of the quota share to update.</p>
            capacity_limits: <p>A list that specifies the quantity and type of compute capacity allocated to the quota share.</p>
            resource_sharing_configuration: <p>Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.</p>
            preemption_configuration: <p>Specifies the preemption behavior for jobs in a quota share.</p>
            state: <p>The state of the quota share. If the quota share is <code>ENABLED</code>, it is able to accept jobs. If the quota share is <code>DISABLED</code>, new jobs won't be accepted but jobs already submitted can finish.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.update_quota_share_request.UpdateQuotaShareRequest]",
        ) -> OperationResponse[
            "capo_batch.types.update_quota_share_response.UpdateQuotaShareResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.update_quota_share

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.update_quota_share.update_quota_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.update_quota_share_request.UpdateQuotaShareRequest = {}
        if quota_share_arn is not None:
            input_["quota_share_arn"] = quota_share_arn
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits
        if resource_sharing_configuration is not None:
            input_["resource_sharing_configuration"] = resource_sharing_configuration
        if preemption_configuration is not None:
            input_["preemption_configuration"] = preemption_configuration
        if state is not None:
            input_["state"] = state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_scheduling_policy(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        arn: Optional["capo_batch.types.string.String"] = None,
        quota_share_policy: Optional[
            "capo_batch.types.quota_share_policy.QuotaSharePolicy"
        ] = None,
        fairshare_policy: Optional[
            "capo_batch.types.fairshare_policy.FairsharePolicy"
        ] = None,
    ) -> "capo_batch.types.update_scheduling_policy_response.UpdateSchedulingPolicyResponse":
        """<p>Updates a scheduling policy.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the scheduling policy to update.</p>
            quota_share_policy: <p>The quota share scheduling policy details. Once set during creation, a quotaSharePolicy cannot be removed or changed to a fairsharePolicy.</p>
            fairshare_policy: <p>The fair-share policy scheduling details. Once set during creation, a fairsharePolicy cannot be removed or changed to a quotaSharePolicy.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.update_scheduling_policy_request.UpdateSchedulingPolicyRequest]",
        ) -> OperationResponse[
            "capo_batch.types.update_scheduling_policy_response.UpdateSchedulingPolicyResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.update_scheduling_policy

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.update_scheduling_policy.update_scheduling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.update_scheduling_policy_request.UpdateSchedulingPolicyRequest = {}
        if arn is not None:
            input_["arn"] = arn
        if quota_share_policy is not None:
            input_["quota_share_policy"] = quota_share_policy
        if fairshare_policy is not None:
            input_["fairshare_policy"] = fairshare_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_environment(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        service_environment: Optional["capo_batch.types.string.String"] = None,
        state: Optional[
            "capo_batch.types.service_environment_state.ServiceEnvironmentState"
        ] = None,
        capacity_limits: Optional[
            "capo_batch.types.capacity_limits.CapacityLimits"
        ] = None,
    ) -> "capo_batch.types.update_service_environment_response.UpdateServiceEnvironmentResponse":
        """<p>Updates a service environment. You can update the state of a service environment from <code>ENABLED</code> to <code>DISABLED</code> to prevent new service jobs from being placed in the service environment.</p>

        Args:
            service_environment: <p>The name or ARN of the service environment to update.</p>
            state: <p>The state of the service environment. </p>
            capacity_limits: <p>The capacity limits for the service environment. This defines the maximum resources that can be used by service jobs in this environment.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.update_service_environment_request.UpdateServiceEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_batch.types.update_service_environment_response.UpdateServiceEnvironmentResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.update_service_environment

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.update_service_environment.update_service_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.update_service_environment_request.UpdateServiceEnvironmentRequest = {}
        if service_environment is not None:
            input_["service_environment"] = service_environment
        if state is not None:
            input_["state"] = state
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_job(
        self,
        *,
        config_overrides: Optional[BatchClientConfig] = None,
        job_id: Optional["capo_batch.types.string.String"] = None,
        scheduling_priority: Optional["capo_batch.types.integer.Integer"] = None,
    ) -> "capo_batch.types.update_service_job_response.UpdateServiceJobResponse":
        """<p>Updates the priority of a specified service job in an Batch job queue.</p>

        Args:
            job_id: <p>The Batch job ID of the job to update.</p>
            scheduling_priority: <p>The scheduling priority for the job. This only affects jobs in job queues with a quota-share or fair-share scheduling policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority within a share.</p> <p>The minimum supported value is 0 and the maximum supported value is 9999.</p>

        Raises:
            capo_batch.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.</p>
            capo_batch.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_batch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_batch.types.update_service_job_request.UpdateServiceJobRequest]",
        ) -> OperationResponse[
            "capo_batch.types.update_service_job_response.UpdateServiceJobResponse"
        ]:
            import capo_batch._operations.aws_batch_v20160810.update_service_job

            output, http_response = (
                capo_batch._operations.aws_batch_v20160810.update_service_job.update_service_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_batch.types.update_service_job_request.UpdateServiceJobRequest = {}
        if job_id is not None:
            input_["job_id"] = job_id
        if scheduling_priority is not None:
            input_["scheduling_priority"] = scheduling_priority

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
