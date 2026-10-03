"""Generated from Smithy shape ``com.amazonaws.eks#DescribeAddonConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.addon_pod_identity_configuration_list
    import capo_eks.types.string


class DescribeAddonConfigurationResponse(TypedDict, closed=True):
    addon_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the add-on.</p>"""
    addon_version: NotRequired["capo_eks.types.string.String"]
    """<p>The version of the add-on. The version must match one of the versions returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html"> <code>DescribeAddonVersions</code> </a>.</p>"""
    configuration_schema: NotRequired["capo_eks.types.string.String"]
    """<p>A JSON schema that's used to validate the configuration values you provide when an add-on is created or updated.</p>"""
    pod_identity_configuration: NotRequired[
        "capo_eks.types.addon_pod_identity_configuration_list.AddonPodIdentityConfigurationList"
    ]
    """<p>The Kubernetes service account name used by the add-on, and any suggested IAM policies. Use this information to create an IAM Role for the add-on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAddonConfigurationResponse) -> dict:
    out: dict = {}
    if "addon_name" in value:
        out["addonName"] = value["addon_name"]
    if "addon_version" in value:
        out["addonVersion"] = value["addon_version"]
    if "configuration_schema" in value:
        out["configurationSchema"] = value["configuration_schema"]
    if "pod_identity_configuration" in value:
        import capo_eks.types.addon_pod_identity_configuration_list

        out["podIdentityConfiguration"] = (
            capo_eks.types.addon_pod_identity_configuration_list.serialize_json(
                value["pod_identity_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAddonConfigurationResponse:
    out: DescribeAddonConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("addonName") is not None:
        out["addon_name"] = data["addonName"]
    if data.get("addonVersion") is not None:
        out["addon_version"] = data["addonVersion"]
    if data.get("configurationSchema") is not None:
        out["configuration_schema"] = data["configurationSchema"]
    if data.get("podIdentityConfiguration") is not None:
        import capo_eks.types.addon_pod_identity_configuration_list

        out["pod_identity_configuration"] = (
            capo_eks.types.addon_pod_identity_configuration_list.deserialize_json(
                data["podIdentityConfiguration"]
            )
        )
    return out
