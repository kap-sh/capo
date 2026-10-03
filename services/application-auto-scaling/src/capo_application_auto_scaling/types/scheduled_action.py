"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScheduledAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.resource_id_max_len1600
    import capo_application_auto_scaling.types.scalable_dimension
    import capo_application_auto_scaling.types.scalable_target_action
    import capo_application_auto_scaling.types.scheduled_action_name
    import capo_application_auto_scaling.types.service_namespace
    import capo_application_auto_scaling.types.timestamp_type


class ScheduledAction(TypedDict, closed=True):
    scheduled_action_name: (
        "capo_application_auto_scaling.types.scheduled_action_name.ScheduledActionName"
    )
    """<p>The name of the scheduled action.</p>"""
    scheduled_action_arn: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    """<p>The Amazon Resource Name (ARN) of the scheduled action.</p>"""
    service_namespace: (
        "capo_application_auto_scaling.types.service_namespace.ServiceNamespace"
    )
    """<p>The namespace of the Amazon Web Services service that provides the resource, or a <code>custom-resource</code>.</p>"""
    schedule: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    """<p>The schedule for this action. The following formats are supported:</p> <ul> <li> <p>At expressions - "<code>at(<i>yyyy</i>-<i>mm</i>-<i>dd</i>T<i>hh</i>:<i>mm</i>:<i>ss</i>)</code>"</p> </li> <li> <p>Rate expressions - "<code>rate(<i>value</i> <i>unit</i>)</code>"</p> </li> <li> <p>Cron expressions - "<code>cron(<i>fields</i>)</code>"</p> </li> </ul> <p>At expressions are useful for one-time schedules. Cron expressions are useful for scheduled actions that run periodically at a specified date and time, and rate expressions are useful for scheduled actions that run at a regular interval.</p> <p>At and cron expressions use Universal Coordinated Time (UTC) by default.</p> <p>The cron format consists of six fields separated by white spaces: [Minutes] [Hours] [Day_of_Month] [Month] [Day_of_Week] [Year].</p> <p>For rate expressions, <i>value</i> is a positive integer and <i>unit</i> is <code>minute</code> | <code>minutes</code> | <code>hour</code> | <code>hours</code> | <code>day</code> | <code>days</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-using-cron-expressions.html">Schedule recurring scaling actions using cron expressions</a> in the <i>Application Auto Scaling User Guide</i>.</p>"""
    timezone: NotRequired[
        "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    ]
    """<p>The time zone used when referring to the date and time of a scheduled action, when the scheduled action uses an at or cron expression.</p>"""
    resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    """<p>The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>"""
    scalable_dimension: NotRequired[
        "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
    ]
    """<p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>"""
    start_time: NotRequired[
        "capo_application_auto_scaling.types.timestamp_type.TimestampType"
    ]
    """<p>The date and time that the action is scheduled to begin, in UTC.</p>"""
    end_time: NotRequired[
        "capo_application_auto_scaling.types.timestamp_type.TimestampType"
    ]
    """<p>The date and time that the action is scheduled to end, in UTC.</p>"""
    scalable_target_action: NotRequired[
        "capo_application_auto_scaling.types.scalable_target_action.ScalableTargetAction"
    ]
    """<p>The new minimum and maximum capacity. You can set both values or just one. At the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.</p>"""
    creation_time: "capo_application_auto_scaling.types.timestamp_type.TimestampType"
    """<p>The date and time that the scheduled action was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledAction) -> dict:
    out: dict = {}
    out["ScheduledActionName"] = value["scheduled_action_name"]
    out["ScheduledActionARN"] = value["scheduled_action_arn"]
    import capo_application_auto_scaling.types.service_namespace

    out["ServiceNamespace"] = (
        capo_application_auto_scaling.types.service_namespace.serialize_aws_json_1_1(
            value["service_namespace"]
        )
    )
    out["Schedule"] = value["schedule"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    out["ResourceId"] = value["resource_id"]
    if "scalable_dimension" in value:
        import capo_application_auto_scaling.types.scalable_dimension

        out["ScalableDimension"] = (
            capo_application_auto_scaling.types.scalable_dimension.serialize_aws_json_1_1(
                value["scalable_dimension"]
            )
        )
    if "start_time" in value:
        import capo_application_auto_scaling.types.timestamp_type

        out["StartTime"] = (
            capo_application_auto_scaling.types.timestamp_type.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_application_auto_scaling.types.timestamp_type

        out["EndTime"] = (
            capo_application_auto_scaling.types.timestamp_type.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "scalable_target_action" in value:
        import capo_application_auto_scaling.types.scalable_target_action

        out["ScalableTargetAction"] = (
            capo_application_auto_scaling.types.scalable_target_action.serialize_aws_json_1_1(
                value["scalable_target_action"]
            )
        )
    import capo_application_auto_scaling.types.timestamp_type

    out["CreationTime"] = (
        capo_application_auto_scaling.types.timestamp_type.serialize_aws_json_1_1(
            value["creation_time"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduledAction:
    out: ScheduledAction = {}  # type: ignore[typeddict-item]
    if data.get("ScheduledActionName") is not None:
        out["scheduled_action_name"] = data["ScheduledActionName"]
    else:
        raise DeserializationError("ScheduledAction.scheduled_action_name required")
    if data.get("ScheduledActionARN") is not None:
        out["scheduled_action_arn"] = data["ScheduledActionARN"]
    else:
        raise DeserializationError("ScheduledAction.scheduled_action_arn required")
    if data.get("ServiceNamespace") is not None:
        import capo_application_auto_scaling.types.service_namespace

        out["service_namespace"] = (
            capo_application_auto_scaling.types.service_namespace.deserialize_aws_json_1_1(
                data["ServiceNamespace"]
            )
        )
    else:
        raise DeserializationError("ScheduledAction.service_namespace required")
    if data.get("Schedule") is not None:
        out["schedule"] = data["Schedule"]
    else:
        raise DeserializationError("ScheduledAction.schedule required")
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ScheduledAction.resource_id required")
    if data.get("ScalableDimension") is not None:
        import capo_application_auto_scaling.types.scalable_dimension

        out["scalable_dimension"] = (
            capo_application_auto_scaling.types.scalable_dimension.deserialize_aws_json_1_1(
                data["ScalableDimension"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_application_auto_scaling.types.timestamp_type

        out["start_time"] = (
            capo_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_application_auto_scaling.types.timestamp_type

        out["end_time"] = (
            capo_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if data.get("ScalableTargetAction") is not None:
        import capo_application_auto_scaling.types.scalable_target_action

        out["scalable_target_action"] = (
            capo_application_auto_scaling.types.scalable_target_action.deserialize_aws_json_1_1(
                data["ScalableTargetAction"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_application_auto_scaling.types.timestamp_type

        out["creation_time"] = (
            capo_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    else:
        raise DeserializationError("ScheduledAction.creation_time required")
    return out
