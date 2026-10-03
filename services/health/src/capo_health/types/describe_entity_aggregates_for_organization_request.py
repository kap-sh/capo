"""Generated from Smithy shape ``com.amazonaws.health#DescribeEntityAggregatesForOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_health.errors import DeserializationError

if TYPE_CHECKING:
    import capo_health.types.organization_account_ids_list
    import capo_health.types.organization_event_arns_list


class DescribeEntityAggregatesForOrganizationRequest(TypedDict, closed=True):
    event_arns: (
        "capo_health.types.organization_event_arns_list.OrganizationEventArnsList"
    )
    """<p>A list of event ARNs (unique identifiers). For example: <code>"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"</code> </p>"""
    aws_account_ids: NotRequired[
        "capo_health.types.organization_account_ids_list.OrganizationAccountIdsList"
    ]
    """<p>A list of 12-digit Amazon Web Services account numbers that contains the affected entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeEntityAggregatesForOrganizationRequest,
) -> dict:
    out: dict = {}
    import capo_health.types.organization_event_arns_list

    out["eventArns"] = (
        capo_health.types.organization_event_arns_list.serialize_aws_json_1_1(
            value["event_arns"]
        )
    )
    if "aws_account_ids" in value:
        import capo_health.types.organization_account_ids_list

        out["awsAccountIds"] = (
            capo_health.types.organization_account_ids_list.serialize_aws_json_1_1(
                value["aws_account_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeEntityAggregatesForOrganizationRequest:
    out: DescribeEntityAggregatesForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventArns") is not None:
        import capo_health.types.organization_event_arns_list

        out["event_arns"] = (
            capo_health.types.organization_event_arns_list.deserialize_aws_json_1_1(
                data["eventArns"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeEntityAggregatesForOrganizationRequest.event_arns required"
        )
    if data.get("awsAccountIds") is not None:
        import capo_health.types.organization_account_ids_list

        out["aws_account_ids"] = (
            capo_health.types.organization_account_ids_list.deserialize_aws_json_1_1(
                data["awsAccountIds"]
            )
        )
    return out
