"""Generated from Smithy shape ``com.amazonaws.licensemanager#AllowedOperation``."""

from typing import Literal, TypeAlias, cast

AllowedOperation: TypeAlias = Literal[
    "CreateGrant",
    "CheckoutLicense",
    "CheckoutBorrowLicense",
    "CheckInLicense",
    "ExtendConsumptionLicense",
    "ListPurchasedLicenses",
    "CreateToken",
    "ListReceivedLicenses",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AllowedOperation:
    return cast(AllowedOperation, data)
