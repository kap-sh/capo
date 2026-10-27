"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListCoreNetworkRoutingInformationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.constrained_string_list
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.filter_map
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class ListCoreNetworkRoutingInformationRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network to retrieve routing information for.</p>"""
    segment_name: "capo_networkmanager.types.constrained_string.ConstrainedString"
    """<p>The name of the segment to filter routing information by.</p>"""
    edge_location: "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    """<p>The edge location to filter routing information by.</p>"""
    next_hop_filters: NotRequired["capo_networkmanager.types.filter_map.FilterMap"]
    """<p>Filters to apply based on next hop information. Each filter value must exactly match the corresponding next hop value. Values for the same filter are joined with OR, and different filters are joined with AND. The following filters are supported:</p> <ul> <li> <p> <code>core-network-attachment-id</code>: The ID of the core network attachment for the next hop, for example <code>attachment-0123456789abcdef0</code>.</p> </li> <li> <p> <code>segment-name</code>: The name of the segment for the next hop.</p> </li> <li> <p> <code>edge-location</code>: The edge location for the next hop, for example <code>us-east-1</code>.</p> </li> <li> <p> <code>resource-id</code>: The ID of the resource for the next hop.</p> </li> <li> <p> <code>resource-type</code>: The type of resource for the next hop. The possible values are <code>vpc</code>, <code>vpn</code>, <code>connect-peer</code>, <code>direct-connect-gateway</code>, <code>transit-gateway-route-table</code>, <code>attachment</code>, and <code>blackhole</code>.</p> </li> <li> <p> <code>ip-address</code>: The IP address of the next hop. For a Site-to-Site VPN next hop, this is the outside IP address of the AWS side of the VPN tunnel. For a Connect peer next hop, this is the core network BGP address of the Connect peer. The value must be a single IPv4 or IPv6 address.</p> </li> </ul> <p>You can specify up to 10 filter values in total across <code>NextHopFilters</code> and the other match parameters in the request. Each filter value can be up to 256 characters.</p>"""
    exact_prefix_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Exact prefix values to match when filtering routing information.</p>"""
    longest_prefix_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Filters routing information based on the longest prefix that matches each provided IP address.</p>"""
    subnet_of_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Prefix values to filter routing information whose prefix is a subnet of the prefixes provided.</p>"""
    supernet_of_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Prefix values to filter routing information whose prefix is a supernet of the prefixes provided.</p>"""
    local_preference_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Local preference values to match when filtering routing information.</p>"""
    exact_as_path_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Exact AS path values to match when filtering routing information.</p>"""
    med_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Multi-Exit Discriminator (MED) values to match when filtering routing information.</p>"""
    community_matches: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>BGP community values to match when filtering routing information.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of routing information entries to return in a single page.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkRoutingInformationRequest) -> dict:
    out: dict = {}
    out["SegmentName"] = value["segment_name"]
    out["EdgeLocation"] = value["edge_location"]
    if "next_hop_filters" in value:
        import capo_networkmanager.types.filter_map

        out["NextHopFilters"] = capo_networkmanager.types.filter_map.serialize_json(
            value["next_hop_filters"]
        )
    if "exact_prefix_matches" in value:
        import capo_networkmanager.types.constrained_string_list

        out["ExactPrefixMatches"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["exact_prefix_matches"]
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
    if "local_preference_matches" in value:
        import capo_networkmanager.types.constrained_string_list

        out["LocalPreferenceMatches"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["local_preference_matches"]
            )
        )
    if "exact_as_path_matches" in value:
        import capo_networkmanager.types.constrained_string_list

        out["ExactAsPathMatches"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["exact_as_path_matches"]
            )
        )
    if "med_matches" in value:
        import capo_networkmanager.types.constrained_string_list

        out["MedMatches"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["med_matches"]
            )
        )
    if "community_matches" in value:
        import capo_networkmanager.types.constrained_string_list

        out["CommunityMatches"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["community_matches"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCoreNetworkRoutingInformationRequest:
    out: ListCoreNetworkRoutingInformationRequest = {}  # type: ignore[typeddict-item]
    if data.get("SegmentName") is not None:
        out["segment_name"] = data["SegmentName"]
    else:
        out["segment_name"] = ""
    if data.get("EdgeLocation") is not None:
        out["edge_location"] = data["EdgeLocation"]
    else:
        out["edge_location"] = ""
    if data.get("NextHopFilters") is not None:
        import capo_networkmanager.types.filter_map

        out["next_hop_filters"] = capo_networkmanager.types.filter_map.deserialize_json(
            data["NextHopFilters"]
        )
    if data.get("ExactPrefixMatches") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["exact_prefix_matches"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["ExactPrefixMatches"]
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
    if data.get("LocalPreferenceMatches") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["local_preference_matches"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["LocalPreferenceMatches"]
            )
        )
    if data.get("ExactAsPathMatches") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["exact_as_path_matches"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["ExactAsPathMatches"]
            )
        )
    if data.get("MedMatches") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["med_matches"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["MedMatches"]
            )
        )
    if data.get("CommunityMatches") is not None:
        import capo_networkmanager.types.constrained_string_list

        out["community_matches"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["CommunityMatches"]
            )
        )
    return out
