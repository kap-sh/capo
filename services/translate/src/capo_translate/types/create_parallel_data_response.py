"""Generated from Smithy shape ``com.amazonaws.translate#CreateParallelDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.parallel_data_status
    import capo_translate.types.resource_name


class CreateParallelDataResponse(TypedDict, closed=True):
    name: NotRequired["capo_translate.types.resource_name.ResourceName"]
    """<p>The custom name that you assigned to the parallel data resource.</p>"""
    status: NotRequired["capo_translate.types.parallel_data_status.ParallelDataStatus"]
    """<p>The status of the parallel data resource. When the resource is ready for you to use, the status is <code>ACTIVE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateParallelDataResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_translate.types.parallel_data_status

        out["Status"] = (
            capo_translate.types.parallel_data_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateParallelDataResponse:
    out: CreateParallelDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_translate.types.parallel_data_status

        out["status"] = (
            capo_translate.types.parallel_data_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateParallelDataResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_translate.types.parallel_data_status

        out["Status"] = capo_translate.types.parallel_data_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateParallelDataResponse:
    out: CreateParallelDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_translate.types.parallel_data_status

        out["status"] = capo_translate.types.parallel_data_status.deserialize_cbor(
            data["Status"]
        )
    return out
