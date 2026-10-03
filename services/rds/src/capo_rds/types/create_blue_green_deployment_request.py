"""Generated from Smithy shape ``com.amazonaws.rds#CreateBlueGreenDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.blue_green_deployment_name
    import capo_rds.types.boolean_optional
    import capo_rds.types.database_arn
    import capo_rds.types.integer_optional
    import capo_rds.types.tag_list
    import capo_rds.types.target_db_cluster_parameter_group_name
    import capo_rds.types.target_db_instance_class
    import capo_rds.types.target_db_parameter_group_name
    import capo_rds.types.target_engine_version
    import capo_rds.types.target_storage_type


class CreateBlueGreenDeploymentRequest(TypedDict, closed=True):
    blue_green_deployment_name: NotRequired[
        "capo_rds.types.blue_green_deployment_name.BlueGreenDeploymentName"
    ]
    """<p>The name of the blue/green deployment.</p> <p>Constraints:</p> <ul> <li> <p>Can't be the same as an existing blue/green deployment name in the same account and Amazon Web Services Region.</p> </li> </ul>"""
    source: NotRequired["capo_rds.types.database_arn.DatabaseArn"]
    """<p>The Amazon Resource Name (ARN) of the source production database.</p> <p>Specify the database that you want to clone. The blue/green deployment creates this database in the green environment. You can make updates to the database in the green environment, such as an engine version upgrade. When you are ready, you can switch the database in the green environment to be the production database.</p>"""
    target_engine_version: NotRequired[
        "capo_rds.types.target_engine_version.TargetEngineVersion"
    ]
    """<p>The engine version of the database in the green environment.</p> <p>Specify the engine version to upgrade to in the green environment.</p>"""
    target_db_parameter_group_name: NotRequired[
        "capo_rds.types.target_db_parameter_group_name.TargetDBParameterGroupName"
    ]
    """<p>The DB parameter group associated with the DB instance in the green environment.</p> <p>To test parameter changes, specify a DB parameter group that is different from the one associated with the source DB instance.</p>"""
    target_db_cluster_parameter_group_name: NotRequired[
        "capo_rds.types.target_db_cluster_parameter_group_name.TargetDBClusterParameterGroupName"
    ]
    """<p>The DB cluster parameter group associated with the Aurora DB cluster in the green environment.</p> <p>To test parameter changes, specify a DB cluster parameter group that is different from the one associated with the source DB cluster.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>Tags to assign to the blue/green deployment.</p>"""
    target_db_instance_class: NotRequired[
        "capo_rds.types.target_db_instance_class.TargetDBInstanceClass"
    ]
    """<p>Specify the DB instance class for the databases in the green environment.</p> <p>This parameter only applies to RDS DB instances, because DB instances within an Aurora DB cluster can have multiple different instance classes. If you're creating a blue/green deployment from an Aurora DB cluster, don't specify this parameter. After the green environment is created, you can individually modify the instance classes of the DB instances within the green DB cluster.</p>"""
    upgrade_target_storage_config: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether to upgrade the storage file system configuration on the green database. This option migrates the green DB instance from the older 32-bit file system to the preferred configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.UpgradeFileSystem">Upgrading the storage file system for a DB instance</a>.</p>"""
    target_iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to allocate for the green DB instance. For information about valid IOPS values, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html">Amazon RDS DB instance storage</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to Amazon Aurora blue/green deployments.</p>"""
    target_storage_type: NotRequired[
        "capo_rds.types.target_storage_type.TargetStorageType"
    ]
    """<p>The storage type to associate with the green DB instance.</p> <p>Valid Values: <code>gp2 | gp3 | io1 | io2</code> </p> <p>This setting doesn't apply to Amazon Aurora blue/green deployments.</p>"""
    target_allocated_storage: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The amount of storage in gibibytes (GiB) to allocate for the green DB instance. You can choose to increase or decrease the allocated storage on the green DB instance.</p> <p>This setting doesn't apply to Amazon Aurora blue/green deployments.</p>"""
    target_storage_throughput: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The storage throughput value for the green DB instance.</p> <p>This setting applies only to the <code>gp3</code> storage type.</p> <p>This setting doesn't apply to Amazon Aurora blue/green deployments.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateBlueGreenDeploymentRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "blue_green_deployment_name" in value:
        pairs.append(
            (
                f"{key_prefix}BlueGreenDeploymentName",
                str(value["blue_green_deployment_name"]),
            )
        )
    if "source" in value:
        pairs.append((f"{key_prefix}Source", str(value["source"])))
    if "target_engine_version" in value:
        pairs.append(
            (f"{key_prefix}TargetEngineVersion", str(value["target_engine_version"]))
        )
    if "target_db_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDBParameterGroupName",
                str(value["target_db_parameter_group_name"]),
            )
        )
    if "target_db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDBClusterParameterGroupName",
                str(value["target_db_cluster_parameter_group_name"]),
            )
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "target_db_instance_class" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDBInstanceClass",
                str(value["target_db_instance_class"]),
            )
        )
    if "upgrade_target_storage_config" in value:
        pairs.append(
            (
                f"{key_prefix}UpgradeTargetStorageConfig",
                "true" if value["upgrade_target_storage_config"] else "false",
            )
        )
    if "target_iops" in value:
        pairs.append((f"{key_prefix}TargetIops", str(value["target_iops"])))
    if "target_storage_type" in value:
        pairs.append(
            (f"{key_prefix}TargetStorageType", str(value["target_storage_type"]))
        )
    if "target_allocated_storage" in value:
        pairs.append(
            (
                f"{key_prefix}TargetAllocatedStorage",
                str(value["target_allocated_storage"]),
            )
        )
    if "target_storage_throughput" in value:
        pairs.append(
            (
                f"{key_prefix}TargetStorageThroughput",
                str(value["target_storage_throughput"]),
            )
        )


