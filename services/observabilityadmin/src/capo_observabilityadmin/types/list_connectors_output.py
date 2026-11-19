"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListConnectorsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_next_token
    import capo_observabilityadmin.types.connector_summaries


class ListConnectorsOutput(TypedDict, closed=True):
    connector_summaries: (
        "capo_observabilityadmin.types.connector_summaries.ConnectorSummaries"
    )
    """<p>The connectors in the account and Region.</p>"""
    next_token: NotRequired[
        "capo_observabilityadmin.types.connector_next_token.ConnectorNextToken"
    ]
    """<p>The token to use in the next call to get the next page of results. Absent when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsOutput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.connector_summaries

    out["ConnectorSummaries"] = (
        capo_observabilityadmin.types.connector_summaries.serialize_json(
            value["connector_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorsOutput:
    out: ListConnectorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorSummaries") is not None:
        import capo_observabilityadmin.types.connector_summaries

        out["connector_summaries"] = (
            capo_observabilityadmin.types.connector_summaries.deserialize_json(
                data["ConnectorSummaries"]
            )
        )
    else:
        out["connector_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListConnectorsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
