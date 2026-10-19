"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ConfluentPublicRegistryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.connection_arn


class ConfluentPublicRegistryConfiguration(TypedDict, closed=True):
    connection_arn: "capo_eventbridgev2.types.connection_arn.ConnectionArn"
    """EventBridge Connection ARN that provides API Key or OAuth credentials for the registry."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfluentPublicRegistryConfiguration) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    return out


def deserialize_cbor(data: dict) -> ConfluentPublicRegistryConfiguration:
    out: ConfluentPublicRegistryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        out["connection_arn"] = ""
    return out
