"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_license_manager_user_subscriptions.types.tags.Tags"]
    """<p>The tags for the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_license_manager_user_subscriptions.types.tags

        out["Tags"] = capo_license_manager_user_subscriptions.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_license_manager_user_subscriptions.types.tags

        out["tags"] = (
            capo_license_manager_user_subscriptions.types.tags.deserialize_json(
                data["Tags"]
            )
        )
    return out


def redact_sensitive(value: ListTagsForResourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
