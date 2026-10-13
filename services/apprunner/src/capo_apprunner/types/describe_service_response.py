"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeServiceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.service


class DescribeServiceResponse(TypedDict, closed=True):
    service: "capo_apprunner.types.service.Service"
    """<p>A full description of the App Runner service that you specified in this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeServiceResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.service

    out["Service"] = capo_apprunner.types.service.serialize_aws_json_1_0(
        value["service"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeServiceResponse:
    out: DescribeServiceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        import capo_apprunner.types.service

        out["service"] = capo_apprunner.types.service.deserialize_aws_json_1_0(
            data["Service"]
        )
    else:
        raise DeserializationError("DescribeServiceResponse.service required")
    return out


def redact_sensitive(value: DescribeServiceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_apprunner.types.service

        out["service"] = capo_apprunner.types.service.redact_sensitive(value["service"])
    return out
