"""Generated from Smithy shape ``com.amazonaws.rtbfabric#Action``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError, SerializationError
from capo_rtbfabric.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_rtbfabric.types.header_tag_action
    import capo_rtbfabric.types.no_bid_action


class _Action_noBid(TypedDict, closed=True):
    noBid: "capo_rtbfabric.types.no_bid_action.NoBidAction"


class _Action_headerTag(TypedDict, closed=True):
    headerTag: "capo_rtbfabric.types.header_tag_action.HeaderTagAction"


Action: TypeAlias = _Action_noBid | _Action_headerTag | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Action: cannot serialize unknown variant {value.name!r}"
        )
    elif "noBid" in value:
        import capo_rtbfabric.types.no_bid_action

        return {
            "noBid": capo_rtbfabric.types.no_bid_action.serialize_json(value["noBid"])
        }
    elif "headerTag" in value:
        import capo_rtbfabric.types.header_tag_action

        return {
            "headerTag": capo_rtbfabric.types.header_tag_action.serialize_json(
                value["headerTag"]
            )
        }
    else:
        raise SerializationError("Action: no variant present")


def deserialize_json(data: dict) -> Action:
    if data.get("noBid") is not None:
        import capo_rtbfabric.types.no_bid_action

        return {
            "noBid": capo_rtbfabric.types.no_bid_action.deserialize_json(data["noBid"])
        }
    elif data.get("headerTag") is not None:
        import capo_rtbfabric.types.header_tag_action

        return {
            "headerTag": capo_rtbfabric.types.header_tag_action.deserialize_json(
                data["headerTag"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Action: no recognized variant key")
