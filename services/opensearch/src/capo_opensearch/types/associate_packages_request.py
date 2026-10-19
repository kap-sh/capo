"""Generated from Smithy shape ``com.amazonaws.opensearch#AssociatePackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.package_details_for_association_list


class AssociatePackagesRequest(TypedDict, closed=True):
    package_list: "capo_opensearch.types.package_details_for_association_list.PackageDetailsForAssociationList"
    """<p>A list of packages and their prerequisites to be associated with a domain.</p>"""
    domain_name: "capo_opensearch.types.domain_name.DomainName"


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePackagesRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.package_details_for_association_list

    out["PackageList"] = (
        capo_opensearch.types.package_details_for_association_list.serialize_json(
            value["package_list"]
        )
    )
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> AssociatePackagesRequest:
    out: AssociatePackagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("PackageList") is not None:
        import capo_opensearch.types.package_details_for_association_list

        out["package_list"] = (
            capo_opensearch.types.package_details_for_association_list.deserialize_json(
                data["PackageList"]
            )
        )
    else:
        out["package_list"] = []
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    return out
