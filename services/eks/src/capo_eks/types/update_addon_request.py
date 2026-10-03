"""Generated from Smithy shape ``com.amazonaws.eks#UpdateAddonRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.addon_pod_identity_associations_list
    import capo_eks.types.cluster_name
    import capo_eks.types.resolve_conflicts
    import capo_eks.types.role_arn
    import capo_eks.types.string


class UpdateAddonRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.cluster_name.ClusterName"
    """<p>The name of your cluster.</p>"""
    addon_name: "capo_eks.types.string.String"
    """<p>The name of the add-on. The name must match one of the names returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html"> <code>ListAddons</code> </a>.</p>"""
    addon_version: NotRequired["capo_eks.types.string.String"]
    """<p>The version of the add-on. The version must match one of the versions returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html"> <code>DescribeAddonVersions</code> </a>.</p>"""
    service_account_role_arn: NotRequired["capo_eks.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an existing IAM role to bind to the add-on's service account. The role must be assigned the IAM permissions required by the add-on. If you don't specify an existing IAM role, then the add-on uses the permissions assigned to the node IAM role. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html">Amazon EKS node IAM role</a> in the <i>Amazon EKS User Guide</i>.</p> <note> <p>To specify an existing IAM role, you must have an IAM OpenID Connect (OIDC) provider created for your cluster. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html">Enabling IAM roles for service accounts on your cluster</a> in the <i>Amazon EKS User Guide</i>.</p> </note>"""
    resolve_conflicts: NotRequired["capo_eks.types.resolve_conflicts.ResolveConflicts"]
    """<p>How to resolve field value conflicts for an Amazon EKS add-on if you've changed a value from the Amazon EKS default value. Conflicts are handled based on the option you choose:</p> <ul> <li> <p> <b>None</b> – Amazon EKS doesn't change the value. The update might fail.</p> </li> <li> <p> <b>Overwrite</b> – Amazon EKS overwrites the changed value back to the Amazon EKS default value.</p> </li> <li> <p> <b>Preserve</b> – Amazon EKS preserves the value. If you choose this option, we recommend that you test any field and value changes on a non-production cluster before updating the add-on on your production cluster.</p> </li> </ul>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    configuration_values: NotRequired["capo_eks.types.string.String"]
    """<p>The set of configuration values for the add-on that's created. The values that you provide are validated against the schema returned by <code>DescribeAddonConfiguration</code>.</p>"""
    pod_identity_associations: NotRequired[
        "capo_eks.types.addon_pod_identity_associations_list.AddonPodIdentityAssociationsList"
    ]
    """<p>An array of EKS Pod Identity associations to be updated. Each association maps a Kubernetes service account to an IAM role. If this value is left blank, no change. If an empty array is provided, existing associations owned by the add-on are deleted.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html">Attach an IAM Role to an Amazon EKS add-on using EKS Pod Identity</a> in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAddonRequest) -> dict:
    out: dict = {}
    if "addon_version" in value:
        out["addonVersion"] = value["addon_version"]
    if "service_account_role_arn" in value:
        out["serviceAccountRoleArn"] = value["service_account_role_arn"]
    if "resolve_conflicts" in value:
        import capo_eks.types.resolve_conflicts

        out["resolveConflicts"] = capo_eks.types.resolve_conflicts.serialize_json(
            value["resolve_conflicts"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "configuration_values" in value:
        out["configurationValues"] = value["configuration_values"]
    if "pod_identity_associations" in value:
        import capo_eks.types.addon_pod_identity_associations_list

        out["podIdentityAssociations"] = (
            capo_eks.types.addon_pod_identity_associations_list.serialize_json(
                value["pod_identity_associations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAddonRequest:
    out: UpdateAddonRequest = {}  # type: ignore[typeddict-item]
    if data.get("addonVersion") is not None:
        out["addon_version"] = data["addonVersion"]
    if data.get("serviceAccountRoleArn") is not None:
        out["service_account_role_arn"] = data["serviceAccountRoleArn"]
    if data.get("resolveConflicts") is not None:
        import capo_eks.types.resolve_conflicts

        out["resolve_conflicts"] = capo_eks.types.resolve_conflicts.deserialize_json(
            data["resolveConflicts"]
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("configurationValues") is not None:
        out["configuration_values"] = data["configurationValues"]
    if data.get("podIdentityAssociations") is not None:
        import capo_eks.types.addon_pod_identity_associations_list

        out["pod_identity_associations"] = (
            capo_eks.types.addon_pod_identity_associations_list.deserialize_json(
                data["podIdentityAssociations"]
            )
        )
    return out
