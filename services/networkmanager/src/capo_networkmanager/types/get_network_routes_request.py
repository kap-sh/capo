"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string_list
    import capo_networkmanager.types.filter_map
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.route_state_list
    import capo_networkmanager.types.route_table_identifier
    import capo_networkmanager.types.route_type_list


class GetNetworkRoutesRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    route_table_identifier: (
        "capo_networkmanager.types.route_table_identifier.RouteTableIdentifier"
    )
    """<p>The ID of the route table.</p>"""
    exact_cidr_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>An exact CIDR block.</p>"""
    longest_prefix_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The most specific route that matches the traffic (longest prefix match).</p>"""
    subnet_of_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The routes with a subnet that match the specified CIDR filter.</p>"""
    supernet_of_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The routes with a CIDR that encompasses the CIDR filter. Example: If you specify 10.0.1.0/30, then the result returns 10.0.1.0/29.</p>"""
    prefix_list_ids: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The IDs of the prefix lists.</p>"""
    states: NotRequired["capo_networkmanager.types.route_state_list.RouteStateList"]
    """<p>The route states.</p>"""
    types: NotRequired["capo_networkmanager.types.route_type_list.RouteTypeList"]
    """<p>The route types.</p>"""
    destination_filters: NotRequired["capo_networkmanager.types.filter_map.FilterMap"]
    """<p>Filter by route table destination. Possible Values: TRANSIT_GATEWAY_ATTACHMENT_ID, RESOURCE_ID, or RESOURCE_TYPE.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkRoutesRequest) -> dict:
    out: dict = {}
    import capo_networkmanager.types.route_table_identifier

    out["RouteTableIdentifier"] = (
        capo_networkmanager.types.route_table_identifier.serialize_json(
            value["route_table_identifier"]
        )
    )
    if "exact_cidr_matches" in value:
        import capo_networkmanager.types.constrained_string_list

        out["ExactCidrMatches"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["exact_cidr_matches"]
            )
        )
    if "longest_prefix_matches" in value:
        import capo_networkmanager.types.constrained_string_list

        out["LongestPrefixMatches"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["longest_prefix_matches"]
            )
        )
    if "subnet_of_matches" in value:
        import capo_networkmanager.types.constrained_string_list

        out["SubnetOfMatches"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["subnet_of_matches"]
            )
        )
    if "supernet_of_matches" in value:
        import capo_networkmanager.types.constrained_string_list

        out["SupernetOfMatches"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["supernet_of_matches"]
            )
        )
    if "prefix_list_ids" in value:
        import capo_networkmanager.types.constrained_string_list

        out["PrefixListIds"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["prefix_list_ids"]
            )
        )
    if "states" in value:
        import capo_networkmanager.types.route_state_list

        out["States"] = capo_networkmanager.types.route_state_list.serialize_json(
            value["states"]
        )
    if "types" in value:
        import capo_networkmanager.types.route_type_list

        out["Types"] = capo_networkmanager.types.route_type_list.serialize_json(
            value["types"]
        )
    if "destination_filters" in value:
        import capo_networkmanager.types.filter_map

        out["DestinationFilters"] = capo_networkmanager.types.filter_map.serialize_json(
            value["destination_filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetNetworkRoutesRequest:
    out: GetNetworkRoutesRequest = {}  # type: ignore[typeddict-item]
    if data.get("RouteTableIdentifier") is not None:
        import capo_networkmanager.types.route_table_identifier

        out["route_table_identifier"] = (
            capo_networkmanager.types.route_table_identifier.deserialize_json(
                data["RouteTableIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "GetNetworkRoutesRequest.route_table_identifier required"
        )
    if data.get("ExactCidrMatches") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["exact_cidr_matches"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["ExactCidrMatches"]
            )
        )
    if data.get("LongestPrefixMatches") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["longest_prefix_matches"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["LongestPrefixMatches"]
            )
        )
    if data.get("SubnetOfMatches") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["subnet_of_matches"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["SubnetOfMatches"]
            )
        )
    if data.get("SupernetOfMatches") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["supernet_of_matches"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["SupernetOfMatches"]
            )
        )
    if data.get("PrefixListIds") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["prefix_list_ids"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["PrefixListIds"]
            )
        )
    if data.get("States") is not None:
        import capo_networkmanager.types.route_state_list

        out["states"] = capo_networkmanager.types.route_state_list.deserialize_json(
            data["States"]
        )
    if data.get("Types") is not None:
        import capo_networkmanager.types.route_type_list

        out["types"] = capo_networkmanager.types.route_type_list.deserialize_json(
            data["Types"]
        )
    if data.get("DestinationFilters") is not None:
        import capo_networkmanager.types.filter_map

        out["destination_filters"] = (
            capo_networkmanager.types.filter_map.deserialize_json(
                data["DestinationFilters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
