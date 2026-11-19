"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_health_issues


class ExtensionHealth(TypedDict, closed=True):
    issues: NotRequired[
        "capo_sagemaker.types.extension_health_issues.ExtensionHealthIssues"
    ]
    """<p>The problems that affect the extension, grouped by cause, from the problem that affects the most nodes to the one that affects the fewest. SageMaker HyperPod counts each node in at most one issue. The list contains at most 20 issues. If more than 20 different problems exist, the list shows the 19 that affect the most nodes, and the 20th issue has the code <code>Other</code> and counts the nodes that the remaining problems affect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionHealth) -> dict:
    out: dict = {}
    if "issues" in value:
        import capo_sagemaker.types.extension_health_issues

        out["Issues"] = (
            capo_sagemaker.types.extension_health_issues.serialize_aws_json_1_1(
                value["issues"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtensionHealth:
    out: ExtensionHealth = {}  # type: ignore[typeddict-item]
    if data.get("Issues") is not None:
        import capo_sagemaker.types.extension_health_issues

        out["issues"] = (
            capo_sagemaker.types.extension_health_issues.deserialize_aws_json_1_1(
                data["Issues"]
            )
        )
    return out
