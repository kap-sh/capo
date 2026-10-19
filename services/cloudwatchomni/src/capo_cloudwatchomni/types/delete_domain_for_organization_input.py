"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteDomainForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_id


class DeleteDomainForOrganizationInput(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The ID of the organization domain to delete."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDomainForOrganizationInput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteDomainForOrganizationInput:
    out: DeleteDomainForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    return out
