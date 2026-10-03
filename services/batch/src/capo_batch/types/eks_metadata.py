"""Generated from Smithy shape ``com.amazonaws.batch#EksMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_annotations_map
    import capo_batch.types.eks_labels_map
    import capo_batch.types.string


class EksMetadata(TypedDict, closed=True):
    labels: NotRequired["capo_batch.types.eks_labels_map.EksLabelsMap"]
    """<p>Key-value pairs used to identify, sort, and organize cube resources. Can contain up to 63 uppercase letters, lowercase letters, numbers, hyphens (-), and underscores (_). Labels can be added or modified at any time. Each resource can have multiple labels, but each key must be unique for a given object.</p>"""
    annotations: NotRequired["capo_batch.types.eks_annotations_map.EksAnnotationsMap"]
    """<p>Key-value pairs used to attach arbitrary, non-identifying metadata to Kubernetes objects. Valid annotation keys have two segments: an optional prefix and a name, separated by a slash (/). </p> <ul> <li> <p>The prefix is optional and must be 253 characters or less. If specified, the prefix must be a DNS subdomain− a series of DNS labels separated by dots (.), and it must end with a slash (/).</p> </li> <li> <p>The name segment is required and must be 63 characters or less. It can include alphanumeric characters ([a-z0-9A-Z]), dashes (-), underscores (_), and dots (.), but must begin and end with an alphanumeric character.</p> </li> </ul> <note> <p>Annotation values must be 255 characters or less.</p> </note> <p>Annotations can be added or modified at any time. Each resource can have multiple annotations. </p>"""
    namespace: NotRequired["capo_batch.types.string.String"]
    """<p>The namespace of the Amazon EKS cluster. In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Batch places Batch Job pods in this namespace. If this field is provided, the value can't be empty or null. It must meet the following requirements:</p> <ul> <li> <p>1-63 characters long</p> </li> <li> <p>Can't be set to default</p> </li> <li> <p>Can't start with <code>kube</code> </p> </li> <li> <p>Must match the following regular expression: <code>^[a-z0-9]([-a-z0-9]*[a-z0-9])?$</code> </p> </li> </ul> <p> For more information, see <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Namespaces</a> in the <i>Kubernetes documentation</i>. This namespace can be different from the <code>kubernetesNamespace</code> set in the compute environment's <code>EksConfiguration</code>, but must have identical role-based access control (RBAC) roles as the compute environment's <code>kubernetesNamespace</code>. For multi-node parallel jobs, the same value must be provided across all the node ranges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksMetadata) -> dict:
    out: dict = {}
    if "labels" in value:
        import capo_batch.types.eks_labels_map

        out["labels"] = capo_batch.types.eks_labels_map.serialize_json(value["labels"])
    if "annotations" in value:
        import capo_batch.types.eks_annotations_map

        out["annotations"] = capo_batch.types.eks_annotations_map.serialize_json(
            value["annotations"]
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> EksMetadata:
    out: EksMetadata = {}  # type: ignore[typeddict-item]
    if data.get("labels") is not None:
        import capo_batch.types.eks_labels_map

        out["labels"] = capo_batch.types.eks_labels_map.deserialize_json(data["labels"])
    if data.get("annotations") is not None:
        import capo_batch.types.eks_annotations_map

        out["annotations"] = capo_batch.types.eks_annotations_map.deserialize_json(
            data["annotations"]
        )
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    return out
