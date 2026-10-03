"""Generated from Smithy shape ``com.amazonaws.appflow#S3OutputFormatConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.aggregation_config
    import capo_appflow.types.file_type
    import capo_appflow.types.java_boolean
    import capo_appflow.types.prefix_config


class S3OutputFormatConfig(TypedDict, closed=True):
    file_type: NotRequired["capo_appflow.types.file_type.FileType"]
    """<p> Indicates the file type that Amazon AppFlow places in the Amazon S3 bucket. </p>"""
    prefix_config: NotRequired["capo_appflow.types.prefix_config.PrefixConfig"]
    """<p> Determines the prefix that Amazon AppFlow applies to the folder name in the Amazon S3 bucket. You can name folders according to the flow frequency and date. </p>"""
    aggregation_config: NotRequired[
        "capo_appflow.types.aggregation_config.AggregationConfig"
    ]
    preserve_source_data_typing: NotRequired[
        "capo_appflow.types.java_boolean.JavaBoolean"
    ]
    """<p>If your file output format is Parquet, use this parameter to set whether Amazon AppFlow preserves the data types in your source data when it writes the output to Amazon S3. </p> <ul> <li> <p> <code>true</code>: Amazon AppFlow preserves the data types when it writes to Amazon S3. For example, an integer or <code>1</code> in your source data is still an integer in your output.</p> </li> <li> <p> <code>false</code>: Amazon AppFlow converts all of the source data into strings when it writes to Amazon S3. For example, an integer of <code>1</code> in your source data becomes the string <code>"1"</code> in the output.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3OutputFormatConfig) -> dict:
    out: dict = {}
    if "file_type" in value:
        import capo_appflow.types.file_type

        out["fileType"] = capo_appflow.types.file_type.serialize_json(
            value["file_type"]
        )
    if "prefix_config" in value:
        import capo_appflow.types.prefix_config

        out["prefixConfig"] = capo_appflow.types.prefix_config.serialize_json(
            value["prefix_config"]
        )
    if "aggregation_config" in value:
        import capo_appflow.types.aggregation_config

        out["aggregationConfig"] = capo_appflow.types.aggregation_config.serialize_json(
            value["aggregation_config"]
        )
    if "preserve_source_data_typing" in value:
        out["preserveSourceDataTyping"] = value["preserve_source_data_typing"]
    return out


def deserialize_json(data: dict) -> S3OutputFormatConfig:
    out: S3OutputFormatConfig = {}  # type: ignore[typeddict-item]
    if data.get("fileType") is not None:
        import capo_appflow.types.file_type

        out["file_type"] = capo_appflow.types.file_type.deserialize_json(
            data["fileType"]
        )
    if data.get("prefixConfig") is not None:
        import capo_appflow.types.prefix_config

        out["prefix_config"] = capo_appflow.types.prefix_config.deserialize_json(
            data["prefixConfig"]
        )
    if data.get("aggregationConfig") is not None:
        import capo_appflow.types.aggregation_config

        out["aggregation_config"] = (
            capo_appflow.types.aggregation_config.deserialize_json(
                data["aggregationConfig"]
            )
        )
    if data.get("preserveSourceDataTyping") is not None:
        out["preserve_source_data_typing"] = data["preserveSourceDataTyping"]
    return out
