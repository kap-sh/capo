"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateRouterInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.maintenance_configuration
    import capo_mediaconnect.types.router_content_quality_analysis_configuration
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_configuration
    import capo_mediaconnect.types.router_input_tier
    import capo_mediaconnect.types.router_input_transit_encryption
    import capo_mediaconnect.types.routing_scope


class UpdateRouterInputRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input that you want to update.</p>"""
    name: NotRequired["str"]
    """<p>The updated name for the router input.</p>"""
    configuration: NotRequired[
        "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
    ]
    """<p>The updated configuration settings for the router input. Changing the type of the configuration is not supported.</p>"""
    maximum_bitrate: NotRequired["int"]
    """<p>The updated maximum bitrate for the router input.</p>"""
    routing_scope: NotRequired["capo_mediaconnect.types.routing_scope.RoutingScope"]
    """<p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - can be assigned only to outputs in the same Region. GLOBAL - can be assigned to outputs in any Region.</p>"""
    tier: NotRequired["capo_mediaconnect.types.router_input_tier.RouterInputTier"]
    """<p>The updated tier level for the router input.</p>"""
    transit_encryption: NotRequired[
        "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
    ]
    """<p>The updated transit encryption settings for the router input.</p>"""
    maintenance_configuration: NotRequired[
        "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
    ]
    """<p>The updated maintenance configuration settings for the router input, including any changes to preferred maintenance windows and schedules.</p>"""
    content_quality_analysis_configuration: NotRequired[
        "capo_mediaconnect.types.router_content_quality_analysis_configuration.RouterContentQualityAnalysisConfiguration"
    ]
    """<p>The content quality analysis configuration for the router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouterInputRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "configuration" in value:
        import capo_mediaconnect.types.router_input_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_input_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "maximum_bitrate" in value:
        out["maximumBitrate"] = value["maximum_bitrate"]
    if "routing_scope" in value:
        import capo_mediaconnect.types.routing_scope

        out["routingScope"] = capo_mediaconnect.types.routing_scope.serialize_json(
            value["routing_scope"]
        )
    if "tier" in value:
        import capo_mediaconnect.types.router_input_tier

        out["tier"] = capo_mediaconnect.types.router_input_tier.serialize_json(
            value["tier"]
        )
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
    if "content_quality_analysis_configuration" in value:
        import capo_mediaconnect.types.router_content_quality_analysis_configuration

        out["contentQualityAnalysisConfiguration"] = (
            capo_mediaconnect.types.router_content_quality_analysis_configuration.serialize_json(
                value["content_quality_analysis_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRouterInputRequest:
    out: UpdateRouterInputRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.router_input_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_input_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if data.get("maximumBitrate") is not None:
        out["maximum_bitrate"] = data["maximumBitrate"]
    if data.get("routingScope") is not None:
        import capo_mediaconnect.types.routing_scope

        out["routing_scope"] = capo_mediaconnect.types.routing_scope.deserialize_json(
            data["routingScope"]
        )
    if data.get("tier") is not None:
        import capo_mediaconnect.types.router_input_tier

        out["tier"] = capo_mediaconnect.types.router_input_tier.deserialize_json(
            data["tier"]
        )
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
    if data.get("contentQualityAnalysisConfiguration") is not None:
        import capo_mediaconnect.types.router_content_quality_analysis_configuration

        out["content_quality_analysis_configuration"] = (
            capo_mediaconnect.types.router_content_quality_analysis_configuration.deserialize_json(
                data["contentQualityAnalysisConfiguration"]
            )
        )
    return out
