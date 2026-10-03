"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#StartResourceScanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.resource_arn


class StartResourceScanRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to use to scan the policies applied to the specified resource.</p>"""
    resource_arn: "capo_accessanalyzer.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource to scan.</p>"""
    resource_owner_account: NotRequired["str"]
    """<p>The Amazon Web Services account ID that owns the resource. For most Amazon Web Services resources, the owning account is the account in which the resource was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartResourceScanRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    out["resourceArn"] = value["resource_arn"]
    if "resource_owner_account" in value:
        out["resourceOwnerAccount"] = value["resource_owner_account"]
    return out


def deserialize_json(data: dict) -> StartResourceScanRequest:
    out: StartResourceScanRequest = {}  # type: ignore[typeddict-item]
    if data.get("analyzerArn") is not None:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError("StartResourceScanRequest.analyzer_arn required")
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("StartResourceScanRequest.resource_arn required")
    if data.get("resourceOwnerAccount") is not None:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    return out
