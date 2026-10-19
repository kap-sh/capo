"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#RegisterAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.iam_resources
    import capo_iotfleetwise.types.registration_status
    import capo_iotfleetwise.types.timestamp
    import capo_iotfleetwise.types.timestream_resources


class RegisterAccountResponse(TypedDict, closed=True):
    register_account_status: (
        "capo_iotfleetwise.types.registration_status.RegistrationStatus"
    )
    """<p> The status of registering your Amazon Web Services account, IAM role, and Timestream resources. </p>"""
    timestream_resources: NotRequired[
        "capo_iotfleetwise.types.timestream_resources.TimestreamResources"
    ]
    iam_resources: "capo_iotfleetwise.types.iam_resources.IamResources"
    """<p> The registered IAM resource that allows Amazon Web Services IoT FleetWise to send data to Amazon Timestream. </p>"""
    creation_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the account was registered, in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p> The time this registration was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegisterAccountResponse) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.registration_status

    out["registerAccountStatus"] = (
        capo_iotfleetwise.types.registration_status.serialize_aws_json_1_0(
            value["register_account_status"]
        )
    )
    if "timestream_resources" in value:
        import capo_iotfleetwise.types.timestream_resources

        out["timestreamResources"] = (
            capo_iotfleetwise.types.timestream_resources.serialize_aws_json_1_0(
                value["timestream_resources"]
            )
        )
    import capo_iotfleetwise.types.iam_resources

    out["iamResources"] = capo_iotfleetwise.types.iam_resources.serialize_aws_json_1_0(
        value["iam_resources"]
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


def deserialize_aws_json_1_0(data: dict) -> RegisterAccountResponse:
    out: RegisterAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("registerAccountStatus") is not None:
        import capo_iotfleetwise.types.registration_status

        out["register_account_status"] = (
            capo_iotfleetwise.types.registration_status.deserialize_aws_json_1_0(
                data["registerAccountStatus"]
            )
        )
    else:
        import typing

        out["register_account_status"] = typing.cast(
            "capo_iotfleetwise.types.registration_status.RegistrationStatus", ""
        )
    if data.get("timestreamResources") is not None:
        import capo_iotfleetwise.types.timestream_resources

        out["timestream_resources"] = (
            capo_iotfleetwise.types.timestream_resources.deserialize_aws_json_1_0(
                data["timestreamResources"]
            )
        )
    if data.get("iamResources") is not None:
        import capo_iotfleetwise.types.iam_resources

        out["iam_resources"] = (
            capo_iotfleetwise.types.iam_resources.deserialize_aws_json_1_0(
                data["iamResources"]
            )
        )
    else:
        raise DeserializationError("RegisterAccountResponse.iam_resources required")
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
