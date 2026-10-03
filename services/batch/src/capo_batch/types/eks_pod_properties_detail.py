"""Generated from Smithy shape ``com.amazonaws.batch#EksPodPropertiesDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.eks_container_details
    import capo_batch.types.eks_metadata
    import capo_batch.types.eks_volumes
    import capo_batch.types.image_pull_secrets
    import capo_batch.types.string


class EksPodPropertiesDetail(TypedDict, closed=True):
    service_account_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the service account that's used to run the pod. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html">Kubernetes service accounts</a> and <a href="https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html">Configure a Kubernetes service account to assume an IAM role</a> in the <i>Amazon EKS User Guide</i> and <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/">Configure service accounts for pods</a> in the <i>Kubernetes documentation</i>.</p>"""
    host_network: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Indicates if the pod uses the hosts' network IP address. The default value is <code>true</code>. Setting this to <code>false</code> enables the Kubernetes pod networking model. Most Batch workloads are egress-only and don't require the overhead of IP allocation for each pod for incoming connections. For more information, see <a href="https://kubernetes.io/docs/concepts/security/pod-security-policy/#host-namespaces">Host namespaces</a> and <a href="https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking">Pod networking</a> in the <i>Kubernetes documentation</i>.</p>"""
    dns_policy: NotRequired["capo_batch.types.string.String"]
    """<p>The DNS policy for the pod. The default value is <code>ClusterFirst</code>. If the <code>hostNetwork</code> parameter is not specified, the default is <code>ClusterFirstWithHostNet</code>. <code>ClusterFirst</code> indicates that any DNS query that does not match the configured cluster domain suffix is forwarded to the upstream nameserver inherited from the node. If no value was specified for <code>dnsPolicy</code> in the <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html">RegisterJobDefinition</a> API operation, then no value will be returned for <code>dnsPolicy</code> by either of <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobDefinitions.html">DescribeJobDefinitions</a> or <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobs.html">DescribeJobs</a> API operations. The pod spec setting will contain either <code>ClusterFirst</code> or <code>ClusterFirstWithHostNet</code>, depending on the value of the <code>hostNetwork</code> parameter. For more information, see <a href="https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy">Pod's DNS policy</a> in the <i>Kubernetes documentation</i>.</p> <p>Valid values: <code>Default</code> | <code>ClusterFirst</code> | <code>ClusterFirstWithHostNet</code> </p>"""
    image_pull_secrets: NotRequired[
        "capo_batch.types.image_pull_secrets.ImagePullSecrets"
    ]
    """<p>Displays the reference pointer to the Kubernetes secret resource. These secrets help to gain access to pull an images from a private registry.</p>"""
    containers: NotRequired[
        "capo_batch.types.eks_container_details.EksContainerDetails"
    ]
    """<p>The properties of the container that's used on the Amazon EKS pod.</p>"""
    init_containers: NotRequired[
        "capo_batch.types.eks_container_details.EksContainerDetails"
    ]
    """<p>The container registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store.</p>"""
    volumes: NotRequired["capo_batch.types.eks_volumes.EksVolumes"]
    """<p>Specifies the volumes for a job definition using Amazon EKS resources.</p>"""
    pod_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the pod for this job.</p>"""
    node_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the node for this job.</p>"""
    metadata: NotRequired["capo_batch.types.eks_metadata.EksMetadata"]
    """<p>Describes and uniquely identifies Kubernetes resources. For example, the compute environment that a pod runs in or the <code>jobID</code> for a job running in the pod. For more information, see <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/">Understanding Kubernetes Objects</a> in the <i>Kubernetes documentation</i>.</p>"""
    share_process_namespace: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Indicates if the processes in a container are shared, or visible, to other containers in the same pod. For more information, see <a href="https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/">Share Process Namespace between Containers in a Pod</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksPodPropertiesDetail) -> dict:
    out: dict = {}
    if "service_account_name" in value:
        out["serviceAccountName"] = value["service_account_name"]
    if "host_network" in value:
        out["hostNetwork"] = value["host_network"]
    if "dns_policy" in value:
        out["dnsPolicy"] = value["dns_policy"]
    if "image_pull_secrets" in value:
        import capo_batch.types.image_pull_secrets

        out["imagePullSecrets"] = capo_batch.types.image_pull_secrets.serialize_json(
            value["image_pull_secrets"]
        )
    if "containers" in value:
        import capo_batch.types.eks_container_details

        out["containers"] = capo_batch.types.eks_container_details.serialize_json(
            value["containers"]
        )
    if "init_containers" in value:
        import capo_batch.types.eks_container_details

        out["initContainers"] = capo_batch.types.eks_container_details.serialize_json(
            value["init_containers"]
        )
    if "volumes" in value:
        import capo_batch.types.eks_volumes

        out["volumes"] = capo_batch.types.eks_volumes.serialize_json(value["volumes"])
    if "pod_name" in value:
        out["podName"] = value["pod_name"]
    if "node_name" in value:
        out["nodeName"] = value["node_name"]
    if "metadata" in value:
        import capo_batch.types.eks_metadata

        out["metadata"] = capo_batch.types.eks_metadata.serialize_json(
            value["metadata"]
        )
    if "share_process_namespace" in value:
        out["shareProcessNamespace"] = value["share_process_namespace"]
    return out


def deserialize_json(data: dict) -> EksPodPropertiesDetail:
    out: EksPodPropertiesDetail = {}  # type: ignore[typeddict-item]
    if data.get("serviceAccountName") is not None:
        out["service_account_name"] = data["serviceAccountName"]
    if data.get("hostNetwork") is not None:
        out["host_network"] = data["hostNetwork"]
    if data.get("dnsPolicy") is not None:
        out["dns_policy"] = data["dnsPolicy"]
    if data.get("imagePullSecrets") is not None:
        import capo_batch.types.image_pull_secrets

        out["image_pull_secrets"] = (
            capo_batch.types.image_pull_secrets.deserialize_json(
                data["imagePullSecrets"]
            )
        )
    if data.get("containers") is not None:
        import capo_batch.types.eks_container_details

        out["containers"] = capo_batch.types.eks_container_details.deserialize_json(
            data["containers"]
        )
    if data.get("initContainers") is not None:
        import capo_batch.types.eks_container_details

        out["init_containers"] = (
            capo_batch.types.eks_container_details.deserialize_json(
                data["initContainers"]
            )
        )
    if data.get("volumes") is not None:
        import capo_batch.types.eks_volumes

        out["volumes"] = capo_batch.types.eks_volumes.deserialize_json(data["volumes"])
    if data.get("podName") is not None:
        out["pod_name"] = data["podName"]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    if data.get("metadata") is not None:
        import capo_batch.types.eks_metadata

        out["metadata"] = capo_batch.types.eks_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("shareProcessNamespace") is not None:
        out["share_process_namespace"] = data["shareProcessNamespace"]
    return out
