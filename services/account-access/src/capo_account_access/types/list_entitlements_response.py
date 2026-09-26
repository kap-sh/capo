"""Generated from Smithy shape ``com.amazonaws.accountaccess#ListEntitlementsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.entitlements_list


class ListEntitlementsResponse(TypedDict, closed=True):
    entitlements: "capo_account_access.types.entitlements_list.EntitlementsList"
    """<p>The list of entitlements for the specified application.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token to use in a subsequent request to retrieve the next set of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitlementsResponse) -> dict:
    out: dict = {}
    import capo_account_access.types.entitlements_list

    out["entitlements"] = capo_account_access.types.entitlements_list.serialize_json(
        value["entitlements"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntitlementsResponse:
    out: ListEntitlementsResponse = {}  # type: ignore[typeddict-item]
    if data.get("entitlements") is not None:
        import capo_account_access.types.entitlements_list

        out["entitlements"] = (
            capo_account_access.types.entitlements_list.deserialize_json(
                data["entitlements"]
            )
        )
    else:
        raise DeserializationError("ListEntitlementsResponse.entitlements required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
