"""Generated from Smithy shape ``com.amazonaws.acmpca#OtherName``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.custom_object_identifier
    import capo_acm_pca.types.string256


class OtherName(TypedDict, closed=True):
    type_id: "capo_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    """<p>Specifies an OID. </p>"""
    value: "capo_acm_pca.types.string256.String256"
    """<p>Specifies an OID value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OtherName) -> dict:
    out: dict = {}
    out["TypeId"] = value["type_id"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OtherName:
    out: OtherName = {}  # type: ignore[typeddict-item]
    if data.get("TypeId") is not None:
        out["type_id"] = data["TypeId"]
    else:
        out["type_id"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
