"""Generated from Smithy shape ``com.amazonaws.acmpca#CustomExtension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.base64_string1_to4096
    import capo_acm_pca.types.boolean
    import capo_acm_pca.types.custom_object_identifier


class CustomExtension(TypedDict, closed=True):
    object_identifier: (
        "capo_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    )
    """<p/> <p>Specifies the object identifier (OID) of the X.509 extension. For more information, see the <a href="https://oidref.com/2.5.29">Global OID reference database.</a> </p>"""
    value: "capo_acm_pca.types.base64_string1_to4096.Base64String1To4096"
    """<p/> <p>Specifies the base64-encoded value of the X.509 extension.</p>"""
    critical: NotRequired["capo_acm_pca.types.boolean.Boolean"]
    """<p/> <p>Specifies the critical flag of the X.509 extension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomExtension) -> dict:
    out: dict = {}
    out["ObjectIdentifier"] = value["object_identifier"]
    out["Value"] = value["value"]
    if "critical" in value:
        out["Critical"] = value["critical"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomExtension:
    out: CustomExtension = {}  # type: ignore[typeddict-item]
    if data.get("ObjectIdentifier") is not None:
        out["object_identifier"] = data["ObjectIdentifier"]
    else:
        raise DeserializationError("CustomExtension.object_identifier required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("CustomExtension.value required")
    if data.get("Critical") is not None:
        out["critical"] = data["Critical"]
    return out
