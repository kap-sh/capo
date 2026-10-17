"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionBlockConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_arc_region_switch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.arc_routing_control_configuration
    import capo_arc_region_switch.types.aurora_provisioned_scaling_configuration
    import capo_arc_region_switch.types.aurora_serverless_scaling_configuration
    import capo_arc_region_switch.types.custom_action_lambda_configuration
    import capo_arc_region_switch.types.document_db_configuration
    import capo_arc_region_switch.types.ec2_asg_capacity_increase_configuration
    import capo_arc_region_switch.types.ecs_capacity_increase_configuration
    import capo_arc_region_switch.types.eks_resource_scaling_configuration
    import capo_arc_region_switch.types.execution_approval_configuration
    import capo_arc_region_switch.types.global_aurora_configuration
    import capo_arc_region_switch.types.lambda_event_source_mapping_configuration
    import capo_arc_region_switch.types.neptune_global_database_configuration
    import capo_arc_region_switch.types.parallel_execution_block_configuration
    import capo_arc_region_switch.types.rds_create_cross_region_replica_configuration
    import capo_arc_region_switch.types.rds_promote_read_replica_configuration
    import capo_arc_region_switch.types.rds_switchover_read_replica_configuration
    import capo_arc_region_switch.types.region_switch_plan_configuration
    import capo_arc_region_switch.types.route53_health_check_configuration


class _ExecutionBlockConfiguration_customActionLambdaConfig(TypedDict, closed=True):
    customActionLambdaConfig: "capo_arc_region_switch.types.custom_action_lambda_configuration.CustomActionLambdaConfiguration"


class _ExecutionBlockConfiguration_ec2AsgCapacityIncreaseConfig(TypedDict, closed=True):
    ec2AsgCapacityIncreaseConfig: "capo_arc_region_switch.types.ec2_asg_capacity_increase_configuration.Ec2AsgCapacityIncreaseConfiguration"


class _ExecutionBlockConfiguration_executionApprovalConfig(TypedDict, closed=True):
    executionApprovalConfig: "capo_arc_region_switch.types.execution_approval_configuration.ExecutionApprovalConfiguration"


class _ExecutionBlockConfiguration_arcRoutingControlConfig(TypedDict, closed=True):
    arcRoutingControlConfig: "capo_arc_region_switch.types.arc_routing_control_configuration.ArcRoutingControlConfiguration"


class _ExecutionBlockConfiguration_globalAuroraConfig(TypedDict, closed=True):
    globalAuroraConfig: "capo_arc_region_switch.types.global_aurora_configuration.GlobalAuroraConfiguration"


class _ExecutionBlockConfiguration_parallelConfig(TypedDict, closed=True):
    parallelConfig: "capo_arc_region_switch.types.parallel_execution_block_configuration.ParallelExecutionBlockConfiguration"


class _ExecutionBlockConfiguration_regionSwitchPlanConfig(TypedDict, closed=True):
    regionSwitchPlanConfig: "capo_arc_region_switch.types.region_switch_plan_configuration.RegionSwitchPlanConfiguration"


class _ExecutionBlockConfiguration_ecsCapacityIncreaseConfig(TypedDict, closed=True):
    ecsCapacityIncreaseConfig: "capo_arc_region_switch.types.ecs_capacity_increase_configuration.EcsCapacityIncreaseConfiguration"


class _ExecutionBlockConfiguration_eksResourceScalingConfig(TypedDict, closed=True):
    eksResourceScalingConfig: "capo_arc_region_switch.types.eks_resource_scaling_configuration.EksResourceScalingConfiguration"


class _ExecutionBlockConfiguration_route53HealthCheckConfig(TypedDict, closed=True):
    route53HealthCheckConfig: "capo_arc_region_switch.types.route53_health_check_configuration.Route53HealthCheckConfiguration"


class _ExecutionBlockConfiguration_documentDbConfig(TypedDict, closed=True):
    documentDbConfig: (
        "capo_arc_region_switch.types.document_db_configuration.DocumentDbConfiguration"
    )


