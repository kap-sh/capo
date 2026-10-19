"""Generated from Smithy shape ``com.amazonaws.notifications#ListOrganizationalUnitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.next_token
    import capo_notifications.types.organizational_units


class ListOrganizationalUnitsResponse(TypedDict, closed=True):
    organizational_units: (
        "capo_notifications.types.organizational_units.OrganizationalUnits"
    )
    """<p>The list of organizational units that match the specified criteria.</p>"""
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>The token to use for the next page of results. If there are no additional results, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationalUnitsResponse) -> dict:
    out: dict = {}
    import capo_notifications.types.organizational_units

    out["organizationalUnits"] = (
        capo_notifications.types.organizational_units.serialize_json(
            value["organizational_units"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrganizationalUnitsResponse:
    out: ListOrganizationalUnitsResponse = {}  # type: ignore[typeddict-item]
    if data.get("organizationalUnits") is not None:
        import capo_notifications.types.organizational_units

        out["organizational_units"] = (
            capo_notifications.types.organizational_units.deserialize_json(
                data["organizationalUnits"]
            )
        )
    else:
        out["organizational_units"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
