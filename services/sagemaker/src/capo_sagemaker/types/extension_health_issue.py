"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionHealthIssue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_health_issue_code
    import capo_sagemaker.types.extension_health_issue_message
    import capo_sagemaker.types.extension_node_count


class ExtensionHealthIssue(TypedDict, closed=True):
    code: NotRequired[
        "capo_sagemaker.types.extension_health_issue_code.ExtensionHealthIssueCode"
    ]
    """<p>A code that describes the type of issue.</p>"""
    message: NotRequired[
        "capo_sagemaker.types.extension_health_issue_message.ExtensionHealthIssueMessage"
    ]
    """<p>A description of the problem, for example the setting or component to check. Every node with the same problem has the same message.</p>"""
    node_count: NotRequired[
        "capo_sagemaker.types.extension_node_count.ExtensionNodeCount"
    ]
    """<p>The number of nodes that have this problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionHealthIssue) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_sagemaker.types.extension_health_issue_code

        out["Code"] = (
            capo_sagemaker.types.extension_health_issue_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "node_count" in value:
        out["NodeCount"] = value["node_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtensionHealthIssue:
    out: ExtensionHealthIssue = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_sagemaker.types.extension_health_issue_code

        out["code"] = (
            capo_sagemaker.types.extension_health_issue_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("NodeCount") is not None:
        out["node_count"] = data["NodeCount"]
    return out
