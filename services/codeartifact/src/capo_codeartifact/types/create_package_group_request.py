"""Generated from Smithy shape ``com.amazonaws.codeartifact#CreatePackageGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.description
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.package_group_contact_info
    import capo_codeartifact.types.package_group_pattern
    import capo_codeartifact.types.tag_list


class CreatePackageGroupRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain in which you want to create a package group. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern"
    """<p>The pattern of the package group to create. The pattern is also the identifier of the package group. </p>"""
    contact_info: NotRequired[
        "capo_codeartifact.types.package_group_contact_info.PackageGroupContactInfo"
    ]
    """<p> The contact information for the created package group. </p>"""
    description: NotRequired["capo_codeartifact.types.description.Description"]
    """<p> A description of the package group. </p>"""
    tags: NotRequired["capo_codeartifact.types.tag_list.TagList"]
    """<p>One or more tag key-value pairs for the package group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageGroupRequest) -> dict:
    out: dict = {}
    out["packageGroup"] = value["package_group"]
    if "contact_info" in value:
        out["contactInfo"] = value["contact_info"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_codeartifact.types.tag_list

        out["tags"] = capo_codeartifact.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePackageGroupRequest:
    out: CreatePackageGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("packageGroup") is not None:
        out["package_group"] = data["packageGroup"]
    else:
        out["package_group"] = ""
    if data.get("contactInfo") is not None:
        out["contact_info"] = data["contactInfo"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_codeartifact.types.tag_list

        out["tags"] = capo_codeartifact.types.tag_list.deserialize_json(data["tags"])
    return out
