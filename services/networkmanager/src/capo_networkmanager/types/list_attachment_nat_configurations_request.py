"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListAttachmentNatConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.filter_map
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class ListAttachmentNatConfigurationsRequest(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network. Returns the NAT configurations of attachments in the core network that support NAT.</p>"""
    attachment_id: NotRequired["capo_networkmanager.types.attachment_id.AttachmentId"]
    """<p>The ID of an attachment. Returns the NAT configuration of the specified attachment. If you specify both an attachment ID and a core network ID, the attachment ID is used.</p>"""
    filters: NotRequired["capo_networkmanager.types.filter_map.FilterMap"]
    """<p>The filters to apply to the results. Values for the same filter are joined with OR, and different filters are joined with AND. You can specify up to 10 filter values in total. The following filters are supported:</p> <ul> <li> <p> <code>nat-gateway-support</code>: The state of NAT gateway support on the attachment, for example <code>ENABLED</code>.</p> </li> <li> <p> <code>nat-system-route-support</code>: Whether system routes are installed for the attachment, <code>true</code> or <code>false</code>.</p> </li> <li> <p> <code>rule-number</code>: The rule number of a NAT rule.</p> </li> <li> <p> <code>match-source-cidr</code>: The source CIDR block of a NAT rule. The value must exactly match the CIDR block of the rule.</p> </li> <li> <p> <code>nat-cidr</code>: The NAT CIDR block of a NAT rule. The value must exactly match the CIDR block of the rule.</p> </li> <li> <p> <code>nat-rule-state</code>: The state of a NAT rule, for example <code>ACTIVATED</code>.</p> </li> </ul>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentNatConfigurationsRequest) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "filters" in value:
        import capo_networkmanager.types.filter_map

        out["Filters"] = capo_networkmanager.types.filter_map.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachmentNatConfigurationsRequest:
    out: ListAttachmentNatConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CoreNetworkId") is not None:
        out["core_network_id"] = data["CoreNetworkId"]
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    if data.get("Filters") is not None:
        import capo_networkmanager.types.filter_map

        out["filters"] = capo_networkmanager.types.filter_map.deserialize_json(
            data["Filters"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
