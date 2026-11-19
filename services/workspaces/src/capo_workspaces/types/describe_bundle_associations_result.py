"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeBundleAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.bundle_resource_association_list


class DescribeBundleAssociationsResult(TypedDict, closed=True):
    associations: NotRequired[
        "capo_workspaces.types.bundle_resource_association_list.BundleResourceAssociationList"
    ]
    """<p>List of information about the specified associations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBundleAssociationsResult) -> dict:
    out: dict = {}
    if "associations" in value:
        import capo_workspaces.types.bundle_resource_association_list

        out["Associations"] = (
            capo_workspaces.types.bundle_resource_association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBundleAssociationsResult:
    out: DescribeBundleAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Associations") is not None:
        import capo_workspaces.types.bundle_resource_association_list

        out["associations"] = (
            capo_workspaces.types.bundle_resource_association_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeBundleAssociationsResult) -> dict:
    out: dict = {}
    if "associations" in value:
        import capo_workspaces.types.bundle_resource_association_list

        out["Associations"] = (
            capo_workspaces.types.bundle_resource_association_list.serialize_cbor(
                value["associations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeBundleAssociationsResult:
    out: DescribeBundleAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Associations") is not None:
        import capo_workspaces.types.bundle_resource_association_list

        out["associations"] = (
            capo_workspaces.types.bundle_resource_association_list.deserialize_cbor(
                data["Associations"]
            )
        )
    return out
