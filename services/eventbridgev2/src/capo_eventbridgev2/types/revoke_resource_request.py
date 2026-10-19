"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#RevokeResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.revocable_resource_arn


class RevokeResourceRequest(TypedDict, closed=True):
    arn: "capo_eventbridgev2.types.revocable_resource_arn.RevocableResourceArn"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevokeResourceRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> RevokeResourceRequest:
    out: RevokeResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
