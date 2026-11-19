"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemsConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class RelatedItemsConfiguration(TypedDict, closed=True):
    comment: NotRequired["bool"]
    """<p>Whether to move Comment related items to the primary case.</p>"""
    connect_case: NotRequired["bool"]
    """<p>Whether to move Case related items to the primary case. If the primary case already links to the same case, the secondary case's link is removed instead of moved.</p>"""
    contact: NotRequired["bool"]
    """<p>Whether to move Contact related items to the primary case. If the same contact is related to both cases, the primary case keeps its related item and gets any tag keys that only the secondary case's related item has.</p>"""
    custom: NotRequired["bool"]
    """<p>Whether to move Custom related items to the primary case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemsConfiguration) -> dict:
    out: dict = {}
    if "comment" in value:
        out["comment"] = value["comment"]
    if "connect_case" in value:
        out["connectCase"] = value["connect_case"]
    if "contact" in value:
        out["contact"] = value["contact"]
    if "custom" in value:
        out["custom"] = value["custom"]
    return out


def deserialize_json(data: dict) -> RelatedItemsConfiguration:
    out: RelatedItemsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("connectCase") is not None:
        out["connect_case"] = data["connectCase"]
    if data.get("contact") is not None:
        out["contact"] = data["contact"]
    if data.get("custom") is not None:
        out["custom"] = data["custom"]
    return out
