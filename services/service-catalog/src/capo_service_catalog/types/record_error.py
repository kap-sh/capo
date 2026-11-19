"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.error_code
    import capo_service_catalog.types.error_description


class RecordError(TypedDict, closed=True):
    code: NotRequired["capo_service_catalog.types.error_code.ErrorCode"]
    """<p>The numeric value of the error.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.error_description.ErrorDescription"
    ]
    """<p>The description of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordError) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordError:
    out: RecordError = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecordError) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> RecordError:
    out: RecordError = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
