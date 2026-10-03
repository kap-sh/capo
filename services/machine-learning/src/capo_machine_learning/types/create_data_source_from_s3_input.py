"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateDataSourceFromS3Input``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import capo_machine_learning.types.compute_statistics
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name
    import capo_machine_learning.types.s3_data_spec


class CreateDataSourceFromS3Input(TypedDict, closed=True):
    data_source_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied identifier that uniquely identifies the <code>DataSource</code>. </p>"""
    data_source_name: NotRequired["capo_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>DataSource</code>. </p>"""
    data_spec: "capo_machine_learning.types.s3_data_spec.S3DataSpec"
    r"""<p>The data specification of a <code>DataSource</code>:</p> <ul> <li> <p>DataLocationS3 - The Amazon S3 location of the observation data.</p> </li> <li> <p>DataSchemaLocationS3 - The Amazon S3 location of the <code>DataSchema</code>.</p> </li> <li> <p>DataSchema - A JSON string representing the schema. This is not required if <code>DataSchemaUri</code> is specified. </p> </li> <li> <p>DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the <code>Datasource</code>. </p> <p> Sample - <code> "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"</code> </p> </li> </ul>"""
    compute_statistics: (
        "capo_machine_learning.types.compute_statistics.ComputeStatistics"
    )
    """<p>The compute statistics for a <code>DataSource</code>. The statistics are generated from the observation data referenced by a <code>DataSource</code>. Amazon ML uses the statistics internally during <code>MLModel</code> training. This parameter must be set to <code>true</code> if the <code></code>DataSource<code></code> needs to be used for <code>MLModel</code> training.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataSourceFromS3Input) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    if "data_source_name" in value:
        out["DataSourceName"] = value["data_source_name"]
    import capo_machine_learning.types.s3_data_spec

    out["DataSpec"] = capo_machine_learning.types.s3_data_spec.serialize_aws_json_1_1(
        value["data_spec"]
    )
    out["ComputeStatistics"] = value.get("compute_statistics", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataSourceFromS3Input:
    out: CreateDataSourceFromS3Input = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError(
            "CreateDataSourceFromS3Input.data_source_id required"
        )
    if data.get("DataSourceName") is not None:
        out["data_source_name"] = data["DataSourceName"]
    if data.get("DataSpec") is not None:
        import capo_machine_learning.types.s3_data_spec

        out["data_spec"] = (
            capo_machine_learning.types.s3_data_spec.deserialize_aws_json_1_1(
                data["DataSpec"]
            )
        )
    else:
        raise DeserializationError("CreateDataSourceFromS3Input.data_spec required")
    if data.get("ComputeStatistics") is not None:
        out["compute_statistics"] = data["ComputeStatistics"]
    else:
        out["compute_statistics"] = False
    return out
