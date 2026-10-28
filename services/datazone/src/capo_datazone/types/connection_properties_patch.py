"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionPropertiesPatch``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.amazon_q_properties_patch
    import capo_datazone.types.athena_properties_patch
    import capo_datazone.types.git_properties_patch
    import capo_datazone.types.glue_properties_patch
    import capo_datazone.types.iam_properties_patch
    import capo_datazone.types.lakehouse_properties_patch
    import capo_datazone.types.mlflow_properties_patch
    import capo_datazone.types.redshift_properties_patch
    import capo_datazone.types.s3_properties_patch
    import capo_datazone.types.snowflake_properties_patch
    import capo_datazone.types.spark_emr_properties_patch
    import capo_datazone.types.vpc_properties_patch


class ConnectionPropertiesPatchAthenaPropertiesMember(TypedDict, closed=True):
    athenaProperties: (
        "capo_datazone.types.athena_properties_patch.AthenaPropertiesPatch"
    )


class ConnectionPropertiesPatchGluePropertiesMember(TypedDict, closed=True):
    glueProperties: "capo_datazone.types.glue_properties_patch.GluePropertiesPatch"


class ConnectionPropertiesPatchIamPropertiesMember(TypedDict, closed=True):
    iamProperties: "capo_datazone.types.iam_properties_patch.IamPropertiesPatch"


class ConnectionPropertiesPatchRedshiftPropertiesMember(TypedDict, closed=True):
    redshiftProperties: (
        "capo_datazone.types.redshift_properties_patch.RedshiftPropertiesPatch"
    )


class ConnectionPropertiesPatchSparkEmrPropertiesMember(TypedDict, closed=True):
    sparkEmrProperties: (
        "capo_datazone.types.spark_emr_properties_patch.SparkEmrPropertiesPatch"
    )


class ConnectionPropertiesPatchS3PropertiesMember(TypedDict, closed=True):
    s3Properties: "capo_datazone.types.s3_properties_patch.S3PropertiesPatch"


class ConnectionPropertiesPatchSnowflakePropertiesMember(TypedDict, closed=True):
    snowflakeProperties: (
        "capo_datazone.types.snowflake_properties_patch.SnowflakePropertiesPatch"
    )


class ConnectionPropertiesPatchAmazonQPropertiesMember(TypedDict, closed=True):
    amazonQProperties: (
        "capo_datazone.types.amazon_q_properties_patch.AmazonQPropertiesPatch"
    )


class ConnectionPropertiesPatchMlflowPropertiesMember(TypedDict, closed=True):
    mlflowProperties: (
        "capo_datazone.types.mlflow_properties_patch.MlflowPropertiesPatch"
    )


class ConnectionPropertiesPatchLakehousePropertiesMember(TypedDict, closed=True):
    lakehouseProperties: (
        "capo_datazone.types.lakehouse_properties_patch.LakehousePropertiesPatch"
    )


class ConnectionPropertiesPatchVpcPropertiesMember(TypedDict, closed=True):
    vpcProperties: "capo_datazone.types.vpc_properties_patch.VpcPropertiesPatch"


class ConnectionPropertiesPatchGitPropertiesMember(TypedDict, closed=True):
    gitProperties: "capo_datazone.types.git_properties_patch.GitPropertiesPatch"


