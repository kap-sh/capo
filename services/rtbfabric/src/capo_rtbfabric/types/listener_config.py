"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ListenerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.protocol_list


class ListenerConfig(TypedDict, closed=True):
    protocols: "capo_rtbfabric.types.protocol_list.ProtocolList"
    """<p>The protocol for connections from clients to the gateway</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerConfig) -> dict:
    out: dict = {}
    import capo_rtbfabric.types.protocol_list

    out["protocols"] = capo_rtbfabric.types.protocol_list.serialize_json(
        value["protocols"]
    )
    return out


def deserialize_json(data: dict) -> ListenerConfig:
    out: ListenerConfig = {}  # type: ignore[typeddict-item]
    if data.get("protocols") is not None:
        import capo_rtbfabric.types.protocol_list

        out["protocols"] = capo_rtbfabric.types.protocol_list.deserialize_json(
            data["protocols"]
        )
    else:
        out["protocols"] = []
    return out
