"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.gateway_capability_summaries
    import capo_iotsitewise.types.gateway_name
    import capo_iotsitewise.types.gateway_platform
    import capo_iotsitewise.types.gateway_version
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.timestamp


class DescribeGatewayResponse(TypedDict, closed=True):
    gateway_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the gateway device.</p>"""
    gateway_name: "capo_iotsitewise.types.gateway_name.GatewayName"
    """<p>The name of the gateway.</p>"""
    gateway_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the gateway, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:gateway/${GatewayId}</code> </p>"""
    gateway_platform: NotRequired[
        "capo_iotsitewise.types.gateway_platform.GatewayPlatform"
    ]
    """<p>The gateway's platform.</p>"""
    gateway_version: NotRequired[
        "capo_iotsitewise.types.gateway_version.GatewayVersion"
    ]
    """<p>The version of the gateway. A value of <code>3</code> indicates an MQTT-enabled, V3 gateway, while <code>2</code> indicates a Classic streams, V2 gateway.</p>"""
    gateway_capability_summaries: (
        "capo_iotsitewise.types.gateway_capability_summaries.GatewayCapabilitySummaries"
    )
    """<p>A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html">DescribeGatewayCapabilityConfiguration</a>.</p>"""
    creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the gateway was created, in Unix epoch time.</p>"""
    last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the gateway was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["gatewayName"] = value["gateway_name"]
    out["gatewayArn"] = value["gateway_arn"]
    if "gateway_platform" in value:
        import capo_iotsitewise.types.gateway_platform

        out["gatewayPlatform"] = capo_iotsitewise.types.gateway_platform.serialize_json(
            value["gateway_platform"]
        )
    if "gateway_version" in value:
        out["gatewayVersion"] = value["gateway_version"]
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


def deserialize_json(data: dict) -> DescribeGatewayResponse:
    out: DescribeGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("DescribeGatewayResponse.gateway_id required")
    if data.get("gatewayName") is not None:
        out["gateway_name"] = data["gatewayName"]
    else:
        raise DeserializationError("DescribeGatewayResponse.gateway_name required")
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("DescribeGatewayResponse.gateway_arn required")
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
    else:
        raise DeserializationError(
            "DescribeGatewayResponse.gateway_capability_summaries required"
        )
    if data.get("creationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        raise DeserializationError("DescribeGatewayResponse.creation_date required")
    if data.get("lastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        raise DeserializationError("DescribeGatewayResponse.last_update_date required")
    return out
