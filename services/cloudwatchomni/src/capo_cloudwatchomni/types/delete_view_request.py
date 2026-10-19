"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.view_name


class DeleteViewRequest(TypedDict, closed=True):
    name: "capo_cloudwatchomni.types.view_name.ViewName"
    """The name of the view to delete."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteViewRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> DeleteViewRequest:
    out: DeleteViewRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