def deserialize_query(el: Element) -> CreateBlueGreenDeploymentRequest:
    out: CreateBlueGreenDeploymentRequest = {}  # type: ignore[typeddict-item]
    child_blue_green_deployment_name = el.find("BlueGreenDeploymentName")
    if child_blue_green_deployment_name is not None:
        out["blue_green_deployment_name"] = str(
            child_blue_green_deployment_name.text or ""
        )
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_target_engine_version = el.find("TargetEngineVersion")
    if child_target_engine_version is not None:
        out["target_engine_version"] = str(child_target_engine_version.text or "")
    child_target_db_parameter_group_name = el.find("TargetDBParameterGroupName")
    if child_target_db_parameter_group_name is not None:
        out["target_db_parameter_group_name"] = str(
            child_target_db_parameter_group_name.text or ""
        )
    child_target_db_cluster_parameter_group_name = el.find(
        "TargetDBClusterParameterGroupName"
    )
    if child_target_db_cluster_parameter_group_name is not None:
        out["target_db_cluster_parameter_group_name"] = str(
            child_target_db_cluster_parameter_group_name.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_target_db_instance_class = el.find("TargetDBInstanceClass")
    if child_target_db_instance_class is not None:
        out["target_db_instance_class"] = str(child_target_db_instance_class.text or "")
    child_upgrade_target_storage_config = el.find("UpgradeTargetStorageConfig")
    if child_upgrade_target_storage_config is not None:
        out["upgrade_target_storage_config"] = (
            child_upgrade_target_storage_config.text or ""
        ).lower() == "true"
    child_target_iops = el.find("TargetIops")
    if child_target_iops is not None:
        out["target_iops"] = int(child_target_iops.text or "")
    child_target_storage_type = el.find("TargetStorageType")
    if child_target_storage_type is not None:
        out["target_storage_type"] = str(child_target_storage_type.text or "")
    child_target_allocated_storage = el.find("TargetAllocatedStorage")
    if child_target_allocated_storage is not None:
        out["target_allocated_storage"] = int(child_target_allocated_storage.text or "")
    child_target_storage_throughput = el.find("TargetStorageThroughput")
    if child_target_storage_throughput is not None:
        out["target_storage_throughput"] = int(
            child_target_storage_throughput.text or ""
        )
    return out
