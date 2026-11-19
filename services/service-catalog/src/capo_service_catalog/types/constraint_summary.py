"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ConstraintSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.constraint_description
    import capo_service_catalog.types.constraint_type


class ConstraintSummary(TypedDict, closed=True):
    type: NotRequired["capo_service_catalog.types.constraint_type.ConstraintType"]
    """<p>The type of constraint.</p> <ul> <li> <p> <code>LAUNCH</code> </p> </li> <li> <p> <code>NOTIFICATION</code> </p> </li> <li> <p>STACKSET</p> </li> <li> <p> <code>TEMPLATE</code> </p> </li> </ul>"""
    description: NotRequired[
        "capo_service_catalog.types.constraint_description.ConstraintDescription"
    ]
    """<p>The description of the constraint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConstraintSummary) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConstraintSummary:
    out: ConstraintSummary = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConstraintSummary) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> ConstraintSummary:
    out: ConstraintSummary = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
