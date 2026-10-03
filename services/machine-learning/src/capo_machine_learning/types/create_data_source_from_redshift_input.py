"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateDataSourceFromRedshiftInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import capo_machine_learning.types.compute_statistics
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name
    import capo_machine_learning.types.redshift_data_spec
    import capo_machine_learning.types.role_arn


class CreateDataSourceFromRedshiftInput(TypedDict, closed=True):
    data_source_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>DataSource</code>.</p>"""
    data_source_name: NotRequired["capo_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>DataSource</code>. </p>"""
    data_spec: "capo_machine_learning.types.redshift_data_spec.RedshiftDataSpec"
    r"""<p>The data specification of an Amazon Redshift <code>DataSource</code>:</p> <ul> <li> <p>DatabaseInformation -</p> <ul> <li> <p> <code>DatabaseName</code> - The name of the Amazon Redshift database.</p> </li> <li> <p> <code> ClusterIdentifier</code> - The unique ID for the Amazon Redshift cluster.</p> </li> </ul> </li> <li> <p>DatabaseCredentials - The AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon Redshift database.</p> </li> <li> <p>SelectSqlQuery - The query that is used to retrieve the observation data for the <code>Datasource</code>.</p> </li> <li> <p>S3StagingLocation - The Amazon Simple Storage Service (Amazon S3) location for staging Amazon Redshift data. The data retrieved from Amazon Redshift using the <code>SelectSqlQuery</code> query is stored in this location.</p> </li> <li> <p>DataSchemaUri - The Amazon S3 location of the <code>DataSchema</code>.</p> </li> <li> <p>DataSchema - A JSON string representing the schema. This is not required if <code>DataSchemaUri</code> is specified. </p> </li> <li> <p>DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the <code>DataSource</code>.</p> <p> Sample - <code> "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"</code> </p> </li> </ul>"""
    role_arn: "capo_machine_learning.types.role_arn.RoleARN"
    """<p>A fully specified role Amazon Resource Name (ARN). Amazon ML assumes the role on behalf of the user to create the following:</p> <ul> <li> <p>A security group to allow Amazon ML to execute the <code>SelectSqlQuery</code> query on an Amazon Redshift cluster</p> </li> <li> <p>An Amazon S3 bucket policy to grant Amazon ML read/write permissions on the <code>S3StagingLocation</code> </p> </li> </ul>"""
    compute_statistics: (
        "capo_machine_learning.types.compute_statistics.ComputeStatistics"
    )
    """<p>The compute statistics for a <code>DataSource</code>. The statistics are generated from the observation data referenced by a <code>DataSource</code>. Amazon ML uses the statistics internally during <code>MLModel</code> training. This parameter must be set to <code>true</code> if the <code>DataSource</code> needs to be used for <code>MLModel</code> training.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataSourceFromRedshiftInput) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    if "data_source_name" in value:
        out["DataSourceName"] = value["data_source_name"]
    import capo_machine_learning.types.redshift_data_spec

    out["DataSpec"] = (
        capo_machine_learning.types.redshift_data_spec.serialize_aws_json_1_1(
            value["data_spec"]
        )
    )
    out["RoleARN"] = value["role_arn"]
    out["ComputeStatistics"] = value.get("compute_statistics", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataSourceFromRedshiftInput:
    out: CreateDataSourceFromRedshiftInput = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError(
            "CreateDataSourceFromRedshiftInput.data_source_id required"
        )
    if data.get("DataSourceName") is not None:
        out["data_source_name"] = data["DataSourceName"]
    if data.get("DataSpec") is not None:
        import capo_machine_learning.types.redshift_data_spec

        out["data_spec"] = (
            capo_machine_learning.types.redshift_data_spec.deserialize_aws_json_1_1(
                data["DataSpec"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataSourceFromRedshiftInput.data_spec required"
        )
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError(
            "CreateDataSourceFromRedshiftInput.role_arn required"
        )
    if data.get("ComputeStatistics") is not None:
        out["compute_statistics"] = data["ComputeStatistics"]
    else:
        out["compute_statistics"] = False
    return out
