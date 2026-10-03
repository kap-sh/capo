"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceRevisionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.string_list


class DescribeServiceRevisionsRequest(TypedDict, closed=True):
    service_revision_arns: "capo_ecs.types.string_list.StringList"
    """<p>The ARN of the service revision. </p> <p>You can specify a maximum of 20 ARNs.</p> <p>You can call <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html">ListServiceDeployments</a> to get the ARNs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceRevisionsRequest) -> dict:
    out: dict = {}
    import capo_ecs.types.string_list

    out["serviceRevisionArns"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
        value["service_revision_arns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceRevisionsRequest:
    out: DescribeServiceRevisionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceRevisionArns") is not None:
        import capo_ecs.types.string_list

        out["service_revision_arns"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["serviceRevisionArns"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeServiceRevisionsRequest.service_revision_arns required"
        )
    return out
