"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.view_name


class GetViewRequest(TypedDict, closed=True):
    name: "capo_cloudwatchomni.types.view_name.ViewName"
    """The name of the view."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetViewRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> GetViewRequest:
    out: GetViewRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
