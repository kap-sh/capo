"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditSuppressionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.audit_check_name
    import capo_iot.types.max_results
    import capo_iot.types.next_token
    import capo_iot.types.resource_identifier


class ListAuditSuppressionsRequest(TypedDict, closed=True):
    check_name: NotRequired["capo_iot.types.audit_check_name.AuditCheckName"]
    resource_identifier: NotRequired[
        "capo_iot.types.resource_identifier.ResourceIdentifier"
    ]
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p> Determines whether suppressions are listed in ascending order by expiration date or not. If parameter isn't provided, <code>ascendingOrder=true</code>. </p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p> The token for the next set of results. </p>"""
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p> The maximum number of results to return at one time. The default is 25. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditSuppressionsRequest) -> dict:
    out: dict = {}
    if "check_name" in value:
        out["checkName"] = value["check_name"]
    if "resource_identifier" in value:
        import capo_iot.types.resource_identifier

        out["resourceIdentifier"] = capo_iot.types.resource_identifier.serialize_json(
            value["resource_identifier"]
        )
    if "ascending_order" in value:
        out["ascendingOrder"] = value["ascending_order"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAuditSuppressionsRequest:
    out: ListAuditSuppressionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("checkName") is not None:
        out["check_name"] = data["checkName"]
    if data.get("resourceIdentifier") is not None:
        import capo_iot.types.resource_identifier

        out["resource_identifier"] = (
            capo_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    if data.get("ascendingOrder") is not None:
        out["ascending_order"] = data["ascendingOrder"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
