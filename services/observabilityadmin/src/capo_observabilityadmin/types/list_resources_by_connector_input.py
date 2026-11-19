"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListResourcesByConnectorInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_identifier
    import capo_observabilityadmin.types.connector_next_token
    import capo_observabilityadmin.types.connector_query
    import capo_observabilityadmin.types.list_resources_by_connector_max_results


class ListResourcesByConnectorInput(TypedDict, closed=True):
    connector_identifier: (
        "capo_observabilityadmin.types.connector_identifier.ConnectorIdentifier"
    )
    """<p>The connector to use for the query. Specify one of the following:</p> <ul> <li> <p>The Amazon Resource Name (ARN) of the connector</p> </li> <li> <p>The ID of the connector</p> </li> </ul>"""
    selector: "capo_observabilityadmin.types.connector_query.ConnectorQuery"
    """<p>What to list: one cloud provider, and one type of resource in that provider.</p>"""
    max_results: NotRequired[
        "capo_observabilityadmin.types.list_resources_by_connector_max_results.ListResourcesByConnectorMaxResults"
    ]
    """<p>The maximum number of results to return in one call. For an <code>EventHubs</code> query, a page can contain more results than this value.</p>"""
    next_token: NotRequired[
        "capo_observabilityadmin.types.connector_next_token.ConnectorNextToken"
    ]
    """<p>The token for the next page of results, returned by a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesByConnectorInput) -> dict:
    out: dict = {}
    out["ConnectorIdentifier"] = value["connector_identifier"]
    import capo_observabilityadmin.types.connector_query

    out["Selector"] = capo_observabilityadmin.types.connector_query.serialize_json(
        value["selector"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcesByConnectorInput:
    out: ListResourcesByConnectorInput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorIdentifier") is not None:
        out["connector_identifier"] = data["ConnectorIdentifier"]
    else:
        out["connector_identifier"] = ""
    if data.get("Selector") is not None:
        import capo_observabilityadmin.types.connector_query

        out["selector"] = (
            capo_observabilityadmin.types.connector_query.deserialize_json(
                data["Selector"]
            )
        )
    else:
        out["selector"] = {"$unknown": {"name": ""}}
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListResourcesByConnectorInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
