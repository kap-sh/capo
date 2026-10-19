"""Generated from Smithy shape ``com.amazonaws.workspaces#AccessEndpointConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.access_endpoint_list
    import capo_workspaces.types.internet_fallback_protocol_list


class AccessEndpointConfig(TypedDict, closed=True):
    access_endpoints: "capo_workspaces.types.access_endpoint_list.AccessEndpointList"
    """<p>Indicates a list of access endpoints associated with this directory.</p>"""
    internet_fallback_protocols: NotRequired[
        "capo_workspaces.types.internet_fallback_protocol_list.InternetFallbackProtocolList"
    ]
    """<p>Indicates a list of protocols that fallback to using the public Internet when streaming over a VPC endpoint is not available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessEndpointConfig) -> dict:
    out: dict = {}
    import capo_workspaces.types.access_endpoint_list

    out["AccessEndpoints"] = (
        capo_workspaces.types.access_endpoint_list.serialize_aws_json_1_1(
            value["access_endpoints"]
        )
    )
    if "internet_fallback_protocols" in value:
        import capo_workspaces.types.internet_fallback_protocol_list

        out["InternetFallbackProtocols"] = (
            capo_workspaces.types.internet_fallback_protocol_list.serialize_aws_json_1_1(
                value["internet_fallback_protocols"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessEndpointConfig:
    out: AccessEndpointConfig = {}  # type: ignore[typeddict-item]
    if data.get("AccessEndpoints") is not None:
        import capo_workspaces.types.access_endpoint_list

        out["access_endpoints"] = (
            capo_workspaces.types.access_endpoint_list.deserialize_aws_json_1_1(
                data["AccessEndpoints"]
            )
        )
    else:
        out["access_endpoints"] = []
    if data.get("InternetFallbackProtocols") is not None:
        import capo_workspaces.types.internet_fallback_protocol_list

        out["internet_fallback_protocols"] = (
            capo_workspaces.types.internet_fallback_protocol_list.deserialize_aws_json_1_1(
                data["InternetFallbackProtocols"]
            )
        )
    return out
