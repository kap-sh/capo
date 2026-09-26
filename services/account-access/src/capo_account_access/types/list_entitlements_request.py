"""Generated from Smithy shape ``com.amazonaws.accountaccess#ListEntitlementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.application_arn
    import capo_account_access.types.entitlement_filter


class ListEntitlementsRequest(TypedDict, closed=True):
    application_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application to list entitlements for.</p>"""
    filter: "capo_account_access.types.entitlement_filter.EntitlementFilter"
    """<p>Specifies filter criteria to narrow the entitlements returned. You can filter by principal, IAM role, or account.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies the pagination token from a previous call to retrieve the next set of results.</p>"""
    max_results: NotRequired["int"]
    """<p>Specifies the maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitlementsRequest) -> dict:
    out: dict = {}
    out["applicationArn"] = value["application_arn"]
    import capo_account_access.types.entitlement_filter

    out["filter"] = capo_account_access.types.entitlement_filter.serialize_json(
        value["filter"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListEntitlementsRequest:
    out: ListEntitlementsRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    else:
        raise DeserializationError("ListEntitlementsRequest.application_arn required")
    if data.get("filter") is not None:
        import capo_account_access.types.entitlement_filter

        out["filter"] = capo_account_access.types.entitlement_filter.deserialize_json(
            data["filter"]
        )
    else:
        raise DeserializationError("ListEntitlementsRequest.filter required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