class _ExecutionBlockConfiguration_rdsPromoteReadReplicaConfig(TypedDict, closed=True):
    rdsPromoteReadReplicaConfig: "capo_arc_region_switch.types.rds_promote_read_replica_configuration.RdsPromoteReadReplicaConfiguration"


class _ExecutionBlockConfiguration_rdsCreateCrossRegionReadReplicaConfig(
    TypedDict, closed=True
):
    rdsCreateCrossRegionReadReplicaConfig: "capo_arc_region_switch.types.rds_create_cross_region_replica_configuration.RdsCreateCrossRegionReplicaConfiguration"


class _ExecutionBlockConfiguration_lambdaEventSourceMappingConfig(
    TypedDict, closed=True
):
    lambdaEventSourceMappingConfig: "capo_arc_region_switch.types.lambda_event_source_mapping_configuration.LambdaEventSourceMappingConfiguration"


class _ExecutionBlockConfiguration_auroraServerlessScalingConfig(
    TypedDict, closed=True
):
    auroraServerlessScalingConfig: "capo_arc_region_switch.types.aurora_serverless_scaling_configuration.AuroraServerlessScalingConfiguration"


class _ExecutionBlockConfiguration_auroraProvisionedScalingConfig(
    TypedDict, closed=True
):
    auroraProvisionedScalingConfig: "capo_arc_region_switch.types.aurora_provisioned_scaling_configuration.AuroraProvisionedScalingConfiguration"


class _ExecutionBlockConfiguration_neptuneGlobalDatabaseConfig(TypedDict, closed=True):
    neptuneGlobalDatabaseConfig: "capo_arc_region_switch.types.neptune_global_database_configuration.NeptuneGlobalDatabaseConfiguration"


class _ExecutionBlockConfiguration_rdsSwitchoverReadReplicaConfig(
    TypedDict, closed=True
):
    rdsSwitchoverReadReplicaConfig: "capo_arc_region_switch.types.rds_switchover_read_replica_configuration.RdsSwitchoverReadReplicaConfiguration"


