"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListChannelHandshakesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.associated_resource_identifier_list
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.handshake_status_list
    import capo_partnercentral_channel.types.handshake_type
    import capo_partnercentral_channel.types.list_channel_handshakes_type_filters
    import capo_partnercentral_channel.types.list_channel_handshakes_type_sort
    import capo_partnercentral_channel.types.next_token
    import capo_partnercentral_channel.types.participant_type


class ListChannelHandshakesRequest(TypedDict, closed=True):
    handshake_type: "capo_partnercentral_channel.types.handshake_type.HandshakeType"
    """<p>Filter results by handshake type.</p>"""
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier to filter handshakes.</p>"""
    participant_type: (
        "capo_partnercentral_channel.types.participant_type.ParticipantType"
    )
    """<p>Filter by participant type (sender or receiver).</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""
    statuses: NotRequired[
        "capo_partnercentral_channel.types.handshake_status_list.HandshakeStatusList"
    ]
    """<p>Filter results by handshake status.</p>"""
    associated_resource_identifiers: NotRequired[
        "capo_partnercentral_channel.types.associated_resource_identifier_list.AssociatedResourceIdentifierList"
    ]
    """<p>Filter by associated resource identifiers.</p>"""
    handshake_type_filters: NotRequired[
        "capo_partnercentral_channel.types.list_channel_handshakes_type_filters.ListChannelHandshakesTypeFilters"
    ]
    """<p>Type-specific filters for handshakes.</p>"""
    handshake_type_sort: NotRequired[
        "capo_partnercentral_channel.types.list_channel_handshakes_type_sort.ListChannelHandshakesTypeSort"
    ]
    """<p>Type-specific sorting options for handshakes.</p>"""
    next_token: NotRequired["capo_partnercentral_channel.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListChannelHandshakesRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_channel.types.handshake_type

    out["handshakeType"] = (
        capo_partnercentral_channel.types.handshake_type.serialize_aws_json_1_0(
            value["handshake_type"]
        )
    )
    out["catalog"] = value["catalog"]
    import capo_partnercentral_channel.types.participant_type

    out["participantType"] = (
        capo_partnercentral_channel.types.participant_type.serialize_aws_json_1_0(
            value["participant_type"]
        )
    )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "statuses" in value:
        import capo_partnercentral_channel.types.handshake_status_list

        out["statuses"] = (
            capo_partnercentral_channel.types.handshake_status_list.serialize_aws_json_1_0(
                value["statuses"]
            )
        )
    if "associated_resource_identifiers" in value:
        import capo_partnercentral_channel.types.associated_resource_identifier_list

        out["associatedResourceIdentifiers"] = (
            capo_partnercentral_channel.types.associated_resource_identifier_list.serialize_aws_json_1_0(
                value["associated_resource_identifiers"]
            )
        )
    if "handshake_type_filters" in value:
        import capo_partnercentral_channel.types.list_channel_handshakes_type_filters

        out["handshakeTypeFilters"] = (
            capo_partnercentral_channel.types.list_channel_handshakes_type_filters.serialize_aws_json_1_0(
                value["handshake_type_filters"]
            )
        )
    if "handshake_type_sort" in value:
        import capo_partnercentral_channel.types.list_channel_handshakes_type_sort

        out["handshakeTypeSort"] = (
            capo_partnercentral_channel.types.list_channel_handshakes_type_sort.serialize_aws_json_1_0(
                value["handshake_type_sort"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListChannelHandshakesRequest:
    out: ListChannelHandshakesRequest = {}  # type: ignore[typeddict-item]
    if data.get("handshakeType") is not None:
        import capo_partnercentral_channel.types.handshake_type

        out["handshake_type"] = (
            capo_partnercentral_channel.types.handshake_type.deserialize_aws_json_1_0(
                data["handshakeType"]
            )
        )
    else:
        import typing

        out["handshake_type"] = typing.cast(
            "capo_partnercentral_channel.types.handshake_type.HandshakeType", ""
        )
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("participantType") is not None:
        import capo_partnercentral_channel.types.participant_type

        out["participant_type"] = (
            capo_partnercentral_channel.types.participant_type.deserialize_aws_json_1_0(
                data["participantType"]
            )
        )
    else:
        import typing

        out["participant_type"] = typing.cast(
            "capo_partnercentral_channel.types.participant_type.ParticipantType", ""
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("statuses") is not None:
        import capo_partnercentral_channel.types.handshake_status_list

        out["statuses"] = (
            capo_partnercentral_channel.types.handshake_status_list.deserialize_aws_json_1_0(
                data["statuses"]
            )
        )
    if data.get("associatedResourceIdentifiers") is not None:
        import capo_partnercentral_channel.types.associated_resource_identifier_list

        out["associated_resource_identifiers"] = (
            capo_partnercentral_channel.types.associated_resource_identifier_list.deserialize_aws_json_1_0(
                data["associatedResourceIdentifiers"]
            )
        )
    if data.get("handshakeTypeFilters") is not None:
        import capo_partnercentral_channel.types.list_channel_handshakes_type_filters

        out["handshake_type_filters"] = (
            capo_partnercentral_channel.types.list_channel_handshakes_type_filters.deserialize_aws_json_1_0(
                data["handshakeTypeFilters"]
            )
        )
    if data.get("handshakeTypeSort") is not None:
        import capo_partnercentral_channel.types.list_channel_handshakes_type_sort

        out["handshake_type_sort"] = (
            capo_partnercentral_channel.types.list_channel_handshakes_type_sort.deserialize_aws_json_1_0(
                data["handshakeTypeSort"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
