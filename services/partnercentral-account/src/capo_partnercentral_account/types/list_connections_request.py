"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.connection_type_filter
    import capo_partnercentral_account.types.max_results
    import capo_partnercentral_account.types.next_token
    import capo_partnercentral_account.types.participant_identifier_list


class ListConnectionsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    next_token: NotRequired["capo_partnercentral_account.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results in paginated responses.</p>"""
    connection_type: NotRequired[
        "capo_partnercentral_account.types.connection_type_filter.ConnectionTypeFilter"
    ]
    """<p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>"""
    max_results: NotRequired["capo_partnercentral_account.types.max_results.MaxResults"]
    """<p>The maximum number of connections to return in a single response.</p>"""
    other_participant_identifiers: NotRequired[
        "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
    ]
    """<p>Filter results by specific participant identifiers.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "connection_type" in value:
        out["ConnectionType"] = value["connection_type"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "other_participant_identifiers" in value:
        import capo_partnercentral_account.types.participant_identifier_list

        out["OtherParticipantIdentifiers"] = (
            capo_partnercentral_account.types.participant_identifier_list.serialize_aws_json_1_0(
                value["other_participant_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsRequest:
    out: ListConnectionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListConnectionsRequest.catalog required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ConnectionType") is not None:
        out["connection_type"] = data["ConnectionType"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("OtherParticipantIdentifiers") is not None:
        import capo_partnercentral_account.types.participant_identifier_list

        out["other_participant_identifiers"] = (
            capo_partnercentral_account.types.participant_identifier_list.deserialize_aws_json_1_0(
                data["OtherParticipantIdentifiers"]
            )
        )
    return out
