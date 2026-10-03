"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#AnyScaleFrontendService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_application_auto_scaling._auth._signers
import capo_application_auto_scaling._auth._sigv4
from capo_application_auto_scaling._auth._identity import Credentials
from capo_application_auto_scaling._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_application_auto_scaling._auth._zapros_handler import AuthMiddleware
from capo_application_auto_scaling._pagination import resolve_path as _resolve_path
from capo_application_auto_scaling._services._aws_config import aws_config
from capo_application_auto_scaling._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.amazon_resource_name
    import capo_application_auto_scaling.types.delete_scaling_policy_request
    import capo_application_auto_scaling.types.delete_scaling_policy_response
    import capo_application_auto_scaling.types.delete_scheduled_action_request
    import capo_application_auto_scaling.types.delete_scheduled_action_response
    import capo_application_auto_scaling.types.deregister_scalable_target_request
    import capo_application_auto_scaling.types.deregister_scalable_target_response
    import capo_application_auto_scaling.types.describe_scalable_targets_request
    import capo_application_auto_scaling.types.describe_scalable_targets_response
    import capo_application_auto_scaling.types.describe_scaling_activities_request
    import capo_application_auto_scaling.types.describe_scaling_activities_response
    import capo_application_auto_scaling.types.describe_scaling_policies_request
    import capo_application_auto_scaling.types.describe_scaling_policies_response
    import capo_application_auto_scaling.types.describe_scheduled_actions_request
    import capo_application_auto_scaling.types.describe_scheduled_actions_response
    import capo_application_auto_scaling.types.get_predictive_scaling_forecast_request
    import capo_application_auto_scaling.types.get_predictive_scaling_forecast_response
    import capo_application_auto_scaling.types.include_not_scaled_activities
    import capo_application_auto_scaling.types.list_tags_for_resource_request
    import capo_application_auto_scaling.types.list_tags_for_resource_response
    import capo_application_auto_scaling.types.max_results
    import capo_application_auto_scaling.types.policy_name
    import capo_application_auto_scaling.types.policy_type
    import capo_application_auto_scaling.types.predictive_scaling_policy_configuration
    import capo_application_auto_scaling.types.put_scaling_policy_request
    import capo_application_auto_scaling.types.put_scaling_policy_response
    import capo_application_auto_scaling.types.put_scheduled_action_request
    import capo_application_auto_scaling.types.put_scheduled_action_response
    import capo_application_auto_scaling.types.register_scalable_target_request
    import capo_application_auto_scaling.types.register_scalable_target_response
    import capo_application_auto_scaling.types.resource_capacity
    import capo_application_auto_scaling.types.resource_id_max_len1600
    import capo_application_auto_scaling.types.resource_ids_max_len1600
    import capo_application_auto_scaling.types.scalable_dimension
    import capo_application_auto_scaling.types.scalable_target
    import capo_application_auto_scaling.types.scalable_target_action
    import capo_application_auto_scaling.types.scaling_activity
    import capo_application_auto_scaling.types.scaling_policy
    import capo_application_auto_scaling.types.scheduled_action
    import capo_application_auto_scaling.types.scheduled_action_name
    import capo_application_auto_scaling.types.service_namespace
    import capo_application_auto_scaling.types.step_scaling_policy_configuration
    import capo_application_auto_scaling.types.suspended_state
    import capo_application_auto_scaling.types.tag_key_list
    import capo_application_auto_scaling.types.tag_map
    import capo_application_auto_scaling.types.tag_resource_request
    import capo_application_auto_scaling.types.tag_resource_response
    import capo_application_auto_scaling.types.target_tracking_scaling_policy_configuration
    import capo_application_auto_scaling.types.timestamp_type
    import capo_application_auto_scaling.types.untag_resource_request
    import capo_application_auto_scaling.types.untag_resource_response
    import capo_application_auto_scaling.types.xml_string


class ApplicationAutoScalingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ApplicationAutoScalingClient:
    """A client for the ``ApplicationAutoScaling`` service.

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
        self._config = ApplicationAutoScalingClientConfig(
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
        self, config_overrides: Optional[ApplicationAutoScalingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ApplicationAutoScalingClientConfig = config_overrides or {}
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

    def delete_scaling_policy(
        self,
        policy_name: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600",
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600",
        scalable_dimension: "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
    ) -> "capo_application_auto_scaling.types.delete_scaling_policy_response.DeleteScalingPolicyResponse":
        """<p>Deletes the specified scaling policy for an Application Auto Scaling scalable target.</p> <p>Deleting a step scaling policy deletes the underlying alarm action, but does not delete the CloudWatch alarm associated with the scaling policy, even if it no longer has an associated action.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/create-step-scaling-policy-cli.html#delete-step-scaling-policy">Delete a step scaling policy</a> and <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/create-target-tracking-policy-cli.html#delete-target-tracking-policy">Delete a target tracking scaling policy</a> in the <i>Application Auto Scaling User Guide</i>.</p>

        Args:
            policy_name: <p>The name of the scaling policy.</p>
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            resource_id: <p>The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.object_not_found_exception.ObjectNotFoundException: <p>The specified object could not be found. For any operation that depends on the existence of a scalable target, this exception is thrown if the scalable target with the specified service namespace, resource ID, and scalable dimension does not exist. For any operation that deletes or deregisters a resource, this exception is thrown if the resource cannot be found.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a scaling policy
            This example deletes a scaling policy for the Amazon ECS service called web-app, which is running in the default cluster.

            >>> client.delete_scaling_policy(policy_name='web-app-cpu-lt-25', service_namespace='ecs', resource_id='service/default/web-app', scalable_dimension='ecs:service:DesiredCount')
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.delete_scaling_policy_request.DeleteScalingPolicyRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.delete_scaling_policy_response.DeleteScalingPolicyResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.delete_scaling_policy

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.delete_scaling_policy.delete_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.delete_scaling_policy_request.DeleteScalingPolicyRequest = {
            "policy_name": policy_name,
            "service_namespace": service_namespace,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_scheduled_action(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        scheduled_action_name: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600",
        resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600",
        scalable_dimension: "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
    ) -> "capo_application_auto_scaling.types.delete_scheduled_action_response.DeleteScheduledActionResponse":
        """<p>Deletes the specified scheduled action for an Application Auto Scaling scalable target.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-additional-cli-commands.html#delete-scheduled-action">Delete a scheduled action</a> in the <i>Application Auto Scaling User Guide</i>.</p>

        Args:
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            scheduled_action_name: <p>The name of the scheduled action.</p>
            resource_id: <p>The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.object_not_found_exception.ObjectNotFoundException: <p>The specified object could not be found. For any operation that depends on the existence of a scalable target, this exception is thrown if the scalable target with the specified service namespace, resource ID, and scalable dimension does not exist. For any operation that deletes or deregisters a resource, this exception is thrown if the resource cannot be found.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a scheduled action
            This example deletes a scheduled action for the AppStream 2.0 fleet called sample-fleet.

            >>> client.delete_scheduled_action(service_namespace='appstream', scheduled_action_name='my-recurring-action', resource_id='fleet/sample-fleet', scalable_dimension='appstream:fleet:DesiredCapacity')
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.delete_scheduled_action_request.DeleteScheduledActionRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.delete_scheduled_action_response.DeleteScheduledActionResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.delete_scheduled_action

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.delete_scheduled_action.delete_scheduled_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.delete_scheduled_action_request.DeleteScheduledActionRequest = {
            "service_namespace": service_namespace,
            "scheduled_action_name": scheduled_action_name,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_scalable_target(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600",
        scalable_dimension: "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
    ) -> "capo_application_auto_scaling.types.deregister_scalable_target_response.DeregisterScalableTargetResponse":
        """<p>Deregisters an Application Auto Scaling scalable target when you have finished using it. To see which resources have been registered, use <a href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html">DescribeScalableTargets</a>. </p> <note> <p>Deregistering a scalable target deletes the scaling policies and the scheduled actions that are associated with it.</p> </note>

        Args:
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            resource_id: <p>The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.object_not_found_exception.ObjectNotFoundException: <p>The specified object could not be found. For any operation that depends on the existence of a scalable target, this exception is thrown if the scalable target with the specified service namespace, resource ID, and scalable dimension does not exist. For any operation that deletes or deregisters a resource, this exception is thrown if the resource cannot be found.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deregister a scalable target
            This example deregisters a scalable target for an Amazon ECS service called web-app that is running in the default cluster.

            >>> client.deregister_scalable_target(service_namespace='ecs', resource_id='service/default/web-app', scalable_dimension='ecs:service:DesiredCount')
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.deregister_scalable_target_request.DeregisterScalableTargetRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.deregister_scalable_target_response.DeregisterScalableTargetResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.deregister_scalable_target

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.deregister_scalable_target.deregister_scalable_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.deregister_scalable_target_request.DeregisterScalableTargetRequest = {
            "service_namespace": service_namespace,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_scalable_targets(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        resource_ids: Optional[
            "capo_application_auto_scaling.types.resource_ids_max_len1600.ResourceIdsMaxLen1600"
        ] = None,
        scalable_dimension: Optional[
            "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
        ] = None,
        max_results: Optional[
            "capo_application_auto_scaling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_auto_scaling.types.xml_string.XmlString"
        ] = None,
    ) -> "capo_application_auto_scaling.types.describe_scalable_targets_response.DescribeScalableTargetsResponse":
        """<p>Gets information about the scalable targets in the specified namespace.</p> <p>You can filter the results using <code>ResourceIds</code> and <code>ScalableDimension</code>.</p>

        Args:
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            resource_ids: <p>The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>
            max_results: <p>The maximum number of scalable targets. This value can be between 1 and 50. The default value is 50.</p> <p>If this parameter is used, the operation returns up to <code>MaxResults</code> results at a time, along with a <code>NextToken</code> value. To get the next set of results, include the <code>NextToken</code> value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a <code>NextToken</code> value, if applicable.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token supplied was invalid.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe scalable targets
            This example describes the scalable targets for the ECS service namespace.

            >>> client.describe_scalable_targets(service_namespace='ecs')
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.describe_scalable_targets_request.DescribeScalableTargetsRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.describe_scalable_targets_response.DescribeScalableTargetsResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.describe_scalable_targets

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.describe_scalable_targets.describe_scalable_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.describe_scalable_targets_request.DescribeScalableTargetsRequest = {
            "service_namespace": service_namespace
        }
        if resource_ids is not None:
            input_["resource_ids"] = resource_ids
        if scalable_dimension is not None:
            input_["scalable_dimension"] = scalable_dimension
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

    def iter_describe_scalable_targets(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        resource_ids: Optional[
            "capo_application_auto_scaling.types.resource_ids_max_len1600.ResourceIdsMaxLen1600"
        ] = None,
        scalable_dimension: Optional[
            "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
        ] = None,
        max_results: Optional[
            "capo_application_auto_scaling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_auto_scaling.types.xml_string.XmlString"
        ] = None,
    ) -> "Iterator[capo_application_auto_scaling.types.scalable_target.ScalableTarget]":
        _token = next_token
        while True:
            _response = self.describe_scalable_targets(
                service_namespace,
                config_overrides=config_overrides,
                resource_ids=resource_ids,
                scalable_dimension=scalable_dimension,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scalable_targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_scaling_activities(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        resource_id: Optional[
            "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
        ] = None,
        scalable_dimension: Optional[
            "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
        ] = None,
        max_results: Optional[
            "capo_application_auto_scaling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_auto_scaling.types.xml_string.XmlString"
        ] = None,
        include_not_scaled_activities: Optional[
            "capo_application_auto_scaling.types.include_not_scaled_activities.IncludeNotScaledActivities"
        ] = None,
    ) -> "capo_application_auto_scaling.types.describe_scaling_activities_response.DescribeScalingActivitiesResponse":
        """<p>Provides descriptive information about the scaling activities in the specified namespace from the previous six weeks.</p> <p>You can filter the results using <code>ResourceId</code> and <code>ScalableDimension</code>.</p> <p>For information about viewing scaling activities using the Amazon Web Services CLI, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scaling-activities.html">Scaling activities for Application Auto Scaling</a>.</p>

        Args:
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            resource_id: <p>The identifier of the resource associated with the scaling activity. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>
            max_results: <p>The maximum number of scalable targets. This value can be between 1 and 50. The default value is 50.</p> <p>If this parameter is used, the operation returns up to <code>MaxResults</code> results at a time, along with a <code>NextToken</code> value. To get the next set of results, include the <code>NextToken</code> value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a <code>NextToken</code> value, if applicable.</p>
            next_token: <p>The token for the next set of results.</p>
            include_not_scaled_activities: <p>Specifies whether to include activities that aren't scaled (<i>not scaled activities</i>) in the response. Not scaled activities are activities that aren't completed or started for various reasons, such as preventing infinite scaling loops. For help interpreting the not scaled reason details in the response, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scaling-activities.html">Scaling activities for Application Auto Scaling</a>.</p>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token supplied was invalid.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe scaling activities for a scalable target
            This example describes the scaling activities for an Amazon ECS service called web-app that is running in the default cluster.

            >>> client.describe_scaling_activities(service_namespace='ecs', resource_id='service/default/web-app', scalable_dimension='ecs:service:DesiredCount')
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.describe_scaling_activities_request.DescribeScalingActivitiesRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.describe_scaling_activities_response.DescribeScalingActivitiesResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.describe_scaling_activities

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.describe_scaling_activities.describe_scaling_activities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.describe_scaling_activities_request.DescribeScalingActivitiesRequest = {
            "service_namespace": service_namespace
        }
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if scalable_dimension is not None:
            input_["scalable_dimension"] = scalable_dimension
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_not_scaled_activities is not None:
            input_["include_not_scaled_activities"] = include_not_scaled_activities

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_scaling_activities(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        resource_id: Optional[
            "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
        ] = None,
        scalable_dimension: Optional[
            "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
        ] = None,
        max_results: Optional[
            "capo_application_auto_scaling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_auto_scaling.types.xml_string.XmlString"
        ] = None,
        include_not_scaled_activities: Optional[
            "capo_application_auto_scaling.types.include_not_scaled_activities.IncludeNotScaledActivities"
        ] = None,
    ) -> (
        "Iterator[capo_application_auto_scaling.types.scaling_activity.ScalingActivity]"
    ):
        _token = next_token
        while True:
            _response = self.describe_scaling_activities(
                service_namespace,
                config_overrides=config_overrides,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                max_results=max_results,
                next_token=_token,
                include_not_scaled_activities=include_not_scaled_activities,
            )
            _page = _resolve_path(_response, ("scaling_activities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_scaling_policies(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        policy_names: Optional[
            "capo_application_auto_scaling.types.resource_ids_max_len1600.ResourceIdsMaxLen1600"
        ] = None,
        resource_id: Optional[
            "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
        ] = None,
        scalable_dimension: Optional[
            "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
        ] = None,
        max_results: Optional[
            "capo_application_auto_scaling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_auto_scaling.types.xml_string.XmlString"
        ] = None,
    ) -> "capo_application_auto_scaling.types.describe_scaling_policies_response.DescribeScalingPoliciesResponse":
        """<p>Describes the Application Auto Scaling scaling policies for the specified service namespace.</p> <p>You can filter the results using <code>ResourceId</code>, <code>ScalableDimension</code>, and <code>PolicyNames</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html">Target tracking scaling policies</a> and <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html">Step scaling policies</a> in the <i>Application Auto Scaling User Guide</i>.</p>

        Args:
            policy_names: <p>The names of the scaling policies to describe.</p>
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            resource_id: <p>The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>
            max_results: <p>The maximum number of scalable targets. This value can be between 1 and 10. The default value is 10.</p> <p>If this parameter is used, the operation returns up to <code>MaxResults</code> results at a time, along with a <code>NextToken</code> value. To get the next set of results, include the <code>NextToken</code> value in a subsequent call. If this parameter is not used, the operation returns up to 10 results and a <code>NextToken</code> value, if applicable.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.failed_resource_access_exception.FailedResourceAccessException: <p>Failed access to resources caused an exception. This exception is thrown when Application Auto Scaling is unable to retrieve the alarms associated with a scaling policy due to a client error, for example, if the role ARN specified for a scalable target does not have permission to call the CloudWatch <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html">DescribeAlarms</a> on your behalf.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token supplied was invalid.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe scaling policies
            This example describes the scaling policies for the ECS service namespace.

            >>> client.describe_scaling_policies(service_namespace='ecs')
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.describe_scaling_policies_request.DescribeScalingPoliciesRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.describe_scaling_policies_response.DescribeScalingPoliciesResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.describe_scaling_policies

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.describe_scaling_policies.describe_scaling_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.describe_scaling_policies_request.DescribeScalingPoliciesRequest = {
            "service_namespace": service_namespace
        }
        if policy_names is not None:
            input_["policy_names"] = policy_names
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if scalable_dimension is not None:
            input_["scalable_dimension"] = scalable_dimension
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

    def iter_describe_scaling_policies(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        policy_names: Optional[
            "capo_application_auto_scaling.types.resource_ids_max_len1600.ResourceIdsMaxLen1600"
        ] = None,
        resource_id: Optional[
            "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
        ] = None,
        scalable_dimension: Optional[
            "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
        ] = None,
        max_results: Optional[
            "capo_application_auto_scaling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_auto_scaling.types.xml_string.XmlString"
        ] = None,
    ) -> "Iterator[capo_application_auto_scaling.types.scaling_policy.ScalingPolicy]":
        _token = next_token
        while True:
            _response = self.describe_scaling_policies(
                service_namespace,
                config_overrides=config_overrides,
                policy_names=policy_names,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scaling_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_scheduled_actions(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        scheduled_action_names: Optional[
            "capo_application_auto_scaling.types.resource_ids_max_len1600.ResourceIdsMaxLen1600"
        ] = None,
        resource_id: Optional[
            "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
        ] = None,
        scalable_dimension: Optional[
            "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
        ] = None,
        max_results: Optional[
            "capo_application_auto_scaling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_auto_scaling.types.xml_string.XmlString"
        ] = None,
    ) -> "capo_application_auto_scaling.types.describe_scheduled_actions_response.DescribeScheduledActionsResponse":
        """<p>Describes the Application Auto Scaling scheduled actions for the specified service namespace.</p> <p>You can filter the results using the <code>ResourceId</code>, <code>ScalableDimension</code>, and <code>ScheduledActionNames</code> parameters.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html">Scheduled scaling</a> in the <i>Application Auto Scaling User Guide</i>.</p>

        Args:
            scheduled_action_names: <p>The names of the scheduled actions to describe.</p>
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            resource_id: <p>The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>
            max_results: <p>The maximum number of scheduled action results. This value can be between 1 and 50. The default value is 50.</p> <p>If this parameter is used, the operation returns up to <code>MaxResults</code> results at a time, along with a <code>NextToken</code> value. To get the next set of results, include the <code>NextToken</code> value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a <code>NextToken</code> value, if applicable.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token supplied was invalid.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe scheduled actions
            This example describes the scheduled actions for the dynamodb service namespace.

            >>> client.describe_scheduled_actions(service_namespace='dynamodb')
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.describe_scheduled_actions_request.DescribeScheduledActionsRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.describe_scheduled_actions_response.DescribeScheduledActionsResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.describe_scheduled_actions

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.describe_scheduled_actions.describe_scheduled_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.describe_scheduled_actions_request.DescribeScheduledActionsRequest = {
            "service_namespace": service_namespace
        }
        if scheduled_action_names is not None:
            input_["scheduled_action_names"] = scheduled_action_names
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if scalable_dimension is not None:
            input_["scalable_dimension"] = scalable_dimension
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

    def iter_describe_scheduled_actions(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        scheduled_action_names: Optional[
            "capo_application_auto_scaling.types.resource_ids_max_len1600.ResourceIdsMaxLen1600"
        ] = None,
        resource_id: Optional[
            "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
        ] = None,
        scalable_dimension: Optional[
            "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
        ] = None,
        max_results: Optional[
            "capo_application_auto_scaling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_auto_scaling.types.xml_string.XmlString"
        ] = None,
    ) -> (
        "Iterator[capo_application_auto_scaling.types.scheduled_action.ScheduledAction]"
    ):
        _token = next_token
        while True:
            _response = self.describe_scheduled_actions(
                service_namespace,
                config_overrides=config_overrides,
                scheduled_action_names=scheduled_action_names,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scheduled_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_predictive_scaling_forecast(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600",
        scalable_dimension: "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension",
        policy_name: "capo_application_auto_scaling.types.policy_name.PolicyName",
        start_time: "capo_application_auto_scaling.types.timestamp_type.TimestampType",
        end_time: "capo_application_auto_scaling.types.timestamp_type.TimestampType",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
    ) -> "capo_application_auto_scaling.types.get_predictive_scaling_forecast_response.GetPredictiveScalingForecastResponse":
        """<p>Retrieves the forecast data for a predictive scaling policy.</p> <p>Load forecasts are predictions of the hourly load values using historical load data from CloudWatch and an analysis of historical trends. Capacity forecasts are represented as predicted values for the minimum capacity that is needed on an hourly basis, based on the hourly load forecast.</p> <p>A minimum of 24 hours of data is required to create the initial forecasts. However, having a full 14 days of historical data results in more accurate forecasts.</p>

        Args:
            service_namespace: <p> The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead. </p>
            resource_id: <p> The identifier of the resource. </p>
            scalable_dimension: <p> The scalable dimension. </p>
            policy_name: <p>The name of the policy.</p>
            start_time: <p> The inclusive start time of the time range for the forecast data to get. At most, the date and time can be one year before the current date and time </p>
            end_time: <p> The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is 30 days. </p>

        Raises:
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.get_predictive_scaling_forecast_request.GetPredictiveScalingForecastRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.get_predictive_scaling_forecast_response.GetPredictiveScalingForecastResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.get_predictive_scaling_forecast

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.get_predictive_scaling_forecast.get_predictive_scaling_forecast(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.get_predictive_scaling_forecast_request.GetPredictiveScalingForecastRequest = {
            "service_namespace": service_namespace,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "policy_name": policy_name,
            "start_time": start_time,
            "end_time": end_time,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_application_auto_scaling.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
    ) -> "capo_application_auto_scaling.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns all the tags on the specified Application Auto Scaling scalable target.</p> <p>For general information about tags, including the format and syntax, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging your Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Args:
            resource_arn: <p>Specify the ARN of the scalable target.</p> <p>For example: <code>arn:aws:application-autoscaling:us-east-1:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123</code> </p> <p>To get the ARN for a scalable target, use <a>DescribeScalableTargets</a>.</p>

        Raises:
            capo_application_auto_scaling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list tags for a scalable target
            This example lists the tag key names and values that are attached to the scalable target specified by its ARN.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123')
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.list_tags_for_resource

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_scaling_policy(
        self,
        policy_name: "capo_application_auto_scaling.types.policy_name.PolicyName",
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600",
        scalable_dimension: "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        policy_type: Optional[
            "capo_application_auto_scaling.types.policy_type.PolicyType"
        ] = None,
        step_scaling_policy_configuration: Optional[
            "capo_application_auto_scaling.types.step_scaling_policy_configuration.StepScalingPolicyConfiguration"
        ] = None,
        target_tracking_scaling_policy_configuration: Optional[
            "capo_application_auto_scaling.types.target_tracking_scaling_policy_configuration.TargetTrackingScalingPolicyConfiguration"
        ] = None,
        predictive_scaling_policy_configuration: Optional[
            "capo_application_auto_scaling.types.predictive_scaling_policy_configuration.PredictiveScalingPolicyConfiguration"
        ] = None,
    ) -> "capo_application_auto_scaling.types.put_scaling_policy_response.PutScalingPolicyResponse":
        """<p>Creates or updates a scaling policy for an Application Auto Scaling scalable target.</p> <p>Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scaling policy applies to the scalable target identified by those three attributes. You cannot create a scaling policy until you have registered the resource as a scalable target.</p> <p>Multiple scaling policies can be in force at the same time for the same scalable target. You can have one or more target tracking scaling policies, one or more step scaling policies, or both. However, there is a chance that multiple policies could conflict, instructing the scalable target to scale out or in at the same time. Application Auto Scaling gives precedence to the policy that provides the largest capacity for both scale out and scale in. For example, if one policy increases capacity by 3, another policy increases capacity by 200 percent, and the current capacity is 10, Application Auto Scaling uses the policy with the highest calculated capacity (200% of 10 = 20) and scales out to 30. </p> <p>We recommend caution, however, when using target tracking scaling policies with step scaling policies because conflicts between these policies can cause undesirable behavior. For example, if the step scaling policy initiates a scale-in activity before the target tracking policy is ready to scale in, the scale-in activity will not be blocked. After the scale-in activity completes, the target tracking policy could instruct the scalable target to scale out again. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html">Target tracking scaling policies</a>, <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html">Step scaling policies</a>, and <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/aas-create-predictive-scaling-policy.html">Predictive scaling policies</a> in the <i>Application Auto Scaling User Guide</i>.</p> <note> <p>If a scalable target is deregistered, the scalable target is no longer available to use scaling policies. Any scaling policies that were specified for the scalable target are deleted.</p> </note>

        Args:
            policy_name: <p>The name of the scaling policy.</p> <p>You cannot change the name of a scaling policy, but you can delete the original scaling policy and create a new scaling policy with the same settings and a different name.</p>
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            resource_id: <p>The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>
            policy_type: <p>The scaling policy type. This parameter is required if you are creating a scaling policy.</p> <p>The following policy types are supported: </p> <p> <code>TargetTrackingScaling</code>—Not supported for Amazon EMR.</p> <p> <code>StepScaling</code>—Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.</p> <p> <code>PredictiveScaling</code>—Only supported for Amazon ECS.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html">Target tracking scaling policies</a>, <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html">Step scaling policies</a>, and <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/aas-create-predictive-scaling-policy.html">Predictive scaling policies</a> in the <i>Application Auto Scaling User Guide</i>.</p>
            step_scaling_policy_configuration: <p>A step scaling policy.</p> <p>This parameter is required if you are creating a policy and the policy type is <code>StepScaling</code>.</p>
            target_tracking_scaling_policy_configuration: <p>A target tracking scaling policy. Includes support for predefined or customized metrics.</p> <p>This parameter is required if you are creating a policy and the policy type is <code>TargetTrackingScaling</code>.</p>
            predictive_scaling_policy_configuration: <p> The configuration of the predictive scaling policy. </p>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.failed_resource_access_exception.FailedResourceAccessException: <p>Failed access to resources caused an exception. This exception is thrown when Application Auto Scaling is unable to retrieve the alarms associated with a scaling policy due to a client error, for example, if the role ARN specified for a scalable target does not have permission to call the CloudWatch <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html">DescribeAlarms</a> on your behalf.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.limit_exceeded_exception.LimitExceededException: <p>A per-account resource limit is exceeded. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-limits.html">Application Auto Scaling service quotas</a>.</p>
            capo_application_auto_scaling.errors.object_not_found_exception.ObjectNotFoundException: <p>The specified object could not be found. For any operation that depends on the existence of a scalable target, this exception is thrown if the scalable target with the specified service namespace, resource ID, and scalable dimension does not exist. For any operation that deletes or deregisters a resource, this exception is thrown if the resource cannot be found.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To apply a target tracking scaling policy with a predefined metric specification
            The following example applies a target tracking scaling policy with a predefined metric specification to an Amazon ECS service called web-app in the default cluster. The policy keeps the average CPU utilization of the service at 75 percent, with scale-out and scale-in cooldown periods of 60 seconds.

            >>> client.put_scaling_policy(policy_name='cpu75-target-tracking-scaling-policy', service_namespace='ecs', resource_id='service/default/web-app', scalable_dimension='ecs:service:DesiredCount', policy_type='TargetTrackingScaling', target_tracking_scaling_policy_configuration={'TargetValue': 75, 'PredefinedMetricSpecification': {'PredefinedMetricType': 'ECSServiceAverageCPUUtilization'}, 'ScaleOutCooldown': 60, 'ScaleInCooldown': 60})
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.put_scaling_policy_request.PutScalingPolicyRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.put_scaling_policy_response.PutScalingPolicyResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.put_scaling_policy

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.put_scaling_policy.put_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.put_scaling_policy_request.PutScalingPolicyRequest = {
            "policy_name": policy_name,
            "service_namespace": service_namespace,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
        }
        if policy_type is not None:
            input_["policy_type"] = policy_type
        if step_scaling_policy_configuration is not None:
            input_["step_scaling_policy_configuration"] = (
                step_scaling_policy_configuration
            )
        if target_tracking_scaling_policy_configuration is not None:
            input_["target_tracking_scaling_policy_configuration"] = (
                target_tracking_scaling_policy_configuration
            )
        if predictive_scaling_policy_configuration is not None:
            input_["predictive_scaling_policy_configuration"] = (
                predictive_scaling_policy_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_scheduled_action(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        scheduled_action_name: "capo_application_auto_scaling.types.scheduled_action_name.ScheduledActionName",
        resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600",
        scalable_dimension: "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        schedule: Optional[
            "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
        ] = None,
        timezone: Optional[
            "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
        ] = None,
        start_time: Optional[
            "capo_application_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
        end_time: Optional[
            "capo_application_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
        scalable_target_action: Optional[
            "capo_application_auto_scaling.types.scalable_target_action.ScalableTargetAction"
        ] = None,
    ) -> "capo_application_auto_scaling.types.put_scheduled_action_response.PutScheduledActionResponse":
        """<p>Creates or updates a scheduled action for an Application Auto Scaling scalable target. </p> <p>Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scheduled action applies to the scalable target identified by those three attributes. You cannot create a scheduled action until you have registered the resource as a scalable target.</p> <p>When you specify start and end times with a recurring schedule using a cron expression or rates, they form the boundaries for when the recurring action starts and stops.</p> <p>To update a scheduled action, specify the parameters that you want to change. If you don't specify start and end times, the old values are deleted.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html">Scheduled scaling</a> in the <i>Application Auto Scaling User Guide</i>.</p> <note> <p>If a scalable target is deregistered, the scalable target is no longer available to run scheduled actions. Any scheduled actions that were specified for the scalable target are deleted.</p> </note>

        Args:
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            schedule: <p>The schedule for this action. The following formats are supported:</p> <ul> <li> <p>At expressions - "<code>at(<i>yyyy</i>-<i>mm</i>-<i>dd</i>T<i>hh</i>:<i>mm</i>:<i>ss</i>)</code>"</p> </li> <li> <p>Rate expressions - "<code>rate(<i>value</i> <i>unit</i>)</code>"</p> </li> <li> <p>Cron expressions - "<code>cron(<i>fields</i>)</code>"</p> </li> </ul> <p>At expressions are useful for one-time schedules. Cron expressions are useful for scheduled actions that run periodically at a specified date and time, and rate expressions are useful for scheduled actions that run at a regular interval.</p> <p>At and cron expressions use Universal Coordinated Time (UTC) by default.</p> <p>The cron format consists of six fields separated by white spaces: [Minutes] [Hours] [Day_of_Month] [Month] [Day_of_Week] [Year].</p> <p>For rate expressions, <i>value</i> is a positive integer and <i>unit</i> is <code>minute</code> | <code>minutes</code> | <code>hour</code> | <code>hours</code> | <code>day</code> | <code>days</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-using-cron-expressions.html">Schedule recurring scaling actions using cron expressions</a> in the <i>Application Auto Scaling User Guide</i>.</p>
            timezone: <p>Specifies the time zone used when setting a scheduled action by using an at or cron expression. If a time zone is not provided, UTC is used by default.</p> <p>Valid values are the canonical names of the IANA time zones supported by Joda-Time (such as <code>Etc/GMT+9</code> or <code>Pacific/Tahiti</code>). For more information, see <a href="https://www.joda.org/joda-time/timezones.html">https://www.joda.org/joda-time/timezones.html</a>.</p>
            scheduled_action_name: <p>The name of the scheduled action. This name must be unique among all other scheduled actions on the specified scalable target. </p>
            resource_id: <p>The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>
            start_time: <p>The date and time for this scheduled action to start, in UTC.</p>
            end_time: <p>The date and time for the recurring schedule to end, in UTC.</p>
            scalable_target_action: <p>The new minimum and maximum capacity. You can set both values or just one. At the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.</p>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.limit_exceeded_exception.LimitExceededException: <p>A per-account resource limit is exceeded. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-limits.html">Application Auto Scaling service quotas</a>.</p>
            capo_application_auto_scaling.errors.object_not_found_exception.ObjectNotFoundException: <p>The specified object could not be found. For any operation that depends on the existence of a scalable target, this exception is thrown if the scalable target with the specified service namespace, resource ID, and scalable dimension does not exist. For any operation that deletes or deregisters a resource, this exception is thrown if the resource cannot be found.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a recurring scheduled action
            This example adds a scheduled action to a DynamoDB table called TestTable to scale out on a recurring schedule. On the specified schedule (every day at 12:15pm UTC), if the current capacity is below the value specified for MinCapacity, Application Auto Scaling scales out to the value specified by MinCapacity.

            >>> client.put_scheduled_action(service_namespace='dynamodb', schedule='cron(15 12 * * ? *)', scheduled_action_name='my-recurring-action', resource_id='table/TestTable', scalable_dimension='dynamodb:table:WriteCapacityUnits', scalable_target_action={'MinCapacity': 6})
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.put_scheduled_action_request.PutScheduledActionRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.put_scheduled_action_response.PutScheduledActionResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.put_scheduled_action

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.put_scheduled_action.put_scheduled_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.put_scheduled_action_request.PutScheduledActionRequest = {
            "service_namespace": service_namespace,
            "scheduled_action_name": scheduled_action_name,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
        }
        if schedule is not None:
            input_["schedule"] = schedule
        if timezone is not None:
            input_["timezone"] = timezone
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if scalable_target_action is not None:
            input_["scalable_target_action"] = scalable_target_action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_scalable_target(
        self,
        service_namespace: "capo_application_auto_scaling.types.service_namespace.ServiceNamespace",
        resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600",
        scalable_dimension: "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
        min_capacity: Optional[
            "capo_application_auto_scaling.types.resource_capacity.ResourceCapacity"
        ] = None,
        max_capacity: Optional[
            "capo_application_auto_scaling.types.resource_capacity.ResourceCapacity"
        ] = None,
        role_arn: Optional[
            "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
        ] = None,
        suspended_state: Optional[
            "capo_application_auto_scaling.types.suspended_state.SuspendedState"
        ] = None,
        tags: Optional["capo_application_auto_scaling.types.tag_map.TagMap"] = None,
    ) -> "capo_application_auto_scaling.types.register_scalable_target_response.RegisterScalableTargetResponse":
        """<p>Registers or updates a scalable target, which is the resource that you want to scale.</p> <p>Scalable targets are uniquely identified by the combination of resource ID, scalable dimension, and namespace, which represents some capacity dimension of the underlying service.</p> <p>When you register a new scalable target, you must specify values for the minimum and maximum capacity. If the specified resource is not active in the target service, this operation does not change the resource's current capacity. Otherwise, it changes the resource's current capacity to a value that is inside of this range.</p> <p>If you add a scaling policy, current capacity is adjustable within the specified range when scaling starts. Application Auto Scaling scaling policies will not scale capacity to values that are outside of the minimum and maximum range.</p> <p>After you register a scalable target, you do not need to register it again to use other Application Auto Scaling operations. To see which resources have been registered, use <a href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html">DescribeScalableTargets</a>. You can also view the scaling policies for a service namespace by using <a href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html">DescribeScalableTargets</a>. If you no longer need a scalable target, you can deregister it by using <a href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeregisterScalableTarget.html">DeregisterScalableTarget</a>.</p> <p>To update a scalable target, specify the parameters that you want to change. Include the parameters that identify the scalable target: resource ID, scalable dimension, and namespace. Any parameters that you don't specify are not changed by this update request. </p> <note> <p>If you call the <code>RegisterScalableTarget</code> API operation to create a scalable target, there might be a brief delay until the operation achieves <a href="https://en.wikipedia.org/wiki/Eventual_consistency">eventual consistency</a>. You might become aware of this brief delay if you get unexpected errors when performing sequential operations. The typical strategy is to retry the request, and some Amazon Web Services SDKs include automatic backoff and retry logic.</p> <p>If you call the <code>RegisterScalableTarget</code> API operation to update an existing scalable target, Application Auto Scaling retrieves the current capacity of the resource. If it's below the minimum capacity or above the maximum capacity, Application Auto Scaling adjusts the capacity of the scalable target to place it within these bounds, even if you don't include the <code>MinCapacity</code> or <code>MaxCapacity</code> request parameters.</p> </note>

        Args:
            service_namespace: <p>The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead.</p>
            resource_id: <p>The identifier of the resource that is associated with the scalable target. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>
            scalable_dimension: <p>The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>
            min_capacity: <p>The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand. This property is required when registering a new scalable target.</p> <p>For the following resources, the minimum value allowed is 0.</p> <ul> <li> <p>AppStream 2.0 fleets</p> </li> <li> <p> Aurora DB clusters</p> </li> <li> <p>ECS services</p> </li> <li> <p>EMR clusters</p> </li> <li> <p>Lambda provisioned concurrency</p> </li> <li> <p>SageMaker endpoint variants</p> </li> <li> <p>SageMaker inference components</p> </li> <li> <p>SageMaker serverless endpoint provisioned concurrency</p> </li> <li> <p>Spot Fleets</p> </li> <li> <p>custom resources</p> </li> </ul> <p>It's strongly recommended that you specify a value greater than 0. A value greater than 0 means that data points are continuously reported to CloudWatch that scaling policies can use to scale on a metric like average CPU utilization.</p> <p>For all other resources, the minimum allowed value depends on the type of resource that you are using. If you provide a value that is lower than what a resource can accept, an error occurs. In which case, the error message will provide the minimum value that the resource can accept.</p>
            max_capacity: <p>The maximum value that you plan to scale out to. When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand. This property is required when registering a new scalable target.</p> <p>Although you can specify a large maximum capacity, note that service quotas might impose lower limits. Each service has its own default quotas for the maximum capacity of the resource. If you want to specify a higher limit, you can request an increase. For more information, consult the documentation for that service. For information about the default quotas for each service, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html">Service endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            role_arn: <p>This parameter is required for services that do not support service-linked roles (such as Amazon EMR), and it must specify the ARN of an IAM role that allows Application Auto Scaling to modify the scalable target on your behalf. </p> <p>If the service supports service-linked roles, Application Auto Scaling uses a service-linked role, which it creates if it does not yet exist. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html">How Application Auto Scaling works with IAM</a>.</p>
            suspended_state: <p>An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to <code>true</code> suspends the specified scaling activities. Setting it to <code>false</code> (default) resumes the specified scaling activities. </p> <p> <b>Suspension Outcomes</b> </p> <ul> <li> <p>For <code>DynamicScalingInSuspended</code>, while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended.</p> </li> <li> <p>For <code>DynamicScalingOutSuspended</code>, while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended.</p> </li> <li> <p>For <code>ScheduledScalingSuspended</code>, while a suspension is in effect, all scaling activities that involve scheduled actions are suspended. </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html">Suspend and resume scaling</a> in the <i>Application Auto Scaling User Guide</i>.</p>
            tags: <p>Assigns one or more tags to the scalable target. Use this parameter to tag the scalable target when it is created. To tag an existing scalable target, use the <a>TagResource</a> operation.</p> <p>Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required. You cannot have more than one tag on a scalable target with the same tag key.</p> <p>Use tags to control access to a scalable target. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/resource-tagging-support.html">Tagging support for Application Auto Scaling</a> in the <i>Application Auto Scaling User Guide</i>.</p>

        Raises:
            capo_application_auto_scaling.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.</p>
            capo_application_auto_scaling.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            capo_application_auto_scaling.errors.limit_exceeded_exception.LimitExceededException: <p>A per-account resource limit is exceeded. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-limits.html">Application Auto Scaling service quotas</a>.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register an ECS service as a scalable target
            This example registers a scalable target from an Amazon ECS service called web-app that is running on the default cluster, with a minimum desired count of 1 task and a maximum desired count of 10 tasks.

            >>> client.register_scalable_target(service_namespace='ecs', resource_id='service/default/web-app', scalable_dimension='ecs:service:DesiredCount', min_capacity=1, max_capacity=10)
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.register_scalable_target_request.RegisterScalableTargetRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.register_scalable_target_response.RegisterScalableTargetResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.register_scalable_target

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.register_scalable_target.register_scalable_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.register_scalable_target_request.RegisterScalableTargetRequest = {
            "service_namespace": service_namespace,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
        }
        if min_capacity is not None:
            input_["min_capacity"] = min_capacity
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if suspended_state is not None:
            input_["suspended_state"] = suspended_state
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_application_auto_scaling.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_application_auto_scaling.types.tag_map.TagMap",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
    ) -> (
        "capo_application_auto_scaling.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Adds or edits tags on an Application Auto Scaling scalable target.</p> <p>Each tag consists of a tag key and a tag value, which are both case-sensitive strings. To add a tag, specify a new tag key and a tag value. To edit a tag, specify an existing tag key and a new tag value.</p> <p>You can use this operation to tag an Application Auto Scaling scalable target, but you cannot tag a scaling policy or scheduled action.</p> <p>You can also add tags to an Application Auto Scaling scalable target while creating it (<code>RegisterScalableTarget</code>).</p> <p>For general information about tags, including the format and syntax, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging your Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p> <p>Use tags to control access to a scalable target. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/resource-tagging-support.html">Tagging support for Application Auto Scaling</a> in the <i>Application Auto Scaling User Guide</i>.</p>

        Args:
            resource_arn: <p>Identifies the Application Auto Scaling scalable target that you want to apply tags to.</p> <p>For example: <code>arn:aws:application-autoscaling:us-east-1:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123</code> </p> <p>To get the ARN for a scalable target, use <a>DescribeScalableTargets</a>.</p>
            tags: <p>The tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource.</p> <p>Each tag consists of a tag key and a tag value.</p> <p>You cannot have more than one tag on an Application Auto Scaling scalable target with the same tag key. If you specify an existing tag key with a different tag value, Application Auto Scaling replaces the current tag value with the specified one.</p> <p>For information about the rules that apply to tag keys and tag values, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html">User-defined tag restrictions</a> in the <i>Amazon Web Services Billing User Guide</i>.</p>

        Raises:
            capo_application_auto_scaling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_application_auto_scaling.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains too many tags. Try the request again with fewer tags.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a tag to a scalable target
            This example adds a tag with the key name "environment" and the value "production" to the scalable target specified by its ARN.

            >>> client.tag_resource(resource_arn='arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123', tags={'environment': 'production'})
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.tag_resource

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_application_auto_scaling.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_application_auto_scaling.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ApplicationAutoScalingClientConfig] = None,
    ) -> "capo_application_auto_scaling.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes tags from an Application Auto Scaling scalable target. To delete a tag, specify the tag key and the Application Auto Scaling scalable target.</p>

        Args:
            resource_arn: <p>Identifies the Application Auto Scaling scalable target from which to remove tags.</p> <p>For example: <code>arn:aws:application-autoscaling:us-east-1:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123</code> </p> <p>To get the ARN for a scalable target, use <a>DescribeScalableTargets</a>.</p>
            tag_keys: <p>One or more tag keys. Specify only the tag keys, not the tag values.</p>

        Raises:
            capo_application_auto_scaling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_application_auto_scaling.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the available parameters for the API request.</p>
            capo_application_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove a tag from a scalable target
            This example removes the tag pair with the key name "environment" from the scalable target specified by its ARN.

            >>> client.untag_resource(resource_arn='arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123', tag_keys=['environment'])
        """

        def _handler(
            req: "OperationRequest[capo_application_auto_scaling.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_application_auto_scaling.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_application_auto_scaling._operations.any_scale_frontend_service.untag_resource

            output, http_response = (
                capo_application_auto_scaling._operations.any_scale_frontend_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_auto_scaling.types.untag_resource_request.UntagResourceRequest = {
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
