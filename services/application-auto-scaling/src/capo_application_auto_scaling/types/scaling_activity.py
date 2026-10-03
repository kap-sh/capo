"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScalingActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.not_scaled_reasons
    import capo_application_auto_scaling.types.resource_id
    import capo_application_auto_scaling.types.resource_id_max_len1600
    import capo_application_auto_scaling.types.scalable_dimension
    import capo_application_auto_scaling.types.scaling_activity_status_code
    import capo_application_auto_scaling.types.service_namespace
    import capo_application_auto_scaling.types.timestamp_type
    import capo_application_auto_scaling.types.xml_string


class ScalingActivity(TypedDict, closed=True):
    activity_id: "capo_application_auto_scaling.types.resource_id.ResourceId"
    """<p>The unique identifier of the scaling activity.</p>"""
    service_namespace: (
        "capo_application_auto_scaling.types.service_namespace.ServiceNamespace"
    )
    """<p>The namespace of the Amazon Web Services service that provides the resource, or a <code>custom-resource</code>.</p>"""
    resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    """<p>The identifier of the resource associated with the scaling activity. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href="https://github.com/aws/aws-auto-scaling-custom-resource">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>"""
    scalable_dimension: (
        "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
    )
    """<p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>"""
    description: "capo_application_auto_scaling.types.xml_string.XmlString"
    """<p>A simple description of what action the scaling activity intends to accomplish.</p>"""
    cause: "capo_application_auto_scaling.types.xml_string.XmlString"
    """<p>A simple description of what caused the scaling activity to happen.</p>"""
    start_time: "capo_application_auto_scaling.types.timestamp_type.TimestampType"
    """<p>The Unix timestamp for when the scaling activity began.</p>"""
    end_time: NotRequired[
        "capo_application_auto_scaling.types.timestamp_type.TimestampType"
    ]
    """<p>The Unix timestamp for when the scaling activity ended.</p>"""
    status_code: "capo_application_auto_scaling.types.scaling_activity_status_code.ScalingActivityStatusCode"
    """<p>Indicates the status of the scaling activity.</p>"""
    status_message: NotRequired[
        "capo_application_auto_scaling.types.xml_string.XmlString"
    ]
    """<p>A simple message about the current status of the scaling activity.</p>"""
    details: NotRequired["capo_application_auto_scaling.types.xml_string.XmlString"]
    """<p>The details about the scaling activity.</p>"""
    not_scaled_reasons: NotRequired[
        "capo_application_auto_scaling.types.not_scaled_reasons.NotScaledReasons"
    ]
    """<p>Machine-readable data that describes the reason for a not scaled activity. Only available when <a href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalingActivities.html">DescribeScalingActivities</a> includes not scaled activities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingActivity) -> dict:
    out: dict = {}
    out["ActivityId"] = value["activity_id"]
    import capo_application_auto_scaling.types.service_namespace

    out["ServiceNamespace"] = (
        capo_application_auto_scaling.types.service_namespace.serialize_aws_json_1_1(
            value["service_namespace"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import capo_application_auto_scaling.types.scalable_dimension

    out["ScalableDimension"] = (
        capo_application_auto_scaling.types.scalable_dimension.serialize_aws_json_1_1(
            value["scalable_dimension"]
        )
    )
    out["Description"] = value["description"]
    out["Cause"] = value["cause"]
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
    import capo_application_auto_scaling.types.scaling_activity_status_code

    out["StatusCode"] = (
        capo_application_auto_scaling.types.scaling_activity_status_code.serialize_aws_json_1_1(
            value["status_code"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "details" in value:
        out["Details"] = value["details"]
    if "not_scaled_reasons" in value:
        import capo_application_auto_scaling.types.not_scaled_reasons

        out["NotScaledReasons"] = (
            capo_application_auto_scaling.types.not_scaled_reasons.serialize_aws_json_1_1(
                value["not_scaled_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingActivity:
    out: ScalingActivity = {}  # type: ignore[typeddict-item]
    if data.get("ActivityId") is not None:
        out["activity_id"] = data["ActivityId"]
    else:
        raise DeserializationError("ScalingActivity.activity_id required")
    if data.get("ServiceNamespace") is not None:
        import capo_application_auto_scaling.types.service_namespace

        out["service_namespace"] = (
            capo_application_auto_scaling.types.service_namespace.deserialize_aws_json_1_1(
                data["ServiceNamespace"]
            )
        )
    else:
        raise DeserializationError("ScalingActivity.service_namespace required")
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ScalingActivity.resource_id required")
    if data.get("ScalableDimension") is not None:
        import capo_application_auto_scaling.types.scalable_dimension

        out["scalable_dimension"] = (
            capo_application_auto_scaling.types.scalable_dimension.deserialize_aws_json_1_1(
                data["ScalableDimension"]
            )
        )
    else:
        raise DeserializationError("ScalingActivity.scalable_dimension required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("ScalingActivity.description required")
    if data.get("Cause") is not None:
        out["cause"] = data["Cause"]
    else:
        raise DeserializationError("ScalingActivity.cause required")
    if data.get("StartTime") is not None:
        import capo_application_auto_scaling.types.timestamp_type

        out["start_time"] = (
            capo_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ScalingActivity.start_time required")
    if data.get("EndTime") is not None:
        import capo_application_auto_scaling.types.timestamp_type

        out["end_time"] = (
            capo_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if data.get("StatusCode") is not None:
        import capo_application_auto_scaling.types.scaling_activity_status_code

        out["status_code"] = (
            capo_application_auto_scaling.types.scaling_activity_status_code.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    else:
        raise DeserializationError("ScalingActivity.status_code required")
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("Details") is not None:
        out["details"] = data["Details"]
    if data.get("NotScaledReasons") is not None:
        import capo_application_auto_scaling.types.not_scaled_reasons

        out["not_scaled_reasons"] = (
            capo_application_auto_scaling.types.not_scaled_reasons.deserialize_aws_json_1_1(
                data["NotScaledReasons"]
            )
        )
    return out
