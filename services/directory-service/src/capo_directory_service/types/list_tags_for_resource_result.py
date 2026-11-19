"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.next_token
    import capo_directory_service.types.tags


class ListTagsForResourceResult(TypedDict, closed=True):
    tags: NotRequired["capo_directory_service.types.tags.Tags"]
    """<p>List of tags returned by the ListTagsForResource operation.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_directory_service.types.tags

        out["Tags"] = capo_directory_service.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_directory_service.types.tags

        out["tags"] = capo_directory_service.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_directory_service.types.tags

        out["Tags"] = capo_directory_service.types.tags.serialize_cbor(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_directory_service.types.tags

        out["tags"] = capo_directory_service.types.tags.deserialize_cbor(data["Tags"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
