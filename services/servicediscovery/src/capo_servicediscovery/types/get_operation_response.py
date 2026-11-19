"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.operation


class GetOperationResponse(TypedDict, closed=True):
    operation: NotRequired["capo_servicediscovery.types.operation.Operation"]
    """<p>A complex type that contains information about the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOperationResponse) -> dict:
    out: dict = {}
    if "operation" in value:
        import capo_servicediscovery.types.operation

        out["Operation"] = capo_servicediscovery.types.operation.serialize_aws_json_1_1(
            value["operation"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOperationResponse:
    out: GetOperationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Operation") is not None:
        import capo_servicediscovery.types.operation

        out["operation"] = (
            capo_servicediscovery.types.operation.deserialize_aws_json_1_1(
                data["Operation"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetOperationResponse) -> dict:
    out: dict = {}
    if "operation" in value:
        import capo_servicediscovery.types.operation

        out["Operation"] = capo_servicediscovery.types.operation.serialize_cbor(
            value["operation"]
        )
    return out


def deserialize_cbor(data: dict) -> GetOperationResponse:
    out: GetOperationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Operation") is not None:
        import capo_servicediscovery.types.operation

        out["operation"] = capo_servicediscovery.types.operation.deserialize_cbor(
            data["Operation"]
        )
    return out
