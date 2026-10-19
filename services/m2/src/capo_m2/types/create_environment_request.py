"""Generated from Smithy shape ``com.amazonaws.m2#CreateEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.boolean
    import capo_m2.types.client_token
    import capo_m2.types.engine_type
    import capo_m2.types.engine_version
    import capo_m2.types.entity_description
    import capo_m2.types.entity_name
    import capo_m2.types.high_availability_config
    import capo_m2.types.network_type
    import capo_m2.types.storage_configuration_list
    import capo_m2.types.string20
    import capo_m2.types.string50
    import capo_m2.types.string50_list
    import capo_m2.types.tag_map


class CreateEnvironmentRequest(TypedDict, closed=True):
    name: "capo_m2.types.entity_name.EntityName"
    """<p>The name of the runtime environment. Must be unique within the account.</p>"""
    instance_type: "capo_m2.types.string20.String20"
    """<p>The type of instance for the runtime environment.</p>"""
    description: NotRequired["capo_m2.types.entity_description.EntityDescription"]
    """<p>The description of the runtime environment.</p>"""
    engine_type: "capo_m2.types.engine_type.EngineType"
    """<p>The engine type for the runtime environment.</p>"""
    engine_version: NotRequired["capo_m2.types.engine_version.EngineVersion"]
    """<p>The version of the engine type for the runtime environment.</p>"""
    subnet_ids: NotRequired["capo_m2.types.string50_list.String50List"]
    """<p>The list of subnets associated with the VPC for this runtime environment.</p>"""
    security_group_ids: NotRequired["capo_m2.types.string50_list.String50List"]
    """<p>The list of security groups for the VPC associated with this runtime environment.</p>"""
    storage_configurations: NotRequired[
        "capo_m2.types.storage_configuration_list.StorageConfigurationList"
    ]
    """<p>Optional. The storage configurations for this runtime environment.</p>"""
    publicly_accessible: "capo_m2.types.boolean.Boolean"
    """<p>Specifies whether the runtime environment is publicly accessible.</p>"""
    high_availability_config: NotRequired[
        "capo_m2.types.high_availability_config.HighAvailabilityConfig"
    ]
    """<p>The details of a high availability configuration for this runtime environment.</p>"""
    tags: NotRequired["capo_m2.types.tag_map.TagMap"]
    """<p>The tags for the runtime environment.</p>"""
    preferred_maintenance_window: NotRequired["capo_m2.types.string50.String50"]
    """<p>Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format <code>ddd:hh24:mi-ddd:hh24:mi</code> and must be less than 24 hours. The following two examples are valid maintenance windows: <code>sun:23:45-mon:00:15</code> or <code>sat:01:00-sat:03:00</code>. </p> <p>If you do not provide a value, a random system-generated value will be assigned.</p>"""
    network_type: NotRequired["capo_m2.types.network_type.NetworkType"]
    """<p>The network type required for the runtime environment.</p>"""
    client_token: NotRequired["capo_m2.types.client_token.ClientToken"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create an environment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>"""
    kms_key_id: NotRequired["str"]
    """<p>The identifier of a customer managed key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["instanceType"] = value["instance_type"]
    if "description" in value:
        out["description"] = value["description"]
    out["engineType"] = value["engine_type"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "subnet_ids" in value:
        import capo_m2.types.string50_list

        out["subnetIds"] = capo_m2.types.string50_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_m2.types.string50_list

        out["securityGroupIds"] = capo_m2.types.string50_list.serialize_json(
            value["security_group_ids"]
        )
    if "storage_configurations" in value:
        import capo_m2.types.storage_configuration_list

        out["storageConfigurations"] = (
            capo_m2.types.storage_configuration_list.serialize_json(
                value["storage_configurations"]
            )
        )
    out["publiclyAccessible"] = value.get("publicly_accessible", False)
    if "high_availability_config" in value:
        import capo_m2.types.high_availability_config

        out["highAvailabilityConfig"] = (
            capo_m2.types.high_availability_config.serialize_json(
                value["high_availability_config"]
            )
        )
    if "tags" in value:
        import capo_m2.types.tag_map

        out["tags"] = capo_m2.types.tag_map.serialize_json(value["tags"])
    if "preferred_maintenance_window" in value:
        out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "network_type" in value:
        out["networkType"] = value["network_type"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentRequest:
    out: CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        out["instance_type"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("engineType") is not None:
        out["engine_type"] = data["engineType"]
    else:
        out["engine_type"] = ""
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("subnetIds") is not None:
        import capo_m2.types.string50_list

        out["subnet_ids"] = capo_m2.types.string50_list.deserialize_json(
            data["subnetIds"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_m2.types.string50_list

        out["security_group_ids"] = capo_m2.types.string50_list.deserialize_json(
            data["securityGroupIds"]
        )
    if data.get("storageConfigurations") is not None:
        import capo_m2.types.storage_configuration_list

        out["storage_configurations"] = (
            capo_m2.types.storage_configuration_list.deserialize_json(
                data["storageConfigurations"]
            )
        )
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    else:
        out["publicly_accessible"] = False
    if data.get("highAvailabilityConfig") is not None:
        import capo_m2.types.high_availability_config

        out["high_availability_config"] = (
            capo_m2.types.high_availability_config.deserialize_json(
                data["highAvailabilityConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_m2.types.tag_map

        out["tags"] = capo_m2.types.tag_map.deserialize_json(data["tags"])
    if data.get("preferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    if data.get("networkType") is not None:
        out["network_type"] = data["networkType"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
