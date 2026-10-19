"""Generated from Smithy shape ``com.amazonaws.cleanrooms#InheritedAllowedResultReceivers``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id_list
    import capo_cleanrooms.types.inherited_allowed_result_receivers_source_list


class InheritedAllowedResultReceivers(TypedDict, closed=True):
    value: "capo_cleanrooms.types.account_id_list.AccountIdList"
    """<p>The effective list of Amazon Web Services account IDs allowed to receive results, inherited from parent tables.</p>"""
    sources: "capo_cleanrooms.types.inherited_allowed_result_receivers_source_list.InheritedAllowedResultReceiversSourceList"
    """<p>The list of parent tables that contribute to this inherited constraint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InheritedAllowedResultReceivers) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.account_id_list

    out["value"] = capo_cleanrooms.types.account_id_list.serialize_json(value["value"])
    import capo_cleanrooms.types.inherited_allowed_result_receivers_source_list

    out["sources"] = (
        capo_cleanrooms.types.inherited_allowed_result_receivers_source_list.serialize_json(
            value["sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> InheritedAllowedResultReceivers:
    out: InheritedAllowedResultReceivers = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_cleanrooms.types.account_id_list

        out["value"] = capo_cleanrooms.types.account_id_list.deserialize_json(
            data["value"]
        )
    else:
        out["value"] = []
    if data.get("sources") is not None:
        import capo_cleanrooms.types.inherited_allowed_result_receivers_source_list

        out["sources"] = (
            capo_cleanrooms.types.inherited_allowed_result_receivers_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    return out
