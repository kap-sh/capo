"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListResourcesByConnectorOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_next_token
    import capo_observabilityadmin.types.connector_query_results


class ListResourcesByConnectorOutput(TypedDict, closed=True):
    results: (
        "capo_observabilityadmin.types.connector_query_results.ConnectorQueryResults"
    )
    """<p>The results, in the same shape as the <code>Selector</code> that you specified.</p>"""
    next_token: NotRequired[
        "capo_observabilityadmin.types.connector_next_token.ConnectorNextToken"
    ]
    """<p>The token to use in the next call to get the next page of results. Absent when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesByConnectorOutput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.connector_query_results

    out["Results"] = (
        capo_observabilityadmin.types.connector_query_results.serialize_json(
            value["results"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcesByConnectorOutput:
    out: ListResourcesByConnectorOutput = {}  # type: ignore[typeddict-item]
    if data.get("Results") is not None:
        import capo_observabilityadmin.types.connector_query_results

        out["results"] = (
            capo_observabilityadmin.types.connector_query_results.deserialize_json(
                data["Results"]
            )
        )
    else:
        out["results"] = {"$unknown": {"name": ""}}
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListResourcesByConnectorOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
