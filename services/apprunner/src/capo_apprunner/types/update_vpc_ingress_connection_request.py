"""Generated from Smithy shape ``com.amazonaws.apprunner#UpdateVpcIngressConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.ingress_vpc_configuration


class UpdateVpcIngressConnectionRequest(TypedDict, closed=True):
    vpc_ingress_connection_arn: (
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (Arn) for the App Runner VPC Ingress Connection resource that you want to update.</p>"""
    ingress_vpc_configuration: (
        "capo_apprunner.types.ingress_vpc_configuration.IngressVpcConfiguration"
    )
    """<p>Specifications for the customer’s Amazon VPC and the related Amazon Web Services PrivateLink VPC endpoint that are used to update the VPC Ingress Connection resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVpcIngressConnectionRequest) -> dict:
    out: dict = {}
    out["VpcIngressConnectionArn"] = value["vpc_ingress_connection_arn"]
    import capo_apprunner.types.ingress_vpc_configuration

    out["IngressVpcConfiguration"] = (
        capo_apprunner.types.ingress_vpc_configuration.serialize_aws_json_1_0(
            value["ingress_vpc_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVpcIngressConnectionRequest:
    out: UpdateVpcIngressConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("VpcIngressConnectionArn") is not None:
        out["vpc_ingress_connection_arn"] = data["VpcIngressConnectionArn"]
    else:
        out["vpc_ingress_connection_arn"] = ""
    if data.get("IngressVpcConfiguration") is not None:
        import capo_apprunner.types.ingress_vpc_configuration

        out["ingress_vpc_configuration"] = (
            capo_apprunner.types.ingress_vpc_configuration.deserialize_aws_json_1_0(
                data["IngressVpcConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateVpcIngressConnectionRequest.ingress_vpc_configuration required"
        )
    return out
