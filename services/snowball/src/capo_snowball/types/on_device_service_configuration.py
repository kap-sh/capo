"""Generated from Smithy shape ``com.amazonaws.snowball#OnDeviceServiceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.eks_on_device_service_configuration
    import capo_snowball.types.nfs_on_device_service_configuration
    import capo_snowball.types.s3_on_device_service_configuration
    import capo_snowball.types.tgw_on_device_service_configuration


class OnDeviceServiceConfiguration(TypedDict, closed=True):
    nfs_on_device_service: NotRequired[
        "capo_snowball.types.nfs_on_device_service_configuration.NFSOnDeviceServiceConfiguration"
    ]
    """<p>Represents the NFS (Network File System) service on a Snow Family device.</p>"""
    tgw_on_device_service: NotRequired[
        "capo_snowball.types.tgw_on_device_service_configuration.TGWOnDeviceServiceConfiguration"
    ]
    """<p>Represents the Storage Gateway service Tape Gateway type on a Snow Family device.</p>"""
    eks_on_device_service: NotRequired[
        "capo_snowball.types.eks_on_device_service_configuration.EKSOnDeviceServiceConfiguration"
    ]
    """<p>The configuration of EKS Anywhere on the Snow Family device.</p>"""
    s3_on_device_service: NotRequired[
        "capo_snowball.types.s3_on_device_service_configuration.S3OnDeviceServiceConfiguration"
    ]
    """<p>Configuration for Amazon S3 compatible storage on Snow family devices.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnDeviceServiceConfiguration) -> dict:
    out: dict = {}
    if "nfs_on_device_service" in value:
        import capo_snowball.types.nfs_on_device_service_configuration

        out["NFSOnDeviceService"] = (
            capo_snowball.types.nfs_on_device_service_configuration.serialize_aws_json_1_1(
                value["nfs_on_device_service"]
            )
        )
    if "tgw_on_device_service" in value:
        import capo_snowball.types.tgw_on_device_service_configuration

        out["TGWOnDeviceService"] = (
            capo_snowball.types.tgw_on_device_service_configuration.serialize_aws_json_1_1(
                value["tgw_on_device_service"]
            )
        )
    if "eks_on_device_service" in value:
        import capo_snowball.types.eks_on_device_service_configuration

        out["EKSOnDeviceService"] = (
            capo_snowball.types.eks_on_device_service_configuration.serialize_aws_json_1_1(
                value["eks_on_device_service"]
            )
        )
    if "s3_on_device_service" in value:
        import capo_snowball.types.s3_on_device_service_configuration

        out["S3OnDeviceService"] = (
            capo_snowball.types.s3_on_device_service_configuration.serialize_aws_json_1_1(
                value["s3_on_device_service"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnDeviceServiceConfiguration:
    out: OnDeviceServiceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("NFSOnDeviceService") is not None:
        import capo_snowball.types.nfs_on_device_service_configuration

        out["nfs_on_device_service"] = (
            capo_snowball.types.nfs_on_device_service_configuration.deserialize_aws_json_1_1(
                data["NFSOnDeviceService"]
            )
        )
    if data.get("TGWOnDeviceService") is not None:
        import capo_snowball.types.tgw_on_device_service_configuration

        out["tgw_on_device_service"] = (
            capo_snowball.types.tgw_on_device_service_configuration.deserialize_aws_json_1_1(
                data["TGWOnDeviceService"]
            )
        )
    if data.get("EKSOnDeviceService") is not None:
        import capo_snowball.types.eks_on_device_service_configuration

        out["eks_on_device_service"] = (
            capo_snowball.types.eks_on_device_service_configuration.deserialize_aws_json_1_1(
                data["EKSOnDeviceService"]
            )
        )
    if data.get("S3OnDeviceService") is not None:
        import capo_snowball.types.s3_on_device_service_configuration

        out["s3_on_device_service"] = (
            capo_snowball.types.s3_on_device_service_configuration.deserialize_aws_json_1_1(
                data["S3OnDeviceService"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OnDeviceServiceConfiguration) -> dict:
    out: dict = {}
    if "nfs_on_device_service" in value:
        import capo_snowball.types.nfs_on_device_service_configuration

        out["NFSOnDeviceService"] = (
            capo_snowball.types.nfs_on_device_service_configuration.serialize_cbor(
                value["nfs_on_device_service"]
            )
        )
    if "tgw_on_device_service" in value:
        import capo_snowball.types.tgw_on_device_service_configuration

        out["TGWOnDeviceService"] = (
            capo_snowball.types.tgw_on_device_service_configuration.serialize_cbor(
                value["tgw_on_device_service"]
            )
        )
    if "eks_on_device_service" in value:
        import capo_snowball.types.eks_on_device_service_configuration

        out["EKSOnDeviceService"] = (
            capo_snowball.types.eks_on_device_service_configuration.serialize_cbor(
                value["eks_on_device_service"]
            )
        )
    if "s3_on_device_service" in value:
        import capo_snowball.types.s3_on_device_service_configuration

        out["S3OnDeviceService"] = (
            capo_snowball.types.s3_on_device_service_configuration.serialize_cbor(
                value["s3_on_device_service"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> OnDeviceServiceConfiguration:
    out: OnDeviceServiceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("NFSOnDeviceService") is not None:
        import capo_snowball.types.nfs_on_device_service_configuration

        out["nfs_on_device_service"] = (
            capo_snowball.types.nfs_on_device_service_configuration.deserialize_cbor(
                data["NFSOnDeviceService"]
            )
        )
    if data.get("TGWOnDeviceService") is not None:
        import capo_snowball.types.tgw_on_device_service_configuration

        out["tgw_on_device_service"] = (
            capo_snowball.types.tgw_on_device_service_configuration.deserialize_cbor(
                data["TGWOnDeviceService"]
            )
        )
    if data.get("EKSOnDeviceService") is not None:
        import capo_snowball.types.eks_on_device_service_configuration

        out["eks_on_device_service"] = (
            capo_snowball.types.eks_on_device_service_configuration.deserialize_cbor(
                data["EKSOnDeviceService"]
            )
        )
    if data.get("S3OnDeviceService") is not None:
        import capo_snowball.types.s3_on_device_service_configuration

        out["s3_on_device_service"] = (
            capo_snowball.types.s3_on_device_service_configuration.deserialize_cbor(
                data["S3OnDeviceService"]
            )
        )
    return out
