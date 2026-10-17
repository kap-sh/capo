"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateRouterInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.client_token
    import capo_mediaconnect.types.maintenance_configuration
    import capo_mediaconnect.types.router_content_quality_analysis_configuration
    import capo_mediaconnect.types.router_input_configuration
    import capo_mediaconnect.types.router_input_tier
    import capo_mediaconnect.types.router_input_transit_encryption
    import capo_mediaconnect.types.routing_scope


class CreateRouterInputRequest(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router input.</p>"""
    configuration: (
        "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
    )
    """<p>The configuration settings for the router input, which can include the protocol, network interface, and other details.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate for the router input.</p>"""
    routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope"
    """<p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - connects only to outputs in same Region. GLOBAL - connects to outputs in any Region.</p>"""
    tier: "capo_mediaconnect.types.router_input_tier.RouterInputTier"
    """<p>The tier level for the router input.</p>"""
    region_name: NotRequired["str"]
    """<p>The Amazon Web Services Region for the router input. Defaults to the current region if not specified.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone where you want to create the router input. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>"""
    transit_encryption: NotRequired[
        "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
    ]
    """<p>The transit encryption settings for the router input.</p>"""
    maintenance_configuration: NotRequired[
        "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
    ]
    """<p>The maintenance configuration settings for the router input, including preferred maintenance windows and schedules.</p>"""
    tags: NotRequired["capo_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p>Key-value pairs that can be used to tag and organize this router input.</p>"""
    client_token: NotRequired["capo_mediaconnect.types.client_token.ClientToken"]
    """<p>A unique identifier for the request to ensure idempotency.</p>"""
    content_quality_analysis_configuration: NotRequired[
        "capo_mediaconnect.types.router_content_quality_analysis_configuration.RouterContentQualityAnalysisConfiguration"
    ]
    """<p>The content quality analysis configuration for the router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRouterInputRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_input_configuration

    out["configuration"] = (
        capo_mediaconnect.types.router_input_configuration.serialize_json(
            value["configuration"]
        )
    )
    out["maximumBitrate"] = value["maximum_bitrate"]
    import capo_mediaconnect.types.routing_scope

    out["routingScope"] = capo_mediaconnect.types.routing_scope.serialize_json(
        value["routing_scope"]
    )
    import capo_mediaconnect.types.router_input_tier

    out["tier"] = capo_mediaconnect.types.router_input_tier.serialize_json(
        value["tier"]
    )
    if "region_name" in value:
        out["regionName"] = value["region_name"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "transit_encryption" in value:
        import capo_mediaconnect.types.router_input_transit_encryption

        out["transitEncryption"] = (
            capo_mediaconnect.types.router_input_transit_encryption.serialize_json(
                value["transit_encryption"]
            )
        )
    if "maintenance_configuration" in value:
        import capo_mediaconnect.types.maintenance_configuration

        out["maintenanceConfiguration"] = (
            capo_mediaconnect.types.maintenance_configuration.serialize_json(
                value["maintenance_configuration"]
            )
        )
    if "tags" in value:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "content_quality_analysis_configuration" in value:
        import capo_mediaconnect.types.router_content_quality_analysis_configuration

        out["contentQualityAnalysisConfiguration"] = (
            capo_mediaconnect.types.router_content_quality_analysis_configuration.serialize_json(
                value["content_quality_analysis_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRouterInputRequest:
    out: CreateRouterInputRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRouterInputRequest.name required")
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.router_input_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_input_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateRouterInputRequest.configuration required")
    if data.get("maximumBitrate") is not None:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        raise DeserializationError("CreateRouterInputRequest.maximum_bitrate required")
    if data.get("routingScope") is not None:
        import capo_mediaconnect.types.routing_scope

        out["routing_scope"] = capo_mediaconnect.types.routing_scope.deserialize_json(
            data["routingScope"]
        )
    else:
        raise DeserializationError("CreateRouterInputRequest.routing_scope required")
    if data.get("tier") is not None:
        import capo_mediaconnect.types.router_input_tier

        out["tier"] = capo_mediaconnect.types.router_input_tier.deserialize_json(
            data["tier"]
        )
    else:
        raise DeserializationError("CreateRouterInputRequest.tier required")
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("transitEncryption") is not None:
        import capo_mediaconnect.types.router_input_transit_encryption

        out["transit_encryption"] = (
            capo_mediaconnect.types.router_input_transit_encryption.deserialize_json(
                data["transitEncryption"]
            )
        )
    if data.get("maintenanceConfiguration") is not None:
        import capo_mediaconnect.types.maintenance_configuration

        out["maintenance_configuration"] = (
            capo_mediaconnect.types.maintenance_configuration.deserialize_json(
                data["maintenanceConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("contentQualityAnalysisConfiguration") is not None:
        import capo_mediaconnect.types.router_content_quality_analysis_configuration

        out["content_quality_analysis_configuration"] = (
            capo_mediaconnect.types.router_content_quality_analysis_configuration.deserialize_json(
                data["contentQualityAnalysisConfiguration"]
            )
        )
    return out
