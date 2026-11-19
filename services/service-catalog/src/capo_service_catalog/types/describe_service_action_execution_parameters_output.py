"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeServiceActionExecutionParametersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.execution_parameters


class DescribeServiceActionExecutionParametersOutput(TypedDict, closed=True):
    service_action_parameters: NotRequired[
        "capo_service_catalog.types.execution_parameters.ExecutionParameters"
    ]
    """<p>The parameters of the self-service action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeServiceActionExecutionParametersOutput,
) -> dict:
    out: dict = {}
    if "service_action_parameters" in value:
        import capo_service_catalog.types.execution_parameters

        out["ServiceActionParameters"] = (
            capo_service_catalog.types.execution_parameters.serialize_aws_json_1_1(
                value["service_action_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeServiceActionExecutionParametersOutput:
    out: DescribeServiceActionExecutionParametersOutput = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionParameters") is not None:
        import capo_service_catalog.types.execution_parameters

        out["service_action_parameters"] = (
            capo_service_catalog.types.execution_parameters.deserialize_aws_json_1_1(
                data["ServiceActionParameters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeServiceActionExecutionParametersOutput) -> dict:
    out: dict = {}
    if "service_action_parameters" in value:
        import capo_service_catalog.types.execution_parameters

        out["ServiceActionParameters"] = (
            capo_service_catalog.types.execution_parameters.serialize_cbor(
                value["service_action_parameters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeServiceActionExecutionParametersOutput:
    out: DescribeServiceActionExecutionParametersOutput = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionParameters") is not None:
        import capo_service_catalog.types.execution_parameters

        out["service_action_parameters"] = (
            capo_service_catalog.types.execution_parameters.deserialize_cbor(
                data["ServiceActionParameters"]
            )
        )
    return out
