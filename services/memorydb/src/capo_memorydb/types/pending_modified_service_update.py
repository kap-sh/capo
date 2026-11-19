"""Generated from Smithy shape ``com.amazonaws.memorydb#PendingModifiedServiceUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.service_update_status
    import capo_memorydb.types.string


class PendingModifiedServiceUpdate(TypedDict, closed=True):
    service_update_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The unique ID of the service update</p>"""
    status: NotRequired["capo_memorydb.types.service_update_status.ServiceUpdateStatus"]
    """<p>The status of the service update</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingModifiedServiceUpdate) -> dict:
    out: dict = {}
    if "service_update_name" in value:
        out["ServiceUpdateName"] = value["service_update_name"]
    if "status" in value:
        import capo_memorydb.types.service_update_status

        out["Status"] = (
            capo_memorydb.types.service_update_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PendingModifiedServiceUpdate:
    out: PendingModifiedServiceUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ServiceUpdateName") is not None:
        out["service_update_name"] = data["ServiceUpdateName"]
    if data.get("Status") is not None:
        import capo_memorydb.types.service_update_status

        out["status"] = (
            capo_memorydb.types.service_update_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PendingModifiedServiceUpdate) -> dict:
    out: dict = {}
    if "service_update_name" in value:
        out["ServiceUpdateName"] = value["service_update_name"]
    if "status" in value:
        import capo_memorydb.types.service_update_status

        out["Status"] = capo_memorydb.types.service_update_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> PendingModifiedServiceUpdate:
    out: PendingModifiedServiceUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ServiceUpdateName") is not None:
        out["service_update_name"] = data["ServiceUpdateName"]
    if data.get("Status") is not None:
        import capo_memorydb.types.service_update_status

        out["status"] = capo_memorydb.types.service_update_status.deserialize_cbor(
            data["Status"]
        )
    return out
