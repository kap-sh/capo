"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.gateway_name
    import capo_iotsitewise.types.gateway_platform
    import capo_iotsitewise.types.gateway_version
    import capo_iotsitewise.types.tag_map


class CreateGatewayRequest(TypedDict, closed=True):
    gateway_name: "capo_iotsitewise.types.gateway_name.GatewayName"
    """<p>A unique name for the gateway.</p>"""
    gateway_platform: "capo_iotsitewise.types.gateway_platform.GatewayPlatform"
    """<p>The gateway's platform. You can only specify one platform in a gateway.</p>"""
    gateway_version: NotRequired[
        "capo_iotsitewise.types.gateway_version.GatewayVersion"
    ]
    """<p>The version of the gateway to create. Specify <code>3</code> to create an MQTT-enabled, V3 gateway and <code>2</code> to create a Classic streams, V2 gateway. If not specified, the default is <code>2</code> (Classic streams, V2 gateway).</p> <note> <p>When creating a V3 gateway (<code>gatewayVersion=3</code>) with the <code>GreengrassV2</code> platform, you must also specify the <code>coreDeviceOperatingSystem</code> parameter.</p> </note> <p> We recommend creating an MQTT-enabled gateway for self-hosted gateways and Siemens Industrial Edge gateways. For more information on gateway versions, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html">Use Amazon Web Services IoT SiteWise Edge Edge gateways</a>.</p>"""
    tags: NotRequired["capo_iotsitewise.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the gateway. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayRequest) -> dict:
    out: dict = {}
    out["gatewayName"] = value["gateway_name"]
    import capo_iotsitewise.types.gateway_platform

    out["gatewayPlatform"] = capo_iotsitewise.types.gateway_platform.serialize_json(
        value["gateway_platform"]
    )
    if "gateway_version" in value:
        out["gatewayVersion"] = value["gateway_version"]
    if "tags" in value:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateGatewayRequest:
    out: CreateGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("gatewayName") is not None:
        out["gateway_name"] = data["gatewayName"]
    else:
        raise DeserializationError("CreateGatewayRequest.gateway_name required")
    if data.get("gatewayPlatform") is not None:
        import capo_iotsitewise.types.gateway_platform

        out["gateway_platform"] = (
            capo_iotsitewise.types.gateway_platform.deserialize_json(
                data["gatewayPlatform"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayRequest.gateway_platform required")
    if data.get("gatewayVersion") is not None:
        out["gateway_version"] = data["gatewayVersion"]
    if data.get("tags") is not None:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    return out
