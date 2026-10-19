"""Generated from Smithy shape ``com.amazonaws.evs#ListVmEntitlementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.connector_id
    import capo_evs.types.entitlement_type
    import capo_evs.types.environment_id
    import capo_evs.types.max_results
    import capo_evs.types.pagination_token


class ListVmEntitlementsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""
    max_results: NotRequired["capo_evs.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>"""
    environment_id: "capo_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment.</p>"""
    connector_id: "capo_evs.types.connector_id.ConnectorId"
    """<p>A unique ID for the connector.</p>"""
    entitlement_type: "capo_evs.types.entitlement_type.EntitlementType"
    """<p>The type of entitlement to list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVmEntitlementsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    out["environmentId"] = value["environment_id"]
    out["connectorId"] = value["connector_id"]
    import capo_evs.types.entitlement_type

    out["entitlementType"] = capo_evs.types.entitlement_type.serialize_aws_json_1_0(
        value["entitlement_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVmEntitlementsRequest:
    out: ListVmEntitlementsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("connectorId") is not None:
        out["connector_id"] = data["connectorId"]
    else:
        out["connector_id"] = ""
    if data.get("entitlementType") is not None:
        import capo_evs.types.entitlement_type

        out["entitlement_type"] = (
            capo_evs.types.entitlement_type.deserialize_aws_json_1_0(
                data["entitlementType"]
            )
        )
    else:
        import typing

        out["entitlement_type"] = typing.cast(
            "capo_evs.types.entitlement_type.EntitlementType", ""
        )
    return out
