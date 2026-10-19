"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateModelVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.external_events_detail
    import capo_frauddetector.types.ingested_events_detail
    import capo_frauddetector.types.model_identifier
    import capo_frauddetector.types.model_type_enum
    import capo_frauddetector.types.tag_list
    import capo_frauddetector.types.training_data_schema
    import capo_frauddetector.types.training_data_source_enum


class CreateModelVersionRequest(TypedDict, closed=True):
    model_id: "capo_frauddetector.types.model_identifier.modelIdentifier"
    """<p>The model ID. </p>"""
    model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum"
    """<p>The model type.</p>"""
    training_data_source: (
        "capo_frauddetector.types.training_data_source_enum.TrainingDataSourceEnum"
    )
    """<p>The training data source location in Amazon S3. </p>"""
    training_data_schema: (
        "capo_frauddetector.types.training_data_schema.TrainingDataSchema"
    )
    """<p>The training data schema.</p>"""
    external_events_detail: NotRequired[
        "capo_frauddetector.types.external_events_detail.ExternalEventsDetail"
    ]
    """<p>Details of the external events data used for model version training. Required if <code>trainingDataSource</code> is <code>EXTERNAL_EVENTS</code>.</p>"""
    ingested_events_detail: NotRequired[
        "capo_frauddetector.types.ingested_events_detail.IngestedEventsDetail"
    ]
    """<p>Details of the ingested events data used for model version training. Required if <code>trainingDataSource</code> is <code>INGESTED_EVENTS</code>.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelVersionRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import capo_frauddetector.types.model_type_enum

    out["modelType"] = capo_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
        value["model_type"]
    )
    import capo_frauddetector.types.training_data_source_enum

    out["trainingDataSource"] = (
        capo_frauddetector.types.training_data_source_enum.serialize_aws_json_1_1(
            value["training_data_source"]
        )
    )
    import capo_frauddetector.types.training_data_schema

    out["trainingDataSchema"] = (
        capo_frauddetector.types.training_data_schema.serialize_aws_json_1_1(
            value["training_data_schema"]
        )
    )
    if "external_events_detail" in value:
        import capo_frauddetector.types.external_events_detail

        out["externalEventsDetail"] = (
            capo_frauddetector.types.external_events_detail.serialize_aws_json_1_1(
                value["external_events_detail"]
            )
        )
    if "ingested_events_detail" in value:
        import capo_frauddetector.types.ingested_events_detail

        out["ingestedEventsDetail"] = (
            capo_frauddetector.types.ingested_events_detail.serialize_aws_json_1_1(
                value["ingested_events_detail"]
            )
        )
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelVersionRequest:
    out: CreateModelVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("modelType") is not None:
        import capo_frauddetector.types.model_type_enum

        out["model_type"] = (
            capo_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    else:
        import typing

        out["model_type"] = typing.cast(
            "capo_frauddetector.types.model_type_enum.ModelTypeEnum", ""
        )
    if data.get("trainingDataSource") is not None:
        import capo_frauddetector.types.training_data_source_enum

        out["training_data_source"] = (
            capo_frauddetector.types.training_data_source_enum.deserialize_aws_json_1_1(
                data["trainingDataSource"]
            )
        )
    else:
        import typing

        out["training_data_source"] = typing.cast(
            "capo_frauddetector.types.training_data_source_enum.TrainingDataSourceEnum",
            "",
        )
    if data.get("trainingDataSchema") is not None:
        import capo_frauddetector.types.training_data_schema

        out["training_data_schema"] = (
            capo_frauddetector.types.training_data_schema.deserialize_aws_json_1_1(
                data["trainingDataSchema"]
            )
        )
    else:
        raise DeserializationError(
            "CreateModelVersionRequest.training_data_schema required"
        )
    if data.get("externalEventsDetail") is not None:
        import capo_frauddetector.types.external_events_detail

        out["external_events_detail"] = (
            capo_frauddetector.types.external_events_detail.deserialize_aws_json_1_1(
                data["externalEventsDetail"]
            )
        )
    if data.get("ingestedEventsDetail") is not None:
        import capo_frauddetector.types.ingested_events_detail

        out["ingested_events_detail"] = (
            capo_frauddetector.types.ingested_events_detail.deserialize_aws_json_1_1(
                data["ingestedEventsDetail"]
            )
        )
    if data.get("tags") is not None:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
