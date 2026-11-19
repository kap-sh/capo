"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EbsVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.ebs_volume_configuration


class EbsVolume(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_compute_optimizer_automation.types.ebs_volume_configuration.EbsVolumeConfiguration"
    ]
    """<p>The configuration details of the EBS volume, including type, size, IOPS, and throughput.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EbsVolume) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_compute_optimizer_automation.types.ebs_volume_configuration

        out["configuration"] = (
            capo_compute_optimizer_automation.types.ebs_volume_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EbsVolume:
    out: EbsVolume = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        import capo_compute_optimizer_automation.types.ebs_volume_configuration

        out["configuration"] = (
            capo_compute_optimizer_automation.types.ebs_volume_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EbsVolume) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_compute_optimizer_automation.types.ebs_volume_configuration

        out["configuration"] = (
            capo_compute_optimizer_automation.types.ebs_volume_configuration.serialize_cbor(
                value["configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> EbsVolume:
    out: EbsVolume = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        import capo_compute_optimizer_automation.types.ebs_volume_configuration

        out["configuration"] = (
            capo_compute_optimizer_automation.types.ebs_volume_configuration.deserialize_cbor(
                data["configuration"]
            )
        )
    return out
