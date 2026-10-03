"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateEc2DeepInspectionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.path_list


class UpdateEc2DeepInspectionConfigurationRequest(TypedDict, closed=True):
    activate_deep_inspection: NotRequired["bool"]
    """<p>Specify <code>TRUE</code> to activate Amazon Inspector deep inspection in your account, or <code>FALSE</code> to deactivate. Member accounts in an organization cannot deactivate deep inspection, instead the delegated administrator for the organization can deactivate a member account using <a href="https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html">BatchUpdateMemberEc2DeepInspectionStatus</a>.</p>"""
    package_paths: NotRequired["capo_inspector2.types.path_list.PathList"]
    """<p>The Amazon Inspector deep inspection custom paths you are adding for your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEc2DeepInspectionConfigurationRequest) -> dict:
    out: dict = {}
    if "activate_deep_inspection" in value:
        out["activateDeepInspection"] = value["activate_deep_inspection"]
    if "package_paths" in value:
        import capo_inspector2.types.path_list

        out["packagePaths"] = capo_inspector2.types.path_list.serialize_json(
            value["package_paths"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEc2DeepInspectionConfigurationRequest:
    out: UpdateEc2DeepInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("activateDeepInspection") is not None:
        out["activate_deep_inspection"] = data["activateDeepInspection"]
    if data.get("packagePaths") is not None:
        import capo_inspector2.types.path_list

        out["package_paths"] = capo_inspector2.types.path_list.deserialize_json(
            data["packagePaths"]
        )
    return out
