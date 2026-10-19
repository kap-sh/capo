"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetDomainAccessGrantForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.grant_id


class GetDomainAccessGrantForOrganizationInput(TypedDict, closed=True):
    grant_id: "capo_cloudwatchomni.types.grant_id.GrantId"
    """The ID of the access grant to retrieve."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDomainAccessGrantForOrganizationInput) -> dict:
    out: dict = {}
    out["grantId"] = value["grant_id"]
    return out


def deserialize_cbor(data: dict) -> GetDomainAccessGrantForOrganizationInput:
    out: GetDomainAccessGrantForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("grantId") is not None:
        out["grant_id"] = data["grantId"]
    else:
        out["grant_id"] = ""
    return out
