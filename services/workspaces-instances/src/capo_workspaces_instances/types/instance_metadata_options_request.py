"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceMetadataOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.http_endpoint_enum
    import capo_workspaces_instances.types.http_protocol_ipv6_enum
    import capo_workspaces_instances.types.http_put_response_hop_limit
    import capo_workspaces_instances.types.http_tokens_enum
    import capo_workspaces_instances.types.instance_metadata_tags_enum


class InstanceMetadataOptionsRequest(TypedDict, closed=True):
    http_endpoint: NotRequired[
        "capo_workspaces_instances.types.http_endpoint_enum.HttpEndpointEnum"
    ]
    """<p>Enables or disables HTTP endpoint for instance metadata.</p>"""
    http_protocol_ipv6: NotRequired[
        "capo_workspaces_instances.types.http_protocol_ipv6_enum.HttpProtocolIpv6Enum"
    ]
    """<p>Configures IPv6 support for instance metadata HTTP protocol.</p>"""
    http_put_response_hop_limit: NotRequired[
        "capo_workspaces_instances.types.http_put_response_hop_limit.HttpPutResponseHopLimit"
    ]
    """<p>Sets maximum number of network hops for metadata PUT responses.</p>"""
    http_tokens: NotRequired[
        "capo_workspaces_instances.types.http_tokens_enum.HttpTokensEnum"
    ]
    """<p>Configures token requirement for instance metadata retrieval.</p>"""
    instance_metadata_tags: NotRequired[
        "capo_workspaces_instances.types.instance_metadata_tags_enum.InstanceMetadataTagsEnum"
    ]
    """<p>Enables or disables instance metadata tags retrieval.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceMetadataOptionsRequest) -> dict:
    out: dict = {}
    if "http_endpoint" in value:
        import capo_workspaces_instances.types.http_endpoint_enum

        out["HttpEndpoint"] = (
            capo_workspaces_instances.types.http_endpoint_enum.serialize_aws_json_1_0(
                value["http_endpoint"]
            )
        )
    if "http_protocol_ipv6" in value:
        import capo_workspaces_instances.types.http_protocol_ipv6_enum

        out["HttpProtocolIpv6"] = (
            capo_workspaces_instances.types.http_protocol_ipv6_enum.serialize_aws_json_1_0(
                value["http_protocol_ipv6"]
            )
        )
    if "http_put_response_hop_limit" in value:
        out["HttpPutResponseHopLimit"] = value["http_put_response_hop_limit"]
    if "http_tokens" in value:
        import capo_workspaces_instances.types.http_tokens_enum

        out["HttpTokens"] = (
            capo_workspaces_instances.types.http_tokens_enum.serialize_aws_json_1_0(
                value["http_tokens"]
            )
        )
    if "instance_metadata_tags" in value:
        import capo_workspaces_instances.types.instance_metadata_tags_enum

        out["InstanceMetadataTags"] = (
            capo_workspaces_instances.types.instance_metadata_tags_enum.serialize_aws_json_1_0(
                value["instance_metadata_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceMetadataOptionsRequest:
    out: InstanceMetadataOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("HttpEndpoint") is not None:
        import capo_workspaces_instances.types.http_endpoint_enum

        out["http_endpoint"] = (
            capo_workspaces_instances.types.http_endpoint_enum.deserialize_aws_json_1_0(
                data["HttpEndpoint"]
            )
        )
    if data.get("HttpProtocolIpv6") is not None:
        import capo_workspaces_instances.types.http_protocol_ipv6_enum

        out["http_protocol_ipv6"] = (
            capo_workspaces_instances.types.http_protocol_ipv6_enum.deserialize_aws_json_1_0(
                data["HttpProtocolIpv6"]
            )
        )
    if data.get("HttpPutResponseHopLimit") is not None:
        out["http_put_response_hop_limit"] = data["HttpPutResponseHopLimit"]
    if data.get("HttpTokens") is not None:
        import capo_workspaces_instances.types.http_tokens_enum

        out["http_tokens"] = (
            capo_workspaces_instances.types.http_tokens_enum.deserialize_aws_json_1_0(
                data["HttpTokens"]
            )
        )
    if data.get("InstanceMetadataTags") is not None:
        import capo_workspaces_instances.types.instance_metadata_tags_enum

        out["instance_metadata_tags"] = (
            capo_workspaces_instances.types.instance_metadata_tags_enum.deserialize_aws_json_1_0(
                data["InstanceMetadataTags"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceMetadataOptionsRequest) -> dict:
    out: dict = {}
    if "http_endpoint" in value:
        import capo_workspaces_instances.types.http_endpoint_enum

        out["HttpEndpoint"] = (
            capo_workspaces_instances.types.http_endpoint_enum.serialize_cbor(
                value["http_endpoint"]
            )
        )
    if "http_protocol_ipv6" in value:
        import capo_workspaces_instances.types.http_protocol_ipv6_enum

        out["HttpProtocolIpv6"] = (
            capo_workspaces_instances.types.http_protocol_ipv6_enum.serialize_cbor(
                value["http_protocol_ipv6"]
            )
        )
    if "http_put_response_hop_limit" in value:
        out["HttpPutResponseHopLimit"] = value["http_put_response_hop_limit"]
    if "http_tokens" in value:
        import capo_workspaces_instances.types.http_tokens_enum

        out["HttpTokens"] = (
            capo_workspaces_instances.types.http_tokens_enum.serialize_cbor(
                value["http_tokens"]
            )
        )
    if "instance_metadata_tags" in value:
        import capo_workspaces_instances.types.instance_metadata_tags_enum

        out["InstanceMetadataTags"] = (
            capo_workspaces_instances.types.instance_metadata_tags_enum.serialize_cbor(
                value["instance_metadata_tags"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> InstanceMetadataOptionsRequest:
    out: InstanceMetadataOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("HttpEndpoint") is not None:
        import capo_workspaces_instances.types.http_endpoint_enum

        out["http_endpoint"] = (
            capo_workspaces_instances.types.http_endpoint_enum.deserialize_cbor(
                data["HttpEndpoint"]
            )
        )
    if data.get("HttpProtocolIpv6") is not None:
        import capo_workspaces_instances.types.http_protocol_ipv6_enum

        out["http_protocol_ipv6"] = (
            capo_workspaces_instances.types.http_protocol_ipv6_enum.deserialize_cbor(
                data["HttpProtocolIpv6"]
            )
        )
    if data.get("HttpPutResponseHopLimit") is not None:
        out["http_put_response_hop_limit"] = data["HttpPutResponseHopLimit"]
    if data.get("HttpTokens") is not None:
        import capo_workspaces_instances.types.http_tokens_enum

        out["http_tokens"] = (
            capo_workspaces_instances.types.http_tokens_enum.deserialize_cbor(
                data["HttpTokens"]
            )
        )
    if data.get("InstanceMetadataTags") is not None:
        import capo_workspaces_instances.types.instance_metadata_tags_enum

        out["instance_metadata_tags"] = (
            capo_workspaces_instances.types.instance_metadata_tags_enum.deserialize_cbor(
                data["InstanceMetadataTags"]
            )
        )
    return out
