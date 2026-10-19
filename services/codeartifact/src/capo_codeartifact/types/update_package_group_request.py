"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpdatePackageGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.description
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.package_group_contact_info
    import capo_codeartifact.types.package_group_pattern


class UpdatePackageGroupRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain which contains the package group to be updated. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern"
    """<p> The pattern of the package group to be updated. </p>"""
    contact_info: NotRequired[
        "capo_codeartifact.types.package_group_contact_info.PackageGroupContactInfo"
    ]
    """<p> Contact information which you want to update the requested package group with. </p>"""
    description: NotRequired["capo_codeartifact.types.description.Description"]
    """<p> The description you want to update the requested package group with. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageGroupRequest) -> dict:
    out: dict = {}
    out["packageGroup"] = value["package_group"]
    if "contact_info" in value:
        out["contactInfo"] = value["contact_info"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdatePackageGroupRequest:
    out: UpdatePackageGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("packageGroup") is not None:
        out["package_group"] = data["packageGroup"]
    else:
        out["package_group"] = ""
    if data.get("contactInfo") is not None:
        out["contact_info"] = data["contactInfo"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
