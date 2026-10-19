"""Generated from Smithy shape ``com.amazonaws.accountaccess#EntitlementsListMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_account_access.types.date_time
    import capo_account_access.types.entitlement_summary


class EntitlementsListMember(TypedDict, closed=True):
    entitlement_id: "str"
    """<p>The unique identifier of the entitlement.</p>"""
    entitlement: "capo_account_access.types.entitlement_summary.EntitlementSummary"
    """<p>The summary information for the entitlement.</p>"""
    created_at: "capo_account_access.types.date_time.DateTime"
    """<p>The date and time when the entitlement was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntitlementsListMember) -> dict:
    out: dict = {}
    out["entitlementId"] = value["entitlement_id"]
    import capo_account_access.types.entitlement_summary

    out["entitlement"] = capo_account_access.types.entitlement_summary.serialize_json(
        value["entitlement"]
    )
    import capo_account_access.types.date_time

    out["createdAt"] = capo_account_access.types.date_time.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> EntitlementsListMember:
    out: EntitlementsListMember = {}  # type: ignore[typeddict-item]
    if data.get("entitlementId") is not None:
        out["entitlement_id"] = data["entitlementId"]
    else:
        out["entitlement_id"] = ""
    if data.get("entitlement") is not None:
        import capo_account_access.types.entitlement_summary

        out["entitlement"] = (
            capo_account_access.types.entitlement_summary.deserialize_json(
                data["entitlement"]
            )
        )
    else:
        import capo_account_access.types._unknown

        out["entitlement"] = capo_account_access.types._unknown.UnknownUnionMember("")
    if data.get("createdAt") is not None:
        import capo_account_access.types.date_time

        out["created_at"] = capo_account_access.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
