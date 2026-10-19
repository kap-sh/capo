"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetRegisterAccountStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.customer_account_id
    import capo_iotfleetwise.types.iam_registration_response
    import capo_iotfleetwise.types.registration_status
    import capo_iotfleetwise.types.timestamp
    import capo_iotfleetwise.types.timestream_registration_response


class GetRegisterAccountStatusResponse(TypedDict, closed=True):
    customer_account_id: "capo_iotfleetwise.types.customer_account_id.customerAccountId"
    """<p> The unique ID of the Amazon Web Services account, provided at account creation. </p>"""
    account_status: "capo_iotfleetwise.types.registration_status.RegistrationStatus"
    """<p> The status of registering your account and resources. The status can be one of:</p> <ul> <li> <p> <code>REGISTRATION_SUCCESS</code> - The Amazon Web Services resource is successfully registered.</p> </li> <li> <p> <code>REGISTRATION_PENDING</code> - Amazon Web Services IoT FleetWise is processing the registration request. This process takes approximately five minutes to complete.</p> </li> <li> <p> <code>REGISTRATION_FAILURE</code> - Amazon Web Services IoT FleetWise can't register the AWS resource. Try again later.</p> </li> </ul>"""
    timestream_registration_response: NotRequired[
        "capo_iotfleetwise.types.timestream_registration_response.TimestreamRegistrationResponse"
    ]
    """<p> Information about the registered Amazon Timestream resources or errors, if any.</p>"""
    iam_registration_response: (
        "capo_iotfleetwise.types.iam_registration_response.IamRegistrationResponse"
    )
    """<p> Information about the registered IAM resources or errors, if any. </p>"""
    creation_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the account was registered, in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p> The time this registration was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRegisterAccountStatusResponse) -> dict:
    out: dict = {}
    out["customerAccountId"] = value["customer_account_id"]
    import capo_iotfleetwise.types.registration_status

    out["accountStatus"] = (
        capo_iotfleetwise.types.registration_status.serialize_aws_json_1_0(
            value["account_status"]
        )
    )
    if "timestream_registration_response" in value:
        import capo_iotfleetwise.types.timestream_registration_response

        out["timestreamRegistrationResponse"] = (
            capo_iotfleetwise.types.timestream_registration_response.serialize_aws_json_1_0(
                value["timestream_registration_response"]
            )
        )
    import capo_iotfleetwise.types.iam_registration_response

    out["iamRegistrationResponse"] = (
        capo_iotfleetwise.types.iam_registration_response.serialize_aws_json_1_0(
            value["iam_registration_response"]
        )
    )
    import capo_iotfleetwise.types.timestamp

    out["creationTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
        value["creation_time"]
    )
    import capo_iotfleetwise.types.timestamp

    out["lastModificationTime"] = (
        capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["last_modification_time"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRegisterAccountStatusResponse:
    out: GetRegisterAccountStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("customerAccountId") is not None:
        out["customer_account_id"] = data["customerAccountId"]
    else:
        out["customer_account_id"] = ""
    if data.get("accountStatus") is not None:
        import capo_iotfleetwise.types.registration_status

        out["account_status"] = (
            capo_iotfleetwise.types.registration_status.deserialize_aws_json_1_0(
                data["accountStatus"]
            )
        )
    else:
        import typing

        out["account_status"] = typing.cast(
            "capo_iotfleetwise.types.registration_status.RegistrationStatus", ""
        )
    if data.get("timestreamRegistrationResponse") is not None:
        import capo_iotfleetwise.types.timestream_registration_response

        out["timestream_registration_response"] = (
            capo_iotfleetwise.types.timestream_registration_response.deserialize_aws_json_1_0(
                data["timestreamRegistrationResponse"]
            )
        )
    if data.get("iamRegistrationResponse") is not None:
        import capo_iotfleetwise.types.iam_registration_response

        out["iam_registration_response"] = (
            capo_iotfleetwise.types.iam_registration_response.deserialize_aws_json_1_0(
                data["iamRegistrationResponse"]
            )
        )
    else:
        raise DeserializationError(
            "GetRegisterAccountStatusResponse.iam_registration_response required"
        )
    if data.get("creationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["creation_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModificationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        import datetime

        out["last_modification_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
