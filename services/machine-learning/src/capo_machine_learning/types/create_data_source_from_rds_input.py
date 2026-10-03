"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateDataSourceFromRDSInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import capo_machine_learning.types.compute_statistics
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name
    import capo_machine_learning.types.rds_data_spec
    import capo_machine_learning.types.role_arn


class CreateDataSourceFromRDSInput(TypedDict, closed=True):
    data_source_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>DataSource</code>. Typically, an Amazon Resource Number (ARN) becomes the ID for a <code>DataSource</code>.</p>"""
    data_source_name: NotRequired["capo_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>DataSource</code>.</p>"""
    rds_data: "capo_machine_learning.types.rds_data_spec.RDSDataSpec"
    r"""<p>The data specification of an Amazon RDS <code>DataSource</code>:</p> <ul> <li> <p>DatabaseInformation -</p> <ul> <li> <p> <code>DatabaseName</code> - The name of the Amazon RDS database.</p> </li> <li> <p> <code>InstanceIdentifier </code> - A unique identifier for the Amazon RDS database instance.</p> </li> </ul> </li> <li> <p>DatabaseCredentials - AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon RDS database.</p> </li> <li> <p>ResourceRole - A role (DataPipelineDefaultResourceRole) assumed by an EC2 instance to carry out the copy task from Amazon RDS to Amazon Simple Storage Service (Amazon S3). For more information, see <a href="https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html">Role templates</a> for data pipelines.</p> </li> <li> <p>ServiceRole - A role (DataPipelineDefaultRole) assumed by the AWS Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see <a href="https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html">Role templates</a> for data pipelines.</p> </li> <li> <p>SecurityInfo - The security information to use to access an RDS DB instance. You need to set up appropriate ingress rules for the security entity IDs provided to allow access to the Amazon RDS instance. Specify a [<code>SubnetId</code>, <code>SecurityGroupIds</code>] pair for a VPC-based RDS DB instance.</p> </li> <li> <p>SelectSqlQuery - A query that is used to retrieve the observation data for the <code>Datasource</code>.</p> </li> <li> <p>S3StagingLocation - The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using <code>SelectSqlQuery</code> is stored in this location.</p> </li> <li> <p>DataSchemaUri - The Amazon S3 location of the <code>DataSchema</code>.</p> </li> <li> <p>DataSchema - A JSON string representing the schema. This is not required if <code>DataSchemaUri</code> is specified. </p> </li> <li> <p>DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the <code>Datasource</code>. </p> <p> Sample - <code> "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"</code> </p> </li> </ul>"""
    role_arn: "capo_machine_learning.types.role_arn.RoleARN"
    """<p>The role that Amazon ML assumes on behalf of the user to create and activate a data pipeline in the user's account and copy data using the <code>SelectSqlQuery</code> query from Amazon RDS to Amazon S3.</p> <p></p>"""
    compute_statistics: (
        "capo_machine_learning.types.compute_statistics.ComputeStatistics"
    )
    """<p>The compute statistics for a <code>DataSource</code>. The statistics are generated from the observation data referenced by a <code>DataSource</code>. Amazon ML uses the statistics internally during <code>MLModel</code> training. This parameter must be set to <code>true</code> if the <code></code>DataSource<code></code> needs to be used for <code>MLModel</code> training. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataSourceFromRDSInput) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    if "data_source_name" in value:
        out["DataSourceName"] = value["data_source_name"]
    import capo_machine_learning.types.rds_data_spec

    out["RDSData"] = capo_machine_learning.types.rds_data_spec.serialize_aws_json_1_1(
        value["rds_data"]
    )
    out["RoleARN"] = value["role_arn"]
    out["ComputeStatistics"] = value.get("compute_statistics", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataSourceFromRDSInput:
    out: CreateDataSourceFromRDSInput = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError(
            "CreateDataSourceFromRDSInput.data_source_id required"
        )
    if data.get("DataSourceName") is not None:
        out["data_source_name"] = data["DataSourceName"]
    if data.get("RDSData") is not None:
        import capo_machine_learning.types.rds_data_spec

        out["rds_data"] = (
            capo_machine_learning.types.rds_data_spec.deserialize_aws_json_1_1(
                data["RDSData"]
            )
        )
    else:
        raise DeserializationError("CreateDataSourceFromRDSInput.rds_data required")
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("CreateDataSourceFromRDSInput.role_arn required")
    if data.get("ComputeStatistics") is not None:
        out["compute_statistics"] = data["ComputeStatistics"]
    else:
        out["compute_statistics"] = False
    return out
