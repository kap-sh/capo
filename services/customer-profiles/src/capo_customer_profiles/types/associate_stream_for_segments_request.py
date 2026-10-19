"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AssociateStreamForSegmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.destination_arn_string
    import capo_customer_profiles.types.destination_role_arn
    import capo_customer_profiles.types.name


class AssociateStreamForSegmentsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    destination_arn: (
        "capo_customer_profiles.types.destination_arn_string.DestinationArnString"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon Kinesis data stream to deliver segment membership events to. For example, <code>arn:aws:kinesis:region:account-id:stream/stream-name</code>. </p>"""
    destination_role_arn: (
        "capo_customer_profiles.types.destination_role_arn.DestinationRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role that allows Customer Profiles service principal to assume the role for conducting AWS Key Management Service (KMS) and Amazon Kinesis operations. The role must grant the following Amazon Kinesis permissions to deliver segment membership events to the stream: </p> <ul> <li> <p> <code>kinesis:PutRecord</code> </p> </li> <li> <p> <code>kinesis:PutRecords</code> </p> </li> <li> <p> <code>kinesis:DescribeStream</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateStreamForSegmentsRequest) -> dict:
    out: dict = {}
    out["DestinationArn"] = value["destination_arn"]
    out["DestinationRoleArn"] = value["destination_role_arn"]
    return out


def deserialize_json(data: dict) -> AssociateStreamForSegmentsRequest:
    out: AssociateStreamForSegmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DestinationArn") is not None:
        out["destination_arn"] = data["DestinationArn"]
    else:
        out["destination_arn"] = ""
    if data.get("DestinationRoleArn") is not None:
        out["destination_role_arn"] = data["DestinationRoleArn"]
    else:
        out["destination_role_arn"] = ""
    return out
