"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateOrgEc2DeepInspectionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.path_list


class UpdateOrgEc2DeepInspectionConfigurationRequest(TypedDict, closed=True):
    org_package_paths: "capo_inspector2.types.path_list.PathList"
    """<p>The Amazon Inspector deep inspection custom paths you are adding for your organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOrgEc2DeepInspectionConfigurationRequest) -> dict:
    out: dict = {}
    import capo_inspector2.types.path_list

    out["orgPackagePaths"] = capo_inspector2.types.path_list.serialize_json(
        value["org_package_paths"]
    )
    return out


def deserialize_json(data: dict) -> UpdateOrgEc2DeepInspectionConfigurationRequest:
    out: UpdateOrgEc2DeepInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("orgPackagePaths") is not None:
        import capo_inspector2.types.path_list

        out["org_package_paths"] = capo_inspector2.types.path_list.deserialize_json(
            data["orgPackagePaths"]
        )
    else:
        out["org_package_paths"] = []
    return out
