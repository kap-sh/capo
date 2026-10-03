"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInsightsPathRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ip_address
    import capo_ec2.types.network_insights_resource_id
    import capo_ec2.types.path_request_filter
    import capo_ec2.types.port
    import capo_ec2.types.protocol
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateNetworkInsightsPathRequest(TypedDict, closed=True):
    source_ip: NotRequired["capo_ec2.types.ip_address.IpAddress"]
    """<p>The IP address of the source.</p>"""
    destination_ip: NotRequired["capo_ec2.types.ip_address.IpAddress"]
    """<p>The IP address of the destination.</p>"""
    source: NotRequired[
        "capo_ec2.types.network_insights_resource_id.NetworkInsightsResourceId"
    ]
    """<p>The ID or ARN of the source. If the resource is in another account, you must specify an ARN.</p>"""
    destination: NotRequired[
        "capo_ec2.types.network_insights_resource_id.NetworkInsightsResourceId"
    ]
    """<p>The ID or ARN of the destination. If the resource is in another account, you must specify an ARN.</p>"""
    protocol: NotRequired["capo_ec2.types.protocol.Protocol"]
    """<p>The protocol.</p>"""
    destination_port: NotRequired["capo_ec2.types.port.Port"]
    """<p>The destination port.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to add to the path.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">How to ensure idempotency</a>.</p>"""
    filter_at_source: NotRequired[
        "capo_ec2.types.path_request_filter.PathRequestFilter"
    ]
    """<p>Scopes the analysis to network paths that match specific filters at the source. If you specify this parameter, you can't specify the parameters for the source IP address or the destination port.</p>"""
    filter_at_destination: NotRequired[
        "capo_ec2.types.path_request_filter.PathRequestFilter"
    ]
    """<p>Scopes the analysis to network paths that match specific filters at the destination. If you specify this parameter, you can't specify the parameter for the destination IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkInsightsPathRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_ip" in value:
        pairs.append((f"{key_prefix}SourceIp", str(value["source_ip"])))
    if "destination_ip" in value:
        pairs.append((f"{key_prefix}DestinationIp", str(value["destination_ip"])))
    if "source" in value:
        pairs.append((f"{key_prefix}Source", str(value["source"])))
    if "destination" in value:
        pairs.append((f"{key_prefix}Destination", str(value["destination"])))
    if "protocol" in value:
        import capo_ec2.types.protocol

        capo_ec2.types.protocol.serialize_ec2_query(
            value["protocol"], pairs, f"{key_prefix}Protocol"
        )
    if "destination_port" in value:
        pairs.append((f"{key_prefix}DestinationPort", str(value["destination_port"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "filter_at_source" in value:
        import capo_ec2.types.path_request_filter

        capo_ec2.types.path_request_filter.serialize_ec2_query(
            value["filter_at_source"], pairs, f"{key_prefix}FilterAtSource"
        )
    if "filter_at_destination" in value:
        import capo_ec2.types.path_request_filter

        capo_ec2.types.path_request_filter.serialize_ec2_query(
            value["filter_at_destination"], pairs, f"{key_prefix}FilterAtDestination"
        )


def deserialize_ec2_query(el: Element) -> CreateNetworkInsightsPathRequest:
    out: CreateNetworkInsightsPathRequest = {}  # type: ignore[typeddict-item]
    child_source_ip = el.find("SourceIp")
    if child_source_ip is not None:
        out["source_ip"] = str(child_source_ip.text or "")
    child_destination_ip = el.find("DestinationIp")
    if child_destination_ip is not None:
        out["destination_ip"] = str(child_destination_ip.text or "")
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_destination = el.find("Destination")
    if child_destination is not None:
        out["destination"] = str(child_destination.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_ec2.types.protocol

        out["protocol"] = capo_ec2.types.protocol.deserialize_ec2_query(child_protocol)
    child_destination_port = el.find("DestinationPort")
    if child_destination_port is not None:
        out["destination_port"] = int(child_destination_port.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_filter_at_source = el.find("FilterAtSource")
    if child_filter_at_source is not None:
        import capo_ec2.types.path_request_filter

        out["filter_at_source"] = (
            capo_ec2.types.path_request_filter.deserialize_ec2_query(
                child_filter_at_source
            )
        )
    child_filter_at_destination = el.find("FilterAtDestination")
    if child_filter_at_destination is not None:
        import capo_ec2.types.path_request_filter

        out["filter_at_destination"] = (
            capo_ec2.types.path_request_filter.deserialize_ec2_query(
                child_filter_at_destination
            )
        )
    return out