ExecutionBlockConfiguration: TypeAlias = (
    _ExecutionBlockConfiguration_customActionLambdaConfig
    | _ExecutionBlockConfiguration_ec2AsgCapacityIncreaseConfig
    | _ExecutionBlockConfiguration_executionApprovalConfig
    | _ExecutionBlockConfiguration_arcRoutingControlConfig
    | _ExecutionBlockConfiguration_globalAuroraConfig
    | _ExecutionBlockConfiguration_parallelConfig
    | _ExecutionBlockConfiguration_regionSwitchPlanConfig
    | _ExecutionBlockConfiguration_ecsCapacityIncreaseConfig
    | _ExecutionBlockConfiguration_eksResourceScalingConfig
    | _ExecutionBlockConfiguration_route53HealthCheckConfig
    | _ExecutionBlockConfiguration_documentDbConfig
    | _ExecutionBlockConfiguration_rdsPromoteReadReplicaConfig
    | _ExecutionBlockConfiguration_rdsCreateCrossRegionReadReplicaConfig
    | _ExecutionBlockConfiguration_lambdaEventSourceMappingConfig
    | _ExecutionBlockConfiguration_auroraServerlessScalingConfig
    | _ExecutionBlockConfiguration_auroraProvisionedScalingConfig
    | _ExecutionBlockConfiguration_neptuneGlobalDatabaseConfig
    | _ExecutionBlockConfiguration_rdsSwitchoverReadReplicaConfig
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionBlockConfiguration) -> dict:
    if "customActionLambdaConfig" in value:
        import capo_arc_region_switch.types.custom_action_lambda_configuration

        return {
            "customActionLambdaConfig": capo_arc_region_switch.types.custom_action_lambda_configuration.serialize_aws_json_1_0(
                value["customActionLambdaConfig"]
            )
        }
    elif "ec2AsgCapacityIncreaseConfig" in value:
        import capo_arc_region_switch.types.ec2_asg_capacity_increase_configuration

        return {
            "ec2AsgCapacityIncreaseConfig": capo_arc_region_switch.types.ec2_asg_capacity_increase_configuration.serialize_aws_json_1_0(
                value["ec2AsgCapacityIncreaseConfig"]
            )
        }
    elif "executionApprovalConfig" in value:
        import capo_arc_region_switch.types.execution_approval_configuration

        return {
            "executionApprovalConfig": capo_arc_region_switch.types.execution_approval_configuration.serialize_aws_json_1_0(
                value["executionApprovalConfig"]
            )
        }
    elif "arcRoutingControlConfig" in value:
        import capo_arc_region_switch.types.arc_routing_control_configuration

        return {
            "arcRoutingControlConfig": capo_arc_region_switch.types.arc_routing_control_configuration.serialize_aws_json_1_0(
                value["arcRoutingControlConfig"]
            )
        }
    elif "globalAuroraConfig" in value:
        import capo_arc_region_switch.types.global_aurora_configuration

        return {
            "globalAuroraConfig": capo_arc_region_switch.types.global_aurora_configuration.serialize_aws_json_1_0(
                value["globalAuroraConfig"]
            )
        }
    elif "parallelConfig" in value:
        import capo_arc_region_switch.types.parallel_execution_block_configuration

        return {
            "parallelConfig": capo_arc_region_switch.types.parallel_execution_block_configuration.serialize_aws_json_1_0(
                value["parallelConfig"]
            )
        }
    elif "regionSwitchPlanConfig" in value:
        import capo_arc_region_switch.types.region_switch_plan_configuration

        return {
            "regionSwitchPlanConfig": capo_arc_region_switch.types.region_switch_plan_configuration.serialize_aws_json_1_0(
                value["regionSwitchPlanConfig"]
            )
        }
    elif "ecsCapacityIncreaseConfig" in value:
        import capo_arc_region_switch.types.ecs_capacity_increase_configuration

        return {
            "ecsCapacityIncreaseConfig": capo_arc_region_switch.types.ecs_capacity_increase_configuration.serialize_aws_json_1_0(
                value["ecsCapacityIncreaseConfig"]
            )
        }
    elif "eksResourceScalingConfig" in value:
        import capo_arc_region_switch.types.eks_resource_scaling_configuration

        return {
            "eksResourceScalingConfig": capo_arc_region_switch.types.eks_resource_scaling_configuration.serialize_aws_json_1_0(
                value["eksResourceScalingConfig"]
            )
        }
    elif "route53HealthCheckConfig" in value:
        import capo_arc_region_switch.types.route53_health_check_configuration

        return {
            "route53HealthCheckConfig": capo_arc_region_switch.types.route53_health_check_configuration.serialize_aws_json_1_0(
                value["route53HealthCheckConfig"]
            )
        }
    elif "documentDbConfig" in value:
        import capo_arc_region_switch.types.document_db_configuration

        return {
            "documentDbConfig": capo_arc_region_switch.types.document_db_configuration.serialize_aws_json_1_0(
                value["documentDbConfig"]
            )
        }
    elif "rdsPromoteReadReplicaConfig" in value:
        import capo_arc_region_switch.types.rds_promote_read_replica_configuration

        return {
            "rdsPromoteReadReplicaConfig": capo_arc_region_switch.types.rds_promote_read_replica_configuration.serialize_aws_json_1_0(
                value["rdsPromoteReadReplicaConfig"]
            )
        }
    elif "rdsCreateCrossRegionReadReplicaConfig" in value:
        import capo_arc_region_switch.types.rds_create_cross_region_replica_configuration

        return {
            "rdsCreateCrossRegionReadReplicaConfig": capo_arc_region_switch.types.rds_create_cross_region_replica_configuration.serialize_aws_json_1_0(
                value["rdsCreateCrossRegionReadReplicaConfig"]
            )
        }
    elif "lambdaEventSourceMappingConfig" in value:
        import capo_arc_region_switch.types.lambda_event_source_mapping_configuration

        return {
            "lambdaEventSourceMappingConfig": capo_arc_region_switch.types.lambda_event_source_mapping_configuration.serialize_aws_json_1_0(
                value["lambdaEventSourceMappingConfig"]
            )
        }
    elif "auroraServerlessScalingConfig" in value:
        import capo_arc_region_switch.types.aurora_serverless_scaling_configuration

        return {
            "auroraServerlessScalingConfig": capo_arc_region_switch.types.aurora_serverless_scaling_configuration.serialize_aws_json_1_0(
                value["auroraServerlessScalingConfig"]
            )
        }
    elif "auroraProvisionedScalingConfig" in value:
        import capo_arc_region_switch.types.aurora_provisioned_scaling_configuration

        return {
            "auroraProvisionedScalingConfig": capo_arc_region_switch.types.aurora_provisioned_scaling_configuration.serialize_aws_json_1_0(
                value["auroraProvisionedScalingConfig"]
            )
        }
    elif "neptuneGlobalDatabaseConfig" in value:
        import capo_arc_region_switch.types.neptune_global_database_configuration

        return {
            "neptuneGlobalDatabaseConfig": capo_arc_region_switch.types.neptune_global_database_configuration.serialize_aws_json_1_0(
                value["neptuneGlobalDatabaseConfig"]
            )
        }
    elif "rdsSwitchoverReadReplicaConfig" in value:
        import capo_arc_region_switch.types.rds_switchover_read_replica_configuration

        return {
            "rdsSwitchoverReadReplicaConfig": capo_arc_region_switch.types.rds_switchover_read_replica_configuration.serialize_aws_json_1_0(
                value["rdsSwitchoverReadReplicaConfig"]
            )
        }
    else:
        raise SerializationError("ExecutionBlockConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ExecutionBlockConfiguration:
    if data.get("customActionLambdaConfig") is not None:
        import capo_arc_region_switch.types.custom_action_lambda_configuration

        return {
            "customActionLambdaConfig": capo_arc_region_switch.types.custom_action_lambda_configuration.deserialize_aws_json_1_0(
                data["customActionLambdaConfig"]
            )
        }
    elif data.get("ec2AsgCapacityIncreaseConfig") is not None:
        import capo_arc_region_switch.types.ec2_asg_capacity_increase_configuration

        return {
            "ec2AsgCapacityIncreaseConfig": capo_arc_region_switch.types.ec2_asg_capacity_increase_configuration.deserialize_aws_json_1_0(
                data["ec2AsgCapacityIncreaseConfig"]
            )
        }
    elif data.get("executionApprovalConfig") is not None:
        import capo_arc_region_switch.types.execution_approval_configuration

        return {
            "executionApprovalConfig": capo_arc_region_switch.types.execution_approval_configuration.deserialize_aws_json_1_0(
                data["executionApprovalConfig"]
            )
        }
    elif data.get("arcRoutingControlConfig") is not None:
        import capo_arc_region_switch.types.arc_routing_control_configuration

        return {
            "arcRoutingControlConfig": capo_arc_region_switch.types.arc_routing_control_configuration.deserialize_aws_json_1_0(
                data["arcRoutingControlConfig"]
            )
        }
    elif data.get("globalAuroraConfig") is not None:
        import capo_arc_region_switch.types.global_aurora_configuration

        return {
            "globalAuroraConfig": capo_arc_region_switch.types.global_aurora_configuration.deserialize_aws_json_1_0(
                data["globalAuroraConfig"]
            )
        }
    elif data.get("parallelConfig") is not None:
        import capo_arc_region_switch.types.parallel_execution_block_configuration

        return {
            "parallelConfig": capo_arc_region_switch.types.parallel_execution_block_configuration.deserialize_aws_json_1_0(
                data["parallelConfig"]
            )
        }
    elif data.get("regionSwitchPlanConfig") is not None:
        import capo_arc_region_switch.types.region_switch_plan_configuration

        return {
            "regionSwitchPlanConfig": capo_arc_region_switch.types.region_switch_plan_configuration.deserialize_aws_json_1_0(
                data["regionSwitchPlanConfig"]
            )
        }
    elif data.get("ecsCapacityIncreaseConfig") is not None:
        import capo_arc_region_switch.types.ecs_capacity_increase_configuration

        return {
            "ecsCapacityIncreaseConfig": capo_arc_region_switch.types.ecs_capacity_increase_configuration.deserialize_aws_json_1_0(
                data["ecsCapacityIncreaseConfig"]
            )
        }
    elif data.get("eksResourceScalingConfig") is not None:
        import capo_arc_region_switch.types.eks_resource_scaling_configuration

        return {
            "eksResourceScalingConfig": capo_arc_region_switch.types.eks_resource_scaling_configuration.deserialize_aws_json_1_0(
                data["eksResourceScalingConfig"]
            )
        }
    elif data.get("route53HealthCheckConfig") is not None:
        import capo_arc_region_switch.types.route53_health_check_configuration

        return {
            "route53HealthCheckConfig": capo_arc_region_switch.types.route53_health_check_configuration.deserialize_aws_json_1_0(
                data["route53HealthCheckConfig"]
            )
        }
    elif data.get("documentDbConfig") is not None:
        import capo_arc_region_switch.types.document_db_configuration

        return {
            "documentDbConfig": capo_arc_region_switch.types.document_db_configuration.deserialize_aws_json_1_0(
                data["documentDbConfig"]
            )
        }
    elif data.get("rdsPromoteReadReplicaConfig") is not None:
        import capo_arc_region_switch.types.rds_promote_read_replica_configuration

        return {
            "rdsPromoteReadReplicaConfig": capo_arc_region_switch.types.rds_promote_read_replica_configuration.deserialize_aws_json_1_0(
                data["rdsPromoteReadReplicaConfig"]
            )
        }
    elif data.get("rdsCreateCrossRegionReadReplicaConfig") is not None:
        import capo_arc_region_switch.types.rds_create_cross_region_replica_configuration

        return {
            "rdsCreateCrossRegionReadReplicaConfig": capo_arc_region_switch.types.rds_create_cross_region_replica_configuration.deserialize_aws_json_1_0(
                data["rdsCreateCrossRegionReadReplicaConfig"]
            )
        }
    elif data.get("lambdaEventSourceMappingConfig") is not None:
        import capo_arc_region_switch.types.lambda_event_source_mapping_configuration

        return {
            "lambdaEventSourceMappingConfig": capo_arc_region_switch.types.lambda_event_source_mapping_configuration.deserialize_aws_json_1_0(
                data["lambdaEventSourceMappingConfig"]
            )
        }
    elif data.get("auroraServerlessScalingConfig") is not None:
        import capo_arc_region_switch.types.aurora_serverless_scaling_configuration

        return {
            "auroraServerlessScalingConfig": capo_arc_region_switch.types.aurora_serverless_scaling_configuration.deserialize_aws_json_1_0(
                data["auroraServerlessScalingConfig"]
            )
        }
    elif data.get("auroraProvisionedScalingConfig") is not None:
        import capo_arc_region_switch.types.aurora_provisioned_scaling_configuration

        return {
            "auroraProvisionedScalingConfig": capo_arc_region_switch.types.aurora_provisioned_scaling_configuration.deserialize_aws_json_1_0(
                data["auroraProvisionedScalingConfig"]
            )
        }
    elif data.get("neptuneGlobalDatabaseConfig") is not None:
        import capo_arc_region_switch.types.neptune_global_database_configuration

        return {
            "neptuneGlobalDatabaseConfig": capo_arc_region_switch.types.neptune_global_database_configuration.deserialize_aws_json_1_0(
                data["neptuneGlobalDatabaseConfig"]
            )
        }
    elif data.get("rdsSwitchoverReadReplicaConfig") is not None:
        import capo_arc_region_switch.types.rds_switchover_read_replica_configuration

        return {
            "rdsSwitchoverReadReplicaConfig": capo_arc_region_switch.types.rds_switchover_read_replica_configuration.deserialize_aws_json_1_0(
                data["rdsSwitchoverReadReplicaConfig"]
            )
        }
    else:
        raise DeserializationError(
            "ExecutionBlockConfiguration: no recognized variant key"
        )
