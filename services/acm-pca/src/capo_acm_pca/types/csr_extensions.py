"""Generated from Smithy shape ``com.amazonaws.acmpca#CsrExtensions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.access_description_list
    import capo_acm_pca.types.key_usage


class CsrExtensions(TypedDict, closed=True):
    key_usage: NotRequired["capo_acm_pca.types.key_usage.KeyUsage"]
    """<p>Indicates the purpose of the certificate and of the key contained in the certificate.</p>"""
    subject_information_access: NotRequired[
        "capo_acm_pca.types.access_description_list.AccessDescriptionList"
    ]
    """<p>For CA certificates, provides a path to additional information pertaining to the CA, such as revocation and policy. For more information, see <a href="https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.2">Subject Information Access</a> in RFC 5280.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CsrExtensions) -> dict:
    out: dict = {}
    if "key_usage" in value:
        import capo_acm_pca.types.key_usage

        out["KeyUsage"] = capo_acm_pca.types.key_usage.serialize_aws_json_1_1(
            value["key_usage"]
        )
    if "subject_information_access" in value:
        import capo_acm_pca.types.access_description_list

        out["SubjectInformationAccess"] = (
            capo_acm_pca.types.access_description_list.serialize_aws_json_1_1(
                value["subject_information_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CsrExtensions:
    out: CsrExtensions = {}  # type: ignore[typeddict-item]
    if data.get("KeyUsage") is not None:
        import capo_acm_pca.types.key_usage

        out["key_usage"] = capo_acm_pca.types.key_usage.deserialize_aws_json_1_1(
            data["KeyUsage"]
        )
    if data.get("SubjectInformationAccess") is not None:
        import capo_acm_pca.types.access_description_list

        out["subject_information_access"] = (
            capo_acm_pca.types.access_description_list.deserialize_aws_json_1_1(
                data["SubjectInformationAccess"]
            )
        )
    return out
