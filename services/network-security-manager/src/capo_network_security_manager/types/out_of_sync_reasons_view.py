"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#OutOfSyncReasonsView``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_network_security_manager.types.not_visible_marker
    import capo_network_security_manager.types.out_of_sync_reasons


class _OutOfSyncReasonsView_reasons(TypedDict, closed=True):
    reasons: "capo_network_security_manager.types.out_of_sync_reasons.OutOfSyncReasons"


class _OutOfSyncReasonsView_notVisible(TypedDict, closed=True):
    notVisible: (
        "capo_network_security_manager.types.not_visible_marker.NotVisibleMarker"
    )


OutOfSyncReasonsView: TypeAlias = (
    _OutOfSyncReasonsView_reasons | _OutOfSyncReasonsView_notVisible
)


# --- restJson1 ser/de ---
def serialize_json(value: OutOfSyncReasonsView) -> dict:
    if "reasons" in value:
        import capo_network_security_manager.types.out_of_sync_reasons

        return {
            "reasons": capo_network_security_manager.types.out_of_sync_reasons.serialize_json(
                value["reasons"]
            )
        }
    elif "notVisible" in value:
        import capo_network_security_manager.types.not_visible_marker

        return {
            "notVisible": capo_network_security_manager.types.not_visible_marker.serialize_json(
                value["notVisible"]
            )
        }
    else:
        raise SerializationError("OutOfSyncReasonsView: no variant present")


def deserialize_json(data: dict) -> OutOfSyncReasonsView:
    if data.get("reasons") is not None:
        import capo_network_security_manager.types.out_of_sync_reasons

        return {
            "reasons": capo_network_security_manager.types.out_of_sync_reasons.deserialize_json(
                data["reasons"]
            )
        }
    elif data.get("notVisible") is not None:
        import capo_network_security_manager.types.not_visible_marker

        return {
            "notVisible": capo_network_security_manager.types.not_visible_marker.deserialize_json(
                data["notVisible"]
            )
        }
    else:
        raise DeserializationError("OutOfSyncReasonsView: no recognized variant key")
