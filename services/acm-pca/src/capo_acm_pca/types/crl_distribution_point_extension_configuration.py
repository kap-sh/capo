"""Generated from Smithy shape ``com.amazonaws.acmpca#CrlDistributionPointExtensionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.boolean


class CrlDistributionPointExtensionConfiguration(TypedDict, closed=True):
    omit_extension: "capo_acm_pca.types.boolean.Boolean"
    """<p>Configures whether the CRL Distribution Point extension should be populated with the default URL to the CRL. If set to <code>true</code>, then the CDP extension will not be present in any certificates issued by that CA unless otherwise specified through CSR or API passthrough.</p> <note> <p>Only set this if you have another way to distribute the CRL Distribution Points for certificates issued by your CA, such as the Matter Distributed Compliance Ledger</p> <p>This configuration cannot be enabled with a custom CNAME set.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrlDistributionPointExtensionConfiguration) -> dict:
    out: dict = {}
    out["OmitExtension"] = value["omit_extension"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CrlDistributionPointExtensionConfiguration:
    out: CrlDistributionPointExtensionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("OmitExtension") is not None:
        out["omit_extension"] = data["OmitExtension"]
    else:
        out["omit_extension"] = False
    return out
