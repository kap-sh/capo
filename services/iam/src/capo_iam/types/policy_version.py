"""Generated from Smithy shape ``com.amazonaws.iam#PolicyVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.date_type
    import capo_iam.types.policy_document_type
    import capo_iam.types.policy_version_id_type


class PolicyVersion(TypedDict, closed=True):
    document: NotRequired["capo_iam.types.policy_document_type.policyDocumentType"]
    """<p>The policy document.</p> <p>The policy document is returned in the response to the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicyVersion.html">GetPolicyVersion</a> and <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html">GetAccountAuthorizationDetails</a> operations. It is not returned in the response to the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicyVersion.html">CreatePolicyVersion</a> or <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicyVersions.html">ListPolicyVersions</a> operations. </p> <p>The policy document returned in this structure is URL-encoded compliant with <a href="https://tools.ietf.org/html/rfc3986">RFC 3986</a>. You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the <code>decode</code> method of the <code>java.net.URLDecoder</code> utility class in the Java SDK. Other languages and SDKs provide similar functionality.</p>"""
    version_id: NotRequired["capo_iam.types.policy_version_id_type.policyVersionIdType"]
    """<p>The identifier for the policy version.</p> <p>Policy version identifiers always begin with <code>v</code> (always lowercase). When a policy is created, the first policy version is <code>v1</code>. </p>"""
    is_default_version: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether the policy version is set as the policy's default version.</p>"""
    create_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the policy version was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "document" in value:
        pairs.append((f"{key_prefix}Document", str(value["document"])))
    if "version_id" in value:
        pairs.append((f"{key_prefix}VersionId", str(value["version_id"])))
    pairs.append(
        (
            f"{key_prefix}IsDefaultVersion",
            "true" if value.get("is_default_version", False) else "false",
        )
    )
    if "create_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )


def deserialize_query(el: Element) -> PolicyVersion:
    out: PolicyVersion = {}  # type: ignore[typeddict-item]
    child_document = el.find("Document")
    if child_document is not None:
        out["document"] = str(child_document.text or "")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    child_is_default_version = el.find("IsDefaultVersion")
    if child_is_default_version is not None:
        out["is_default_version"] = (
            child_is_default_version.text or ""
        ).lower() == "true"
    else:
        out["is_default_version"] = False
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    return out
