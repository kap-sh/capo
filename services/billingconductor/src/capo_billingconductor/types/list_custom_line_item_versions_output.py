"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemVersionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_version_list
    import capo_billingconductor.types.token


class ListCustomLineItemVersionsOutput(TypedDict, closed=True):
    custom_line_item_versions: NotRequired[
        "capo_billingconductor.types.custom_line_item_version_list.CustomLineItemVersionList"
    ]
    """<p>A list of <code>CustomLineItemVersionListElements</code> that are received.</p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to retrieve custom line item versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemVersionsOutput) -> dict:
    out: dict = {}
    if "custom_line_item_versions" in value:
        import capo_billingconductor.types.custom_line_item_version_list

        out["CustomLineItemVersions"] = (
            capo_billingconductor.types.custom_line_item_version_list.serialize_json(
                value["custom_line_item_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomLineItemVersionsOutput:
    out: ListCustomLineItemVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("CustomLineItemVersions") is not None:
        import capo_billingconductor.types.custom_line_item_version_list

        out["custom_line_item_versions"] = (
            capo_billingconductor.types.custom_line_item_version_list.deserialize_json(
                data["CustomLineItemVersions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListCustomLineItemVersionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_line_item_versions" in value:
        import capo_billingconductor.types.custom_line_item_version_list

        out["custom_line_item_versions"] = (
            capo_billingconductor.types.custom_line_item_version_list.redact_sensitive(
                value["custom_line_item_versions"]
            )
        )
    return out
