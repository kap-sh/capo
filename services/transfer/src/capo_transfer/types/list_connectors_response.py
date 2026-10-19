"""Generated from Smithy shape ``com.amazonaws.transfer#ListConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.listed_connectors
    import capo_transfer.types.next_token


class ListConnectorsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>Returns a token that you can use to call <code>ListConnectors</code> again and receive additional results, if there are any.</p>"""
    connectors: "capo_transfer.types.listed_connectors.ListedConnectors"
    """<p>Returns an array, where each item contains the details of a connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConnectorsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_transfer.types.listed_connectors

    out["Connectors"] = capo_transfer.types.listed_connectors.serialize_aws_json_1_1(
        value["connectors"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConnectorsResponse:
    out: ListConnectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Connectors") is not None:
        import capo_transfer.types.listed_connectors

        out["connectors"] = (
            capo_transfer.types.listed_connectors.deserialize_aws_json_1_1(
                data["Connectors"]
            )
        )
    else:
        out["connectors"] = []
    return out