ConnectionPropertiesPatch: TypeAlias = (
    ConnectionPropertiesPatchAthenaPropertiesMember
    | ConnectionPropertiesPatchGluePropertiesMember
    | ConnectionPropertiesPatchIamPropertiesMember
    | ConnectionPropertiesPatchRedshiftPropertiesMember
    | ConnectionPropertiesPatchSparkEmrPropertiesMember
    | ConnectionPropertiesPatchS3PropertiesMember
    | ConnectionPropertiesPatchSnowflakePropertiesMember
    | ConnectionPropertiesPatchAmazonQPropertiesMember
    | ConnectionPropertiesPatchMlflowPropertiesMember
    | ConnectionPropertiesPatchLakehousePropertiesMember
    | ConnectionPropertiesPatchVpcPropertiesMember
    | ConnectionPropertiesPatchGitPropertiesMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionPropertiesPatch) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConnectionPropertiesPatch: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "athenaProperties" in value:
        import capo_datazone.types.athena_properties_patch

        return {
            "athenaProperties": capo_datazone.types.athena_properties_patch.serialize_json(
                value["athenaProperties"]
            )
        }
    elif "glueProperties" in value:
        import capo_datazone.types.glue_properties_patch

        return {
            "glueProperties": capo_datazone.types.glue_properties_patch.serialize_json(
                value["glueProperties"]
            )
        }
    elif "iamProperties" in value:
        import capo_datazone.types.iam_properties_patch

        return {
            "iamProperties": capo_datazone.types.iam_properties_patch.serialize_json(
                value["iamProperties"]
            )
        }
    elif "redshiftProperties" in value:
        import capo_datazone.types.redshift_properties_patch

        return {
            "redshiftProperties": capo_datazone.types.redshift_properties_patch.serialize_json(
                value["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in value:
        import capo_datazone.types.spark_emr_properties_patch

        return {
            "sparkEmrProperties": capo_datazone.types.spark_emr_properties_patch.serialize_json(
                value["sparkEmrProperties"]
            )
        }
    elif "s3Properties" in value:
        import capo_datazone.types.s3_properties_patch

        return {
            "s3Properties": capo_datazone.types.s3_properties_patch.serialize_json(
                value["s3Properties"]
            )
        }
    elif "snowflakeProperties" in value:
        import capo_datazone.types.snowflake_properties_patch

        return {
            "snowflakeProperties": capo_datazone.types.snowflake_properties_patch.serialize_json(
                value["snowflakeProperties"]
            )
        }
    elif "amazonQProperties" in value:
        import capo_datazone.types.amazon_q_properties_patch

        return {
            "amazonQProperties": capo_datazone.types.amazon_q_properties_patch.serialize_json(
                value["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in value:
        import capo_datazone.types.mlflow_properties_patch

        return {
            "mlflowProperties": capo_datazone.types.mlflow_properties_patch.serialize_json(
                value["mlflowProperties"]
            )
        }
    elif "lakehouseProperties" in value:
        import capo_datazone.types.lakehouse_properties_patch

        return {
            "lakehouseProperties": capo_datazone.types.lakehouse_properties_patch.serialize_json(
                value["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in value:
        import capo_datazone.types.vpc_properties_patch

        return {
            "vpcProperties": capo_datazone.types.vpc_properties_patch.serialize_json(
                value["vpcProperties"]
            )
        }
    elif "gitProperties" in value:
        import capo_datazone.types.git_properties_patch

        return {
            "gitProperties": capo_datazone.types.git_properties_patch.serialize_json(
                value["gitProperties"]
            )
        }
    else:
        raise SerializationError("ConnectionPropertiesPatch: no variant present")


def deserialize_json(data: dict) -> ConnectionPropertiesPatch:
    if data.get("athenaProperties") is not None:
        import capo_datazone.types.athena_properties_patch

        return {
            "athenaProperties": capo_datazone.types.athena_properties_patch.deserialize_json(
                data["athenaProperties"]
            )
        }
    elif data.get("glueProperties") is not None:
        import capo_datazone.types.glue_properties_patch

        return {
            "glueProperties": capo_datazone.types.glue_properties_patch.deserialize_json(
                data["glueProperties"]
            )
        }
    elif data.get("iamProperties") is not None:
        import capo_datazone.types.iam_properties_patch

        return {
            "iamProperties": capo_datazone.types.iam_properties_patch.deserialize_json(
                data["iamProperties"]
            )
        }
    elif data.get("redshiftProperties") is not None:
        import capo_datazone.types.redshift_properties_patch

        return {
            "redshiftProperties": capo_datazone.types.redshift_properties_patch.deserialize_json(
                data["redshiftProperties"]
            )
        }
    elif data.get("sparkEmrProperties") is not None:
        import capo_datazone.types.spark_emr_properties_patch

        return {
            "sparkEmrProperties": capo_datazone.types.spark_emr_properties_patch.deserialize_json(
                data["sparkEmrProperties"]
            )
        }
    elif data.get("s3Properties") is not None:
        import capo_datazone.types.s3_properties_patch

        return {
            "s3Properties": capo_datazone.types.s3_properties_patch.deserialize_json(
                data["s3Properties"]
            )
        }
    elif data.get("snowflakeProperties") is not None:
        import capo_datazone.types.snowflake_properties_patch

        return {
            "snowflakeProperties": capo_datazone.types.snowflake_properties_patch.deserialize_json(
                data["snowflakeProperties"]
            )
        }
    elif data.get("amazonQProperties") is not None:
        import capo_datazone.types.amazon_q_properties_patch

        return {
            "amazonQProperties": capo_datazone.types.amazon_q_properties_patch.deserialize_json(
                data["amazonQProperties"]
            )
        }
    elif data.get("mlflowProperties") is not None:
        import capo_datazone.types.mlflow_properties_patch

        return {
            "mlflowProperties": capo_datazone.types.mlflow_properties_patch.deserialize_json(
                data["mlflowProperties"]
            )
        }
    elif data.get("lakehouseProperties") is not None:
        import capo_datazone.types.lakehouse_properties_patch

        return {
            "lakehouseProperties": capo_datazone.types.lakehouse_properties_patch.deserialize_json(
                data["lakehouseProperties"]
            )
        }
    elif data.get("vpcProperties") is not None:
        import capo_datazone.types.vpc_properties_patch

        return {
            "vpcProperties": capo_datazone.types.vpc_properties_patch.deserialize_json(
                data["vpcProperties"]
            )
        }
    elif data.get("gitProperties") is not None:
        import capo_datazone.types.git_properties_patch

        return {
            "gitProperties": capo_datazone.types.git_properties_patch.deserialize_json(
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
            "ConnectionPropertiesPatch: no recognized variant key"
        )


def redact_sensitive(value: ConnectionPropertiesPatch) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "glueProperties" in value:
        import capo_datazone.types.glue_properties_patch

        out["glueProperties"] = (
            capo_datazone.types.glue_properties_patch.redact_sensitive(
                value["glueProperties"]
            )
        )
    if "redshiftProperties" in value:
        import capo_datazone.types.redshift_properties_patch

        out["redshiftProperties"] = (
            capo_datazone.types.redshift_properties_patch.redact_sensitive(
                value["redshiftProperties"]
            )
        )
    if "snowflakeProperties" in value:
        import capo_datazone.types.snowflake_properties_patch

        out["snowflakeProperties"] = (
            capo_datazone.types.snowflake_properties_patch.redact_sensitive(
                value["snowflakeProperties"]
            )
        )
    return out
