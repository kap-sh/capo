"""Generated from Smithy shape ``com.amazonaws.glue#StatisticSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.column_name_list
    import capo_glue.types.distribution_data
    import capo_glue.types.double
    import capo_glue.types.hash_string
    import capo_glue.types.reference_datasets_list
    import capo_glue.types.run_identifier
    import capo_glue.types.statistic_evaluation_level
    import capo_glue.types.statistic_name_string
    import capo_glue.types.statistic_properties_map
    import capo_glue.types.timestamp
    import capo_glue.types.timestamped_inclusion_annotation


class StatisticSummary(TypedDict, closed=True):
    statistic_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The Statistic ID.</p>"""
    profile_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The Profile ID.</p>"""
    run_identifier: NotRequired["capo_glue.types.run_identifier.RunIdentifier"]
    """<p>The Run Identifier</p>"""
    statistic_name: NotRequired[
        "capo_glue.types.statistic_name_string.StatisticNameString"
    ]
    """<p>The name of the statistic.</p>"""
    double_value: "capo_glue.types.double.Double"
    """<p>The value of the statistic.</p>"""
    distribution_value: NotRequired[
        "capo_glue.types.distribution_data.DistributionData"
    ]
    """<p>The distribution value for the statistic.</p>"""
    evaluation_level: NotRequired[
        "capo_glue.types.statistic_evaluation_level.StatisticEvaluationLevel"
    ]
    """<p>The evaluation level of the statistic. Possible values: <code>Dataset</code>, <code>Column</code>, <code>Multicolumn</code>.</p>"""
    columns_referenced: NotRequired["capo_glue.types.column_name_list.ColumnNameList"]
    """<p>The list of columns referenced by the statistic.</p>"""
    referenced_datasets: NotRequired[
        "capo_glue.types.reference_datasets_list.ReferenceDatasetsList"
    ]
    """<p>The list of datasets referenced by the statistic.</p>"""
    statistic_properties: NotRequired[
        "capo_glue.types.statistic_properties_map.StatisticPropertiesMap"
    ]
    """<p>A <code>StatisticPropertiesMap</code>, which contains a <code>NameString</code> and <code>DescriptionString</code> </p>"""
    recorded_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The timestamp when the statistic was recorded.</p>"""
    inclusion_annotation: NotRequired[
        "capo_glue.types.timestamped_inclusion_annotation.TimestampedInclusionAnnotation"
    ]
    """<p>The inclusion annotation for the statistic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatisticSummary) -> dict:
    out: dict = {}
    if "statistic_id" in value:
        out["StatisticId"] = value["statistic_id"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "run_identifier" in value:
        import capo_glue.types.run_identifier

        out["RunIdentifier"] = capo_glue.types.run_identifier.serialize_aws_json_1_1(
            value["run_identifier"]
        )
    if "statistic_name" in value:
        out["StatisticName"] = value["statistic_name"]
    out["DoubleValue"] = (
        "NaN"
        if value.get("double_value", 0) != value.get("double_value", 0)
        else "Infinity"
        if value.get("double_value", 0) == float("inf")
        else "-Infinity"
        if value.get("double_value", 0) == float("-inf")
        else value.get("double_value", 0)
    )
    if "distribution_value" in value:
        import capo_glue.types.distribution_data

        out["DistributionValue"] = (
            capo_glue.types.distribution_data.serialize_aws_json_1_1(
                value["distribution_value"]
            )
        )
    if "evaluation_level" in value:
        import capo_glue.types.statistic_evaluation_level

        out["EvaluationLevel"] = (
            capo_glue.types.statistic_evaluation_level.serialize_aws_json_1_1(
                value["evaluation_level"]
            )
        )
    if "columns_referenced" in value:
        import capo_glue.types.column_name_list

        out["ColumnsReferenced"] = (
            capo_glue.types.column_name_list.serialize_aws_json_1_1(
                value["columns_referenced"]
            )
        )
    if "referenced_datasets" in value:
        import capo_glue.types.reference_datasets_list

        out["ReferencedDatasets"] = (
            capo_glue.types.reference_datasets_list.serialize_aws_json_1_1(
                value["referenced_datasets"]
            )
        )
    if "statistic_properties" in value:
        import capo_glue.types.statistic_properties_map

        out["StatisticProperties"] = (
            capo_glue.types.statistic_properties_map.serialize_aws_json_1_1(
                value["statistic_properties"]
            )
        )
    if "recorded_on" in value:
        import capo_glue.types.timestamp

        out["RecordedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["recorded_on"]
        )
    if "inclusion_annotation" in value:
        import capo_glue.types.timestamped_inclusion_annotation

        out["InclusionAnnotation"] = (
            capo_glue.types.timestamped_inclusion_annotation.serialize_aws_json_1_1(
                value["inclusion_annotation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatisticSummary:
    out: StatisticSummary = {}  # type: ignore[typeddict-item]
    if data.get("StatisticId") is not None:
        out["statistic_id"] = data["StatisticId"]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("RunIdentifier") is not None:
        import capo_glue.types.run_identifier

        out["run_identifier"] = capo_glue.types.run_identifier.deserialize_aws_json_1_1(
            data["RunIdentifier"]
        )
    if data.get("StatisticName") is not None:
        out["statistic_name"] = data["StatisticName"]
    if data.get("DoubleValue") is not None:
        out["double_value"] = float(data["DoubleValue"])
    else:
        out["double_value"] = 0
    if data.get("DistributionValue") is not None:
        import capo_glue.types.distribution_data

        out["distribution_value"] = (
            capo_glue.types.distribution_data.deserialize_aws_json_1_1(
                data["DistributionValue"]
            )
        )
    if data.get("EvaluationLevel") is not None:
        import capo_glue.types.statistic_evaluation_level

        out["evaluation_level"] = (
            capo_glue.types.statistic_evaluation_level.deserialize_aws_json_1_1(
                data["EvaluationLevel"]
            )
        )
    if data.get("ColumnsReferenced") is not None:
        import capo_glue.types.column_name_list

        out["columns_referenced"] = (
            capo_glue.types.column_name_list.deserialize_aws_json_1_1(
                data["ColumnsReferenced"]
            )
        )
    if data.get("ReferencedDatasets") is not None:
        import capo_glue.types.reference_datasets_list

        out["referenced_datasets"] = (
            capo_glue.types.reference_datasets_list.deserialize_aws_json_1_1(
                data["ReferencedDatasets"]
            )
        )
    if data.get("StatisticProperties") is not None:
        import capo_glue.types.statistic_properties_map

        out["statistic_properties"] = (
            capo_glue.types.statistic_properties_map.deserialize_aws_json_1_1(
                data["StatisticProperties"]
            )
        )
    if data.get("RecordedOn") is not None:
        import capo_glue.types.timestamp

        out["recorded_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["RecordedOn"]
        )
    if data.get("InclusionAnnotation") is not None:
        import capo_glue.types.timestamped_inclusion_annotation

        out["inclusion_annotation"] = (
            capo_glue.types.timestamped_inclusion_annotation.deserialize_aws_json_1_1(
                data["InclusionAnnotation"]
            )
        )
    return out


def redact_sensitive(value: StatisticSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "statistic_properties" in value:
        out["statistic_properties"] = "*** Sensitive Data Redacted ***"
    return out
