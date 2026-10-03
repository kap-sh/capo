"""Generated from Smithy shape ``com.amazonaws.acmpca#AccessMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.access_method_type
    import capo_acm_pca.types.custom_object_identifier


class AccessMethod(TypedDict, closed=True):
    custom_object_identifier: NotRequired[
        "capo_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    ]
    """<p>An object identifier (OID) specifying the <code>AccessMethod</code>. The OID must satisfy the regular expression shown below. For more information, see NIST's definition of <a href="https://csrc.nist.gov/glossary/term/Object_Identifier">Object Identifier (OID)</a>.</p>"""
    access_method_type: NotRequired[
        "capo_acm_pca.types.access_method_type.AccessMethodType"
    ]
    """<p>Specifies the <code>AccessMethod</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessMethod) -> dict:
    out: dict = {}
    if "custom_object_identifier" in value:
        out["CustomObjectIdentifier"] = value["custom_object_identifier"]
    if "access_method_type" in value:
        import capo_acm_pca.types.access_method_type

        out["AccessMethodType"] = (
            capo_acm_pca.types.access_method_type.serialize_aws_json_1_1(
                value["access_method_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessMethod:
    out: AccessMethod = {}  # type: ignore[typeddict-item]
    if data.get("CustomObjectIdentifier") is not None:
        out["custom_object_identifier"] = data["CustomObjectIdentifier"]
    if data.get("AccessMethodType") is not None:
        import capo_acm_pca.types.access_method_type

        out["access_method_type"] = (
            capo_acm_pca.types.access_method_type.deserialize_aws_json_1_1(
                data["AccessMethodType"]
            )
        )
    return out
