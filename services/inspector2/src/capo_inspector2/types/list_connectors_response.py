"""Generated from Smithy shape ``com.amazonaws.inspector2#ListConnectorsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.connector_list
    import capo_inspector2.types.connector_next_token


class ListConnectorsResponse(TypedDict, closed=True):
    items: "capo_inspector2.types.connector_list.ConnectorList"
    """<p>A list of connectors.</p>"""
    next_token: NotRequired[
        "capo_inspector2.types.connector_next_token.ConnectorNextToken"
    ]
    """<p>A pagination token. If this value is not null, there are additional results available. Use this token in the <code>nextToken</code> parameter of a subsequent request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.connector_list

    out["items"] = capo_inspector2.types.connector_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorsResponse:
    out: ListConnectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_inspector2.types.connector_list

        out["items"] = capo_inspector2.types.connector_list.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListConnectorsResponse.items required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListConnectorsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
