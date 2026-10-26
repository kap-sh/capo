"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cost_optimization_hub.errors import DeserializationError, SerializationError
from capo_cost_optimization_hub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.aurora_db_cluster_storage
    import capo_cost_optimization_hub.types.compute_savings_plans
    import capo_cost_optimization_hub.types.document_db_cluster
    import capo_cost_optimization_hub.types.dynamo_db_reserved_capacity
    import capo_cost_optimization_hub.types.dynamo_db_table
    import capo_cost_optimization_hub.types.ebs_volume
    import capo_cost_optimization_hub.types.ec2_auto_scaling_group
    import capo_cost_optimization_hub.types.ec2_instance
    import capo_cost_optimization_hub.types.ec2_instance_savings_plans
    import capo_cost_optimization_hub.types.ec2_reserved_instances
    import capo_cost_optimization_hub.types.ecs_service
    import capo_cost_optimization_hub.types.elasti_cache_cluster
    import capo_cost_optimization_hub.types.elasti_cache_reserved_instances
    import capo_cost_optimization_hub.types.lambda_function
    import capo_cost_optimization_hub.types.memory_db_cluster
    import capo_cost_optimization_hub.types.memory_db_reserved_instances
    import capo_cost_optimization_hub.types.nat_gateway
    import capo_cost_optimization_hub.types.open_search_reserved_instances
    import capo_cost_optimization_hub.types.rds_db_instance
    import capo_cost_optimization_hub.types.rds_db_instance_storage
    import capo_cost_optimization_hub.types.rds_reserved_instances
    import capo_cost_optimization_hub.types.redshift_reserved_instances
    import capo_cost_optimization_hub.types.sage_maker_endpoint
    import capo_cost_optimization_hub.types.sage_maker_savings_plans
    import capo_cost_optimization_hub.types.work_spaces


class _ResourceDetails_lambdaFunction(TypedDict, closed=True):
    lambdaFunction: "capo_cost_optimization_hub.types.lambda_function.LambdaFunction"


class _ResourceDetails_ecsService(TypedDict, closed=True):
    ecsService: "capo_cost_optimization_hub.types.ecs_service.EcsService"


class _ResourceDetails_ec2Instance(TypedDict, closed=True):
    ec2Instance: "capo_cost_optimization_hub.types.ec2_instance.Ec2Instance"


class _ResourceDetails_ebsVolume(TypedDict, closed=True):
    ebsVolume: "capo_cost_optimization_hub.types.ebs_volume.EbsVolume"


class _ResourceDetails_ec2AutoScalingGroup(TypedDict, closed=True):
    ec2AutoScalingGroup: (
        "capo_cost_optimization_hub.types.ec2_auto_scaling_group.Ec2AutoScalingGroup"
    )


class _ResourceDetails_ec2ReservedInstances(TypedDict, closed=True):
    ec2ReservedInstances: (
        "capo_cost_optimization_hub.types.ec2_reserved_instances.Ec2ReservedInstances"
    )


class _ResourceDetails_rdsReservedInstances(TypedDict, closed=True):
    rdsReservedInstances: (
        "capo_cost_optimization_hub.types.rds_reserved_instances.RdsReservedInstances"
    )


class _ResourceDetails_elastiCacheReservedInstances(TypedDict, closed=True):
    elastiCacheReservedInstances: "capo_cost_optimization_hub.types.elasti_cache_reserved_instances.ElastiCacheReservedInstances"


class _ResourceDetails_openSearchReservedInstances(TypedDict, closed=True):
    openSearchReservedInstances: "capo_cost_optimization_hub.types.open_search_reserved_instances.OpenSearchReservedInstances"


class _ResourceDetails_redshiftReservedInstances(TypedDict, closed=True):
    redshiftReservedInstances: "capo_cost_optimization_hub.types.redshift_reserved_instances.RedshiftReservedInstances"


class _ResourceDetails_ec2InstanceSavingsPlans(TypedDict, closed=True):
    ec2InstanceSavingsPlans: "capo_cost_optimization_hub.types.ec2_instance_savings_plans.Ec2InstanceSavingsPlans"


