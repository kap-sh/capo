"""Generated from Smithy shape ``com.amazonaws.osis#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline_arn
    import capo_osis.types.string_list


class UntagResourceRequest(TypedDict, closed=True):
    arn: "capo_osis.types.pipeline_arn.PipelineArn"
    """<p>The Amazon Resource Name (ARN) of the pipeline to remove tags from.</p>"""
    tag_keys: "capo_osis.types.string_list.StringList"
    """<p>The tag keys to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    import capo_osis.types.string_list

    out["TagKeys"] = capo_osis.types.string_list.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("TagKeys") is not None:
        import capo_osis.types.string_list

        out["tag_keys"] = capo_osis.types.string_list.deserialize_json(data["TagKeys"])
    else:
        out["tag_keys"] = []
    return out
