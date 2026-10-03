"""Generated from Smithy shape ``com.amazonaws.sagemaker#SourceIpConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cidrs


class SourceIpConfig(TypedDict, closed=True):
    cidrs: NotRequired["capo_sagemaker.types.cidrs.Cidrs"]
    """<p>A list of one to ten <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">Classless Inter-Domain Routing</a> (CIDR) values.</p> <p>Maximum: Ten CIDR values</p> <note> <p>The following Length Constraints apply to individual CIDR values in the CIDR value list.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceIpConfig) -> dict:
    out: dict = {}
    if "cidrs" in value:
        import capo_sagemaker.types.cidrs

        out["Cidrs"] = capo_sagemaker.types.cidrs.serialize_aws_json_1_1(value["cidrs"])
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceIpConfig:
    out: SourceIpConfig = {}  # type: ignore[typeddict-item]
    if data.get("Cidrs") is not None:
        import capo_sagemaker.types.cidrs

        out["cidrs"] = capo_sagemaker.types.cidrs.deserialize_aws_json_1_1(
            data["Cidrs"]
        )
    return out
