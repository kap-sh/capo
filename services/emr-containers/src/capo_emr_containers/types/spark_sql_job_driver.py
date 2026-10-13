"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SparkSqlJobDriver``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.entry_point_path
    import capo_emr_containers.types.spark_sql_parameters


class SparkSqlJobDriver(TypedDict, closed=True):
    entry_point: NotRequired[
        "capo_emr_containers.types.entry_point_path.EntryPointPath"
    ]
    """<p>The SQL file to be executed.</p>"""
    spark_sql_parameters: NotRequired[
        "capo_emr_containers.types.spark_sql_parameters.SparkSqlParameters"
    ]
    """<p>The Spark parameters to be included in the Spark SQL command.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkSqlJobDriver) -> dict:
    out: dict = {}
    if "entry_point" in value:
        out["entryPoint"] = value["entry_point"]
    if "spark_sql_parameters" in value:
        out["sparkSqlParameters"] = value["spark_sql_parameters"]
    return out


def deserialize_json(data: dict) -> SparkSqlJobDriver:
    out: SparkSqlJobDriver = {}  # type: ignore[typeddict-item]
    if data.get("entryPoint") is not None:
        out["entry_point"] = data["entryPoint"]
    if data.get("sparkSqlParameters") is not None:
        out["spark_sql_parameters"] = data["sparkSqlParameters"]
    return out


def redact_sensitive(value: SparkSqlJobDriver) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entry_point" in value:
        out["entry_point"] = "*** Sensitive Data Redacted ***"
    if "spark_sql_parameters" in value:
        out["spark_sql_parameters"] = "*** Sensitive Data Redacted ***"
    return out
