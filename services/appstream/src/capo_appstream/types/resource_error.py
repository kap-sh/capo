"""Generated from Smithy shape ``com.amazonaws.appstream#ResourceError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.fleet_error_code
    import capo_appstream.types.string
    import capo_appstream.types.timestamp


class ResourceError(TypedDict, closed=True):
    error_code: NotRequired["capo_appstream.types.fleet_error_code.FleetErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired["capo_appstream.types.string.String"]
    """<p>The error message.</p>"""
    error_timestamp: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The time the error occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_appstream.types.fleet_error_code

        out["ErrorCode"] = capo_appstream.types.fleet_error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_timestamp" in value:
        import capo_appstream.types.timestamp

        out["ErrorTimestamp"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["error_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceError:
    out: ResourceError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_appstream.types.fleet_error_code

        out["error_code"] = (
            capo_appstream.types.fleet_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ErrorTimestamp") is not None:
        import capo_appstream.types.timestamp

        out["error_timestamp"] = (
            capo_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["ErrorTimestamp"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_appstream.types.fleet_error_code

        out["ErrorCode"] = capo_appstream.types.fleet_error_code.serialize_cbor(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_timestamp" in value:
        import capo_appstream.types.timestamp

        out["ErrorTimestamp"] = capo_appstream.types.timestamp.serialize_cbor(
            value["error_timestamp"]
        )
    return out


def deserialize_cbor(data: dict) -> ResourceError:
    out: ResourceError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_appstream.types.fleet_error_code

        out["error_code"] = capo_appstream.types.fleet_error_code.deserialize_cbor(
            data["ErrorCode"]
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ErrorTimestamp") is not None:
        import capo_appstream.types.timestamp

        out["error_timestamp"] = capo_appstream.types.timestamp.deserialize_cbor(
            data["ErrorTimestamp"]
        )
    return out
