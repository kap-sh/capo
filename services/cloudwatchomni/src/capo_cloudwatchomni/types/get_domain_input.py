"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_id


class GetDomainInput(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The unique ID of the domain."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDomainInput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    return out


def deserialize_cbor(data: dict) -> GetDomainInput:
    out: GetDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    return out
