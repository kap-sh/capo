"""Generated from Smithy shape ``com.amazonaws.personalize#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>The resource's tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out


def redact_sensitive(value: ListTagsForResourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.redact_sensitive(value["tags"])
    return out
