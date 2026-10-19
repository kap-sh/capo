"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#InitializeClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cert
    import capo_cloudhsm_v2.types.cluster_id


class InitializeClusterRequest(TypedDict, closed=True):
    cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId"
    """<p>The identifier (ID) of the cluster that you are claiming. To find the cluster ID, use <a>DescribeClusters</a>.</p>"""
    signed_cert: "capo_cloudhsm_v2.types.cert.Cert"
    """<p>The cluster certificate issued (signed) by your issuing certificate authority (CA). The certificate must be in PEM format and can contain a maximum of 5000 characters.</p>"""
    trust_anchor: "capo_cloudhsm_v2.types.cert.Cert"
    """<p>The issuing certificate of the issuing certificate authority (CA) that issued (signed) the cluster certificate. You must use a self-signed certificate. The certificate used to sign the HSM CSR must be directly available, and thus must be the root certificate. The certificate must be in PEM format and can contain a maximum of 5000 characters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InitializeClusterRequest) -> dict:
    out: dict = {}
    out["ClusterId"] = value["cluster_id"]
    out["SignedCert"] = value["signed_cert"]
    out["TrustAnchor"] = value["trust_anchor"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InitializeClusterRequest:
    out: InitializeClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    else:
        out["cluster_id"] = ""
    if data.get("SignedCert") is not None:
        out["signed_cert"] = data["SignedCert"]
    else:
        out["signed_cert"] = ""
    if data.get("TrustAnchor") is not None:
        out["trust_anchor"] = data["TrustAnchor"]
    else:
        out["trust_anchor"] = ""
    return out
