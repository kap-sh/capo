"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpPushRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.rtmp_push_naming_configuration
    import capo_mediaconnect.types.rtmp_push_naming_type


class RtmpPushRouterInputConfiguration(TypedDict, closed=True):
    port: "int"
    """<p>The port number for the RTMP protocol. The only valid value is <code>1935</code>.</p>"""
    naming_type: NotRequired[
        "capo_mediaconnect.types.rtmp_push_naming_type.RtmpPushNamingType"
    ]
    """<p>The naming type. If you specify it, it must match the naming configuration.</p>"""
    naming_configuration: "capo_mediaconnect.types.rtmp_push_naming_configuration.RtmpPushNamingConfiguration"
    """<p>The configuration settings for the application and stream names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpPushRouterInputConfiguration) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    if "naming_type" in value:
        import capo_mediaconnect.types.rtmp_push_naming_type

        out["namingType"] = (
            capo_mediaconnect.types.rtmp_push_naming_type.serialize_json(
                value["naming_type"]
            )
        )
    import capo_mediaconnect.types.rtmp_push_naming_configuration

    out["namingConfiguration"] = (
        capo_mediaconnect.types.rtmp_push_naming_configuration.serialize_json(
            value["naming_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RtmpPushRouterInputConfiguration:
    out: RtmpPushRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    if data.get("namingType") is not None:
        import capo_mediaconnect.types.rtmp_push_naming_type

        out["naming_type"] = (
            capo_mediaconnect.types.rtmp_push_naming_type.deserialize_json(
                data["namingType"]
            )
        )
    if data.get("namingConfiguration") is not None:
        import capo_mediaconnect.types.rtmp_push_naming_configuration

        out["naming_configuration"] = (
            capo_mediaconnect.types.rtmp_push_naming_configuration.deserialize_json(
                data["namingConfiguration"]
            )
        )
    else:
        out["naming_configuration"] = {"$unknown": {"name": ""}}
    return out