class _ResourceDetails_computeSavingsPlans(TypedDict, closed=True):
    computeSavingsPlans: (
        "capo_cost_optimization_hub.types.compute_savings_plans.ComputeSavingsPlans"
    )


class _ResourceDetails_sageMakerSavingsPlans(TypedDict, closed=True):
    sageMakerSavingsPlans: "capo_cost_optimization_hub.types.sage_maker_savings_plans.SageMakerSavingsPlans"


class _ResourceDetails_rdsDbInstance(TypedDict, closed=True):
    rdsDbInstance: "capo_cost_optimization_hub.types.rds_db_instance.RdsDbInstance"


class _ResourceDetails_rdsDbInstanceStorage(TypedDict, closed=True):
    rdsDbInstanceStorage: (
        "capo_cost_optimization_hub.types.rds_db_instance_storage.RdsDbInstanceStorage"
    )


class _ResourceDetails_auroraDbClusterStorage(TypedDict, closed=True):
    auroraDbClusterStorage: "capo_cost_optimization_hub.types.aurora_db_cluster_storage.AuroraDbClusterStorage"


class _ResourceDetails_dynamoDbReservedCapacity(TypedDict, closed=True):
    dynamoDbReservedCapacity: "capo_cost_optimization_hub.types.dynamo_db_reserved_capacity.DynamoDbReservedCapacity"


class _ResourceDetails_memoryDbReservedInstances(TypedDict, closed=True):
    memoryDbReservedInstances: "capo_cost_optimization_hub.types.memory_db_reserved_instances.MemoryDbReservedInstances"


class _ResourceDetails_natGateway(TypedDict, closed=True):
    natGateway: "capo_cost_optimization_hub.types.nat_gateway.NatGateway"


class _ResourceDetails_dynamoDbTable(TypedDict, closed=True):
    dynamoDbTable: "capo_cost_optimization_hub.types.dynamo_db_table.DynamoDbTable"


class _ResourceDetails_elastiCacheCluster(TypedDict, closed=True):
    elastiCacheCluster: (
        "capo_cost_optimization_hub.types.elasti_cache_cluster.ElastiCacheCluster"
    )


class _ResourceDetails_memoryDbCluster(TypedDict, closed=True):
    memoryDbCluster: (
        "capo_cost_optimization_hub.types.memory_db_cluster.MemoryDbCluster"
    )


class _ResourceDetails_documentDbCluster(TypedDict, closed=True):
    documentDbCluster: (
        "capo_cost_optimization_hub.types.document_db_cluster.DocumentDbCluster"
    )


class _ResourceDetails_workSpaces(TypedDict, closed=True):
    workSpaces: "capo_cost_optimization_hub.types.work_spaces.WorkSpaces"


class _ResourceDetails_sageMakerEndpoint(TypedDict, closed=True):
    sageMakerEndpoint: (
        "capo_cost_optimization_hub.types.sage_maker_endpoint.SageMakerEndpoint"
    )


