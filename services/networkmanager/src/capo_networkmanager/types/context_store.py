"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextStore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.context_store_arn
    import capo_networkmanager.types.context_store_id
    import capo_networkmanager.types.context_store_state
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.tag_list


class ContextStore(TypedDict, closed=True):
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network that the context store belongs to.</p>"""
    context_store_id: NotRequired[
        "capo_networkmanager.types.context_store_id.ContextStoreId"
    ]
    """<p>The ID of the context store.</p>"""
    context_store_arn: NotRequired[
        "capo_networkmanager.types.context_store_arn.ContextStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the context store.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of the context store.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the context store was created.</p>"""
    state: NotRequired[
        "capo_networkmanager.types.context_store_state.ContextStoreState"
    ]
    """<p>The state of the context store. The possible values are the following:</p> <ul> <li> <p> <code>PENDING</code>: The context store is being created.</p> </li> <li> <p> <code>AVAILABLE</code>: The context store is ready to use.</p> </li> <li> <p> <code>UPDATING</code>: The context store is being updated.</p> </li> <li> <p> <code>DELETING</code>: The context store is being deleted.</p> </li> <li> <p> <code>DELETED</code>: The context store is deleted.</p> </li> </ul>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags associated with the context store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextStore) -> dict:
    out: dict = {}
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "context_store_id" in value:
        out["ContextStoreId"] = value["context_store_id"]
    if "context_store_arn" in value:
        out["ContextStoreArn"] = value["context_store_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import capo_networkmanager.types.context_store_state

        out["State"] = capo_networkmanager.types.context_store_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ContextStore:
    out: ContextStore = {}  # type: ignore[typeddict-item]
    if data.get("GlobalNetworkId") is not None:
        out["global_network_id"] = data["GlobalNetworkId"]
    if data.get("ContextStoreId") is not None:
        out["context_store_id"] = data["ContextStoreId"]
    if data.get("ContextStoreArn") is not None:
        out["context_store_arn"] = data["ContextStoreArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("State") is not None:
        import capo_networkmanager.types.context_store_state

        out["state"] = capo_networkmanager.types.context_store_state.deserialize_json(
            data["State"]
        )
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out
