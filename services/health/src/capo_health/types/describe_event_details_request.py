"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_health.errors import DeserializationError

if TYPE_CHECKING:
    import capo_health.types.event_arn_list
    import capo_health.types.locale


class DescribeEventDetailsRequest(TypedDict, closed=True):
    event_arns: "capo_health.types.event_arn_list.eventArnList"
    """<p>A list of event ARNs (unique identifiers). For example: <code>"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"</code> </p>"""
    locale: NotRequired["capo_health.types.locale.locale"]
    """<p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventDetailsRequest) -> dict:
    out: dict = {}
    import capo_health.types.event_arn_list

    out["eventArns"] = capo_health.types.event_arn_list.serialize_aws_json_1_1(
        value["event_arns"]
    )
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventDetailsRequest:
    out: DescribeEventDetailsRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventArns") is not None:
        import capo_health.types.event_arn_list

        out["event_arns"] = capo_health.types.event_arn_list.deserialize_aws_json_1_1(
            data["eventArns"]
        )
    else:
        raise DeserializationError("DescribeEventDetailsRequest.event_arns required")
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    return out
