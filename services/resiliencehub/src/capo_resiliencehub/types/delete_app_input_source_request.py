"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteAppInputSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.client_token
    import capo_resiliencehub.types.eks_source_cluster_namespace
    import capo_resiliencehub.types.terraform_source


class DeleteAppInputSourceRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    source_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the imported resource you want to remove from the Resilience Hub application. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    terraform_source: NotRequired[
        "capo_resiliencehub.types.terraform_source.TerraformSource"
    ]
    """<p>The imported Terraform s3 state ﬁle you want to remove from the Resilience Hub application.</p>"""
    client_token: NotRequired["capo_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""
    eks_source_cluster_namespace: NotRequired[
        "capo_resiliencehub.types.eks_source_cluster_namespace.EksSourceClusterNamespace"
    ]
    """<p>The namespace on your Amazon Elastic Kubernetes Service cluster that you want to delete from the Resilience Hub application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppInputSourceRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "source_arn" in value:
        out["sourceArn"] = value["source_arn"]
    if "terraform_source" in value:
        import capo_resiliencehub.types.terraform_source

        out["terraformSource"] = (
            capo_resiliencehub.types.terraform_source.serialize_json(
                value["terraform_source"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "eks_source_cluster_namespace" in value:
        import capo_resiliencehub.types.eks_source_cluster_namespace

        out["eksSourceClusterNamespace"] = (
            capo_resiliencehub.types.eks_source_cluster_namespace.serialize_json(
                value["eks_source_cluster_namespace"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteAppInputSourceRequest:
    out: DeleteAppInputSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("DeleteAppInputSourceRequest.app_arn required")
    if data.get("sourceArn") is not None:
        out["source_arn"] = data["sourceArn"]
    if data.get("terraformSource") is not None:
        import capo_resiliencehub.types.terraform_source

        out["terraform_source"] = (
            capo_resiliencehub.types.terraform_source.deserialize_json(
                data["terraformSource"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("eksSourceClusterNamespace") is not None:
        import capo_resiliencehub.types.eks_source_cluster_namespace

        out["eks_source_cluster_namespace"] = (
            capo_resiliencehub.types.eks_source_cluster_namespace.deserialize_json(
                data["eksSourceClusterNamespace"]
            )
        )
    return out
