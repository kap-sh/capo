"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PutEventSelectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.advanced_event_selectors
    import capo_cloudtrail.types.event_selectors
    import capo_cloudtrail.types.string


class PutEventSelectorsRequest(TypedDict, closed=True):
    trail_name: "capo_cloudtrail.types.string.String"
    """<p>Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)</p> </li> <li> <p>Start with a letter or number, and end with a letter or number</p> </li> <li> <p>Be between 3 and 128 characters</p> </li> <li> <p>Have no adjacent periods, underscores or dashes. Names like <code>my-_namespace</code> and <code>my--namespace</code> are not valid.</p> </li> <li> <p>Not be in IP address format (for example, 192.168.5.4)</p> </li> </ul> <p>If you specify a trail ARN, it must be in the following format.</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>"""
    event_selectors: NotRequired["capo_cloudtrail.types.event_selectors.EventSelectors"]
    """<p>Specifies the settings for your event selectors. You can use event selectors to log management events and data events for the following resource types:</p> <ul> <li> <p> <code>AWS::DynamoDB::Table</code> </p> </li> <li> <p> <code>AWS::Lambda::Function</code> </p> </li> <li> <p> <code>AWS::S3::Object</code> </p> </li> </ul> <p>You can't use event selectors to log network activity events.</p> <p>You can configure up to five event selectors for a trail. You can use either <code>EventSelectors</code> or <code>AdvancedEventSelectors</code> in a <code>PutEventSelectors</code> request, but not both. If you apply <code>EventSelectors</code> to a trail, any existing <code>AdvancedEventSelectors</code> are overwritten.</p>"""
    advanced_event_selectors: NotRequired[
        "capo_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
    ]
    """<p> Specifies the settings for advanced event selectors. You can use advanced event selectors to log management events, data events for all resource types, and network activity events.</p> <p>You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use either <code>AdvancedEventSelectors</code> or <code>EventSelectors</code>, but not both. If you apply <code>AdvancedEventSelectors</code> to a trail, any existing <code>EventSelectors</code> are overwritten. For more information about advanced event selectors, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html">Logging data events</a> and <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html">Logging network activity events</a> in the <i>CloudTrail User Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventSelectorsRequest) -> dict:
    out: dict = {}
    out["TrailName"] = value["trail_name"]
    if "event_selectors" in value:
        import capo_cloudtrail.types.event_selectors

        out["EventSelectors"] = (
            capo_cloudtrail.types.event_selectors.serialize_aws_json_1_1(
                value["event_selectors"]
            )
        )
    if "advanced_event_selectors" in value:
        import capo_cloudtrail.types.advanced_event_selectors

        out["AdvancedEventSelectors"] = (
            capo_cloudtrail.types.advanced_event_selectors.serialize_aws_json_1_1(
                value["advanced_event_selectors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEventSelectorsRequest:
    out: PutEventSelectorsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrailName") is not None:
        out["trail_name"] = data["TrailName"]
    else:
        raise DeserializationError("PutEventSelectorsRequest.trail_name required")
    if data.get("EventSelectors") is not None:
        import capo_cloudtrail.types.event_selectors

        out["event_selectors"] = (
            capo_cloudtrail.types.event_selectors.deserialize_aws_json_1_1(
                data["EventSelectors"]
            )
        )
    if data.get("AdvancedEventSelectors") is not None:
        import capo_cloudtrail.types.advanced_event_selectors

        out["advanced_event_selectors"] = (
            capo_cloudtrail.types.advanced_event_selectors.deserialize_aws_json_1_1(
                data["AdvancedEventSelectors"]
            )
        )
    return out
