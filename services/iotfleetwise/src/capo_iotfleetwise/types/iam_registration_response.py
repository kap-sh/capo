"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#IamRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.error_message
    import capo_iotfleetwise.types.registration_status


class IamRegistrationResponse(TypedDict, closed=True):
    role_arn: "capo_iotfleetwise.types.arn.arn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to register.</p>"""
    registration_status: (
        "capo_iotfleetwise.types.registration_status.RegistrationStatus"
    )
    """<p>The status of registering your IAM resource. The status can be one of <code>REGISTRATION_SUCCESS</code>, <code>REGISTRATION_PENDING</code>, <code>REGISTRATION_FAILURE</code>.</p>"""
    error_message: NotRequired["capo_iotfleetwise.types.error_message.errorMessage"]
    """<p>A message associated with a registration error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IamRegistrationResponse) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    import capo_iotfleetwise.types.registration_status

    out["registrationStatus"] = (
        capo_iotfleetwise.types.registration_status.serialize_aws_json_1_0(
            value["registration_status"]
        )
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IamRegistrationResponse:
    out: IamRegistrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("registrationStatus") is not None:
        import capo_iotfleetwise.types.registration_status

        out["registration_status"] = (
            capo_iotfleetwise.types.registration_status.deserialize_aws_json_1_0(
                data["registrationStatus"]
            )
        )
    else:
        import typing

        out["registration_status"] = typing.cast(
            "capo_iotfleetwise.types.registration_status.RegistrationStatus", ""
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
