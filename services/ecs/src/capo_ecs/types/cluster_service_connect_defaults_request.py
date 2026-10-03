"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterServiceConnectDefaultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.string


class ClusterServiceConnectDefaultsRequest(TypedDict, closed=True):
    namespace: "capo_ecs.types.string.String"
    """<p>The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace that's used when you create a service and don't specify a Service Connect configuration. The namespace name can include up to 1024 characters. The name is case-sensitive. The name can't include greater than (&gt;), less than (&lt;), double quotation marks ("), or slash (/).</p> <p>If you enter an existing namespace name or ARN, then that namespace will be used. Any namespace type is supported. The namespace must be in this account and this Amazon Web Services Region.</p> <p>If you enter a new name, a Cloud Map namespace will be created. Amazon ECS creates a Cloud Map namespace with the "API calls" method of instance discovery only. This instance discovery method is the "HTTP" namespace type in the Command Line Interface. Other types of instance discovery aren't used by Service Connect.</p> <p>If you update the cluster with an empty string <code>""</code> for the namespace name, the cluster configuration for Service Connect is removed. Note that the namespace will remain in Cloud Map and must be deleted separately.</p> <p>For more information about Cloud Map, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html">Working with Services</a> in the <i>Cloud Map Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterServiceConnectDefaultsRequest) -> dict:
    out: dict = {}
    out["namespace"] = value["namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterServiceConnectDefaultsRequest:
    out: ClusterServiceConnectDefaultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError(
            "ClusterServiceConnectDefaultsRequest.namespace required"
        )
    return out
