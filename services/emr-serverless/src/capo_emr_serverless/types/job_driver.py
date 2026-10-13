"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobDriver``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_emr_serverless.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.hive
    import capo_emr_serverless.types.spark_submit


class _JobDriver_sparkSubmit(TypedDict, closed=True):
    sparkSubmit: "capo_emr_serverless.types.spark_submit.SparkSubmit"


class _JobDriver_hive(TypedDict, closed=True):
    hive: "capo_emr_serverless.types.hive.Hive"


JobDriver: TypeAlias = _JobDriver_sparkSubmit | _JobDriver_hive


# --- restJson1 ser/de ---
def serialize_json(value: JobDriver) -> dict:
    if "sparkSubmit" in value:
        import capo_emr_serverless.types.spark_submit

        return {
            "sparkSubmit": capo_emr_serverless.types.spark_submit.serialize_json(
                value["sparkSubmit"]
            )
        }
    elif "hive" in value:
        import capo_emr_serverless.types.hive

        return {"hive": capo_emr_serverless.types.hive.serialize_json(value["hive"])}
    else:
        raise SerializationError("JobDriver: no variant present")


def deserialize_json(data: dict) -> JobDriver:
    if data.get("sparkSubmit") is not None:
        import capo_emr_serverless.types.spark_submit

        return {
            "sparkSubmit": capo_emr_serverless.types.spark_submit.deserialize_json(
                data["sparkSubmit"]
            )
        }
    elif data.get("hive") is not None:
        import capo_emr_serverless.types.hive

        return {"hive": capo_emr_serverless.types.hive.deserialize_json(data["hive"])}
    else:
        raise DeserializationError("JobDriver: no recognized variant key")


def redact_sensitive(value: JobDriver) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sparkSubmit" in value:
        import capo_emr_serverless.types.spark_submit

        out["sparkSubmit"] = capo_emr_serverless.types.spark_submit.redact_sensitive(
            value["sparkSubmit"]
        )
    if "hive" in value:
        import capo_emr_serverless.types.hive

        out["hive"] = capo_emr_serverless.types.hive.redact_sensitive(value["hive"])
    return out
