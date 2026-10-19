"""Generated from Smithy shape ``com.amazonaws.apprunner#UpdateServiceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.service
    import capo_apprunner.types.uuid


class UpdateServiceResponse(TypedDict, closed=True):
    service: "capo_apprunner.types.service.Service"
    """<p>A description of the App Runner service updated by this request. All configuration values in the returned <code>Service</code> structure reflect configuration changes that are being applied by this request.</p>"""
    operation_id: "capo_apprunner.types.uuid.UUID"
    """<p>The unique ID of the asynchronous operation that this request started. You can use it combined with the <a>ListOperations</a> call to track the operation's progress.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.service

    out["Service"] = capo_apprunner.types.service.serialize_aws_json_1_0(
        value["service"]
    )
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceResponse:
    out: UpdateServiceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        import capo_apprunner.types.service

        out["service"] = capo_apprunner.types.service.deserialize_aws_json_1_0(
            data["Service"]
        )
    else:
        raise DeserializationError("UpdateServiceResponse.service required")
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    else:
        out["operation_id"] = ""
    return out


def redact_sensitive(value: UpdateServiceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_apprunner.types.service

        out["service"] = capo_apprunner.types.service.redact_sensitive(value["service"])
    return out
