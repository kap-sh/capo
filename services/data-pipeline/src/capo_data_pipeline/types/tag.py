"""Generated from Smithy shape ``com.amazonaws.datapipeline#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_data_pipeline.types.tag_key
    import capo_data_pipeline.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_data_pipeline.types.tag_key.tagKey"
    """<p>The key name of a tag defined by a user. For more information, see <a href="http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html">Controlling User Access to Pipelines</a> in the <i>AWS Data Pipeline Developer Guide</i>.</p>"""
    value: "capo_data_pipeline.types.tag_value.tagValue"
    """<p>The optional value portion of a tag defined by a user. For more information, see <a href="http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html">Controlling User Access to Pipelines</a> in the <i>AWS Data Pipeline Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
