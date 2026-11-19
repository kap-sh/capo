"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListTLSInspectionConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.tls_inspection_configurations


class ListTLSInspectionConfigurationsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    tls_inspection_configurations: NotRequired[
        "capo_network_firewall.types.tls_inspection_configurations.TLSInspectionConfigurations"
    ]
    """<p>The TLS inspection configuration metadata objects that you've defined. Depending on your setting for max results and the number of TLS inspection configurations, this might not be the full list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTLSInspectionConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tls_inspection_configurations" in value:
        import capo_network_firewall.types.tls_inspection_configurations

        out["TLSInspectionConfigurations"] = (
            capo_network_firewall.types.tls_inspection_configurations.serialize_aws_json_1_0(
                value["tls_inspection_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTLSInspectionConfigurationsResponse:
    out: ListTLSInspectionConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("TLSInspectionConfigurations") is not None:
        import capo_network_firewall.types.tls_inspection_configurations

        out["tls_inspection_configurations"] = (
            capo_network_firewall.types.tls_inspection_configurations.deserialize_aws_json_1_0(
                data["TLSInspectionConfigurations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTLSInspectionConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tls_inspection_configurations" in value:
        import capo_network_firewall.types.tls_inspection_configurations

        out["TLSInspectionConfigurations"] = (
            capo_network_firewall.types.tls_inspection_configurations.serialize_cbor(
                value["tls_inspection_configurations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListTLSInspectionConfigurationsResponse:
    out: ListTLSInspectionConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("TLSInspectionConfigurations") is not None:
        import capo_network_firewall.types.tls_inspection_configurations

        out["tls_inspection_configurations"] = (
            capo_network_firewall.types.tls_inspection_configurations.deserialize_cbor(
                data["TLSInspectionConfigurations"]
            )
        )
    return out
