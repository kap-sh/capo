"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionPropertiesOutput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.amazon_q_properties_output
    import capo_datazone.types.athena_properties_output
    import capo_datazone.types.git_properties_output
    import capo_datazone.types.glue_properties_output
    import capo_datazone.types.hyper_pod_properties_output
    import capo_datazone.types.iam_properties_output
    import capo_datazone.types.lakehouse_properties_output
    import capo_datazone.types.mlflow_properties_output
    import capo_datazone.types.redshift_properties_output
    import capo_datazone.types.s3_properties_output
    import capo_datazone.types.snowflake_properties_output
    import capo_datazone.types.spark_emr_properties_output
    import capo_datazone.types.spark_glue_properties_output
    import capo_datazone.types.vpc_properties_output
    import capo_datazone.types.workflows_mwaa_properties_output
    import capo_datazone.types.workflows_serverless_properties_output


class ConnectionPropertiesOutputAthenaPropertiesMember(TypedDict, closed=True):
    athenaProperties: (
        "capo_datazone.types.athena_properties_output.AthenaPropertiesOutput"
    )


class ConnectionPropertiesOutputGluePropertiesMember(TypedDict, closed=True):
    glueProperties: "capo_datazone.types.glue_properties_output.GluePropertiesOutput"


class ConnectionPropertiesOutputHyperPodPropertiesMember(TypedDict, closed=True):
    hyperPodProperties: (
        "capo_datazone.types.hyper_pod_properties_output.HyperPodPropertiesOutput"
    )


class ConnectionPropertiesOutputIamPropertiesMember(TypedDict, closed=True):
    iamProperties: "capo_datazone.types.iam_properties_output.IamPropertiesOutput"


class ConnectionPropertiesOutputRedshiftPropertiesMember(TypedDict, closed=True):
    redshiftProperties: (
        "capo_datazone.types.redshift_properties_output.RedshiftPropertiesOutput"
    )


class ConnectionPropertiesOutputSparkEmrPropertiesMember(TypedDict, closed=True):
    sparkEmrProperties: (
        "capo_datazone.types.spark_emr_properties_output.SparkEmrPropertiesOutput"
    )


class ConnectionPropertiesOutputSparkGluePropertiesMember(TypedDict, closed=True):
    sparkGlueProperties: (
        "capo_datazone.types.spark_glue_properties_output.SparkGluePropertiesOutput"
    )


class ConnectionPropertiesOutputS3PropertiesMember(TypedDict, closed=True):
    s3Properties: "capo_datazone.types.s3_properties_output.S3PropertiesOutput"


class ConnectionPropertiesOutputSnowflakePropertiesMember(TypedDict, closed=True):
    snowflakeProperties: (
        "capo_datazone.types.snowflake_properties_output.SnowflakePropertiesOutput"
    )


class ConnectionPropertiesOutputAmazonQPropertiesMember(TypedDict, closed=True):
    amazonQProperties: (
        "capo_datazone.types.amazon_q_properties_output.AmazonQPropertiesOutput"
    )


class ConnectionPropertiesOutputMlflowPropertiesMember(TypedDict, closed=True):
    mlflowProperties: (
        "capo_datazone.types.mlflow_properties_output.MlflowPropertiesOutput"
    )


class ConnectionPropertiesOutputWorkflowsMwaaPropertiesMember(TypedDict, closed=True):
    workflowsMwaaProperties: "capo_datazone.types.workflows_mwaa_properties_output.WorkflowsMwaaPropertiesOutput"


class ConnectionPropertiesOutputWorkflowsServerlessPropertiesMember(
    TypedDict, closed=True
):
    workflowsServerlessProperties: "capo_datazone.types.workflows_serverless_properties_output.WorkflowsServerlessPropertiesOutput"


class ConnectionPropertiesOutputLakehousePropertiesMember(TypedDict, closed=True):
    lakehouseProperties: (
        "capo_datazone.types.lakehouse_properties_output.LakehousePropertiesOutput"
    )


class ConnectionPropertiesOutputVpcPropertiesMember(TypedDict, closed=True):
    vpcProperties: "capo_datazone.types.vpc_properties_output.VpcPropertiesOutput"


class ConnectionPropertiesOutputGitPropertiesMember(TypedDict, closed=True):
    gitProperties: "capo_datazone.types.git_properties_output.GitPropertiesOutput"


