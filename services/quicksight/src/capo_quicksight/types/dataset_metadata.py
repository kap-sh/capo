"""Generated from Smithy shape ``com.amazonaws.quicksight#DatasetMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.data_aggregation
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.topic_calculated_fields
    import capo_quicksight.types.topic_columns
    import capo_quicksight.types.topic_filters
    import capo_quicksight.types.topic_named_entities


class DatasetMetadata(TypedDict, closed=True):
    dataset_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    dataset_name: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The name of the dataset.</p>"""
    dataset_description: NotRequired[
        "capo_quicksight.types.limited_string.LimitedString"
    ]
    """<p>The description of the dataset.</p>"""
    data_aggregation: NotRequired[
        "capo_quicksight.types.data_aggregation.DataAggregation"
    ]
    """<p>The definition of a data aggregation.</p>"""
    filters: NotRequired["capo_quicksight.types.topic_filters.TopicFilters"]
    """<p>The list of filter definitions.</p>"""
    columns: NotRequired["capo_quicksight.types.topic_columns.TopicColumns"]
    """<p>The list of column definitions.</p>"""
    calculated_fields: NotRequired[
        "capo_quicksight.types.topic_calculated_fields.TopicCalculatedFields"
    ]
    """<p>The list of calculated field definitions.</p>"""
    named_entities: NotRequired[
        "capo_quicksight.types.topic_named_entities.TopicNamedEntities"
    ]
    """<p>The list of named entities definitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetMetadata) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_description" in value:
        out["DatasetDescription"] = value["dataset_description"]
    if "data_aggregation" in value:
        import capo_quicksight.types.data_aggregation

        out["DataAggregation"] = capo_quicksight.types.data_aggregation.serialize_json(
            value["data_aggregation"]
        )
    if "filters" in value:
        import capo_quicksight.types.topic_filters

        out["Filters"] = capo_quicksight.types.topic_filters.serialize_json(
            value["filters"]
        )
    if "columns" in value:
        import capo_quicksight.types.topic_columns

        out["Columns"] = capo_quicksight.types.topic_columns.serialize_json(
            value["columns"]
        )
    if "calculated_fields" in value:
        import capo_quicksight.types.topic_calculated_fields

        out["CalculatedFields"] = (
            capo_quicksight.types.topic_calculated_fields.serialize_json(
                value["calculated_fields"]
            )
        )
    if "named_entities" in value:
        import capo_quicksight.types.topic_named_entities

        out["NamedEntities"] = (
            capo_quicksight.types.topic_named_entities.serialize_json(
                value["named_entities"]
            )
        )
    return out


def deserialize_json(data: dict) -> DatasetMetadata:
    out: DatasetMetadata = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("DatasetMetadata.dataset_arn required")
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("DatasetDescription") is not None:
        out["dataset_description"] = data["DatasetDescription"]
    if data.get("DataAggregation") is not None:
        import capo_quicksight.types.data_aggregation

        out["data_aggregation"] = (
            capo_quicksight.types.data_aggregation.deserialize_json(
                data["DataAggregation"]
            )
        )
    if data.get("Filters") is not None:
        import capo_quicksight.types.topic_filters

        out["filters"] = capo_quicksight.types.topic_filters.deserialize_json(
            data["Filters"]
        )
    if data.get("Columns") is not None:
        import capo_quicksight.types.topic_columns

        out["columns"] = capo_quicksight.types.topic_columns.deserialize_json(
            data["Columns"]
        )
    if data.get("CalculatedFields") is not None:
        import capo_quicksight.types.topic_calculated_fields

        out["calculated_fields"] = (
            capo_quicksight.types.topic_calculated_fields.deserialize_json(
                data["CalculatedFields"]
            )
        )
    if data.get("NamedEntities") is not None:
        import capo_quicksight.types.topic_named_entities

        out["named_entities"] = (
            capo_quicksight.types.topic_named_entities.deserialize_json(
                data["NamedEntities"]
            )
        )
    return out


def redact_sensitive(value: DatasetMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_quicksight.types.topic_filters

        out["filters"] = capo_quicksight.types.topic_filters.redact_sensitive(
            value["filters"]
        )
    if "columns" in value:
        import capo_quicksight.types.topic_columns

        out["columns"] = capo_quicksight.types.topic_columns.redact_sensitive(
            value["columns"]
        )
    if "calculated_fields" in value:
        import capo_quicksight.types.topic_calculated_fields

        out["calculated_fields"] = (
            capo_quicksight.types.topic_calculated_fields.redact_sensitive(
                value["calculated_fields"]
            )
        )
    if "named_entities" in value:
        import capo_quicksight.types.topic_named_entities

        out["named_entities"] = (
            capo_quicksight.types.topic_named_entities.redact_sensitive(
                value["named_entities"]
            )
        )
    return out
