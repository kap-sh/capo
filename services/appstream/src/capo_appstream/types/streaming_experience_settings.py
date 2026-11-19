"""Generated from Smithy shape ``com.amazonaws.appstream#StreamingExperienceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.preferred_protocol


class StreamingExperienceSettings(TypedDict, closed=True):
    preferred_protocol: NotRequired[
        "capo_appstream.types.preferred_protocol.PreferredProtocol"
    ]
    """<p>The preferred protocol that you want to use while streaming your application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamingExperienceSettings) -> dict:
    out: dict = {}
    if "preferred_protocol" in value:
        import capo_appstream.types.preferred_protocol

        out["PreferredProtocol"] = (
            capo_appstream.types.preferred_protocol.serialize_aws_json_1_1(
                value["preferred_protocol"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamingExperienceSettings:
    out: StreamingExperienceSettings = {}  # type: ignore[typeddict-item]
    if data.get("PreferredProtocol") is not None:
        import capo_appstream.types.preferred_protocol

        out["preferred_protocol"] = (
            capo_appstream.types.preferred_protocol.deserialize_aws_json_1_1(
                data["PreferredProtocol"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StreamingExperienceSettings) -> dict:
    out: dict = {}
    if "preferred_protocol" in value:
        import capo_appstream.types.preferred_protocol

        out["PreferredProtocol"] = (
            capo_appstream.types.preferred_protocol.serialize_cbor(
                value["preferred_protocol"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StreamingExperienceSettings:
    out: StreamingExperienceSettings = {}  # type: ignore[typeddict-item]
    if data.get("PreferredProtocol") is not None:
        import capo_appstream.types.preferred_protocol

        out["preferred_protocol"] = (
            capo_appstream.types.preferred_protocol.deserialize_cbor(
                data["PreferredProtocol"]
            )
        )
    return out
