"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayResourceFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_operation_error_list
    import capo_ecs.types.string


class GatewayResourceFailure(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource that failed to update, such as a load balancer ARN.</p>"""
    errors: NotRequired[
        "capo_ecs.types.gateway_operation_error_list.GatewayOperationErrorList"
    ]
    """<p>The errors that were encountered while operating on the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayResourceFailure) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "errors" in value:
        import capo_ecs.types.gateway_operation_error_list

        out["errors"] = (
            capo_ecs.types.gateway_operation_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayResourceFailure:
    out: GatewayResourceFailure = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("errors") is not None:
        import capo_ecs.types.gateway_operation_error_list

        out["errors"] = (
            capo_ecs.types.gateway_operation_error_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out
