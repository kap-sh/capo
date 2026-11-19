"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Constraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string


class Constraints(TypedDict, closed=True):
    multiple_dimension_selection: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Determines if buyers are allowed to select multiple dimensions in the rate card. The possible values are <code>Allowed</code> and <code>Disallowed</code>. The default value is <code>Allowed</code>.</p>"""
    quantity_configuration: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Determines if acceptors are allowed to configure quantity for each dimension in rate card. The possible values are <code>Allowed</code> and <code>Disallowed</code>. The default value is <code>Allowed</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Constraints) -> dict:
    out: dict = {}
    if "multiple_dimension_selection" in value:
        out["multipleDimensionSelection"] = value["multiple_dimension_selection"]
    if "quantity_configuration" in value:
        out["quantityConfiguration"] = value["quantity_configuration"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Constraints:
    out: Constraints = {}  # type: ignore[typeddict-item]
    if data.get("multipleDimensionSelection") is not None:
        out["multiple_dimension_selection"] = data["multipleDimensionSelection"]
    if data.get("quantityConfiguration") is not None:
        out["quantity_configuration"] = data["quantityConfiguration"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Constraints) -> dict:
    out: dict = {}
    if "multiple_dimension_selection" in value:
        out["multipleDimensionSelection"] = value["multiple_dimension_selection"]
    if "quantity_configuration" in value:
        out["quantityConfiguration"] = value["quantity_configuration"]
    return out


def deserialize_cbor(data: dict) -> Constraints:
    out: Constraints = {}  # type: ignore[typeddict-item]
    if data.get("multipleDimensionSelection") is not None:
        out["multiple_dimension_selection"] = data["multipleDimensionSelection"]
    if data.get("quantityConfiguration") is not None:
        out["quantity_configuration"] = data["quantityConfiguration"]
    return out
