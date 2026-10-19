"""Generated from Smithy shape ``com.amazonaws.glue#DirectKafkaSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.boxed_positive_int
    import capo_glue.types.kafka_streaming_source_options
    import capo_glue.types.node_name
    import capo_glue.types.streaming_data_preview_options


class DirectKafkaSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data store.</p>"""
    streaming_options: NotRequired[
        "capo_glue.types.kafka_streaming_source_options.KafkaStreamingSourceOptions"
    ]
    """<p>Specifies the streaming options.</p>"""
    window_size: NotRequired["capo_glue.types.boxed_positive_int.BoxedPositiveInt"]
    """<p>The amount of time to spend processing each micro batch.</p>"""
    detect_schema: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Whether to automatically determine the schema from the incoming data.</p>"""
    data_preview_options: NotRequired[
        "capo_glue.types.streaming_data_preview_options.StreamingDataPreviewOptions"
    ]
    """<p>Specifies options related to data preview for viewing a sample of your data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectKafkaSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "streaming_options" in value:
        import capo_glue.types.kafka_streaming_source_options

        out["StreamingOptions"] = (
            capo_glue.types.kafka_streaming_source_options.serialize_aws_json_1_1(
                value["streaming_options"]
            )
        )
    if "window_size" in value:
        out["WindowSize"] = value["window_size"]
    if "detect_schema" in value:
        out["DetectSchema"] = value["detect_schema"]
    if "data_preview_options" in value:
        import capo_glue.types.streaming_data_preview_options

        out["DataPreviewOptions"] = (
            capo_glue.types.streaming_data_preview_options.serialize_aws_json_1_1(
                value["data_preview_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectKafkaSource:
    out: DirectKafkaSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("StreamingOptions") is not None:
        import capo_glue.types.kafka_streaming_source_options

        out["streaming_options"] = (
            capo_glue.types.kafka_streaming_source_options.deserialize_aws_json_1_1(
                data["StreamingOptions"]
            )
        )
    if data.get("WindowSize") is not None:
        out["window_size"] = data["WindowSize"]
    if data.get("DetectSchema") is not None:
        out["detect_schema"] = data["DetectSchema"]
    if data.get("DataPreviewOptions") is not None:
        import capo_glue.types.streaming_data_preview_options

        out["data_preview_options"] = (
            capo_glue.types.streaming_data_preview_options.deserialize_aws_json_1_1(
                data["DataPreviewOptions"]
            )
        )
    return out
