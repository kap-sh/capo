"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EksSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.eks_label_selector
    import capo_resiliencehubv2.types.eks_namespace_list


class EksSource(TypedDict, closed=True):
    cluster_arn: "capo_resiliencehubv2.types.arn.Arn"
    namespaces: "capo_resiliencehubv2.types.eks_namespace_list.EksNamespaceList"
    """<p>The list of Kubernetes namespaces within the EKS cluster.</p>"""
    label_selector: NotRequired[
        "capo_resiliencehubv2.types.eks_label_selector.EksLabelSelector"
    ]
    """<p>Filters discovery to the Kubernetes objects whose labels match the selector. When omitted, all supported objects in the specified namespaces are discovered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksSource) -> dict:
    out: dict = {}
    out["clusterArn"] = value["cluster_arn"]
    import capo_resiliencehubv2.types.eks_namespace_list

    out["namespaces"] = capo_resiliencehubv2.types.eks_namespace_list.serialize_json(
        value["namespaces"]
    )
    if "label_selector" in value:
        import capo_resiliencehubv2.types.eks_label_selector

        out["labelSelector"] = (
            capo_resiliencehubv2.types.eks_label_selector.serialize_json(
                value["label_selector"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksSource:
    out: EksSource = {}  # type: ignore[typeddict-item]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        raise DeserializationError("EksSource.cluster_arn required")
    if data.get("namespaces") is not None:
        import capo_resiliencehubv2.types.eks_namespace_list

        out["namespaces"] = (
            capo_resiliencehubv2.types.eks_namespace_list.deserialize_json(
                data["namespaces"]
            )
        )
    else:
        raise DeserializationError("EksSource.namespaces required")
    if data.get("labelSelector") is not None:
        import capo_resiliencehubv2.types.eks_label_selector

        out["label_selector"] = (
            capo_resiliencehubv2.types.eks_label_selector.deserialize_json(
                data["labelSelector"]
            )
        )
    return out


def redact_sensitive(value: EksSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "label_selector" in value:
        import capo_resiliencehubv2.types.eks_label_selector

        out["label_selector"] = (
            capo_resiliencehubv2.types.eks_label_selector.redact_sensitive(
                value["label_selector"]
            )
        )
    return out
