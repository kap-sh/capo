"""Generated from Smithy shape ``com.amazonaws.m2#GetEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.arn
    import capo_m2.types.boolean
    import capo_m2.types.capacity_value
    import capo_m2.types.engine_type
    import capo_m2.types.engine_version
    import capo_m2.types.entity_description
    import capo_m2.types.entity_name
    import capo_m2.types.environment_lifecycle
    import capo_m2.types.high_availability_config
    import capo_m2.types.identifier
    import capo_m2.types.network_type
    import capo_m2.types.pending_maintenance
    import capo_m2.types.storage_configuration_list
    import capo_m2.types.string20
    import capo_m2.types.string50
    import capo_m2.types.string50_list
    import capo_m2.types.tag_map
    import capo_m2.types.timestamp


class GetEnvironmentResponse(TypedDict, closed=True):
    name: "capo_m2.types.entity_name.EntityName"
    """<p>The name of the runtime environment. Must be unique within the account.</p>"""
    description: NotRequired["capo_m2.types.entity_description.EntityDescription"]
    """<p>The description of the runtime environment.</p>"""
    environment_arn: "capo_m2.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the runtime environment.</p>"""
    environment_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment.</p>"""
    instance_type: "capo_m2.types.string20.String20"
    """<p>The type of instance underlying the runtime environment.</p>"""
    status: "capo_m2.types.environment_lifecycle.EnvironmentLifecycle"
    """<p>The status of the runtime environment. If the Amazon Web Services Mainframe Modernization environment is missing a connection to the customer owned dependent resource, the status will be <code>Unhealthy</code>.</p>"""
    engine_type: "capo_m2.types.engine_type.EngineType"
    """<p>The target platform for the runtime environment.</p>"""
    engine_version: "capo_m2.types.engine_version.EngineVersion"
    """<p>The version of the runtime engine.</p>"""
    vpc_id: "capo_m2.types.string50.String50"
    """<p>The unique identifier for the VPC used with this runtime environment.</p>"""
    subnet_ids: "capo_m2.types.string50_list.String50List"
    """<p>The unique identifiers of the subnets assigned to this runtime environment.</p>"""
    security_group_ids: "capo_m2.types.string50_list.String50List"
    """<p>The unique identifiers of the security groups assigned to this runtime environment.</p>"""
    creation_time: "capo_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the runtime environment was created.</p>"""
    storage_configurations: NotRequired[
        "capo_m2.types.storage_configuration_list.StorageConfigurationList"
    ]
    """<p>The storage configurations defined for the runtime environment.</p>"""
    tags: NotRequired["capo_m2.types.tag_map.TagMap"]
    """<p>The tags defined for this runtime environment.</p>"""
    high_availability_config: NotRequired[
        "capo_m2.types.high_availability_config.HighAvailabilityConfig"
    ]
    """<p>The desired capacity of the high availability configuration for the runtime environment.</p>"""
    publicly_accessible: "capo_m2.types.boolean.Boolean"
    """<p>Whether applications running in this runtime environment are publicly accessible. </p>"""
    actual_capacity: NotRequired["capo_m2.types.capacity_value.CapacityValue"]
    """<p>The number of instances included in the runtime environment. A standalone runtime environment has a maximum of one instance. Currently, a high availability runtime environment has a maximum of two instances. </p>"""
    load_balancer_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the load balancer used with the runtime environment.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""
    preferred_maintenance_window: NotRequired["capo_m2.types.string50.String50"]
    """<p>The maintenance window for the runtime environment. If you don't provide a value for the maintenance window, the service assigns a random value.</p>"""
    pending_maintenance: NotRequired[
        "capo_m2.types.pending_maintenance.PendingMaintenance"
    ]
    """<p>Indicates the pending maintenance scheduled on this environment.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The identifier of a customer managed key.</p>"""
    network_type: NotRequired["capo_m2.types.network_type.NetworkType"]
    """<p>The network type supported by the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["environmentArn"] = value["environment_arn"]
    out["environmentId"] = value["environment_id"]
    out["instanceType"] = value["instance_type"]
    out["status"] = value["status"]
    out["engineType"] = value["engine_type"]
    out["engineVersion"] = value["engine_version"]
    out["vpcId"] = value["vpc_id"]
    import capo_m2.types.string50_list

    out["subnetIds"] = capo_m2.types.string50_list.serialize_json(value["subnet_ids"])
    import capo_m2.types.string50_list

    out["securityGroupIds"] = capo_m2.types.string50_list.serialize_json(
        value["security_group_ids"]
    )
    import capo_m2.types.timestamp

    out["creationTime"] = capo_m2.types.timestamp.serialize_json(value["creation_time"])
    if "storage_configurations" in value:
        import capo_m2.types.storage_configuration_list

        out["storageConfigurations"] = (
            capo_m2.types.storage_configuration_list.serialize_json(
                value["storage_configurations"]
            )
        )
    if "tags" in value:
        import capo_m2.types.tag_map

        out["tags"] = capo_m2.types.tag_map.serialize_json(value["tags"])
    if "high_availability_config" in value:
        import capo_m2.types.high_availability_config

        out["highAvailabilityConfig"] = (
            capo_m2.types.high_availability_config.serialize_json(
                value["high_availability_config"]
            )
        )
    out["publiclyAccessible"] = value.get("publicly_accessible", False)
    if "actual_capacity" in value:
        out["actualCapacity"] = value["actual_capacity"]
    if "load_balancer_arn" in value:
        out["loadBalancerArn"] = value["load_balancer_arn"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "preferred_maintenance_window" in value:
        out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "pending_maintenance" in value:
        import capo_m2.types.pending_maintenance

        out["pendingMaintenance"] = capo_m2.types.pending_maintenance.serialize_json(
            value["pending_maintenance"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "network_type" in value:
        out["networkType"] = value["network_type"]
    return out


def deserialize_json(data: dict) -> GetEnvironmentResponse:
    out: GetEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("environmentArn") is not None:
        out["environment_arn"] = data["environmentArn"]
    else:
        out["environment_arn"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        out["instance_type"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("engineType") is not None:
        out["engine_type"] = data["engineType"]
    else:
        out["engine_type"] = ""
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    else:
        out["engine_version"] = ""
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("subnetIds") is not None:
        import capo_m2.types.string50_list

        out["subnet_ids"] = capo_m2.types.string50_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("securityGroupIds") is not None:
        import capo_m2.types.string50_list

        out["security_group_ids"] = capo_m2.types.string50_list.deserialize_json(
            data["securityGroupIds"]
        )
    else:
        out["security_group_ids"] = []
    if data.get("creationTime") is not None:
        import capo_m2.types.timestamp

        out["creation_time"] = capo_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("storageConfigurations") is not None:
        import capo_m2.types.storage_configuration_list

        out["storage_configurations"] = (
            capo_m2.types.storage_configuration_list.deserialize_json(
                data["storageConfigurations"]
            )
        )
    if data.get("tags") is not None:
        import capo_m2.types.tag_map

        out["tags"] = capo_m2.types.tag_map.deserialize_json(data["tags"])
    if data.get("highAvailabilityConfig") is not None:
        import capo_m2.types.high_availability_config

        out["high_availability_config"] = (
            capo_m2.types.high_availability_config.deserialize_json(
                data["highAvailabilityConfig"]
            )
        )
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    else:
        out["publicly_accessible"] = False
    if data.get("actualCapacity") is not None:
        out["actual_capacity"] = data["actualCapacity"]
    if data.get("loadBalancerArn") is not None:
        out["load_balancer_arn"] = data["loadBalancerArn"]
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("preferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    if data.get("pendingMaintenance") is not None:
        import capo_m2.types.pending_maintenance

        out["pending_maintenance"] = capo_m2.types.pending_maintenance.deserialize_json(
            data["pendingMaintenance"]
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("networkType") is not None:
        out["network_type"] = data["networkType"]
    return out
