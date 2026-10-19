"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleResourcePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.action_list
    import capo_quicksight.types.asset_bundle_principal_list


class AssetBundleResourcePermissions(TypedDict, closed=True):
    principals: (
        "capo_quicksight.types.asset_bundle_principal_list.AssetBundlePrincipalList"
    )
    """<p>A list of principals to grant permissions on.</p>"""
    actions: "capo_quicksight.types.action_list.ActionList"
    """<p>A list of IAM actions to grant permissions on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleResourcePermissions) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_principal_list

    out["Principals"] = (
        capo_quicksight.types.asset_bundle_principal_list.serialize_json(
            value["principals"]
        )
    )
    import capo_quicksight.types.action_list

    out["Actions"] = capo_quicksight.types.action_list.serialize_json(value["actions"])
    return out


def deserialize_json(data: dict) -> AssetBundleResourcePermissions:
    out: AssetBundleResourcePermissions = {}  # type: ignore[typeddict-item]
    if data.get("Principals") is not None:
        import capo_quicksight.types.asset_bundle_principal_list

        out["principals"] = (
            capo_quicksight.types.asset_bundle_principal_list.deserialize_json(
                data["Principals"]
            )
        )
    else:
        out["principals"] = []
    if data.get("Actions") is not None:
        import capo_quicksight.types.action_list

        out["actions"] = capo_quicksight.types.action_list.deserialize_json(
            data["Actions"]
        )
    else:
        out["actions"] = []
    return out
