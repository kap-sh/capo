"""Generated from Smithy shape ``com.amazonaws.emrserverless#SparkSubmit``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.entry_point_arguments
    import capo_emr_serverless.types.entry_point_path
    import capo_emr_serverless.types.spark_submit_parameters


class SparkSubmit(TypedDict, closed=True):
    entry_point: "capo_emr_serverless.types.entry_point_path.EntryPointPath"
    """<p>The entry point for the Spark submit job run.</p>"""
    entry_point_arguments: NotRequired[
        "capo_emr_serverless.types.entry_point_arguments.EntryPointArguments"
    ]
    """<p>The arguments for the Spark submit job run.</p>"""
    spark_submit_parameters: NotRequired[
        "capo_emr_serverless.types.spark_submit_parameters.SparkSubmitParameters"
    ]
    """<p>The parameters for the Spark submit job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkSubmit) -> dict:
    out: dict = {}
    out["entryPoint"] = value["entry_point"]
    if "entry_point_arguments" in value:
        import capo_emr_serverless.types.entry_point_arguments

        out["entryPointArguments"] = (
            capo_emr_serverless.types.entry_point_arguments.serialize_json(
                value["entry_point_arguments"]
            )
        )
    if "spark_submit_parameters" in value:
        out["sparkSubmitParameters"] = value["spark_submit_parameters"]
    return out


def deserialize_json(data: dict) -> SparkSubmit:
    out: SparkSubmit = {}  # type: ignore[typeddict-item]
    if data.get("entryPoint") is not None:
        out["entry_point"] = data["entryPoint"]
    else:
        raise DeserializationError("SparkSubmit.entry_point required")
    if data.get("entryPointArguments") is not None:
        import capo_emr_serverless.types.entry_point_arguments

        out["entry_point_arguments"] = (
            capo_emr_serverless.types.entry_point_arguments.deserialize_json(
                data["entryPointArguments"]
            )
        )
    if data.get("sparkSubmitParameters") is not None:
        out["spark_submit_parameters"] = data["sparkSubmitParameters"]
    return out


def redact_sensitive(value: SparkSubmit) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entry_point" in value:
        out["entry_point"] = "*** Sensitive Data Redacted ***"
    if "entry_point_arguments" in value:
        import capo_emr_serverless.types.entry_point_arguments

        out["entry_point_arguments"] = (
            capo_emr_serverless.types.entry_point_arguments.redact_sensitive(
                value["entry_point_arguments"]
            )
        )
    if "spark_submit_parameters" in value:
        out["spark_submit_parameters"] = "*** Sensitive Data Redacted ***"
    return out
