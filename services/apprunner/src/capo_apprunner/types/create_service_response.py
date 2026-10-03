"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.service
    import capo_apprunner.types.uuid


class CreateServiceResponse(TypedDict, closed=True):
    service: "capo_apprunner.types.service.Service"
    """<p>A description of the App Runner service that's created by this request.</p>"""
    operation_id: "capo_apprunner.types.uuid.UUID"
    """<p>The unique ID of the asynchronous operation that this request started. You can use it combined with the <a href="https://docs.aws.amazon.com/apprunner/latest/api/API_ListOperations.html">ListOperations</a> call to track the operation's progress.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateServiceResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.service

    out["Service"] = capo_apprunner.types.service.serialize_aws_json_1_0(
        value["service"]
    )
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateServiceResponse:
    out: CreateServiceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        import capo_apprunner.types.service

        out["service"] = capo_apprunner.types.service.deserialize_aws_json_1_0(
            data["Service"]
        )
    else:
        raise DeserializationError("CreateServiceResponse.service required")
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    else:
        raise DeserializationError("CreateServiceResponse.operation_id required")
    return out
