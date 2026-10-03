"""Generated from Smithy shape ``com.amazonaws.iam#ListPolicyVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.policy_document_version_list_type
    import capo_iam.types.response_marker_type


class ListPolicyVersionsResponse(TypedDict, closed=True):
    versions: NotRequired[
        "capo_iam.types.policy_document_version_list_type.policyDocumentVersionListType"
    ]
    """<p>A list of policy versions.</p> <p>For more information about managed policy versions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html">Versioning for managed policies</a> in the <i>IAM User Guide</i>.</p>"""
    is_truncated: "capo_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["capo_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPolicyVersionsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "versions" in value:
        import capo_iam.types.policy_document_version_list_type

        capo_iam.types.policy_document_version_list_type.serialize_query(
            value["versions"], pairs, f"{key_prefix}Versions"
        )
    pairs.append(
        (
            f"{key_prefix}IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> ListPolicyVersionsResponse:
    out: ListPolicyVersionsResponse = {}  # type: ignore[typeddict-item]
    child_versions = el.find("Versions")
    if child_versions is not None:
        import capo_iam.types.policy_document_version_list_type

        out["versions"] = (
            capo_iam.types.policy_document_version_list_type.deserialize_query(
                child_versions
            )
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