ResourceDetails: TypeAlias = (
    _ResourceDetails_lambdaFunction
    | _ResourceDetails_ecsService
    | _ResourceDetails_ec2Instance
    | _ResourceDetails_ebsVolume
    | _ResourceDetails_ec2AutoScalingGroup
    | _ResourceDetails_ec2ReservedInstances
    | _ResourceDetails_rdsReservedInstances
    | _ResourceDetails_elastiCacheReservedInstances
    | _ResourceDetails_openSearchReservedInstances
    | _ResourceDetails_redshiftReservedInstances
    | _ResourceDetails_ec2InstanceSavingsPlans
    | _ResourceDetails_computeSavingsPlans
    | _ResourceDetails_sageMakerSavingsPlans
    | _ResourceDetails_rdsDbInstance
    | _ResourceDetails_rdsDbInstanceStorage
    | _ResourceDetails_auroraDbClusterStorage
    | _ResourceDetails_dynamoDbReservedCapacity
    | _ResourceDetails_memoryDbReservedInstances
    | _ResourceDetails_natGateway
    | _ResourceDetails_dynamoDbTable
    | _ResourceDetails_elastiCacheCluster
    | _ResourceDetails_memoryDbCluster
    | _ResourceDetails_documentDbCluster
    | _ResourceDetails_workSpaces
    | _ResourceDetails_sageMakerEndpoint
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ResourceDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "lambdaFunction" in value:
        import capo_cost_optimization_hub.types.lambda_function

        return {
            "lambdaFunction": capo_cost_optimization_hub.types.lambda_function.serialize_aws_json_1_0(
                value["lambdaFunction"]
            )
        }
    elif "ecsService" in value:
        import capo_cost_optimization_hub.types.ecs_service

        return {
            "ecsService": capo_cost_optimization_hub.types.ecs_service.serialize_aws_json_1_0(
                value["ecsService"]
            )
        }
    elif "ec2Instance" in value:
        import capo_cost_optimization_hub.types.ec2_instance

        return {
            "ec2Instance": capo_cost_optimization_hub.types.ec2_instance.serialize_aws_json_1_0(
                value["ec2Instance"]
            )
        }
    elif "ebsVolume" in value:
        import capo_cost_optimization_hub.types.ebs_volume

        return {
            "ebsVolume": capo_cost_optimization_hub.types.ebs_volume.serialize_aws_json_1_0(
                value["ebsVolume"]
            )
        }
    elif "ec2AutoScalingGroup" in value:
        import capo_cost_optimization_hub.types.ec2_auto_scaling_group

        return {
            "ec2AutoScalingGroup": capo_cost_optimization_hub.types.ec2_auto_scaling_group.serialize_aws_json_1_0(
                value["ec2AutoScalingGroup"]
            )
        }
    elif "ec2ReservedInstances" in value:
        import capo_cost_optimization_hub.types.ec2_reserved_instances

        return {
            "ec2ReservedInstances": capo_cost_optimization_hub.types.ec2_reserved_instances.serialize_aws_json_1_0(
                value["ec2ReservedInstances"]
            )
        }
    elif "rdsReservedInstances" in value:
        import capo_cost_optimization_hub.types.rds_reserved_instances

        return {
            "rdsReservedInstances": capo_cost_optimization_hub.types.rds_reserved_instances.serialize_aws_json_1_0(
                value["rdsReservedInstances"]
            )
        }
    elif "elastiCacheReservedInstances" in value:
        import capo_cost_optimization_hub.types.elasti_cache_reserved_instances

        return {
            "elastiCacheReservedInstances": capo_cost_optimization_hub.types.elasti_cache_reserved_instances.serialize_aws_json_1_0(
                value["elastiCacheReservedInstances"]
            )
        }
    elif "openSearchReservedInstances" in value:
        import capo_cost_optimization_hub.types.open_search_reserved_instances

        return {
            "openSearchReservedInstances": capo_cost_optimization_hub.types.open_search_reserved_instances.serialize_aws_json_1_0(
                value["openSearchReservedInstances"]
            )
        }
    elif "redshiftReservedInstances" in value:
        import capo_cost_optimization_hub.types.redshift_reserved_instances

        return {
            "redshiftReservedInstances": capo_cost_optimization_hub.types.redshift_reserved_instances.serialize_aws_json_1_0(
                value["redshiftReservedInstances"]
            )
        }
    elif "ec2InstanceSavingsPlans" in value:
        import capo_cost_optimization_hub.types.ec2_instance_savings_plans

        return {
            "ec2InstanceSavingsPlans": capo_cost_optimization_hub.types.ec2_instance_savings_plans.serialize_aws_json_1_0(
                value["ec2InstanceSavingsPlans"]
            )
        }
    elif "computeSavingsPlans" in value:
        import capo_cost_optimization_hub.types.compute_savings_plans

        return {
            "computeSavingsPlans": capo_cost_optimization_hub.types.compute_savings_plans.serialize_aws_json_1_0(
                value["computeSavingsPlans"]
            )
        }
    elif "sageMakerSavingsPlans" in value:
        import capo_cost_optimization_hub.types.sage_maker_savings_plans

        return {
            "sageMakerSavingsPlans": capo_cost_optimization_hub.types.sage_maker_savings_plans.serialize_aws_json_1_0(
                value["sageMakerSavingsPlans"]
            )
        }
    elif "rdsDbInstance" in value:
        import capo_cost_optimization_hub.types.rds_db_instance

        return {
            "rdsDbInstance": capo_cost_optimization_hub.types.rds_db_instance.serialize_aws_json_1_0(
                value["rdsDbInstance"]
            )
        }
    elif "rdsDbInstanceStorage" in value:
        import capo_cost_optimization_hub.types.rds_db_instance_storage

        return {
            "rdsDbInstanceStorage": capo_cost_optimization_hub.types.rds_db_instance_storage.serialize_aws_json_1_0(
                value["rdsDbInstanceStorage"]
            )
        }
    elif "auroraDbClusterStorage" in value:
        import capo_cost_optimization_hub.types.aurora_db_cluster_storage

        return {
            "auroraDbClusterStorage": capo_cost_optimization_hub.types.aurora_db_cluster_storage.serialize_aws_json_1_0(
                value["auroraDbClusterStorage"]
            )
        }
    elif "dynamoDbReservedCapacity" in value:
        import capo_cost_optimization_hub.types.dynamo_db_reserved_capacity

        return {
            "dynamoDbReservedCapacity": capo_cost_optimization_hub.types.dynamo_db_reserved_capacity.serialize_aws_json_1_0(
                value["dynamoDbReservedCapacity"]
            )
        }
    elif "memoryDbReservedInstances" in value:
        import capo_cost_optimization_hub.types.memory_db_reserved_instances

        return {
            "memoryDbReservedInstances": capo_cost_optimization_hub.types.memory_db_reserved_instances.serialize_aws_json_1_0(
                value["memoryDbReservedInstances"]
            )
        }
    elif "natGateway" in value:
        import capo_cost_optimization_hub.types.nat_gateway

        return {
            "natGateway": capo_cost_optimization_hub.types.nat_gateway.serialize_aws_json_1_0(
                value["natGateway"]
            )
        }
    elif "dynamoDbTable" in value:
        import capo_cost_optimization_hub.types.dynamo_db_table

        return {
            "dynamoDbTable": capo_cost_optimization_hub.types.dynamo_db_table.serialize_aws_json_1_0(
                value["dynamoDbTable"]
            )
        }
    elif "elastiCacheCluster" in value:
        import capo_cost_optimization_hub.types.elasti_cache_cluster

        return {
            "elastiCacheCluster": capo_cost_optimization_hub.types.elasti_cache_cluster.serialize_aws_json_1_0(
                value["elastiCacheCluster"]
            )
        }
    elif "memoryDbCluster" in value:
        import capo_cost_optimization_hub.types.memory_db_cluster

        return {
            "memoryDbCluster": capo_cost_optimization_hub.types.memory_db_cluster.serialize_aws_json_1_0(
                value["memoryDbCluster"]
            )
        }
    elif "documentDbCluster" in value:
        import capo_cost_optimization_hub.types.document_db_cluster

        return {
            "documentDbCluster": capo_cost_optimization_hub.types.document_db_cluster.serialize_aws_json_1_0(
                value["documentDbCluster"]
            )
        }
    elif "workSpaces" in value:
        import capo_cost_optimization_hub.types.work_spaces

        return {
            "workSpaces": capo_cost_optimization_hub.types.work_spaces.serialize_aws_json_1_0(
                value["workSpaces"]
            )
        }
    elif "sageMakerEndpoint" in value:
        import capo_cost_optimization_hub.types.sage_maker_endpoint

        return {
            "sageMakerEndpoint": capo_cost_optimization_hub.types.sage_maker_endpoint.serialize_aws_json_1_0(
                value["sageMakerEndpoint"]
            )
        }
    else:
        raise SerializationError("ResourceDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ResourceDetails:
    if data.get("lambdaFunction") is not None:
        import capo_cost_optimization_hub.types.lambda_function

        return {
            "lambdaFunction": capo_cost_optimization_hub.types.lambda_function.deserialize_aws_json_1_0(
                data["lambdaFunction"]
            )
        }
    elif data.get("ecsService") is not None:
        import capo_cost_optimization_hub.types.ecs_service

        return {
            "ecsService": capo_cost_optimization_hub.types.ecs_service.deserialize_aws_json_1_0(
                data["ecsService"]
            )
        }
    elif data.get("ec2Instance") is not None:
        import capo_cost_optimization_hub.types.ec2_instance

        return {
            "ec2Instance": capo_cost_optimization_hub.types.ec2_instance.deserialize_aws_json_1_0(
                data["ec2Instance"]
            )
        }
    elif data.get("ebsVolume") is not None:
        import capo_cost_optimization_hub.types.ebs_volume

        return {
            "ebsVolume": capo_cost_optimization_hub.types.ebs_volume.deserialize_aws_json_1_0(
                data["ebsVolume"]
            )
        }
    elif data.get("ec2AutoScalingGroup") is not None:
        import capo_cost_optimization_hub.types.ec2_auto_scaling_group

        return {
            "ec2AutoScalingGroup": capo_cost_optimization_hub.types.ec2_auto_scaling_group.deserialize_aws_json_1_0(
                data["ec2AutoScalingGroup"]
            )
        }
    elif data.get("ec2ReservedInstances") is not None:
        import capo_cost_optimization_hub.types.ec2_reserved_instances

        return {
            "ec2ReservedInstances": capo_cost_optimization_hub.types.ec2_reserved_instances.deserialize_aws_json_1_0(
                data["ec2ReservedInstances"]
            )
        }
    elif data.get("rdsReservedInstances") is not None:
        import capo_cost_optimization_hub.types.rds_reserved_instances

        return {
            "rdsReservedInstances": capo_cost_optimization_hub.types.rds_reserved_instances.deserialize_aws_json_1_0(
                data["rdsReservedInstances"]
            )
        }
    elif data.get("elastiCacheReservedInstances") is not None:
        import capo_cost_optimization_hub.types.elasti_cache_reserved_instances

        return {
            "elastiCacheReservedInstances": capo_cost_optimization_hub.types.elasti_cache_reserved_instances.deserialize_aws_json_1_0(
                data["elastiCacheReservedInstances"]
            )
        }
    elif data.get("openSearchReservedInstances") is not None:
        import capo_cost_optimization_hub.types.open_search_reserved_instances

        return {
            "openSearchReservedInstances": capo_cost_optimization_hub.types.open_search_reserved_instances.deserialize_aws_json_1_0(
                data["openSearchReservedInstances"]
            )
        }
    elif data.get("redshiftReservedInstances") is not None:
        import capo_cost_optimization_hub.types.redshift_reserved_instances

        return {
            "redshiftReservedInstances": capo_cost_optimization_hub.types.redshift_reserved_instances.deserialize_aws_json_1_0(
                data["redshiftReservedInstances"]
            )
        }
    elif data.get("ec2InstanceSavingsPlans") is not None:
        import capo_cost_optimization_hub.types.ec2_instance_savings_plans

        return {
            "ec2InstanceSavingsPlans": capo_cost_optimization_hub.types.ec2_instance_savings_plans.deserialize_aws_json_1_0(
                data["ec2InstanceSavingsPlans"]
            )
        }
    elif data.get("computeSavingsPlans") is not None:
        import capo_cost_optimization_hub.types.compute_savings_plans

        return {
            "computeSavingsPlans": capo_cost_optimization_hub.types.compute_savings_plans.deserialize_aws_json_1_0(
                data["computeSavingsPlans"]
            )
        }
    elif data.get("sageMakerSavingsPlans") is not None:
        import capo_cost_optimization_hub.types.sage_maker_savings_plans

        return {
            "sageMakerSavingsPlans": capo_cost_optimization_hub.types.sage_maker_savings_plans.deserialize_aws_json_1_0(
                data["sageMakerSavingsPlans"]
            )
        }
    elif data.get("rdsDbInstance") is not None:
        import capo_cost_optimization_hub.types.rds_db_instance

        return {
            "rdsDbInstance": capo_cost_optimization_hub.types.rds_db_instance.deserialize_aws_json_1_0(
                data["rdsDbInstance"]
            )
        }
    elif data.get("rdsDbInstanceStorage") is not None:
        import capo_cost_optimization_hub.types.rds_db_instance_storage

        return {
            "rdsDbInstanceStorage": capo_cost_optimization_hub.types.rds_db_instance_storage.deserialize_aws_json_1_0(
                data["rdsDbInstanceStorage"]
            )
        }
    elif data.get("auroraDbClusterStorage") is not None:
        import capo_cost_optimization_hub.types.aurora_db_cluster_storage

        return {
            "auroraDbClusterStorage": capo_cost_optimization_hub.types.aurora_db_cluster_storage.deserialize_aws_json_1_0(
                data["auroraDbClusterStorage"]
            )
        }
    elif data.get("dynamoDbReservedCapacity") is not None:
        import capo_cost_optimization_hub.types.dynamo_db_reserved_capacity

        return {
            "dynamoDbReservedCapacity": capo_cost_optimization_hub.types.dynamo_db_reserved_capacity.deserialize_aws_json_1_0(
                data["dynamoDbReservedCapacity"]
            )
        }
    elif data.get("memoryDbReservedInstances") is not None:
        import capo_cost_optimization_hub.types.memory_db_reserved_instances

        return {
            "memoryDbReservedInstances": capo_cost_optimization_hub.types.memory_db_reserved_instances.deserialize_aws_json_1_0(
                data["memoryDbReservedInstances"]
            )
        }
    elif data.get("natGateway") is not None:
        import capo_cost_optimization_hub.types.nat_gateway

        return {
            "natGateway": capo_cost_optimization_hub.types.nat_gateway.deserialize_aws_json_1_0(
                data["natGateway"]
            )
        }
    elif data.get("dynamoDbTable") is not None:
        import capo_cost_optimization_hub.types.dynamo_db_table

        return {
            "dynamoDbTable": capo_cost_optimization_hub.types.dynamo_db_table.deserialize_aws_json_1_0(
                data["dynamoDbTable"]
            )
        }
    elif data.get("elastiCacheCluster") is not None:
        import capo_cost_optimization_hub.types.elasti_cache_cluster

        return {
            "elastiCacheCluster": capo_cost_optimization_hub.types.elasti_cache_cluster.deserialize_aws_json_1_0(
                data["elastiCacheCluster"]
            )
        }
    elif data.get("memoryDbCluster") is not None:
        import capo_cost_optimization_hub.types.memory_db_cluster

        return {
            "memoryDbCluster": capo_cost_optimization_hub.types.memory_db_cluster.deserialize_aws_json_1_0(
                data["memoryDbCluster"]
            )
        }
    elif data.get("documentDbCluster") is not None:
        import capo_cost_optimization_hub.types.document_db_cluster

        return {
            "documentDbCluster": capo_cost_optimization_hub.types.document_db_cluster.deserialize_aws_json_1_0(
                data["documentDbCluster"]
            )
        }
    elif data.get("workSpaces") is not None:
        import capo_cost_optimization_hub.types.work_spaces

        return {
            "workSpaces": capo_cost_optimization_hub.types.work_spaces.deserialize_aws_json_1_0(
                data["workSpaces"]
            )
        }
    elif data.get("sageMakerEndpoint") is not None:
        import capo_cost_optimization_hub.types.sage_maker_endpoint

        return {
            "sageMakerEndpoint": capo_cost_optimization_hub.types.sage_maker_endpoint.deserialize_aws_json_1_0(
                data["sageMakerEndpoint"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ResourceDetails: no recognized variant key")
