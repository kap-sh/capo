"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CreateAccessPreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.configurations_map


class CreateAccessPreviewRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the account analyzer</a> used to generate the access preview. You can only create an access preview for analyzers with an <code>Account</code> type and <code>Active</code> status.</p>"""
    configurations: "capo_accessanalyzer.types.configurations_map.ConfigurationsMap"
    """<p>Access control configuration for your resource that is used to generate the access preview. The access preview includes findings for external access allowed to the resource with the proposed access control configuration. The configuration must contain exactly one element.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessPreviewRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    import capo_accessanalyzer.types.configurations_map

    out["configurations"] = capo_accessanalyzer.types.configurations_map.serialize_json(
        value["configurations"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAccessPreviewRequest:
    out: CreateAccessPreviewRequest = {}  # type: ignore[typeddict-item]
    if data.get("analyzerArn") is not None:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError("CreateAccessPreviewRequest.analyzer_arn required")
    if data.get("configurations") is not None:
        import capo_accessanalyzer.types.configurations_map

        out["configurations"] = (
            capo_accessanalyzer.types.configurations_map.deserialize_json(
                data["configurations"]
            )
        )
    else:
        raise DeserializationError("CreateAccessPreviewRequest.configurations required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
