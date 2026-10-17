"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityTelemetry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_engine
    import capo_glue.types.data_quality_flags_enabled
    import capo_glue.types.name_string
    import capo_glue.types.nullable_double


class DataQualityTelemetry(TypedDict, closed=True):
    vcpu_hours: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    flags_enabled: NotRequired[
        "capo_glue.types.data_quality_flags_enabled.DataQualityFlagsEnabled"
    ]
    library_version: NotRequired["capo_glue.types.name_string.NameString"]
    spark_version: NotRequired["capo_glue.types.name_string.NameString"]
    host_runtime_version: NotRequired["capo_glue.types.name_string.NameString"]
    engine: NotRequired["capo_glue.types.data_quality_engine.DataQualityEngine"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityTelemetry) -> dict:
    out: dict = {}
    if "vcpu_hours" in value:
        out["VcpuHours"] = (
            "NaN"
            if value["vcpu_hours"] != value["vcpu_hours"]
            else "Infinity"
            if value["vcpu_hours"] == float("inf")
            else "-Infinity"
            if value["vcpu_hours"] == float("-inf")
            else value["vcpu_hours"]
        )
    if "flags_enabled" in value:
        import capo_glue.types.data_quality_flags_enabled

        out["FlagsEnabled"] = (
            capo_glue.types.data_quality_flags_enabled.serialize_aws_json_1_1(
                value["flags_enabled"]
            )
        )
    if "library_version" in value:
        out["LibraryVersion"] = value["library_version"]
    if "spark_version" in value:
        out["SparkVersion"] = value["spark_version"]
    if "host_runtime_version" in value:
        out["HostRuntimeVersion"] = value["host_runtime_version"]
    if "engine" in value:
        import capo_glue.types.data_quality_engine

        out["Engine"] = capo_glue.types.data_quality_engine.serialize_aws_json_1_1(
            value["engine"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityTelemetry:
    out: DataQualityTelemetry = {}  # type: ignore[typeddict-item]
    if data.get("VcpuHours") is not None:
        out["vcpu_hours"] = float(data["VcpuHours"])
    if data.get("FlagsEnabled") is not None:
        import capo_glue.types.data_quality_flags_enabled

        out["flags_enabled"] = (
            capo_glue.types.data_quality_flags_enabled.deserialize_aws_json_1_1(
                data["FlagsEnabled"]
            )
        )
    if data.get("LibraryVersion") is not None:
        out["library_version"] = data["LibraryVersion"]
    if data.get("SparkVersion") is not None:
        out["spark_version"] = data["SparkVersion"]
    if data.get("HostRuntimeVersion") is not None:
        out["host_runtime_version"] = data["HostRuntimeVersion"]
    if data.get("Engine") is not None:
        import capo_glue.types.data_quality_engine

        out["engine"] = capo_glue.types.data_quality_engine.deserialize_aws_json_1_1(
            data["Engine"]
        )
    return out
