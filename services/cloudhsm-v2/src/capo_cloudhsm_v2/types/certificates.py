"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Certificates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cert


class Certificates(TypedDict, closed=True):
    cluster_csr: NotRequired["capo_cloudhsm_v2.types.cert.Cert"]
    """<p>The cluster's certificate signing request (CSR). The CSR exists only when the cluster's state is <code>UNINITIALIZED</code>.</p>"""
    hsm_certificate: NotRequired["capo_cloudhsm_v2.types.cert.Cert"]
    """<p>The HSM certificate issued (signed) by the HSM hardware.</p>"""
    aws_hardware_certificate: NotRequired["capo_cloudhsm_v2.types.cert.Cert"]
    """<p>The HSM hardware certificate issued (signed) by CloudHSM.</p>"""
    manufacturer_hardware_certificate: NotRequired["capo_cloudhsm_v2.types.cert.Cert"]
    """<p>The HSM hardware certificate issued (signed) by the hardware manufacturer.</p>"""
    cluster_certificate: NotRequired["capo_cloudhsm_v2.types.cert.Cert"]
    """<p>The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster's owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Certificates) -> dict:
    out: dict = {}
    if "cluster_csr" in value:
        out["ClusterCsr"] = value["cluster_csr"]
    if "hsm_certificate" in value:
        out["HsmCertificate"] = value["hsm_certificate"]
    if "aws_hardware_certificate" in value:
        out["AwsHardwareCertificate"] = value["aws_hardware_certificate"]
    if "manufacturer_hardware_certificate" in value:
        out["ManufacturerHardwareCertificate"] = value[
            "manufacturer_hardware_certificate"
        ]
    if "cluster_certificate" in value:
        out["ClusterCertificate"] = value["cluster_certificate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Certificates:
    out: Certificates = {}  # type: ignore[typeddict-item]
    if data.get("ClusterCsr") is not None:
        out["cluster_csr"] = data["ClusterCsr"]
    if data.get("HsmCertificate") is not None:
        out["hsm_certificate"] = data["HsmCertificate"]
    if data.get("AwsHardwareCertificate") is not None:
        out["aws_hardware_certificate"] = data["AwsHardwareCertificate"]
    if data.get("ManufacturerHardwareCertificate") is not None:
        out["manufacturer_hardware_certificate"] = data[
            "ManufacturerHardwareCertificate"
        ]
    if data.get("ClusterCertificate") is not None:
        out["cluster_certificate"] = data["ClusterCertificate"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Certificates) -> dict:
    out: dict = {}
    if "cluster_csr" in value:
        out["ClusterCsr"] = value["cluster_csr"]
    if "hsm_certificate" in value:
        out["HsmCertificate"] = value["hsm_certificate"]
    if "aws_hardware_certificate" in value:
        out["AwsHardwareCertificate"] = value["aws_hardware_certificate"]
    if "manufacturer_hardware_certificate" in value:
        out["ManufacturerHardwareCertificate"] = value[
            "manufacturer_hardware_certificate"
        ]
    if "cluster_certificate" in value:
        out["ClusterCertificate"] = value["cluster_certificate"]
    return out


def deserialize_cbor(data: dict) -> Certificates:
    out: Certificates = {}  # type: ignore[typeddict-item]
    if data.get("ClusterCsr") is not None:
        out["cluster_csr"] = data["ClusterCsr"]
    if data.get("HsmCertificate") is not None:
        out["hsm_certificate"] = data["HsmCertificate"]
    if data.get("AwsHardwareCertificate") is not None:
        out["aws_hardware_certificate"] = data["AwsHardwareCertificate"]
    if data.get("ManufacturerHardwareCertificate") is not None:
        out["manufacturer_hardware_certificate"] = data[
            "ManufacturerHardwareCertificate"
        ]
    if data.get("ClusterCertificate") is not None:
        out["cluster_certificate"] = data["ClusterCertificate"]
    return out
