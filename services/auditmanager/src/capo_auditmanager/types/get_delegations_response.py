"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetDelegationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.delegation_metadata_list
    import capo_auditmanager.types.token


class GetDelegationsResponse(TypedDict, closed=True):
    delegations: NotRequired[
        "capo_auditmanager.types.delegation_metadata_list.DelegationMetadataList"
    ]
    """<p> The list of delegations that the <code>GetDelegations</code> API returned. </p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDelegationsResponse) -> dict:
    out: dict = {}
    if "delegations" in value:
        import capo_auditmanager.types.delegation_metadata_list

        out["delegations"] = (
            capo_auditmanager.types.delegation_metadata_list.serialize_json(
                value["delegations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDelegationsResponse:
    out: GetDelegationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("delegations") is not None:
        import capo_auditmanager.types.delegation_metadata_list

        out["delegations"] = (
            capo_auditmanager.types.delegation_metadata_list.deserialize_json(
                data["delegations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: GetDelegationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "delegations" in value:
        import capo_auditmanager.types.delegation_metadata_list

        out["delegations"] = (
            capo_auditmanager.types.delegation_metadata_list.redact_sensitive(
                value["delegations"]
            )
        )
    return out
