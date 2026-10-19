"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessGrantPrincipalAttribute``."""

from typing_extensions import TypedDict


class AccessGrantPrincipalAttribute(TypedDict, closed=True):
    key: "str"
    """The Identity Center user attribute to match on. One of userName, active, userStatus, displayName, email, name.givenName, name.familyName, enterprise.department, enterprise.division, enterprise.organization, enterprise.costCenter, or enterprise.employeeNumber. Each key may appear only once per grant."""
    value: "str"
    """The attribute value."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessGrantPrincipalAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> AccessGrantPrincipalAttribute:
    out: AccessGrantPrincipalAttribute = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
