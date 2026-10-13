"""Generated from Smithy shape ``com.amazonaws.pipes#NetworkConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.aws_vpc_configuration


class NetworkConfiguration(TypedDict, closed=True):
    awsvpc_configuration: NotRequired[
        "capo_pipes.types.aws_vpc_configuration.AwsVpcConfiguration"
    ]
    """<p>Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the <code>awsvpc</code> network mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "awsvpc_configuration" in value:
        import capo_pipes.types.aws_vpc_configuration

        out["awsvpcConfiguration"] = (
            capo_pipes.types.aws_vpc_configuration.serialize_json(
                value["awsvpc_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("awsvpcConfiguration") is not None:
        import capo_pipes.types.aws_vpc_configuration

        out["awsvpc_configuration"] = (
            capo_pipes.types.aws_vpc_configuration.deserialize_json(
                data["awsvpcConfiguration"]
            )
        )
    return out


def redact_sensitive(value: NetworkConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "awsvpc_configuration" in value:
        import capo_pipes.types.aws_vpc_configuration

        out["awsvpc_configuration"] = (
            capo_pipes.types.aws_vpc_configuration.redact_sensitive(
                value["awsvpc_configuration"]
            )
        )
    return out
