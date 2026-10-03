"""Generated from Smithy shape ``com.amazonaws.mwaa#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mwaa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa.types.environment_arn
    import capo_mwaa.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_mwaa.types.environment_arn.EnvironmentArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.</p>"""
    tags: "capo_mwaa.types.tag_map.TagMap"
    """<p>The key-value tag pairs you want to associate to your environment. For example, <code>"Environment": "Staging"</code>. For more information, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_mwaa.types.tag_map

    out["Tags"] = capo_mwaa.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_mwaa.types.tag_map

        out["tags"] = capo_mwaa.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
