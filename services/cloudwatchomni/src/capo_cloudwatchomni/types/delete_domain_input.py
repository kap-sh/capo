"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_id


class DeleteDomainInput(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The unique ID of the domain to delete."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDomainInput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteDomainInput:
    out: DeleteDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    return out
