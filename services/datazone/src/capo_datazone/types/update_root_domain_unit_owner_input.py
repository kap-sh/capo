"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateRootDomainUnitOwnerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.user_identifier


class UpdateRootDomainUnitOwnerInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the root domain unit owner is to be updated.</p>"""
    current_owner: "capo_datazone.types.user_identifier.UserIdentifier"
    """<p>The current owner of the root domain unit.</p>"""
    new_owner: "str"
    """<p>The new owner of the root domain unit.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRootDomainUnitOwnerInput) -> dict:
    out: dict = {}
    out["currentOwner"] = value["current_owner"]
    out["newOwner"] = value["new_owner"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateRootDomainUnitOwnerInput:
    out: UpdateRootDomainUnitOwnerInput = {}  # type: ignore[typeddict-item]
    if data.get("currentOwner") is not None:
        out["current_owner"] = data["currentOwner"]
    else:
        out["current_owner"] = ""
    if data.get("newOwner") is not None:
        out["new_owner"] = data["newOwner"]
    else:
        out["new_owner"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
