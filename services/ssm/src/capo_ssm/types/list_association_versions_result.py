"""Generated from Smithy shape ``com.amazonaws.ssm#ListAssociationVersionsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_version_list
    import capo_ssm.types.next_token


class ListAssociationVersionsResult(TypedDict, closed=True):
    association_versions: NotRequired[
        "capo_ssm.types.association_version_list.AssociationVersionList"
    ]
    """<p>Information about all versions of the association for the specified association ID.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssociationVersionsResult) -> dict:
    out: dict = {}
    if "association_versions" in value:
        import capo_ssm.types.association_version_list

        out["AssociationVersions"] = (
            capo_ssm.types.association_version_list.serialize_aws_json_1_1(
                value["association_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssociationVersionsResult:
    out: ListAssociationVersionsResult = {}  # type: ignore[typeddict-item]
    if data.get("AssociationVersions") is not None:
        import capo_ssm.types.association_version_list

        out["association_versions"] = (
            capo_ssm.types.association_version_list.deserialize_aws_json_1_1(
                data["AssociationVersions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAssociationVersionsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "association_versions" in value:
        import capo_ssm.types.association_version_list

        out["association_versions"] = (
            capo_ssm.types.association_version_list.redact_sensitive(
                value["association_versions"]
            )
        )
    return out
