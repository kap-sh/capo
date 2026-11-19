"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.description
    import capo_service_catalog.types.output_key
    import capo_service_catalog.types.output_value


class RecordOutput(TypedDict, closed=True):
    output_key: NotRequired["capo_service_catalog.types.output_key.OutputKey"]
    """<p>The output key.</p>"""
    output_value: NotRequired["capo_service_catalog.types.output_value.OutputValue"]
    """<p>The output value.</p>"""
    description: NotRequired["capo_service_catalog.types.description.Description"]
    """<p>The description of the output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordOutput) -> dict:
    out: dict = {}
    if "output_key" in value:
        out["OutputKey"] = value["output_key"]
    if "output_value" in value:
        out["OutputValue"] = value["output_value"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordOutput:
    out: RecordOutput = {}  # type: ignore[typeddict-item]
    if data.get("OutputKey") is not None:
        out["output_key"] = data["OutputKey"]
    if data.get("OutputValue") is not None:
        out["output_value"] = data["OutputValue"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecordOutput) -> dict:
    out: dict = {}
    if "output_key" in value:
        out["OutputKey"] = value["output_key"]
    if "output_value" in value:
        out["OutputValue"] = value["output_value"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> RecordOutput:
    out: RecordOutput = {}  # type: ignore[typeddict-item]
    if data.get("OutputKey") is not None:
        out["output_key"] = data["OutputKey"]
    if data.get("OutputValue") is not None:
        out["output_value"] = data["OutputValue"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
