"""Generated from Smithy shape ``com.amazonaws.snowball#EKSOnDeviceServiceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.string


class EKSOnDeviceServiceConfiguration(TypedDict, closed=True):
    kubernetes_version: NotRequired["capo_snowball.types.string.String"]
    """<p>The Kubernetes version for EKS Anywhere on the Snow Family device.</p>"""
    eks_anywhere_version: NotRequired["capo_snowball.types.string.String"]
    """<p>The optional version of EKS Anywhere on the Snow Family device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EKSOnDeviceServiceConfiguration) -> dict:
    out: dict = {}
    if "kubernetes_version" in value:
        out["KubernetesVersion"] = value["kubernetes_version"]
    if "eks_anywhere_version" in value:
        out["EKSAnywhereVersion"] = value["eks_anywhere_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EKSOnDeviceServiceConfiguration:
    out: EKSOnDeviceServiceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KubernetesVersion") is not None:
        out["kubernetes_version"] = data["KubernetesVersion"]
    if data.get("EKSAnywhereVersion") is not None:
        out["eks_anywhere_version"] = data["EKSAnywhereVersion"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EKSOnDeviceServiceConfiguration) -> dict:
    out: dict = {}
    if "kubernetes_version" in value:
        out["KubernetesVersion"] = value["kubernetes_version"]
    if "eks_anywhere_version" in value:
        out["EKSAnywhereVersion"] = value["eks_anywhere_version"]
    return out


def deserialize_cbor(data: dict) -> EKSOnDeviceServiceConfiguration:
    out: EKSOnDeviceServiceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KubernetesVersion") is not None:
        out["kubernetes_version"] = data["KubernetesVersion"]
    if data.get("EKSAnywhereVersion") is not None:
        out["eks_anywhere_version"] = data["EKSAnywhereVersion"]
    return out
