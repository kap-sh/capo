"""Generated from Smithy shape ``com.amazonaws.cloudfront#LambdaFunctionAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.event_type
    import capo_cloudfront.types.lambda_function_arn


class LambdaFunctionAssociation(TypedDict, closed=True):
    lambda_function_arn: "capo_cloudfront.types.lambda_function_arn.LambdaFunctionARN"
    """<p>The ARN of the Lambda@Edge function. You must specify the ARN of a function version; you can't specify an alias or $LATEST.</p>"""
    event_type: "capo_cloudfront.types.event_type.EventType"
    """<p>Specifies the event type that triggers a Lambda@Edge function invocation. You can specify the following values:</p> <ul> <li> <p> <code>viewer-request</code>: The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.</p> </li> <li> <p> <code>origin-request</code>: The function executes only when CloudFront sends a request to your origin. When the requested object is in the edge cache, the function doesn't execute.</p> </li> <li> <p> <code>origin-response</code>: The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn't execute.</p> </li> <li> <p> <code>viewer-response</code>: The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache.</p> <p>If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn't execute.</p> </li> </ul>"""
    include_body: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>A flag that allows a Lambda@Edge function to have read access to the body content. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-include-body-access.html">Accessing the Request Body by Choosing the Include Body Option</a> in the Amazon CloudFront Developer Guide.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: LambdaFunctionAssociation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "LambdaFunctionARN").text = str(value["lambda_function_arn"])
    import capo_cloudfront.types.event_type

    capo_cloudfront.types.event_type.serialize_xml(value["event_type"], el, "EventType")
    if "include_body" in value:
        SubElement(el, "IncludeBody").text = (
            "true" if value["include_body"] else "false"
        )


def deserialize_xml(el: Element) -> LambdaFunctionAssociation:
    out: LambdaFunctionAssociation = {}  # type: ignore[typeddict-item]
    child_lambda_function_arn = el.find("LambdaFunctionARN")
    if child_lambda_function_arn is not None:
        out["lambda_function_arn"] = str(child_lambda_function_arn.text or "")
    else:
        raise DeserializationError(
            "LambdaFunctionAssociation.lambda_function_arn required"
        )
    child_event_type = el.find("EventType")
    if child_event_type is not None:
        import capo_cloudfront.types.event_type

        out["event_type"] = capo_cloudfront.types.event_type.deserialize_xml(
            child_event_type
        )
    else:
        raise DeserializationError("LambdaFunctionAssociation.event_type required")
    child_include_body = el.find("IncludeBody")
    if child_include_body is not None:
        out["include_body"] = (child_include_body.text or "").lower() == "true"
    return out
