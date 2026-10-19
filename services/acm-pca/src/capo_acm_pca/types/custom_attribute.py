"""Generated from Smithy shape ``com.amazonaws.acmpca#CustomAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.custom_object_identifier
    import capo_acm_pca.types.string1_to256


class CustomAttribute(TypedDict, closed=True):
    object_identifier: (
        "capo_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    )
    """<p>Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).</p>"""
    value: "capo_acm_pca.types.string1_to256.String1To256"
    """<p/> <p>Specifies the attribute value of relative distinguished name (RDN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomAttribute) -> dict:
    out: dict = {}
    out["ObjectIdentifier"] = value["object_identifier"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomAttribute:
    out: CustomAttribute = {}  # type: ignore[typeddict-item]
    if data.get("ObjectIdentifier") is not None:
        out["object_identifier"] = data["ObjectIdentifier"]
    else:
        out["object_identifier"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
