"""Generated from Smithy shape ``com.amazonaws.groundstation#AggregateStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.agent_status
    import capo_groundstation.types.signature_map


class AggregateStatus(TypedDict, closed=True):
    status: "capo_groundstation.types.agent_status.AgentStatus"
    """<p>Aggregate status.</p>"""
    signature_map: NotRequired["capo_groundstation.types.signature_map.SignatureMap"]
    """<p>Sparse map of failure signatures.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregateStatus) -> dict:
    out: dict = {}
    import capo_groundstation.types.agent_status

    out["status"] = capo_groundstation.types.agent_status.serialize_json(
        value["status"]
    )
    if "signature_map" in value:
        import capo_groundstation.types.signature_map

        out["signatureMap"] = capo_groundstation.types.signature_map.serialize_json(
            value["signature_map"]
        )
    return out


def deserialize_json(data: dict) -> AggregateStatus:
    out: AggregateStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_groundstation.types.agent_status

        out["status"] = capo_groundstation.types.agent_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_groundstation.types.agent_status.AgentStatus", ""
        )
    if data.get("signatureMap") is not None:
        import capo_groundstation.types.signature_map

        out["signature_map"] = capo_groundstation.types.signature_map.deserialize_json(
            data["signatureMap"]
        )
    return out
