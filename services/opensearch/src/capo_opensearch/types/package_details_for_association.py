"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageDetailsForAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.package_association_configuration
    import capo_opensearch.types.package_id
    import capo_opensearch.types.package_id_list


class PackageDetailsForAssociation(TypedDict, closed=True):
    package_id: "capo_opensearch.types.package_id.PackageID"
    """<p>Internal ID of the package that you want to associate with a domain.</p>"""
    prerequisite_package_id_list: NotRequired[
        "capo_opensearch.types.package_id_list.PackageIDList"
    ]
    """<p>List of package IDs that must be linked to the domain before or simultaneously with the package association.</p>"""
    association_configuration: NotRequired[
        "capo_opensearch.types.package_association_configuration.PackageAssociationConfiguration"
    ]
    """<p>The configuration parameters for associating the package with a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageDetailsForAssociation) -> dict:
    out: dict = {}
    out["PackageID"] = value["package_id"]
    if "prerequisite_package_id_list" in value:
        import capo_opensearch.types.package_id_list

        out["PrerequisitePackageIDList"] = (
            capo_opensearch.types.package_id_list.serialize_json(
                value["prerequisite_package_id_list"]
            )
        )
    if "association_configuration" in value:
        import capo_opensearch.types.package_association_configuration

        out["AssociationConfiguration"] = (
            capo_opensearch.types.package_association_configuration.serialize_json(
                value["association_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageDetailsForAssociation:
    out: PackageDetailsForAssociation = {}  # type: ignore[typeddict-item]
    if data.get("PackageID") is not None:
        out["package_id"] = data["PackageID"]
    else:
        out["package_id"] = ""
    if data.get("PrerequisitePackageIDList") is not None:
        import capo_opensearch.types.package_id_list

        out["prerequisite_package_id_list"] = (
            capo_opensearch.types.package_id_list.deserialize_json(
                data["PrerequisitePackageIDList"]
            )
        )
    if data.get("AssociationConfiguration") is not None:
        import capo_opensearch.types.package_association_configuration

        out["association_configuration"] = (
            capo_opensearch.types.package_association_configuration.deserialize_json(
                data["AssociationConfiguration"]
            )
        )
    return out
