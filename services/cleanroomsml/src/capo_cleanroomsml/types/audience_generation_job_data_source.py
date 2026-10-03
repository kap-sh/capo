"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceGenerationJobDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.compute_configuration
    import capo_cleanroomsml.types.iam_role_arn
    import capo_cleanroomsml.types.protected_query_sql_parameters
    import capo_cleanroomsml.types.s3_config_map


class AudienceGenerationJobDataSource(TypedDict, closed=True):
    data_source: NotRequired["capo_cleanroomsml.types.s3_config_map.S3ConfigMap"]
    """<p>Defines the Amazon S3 bucket where the seed audience for the generating audience is stored. A valid data source is a JSON line file in the following format:</p> <p> <code>{"user_id": "111111"}</code> </p> <p> <code>{"user_id": "222222"}</code> </p> <p> <code>...</code> </p>"""
    role_arn: "capo_cleanroomsml.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of the IAM role that can read the Amazon S3 bucket where the seed audience is stored.</p>"""
    sql_parameters: NotRequired[
        "capo_cleanroomsml.types.protected_query_sql_parameters.ProtectedQuerySQLParameters"
    ]
    """<p>The protected SQL query parameters.</p>"""
    sql_compute_configuration: NotRequired[
        "capo_cleanroomsml.types.compute_configuration.ComputeConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceGenerationJobDataSource) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_cleanroomsml.types.s3_config_map

        out["dataSource"] = capo_cleanroomsml.types.s3_config_map.serialize_json(
            value["data_source"]
        )
    out["roleArn"] = value["role_arn"]
    if "sql_parameters" in value:
        import capo_cleanroomsml.types.protected_query_sql_parameters

        out["sqlParameters"] = (
            capo_cleanroomsml.types.protected_query_sql_parameters.serialize_json(
                value["sql_parameters"]
            )
        )
    if "sql_compute_configuration" in value:
        import capo_cleanroomsml.types.compute_configuration

        out["sqlComputeConfiguration"] = (
            capo_cleanroomsml.types.compute_configuration.serialize_json(
                value["sql_compute_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudienceGenerationJobDataSource:
    out: AudienceGenerationJobDataSource = {}  # type: ignore[typeddict-item]
    if data.get("dataSource") is not None:
        import capo_cleanroomsml.types.s3_config_map

        out["data_source"] = capo_cleanroomsml.types.s3_config_map.deserialize_json(
            data["dataSource"]
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("AudienceGenerationJobDataSource.role_arn required")
    if data.get("sqlParameters") is not None:
        import capo_cleanroomsml.types.protected_query_sql_parameters

        out["sql_parameters"] = (
            capo_cleanroomsml.types.protected_query_sql_parameters.deserialize_json(
                data["sqlParameters"]
            )
        )
    if data.get("sqlComputeConfiguration") is not None:
        import capo_cleanroomsml.types.compute_configuration

        out["sql_compute_configuration"] = (
            capo_cleanroomsml.types.compute_configuration.deserialize_json(
                data["sqlComputeConfiguration"]
            )
        )
    return out