ConnectionPropertiesOutput: TypeAlias = (
    ConnectionPropertiesOutputAthenaPropertiesMember
    | ConnectionPropertiesOutputGluePropertiesMember
    | ConnectionPropertiesOutputHyperPodPropertiesMember
    | ConnectionPropertiesOutputIamPropertiesMember
    | ConnectionPropertiesOutputRedshiftPropertiesMember
    | ConnectionPropertiesOutputSparkEmrPropertiesMember
    | ConnectionPropertiesOutputSparkGluePropertiesMember
    | ConnectionPropertiesOutputS3PropertiesMember
    | ConnectionPropertiesOutputSnowflakePropertiesMember
    | ConnectionPropertiesOutputAmazonQPropertiesMember
    | ConnectionPropertiesOutputMlflowPropertiesMember
    | ConnectionPropertiesOutputWorkflowsMwaaPropertiesMember
    | ConnectionPropertiesOutputWorkflowsServerlessPropertiesMember
    | ConnectionPropertiesOutputLakehousePropertiesMember
    | ConnectionPropertiesOutputVpcPropertiesMember
    | ConnectionPropertiesOutputGitPropertiesMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionPropertiesOutput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConnectionPropertiesOutput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "athenaProperties" in value:
        import capo_datazone.types.athena_properties_output

        return {
            "athenaProperties": capo_datazone.types.athena_properties_output.serialize_json(
                value["athenaProperties"]
            )
        }
    elif "glueProperties" in value:
        import capo_datazone.types.glue_properties_output

        return {
            "glueProperties": capo_datazone.types.glue_properties_output.serialize_json(
                value["glueProperties"]
            )
        }
    elif "hyperPodProperties" in value:
        import capo_datazone.types.hyper_pod_properties_output

        return {
            "hyperPodProperties": capo_datazone.types.hyper_pod_properties_output.serialize_json(
                value["hyperPodProperties"]
            )
        }
    elif "iamProperties" in value:
        import capo_datazone.types.iam_properties_output

        return {
            "iamProperties": capo_datazone.types.iam_properties_output.serialize_json(
                value["iamProperties"]
            )
        }
    elif "redshiftProperties" in value:
        import capo_datazone.types.redshift_properties_output

        return {
            "redshiftProperties": capo_datazone.types.redshift_properties_output.serialize_json(
                value["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in value:
        import capo_datazone.types.spark_emr_properties_output

        return {
            "sparkEmrProperties": capo_datazone.types.spark_emr_properties_output.serialize_json(
                value["sparkEmrProperties"]
            )
        }
    elif "sparkGlueProperties" in value:
        import capo_datazone.types.spark_glue_properties_output

        return {
            "sparkGlueProperties": capo_datazone.types.spark_glue_properties_output.serialize_json(
                value["sparkGlueProperties"]
            )
        }
    elif "s3Properties" in value:
        import capo_datazone.types.s3_properties_output

        return {
            "s3Properties": capo_datazone.types.s3_properties_output.serialize_json(
                value["s3Properties"]
            )
        }
    elif "snowflakeProperties" in value:
        import capo_datazone.types.snowflake_properties_output

        return {
            "snowflakeProperties": capo_datazone.types.snowflake_properties_output.serialize_json(
                value["snowflakeProperties"]
            )
        }
    elif "amazonQProperties" in value:
        import capo_datazone.types.amazon_q_properties_output

        return {
            "amazonQProperties": capo_datazone.types.amazon_q_properties_output.serialize_json(
                value["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in value:
        import capo_datazone.types.mlflow_properties_output

        return {
            "mlflowProperties": capo_datazone.types.mlflow_properties_output.serialize_json(
                value["mlflowProperties"]
            )
        }
    elif "workflowsMwaaProperties" in value:
        import capo_datazone.types.workflows_mwaa_properties_output

        return {
            "workflowsMwaaProperties": capo_datazone.types.workflows_mwaa_properties_output.serialize_json(
                value["workflowsMwaaProperties"]
            )
        }
    elif "workflowsServerlessProperties" in value:
        import capo_datazone.types.workflows_serverless_properties_output

        return {
            "workflowsServerlessProperties": capo_datazone.types.workflows_serverless_properties_output.serialize_json(
                value["workflowsServerlessProperties"]
            )
        }
    elif "lakehouseProperties" in value:
        import capo_datazone.types.lakehouse_properties_output

        return {
            "lakehouseProperties": capo_datazone.types.lakehouse_properties_output.serialize_json(
                value["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in value:
        import capo_datazone.types.vpc_properties_output

        return {
            "vpcProperties": capo_datazone.types.vpc_properties_output.serialize_json(
                value["vpcProperties"]
            )
        }
    elif "gitProperties" in value:
        import capo_datazone.types.git_properties_output

        return {
            "gitProperties": capo_datazone.types.git_properties_output.serialize_json(
                value["gitProperties"]
            )
        }
    else:
        raise SerializationError("ConnectionPropertiesOutput: no variant present")


def deserialize_json(data: dict) -> ConnectionPropertiesOutput:
    if data.get("athenaProperties") is not None:
        import capo_datazone.types.athena_properties_output

        return {
            "athenaProperties": capo_datazone.types.athena_properties_output.deserialize_json(
                data["athenaProperties"]
            )
        }
    elif data.get("glueProperties") is not None:
        import capo_datazone.types.glue_properties_output

        return {
            "glueProperties": capo_datazone.types.glue_properties_output.deserialize_json(
                data["glueProperties"]
            )
        }
    elif data.get("hyperPodProperties") is not None:
        import capo_datazone.types.hyper_pod_properties_output

        return {
            "hyperPodProperties": capo_datazone.types.hyper_pod_properties_output.deserialize_json(
                data["hyperPodProperties"]
            )
        }
    elif data.get("iamProperties") is not None:
        import capo_datazone.types.iam_properties_output

        return {
            "iamProperties": capo_datazone.types.iam_properties_output.deserialize_json(
                data["iamProperties"]
            )
        }
    elif data.get("redshiftProperties") is not None:
        import capo_datazone.types.redshift_properties_output

        return {
            "redshiftProperties": capo_datazone.types.redshift_properties_output.deserialize_json(
                data["redshiftProperties"]
            )
        }
    elif data.get("sparkEmrProperties") is not None:
        import capo_datazone.types.spark_emr_properties_output

        return {
            "sparkEmrProperties": capo_datazone.types.spark_emr_properties_output.deserialize_json(
                data["sparkEmrProperties"]
            )
        }
    elif data.get("sparkGlueProperties") is not None:
        import capo_datazone.types.spark_glue_properties_output

        return {
            "sparkGlueProperties": capo_datazone.types.spark_glue_properties_output.deserialize_json(
                data["sparkGlueProperties"]
            )
        }
    elif data.get("s3Properties") is not None:
        import capo_datazone.types.s3_properties_output

        return {
            "s3Properties": capo_datazone.types.s3_properties_output.deserialize_json(
                data["s3Properties"]
            )
        }
    elif data.get("snowflakeProperties") is not None:
        import capo_datazone.types.snowflake_properties_output

        return {
            "snowflakeProperties": capo_datazone.types.snowflake_properties_output.deserialize_json(
                data["snowflakeProperties"]
            )
        }
    elif data.get("amazonQProperties") is not None:
        import capo_datazone.types.amazon_q_properties_output

        return {
            "amazonQProperties": capo_datazone.types.amazon_q_properties_output.deserialize_json(
                data["amazonQProperties"]
            )
        }
    elif data.get("mlflowProperties") is not None:
        import capo_datazone.types.mlflow_properties_output

        return {
            "mlflowProperties": capo_datazone.types.mlflow_properties_output.deserialize_json(
                data["mlflowProperties"]
            )
        }
    elif data.get("workflowsMwaaProperties") is not None:
        import capo_datazone.types.workflows_mwaa_properties_output

        return {
            "workflowsMwaaProperties": capo_datazone.types.workflows_mwaa_properties_output.deserialize_json(
                data["workflowsMwaaProperties"]
            )
        }
    elif data.get("workflowsServerlessProperties") is not None:
        import capo_datazone.types.workflows_serverless_properties_output

        return {
            "workflowsServerlessProperties": capo_datazone.types.workflows_serverless_properties_output.deserialize_json(
                data["workflowsServerlessProperties"]
            )
        }
    elif data.get("lakehouseProperties") is not None:
        import capo_datazone.types.lakehouse_properties_output

        return {
            "lakehouseProperties": capo_datazone.types.lakehouse_properties_output.deserialize_json(
                data["lakehouseProperties"]
            )
        }
    elif data.get("vpcProperties") is not None:
        import capo_datazone.types.vpc_properties_output

        return {
            "vpcProperties": capo_datazone.types.vpc_properties_output.deserialize_json(
                data["vpcProperties"]
            )
        }
    elif data.get("gitProperties") is not None:
        import capo_datazone.types.git_properties_output

        return {
            "gitProperties": capo_datazone.types.git_properties_output.deserialize_json(
                data["gitProperties"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ConnectionPropertiesOutput: no recognized variant key"
        )


def redact_sensitive(value: ConnectionPropertiesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "redshiftProperties" in value:
        import capo_datazone.types.redshift_properties_output

        out["redshiftProperties"] = (
            capo_datazone.types.redshift_properties_output.redact_sensitive(
                value["redshiftProperties"]
            )
        )
    if "sparkEmrProperties" in value:
        import capo_datazone.types.spark_emr_properties_output

        out["sparkEmrProperties"] = (
            capo_datazone.types.spark_emr_properties_output.redact_sensitive(
                value["sparkEmrProperties"]
            )
        )
    return out
