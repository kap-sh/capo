"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_config_glue_tables


class DataQualityEvaluationConfigDataSource(TypedDict, closed=True):
    glue_tables: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_glue_tables.DataQualityEvaluationConfigGlueTables"
    ]
    """<p>The Glue Data Catalog tables that the configuration applies to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationConfigDataSource) -> dict:
    out: dict = {}
    if "glue_tables" in value:
        import capo_glue.types.data_quality_evaluation_config_glue_tables

        out["GlueTables"] = (
            capo_glue.types.data_quality_evaluation_config_glue_tables.serialize_aws_json_1_1(
                value["glue_tables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityEvaluationConfigDataSource:
    out: DataQualityEvaluationConfigDataSource = {}  # type: ignore[typeddict-item]
    if data.get("GlueTables") is not None:
        import capo_glue.types.data_quality_evaluation_config_glue_tables

        out["glue_tables"] = (
            capo_glue.types.data_quality_evaluation_config_glue_tables.deserialize_aws_json_1_1(
                data["GlueTables"]
            )
        )
    return out
