"""Generated from Smithy shape ``com.amazonaws.lightsail#DetachCertificateFromDistributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class DetachCertificateFromDistributionRequest(TypedDict, closed=True):
    distribution_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the distribution from which to detach the certificate.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachCertificateFromDistributionRequest) -> dict:
    out: dict = {}
    out["distributionName"] = value["distribution_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachCertificateFromDistributionRequest:
    out: DetachCertificateFromDistributionRequest = {}  # type: ignore[typeddict-item]
    if data.get("distributionName") is not None:
        out["distribution_name"] = data["distributionName"]
    else:
        out["distribution_name"] = ""
    return out
