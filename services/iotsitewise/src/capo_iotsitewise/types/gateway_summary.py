"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GatewaySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.gateway_capability_summaries
    import capo_iotsitewise.types.gateway_name
    import capo_iotsitewise.types.gateway_platform
    import capo_iotsitewise.types.gateway_version
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.timestamp


class GatewaySummary(TypedDict, closed=True):
    gateway_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the gateway device.</p>"""
    gateway_name: "capo_iotsitewise.types.gateway_name.GatewayName"
    """<p>The name of the gateway.</p>"""
    gateway_platform: NotRequired[
        "capo_iotsitewise.types.gateway_platform.GatewayPlatform"
    ]
    gateway_version: NotRequired[
        "capo_iotsitewise.types.gateway_version.GatewayVersion"
    ]
    """<p>The version of the gateway. A value of <code>3</code> indicates an MQTT-enabled, V3 gateway, while <code>2</code> indicates a Classic streams, V2 gateway.</p>"""
    gateway_capability_summaries: NotRequired[
        "capo_iotsitewise.types.gateway_capability_summaries.GatewayCapabilitySummaries"
    ]
    """<p>A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html">DescribeGatewayCapabilityConfiguration</a>.</p>"""
    creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the gateway was created, in Unix epoch time.</p>"""
    last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the gateway was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewaySummary) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["gatewayName"] = value["gateway_name"]
    if "gateway_platform" in value:
        import capo_iotsitewise.types.gateway_platform

        out["gatewayPlatform"] = capo_iotsitewise.types.gateway_platform.serialize_json(
            value["gateway_platform"]
        )
    if "gateway_version" in value:
        out["gatewayVersion"] = value["gateway_version"]
    if "gateway_capability_summaries" in value:
        import capo_iotsitewise.types.gateway_capability_summaries

        out["gatewayCapabilitySummaries"] = (
            capo_iotsitewise.types.gateway_capability_summaries.serialize_json(
                value["gateway_capability_summaries"]
            )
        )
    import capo_iotsitewise.types.timestamp

    out["creationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["lastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["last_update_date"]
    )
    return out


def deserialize_json(data: dict) -> GatewaySummary:
    out: GatewaySummary = {}  # type: ignore[typeddict-item]
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        out["gateway_id"] = ""
    if data.get("gatewayName") is not None:
        out["gateway_name"] = data["gatewayName"]
    else:
        out["gateway_name"] = ""
    if data.get("gatewayPlatform") is not None:
        import capo_iotsitewise.types.gateway_platform

        out["gateway_platform"] = (
            capo_iotsitewise.types.gateway_platform.deserialize_json(
                data["gatewayPlatform"]
            )
        )
    if data.get("gatewayVersion") is not None:
        out["gateway_version"] = data["gatewayVersion"]
    if data.get("gatewayCapabilitySummaries") is not None:
        import capo_iotsitewise.types.gateway_capability_summaries

        out["gateway_capability_summaries"] = (
            capo_iotsitewise.types.gateway_capability_summaries.deserialize_json(
                data["gatewayCapabilitySummaries"]
            )
        )
    if data.get("creationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        import datetime

        out["last_update_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
