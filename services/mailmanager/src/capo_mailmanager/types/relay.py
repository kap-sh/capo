"""Generated from Smithy shape ``com.amazonaws.mailmanager#Relay``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.relay_id
    import capo_mailmanager.types.relay_name


class Relay(TypedDict, closed=True):
    relay_id: NotRequired["capo_mailmanager.types.relay_id.RelayId"]
    """<p>The unique relay identifier.</p>"""
    relay_name: NotRequired["capo_mailmanager.types.relay_name.RelayName"]
    """<p>The unique relay name.</p>"""
    last_modified_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the relay was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Relay) -> dict:
    out: dict = {}
    if "relay_id" in value:
        out["RelayId"] = value["relay_id"]
    if "relay_name" in value:
        out["RelayName"] = value["relay_name"]
    if "last_modified_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["LastModifiedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_modified_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Relay:
    out: Relay = {}  # type: ignore[typeddict-item]
    if data.get("RelayId") is not None:
        out["relay_id"] = data["RelayId"]
    if data.get("RelayName") is not None:
        out["relay_name"] = data["RelayName"]
    if data.get("LastModifiedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_modified_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastModifiedTimestamp"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Relay) -> dict:
    out: dict = {}
    if "relay_id" in value:
        out["RelayId"] = value["relay_id"]
    if "relay_name" in value:
        out["RelayName"] = value["relay_name"]
    if "last_modified_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["LastModifiedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_cbor(
                value["last_modified_timestamp"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Relay:
    out: Relay = {}  # type: ignore[typeddict-item]
    if data.get("RelayId") is not None:
        out["relay_id"] = data["RelayId"]
    if data.get("RelayName") is not None:
        out["relay_name"] = data["RelayName"]
    if data.get("LastModifiedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_modified_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_cbor(
                data["LastModifiedTimestamp"]
            )
        )
    return out
