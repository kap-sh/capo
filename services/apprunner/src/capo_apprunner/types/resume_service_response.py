"""Generated from Smithy shape ``com.amazonaws.apprunner#ResumeServiceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.service
    import capo_apprunner.types.uuid


class ResumeServiceResponse(TypedDict, closed=True):
    service: "capo_apprunner.types.service.Service"
    """<p>A description of the App Runner service that this request just resumed.</p>"""
    operation_id: NotRequired["capo_apprunner.types.uuid.UUID"]
    """<p>The unique ID of the asynchronous operation that this request started. You can use it combined with the <a>ListOperations</a> call to track the operation's progress.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResumeServiceResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.service

    out["Service"] = capo_apprunner.types.service.serialize_aws_json_1_0(
        value["service"]
    )
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResumeServiceResponse:
    out: ResumeServiceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        import capo_apprunner.types.service

        out["service"] = capo_apprunner.types.service.deserialize_aws_json_1_0(
            data["Service"]
        )
    else:
        raise DeserializationError("ResumeServiceResponse.service required")
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    return out


def redact_sensitive(value: ResumeServiceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_apprunner.types.service

        out["service"] = capo_apprunner.types.service.redact_sensitive(value["service"])
    return out
