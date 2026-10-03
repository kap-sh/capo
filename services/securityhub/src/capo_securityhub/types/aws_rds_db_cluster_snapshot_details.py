"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterSnapshotDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attributes
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class AwsRdsDbClusterSnapshotDetails(TypedDict, closed=True):
    availability_zones: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>A list of Availability Zones where instances in the DB cluster can be created.</p>"""
    snapshot_create_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the snapshot was taken.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    engine: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the database engine that you want to use for this DB instance.</p>"""
    allocated_storage: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>Specifies the allocated storage size in gibibytes (GiB).</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of this DB cluster snapshot.</p>"""
    port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The port number on which the DB instances in the DB cluster accept connections.</p>"""
    vpc_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The VPC ID that is associated with the DB cluster snapshot.</p>"""
    cluster_create_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the DB cluster was created, in Universal Coordinated Time (UTC).</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    master_username: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the master user for the DB cluster.</p>"""
    engine_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the database engine to use.</p>"""
    license_model: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The license model information for this DB cluster snapshot.</p>"""
    snapshot_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of DB cluster snapshot.</p>"""
    percent_progress: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>Specifies the percentage of the estimated data that has been transferred.</p>"""
    storage_encrypted: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the DB cluster is encrypted.</p>"""
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the KMS master key that is used to encrypt the database instances in the DB cluster.</p>"""
    db_cluster_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The DB cluster identifier.</p>"""
    db_cluster_snapshot_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the DB cluster snapshot.</p>"""
    iam_database_authentication_enabled: NotRequired[
        "capo_securityhub.types.boolean.Boolean"
    ]
    """<p>Whether mapping of IAM accounts to database accounts is enabled.</p>"""
    db_cluster_snapshot_attributes: NotRequired[
        "capo_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attributes.AwsRdsDbClusterSnapshotDbClusterSnapshotAttributes"
    ]
    """<p> Contains the name and values of a manual DB cluster snapshot attribute. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterSnapshotDetails) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import capo_securityhub.types.string_list

        out["AvailabilityZones"] = capo_securityhub.types.string_list.serialize_json(
            value["availability_zones"]
        )
    if "snapshot_create_time" in value:
        out["SnapshotCreateTime"] = value["snapshot_create_time"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "allocated_storage" in value:
        out["AllocatedStorage"] = value["allocated_storage"]
    if "status" in value:
        out["Status"] = value["status"]
    if "port" in value:
        out["Port"] = value["port"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "cluster_create_time" in value:
        out["ClusterCreateTime"] = value["cluster_create_time"]
    if "master_username" in value:
        out["MasterUsername"] = value["master_username"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "license_model" in value:
        out["LicenseModel"] = value["license_model"]
    if "snapshot_type" in value:
        out["SnapshotType"] = value["snapshot_type"]
    if "percent_progress" in value:
        out["PercentProgress"] = value["percent_progress"]
    if "storage_encrypted" in value:
        out["StorageEncrypted"] = value["storage_encrypted"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "db_cluster_identifier" in value:
        out["DbClusterIdentifier"] = value["db_cluster_identifier"]
    if "db_cluster_snapshot_identifier" in value:
        out["DbClusterSnapshotIdentifier"] = value["db_cluster_snapshot_identifier"]
    if "iam_database_authentication_enabled" in value:
        out["IamDatabaseAuthenticationEnabled"] = value[
            "iam_database_authentication_enabled"
        ]
    if "db_cluster_snapshot_attributes" in value:
        import capo_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attributes

        out["DbClusterSnapshotAttributes"] = (
            capo_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attributes.serialize_json(
                value["db_cluster_snapshot_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsRdsDbClusterSnapshotDetails:
    out: AwsRdsDbClusterSnapshotDetails = {}  # type: ignore[typeddict-item]
    if data.get("AvailabilityZones") is not None:
        import capo_securityhub.types.string_list

        out["availability_zones"] = capo_securityhub.types.string_list.deserialize_json(
            data["AvailabilityZones"]
        )
    if data.get("SnapshotCreateTime") is not None:
        out["snapshot_create_time"] = data["SnapshotCreateTime"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("AllocatedStorage") is not None:
        out["allocated_storage"] = data["AllocatedStorage"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("ClusterCreateTime") is not None:
        out["cluster_create_time"] = data["ClusterCreateTime"]
    if data.get("MasterUsername") is not None:
        out["master_username"] = data["MasterUsername"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("LicenseModel") is not None:
        out["license_model"] = data["LicenseModel"]
    if data.get("SnapshotType") is not None:
        out["snapshot_type"] = data["SnapshotType"]
    if data.get("PercentProgress") is not None:
        out["percent_progress"] = data["PercentProgress"]
    if data.get("StorageEncrypted") is not None:
        out["storage_encrypted"] = data["StorageEncrypted"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("DbClusterIdentifier") is not None:
        out["db_cluster_identifier"] = data["DbClusterIdentifier"]
    if data.get("DbClusterSnapshotIdentifier") is not None:
        out["db_cluster_snapshot_identifier"] = data["DbClusterSnapshotIdentifier"]
    if data.get("IamDatabaseAuthenticationEnabled") is not None:
        out["iam_database_authentication_enabled"] = data[
            "IamDatabaseAuthenticationEnabled"
        ]
    if data.get("DbClusterSnapshotAttributes") is not None:
        import capo_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attributes

        out["db_cluster_snapshot_attributes"] = (
            capo_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attributes.deserialize_json(
                data["DbClusterSnapshotAttributes"]
            )
        )
    return out
